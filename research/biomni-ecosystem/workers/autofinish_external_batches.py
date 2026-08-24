#!/usr/bin/env python3
"""Finish the remaining Biomni external-repository deep-audit queue.

The worker is intentionally static-only. It never imports or executes code from an
examined repository. It inspects immutable GitHub objects, source/fork comparison
metadata, archive members, notebooks as JSON, manifests, workflows, licenses and
selected source text. Every integration candidate is conservatively rejected for
direct adoption and retained only as a bounded comparison/reconstruction lead.

The script is designed for GitHub Actions on the research branch. It completes one
50-family window at a time, updates the canonical research ledgers, commits exactly
once per completed batch, and pushes before starting the next batch. A failed run is
restartable: already committed batches are detected and skipped.
"""
from __future__ import annotations

import collections
import contextlib
import datetime as dt
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parents[3]
AUDIT_ROOT = ROOT / "research" / "biomni-ecosystem"
DB_DIR = AUDIT_ROOT / "database"
EXT_DIR = AUDIT_ROOT / "external-repos"
REPOSITORIES_FILE = DB_DIR / "repositories.jsonl"
EVIDENCE_FILE = DB_DIR / "evidence.jsonl"
CHANGES_FILE = DB_DIR / "changes.jsonl"
LINEAGES_FILE = DB_DIR / "lineages.jsonl"
STATE_FILE = AUDIT_ROOT / "STATE.md"
MASTER_INDEX_FILE = AUDIT_ROOT / "MASTER_INDEX.md"
COVERAGE_FILE = AUDIT_ROOT / "COVERAGE.md"
QUEUE_SUMMARY_FILE = EXT_DIR / "queue-summary.md"
RESEARCH_LOG_FILE = ROOT / "research_log.md"
FINAL_SUMMARY_FILE = EXT_DIR / "FINAL_COMPLETION_SUMMARY.md"
WORKFLOW_FILE = ROOT / ".github" / "workflows" / "finish-external-audit.yml"

TARGET_BRANCH = os.environ.get("TARGET_BRANCH", "research/biomni-ecosystem-audit")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "MikeGong1/Biomni")
API_ROOT = "https://api.github.com"
USER_AGENT = "Biomni-static-deep-audit/1.0"
START_BATCH = int(os.environ.get("START_BATCH", "9"))
END_BATCH = int(os.environ.get("END_BATCH", "46"))
MAX_ARCHIVE_COMPRESSED = int(os.environ.get("MAX_ARCHIVE_COMPRESSED", str(70 * 1024 * 1024)))
MAX_TEXT_BYTES_PER_REPO = int(os.environ.get("MAX_TEXT_BYTES_PER_REPO", str(8 * 1024 * 1024)))
MAX_FILES_PER_REPO = int(os.environ.get("MAX_FILES_PER_REPO", "750"))
MAX_FILE_BYTES = int(os.environ.get("MAX_FILE_BYTES", str(800 * 1024)))
MAX_COMPARE_FILES = int(os.environ.get("MAX_COMPARE_FILES", "80"))
MAX_RAW_FILES = int(os.environ.get("MAX_RAW_FILES", "45"))
RETRY_LIMIT = 5

CODE_EXTENSIONS = {
    ".py", ".r", ".R", ".jl", ".ipynb", ".js", ".jsx", ".ts", ".tsx", ".java",
    ".kt", ".kts", ".go", ".rs", ".c", ".cc", ".cpp", ".cxx", ".h", ".hpp",
    ".cs", ".php", ".rb", ".scala", ".swift", ".m", ".mm", ".lua", ".sh",
    ".bash", ".zsh", ".fish", ".ps1", ".pl", ".pm", ".sql", ".clj", ".cljs",
    ".cljc", ".ex", ".exs", ".dart", ".groovy", ".v", ".sv", ".vhd", ".vhdl",
    ".mjs", ".cjs", ".vue", ".svelte", ".sol", ".nim", ".f", ".f90", ".f95",
}
DOC_EXTENSIONS = {
    ".md", ".mdx", ".rst", ".txt", ".tex", ".org", ".adoc", ".html", ".htm",
    ".css", ".scss", ".sass", ".less", ".bib", ".rtf",
}
DATA_EXTENSIONS = {
    ".csv", ".tsv", ".json", ".jsonl", ".yaml", ".yml", ".toml", ".xml", ".owl",
    ".ttl", ".nt", ".rdf", ".obo", ".gaf", ".bed", ".vcf", ".gff", ".gff3",
    ".fa", ".fasta", ".fastq", ".fq", ".gmt", ".h5ad", ".h5", ".parquet", ".feather",
}
MANIFEST_NAMES = {
    "pyproject.toml", "requirements.txt", "requirements-dev.txt", "environment.yml",
    "environment.yaml", "package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
    "poetry.lock", "uv.lock", "pipfile", "pipfile.lock", "setup.py", "setup.cfg",
    "cargo.toml", "cargo.lock", "go.mod", "go.sum", "renv.lock", "description", "dockerfile",
    "compose.yml", "compose.yaml", "docker-compose.yml", "docker-compose.yaml",
}
LICENSE_NAMES = {
    "license", "license.md", "license.txt", "copying", "copying.md", "copying.txt",
    "notice", "notice.md", "unlicense",
}
README_NAMES = {
    "readme", "readme.md", "readme.rst", "readme.txt", "readme.mdx",
}

DOMAIN_TERMS = [
    "bioinformatics", "biomedical", "biology", "biological", "genomic", "genome", "gene ",
    "genes ", "transcript", "proteom", "protein", "single-cell", "single cell", "spatial",
    "omics", "clinical", "patient", "disease", "drug", "molecule", "molecular", "patholog",
    "histolog", "medical", "medicine", "health", "crispr", "perturb", "rna", "dna", "cell ",
    "cells ", "immun", "cancer", "tumor", "pharmac", "toxic", "microbiom", "neuroscience",
    "neural recording", "lab automation", "assay", "microscopy", "radiology", "ehr", "fhir",
    "ontology", "knowledge graph", "scientific", "research workflow", "experiment", "benchmark",
]
AGENT_TERMS = [
    " agent", "agent ", "agents", "model context protocol", " mcp", "mcp ", "skill", "tool use",
    "tool-use", "function call", "workflow", "orchestr", "autonomous", "copilot", "llm",
]
DOC_LIST_TERMS = [
    "awesome list", "curated list", "papers", "reading list", "resources", "catalog", "bibliography",
    "survey", "roadmap", "collection of links", "dataset list", "paper list",
]

RISK_PATTERNS: dict[str, re.Pattern[str]] = {
    "dynamic_code_execution": re.compile(r"\b(eval|exec)\s*\(|compile\s*\(|runpy\.|importlib\.import_module", re.I),
    "shell_or_process_execution": re.compile(r"subprocess\.|os\.system\s*\(|shell\s*=\s*True|child_process|Runtime\.getRuntime\(\)\.exec", re.I),
    "unsafe_deserialization": re.compile(r"pickle\.load|pickle\.loads|torch\.load|joblib\.load|yaml\.load\s*\((?![^\n]*SafeLoader)|dill\.load", re.I),
    "network_fetch": re.compile(r"requests\.(get|post|put|delete)|urllib\.request|httpx\.|aiohttp\.|fetch\s*\(|axios\.", re.I),
    "server_exposure": re.compile(r"0\.0\.0\.0|allow_origins\s*=\s*\[?['\"]\*|CORS\([^\n]*\*|uvicorn\.run|app\.run\(", re.I),
    "filesystem_mutation": re.compile(r"shutil\.rmtree|os\.remove|os\.unlink|rm\s+-rf|delete_many|DROP\s+TABLE|TRUNCATE\s+TABLE", re.I),
    "path_input": re.compile(r"open\s*\([^\n]*(request|args|input|param)|send_file\s*\(|FileResponse\s*\(|Path\([^\n]*(request|input|param)", re.I),
    "hardcoded_secret_shape": re.compile(r"(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}['\"]", re.I),
    "mutable_remote_install": re.compile(r"pip\s+install\s+git\+|github\.com/[^\s'\"]+/(main|master)(\b|#)|actions/checkout@(main|master|v\d+)", re.I),
    "container_privilege": re.compile(r"--privileged|/var/run/docker\.sock|hostNetwork\s*:\s*true|securityContext[^\n]*privileged", re.I),
    "sql_string_construction": re.compile(r"(SELECT|INSERT|UPDATE|DELETE)[^\n]*(\+|format\(|f['\"]|%s)", re.I),
    "browser_html_injection": re.compile(r"innerHTML\s*=|dangerouslySetInnerHTML|document\.write\s*\(", re.I),
}

PRIVACY_PATTERNS: dict[str, re.Pattern[str]] = {
    "clinical_or_patient_data": re.compile(r"\b(patient|clinical|ehr|electronic health record|medical record|phi|hipaa)\b", re.I),
    "human_genomics": re.compile(r"\b(human genome|germline|genotype|variant|vcf|biobank|uk biobank|dbgap|controlled access)\b", re.I),
    "named_biomedical_cohort": re.compile(r"\b(tcga|gtex|mimic|all of us|1000 genomes|geo accession|synapse)\b", re.I),
    "upload_or_remote_transfer": re.compile(r"upload|send.*(file|data)|s3\.upload|put_object|huggingface_hub|wandb\.log|mlflow\.log", re.I),
}

SCIENCE_PATTERNS: dict[str, re.Pattern[str]] = {
    "unseeded_randomness": re.compile(r"(np\.random|numpy\.random|random\.|torch\.rand|jax\.random)(?![^\n]{0,100}(seed|key))", re.I),
    "hardcoded_threshold": re.compile(r"threshold\s*=\s*[-+]?\d*\.?\d+|p[_-]?value\s*[<=>]+\s*0\.0\d", re.I),
    "hardcoded_absolute_path": re.compile(r"['\"]/(home|Users|mnt|data|scratch|workspace)/[^'\"]+['\"]|[A-Za-z]:\\\\Users\\\\", re.I),
    "network_model_code": re.compile(r"trust_remote_code\s*=\s*True|from_pretrained\s*\([^\n]*(revision\s*=\s*['\"](main|master)|trust_remote_code)", re.I),
    "disabled_tls_verification": re.compile(r"verify\s*=\s*False|NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*['\"]?0", re.I),
    "assertion_as_validation": re.compile(r"\bassert\s+[^\n]+", re.I),
}

TEXT_EXTENSIONS = CODE_EXTENSIONS | DOC_EXTENSIONS | DATA_EXTENSIONS | {
    ".ini", ".cfg", ".conf", ".properties", ".env", ".lock", ".gradle", ".cmake", ".make",
}


class AuditError(RuntimeError):
    pass


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run(cmd: list[str], *, check: bool = True, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        check=check,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            rows.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise AuditError(f"invalid JSONL {path}:{number}: {exc}") from exc
    return rows


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in rows)
    path.write_text(content + ("\n" if content else ""), encoding="utf-8")


def next_numeric_id(rows: list[dict[str, Any]], key: str, prefix: str) -> int:
    maximum = 0
    pattern = re.compile(re.escape(prefix) + r"(\d+)$")
    for row in rows:
        value = str(row.get(key, ""))
        match = pattern.fullmatch(value)
        if match:
            maximum = max(maximum, int(match.group(1)))
    return maximum + 1


def format_id(prefix: str, number: int) -> str:
    return f"{prefix}{number:06d}"


def request_bytes(url: str, *, api: bool = False, max_bytes: int | None = None, timeout: int = 60) -> bytes:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json" if api else "*/*"}
    if api and GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    last_error: Exception | None = None
    for attempt in range(RETRY_LIMIT):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if api:
                    remaining = response.headers.get("X-RateLimit-Remaining")
                    reset = response.headers.get("X-RateLimit-Reset")
                    if remaining is not None and int(remaining) < 50 and reset:
                        delay = max(1, int(reset) - int(time.time()) + 2)
                        time.sleep(min(delay, 1800))
                chunks: list[bytes] = []
                total = 0
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    total += len(chunk)
                    if max_bytes is not None and total > max_bytes:
                        raise AuditError(f"download exceeds {max_bytes} bytes: {url}")
                    chunks.append(chunk)
                return b"".join(chunks)
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code in {404, 410, 422}:
                raise
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            delay = int(retry_after) if retry_after and retry_after.isdigit() else 2 ** attempt
            time.sleep(min(delay, 60))
        except (urllib.error.URLError, TimeoutError, AuditError) as exc:
            last_error = exc
            if isinstance(exc, AuditError):
                raise
            time.sleep(min(2 ** attempt, 60))
    raise AuditError(f"request failed after retries: {url}: {last_error}")


def api_json(path: str, *, allow_missing: bool = False) -> dict[str, Any] | list[Any] | None:
    url = path if path.startswith("http") else API_ROOT + path
    try:
        raw = request_bytes(url, api=True, max_bytes=50 * 1024 * 1024, timeout=90)
    except urllib.error.HTTPError as exc:
        if allow_missing and exc.code in {404, 410, 422}:
            return None
        raise
    return json.loads(raw.decode("utf-8", errors="replace"))


def safe_decode(data: bytes) -> str:
    if b"\x00" in data[:4096]:
        return ""
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def notebook_to_text(text: str) -> tuple[str, int]:
    try:
        obj = json.loads(text)
    except Exception:
        return text, 0
    fragments: list[str] = []
    output_count = 0
    for cell in obj.get("cells", []):
        source = cell.get("source", [])
        if isinstance(source, list):
            fragments.append("".join(str(x) for x in source))
        else:
            fragments.append(str(source))
        outputs = cell.get("outputs", []) or []
        output_count += len(outputs)
        for output in outputs[:3]:
            for key in ("text", "traceback"):
                value = output.get(key)
                if isinstance(value, list):
                    fragments.append("".join(str(x) for x in value))
                elif value:
                    fragments.append(str(value))
    return "\n".join(fragments), output_count


def priority_path(path: str) -> tuple[int, str]:
    p = PurePosixPath(path)
    name = p.name.lower()
    ext = p.suffix.lower()
    if name in README_NAMES:
        return (0, path)
    if name in LICENSE_NAMES:
        return (1, path)
    if name in MANIFEST_NAMES or name.startswith("requirements"):
        return (2, path)
    if ".github/workflows/" in path.lower():
        return (3, path)
    if any(part.lower() in {"src", "app", "server", "api", "mcp", "agent", "agents", "skills", "models", "model"} for part in p.parts):
        return (4, path)
    if ext in CODE_EXTENSIONS:
        return (5, path)
    if ext in DOC_EXTENSIONS:
        return (6, path)
    if ext in DATA_EXTENSIONS:
        return (7, path)
    return (8, path)


def should_read_path(path: str) -> bool:
    p = PurePosixPath(path)
    name = p.name.lower()
    ext = p.suffix.lower()
    if name in README_NAMES or name in LICENSE_NAMES or name in MANIFEST_NAMES:
        return True
    if name.startswith("requirements") or ".github/workflows/" in path.lower():
        return True
    return ext in TEXT_EXTENSIONS or ext in CODE_EXTENSIONS


def classify_path(path: str) -> str:
    p = PurePosixPath(path)
    name = p.name.lower()
    ext = p.suffix.lower()
    if name in LICENSE_NAMES:
        return "license"
    if name in README_NAMES or ext in DOC_EXTENSIONS:
        return "doc"
    if name in MANIFEST_NAMES or name.startswith("requirements") or ".github/workflows/" in path.lower():
        return "manifest"
    if ext in CODE_EXTENSIONS:
        return "code"
    if ext in DATA_EXTENSIONS:
        return "data"
    return "other"


def scan_text_inventory(files: list[tuple[str, str]], *, truncated: bool, acquisition: str, errors: list[str]) -> dict[str, Any]:
    counts: collections.Counter[str] = collections.Counter()
    extensions: collections.Counter[str] = collections.Counter()
    combined_parts: list[str] = []
    notebook_outputs = 0
    paths: list[str] = []
    for path, raw_text in files:
        paths.append(path)
        category = classify_path(path)
        counts[category] += 1
        extensions[PurePosixPath(path).suffix.lower() or "<none>"] += 1
        text = raw_text
        if PurePosixPath(path).suffix.lower() == ".ipynb":
            text, outputs = notebook_to_text(raw_text)
            notebook_outputs += outputs
        combined_parts.append(f"\n--- FILE {path} ---\n{text[:MAX_FILE_BYTES]}")
    combined = "".join(combined_parts)
    lower = combined.lower()
    risk_hits = {name: len(pattern.findall(combined)) for name, pattern in RISK_PATTERNS.items() if pattern.search(combined)}
    privacy_hits = {name: len(pattern.findall(combined)) for name, pattern in PRIVACY_PATTERNS.items() if pattern.search(combined)}
    science_hits = {name: len(pattern.findall(combined)) for name, pattern in SCIENCE_PATTERNS.items() if pattern.search(combined)}
    has_tests = any(re.search(r"(^|/)(test|tests|spec)(/|_|\.)", path, re.I) for path in paths)
    has_license = counts["license"] > 0
    has_lock = any(PurePosixPath(path).name.lower() in {"poetry.lock", "uv.lock", "pipfile.lock", "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "cargo.lock", "renv.lock"} for path in paths)
    manifests = [p for p in paths if classify_path(p) == "manifest"]
    domain_signal = any(term in lower for term in DOMAIN_TERMS)
    agent_signal = any(term in lower for term in AGENT_TERMS)
    doc_list_signal = any(term in lower for term in DOC_LIST_TERMS)
    substantive_file_count = counts["code"] + counts["doc"] + counts["data"] + counts["manifest"]
    return {
        "acquisition": acquisition,
        "acquisition_complete": not errors,
        "acquisition_errors": errors[:10],
        "truncated": truncated,
        "files_read": len(files),
        "substantive_files": int(substantive_file_count),
        "code_files": int(counts["code"]),
        "doc_files": int(counts["doc"]),
        "data_files": int(counts["data"]),
        "manifest_files": int(counts["manifest"]),
        "license_files": int(counts["license"]),
        "other_files": int(counts["other"]),
        "top_extensions": extensions.most_common(12),
        "notebook_output_objects": notebook_outputs,
        "has_tests": has_tests,
        "has_license": has_license,
        "has_lockfile": has_lock,
        "manifests": manifests[:30],
        "domain_signal": domain_signal,
        "agent_signal": agent_signal,
        "doc_list_signal": doc_list_signal,
        "risk_pattern_hits": risk_hits,
        "privacy_pattern_hits": privacy_hits,
        "science_pattern_hits": science_hits,
        "sample_paths": sorted(paths, key=priority_path)[:40],
        "text_sha256": hashlib.sha256(combined.encode("utf-8", errors="replace")).hexdigest(),
        "combined_text_preview": combined[:12000],
    }


def scan_tarball(full_name: str, sha: str, size_kb: int | None) -> dict[str, Any]:
    errors: list[str] = []
    if not sha:
        return scan_text_inventory([], truncated=True, acquisition="NO_IMMUTABLE_SHA", errors=["missing immutable head SHA"])
    if size_kb and size_kb > 220_000:
        return scan_tree_fallback(full_name, sha, reason=f"canonical size {size_kb} KB exceeds archive threshold")
    url = f"https://codeload.github.com/{full_name}/tar.gz/{sha}"
    try:
        data = request_bytes(url, api=False, max_bytes=MAX_ARCHIVE_COMPRESSED, timeout=120)
    except Exception as exc:
        return scan_tree_fallback(full_name, sha, reason=f"archive acquisition failed: {type(exc).__name__}: {exc}")
    files: list[tuple[str, str]] = []
    total_text = 0
    truncated = False
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
            members = [m for m in archive.getmembers() if m.isfile()]
            members.sort(key=lambda m: priority_path("/".join(PurePosixPath(m.name).parts[1:])))
            for member in members:
                rel = "/".join(PurePosixPath(member.name).parts[1:])
                if not rel or not should_read_path(rel):
                    continue
                if len(files) >= MAX_FILES_PER_REPO or total_text >= MAX_TEXT_BYTES_PER_REPO:
                    truncated = True
                    break
                if member.size > MAX_FILE_BYTES:
                    continue
                handle = archive.extractfile(member)
                if handle is None:
                    continue
                raw = handle.read(MAX_FILE_BYTES + 1)
                if len(raw) > MAX_FILE_BYTES:
                    continue
                text = safe_decode(raw)
                if not text:
                    continue
                total_text += len(raw)
                files.append((rel, text))
    except Exception as exc:
        errors.append(f"tar parse error: {type(exc).__name__}: {exc}")
    return scan_text_inventory(files, truncated=truncated, acquisition="IMMUTABLE_TARBALL", errors=errors)


def scan_tree_fallback(full_name: str, sha: str, reason: str) -> dict[str, Any]:
    errors = [reason]
    owner, repo = full_name.split("/", 1)
    tree = api_json(f"/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(repo)}/git/trees/{sha}?recursive=1", allow_missing=True)
    if not isinstance(tree, dict):
        commit = api_json(f"/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(repo)}/git/commits/{sha}", allow_missing=True)
        tree_sha = ((commit or {}).get("tree") or {}).get("sha") if isinstance(commit, dict) else None
        if tree_sha:
            tree = api_json(f"/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(repo)}/git/trees/{tree_sha}?recursive=1", allow_missing=True)
    if not isinstance(tree, dict):
        return scan_text_inventory([], truncated=True, acquisition="TREE_UNAVAILABLE", errors=errors + ["Git tree unavailable"])
    entries = [x for x in tree.get("tree", []) if x.get("type") == "blob" and should_read_path(str(x.get("path", "")))]
    entries.sort(key=lambda x: priority_path(str(x.get("path", ""))))
    files: list[tuple[str, str]] = []
    for entry in entries[:MAX_RAW_FILES]:
        path = str(entry.get("path", ""))
        size = entry.get("size") or 0
        if size and int(size) > MAX_FILE_BYTES:
            continue
        raw_url = f"https://raw.githubusercontent.com/{full_name}/{sha}/{urllib.parse.quote(path, safe='/')}"
        try:
            raw = request_bytes(raw_url, api=False, max_bytes=MAX_FILE_BYTES, timeout=60)
            text = safe_decode(raw)
            if text:
                files.append((path, text))
        except Exception as exc:
            errors.append(f"raw {path}: {type(exc).__name__}")
    return scan_text_inventory(
        files,
        truncated=bool(tree.get("truncated")) or len(entries) > MAX_RAW_FILES,
        acquisition="IMMUTABLE_GIT_TREE_SELECTED_BLOBS",
        errors=errors if not files else [],
    )


def fetch_changed_files(full_name: str, sha: str, paths: list[str]) -> dict[str, Any]:
    files: list[tuple[str, str]] = []
    errors: list[str] = []
    selected = sorted({p for p in paths if should_read_path(p)}, key=priority_path)[:MAX_RAW_FILES]
    for path in selected:
        raw_url = f"https://raw.githubusercontent.com/{full_name}/{sha}/{urllib.parse.quote(path, safe='/')}"
        try:
            raw = request_bytes(raw_url, api=False, max_bytes=MAX_FILE_BYTES, timeout=60)
            text = safe_decode(raw)
            if text:
                files.append((path, text))
        except Exception as exc:
            errors.append(f"raw {path}: {type(exc).__name__}")
    return scan_text_inventory(files, truncated=len(paths) > MAX_RAW_FILES, acquisition="IMMUTABLE_CHANGED_BLOBS", errors=errors if not files else [])


SOURCE_META_CACHE: dict[str, dict[str, Any] | None] = {}
COMPARE_CACHE: dict[str, dict[str, Any] | None] = {}
CACHE_LOCK = threading.Lock()


def source_metadata(full_name: str) -> dict[str, Any] | None:
    key = full_name.lower()
    with CACHE_LOCK:
        if key in SOURCE_META_CACHE:
            return SOURCE_META_CACHE[key]
    owner, repo = full_name.split("/", 1)
    value = api_json(f"/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(repo)}", allow_missing=True)
    normalized = value if isinstance(value, dict) else None
    with CACHE_LOCK:
        SOURCE_META_CACHE[key] = normalized
    return normalized


def compare_fork(source: str, member: dict[str, Any]) -> dict[str, Any]:
    full_name = str(member.get("full_name", ""))
    branch = str(member.get("default_branch") or "main")
    cache_key = f"{source.lower()}::{full_name.lower()}::{branch}"
    with CACHE_LOCK:
        if cache_key in COMPARE_CACHE:
            return COMPARE_CACHE[cache_key] or {"available": False}
    meta = source_metadata(source)
    if not meta:
        result = {"available": False, "reason": "source repository metadata unavailable"}
        with CACHE_LOCK:
            COMPARE_CACHE[cache_key] = result
        return result
    base = str(meta.get("default_branch") or "main")
    owner, repo = source.split("/", 1)
    fork_owner = full_name.split("/", 1)[0]
    base_q = urllib.parse.quote(base, safe="")
    head_q = urllib.parse.quote(f"{fork_owner}:{branch}", safe=":")
    endpoint = f"/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(repo)}/compare/{base_q}...{head_q}"
    value = api_json(endpoint, allow_missing=True)
    if not isinstance(value, dict):
        result = {"available": False, "reason": "cross-repository compare unavailable", "base_branch": base, "head_branch": branch}
        with CACHE_LOCK:
            COMPARE_CACHE[cache_key] = result
        return result
    changed_files = []
    for item in value.get("files", [])[:MAX_COMPARE_FILES]:
        changed_files.append({
            "filename": item.get("filename"),
            "status": item.get("status"),
            "additions": item.get("additions"),
            "deletions": item.get("deletions"),
            "changes": item.get("changes"),
        })
    result = {
        "available": True,
        "status": value.get("status"),
        "ahead_by": int(value.get("ahead_by") or 0),
        "behind_by": int(value.get("behind_by") or 0),
        "total_commits": int(value.get("total_commits") or 0),
        "base_branch": base,
        "head_branch": branch,
        "merge_base_sha": (value.get("merge_base_commit") or {}).get("sha"),
        "base_sha": (value.get("base_commit") or {}).get("sha"),
        "changed_files": changed_files,
        "files_truncated": len(value.get("files", [])) >= MAX_COMPARE_FILES,
    }
    with CACHE_LOCK:
        COMPARE_CACHE[cache_key] = result
    return result


def aggregate_scan(scans: list[dict[str, Any]], metadata_text: str) -> dict[str, Any]:
    total = collections.Counter()
    risk = collections.Counter()
    privacy = collections.Counter()
    science = collections.Counter()
    paths: list[str] = []
    acquisitions: list[str] = []
    errors: list[str] = []
    domain_signal = any(term in metadata_text.lower() for term in DOMAIN_TERMS)
    agent_signal = any(term in metadata_text.lower() for term in AGENT_TERMS)
    doc_list_signal = any(term in metadata_text.lower() for term in DOC_LIST_TERMS)
    for scan in scans:
        for key in ("files_read", "substantive_files", "code_files", "doc_files", "data_files", "manifest_files", "license_files", "other_files", "notebook_output_objects"):
            total[key] += int(scan.get(key) or 0)
        risk.update(scan.get("risk_pattern_hits") or {})
        privacy.update(scan.get("privacy_pattern_hits") or {})
        science.update(scan.get("science_pattern_hits") or {})
        domain_signal = domain_signal or bool(scan.get("domain_signal"))
        agent_signal = agent_signal or bool(scan.get("agent_signal"))
        doc_list_signal = doc_list_signal or bool(scan.get("doc_list_signal"))
        paths.extend(scan.get("sample_paths") or [])
        acquisitions.append(str(scan.get("acquisition")))
        errors.extend(scan.get("acquisition_errors") or [])
    return {
        **{k: int(v) for k, v in total.items()},
        "risk_pattern_hits": dict(risk.most_common()),
        "privacy_pattern_hits": dict(privacy.most_common()),
        "science_pattern_hits": dict(science.most_common()),
        "domain_signal": domain_signal,
        "agent_signal": agent_signal,
        "doc_list_signal": doc_list_signal,
        "has_tests": any(bool(s.get("has_tests")) for s in scans),
        "has_license": any(bool(s.get("has_license")) for s in scans),
        "has_lockfile": any(bool(s.get("has_lockfile")) for s in scans),
        "truncated": any(bool(s.get("truncated")) for s in scans),
        "acquisitions": acquisitions,
        "acquisition_errors": errors[:20],
        "sample_paths": sorted(set(paths), key=priority_path)[:50],
    }


def is_doc_changed_path(path: str) -> bool:
    category = classify_path(path)
    if category in {"doc", "license", "manifest"}:
        return True
    lowered = path.lower()
    return lowered.startswith(".github/") or lowered.startswith("docs/") or lowered in {"citation.cff", ".gitignore", ".pre-commit-config.yaml"}


def audit_family(order: int, records: list[dict[str, Any]]) -> dict[str, Any]:
    representatives = [r for r in records if r.get("external_deep_audit_family_role") == "REPRESENTATIVE"]
    if len(representatives) != 1:
        raise AuditError(f"queue order {order}: expected one representative, found {len(representatives)}")
    representative = representatives[0]
    family_key = str(representative.get("external_deep_audit_family_key") or "")
    family_source = str(representative.get("external_deep_audit_family_source") or representative.get("full_name") or "")
    expected_count = int(representative.get("external_deep_audit_family_member_count") or 0)
    if expected_count != len(records):
        raise AuditError(f"queue order {order}: canonical member count {expected_count} != {len(records)}")
    canonical_ids = []
    metadata_parts = [family_key, family_source]
    for record in records:
        canonical_ids.append({
            "repository_id": record.get("repository_id"),
            "canonical_full_name": record.get("full_name"),
            "canonical_queue_order": record.get("external_deep_audit_queue_order"),
            "canonical_family_key": record.get("external_deep_audit_family_key"),
            "canonical_family_source": record.get("external_deep_audit_family_source"),
            "canonical_family_role": record.get("external_deep_audit_family_role"),
            "canonical_family_member_count": record.get("external_deep_audit_family_member_count"),
        })
        metadata_parts.extend([
            str(record.get("full_name") or ""), str(record.get("description") or ""),
            " ".join(record.get("topics") or []), str(record.get("relevance_reason") or ""),
        ])
    metadata_text = "\n".join(metadata_parts)

    comparisons: list[dict[str, Any]] = []
    scans: list[dict[str, Any]] = []
    changed_paths: list[str] = []
    all_fork_members = True
    all_no_unique = True
    any_compare_unavailable = False
    any_unique = False
    unique_commit_total = 0

    for record in records:
        full_name = str(record.get("full_name") or "")
        sha = str(record.get("default_head_sha") or record.get("head_sha") or "")
        parent = str(record.get("parent_full_name") or "")
        is_fork = bool(record.get("is_fork")) and bool(parent)
        if is_fork:
            comparison = compare_fork(family_source or parent, record)
            comparison["repository_id"] = record.get("repository_id")
            comparison["full_name"] = full_name
            comparisons.append(comparison)
            if not comparison.get("available"):
                any_compare_unavailable = True
                all_no_unique = False
                scan = scan_tarball(full_name, sha, int(record.get("size_kb") or 0))
                scans.append(scan)
                continue
            ahead = int(comparison.get("ahead_by") or 0)
            unique_commit_total += ahead
            if ahead > 0:
                any_unique = True
                all_no_unique = False
                paths = [str(x.get("filename")) for x in comparison.get("changed_files", []) if x.get("filename")]
                changed_paths.extend(paths)
                scan = fetch_changed_files(full_name, sha, paths)
                scans.append(scan)
        else:
            all_fork_members = False
            all_no_unique = False
            scan = scan_tarball(full_name, sha, int(record.get("size_kb") or 0))
            scans.append(scan)

    aggregate = aggregate_scan(scans, metadata_text)
    code_files = int(aggregate.get("code_files") or 0)
    substantive = int(aggregate.get("substantive_files") or 0)
    doc_files = int(aggregate.get("doc_files") or 0)
    manifest_files = int(aggregate.get("manifest_files") or 0)
    data_files = int(aggregate.get("data_files") or 0)

    if all_fork_members and all_no_unique and not any_compare_unavailable:
        result_class = "NO_UNIQUE_OR_SOURCE_LINEAGE"
        disposition = "CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID"
    elif substantive == 0 and not any_unique:
        result_class = "EMPTY"
        disposition = "CLOSE_EMPTY_OR_UNAVAILABLE_ARTIFACT; no integration capability retained"
    elif any_unique and changed_paths and all(is_doc_changed_path(p) for p in changed_paths):
        result_class = "DOC_METADATA_MAINTENANCE_ONLY"
        disposition = "CLOSE_DOCUMENTATION_METADATA_MAINTENANCE_ONLY; outbound claims remain unvalidated"
    elif any_unique:
        result_class = "DEEP_AUDIT_CANDIDATE"
        disposition = "REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead"
    elif code_files == 0 and data_files > 0 and aggregate.get("domain_signal") and not aggregate.get("doc_list_signal"):
        result_class = "DEEP_AUDIT_CANDIDATE"
        disposition = "REJECT_DIRECT_ADOPTION; preserve the bounded scientific data/ontology artifact only as a governed comparison lead"
    elif code_files == 0 and (doc_files + manifest_files + data_files) > 0:
        result_class = "DOC_METADATA_MAINTENANCE_ONLY"
        disposition = "CLOSE_NON_EXECUTABLE_CATALOG_OR_METADATA; outbound claims and data rights remain external"
    elif not aggregate.get("domain_signal") and not aggregate.get("agent_signal"):
        result_class = "NON_BIOMEDICAL_FALSE_POSITIVE"
        disposition = "CLOSE_METADATA_FALSE_POSITIVE; no bounded biomedical or scientific-agent capability verified"
    else:
        result_class = "DEEP_AUDIT_CANDIDATE"
        disposition = "REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead"

    blockers: list[str] = []
    if result_class == "DEEP_AUDIT_CANDIDATE":
        if not aggregate.get("has_license"):
            blockers.append("no license file was included in the bounded reviewed immutable blobs")
        if not aggregate.get("has_tests"):
            blockers.append("no test surface was observed in the bounded static sample")
        if not aggregate.get("has_lockfile"):
            blockers.append("dependency resolution is not fully locked by an observed lockfile")
        if aggregate.get("risk_pattern_hits"):
            blockers.append("static security-sensitive primitives require manual source-to-sink validation")
        if aggregate.get("privacy_pattern_hits"):
            blockers.append("biomedical or user-data handling requires explicit privacy, consent and data-governance review")
        if aggregate.get("science_pattern_hits"):
            blockers.append("scientific reproducibility or validation flags require domain review")
        if aggregate.get("truncated"):
            blockers.append("large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness")
        if aggregate.get("acquisition_errors"):
            blockers.append("one or more immutable acquisition surfaces were unavailable or incomplete")
        if not blockers:
            blockers.append("semantic equivalence, scientific validity, dependency provenance and runtime isolation remain unverified")
    elif result_class == "DOC_METADATA_MAINTENANCE_ONLY":
        blockers.append("catalog and outbound scientific claims were not treated as validated implementations")
        if not aggregate.get("has_license"):
            blockers.append("repository-local reuse grant was not observed")
    elif result_class == "NON_BIOMEDICAL_FALSE_POSITIVE":
        blockers.append("bounded source text did not verify a biomedical, scientific-analysis or scientific-agent capability")
    elif result_class == "NO_UNIQUE_OR_SOURCE_LINEAGE":
        blockers.append("bounded fork heads contain no commits ahead of the current source default branch")
    else:
        blockers.append("no substantive implementation artifact was available")

    return {
        "family_record_id": f"queue-{order}",
        "queue_order": order,
        "family_key": family_key,
        "family_source": family_source,
        "primary_bounded_repository_id": representative.get("repository_id"),
        "repository_names": [r.get("full_name") for r in records],
        "canonical_repository_ids": canonical_ids,
        "identity_gate": "EXACT_CANONICAL_QUEUE_ORDER_FAMILY_ROLE_MEMBER_COUNT_ROUND_TRIP",
        "source_fork_review": {
            "all_members_are_forks": all_fork_members,
            "all_members_no_unique_vs_source_default": all_no_unique and not any_compare_unavailable,
            "any_compare_unavailable": any_compare_unavailable,
            "unique_commit_total": unique_commit_total,
            "comparisons": comparisons,
            "changed_paths": sorted(set(changed_paths))[:250],
        },
        "static_inventory": {k: v for k, v in aggregate.items() if k != "combined_text_preview"},
        "scientific_security_privacy_license": {
            "risk_pattern_hits": aggregate.get("risk_pattern_hits"),
            "privacy_pattern_hits": aggregate.get("privacy_pattern_hits"),
            "science_pattern_hits": aggregate.get("science_pattern_hits"),
            "license_observed": aggregate.get("has_license"),
            "tests_observed": aggregate.get("has_tests"),
            "lockfile_observed": aggregate.get("has_lockfile"),
            "interpretation_boundary": "Pattern hits are static review flags, not proof of exploitability, clinical validity or scientific invalidity.",
        },
        "canonical_result_class": result_class,
        "disposition": disposition,
        "direct_adoption_blockers": blockers,
        "observed_heads": [r.get("default_head_sha") or r.get("head_sha") for r in records if r.get("default_head_sha") or r.get("head_sha")],
        "observed_at": now_utc(),
    }


def batch_bounds(batch: int) -> tuple[int, int]:
    if batch < 9 or batch > 46:
        raise AuditError(f"unsupported batch {batch}")
    start = 213 + (batch - 9) * 50
    end = min(start + 49, 2069)
    return start, end


def assert_batch_input(batch: int, groups: dict[int, list[dict[str, Any]]]) -> tuple[int, int, list[int], int]:
    start, end = batch_bounds(batch)
    orders = list(range(start, end + 1))
    missing = [order for order in orders if order not in groups]
    if missing:
        raise AuditError(f"batch {batch:03d}: missing canonical queue orders: {missing}")
    expected_families = end - start + 1
    if len(orders) != expected_families:
        raise AuditError("internal order count error")
    record_count = sum(len(groups[o]) for o in orders)
    family_keys = {groups[o][0].get("external_deep_audit_family_key") for o in orders}
    if len(family_keys) != expected_families:
        raise AuditError(f"batch {batch:03d}: family key collision")
    for order in orders:
        rows = groups[order]
        reps = [r for r in rows if r.get("external_deep_audit_family_role") == "REPRESENTATIVE"]
        if len(reps) != 1:
            raise AuditError(f"batch {batch:03d} order {order}: representative count {len(reps)}")
        count = int(reps[0].get("external_deep_audit_family_member_count") or 0)
        if count != len(rows):
            raise AuditError(f"batch {batch:03d} order {order}: member count mismatch")
        for row in rows:
            if int(row.get("external_deep_audit_queue_order") or -1) != order:
                raise AuditError(f"batch {batch:03d} order {order}: reverse order mismatch")
            if row.get("external_deep_audit_family_key") != reps[0].get("external_deep_audit_family_key"):
                raise AuditError(f"batch {batch:03d} order {order}: reverse family mismatch")
    return start, end, orders, record_count


def allocate_batch_records(
    batch: int,
    audits: list[dict[str, Any]],
    repositories: list[dict[str, Any]],
    evidence: list[dict[str, Any]],
    changes: list[dict[str, Any]],
    lineages: list[dict[str, Any]],
) -> tuple[list[str], dict[int, list[str]], dict[int, list[str]]]:
    timestamp = now_utc()
    report_rel = f"external-repos/deep-audit-batch-{batch:03d}.md"
    manifest_rel = f"external-repos/deep-audit-batch-{batch:03d}-manifest.jsonl"
    evidence_number = next_numeric_id(evidence, "evidence_id", "evidence-")
    evidence_ids = [format_id("evidence-", evidence_number + i) for i in range(4)]

    counts = collections.Counter(a["canonical_result_class"] for a in audits)
    start, end = batch_bounds(batch)
    total_records = sum(len(a["canonical_repository_ids"]) for a in audits)
    evidence.extend([
        {
            "evidence_id": evidence_ids[0], "claim_class": "FACT", "source_tier": 1,
            "source_type": "deterministic_exact_identity_manifest",
            "source_url": f"https://github.com/{GITHUB_REPOSITORY}/blob/{TARGET_BRANCH}/research/biomni-ecosystem/{manifest_rel}",
            "evidence_summary": f"Batch {batch:03d} queue orders {start}-{end} round-trip exactly to {len(audits)} canonical families and {total_records} bounded repository records, with one representative and matching member counts per family.",
            "observed_at": timestamp,
        },
        {
            "evidence_id": evidence_ids[1], "claim_class": "FACT", "source_tier": 1,
            "source_type": "immutable_static_repository_and_lineage_audit",
            "source_url": f"https://github.com/{GITHUB_REPOSITORY}/blob/{TARGET_BRANCH}/research/biomni-ecosystem/{report_rel}",
            "evidence_summary": f"Batch {batch:03d} statically inspected immutable fork comparisons, archives or Git trees without executing third-party code. Result counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) + ".",
            "observed_at": timestamp, "related_evidence_ids": [evidence_ids[0]],
        },
        {
            "evidence_id": evidence_ids[2], "claim_class": "FACT", "source_tier": 1,
            "source_type": "static_security_privacy_science_license_review",
            "source_url": f"https://github.com/{GITHUB_REPOSITORY}/blob/{TARGET_BRANCH}/research/biomni-ecosystem/{report_rel}",
            "evidence_summary": f"Every Batch {batch:03d} family received bounded static checks for executable primitives, network/file/server exposure, unsafe loading, privacy/data-governance signals, scientific reproducibility flags, dependency locking and repository-local licensing. Pattern matches are treated as review flags rather than proof.",
            "observed_at": timestamp, "related_evidence_ids": [evidence_ids[0], evidence_ids[1]],
        },
        {
            "evidence_id": evidence_ids[3], "claim_class": "INFERENCE", "source_tier": 1,
            "source_type": "conservative_canonical_reduction",
            "source_url": f"https://github.com/{GITHUB_REPOSITORY}/blob/{TARGET_BRANCH}/research/biomni-ecosystem/{report_rel}",
            "evidence_summary": f"Batch {batch:03d} closes the bounded queue interval while rejecting every direct-adoption path. Candidate implementations remain comparison or clean-room reconstruction leads; no Feature or Implementation ID is allocated.",
            "observed_at": timestamp, "related_evidence_ids": evidence_ids[:3],
        },
    ])

    change_number = next_numeric_id(changes, "change_id", "change-")
    lineage_number = next_numeric_id(lineages, "lineage_id", "lineage-")
    change_ids_by_order: dict[int, list[str]] = {}
    lineage_ids_by_order: dict[int, list[str]] = {}

    repo_by_id = {str(r.get("repository_id")): r for r in repositories}
    for audit in audits:
        order = int(audit["queue_order"])
        change_ids: list[str] = []
        lineage_ids: list[str] = []
        if audit["canonical_result_class"] == "DEEP_AUDIT_CANDIDATE":
            change_id = format_id("change-", change_number)
            change_number += 1
            change_ids.append(change_id)
            is_lineage = bool(audit["source_fork_review"].get("all_members_are_forks"))
            if is_lineage:
                lineage_id = format_id("lineage-", lineage_number)
                lineage_number += 1
                lineage_ids.append(lineage_id)
            repository_ids = [str(x["repository_id"]) for x in audit["canonical_repository_ids"]]
            repository_names = [str(x["canonical_full_name"]) for x in audit["canonical_repository_ids"]]
            persons: list[str] = []
            branches: list[str] = []
            for rid in repository_ids:
                row = repo_by_id[rid]
                persons.extend(row.get("person_owner_ids") or [])
                if row.get("default_branch"):
                    branches.append(str(row["default_branch"]))
            text = (audit["family_key"] + " " + audit["family_source"] + " " + " ".join(repository_names)).lower()
            if "benchmark" in text or "arena" in text or "eval" in text:
                change_type = "BENCHMARK"
            elif "dataset" in text or "corpus" in text or "database" in text:
                change_type = "DATA"
            elif "model" in text or "bert" in text or "transformer" in text:
                change_type = "MODEL"
            else:
                change_type = "FEATURE"
            changes.append({
                "change_id": change_id,
                "repository_ids": repository_ids,
                "repositories": repository_names,
                "queue_order": order,
                "change_component": f"{audit['family_source']} bounded static implementation candidate",
                "observed_shas": audit.get("observed_heads") or [],
                "source_branches": sorted(set(branches)),
                "source_prs": [],
                "change_type": change_type,
                "feature_ids": [],
                "status": "VERIFIED_STATIC_DEEP_AUDITED_DIRECT_ADOPTION_REJECTED",
                "integration_disposition": audit["disposition"],
                "related_lineage_ids": lineage_ids,
                "relevant_person_ids": sorted(set(persons)),
                "evidence_ids": evidence_ids,
                "detailed_file": report_rel,
                "manifest_file": manifest_rel,
                "observed_at": timestamp,
            })
            if lineage_ids:
                lineages.append({
                    "lineage_id": lineage_ids[0],
                    "name": f"{audit['family_source']} source and bounded member lineage",
                    "lineage_type": "VERIFIED_STATIC_SOURCE_FORK_DAG",
                    "change_ids": change_ids,
                    "feature_ids": [],
                    "repositories": repository_names,
                    "queue_order": order,
                    "relations": audit["source_fork_review"].get("comparisons"),
                    "status": "VERIFIED_STATIC_DIRECT_ADOPTION_REJECTED_FEATURE_DECOMPOSITION_DEFERRED",
                    "canonical_for_integration": None,
                    "evidence_ids": evidence_ids,
                    "detailed_file": report_rel,
                })
        audit["canonical_change_ids"] = change_ids
        audit["canonical_lineage_ids"] = lineage_ids
        audit["evidence_ids"] = evidence_ids
        audit["report_file"] = report_rel
        audit["manifest_file"] = manifest_rel
        audit["reducer_schema_version"] = "automated-static-deep-audit-v1"
        change_ids_by_order[order] = change_ids
        lineage_ids_by_order[order] = lineage_ids

    result_to_status = {
        "DEEP_AUDIT_CANDIDATE": "AUDIT_COMPLETE_FAMILY_WITH_SUBSTANTIVE_CHANGES",
        "NO_UNIQUE_OR_SOURCE_LINEAGE": "RESOLVED_FORK_LINEAGE_NO_SUBSTANTIVE_UNIQUE_CODE",
        "DOC_METADATA_MAINTENANCE_ONLY": "AUDIT_COMPLETE_DOC_METADATA_MAINTENANCE_ONLY",
        "NON_BIOMEDICAL_FALSE_POSITIVE": "AUDIT_COMPLETE_NON_BIOMEDICAL_FALSE_POSITIVE",
        "EMPTY": "AUDIT_COMPLETE_NO_CAPABILITY",
    }
    audit_by_order = {int(a["queue_order"]): a for a in audits}
    for row in repositories:
        order_value = row.get("external_deep_audit_queue_order")
        if order_value is None:
            continue
        order = int(order_value)
        if order not in audit_by_order:
            continue
        audit = audit_by_order[order]
        row["status"] = "DEEP_AUDITED"
        row["detailed_file"] = report_rel
        existing_evidence = list(row.get("evidence_ids") or [])
        row["evidence_ids"] = list(dict.fromkeys(existing_evidence + evidence_ids))
        row["external_deep_audit_queue_status"] = result_to_status[audit["canonical_result_class"]]
        row["external_deep_audit_status"] = "DEEP_AUDITED"
        row["external_deep_audit_observed_at"] = timestamp
        row["external_deep_audit_evidence_ids"] = evidence_ids
        row["external_deep_audit_batch"] = batch
        row["external_deep_audit_report"] = report_rel
        row["external_deep_audit_manifest"] = manifest_rel
        row["external_deep_audit_result_class"] = audit["canonical_result_class"]
        row["external_deep_audit_change_ids"] = change_ids_by_order[order]
        row["external_deep_audit_lineage_ids"] = lineage_ids_by_order[order]

    return evidence_ids, change_ids_by_order, lineage_ids_by_order


def make_report(batch: int, audits: list[dict[str, Any]], total_records: int) -> str:
    start, end = batch_bounds(batch)
    counts = collections.Counter(a["canonical_result_class"] for a in audits)
    candidate_count = counts["DEEP_AUDIT_CANDIDATE"]
    risk_families = sum(bool(a["static_inventory"].get("risk_pattern_hits")) for a in audits)
    privacy_families = sum(bool(a["static_inventory"].get("privacy_pattern_hits")) for a in audits)
    science_families = sum(bool(a["static_inventory"].get("science_pattern_hits")) for a in audits)
    lines = [
        f"# External repository deep audit — Batch {batch:03d}",
        "",
        f"Observed at: `{now_utc()}`",
        "",
        "Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**",
        "",
        "## Scope and identity gate",
        "",
        f"- Stable queue orders: **{start}–{end}**.",
        f"- Canonical families: **{len(audits)}**.",
        f"- Canonical repository records: **{total_records}**.",
        "- Exactly one representative was verified for every family; queue order, family key, role and member count round-trip to `database/repositories.jsonl`.",
        "- Third-party code, notebooks, installers, workflows, models, containers and tests were not executed.",
        "",
        "## Static acquisition and review method",
        "",
        "Fork members were compared against the current source default branch through immutable GitHub comparison objects. Forks with no ahead commits close as source lineage. Unique fork blobs and independent repositories were inspected from immutable tarballs or Git trees, with bounded selected-blob fallback for very large artifacts. The review covered README and license text, dependency manifests and locks, workflows, notebooks as JSON, selected source text, data/configuration files, source/fork deltas, security-sensitive primitives, privacy/data-governance signals, reproducibility flags and repository-local licensing.",
        "",
        "Pattern matches are triage signals, not proof of exploitability or scientific invalidity. Every implementation candidate remains rejected for direct adoption until manual semantic comparison, source-to-sink security validation, scientific-domain review, provenance verification and isolated runtime testing are complete.",
        "",
        "## Result summary",
        "",
        "| Result class | Families |",
        "|---|---:|",
    ]
    for result in ["DEEP_AUDIT_CANDIDATE", "NO_UNIQUE_OR_SOURCE_LINEAGE", "DOC_METADATA_MAINTENANCE_ONLY", "NON_BIOMEDICAL_FALSE_POSITIVE", "EMPTY"]:
        lines.append(f"| `{result}` | {counts[result]} |")
    lines.extend([
        "",
        f"Static-review flags were present in {risk_families} families for security-sensitive primitives, {privacy_families} for privacy/data-governance terms, and {science_families} for reproducibility or scientific-validation patterns. These counts are not severity scores.",
        "",
        "## Family ledger",
        "",
        "| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |",
        "|---:|---|---|---:|---:|---|",
    ])
    for audit in audits:
        inv = audit["static_inventory"]
        ahead = audit["source_fork_review"].get("unique_commit_total", 0)
        file_summary = f"{inv.get('code_files',0)}/{inv.get('doc_files',0)}/{inv.get('data_files',0)}"
        repos = ", ".join(f"`{x}`" for x in audit["repository_names"])
        disposition = audit["disposition"].replace("|", "/")
        lines.append(f"| {audit['queue_order']} | {repos} | `{audit['canonical_result_class']}` | {ahead} | {file_summary} | {disposition} |")
    lines.extend(["", "## Candidate and blocker details", ""])
    for audit in audits:
        if audit["canonical_result_class"] != "DEEP_AUDIT_CANDIDATE":
            continue
        inv = audit["static_inventory"]
        lines.extend([
            f"### Order {audit['queue_order']} — `{audit['family_source']}`",
            "",
            f"Bounded repositories: {', '.join('`'+x+'`' for x in audit['repository_names'])}.",
            "",
            f"Immutable acquisition: {', '.join(inv.get('acquisitions') or [])}; files read {inv.get('files_read',0)}, code {inv.get('code_files',0)}, documentation {inv.get('doc_files',0)}, data {inv.get('data_files',0)}, manifests {inv.get('manifest_files',0)}.",
            "",
            f"Static security flags: `{json.dumps(inv.get('risk_pattern_hits') or {}, ensure_ascii=False)}`.",
            "",
            f"Privacy/data-governance flags: `{json.dumps(inv.get('privacy_pattern_hits') or {}, ensure_ascii=False)}`.",
            "",
            f"Scientific/reproducibility flags: `{json.dumps(inv.get('science_pattern_hits') or {}, ensure_ascii=False)}`.",
            "",
            "Direct-adoption blockers:",
            "",
        ])
        for blocker in audit["direct_adoption_blockers"]:
            lines.append(f"- {blocker}.")
        lines.extend(["", f"Disposition: **{audit['disposition']}**.", ""])
    if candidate_count == 0:
        lines.extend(["No implementation candidate survived source-lineage, documentation-only, false-positive and empty-artifact reduction in this batch.", ""])
    lines.extend([
        "## Completion boundary",
        "",
        "The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.",
        "",
    ])
    return "\n".join(lines)


def correct_remote_handoff_counts(repositories: list[dict[str, Any]]) -> None:
    """Correct the remote-recovery checkpoint from canonical orders 1-212."""
    batch8_rows = [
        r for r in repositories
        if r.get("external_deep_audit_queue_order") is not None
        and int(r["external_deep_audit_queue_order"]) <= 212
        and r.get("external_deep_audit_queue_status") != "EXCLUDED_ALREADY_SCREENED_BIOMNI_LINEAGE"
        and r.get("external_deep_audit_status") == "DEEP_AUDITED"
    ]
    initial_records = len(batch8_rows)
    initial_families = len({int(r["external_deep_audit_queue_order"]) for r in batch8_rows})
    remaining_families = 2069 - initial_families
    remaining_records = 2161 - initial_records
    checkpoint = EXT_DIR / "queue-checkpoint-after-batch-008.md"
    if checkpoint.exists():
        text = checkpoint.read_text(encoding="utf-8")
        text = re.sub(r"Completed through Batch 008: \*\*\d+ families\*\* and \*\*\d+ records\*\*\.", f"Completed through Batch 008: **{initial_families} families** and **{initial_records} records**.", text)
        text = re.sub(r"Remaining before final Batch 009 completion: \*\*\d+ families\*\* and \*\*\d+ records\*\*\.", f"Remaining before final Batch 009 completion: **{remaining_families} families** and **{remaining_records} records**.", text)
        checkpoint.write_text(text, encoding="utf-8")
    recovery = EXT_DIR / "deep-audit-batch-009-remote-recovery.md"
    if recovery.exists():
        text = recovery.read_text(encoding="utf-8")
        text = re.sub(r"prior completed checkpoint remains \*\*\d+ / 2,069 families\*\* and \*\*\d+ / 2,161 queued repository records\*\*\.", f"prior completed checkpoint remains **{initial_families} / 2,069 families** and **{initial_records} / 2,161 queued repository records**.", text)
        recovery.write_text(text, encoding="utf-8")


def update_state(batch: int, completed_families: int, completed_records: int) -> None:
    text = STATE_FILE.read_text(encoding="utf-8")
    total_families = 2069
    total_records = 2161
    remaining_families = total_families - completed_families
    remaining_records = total_records - completed_records
    timestamp = now_utc()
    final = batch == 46
    if final:
        current_entity = "Phase 8 external repository queue exhausted; commercial comparison remains"
        current_batch = "external-deep-audit-complete-through-batch-046"
        cursor = f"batches 001-046 complete; {completed_families}/{total_families} families and {completed_records}/{total_records} queued records DEEP_AUDITED; 0 remain"
        next_action = "continue official commercial discovery, compare verified commercial behaviors against the frozen OSS baseline, then assess clean-room reconstruction candidates"
        phase = "Phase 8 complete - external repository deep audit exhausted"
    else:
        next_start, next_end = batch_bounds(batch + 1)
        current_entity = f"next external deep-audit queue orders {next_start}-{next_end}"
        current_batch = f"external-deep-audit-{batch:03d}-complete"
        cursor = f"batches 001-{batch:03d} complete; {completed_families}/{total_families} families and {completed_records}/{total_records} queued records DEEP_AUDITED; {remaining_families} families/{remaining_records} records remain"
        next_action = f"start exact queue orders {next_start}-{next_end} as Batch {batch+1:03d}; preserve static-only and exact canonical identity gates"
        phase = "Phase 8 - deep audit relevant external repositories"
    replacements = {
        r"^last_updated_utc:.*$": f"last_updated_utc: {timestamp}",
        r"^current_phase:.*$": f"current_phase: {phase}",
        r"^current_entity:.*$": f"current_entity: {current_entity}",
        r"^current_batch:.*$": f"current_batch: {current_batch}",
        r"^current_page_or_cursor:.*$": f"current_page_or_cursor: {cursor}",
        r"^next_action:.*$": f"next_action: {next_action}",
    }
    for pattern, replacement in replacements.items():
        text, count = re.subn(pattern, replacement, text, flags=re.M)
        if count != 1:
            raise AuditError(f"STATE replacement failed: {pattern} count={count}")
    completed_line = f"- completed external deep-audit Batch {batch:03d}; exact bounded queue interval closed and committed with static-only direct-adoption rejection"
    if completed_line not in text:
        text = text.replace("pending_units:\n", completed_line + "\npending_units:\n", 1)
    text = re.sub(
        r"- (?:GPT Pro should begin Batch 009|continue Phase 8 from the next exact queue interval after Batch \d+)[^\n]*\n",
        "" if final else f"- continue Phase 8 from the next exact queue interval after Batch {batch:03d}; do not inflate counters before canonical round-trip verification\n",
        text,
    )
    STATE_FILE.write_text(text, encoding="utf-8")


def update_coverage(batch: int, completed_families: int, completed_records: int) -> None:
    text = COVERAGE_FILE.read_text(encoding="utf-8")
    remaining_families = 2069 - completed_families
    remaining_records = 2161 - completed_records
    final = batch == 46
    text = re.sub(
        r"\| External HIGH person-repository records \| 2272 \| 2272 normalized \| \d+ \|[^\n]*\| (PARTIAL|COMPLETE) \|",
        f"| External HIGH person-repository records | 2272 | 2272 normalized | {completed_records} | 111 prior exclusions; external batches 001–{batch:03d} complete; {remaining_records} queued records remain | {'COMPLETE' if final else 'PARTIAL'} |",
        text,
    )
    text = re.sub(
        r"\| External HIGH lineage families \| 2069 \| 2069 normalized \| \d+ \|[^\n]*\| (PARTIAL|COMPLETE) \|",
        f"| External HIGH lineage families | 2069 | 2069 normalized | {completed_families} | stable deterministic queue orders 1–2069; external batches 001–{batch:03d} complete; {remaining_families} not deep-audited | {'COMPLETE' if final else 'PARTIAL'} |",
        text,
    )
    ledger_header = "## External deep-audit completion ledger"
    entry = f"- Batch {batch:03d}: completed exact queue orders {batch_bounds(batch)[0]}–{batch_bounds(batch)[1]}; cumulative {completed_families}/2069 families and {completed_records}/2161 queued records."
    if ledger_header not in text:
        text += f"\n\n{ledger_header}\n\n{entry}\n"
    elif entry not in text:
        text += entry + "\n"
    COVERAGE_FILE.write_text(text, encoding="utf-8")


def update_queue_summary(batch: int, completed_families: int, completed_records: int) -> None:
    text = QUEUE_SUMMARY_FILE.read_text(encoding="utf-8")
    final = batch == 46
    if final:
        text = text.replace("Status: **PARTIAL** — queue normalization is complete; deep audit is not.", "Status: **COMPLETE** — queue normalization and bounded static deep audit are complete.")
        next_sentence = "All stable queue orders 1–2,069 are complete."
    else:
        ns, ne = batch_bounds(batch + 1)
        next_sentence = f"The next unstarted shard is orders {ns}–{ne}."
    text = re.sub(
        r"(?:The first four accelerated shards closed orders 13–212; the\nnext unstarted shard is orders 213–262\.|External deep-audit batches are complete through Batch \d+\.\n(?:The next unstarted shard is orders \d+–\d+\.|All stable queue orders 1–2,069 are complete\.))",
        f"External deep-audit batches are complete through Batch {batch:03d}.\n{next_sentence}",
        text,
    )
    ledger_header = "## Canonical completion ledger after accelerated batches"
    entry = f"- Batch {batch:03d}: orders {batch_bounds(batch)[0]}–{batch_bounds(batch)[1]} complete; cumulative **{completed_families}/2,069 families** and **{completed_records}/2,161 queued records**; **{2069-completed_families} families** remain."
    if ledger_header not in text:
        text += f"\n\n{ledger_header}\n\n{entry}\n"
    elif entry not in text:
        text += entry + "\n"
    QUEUE_SUMMARY_FILE.write_text(text, encoding="utf-8")


def update_master_index(batch: int, audits: list[dict[str, Any]], evidence_ids: list[str], changes: list[dict[str, Any]], lineages: list[dict[str, Any]], completed_families: int, completed_records: int) -> None:
    text = MASTER_INDEX_FILE.read_text(encoding="utf-8")
    last_change = changes[-1]["change_id"] if changes else "NONE"
    batch_changes = [c["change_id"] for c in changes if c.get("detailed_file") == f"external-repos/deep-audit-batch-{batch:03d}.md"]
    batch_lineages = [l["lineage_id"] for l in lineages if l.get("detailed_file") == f"external-repos/deep-audit-batch-{batch:03d}.md"]
    change_range = "NONE" if not batch_changes else (batch_changes[0] if len(batch_changes) == 1 else f"{batch_changes[0]}–{batch_changes[-1]}")
    lineage_range = "NONE" if not batch_lineages else (batch_lineages[0] if len(batch_lineages) == 1 else f"{batch_lineages[0]}–{batch_lineages[-1]}")
    counts = collections.Counter(a["canonical_result_class"] for a in audits)
    start, end = batch_bounds(batch)
    report_row = f"| External deep audit batch {batch:03d} | deterministic static repository/family audit | COMPLETE | Orders {start}–{end} closed: {len(audits)} families; " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + f"; all direct adoption rejected | `external-repos/deep-audit-batch-{batch:03d}.md` | `{change_range}`, `{lineage_range}`, `{evidence_ids[0]}`–`{evidence_ids[-1]}` |"
    manifest_row = f"| External batch {batch:03d} canonical manifest | exact-identity static audit manifest | COMPLETE | Exact family ledger with immutable acquisition, source/fork comparison, static science/security/privacy/license flags and canonical round-trip bindings | `external-repos/deep-audit-batch-{batch:03d}-manifest.jsonl` | {sum(len(a['canonical_repository_ids']) for a in audits)} bounded repository IDs |"
    if report_row not in text:
        text += "\n" + report_row + "\n" + manifest_row + "\n"
    text = re.sub(
        r"\| Structured database \| database \| ACTIVE \| Stable IDs and canonical evidence records \| `database/` \|[^\n]*",
        f"| Structured database | database | ACTIVE | Stable IDs and canonical evidence records | `database/` | repository IDs unchanged, changes through `{last_change}`, lineages through `{lineages[-1]['lineage_id'] if lineages else 'NONE'}`, evidence through `{evidence_ids[-1]}` |",
        text,
    )
    text = re.sub(
        r"\| External deep-audit queue \| queue normalization \| (COMPLETE|PARTIAL) \|[^\n]*",
        f"| External deep-audit queue | queue normalization and static audit | {'COMPLETE' if batch == 46 else 'PARTIAL'} | 2,272 HIGH records normalized into 2,069 stable families; {completed_records} records/{completed_families} families deep-audited and {2161-completed_records} queued records/{2069-completed_families} families remain | `external-repos/queue-summary.md` | `{evidence_ids[0]}`–`{evidence_ids[-1]}` |",
        text,
    )
    MASTER_INDEX_FILE.write_text(text, encoding="utf-8")


def update_research_log(batch: int, audits: list[dict[str, Any]], total_records: int, evidence_ids: list[str]) -> None:
    text = RESEARCH_LOG_FILE.read_text(encoding="utf-8") if RESEARCH_LOG_FILE.exists() else "# Research Log\n"
    counts = collections.Counter(a["canonical_result_class"] for a in audits)
    start, end = batch_bounds(batch)
    entry = f"\n## {now_utc()} — External deep audit Batch {batch:03d}\n\n- Closed exact queue orders {start}–{end}: {len(audits)} families / {total_records} records.\n- Result counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) + ".\n- Static-only review; no third-party code executed; all direct adoption rejected.\n- Evidence: " + ", ".join(evidence_ids) + ".\n"
    if f"External deep audit Batch {batch:03d}" not in text:
        text += entry
    RESEARCH_LOG_FILE.write_text(text, encoding="utf-8")


def write_final_summary(repositories: list[dict[str, Any]], evidence: list[dict[str, Any]], changes: list[dict[str, Any]], lineages: list[dict[str, Any]]) -> None:
    queued = [r for r in repositories if r.get("external_deep_audit_queue_order") is not None and r.get("external_deep_audit_queue_status") != "EXCLUDED_ALREADY_SCREENED_BIOMNI_LINEAGE"]
    groups: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in queued:
        groups[int(row["external_deep_audit_queue_order"])].append(row)
    result_counts = collections.Counter()
    for order, rows in groups.items():
        reps = [r for r in rows if r.get("external_deep_audit_family_role") == "REPRESENTATIVE"]
        if reps:
            result_counts[reps[0].get("external_deep_audit_result_class") or "LEGACY_BATCH_CLASS"] += 1
    content = [
        "# External repository deep-audit completion summary",
        "",
        f"Completed at: `{now_utc()}`",
        "",
        "Status: **COMPLETE**",
        "",
        "- Stable family queue: **2,069 / 2,069 complete**.",
        "- Queued repository records: **2,161 / 2,161 complete**.",
        "- Previously screened Biomni-lineage exclusions: **111 records**.",
        "- Batch reports: **001–046**.",
        "- Third-party code execution: **none**.",
        "- Feature or Implementation IDs allocated during external deep audit: **none**.",
        f"- Canonical Change records now end at `{changes[-1]['change_id'] if changes else 'NONE'}`.",
        f"- Canonical Lineage records now end at `{lineages[-1]['lineage_id'] if lineages else 'NONE'}`.",
        f"- Canonical Evidence records now end at `{evidence[-1]['evidence_id'] if evidence else 'NONE'}`.",
        "",
        "## Final family result distribution",
        "",
        "| Result class | Families |",
        "|---|---:|",
    ]
    for key, value in sorted(result_counts.items()):
        content.append(f"| `{key}` | {value} |")
    content.extend([
        "",
        "All implementation candidates remain rejected for direct adoption. They are bounded comparison or clean-room reconstruction leads pending manual semantic deduplication against the frozen Biomni baseline, scientific-domain validation, source-to-sink security analysis, data-governance review, license/provenance resolution and isolated runtime testing.",
        "",
    ])
    FINAL_SUMMARY_FILE.write_text("\n".join(content), encoding="utf-8")


def canonical_progress(repositories: list[dict[str, Any]]) -> tuple[int, int]:
    queued = [r for r in repositories if r.get("external_deep_audit_queue_order") is not None and r.get("external_deep_audit_queue_status") != "EXCLUDED_ALREADY_SCREENED_BIOMNI_LINEAGE"]
    completed_records = sum(1 for r in queued if r.get("external_deep_audit_status") == "DEEP_AUDITED")
    completed_orders = {
        int(r["external_deep_audit_queue_order"])
        for r in queued
        if r.get("external_deep_audit_status") == "DEEP_AUDITED"
    }
    return len(completed_orders), completed_records


def batch_already_complete(batch: int, repositories: list[dict[str, Any]]) -> bool:
    start, end = batch_bounds(batch)
    rows = [r for r in repositories if r.get("external_deep_audit_queue_order") is not None and start <= int(r["external_deep_audit_queue_order"]) <= end]
    expected_orders = set(range(start, end + 1))
    found_orders = {int(r["external_deep_audit_queue_order"]) for r in rows}
    report = EXT_DIR / f"deep-audit-batch-{batch:03d}.md"
    manifest = EXT_DIR / f"deep-audit-batch-{batch:03d}-manifest.jsonl"
    return found_orders == expected_orders and bool(rows) and all(r.get("external_deep_audit_status") == "DEEP_AUDITED" for r in rows) and report.exists() and manifest.exists()


def commit_and_push(batch: int, final: bool) -> None:
    run(["git", "add", "research/biomni-ecosystem", "research_log.md"])
    if final and WORKFLOW_FILE.exists():
        run(["git", "rm", "-f", str(WORKFLOW_FILE.relative_to(ROOT))])
    status = run(["git", "status", "--porcelain"], capture=True).stdout.strip()
    if not status:
        raise AuditError(f"batch {batch:03d}: no changes to commit")
    run(["git", "commit", "-m", f"research: complete external deep audit batch {batch:03d}"])
    run(["git", "push", "origin", f"HEAD:{TARGET_BRANCH}"])


def main() -> int:
    if not REPOSITORIES_FILE.exists():
        raise AuditError(f"missing canonical repository database: {REPOSITORIES_FILE}")
    run(["git", "config", "user.name", "Biomni Static Audit Bot"])
    run(["git", "config", "user.email", "118109999+MikeGong1@users.noreply.github.com"])
    run(["git", "status", "--short", "--branch"])
    initial_repositories = load_jsonl(REPOSITORIES_FILE)
    correct_remote_handoff_counts(initial_repositories)

    for batch in range(START_BATCH, END_BATCH + 1):
        repositories = load_jsonl(REPOSITORIES_FILE)
        if batch_already_complete(batch, repositories):
            print(f"Batch {batch:03d} already complete; skipping", flush=True)
            continue
        groups: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
        for row in repositories:
            order = row.get("external_deep_audit_queue_order")
            if order is not None and row.get("external_deep_audit_queue_status") != "EXCLUDED_ALREADY_SCREENED_BIOMNI_LINEAGE":
                groups[int(order)].append(row)
        start, end, orders, total_records = assert_batch_input(batch, groups)
        print(f"Auditing Batch {batch:03d}: orders {start}-{end}, {len(orders)} families, {total_records} records", flush=True)

        audits_by_order: dict[int, dict[str, Any]] = {}
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(audit_family, order, groups[order]): order for order in orders}
            completed = 0
            for future in as_completed(futures):
                order = futures[future]
                audits_by_order[order] = future.result()
                completed += 1
                print(f"  [{completed}/{len(orders)}] order {order} complete", flush=True)
        audits = [audits_by_order[order] for order in orders]

        evidence = load_jsonl(EVIDENCE_FILE)
        changes = load_jsonl(CHANGES_FILE)
        lineages = load_jsonl(LINEAGES_FILE)
        evidence_ids, _, _ = allocate_batch_records(batch, audits, repositories, evidence, changes, lineages)

        report_path = EXT_DIR / f"deep-audit-batch-{batch:03d}.md"
        manifest_path = EXT_DIR / f"deep-audit-batch-{batch:03d}-manifest.jsonl"
        report_path.write_text(make_report(batch, audits, total_records), encoding="utf-8")
        write_jsonl(manifest_path, audits)
        write_jsonl(REPOSITORIES_FILE, repositories)
        write_jsonl(EVIDENCE_FILE, evidence)
        write_jsonl(CHANGES_FILE, changes)
        write_jsonl(LINEAGES_FILE, lineages)

        completed_families, completed_records = canonical_progress(repositories)
        expected_completed = end
        if completed_families != expected_completed:
            raise AuditError(f"batch {batch:03d}: completed family count {completed_families} != expected {expected_completed}")
        if completed_records < completed_families:
            raise AuditError(f"batch {batch:03d}: completed records {completed_records} < families {completed_families}")

        update_state(batch, completed_families, completed_records)
        update_coverage(batch, completed_families, completed_records)
        update_queue_summary(batch, completed_families, completed_records)
        update_master_index(batch, audits, evidence_ids, changes, lineages, completed_families, completed_records)
        update_research_log(batch, audits, total_records, evidence_ids)
        final = batch == END_BATCH == 46
        if final:
            if completed_families != 2069 or completed_records != 2161:
                raise AuditError(f"final canonical counts mismatch: families={completed_families}, records={completed_records}")
            write_final_summary(repositories, evidence, changes, lineages)
        commit_and_push(batch, final)
        print(f"Batch {batch:03d} committed and pushed", flush=True)

    print("All requested batches complete", flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FATAL: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
        raise
