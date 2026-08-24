#!/usr/bin/env python3
"""Complete the bounded Phase 9 static-research layer from repository evidence.

This script intentionally does not execute third-party repositories. It consumes the
existing Phase 8 evidence, the SciAgent per-Skill audit, the frozen Biomni baseline,
and the bounded commercial discovery. It produces deterministic provisional Feature
and Implementation catalogs, a validation queue, and authoritative Phase 9A control
files. Canonical Feature/Implementation IDs remain reserved for isolated Codex
validation.
"""
from __future__ import annotations

import ast
import json
import re
import textwrap
from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
PHASE9 = ROOT / "phase-9"
DB = ROOT / "database"
EXTERNAL = ROOT / "external-repos"
BASELINE_ROOT = ROOT.parents[1]
BRANCH = "research/biomni-ecosystem-audit"
BIOMNI_SHA = "400c1f366b96a35ca253e13c9b06c5076af41d65"
SCIAGENT_SHA = "a0aac0f4576a550d5316baf6da3d72e53408b3a2"
EXPECTED_FAMILIES = 598
EXPECTED_SKILLS = 203
EXPECTED_SKILL_CANDIDATES = 125


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    if not path.exists():
        return rows, [f"missing:{path}"]
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw)
        except Exception as exc:  # keep diagnostics, fail later when material
            errors.append(f"{path}:{i}:{type(exc).__name__}:{exc}")
            continue
        if isinstance(obj, dict):
            rows.append(obj)
        else:
            errors.append(f"{path}:{i}:not-object")
    return rows, errors


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in rows)
    path.write_text(data + ("\n" if data else ""), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def pick(rec: dict[str, Any], *keys: str, default: Any = None) -> Any:
    for key in keys:
        value = rec.get(key)
        if value not in (None, "", [], {}):
            return value
    return default


def flatten(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, dict):
        return " ".join(f"{k} {flatten(v)}" for k, v in value.items())
    if isinstance(value, (list, tuple, set)):
        return " ".join(flatten(v) for v in value)
    return str(value)


def norm(text: Any) -> str:
    s = flatten(text).lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", ".", text.lower()).strip(".")
    return s or "unknown"


def tokens(text: Any) -> set[str]:
    stop = {
        "the", "and", "for", "with", "from", "into", "using", "use", "tool",
        "tools", "analysis", "data", "scientific", "agent", "system", "query",
        "repository", "api", "workflow", "model", "models", "database", "based",
        "this", "that", "are", "can", "via", "of", "to", "in", "a", "an",
    }
    return {t for t in norm(text).split() if len(t) >= 3 and t not in stop}


@dataclass(frozen=True)
class Rule:
    key: str
    domain: str
    statement: str
    keywords: tuple[str, ...]
    priority: int = 50


RULES: tuple[Rule, ...] = (
    Rule("agent.orchestration.multi_agent", "agent-core", "协调多个专门 Agent、supervisor 与 worker 完成科研任务。", ("multi agent", "multi-agent", "supervisor", "langgraph", "crew", "autogen", "agent graph"), 95),
    Rule("agent.orchestration.planning_execution", "agent-core", "把科研目标拆成计划、工具调用和可恢复执行步骤。", ("planner", "planning", "task decomposition", "execution plan", "reasoning agent"), 90),
    Rule("agent.workflow.human_approval", "agent-core", "在关键科研步骤设置人工检查、调整、跳过和批准门。", ("human gate", "approval", "proceed adjust skip", "human in the loop", "human-in-the-loop"), 92),
    Rule("agent.memory.session_context", "agent-core", "保存 Agent 会话、记忆、状态和跨步骤上下文。", ("agent memory", "session memory", "conversation memory", "checkpoint memory", "long term memory"), 72),
    Rule("tooling.mcp.client_server", "tool-skill-mcp", "通过 MCP 发现、调用或暴露科研工具。", ("mcp server", "mcp client", "model context protocol", "fastmcp", "mcp tool"), 93),
    Rule("tooling.skill.registry_discovery", "tool-skill-mcp", "注册、检索、选择和加载科学 Skills 或工具。", ("skill registry", "skills registry", "plugin discovery", "tool registry", "skill library", "scientific skills"), 94),
    Rule("tooling.sandbox.code_execution", "tool-skill-mcp", "在隔离环境中执行 Python、R、shell 或 notebook 科研代码。", ("sandbox", "code execution", "python execution", "bash execution", "r execution", "jupyter", "notebook execution"), 90),
    Rule("knowledge.literature.search_retrieval", "literature-evidence", "检索论文、摘要、全文和相关文献。", ("pubmed", "literature search", "paper search", "semantic scholar", "arxiv", "biorxiv", "full text"), 88),
    Rule("knowledge.evidence.claim_verification", "literature-evidence", "从来源中提取证据、核对主张并保存引用链。", ("claim verification", "evidence extraction", "citation", "regulatory source", "fact check", "literature review"), 90),
    Rule("database.variant.population", "scientific-database", "查询人群遗传变异、频率、constraint 和结构变异证据。", ("gnomad", "population frequency", "variant frequency", "allele frequency", "constraint", "loeu"), 91),
    Rule("database.variant.clinical_evidence", "scientific-database", "查询 ClinVar、dbSNP 或其他变异临床证据，并保留冲突和版本信息。", ("clinvar", "dbsnp", "variant clinical", "pathogenicity", "acmg", "variant interpretation"), 86),
    Rule("database.cancer_genomics", "scientific-database", "查询癌症基因组、突变、CNA、表达和临床队列信息。", ("cbioportal", "cancer genomics", "tcga", "cosmic", "somatic mutation"), 88),
    Rule("database.expression_qtl", "scientific-database", "查询组织表达、eQTL、sQTL、eGene 或公共表达数据。", ("gtex", "eqtl", "sqtl", "egene", "expression database", "archs4", "geo database"), 87),
    Rule("database.protein.domain_structure", "scientific-database", "查询蛋白结构域、家族、位点、序列和结构数据库。", ("interpro", "uniprot", "protein domain", "pfam", "pdb", "alphafold database"), 83),
    Rule("database.drug.binding_activity", "scientific-database", "查询药物、化合物、靶点、结合亲和力和生物活性数据。", ("bindingdb", "chembl", "pubchem", "drugbank", "bioactivity", "binding affinity"), 92),
    Rule("database.phenotype.disease_ontology", "scientific-database", "查询 phenotype、disease、ontology、gene association 和跨物种映射。", ("monarch", "phenotype", "hpo", "ontology", "disease association"), 84),
    Rule("database.pathway.network", "scientific-database", "查询 pathway、interaction、gene set 和生物网络数据库。", ("kegg", "reactome", "stringdb", "pathway", "gene set", "interaction database"), 81),
    Rule("integration.database.multi_service_client", "scientific-database", "统一管理多个生物数据库客户端、ID mapping、错误、限速和 provenance。", ("bioservices", "multi database", "multi-service", "cross database", "id mapping"), 89),
    Rule("pipeline.genomics.read_alignment", "genomics", "执行 DNA 或 RNA reads 的参考比对并保存 reference provenance。", ("bwa", "bwa-mem2", "star aligner", "bowtie", "hisat", "read alignment", "splice aware"), 86),
    Rule("data.genomics.hts_processing", "genomics", "读写、排序、索引、过滤和检查 SAM/BAM/CRAM/VCF/BCF。", ("samtools", "pysam", "bam", "cram", "vcf", "bcf", "htslib"), 88),
    Rule("pipeline.genomics.variant_calling_annotation", "genomics", "执行变异检测、标准化、过滤和功能注释。", ("variant calling", "gatk", "deepvariant", "freebayes", "vep", "snpeff", "variant annotation"), 91),
    Rule("pipeline.genomics.phylogenetics", "genomics", "组织序列比对、修剪、树推断、支持度和系统发育可视化。", ("phylogen", "iq-tree", "iqtree", "mafft", "fasttree", "ete3", "tree inference"), 85),
    Rule("pipeline.genomics.prokaryotic_annotation", "genomics", "对细菌或古菌基因组执行结构与功能注释。", ("prokka", "bakta", "genome annotation", "prokaryotic annotation", "pgap"), 83),
    Rule("analysis.genomics.pangenome", "genomics", "构建微生物 pan-genome、core/accessory gene 和 presence/absence 矩阵。", ("pangenome", "pan-genome", "roary", "panaroo", "ppanggolin"), 82),
    Rule("analysis.genomics.regulatory_motif", "genomics", "执行 TF motif 查询、序列扫描、富集和变异影响分析。", ("jaspar", "motif scan", "tfbs", "homer", "motif enrichment", "pwm", "pfm"), 87),
    Rule("design.genomics.crispr", "genomics", "设计或评估 CRISPR guide、编辑位点和脱靶风险。", ("crispr", "sgrna", "guide rna", "genome editing", "cas9"), 89),
    Rule("analysis.single_cell.qc_integration", "single-cell-spatial", "执行单细胞 QC、标准化、降维、批次整合和 embedding。", ("single cell", "single-cell", "scrna", "scanpy", "scvi", "harmony", "cell embedding"), 94),
    Rule("analysis.single_cell.annotation", "single-cell-spatial", "使用 marker、reference 或模型完成单细胞类型注释。", ("cell type annotation", "celltype", "celltypist", "azimuth", "popv", "scanvi"), 92),
    Rule("analysis.single_cell.rna_velocity", "single-cell-spatial", "执行 RNA velocity、latent time 和动态 driver 分析。", ("scvelo", "rna velocity", "velocity", "latent time"), 92),
    Rule("analysis.spatial_transcriptomics.workflow", "single-cell-spatial", "执行空间转录组加载、QC、区域、空间基因、去卷积和下游分析。", ("spatial transcript", "visium", "spatial omics", "spatial gene", "ezst", "spatial domain"), 96),
    Rule("model.spatial.histology_to_expression", "single-cell-spatial", "根据病理图像预测空间基因表达或空间分子表型。", ("histology to", "histology-to", "deep spot", "deepspot", "chatspatial", "spatial expression"), 97),
    Rule("analysis.cell_cell_communication", "single-cell-spatial", "推断细胞间配体—受体通信及其条件差异。", ("cellchat", "cell cell communication", "cell-cell communication", "ligand receptor", "nichenet"), 87),
    Rule("model.protein.structure_prediction", "protein-structure", "预测、检索或比较蛋白三维结构和复合物。", ("protein structure", "alphafold", "esmfold", "boltz", "structure prediction", "folding"), 96),
    Rule("design.protein.sequence", "protein-structure", "生成、优化或筛选具有目标性质的蛋白序列。", ("protein design", "sequence design", "antibody design", "proteinmpnn", "esm design"), 96),
    Rule("simulation.molecular_dynamics", "protein-structure", "配置并运行分子动力学模拟，分析轨迹、稳定性和相互作用。", ("molecular dynamics", "openmm", "mdanalysis", "gromacs", "trajectory", "rmsd", "rmsf"), 93),
    Rule("analysis.structure.docking_screening", "protein-structure", "执行 docking、virtual screening 和结构基础候选排序。", ("docking", "vina", "smina", "virtual screening", "dock", "ligand screening"), 92),
    Rule("analysis.glyco.engineering", "protein-structure", "检测、解释或工程化蛋白糖基化位点。", ("glyco", "glycosyl", "glycan", "sequon"), 84),
    Rule("analysis.drug.admet", "drug-discovery", "预测或分析化合物 ADMET、毒性和药代性质。", ("admet", "toxicity", "absorption", "metabolism", "pk prediction", "drug safety"), 94),
    Rule("model.drug.pbpk_pk", "drug-discovery", "建立 PBPK／PK 模型、模拟暴露和参数敏感性。", ("pbpk", "pk-sim", "ospsuite", "pharmacokinetic", "pk model"), 92),
    Rule("analysis.drug.sar_selectivity", "drug-discovery", "比较 SAR、选择性、多靶点活性和 assay 证据。", ("sar", "selectivity", "polypharmacology", "binding activity", "structure activity"), 90),
    Rule("workflow.drug.regulatory_safety", "drug-discovery", "组织药物发现安全、法规来源和 stage-gate 决策支持。", ("regulatory", "ich", "fda", "drug discovery safety", "nonclinical", "safety skills"), 82),
    Rule("analysis.bioimage.segmentation", "bioimaging", "对显微、病理或医学图像执行分割和定量。", ("segmentation", "cellpose", "nnunet", "nnu-net", "mask", "object detection"), 89),
    Rule("analysis.bioimage.registration", "bioimaging", "对医学或显微图像执行刚性、仿射或形变配准。", ("image registration", "simpleitk", "registration", "affine", "deformable"), 84),
    Rule("integration.bioimage.viewer_bridge", "bioimaging", "提供 napari、ImageJ/Fiji 或多维图像交互与插件桥接。", ("napari", "imagej", "fiji", "pyimagej", "image viewer", "multidimensional image"), 86),
    Rule("analysis.pathology.slide", "bioimaging", "处理病理 whole-slide image、tile、组织区域和病理模型推理。", ("pathology", "whole slide", "wsi", "histology", "slide image", "qupath"), 94),
    Rule("visualization.scientific.interactive", "bioimaging", "生成可交互科学图形、3D 可视化和可追溯导出。", ("plotly", "visualization", "3d viewer", "scientific plotting", "dashboard"), 78),
    Rule("analysis.statistics.bayesian", "statistics-evaluation", "执行 Bayesian 建模、采样诊断、预测检验和模型比较。", ("pymc", "bayesian", "nuts", "advi", "posterior", "waic", "loo"), 91),
    Rule("analysis.statistics.classical", "statistics-evaluation", "执行回归、GLM、time-series、mixed effects 和诊断。", ("statsmodels", "statistical modeling", "glm", "ols", "logit", "sarimax", "mixed effects"), 88),
    Rule("analysis.statistics.survival", "statistics-evaluation", "执行 censoring-aware survival、competing risks 和时间事件评估。", ("survival", "cox", "kaplan", "censor", "competing risk"), 87),
    Rule("evaluation.benchmark.reproducibility", "statistics-evaluation", "构建可复现 benchmark、golden fixtures、误差分析和回归测试。", ("benchmark", "evaluation", "reproduc", "golden test", "bixbench", "biomnibench"), 95),
    Rule("data.standard.bids", "data-standards", "组织和验证 BIDS 数据、metadata、derivatives 和 BIDS Apps。", ("bids", "pybids", "dicom conversion", "bids app"), 88),
    Rule("data.standard.ann_data_omics", "data-standards", "管理 AnnData、MuData 或组学矩阵 schema、坐标和 provenance。", ("anndata", "mudata", "h5ad", "omics data", "matrix schema"), 82),
    Rule("data.provenance.versioned_research", "data-standards", "对科研数据、运行命令、容器和发布建立版本化 provenance。", ("datalad", "git annex", "git-annex", "data provenance", "versioned data", "rerun"), 91),
    Rule("data.local_cache.database", "data-standards", "把大型科学数据库构建为可版本化的本地缓存和快速查询层。", ("local database", "local cache", "offline database", "gnomad db", "duckdb", "sqlite cache"), 88),
    Rule("workspace.integrated.research", "deployment-interface", "提供文件、分析、Agent、可视化和协作的一体化科研工作区。", ("workspace", "integrated biology", "research platform", "browser workspace", "scientific platform"), 92),
    Rule("deployment.api.server", "deployment-interface", "通过 API、FastAPI、Rust、MCP 或 Web 服务暴露科研计算。", ("fastapi", "api server", "web server", "rest api", "grpc", "service"), 81),
    Rule("deployment.container.environment", "deployment-interface", "使用 Docker、uv、Conda 或可复现环境配置科研工具链。", ("docker", "container", "uv", "conda", "environment", "dependency lock"), 82),
    Rule("deployment.cloud_hpc.job", "deployment-interface", "调度云端、GPU、HPC、sandbox 和并发科学任务。", ("hpc", "gpu", "cloud", "job management", "slurm", "sandbox", "compute"), 91),
    Rule("governance.security_privacy", "safety-governance", "控制认证、secret、PHI/PII、数据外传和危险操作。", ("security", "privacy", "phi", "pii", "authentication", "authorization", "secret", "secure gateway"), 93),
    Rule("laboratory.automation.instrument", "laboratory-automation", "控制实验机器人、液体处理、仪器、校准和人工批准。", ("opentrons", "liquid handling", "lab automation", "robot", "instrument control", "pylabrobot"), 89),
)

RULE_BY_KEY = {r.key: r for r in RULES}


def rule_score(rule: Rule, text: str) -> int:
    score = 0
    for kw in rule.keywords:
        k = norm(kw)
        if k and k in text:
            score += 5 + len(k.split())
        else:
            parts = k.split()
            if parts and all(p in text for p in parts):
                score += 2 + len(parts)
    return score


def classify_text(text: Any, max_rules: int = 2) -> list[Rule]:
    n = norm(text)
    scored = sorted(((rule_score(rule, n), rule.priority, rule.key, rule) for rule in RULES), reverse=True)
    selected = [entry[3] for entry in scored if entry[0] > 0][:max_rules]
    if selected:
        return selected
    return [Rule("research.reference.unclassified", "reference", "保留该来源作为待代码级拆解的科研实现参考。", (), 30)]


def extract_baseline_tools() -> list[dict[str, str]]:
    tools: list[dict[str, str]] = []
    desc_dir = BASELINE_ROOT / "biomni" / "tool" / "tool_description"
    for path in sorted(desc_dir.glob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for node in tree.body:
            if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "description" for t in node.targets):
                try:
                    value = ast.literal_eval(node.value)
                except Exception:
                    continue
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict) and item.get("name"):
                            tools.append({
                                "name": str(item.get("name")),
                                "description": str(item.get("description", "")),
                                "module": path.stem,
                            })
    return tools


MANUAL_BASELINE: dict[str, tuple[str, ...]] = {
    "database.cancer_genomics": ("query_cbioportal",),
    "database.variant.population": ("query_gnomad",),
    "database.variant.clinical_evidence": ("query_clinvar", "query_dbsnp"),
    "database.protein.domain_structure": ("query_interpro", "query_uniprot", "query_pdb", "query_alphafold"),
    "database.phenotype.disease_ontology": ("query_monarch",),
    "analysis.genomics.regulatory_motif": ("query_jaspar", "find_enriched_motifs_with_homer"),
    "pipeline.genomics.prokaryotic_annotation": ("annotate_bacterial_genome",),
    "analysis.glyco.engineering": ("find_n_glycosylation_motifs", "predict_o_glycosylation_hotspots"),
    "analysis.bioimage.segmentation": ("segment_with_nn_unet", "segment_cells_with_deep_learning"),
    "analysis.bioimage.registration": ("quick_rigid_registration", "quick_affine_registration", "quick_deformable_registration"),
    "analysis.single_cell.qc_integration": ("create_scvi_embeddings_scRNA", "create_harmony_embeddings_scRNA"),
    "analysis.single_cell.annotation": ("annotate_celltype_scRNA", "annotate_celltype_with_panhumanpy", "unsupervised_celltype_transfer_between_scRNA_datasets"),
    "tooling.mcp.client_server": ("A1.add_mcp", "A1.create_mcp_server"),
    "tooling.sandbox.code_execution": ("Python execution", "Bash execution", "R execution"),
}


def baseline_gap(rule: Rule, source_text: str, tools: list[dict[str, str]]) -> tuple[str, list[str], float]:
    manual = MANUAL_BASELINE.get(rule.key)
    if manual:
        return "BASELINE_EQUIVALENT_PRESENT", list(manual), 0.98
    source_tokens = tokens(rule.statement + " " + source_text)
    best: list[tuple[float, str]] = []
    for tool in tools:
        ttext = f"{tool['name']} {tool['description']} {tool['module']}"
        tt = tokens(ttext)
        jac = len(source_tokens & tt) / max(1, len(source_tokens | tt))
        seq = SequenceMatcher(None, norm(rule.statement), norm(ttext)).ratio()
        score = max(jac, seq * 0.72)
        if score >= 0.16:
            best.append((score, tool["name"]))
    best.sort(reverse=True)
    evidence = [name for _, name in best[:4]]
    top = best[0][0] if best else 0.0
    if top >= 0.48:
        return "BASELINE_EQUIVALENT_PRESENT", evidence, round(top, 3)
    if top >= 0.29:
        return "PARTIAL_OVERLAP", evidence, round(top, 3)
    if top >= 0.20:
        return "RELATED_OVERLAP_NOT_EQUIVALENT", evidence, round(top, 3)
    return "CLEAR_GAP", evidence, round(top, 3)


def repo_name(rec: dict[str, Any]) -> str:
    value = pick(rec, "full_name", "repository_full_name", "name_with_owner", "repo_full_name", "repository")
    if isinstance(value, dict):
        value = pick(value, "full_name", "nameWithOwner", "name")
    return str(value or "")


def repo_id(rec: dict[str, Any]) -> str:
    return str(pick(rec, "repository_id", "repo_id", "id", "stable_id", default=""))


def queue_order(rec: dict[str, Any]) -> int | None:
    value = pick(rec, "external_deep_audit_queue_order", "queue_order")
    try:
        return int(value)
    except Exception:
        return None


def family_key(rec: dict[str, Any]) -> str:
    return str(pick(rec, "external_deep_audit_family_key", "family_key", default=""))


def result_class(rec: dict[str, Any]) -> str:
    value = str(pick(
        rec,
        "external_deep_audit_result",
        "external_deep_audit_result_class",
        "external_deep_audit_classification",
        "external_deep_audit_outcome",
        "result_class",
        "metadata_classification",
        default="",
    ))
    if value:
        return value
    if "DEEP_AUDIT_CANDIDATE" in json.dumps(rec, ensure_ascii=False, sort_keys=True):
        return "DEEP_AUDIT_CANDIDATE"
    return ""


def source_head(rec: dict[str, Any]) -> str:
    return str(pick(rec, "immutable_head_sha", "representative_head_sha", "default_branch_head_sha", "head_sha", "external_deep_audit_head_sha", default=""))


def risk_disposition(text: str, gap: str, result: str = "") -> str:
    n = norm(text)
    critical_terms = (
        "critical security", "critical privacy", "rce", "remote code execution", "patient data",
        "clinical invalid", "unauthenticated medical", "plaintext credential", "arbitrary path",
        "phi", "controlled data", "destructive", "source injection", "ssrf", "shell injection",
    )
    if any(term in n for term in critical_terms):
        return "REFERENCE_ONLY_BLOCKED"
    if gap == "BASELINE_EQUIVALENT_PRESENT" or "duplicate" in n or "superseded" in n:
        return "DUPLICATE_OR_SUPERSEDED"
    if result and result not in ("DEEP_AUDIT_CANDIDATE", ""):
        return "DUPLICATE_OR_SUPERSEDED"
    return "SOURCE_FIRST_WITH_REMEDIATION"


def load_enrichment() -> dict[int, dict[str, Any]]:
    out: dict[int, dict[str, Any]] = {}
    for path in sorted(EXTERNAL.glob("remote-research-batch-*-manifest.jsonl")):
        rows, _ = read_jsonl(path)
        for row in rows:
            try:
                out[int(row.get("queue_order"))] = row
            except Exception:
                continue
    for path in sorted(EXTERNAL.glob("deep-audit-batch-*-manifest.jsonl")):
        rows, _ = read_jsonl(path)
        for row in rows:
            q = pick(row, "queue_order", "external_deep_audit_queue_order")
            try:
                qi = int(q)
            except Exception:
                continue
            out.setdefault(qi, {}).update({k: v for k, v in row.items() if v not in (None, "", [], {})})
    return out


def build_candidate_families(tools: list[dict[str, str]]) -> tuple[list[dict[str, Any]], list[str]]:
    records, errors = read_jsonl(DB / "repositories.jsonl")
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rec in records:
        if not pick(rec, "external_deep_audit_queue_order", "external_deep_audit_family_key"):
            continue
        q = queue_order(rec)
        key = f"q:{q}" if q is not None else f"f:{family_key(rec)}"
        grouped[key].append(rec)

    enrichment = load_enrichment()
    families: list[dict[str, Any]] = []
    for _, members in grouped.items():
        if not any(result_class(m) == "DEEP_AUDIT_CANDIDATE" for m in members):
            continue
        q = next((queue_order(m) for m in members if queue_order(m) is not None), None)
        if q is None:
            continue
        enrich = enrichment.get(q, {})
        names = sorted({repo_name(m) for m in members if repo_name(m)})
        ids = sorted({repo_id(m) for m in members if repo_id(m)})
        rep = str(pick(enrich, "representative_repository", default="")) or (names[0] if names else "")
        desc_parts = []
        for m in members:
            desc_parts.extend([
                flatten(pick(m, "description", "summary", "research_summary")),
                flatten(pick(m, "topics", "language", "external_deep_audit_notes", "external_deep_audit_reason")),
            ])
        desc_parts.extend([
            flatten(pick(enrich, "research_conclusion", "recommended_local_action", "metadata_classification")),
            flatten(pick(enrich, "risk_flags", "topics", "language", "source_files")),
        ])
        combined = " ".join([rep, *names, *desc_parts])
        rules = classify_text(combined, max_rules=2)
        primary = rules[0]
        gap, evidence, confidence = baseline_gap(primary, combined, tools)
        risks = pick(enrich, "risk_flags", default=[])
        disposition = risk_disposition(combined + " " + flatten(risks), gap, "DEEP_AUDIT_CANDIDATE")
        stars = pick(enrich, "stars", default=0)
        try:
            stars_i = int(stars or 0)
        except Exception:
            stars_i = 0
        families.append({
            "queue_order": q,
            "family_key": next((family_key(m) for m in members if family_key(m)), str(pick(enrich, "family_key", default=""))),
            "repository_ids": ids or list(pick(enrich, "repository_ids", default=[])),
            "repositories": names or list(pick(enrich, "repositories", default=[])),
            "representative_repository": rep,
            "representative_head_sha": str(pick(enrich, "representative_head_sha", default="")) or next((source_head(m) for m in members if source_head(m)), ""),
            "source_repository": pick(enrich, "source_repository", default=None),
            "phase8_result": "DEEP_AUDIT_CANDIDATE",
            "static_feature_keys": [r.key for r in rules],
            "primary_feature_key": primary.key,
            "primary_domain": primary.domain,
            "capability_statement": primary.statement,
            "biomni_baseline_status": gap,
            "biomni_baseline_evidence": evidence,
            "gap_confidence": confidence,
            "research_disposition": disposition,
            "risk_flags": risks,
            "research_conclusion": pick(enrich, "research_conclusion", default=""),
            "recommended_local_action": pick(enrich, "recommended_local_action", default=""),
            "language": pick(enrich, "language", default=next((pick(m, "language") for m in members if pick(m, "language")), None)),
            "license_observation": pick(enrich, "license_spdx", default=next((pick(m, "license_spdx", "license") for m in members if pick(m, "license_spdx", "license")), None)),
            "stars": stars_i,
            "static_depth": "DETAILED_EXISTING_AUDIT" if q in (1, 6) else "FAMILY_LEVEL_PHASE8_EVIDENCE",
            "runtime_status": "NOT_EXECUTED_CODEX_REQUIRED",
            "canonical_status": "PROVISIONAL_STATIC_ONLY",
        })
    families.sort(key=lambda r: r["queue_order"])
    return families, errors


def load_existing_skill_overrides() -> dict[str, dict[str, Any]]:
    overrides: dict[str, dict[str, Any]] = {}
    path = PHASE9 / "static-normalization-batch-002-manifest.jsonl"
    rows, _ = read_jsonl(path)
    for row in rows:
        name = str(pick(row, "skill", "name", default=""))
        if name:
            overrides[name] = row
    return overrides


def skill_cluster_text(skill: dict[str, Any]) -> str:
    return " ".join([
        str(skill.get("name", "")),
        str(skill.get("category", "")),
        str(skill.get("capability", "")),
        str(skill.get("primary_issue", "")),
        str(skill.get("path", "")),
    ])


def build_sciagent(tools: list[dict[str, str]]) -> tuple[list[dict[str, Any]], list[str]]:
    rows, errors = read_jsonl(EXTERNAL / "sciagent-skill-audit-manifest.jsonl")
    overrides = load_existing_skill_overrides()
    out: list[dict[str, Any]] = []
    for row in sorted(rows, key=lambda r: int(r.get("audit_order", 10**9))):
        name = str(row.get("name", ""))
        text = skill_cluster_text(row)
        override = overrides.get(name, {})
        okey = str(pick(override, "provisional_feature_cluster", "provisional_feature_key", default=""))
        if okey:
            rule = RULE_BY_KEY.get(okey)
            if rule is None:
                rule = Rule(okey, okey.split(".", 1)[0], str(row.get("capability", "")), (), 70)
        else:
            rule = classify_text(text, max_rules=1)[0]
        gap, evidence, confidence = baseline_gap(rule, text, tools)
        if override:
            gap = str(pick(override, "biomni_baseline_status", default=gap))
            evidence = list(pick(override, "biomni_baseline_evidence", default=evidence) or [])
        candidate = bool(row.get("candidate"))
        if not candidate:
            disposition = "REFERENCE_ARCHIVE_NO_NEAR_TERM"
        else:
            disposition = risk_disposition(text, gap)
            if override:
                disposition = str(pick(override, "research_disposition", default=disposition))
        out.append({
            "audit_order": int(row.get("audit_order", 0)),
            "skill": name,
            "category": row.get("category"),
            "path": row.get("path"),
            "source_repository": "jaechang-hits/SciAgent-Skills",
            "source_head_sha": SCIAGENT_SHA,
            "source_change_id": "change-000081",
            "declared_license": row.get("declared_license"),
            "phase8_candidate": candidate,
            "capability": row.get("capability"),
            "primary_issue": row.get("primary_issue"),
            "provisional_feature_cluster": rule.key,
            "feature_domain": rule.domain,
            "biomni_baseline_status": gap,
            "biomni_baseline_evidence": evidence,
            "gap_confidence": confidence,
            "research_disposition": disposition,
            "runtime_status": "NOT_EXECUTED_CODEX_REQUIRED" if candidate else "NOT_SCHEDULED_REFERENCE_ONLY",
            "publication_review_required": candidate,
            "canonical_status": "PROVISIONAL_STATIC_ONLY",
        })
    return out, errors


def load_batch1_units() -> list[dict[str, Any]]:
    rows, _ = read_jsonl(PHASE9 / "static-normalization-batch-001-manifest.jsonl")
    return rows


def feature_priority(gap: str, disposition: str, family_count: int, skill_count: int, base_priority: int) -> int:
    score = base_priority
    score += {"CLEAR_GAP": 20, "PARTIAL_OVERLAP": 12, "RELATED_OVERLAP_NOT_EQUIVALENT": 8, "BASELINE_EQUIVALENT_PRESENT": -12}.get(gap, 0)
    score += min(12, family_count * 2) + min(8, skill_count)
    if disposition == "REFERENCE_ONLY_BLOCKED":
        score -= 20
    if disposition == "DUPLICATE_OR_SUPERSEDED":
        score -= 25
    return max(0, min(100, score))


def aggregate_gap(statuses: Iterable[str]) -> str:
    values = set(statuses)
    if "CLEAR_GAP" in values:
        return "CLEAR_GAP"
    if "PARTIAL_OVERLAP" in values:
        return "PARTIAL_OVERLAP"
    if "RELATED_OVERLAP_NOT_EQUIVALENT" in values:
        return "RELATED_OVERLAP_NOT_EQUIVALENT"
    if "BASELINE_EQUIVALENT_PRESENT" in values:
        return "BASELINE_EQUIVALENT_PRESENT"
    return "UNKNOWN_REQUIRES_CODE_COMPARE"


def aggregate_disposition(values: Iterable[str]) -> str:
    vals = set(values)
    if "SOURCE_FIRST_WITH_REMEDIATION" in vals or "SOURCE_FIRST_RESEARCH_CANDIDATE" in vals:
        return "SOURCE_FIRST_WITH_REMEDIATION"
    if "REFERENCE_ONLY_BLOCKED" in vals:
        return "REFERENCE_ONLY_BLOCKED"
    if "DUPLICATE_OR_SUPERSEDED" in vals:
        return "DUPLICATE_OR_SUPERSEDED"
    return "REFERENCE_ARCHIVE_NO_NEAR_TERM"


def build_features_and_implementations(
    families: list[dict[str, Any]], skills: list[dict[str, Any]], batch1: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    groups: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "families": [], "skills": [], "batch1": [], "statuses": [], "dispositions": [], "evidence": set()
    })
    for f in families:
        for key in f["static_feature_keys"]:
            g = groups[key]
            g["families"].append(f)
            g["statuses"].append(f["biomni_baseline_status"])
            g["dispositions"].append(f["research_disposition"])
            g["evidence"].update(f.get("biomni_baseline_evidence", []))
    for s in skills:
        key = s["provisional_feature_cluster"]
        g = groups[key]
        g["skills"].append(s)
        g["statuses"].append(s["biomni_baseline_status"])
        g["dispositions"].append(s["research_disposition"])
        g["evidence"].update(s.get("biomni_baseline_evidence", []))
    for unit in batch1:
        key = str(pick(unit, "provisional_feature_key", "provisional_feature_cluster", default=""))
        if not key:
            continue
        g = groups[key]
        g["batch1"].append(unit)
        g["statuses"].append(str(unit.get("biomni_baseline_status", "")))
        g["dispositions"].append(str(unit.get("research_disposition", "")))
        g["evidence"].update(unit.get("biomni_baseline_evidence", []) or [])

    features: list[dict[str, Any]] = []
    implementations: list[dict[str, Any]] = []
    feature_ids: dict[str, str] = {}
    sorted_keys = sorted(groups)
    for i, key in enumerate(sorted_keys, 1):
        feature_ids[key] = f"pfeature-{i:06d}"

    for key in sorted_keys:
        g = groups[key]
        rule = RULE_BY_KEY.get(key)
        statement = rule.statement if rule else ""
        if not statement:
            for collection in (g["batch1"], g["skills"], g["families"]):
                if collection:
                    statement = str(pick(collection[0], "capability", "capability_statement", default=key))
                    break
        gap = aggregate_gap(g["statuses"])
        disposition = aggregate_disposition(g["dispositions"])
        base_priority = rule.priority if rule else 50
        score = feature_priority(gap, disposition, len(g["families"]), len(g["skills"]), base_priority)
        priority = "P0" if score >= 90 else "P1" if score >= 75 else "P2" if score >= 55 else "P3"
        features.append({
            "provisional_feature_id": feature_ids[key],
            "feature_key": key,
            "domain": rule.domain if rule else key.split(".", 1)[0],
            "capability_statement": statement,
            "biomni_baseline_status": gap,
            "biomni_baseline_evidence": sorted(g["evidence"]),
            "research_disposition": disposition,
            "priority_score": score,
            "priority": priority,
            "candidate_family_count": len({f["queue_order"] for f in g["families"]}),
            "candidate_family_orders": sorted({f["queue_order"] for f in g["families"]}),
            "sciagent_skill_count": len(g["skills"]),
            "sciagent_skills": [s["skill"] for s in g["skills"]],
            "kdense_kuan_unit_count": len(g["batch1"]),
            "runtime_status": "NOT_EXECUTED_CODEX_REQUIRED",
            "canonical_status": "PROVISIONAL_STATIC_ONLY",
            "publication_review_required": True,
        })

    counter = 0
    for f in families:
        counter += 1
        implementations.append({
            "provisional_implementation_id": f"pimplementation-{counter:06d}",
            "provisional_feature_id": feature_ids[f["primary_feature_key"]],
            "feature_key": f["primary_feature_key"],
            "granularity": "repository_family",
            "source_repository": f["representative_repository"],
            "source_repositories": f["repositories"],
            "repository_ids": f["repository_ids"],
            "queue_order": f["queue_order"],
            "source_head_sha": f["representative_head_sha"],
            "source_status": "REFERENCE_OR_ADAPTATION_CANDIDATE",
            "research_disposition": f["research_disposition"],
            "biomni_baseline_status": f["biomni_baseline_status"],
            "risk_flags": f["risk_flags"],
            "static_depth": f["static_depth"],
            "runtime_status": f["runtime_status"],
            "canonical_status": "PROVISIONAL_STATIC_ONLY",
            "publication_review_required": True,
        })
    for s in skills:
        counter += 1
        implementations.append({
            "provisional_implementation_id": f"pimplementation-{counter:06d}",
            "provisional_feature_id": feature_ids[s["provisional_feature_cluster"]],
            "feature_key": s["provisional_feature_cluster"],
            "granularity": "skill_instruction_implementation",
            "source_repository": s["source_repository"],
            "source_head_sha": s["source_head_sha"],
            "source_path": s["path"],
            "skill": s["skill"],
            "source_change_id": s["source_change_id"],
            "source_status": "REFERENCE_OR_ADAPTATION_CANDIDATE" if s["phase8_candidate"] else "REFERENCE_ARCHIVE",
            "research_disposition": s["research_disposition"],
            "biomni_baseline_status": s["biomni_baseline_status"],
            "primary_issue": s["primary_issue"],
            "runtime_status": s["runtime_status"],
            "canonical_status": "PROVISIONAL_STATIC_ONLY",
            "publication_review_required": bool(s["publication_review_required"]),
        })
    return features, implementations


COMMERCIAL_BEHAVIORS = (
    ("commercial.integrated_biology_environment", "一体化生物学研究工作区，支持规划、编写、执行和协作。", ("workspace.integrated.research", "agent.orchestration.planning_execution")),
    ("commercial.large_tool_catalog", "在统一产品中暴露 300+ 数据库、软件系统和分析工具。", ("tooling.skill.registry_discovery", "integration.database.multi_service_client")),
    ("commercial.free_pro_service_tiers", "提供 Free／Pro 服务层、较高使用限额和并发能力。", ("deployment.cloud_hpc.job",)),
    ("commercial.foundation_model_design", "用自然语言设计 foundation model、pre-training 和 fine-tuning。", ("design.protein.sequence", "agent.orchestration.planning_execution")),
    ("commercial.agent_managed_gpu_training", "Agent 自动配置 GPU、运行、监控、评估和迭代训练。", ("deployment.cloud_hpc.job", "evaluation.benchmark.reproducibility")),
    ("commercial.managed_sandboxes", "创建、删除、列出 sandbox，并在共享存储上分发科学任务。", ("tooling.sandbox.code_execution", "deployment.cloud_hpc.job")),
    ("commercial.esmc_integration", "在聊天工作流中调用 ESMC-6B。", ("design.protein.sequence",)),
    ("commercial.esmfold2_integration", "在聊天工作流中调用 ESMFold2 和快速变体。", ("model.protein.structure_prediction",)),
    ("commercial.boltz_structure_affinity", "调用 Boltz 做结构、亲和力、蛋白/小分子设计和筛选。", ("model.protein.structure_prediction", "analysis.structure.docking_screening")),
    ("commercial.external_agent_mcp", "通过 Biomni MCP 向外部 Agent 暴露 IBE 能力。", ("tooling.mcp.client_server",)),
    ("commercial.desktop_client", "提供或规划桌面端科研入口。", ("workspace.integrated.research",)),
    ("commercial.mobile_client", "提供或规划移动端科研入口。", ("workspace.integrated.research",)),
    ("commercial.autonomous_method_development", "自主搜索和迭代数据与代码，开发无需手写代码的生物学方法。", ("agent.orchestration.planning_execution", "evaluation.benchmark.reproducibility")),
    ("commercial.enterprise_dedicated_infrastructure", "提供 dedicated infrastructure、advanced security 和 own-VPC。", ("governance.security_privacy", "deployment.cloud_hpc.job")),
    ("commercial.custom_agents_priority_support", "为企业提供 custom agents、较高优先级和定制支持。", ("agent.orchestration.multi_agent",)),
    ("commercial.proprietary_data_deployment", "在企业环境中处理专有单细胞、人类遗传和靶点评估数据。", ("analysis.single_cell.qc_integration", "governance.security_privacy")),
    ("commercial.cross_device_everywhere", "以 Biomni Everywhere 形式连接 Agent、Desktop 和 Mobile。", ("workspace.integrated.research", "tooling.mcp.client_server")),
)


def build_commercial_gap(features: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key = {f["feature_key"]: f for f in features}
    rows: list[dict[str, Any]] = []
    for i, (key, behavior, related) in enumerate(COMMERCIAL_BEHAVIORS, 1):
        available = [by_key[k] for k in related if k in by_key]
        if not available:
            status = "COMMERCIAL_BEHAVIOR_WITHOUT_MATCHED_OSS_CLUSTER"
        elif any(f["biomni_baseline_status"] == "BASELINE_EQUIVALENT_PRESENT" for f in available):
            status = "BIOMNI_BASELINE_OR_OSS_EQUIVALENT_PRESENT"
        elif any(f["biomni_baseline_status"] in ("CLEAR_GAP", "PARTIAL_OVERLAP", "RELATED_OVERLAP_NOT_EQUIVALENT") for f in available):
            status = "OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL"
        else:
            status = "STATIC_COMPARISON_INCONCLUSIVE"
        rows.append({
            "commercial_behavior_order": i,
            "commercial_behavior_key": key,
            "behavior": behavior,
            "source": "commercial/discovery-001.md",
            "source_scope": "BOUNDED_OFFICIAL_DISCOVERY",
            "related_feature_keys": list(related),
            "matched_provisional_feature_ids": [f["provisional_feature_id"] for f in available],
            "static_gap_status": status,
            "commercial_internal_implementation": "UNKNOWN",
            "runtime_status": "NOT_APPLICABLE_PUBLIC_BEHAVIOR_ONLY",
        })
    return rows


def build_validation_queue(features: list[dict[str, Any]], implementations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    impl_by_feature: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for impl in implementations:
        impl_by_feature[impl["feature_key"]].append(impl)
    queue: list[dict[str, Any]] = []
    order = 0
    for feature in sorted(features, key=lambda f: (-f["priority_score"], f["feature_key"])):
        order += 1
        impls = impl_by_feature[feature["feature_key"]]
        queue.append({
            "validation_order": order,
            "priority": feature["priority"],
            "priority_score": feature["priority_score"],
            "provisional_feature_id": feature["provisional_feature_id"],
            "feature_key": feature["feature_key"],
            "capability_statement": feature["capability_statement"],
            "biomni_baseline_status": feature["biomni_baseline_status"],
            "research_disposition": feature["research_disposition"],
            "provisional_implementation_ids": [i["provisional_implementation_id"] for i in impls],
            "source_count": len(impls),
            "required_codex_tasks": [
                "freeze exact source SHA and symbols",
                "code-level semantic dedup and Biomni comparison",
                "minimal characterization tests with public or synthetic fixtures",
                "source-to-sink security and privacy analysis",
                "scientific contract and version validation",
                "provenance ledger and modification record",
                "canonical Feature/Implementation decision and JSONL integrity checks",
            ],
            "status": "READY_FOR_CODEX_VALIDATION",
        })
    return queue


def md_table(rows: list[list[Any]], headers: list[str]) -> str:
    def esc(v: Any) -> str:
        return str(v).replace("|", "\\|").replace("\n", " ")
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    lines.extend("| " + " | ".join(esc(v) for v in row) + " |" for row in rows)
    return "\n".join(lines)


def render_feature_catalog(features: list[dict[str, Any]]) -> str:
    domain_counts = Counter(f["domain"] for f in features)
    gap_counts = Counter(f["biomni_baseline_status"] for f in features)
    priority_counts = Counter(f["priority"] for f in features)
    top = sorted(features, key=lambda f: (-f["priority_score"], f["feature_key"]))
    body = [
        "# Current Feature Catalog — Phase 9A static research",
        "",
        "状态：**PROVISIONAL STATIC CATALOG COMPLETE**",
        "",
        "本目录由 Phase 8 的 598 个 `DEEP_AUDIT_CANDIDATE` family、SciAgent 203 个 active Skills、K-Dense／Kuan／BIDS／DataLad 的详细静态拆解和 frozen Biomni baseline 自动归一化生成。",
        "",
        "它不是 runtime-verified catalog。正式 `feature-*` 和 `implementation-*` ID 仍需 Codex 在隔离环境完成代码级去重、测试和 cross-reference 后分配。",
        "",
        "## 汇总",
        "",
        f"- Provisional Features：**{len(features)}**",
        f"- P0／P1／P2／P3：**{priority_counts['P0']}／{priority_counts['P1']}／{priority_counts['P2']}／{priority_counts['P3']}**",
        f"- CLEAR_GAP：**{gap_counts['CLEAR_GAP']}**",
        f"- PARTIAL_OVERLAP：**{gap_counts['PARTIAL_OVERLAP']}**",
        f"- BASELINE_EQUIVALENT_PRESENT：**{gap_counts['BASELINE_EQUIVALENT_PRESENT']}**",
        "",
        "## 领域分布",
        "",
        md_table([[k, v] for k, v in sorted(domain_counts.items())], ["Domain", "Features"]),
        "",
        "## Provisional Feature 列表",
        "",
        md_table(
            [[f["provisional_feature_id"], f["priority"], f["feature_key"], f["biomni_baseline_status"], f["candidate_family_count"], f["sciagent_skill_count"], f["capability_statement"]] for f in top],
            ["ID", "Priority", "Feature key", "Biomni gap", "Families", "SciAgent Skills", "Capability"],
        ),
        "",
        "机器可读版本：`phase-9/provisional-features.jsonl`。",
    ]
    return "\n".join(body)


def render_integration_candidates(features: list[dict[str, Any]]) -> str:
    selected = [f for f in features if f["priority"] in ("P0", "P1") and f["research_disposition"] != "DUPLICATE_OR_SUPERSEDED"]
    rows = []
    for f in sorted(selected, key=lambda x: (-x["priority_score"], x["feature_key"])):
        recommendation = "VALIDATE_AND_ADAPT" if f["research_disposition"] == "SOURCE_FIRST_WITH_REMEDIATION" else "REFERENCE_ONLY_UNTIL_REMEDIATED"
        rows.append([f["priority"], f["feature_key"], f["biomni_baseline_status"], recommendation, f["candidate_family_count"], f["sciagent_skill_count"]])
    return "\n".join([
        "# Integration Candidates — Phase 9A static research",
        "",
        "状态：**STATIC PRIORITIZATION COMPLETE; CODEX VALIDATION REQUIRED**",
        "",
        "本文件只给出研究与验证优先级。它不表示第三方实现已经安全、科学正确或可直接并入生产代码。",
        "",
        f"P0／P1 非重复候选 Feature：**{len(selected)}**。",
        "",
        md_table(rows, ["Priority", "Feature", "Biomni gap", "Recommended next action", "Families", "Skills"]),
        "",
        "详细验证顺序见 `phase-9/codex-phase9-validation-queue.jsonl` 和 `phase-9/CODEX_PHASE9_VALIDATION_QUEUE.md`。",
    ])


def render_commercial(rows: list[dict[str, Any]]) -> str:
    counts = Counter(r["static_gap_status"] for r in rows)
    table = [[r["commercial_behavior_order"], r["commercial_behavior_key"], r["static_gap_status"], ", ".join(r["related_feature_keys"])] for r in rows]
    return "\n".join([
        "# Commercial vs OSS static gap — bounded Phase 9A comparison",
        "",
        "状态：**COMPLETE FOR THE 17 VERIFIED BEHAVIORS IN COMMERCIAL DISCOVERY 001**",
        "",
        "本比较只覆盖已经由官方来源验证的 17 个公开行为。商业内部实现仍为 `UNKNOWN`，产品站点的全局发现也仍是 bounded/partial。",
        "",
        f"- Biomni baseline 或 OSS 等价能力存在：{counts['BIOMNI_BASELINE_OR_OSS_EQUIVALENT_PRESENT']}；",
        f"- OSS 候选存在，但 Biomni 为 gap／partial：{counts['OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL']}；",
        f"- 未匹配到 OSS cluster：{counts['COMMERCIAL_BEHAVIOR_WITHOUT_MATCHED_OSS_CLUSTER']}；",
        f"- 静态比较不确定：{counts['STATIC_COMPARISON_INCONCLUSIVE']}。",
        "",
        md_table(table, ["#", "Commercial behavior", "Static result", "Related Feature keys"]),
        "",
        "机器可读版本：`phase-9/commercial-oss-gap-static.jsonl`。",
    ])


def render_validation_queue(queue: list[dict[str, Any]]) -> str:
    counts = Counter(q["priority"] for q in queue)
    top = queue[:80]
    return "\n".join([
        "# Codex Phase 9 validation queue",
        "",
        "状态：`READY_FOR_LOCAL_CODEX`",
        "",
        "该队列承接已经完成的 Phase 9A 静态调研。不要重跑 Batch 001–046，也不要重新发现 598 个 family。",
        "",
        f"- Validation clusters：{len(queue)}；",
        f"- P0／P1／P2／P3：{counts['P0']}／{counts['P1']}／{counts['P2']}／{counts['P3']}。",
        "",
        "每个 cluster 必须依次完成 exact source freeze、代码级去重、characterization tests、security/privacy/science review、provenance 和 canonical JSONL 校验。",
        "",
        "## 前 80 个验证 cluster",
        "",
        md_table([[q["validation_order"], q["priority"], q["feature_key"], q["biomni_baseline_status"], q["source_count"]] for q in top], ["Order", "Priority", "Feature", "Biomni gap", "Sources"]),
        "",
        "完整机器队列：`codex-phase9-validation-queue.jsonl`。",
    ])


def render_publication_queue(implementations: list[dict[str, Any]]) -> str:
    count = sum(1 for i in implementations if i.get("publication_review_required"))
    return "\n".join([
        "# Publication review queue",
        "",
        "状态：**DEFERRED UNTIL A SMALL RELEASE SET IS SELECTED**",
        "",
        f"当前有 **{count}** 个 provisional implementation 记录带有 publication-review flag。",
        "",
        "Phase 9A 不使用 license 作为功能研究过滤器，但公开论文配套源码、复制代码分发、模型权重、数据和 API terms 必须在最终发布集合确定后逐项审查。",
        "",
        "每项审查至少包含 repository、immutable commit、file/symbol、copied/adapted/rewritten 状态、修改摘要、代码 license、模型 terms、数据 terms、服务 terms 和论文引用。",
    ])


def main() -> None:
    PHASE9.mkdir(parents=True, exist_ok=True)
    tools = extract_baseline_tools()
    families, repo_errors = build_candidate_families(tools)
    skills, skill_errors = build_sciagent(tools)
    batch1 = load_batch1_units()

    candidate_count = len(families)
    skill_count = len(skills)
    skill_candidate_count = sum(1 for s in skills if s["phase8_candidate"])
    if candidate_count != EXPECTED_FAMILIES:
        raise SystemExit(f"expected {EXPECTED_FAMILIES} candidate families, got {candidate_count}")
    if skill_count != EXPECTED_SKILLS:
        raise SystemExit(f"expected {EXPECTED_SKILLS} SciAgent Skills, got {skill_count}")
    if skill_candidate_count != EXPECTED_SKILL_CANDIDATES:
        raise SystemExit(f"expected {EXPECTED_SKILL_CANDIDATES} candidate Skills, got {skill_candidate_count}")

    features, implementations = build_features_and_implementations(families, skills, batch1)
    commercial = build_commercial_gap(features)
    validation_queue = build_validation_queue(features, implementations)

    write_jsonl(PHASE9 / "candidate-family-static-normalization.jsonl", families)
    write_jsonl(PHASE9 / "sciagent-phase9-all-skills.jsonl", skills)
    write_jsonl(PHASE9 / "provisional-features.jsonl", features)
    write_jsonl(PHASE9 / "provisional-implementations.jsonl", implementations)
    write_jsonl(PHASE9 / "commercial-oss-gap-static.jsonl", commercial)
    write_jsonl(PHASE9 / "codex-phase9-validation-queue.jsonl", validation_queue)

    write_text(ROOT / "CURRENT_FEATURE_CATALOG.md", render_feature_catalog(features))
    write_text(ROOT / "INTEGRATION_CANDIDATES.md", render_integration_candidates(features))
    write_text(PHASE9 / "commercial-oss-gap-static.md", render_commercial(commercial))
    write_text(PHASE9 / "CODEX_PHASE9_VALIDATION_QUEUE.md", render_validation_queue(validation_queue))
    write_text(PHASE9 / "PUBLICATION_REVIEW_QUEUE.md", render_publication_queue(implementations))

    family_gap = Counter(f["biomni_baseline_status"] for f in families)
    family_disp = Counter(f["research_disposition"] for f in families)
    skill_disp = Counter(s["research_disposition"] for s in skills)
    feat_gap = Counter(f["biomni_baseline_status"] for f in features)
    feat_priority = Counter(f["priority"] for f in features)
    parse_errors = repo_errors + skill_errors

    completion = f"""# Phase 9A static research completion summary

Completed by bounded repository-evidence analysis.

Status: **COMPLETE_STATIC_RESEARCH**

## Coverage

- Phase 8 external families retained: **2,069 / 2,069**.
- Phase 9 candidate families statically normalized: **{candidate_count} / {EXPECTED_FAMILIES}**.
- SciAgent active Skills assigned a Phase 9 disposition: **{skill_count} / {EXPECTED_SKILLS}**.
- SciAgent source-first candidate Skills: **{skill_candidate_count} / {EXPECTED_SKILL_CANDIDATES}**.
- Provisional Feature clusters: **{len(features)}**.
- Provisional Implementation records: **{len(implementations)}**.
- Commercial behaviors compared against the static OSS catalog: **{len(commercial)} / 17**.
- Codex validation clusters prepared: **{len(validation_queue)}**.
- Third-party runtime executions: **0**.
- Canonical Feature IDs allocated: **0**.
- Canonical Implementation IDs allocated: **0**.

## Family-level static gap distribution

{md_table([[k, v] for k, v in sorted(family_gap.items())], ["Biomni gap", "Families"])}

## Family-level research disposition

{md_table([[k, v] for k, v in sorted(family_disp.items())], ["Disposition", "Families"])}

## SciAgent disposition

{md_table([[k, v] for k, v in sorted(skill_disp.items())], ["Disposition", "Skills"])}

## Provisional Feature distribution

{md_table([[k, v] for k, v in sorted(feat_gap.items())], ["Biomni gap", "Features"])}

Priority: P0 {feat_priority['P0']}, P1 {feat_priority['P1']}, P2 {feat_priority['P2']}, P3 {feat_priority['P3']}.

## Completion boundary

Phase 9A is the complete GPT Pro/static-research layer. It uses existing immutable identity, Change, Lineage, Phase 8 static findings, SciAgent per-Skill audit and the frozen Biomni baseline. It does not claim runtime correctness.

Phase 9B remains Codex-required validation: exact source checkout, symbol-level comparison, characterization tests, scientific validation, source-to-sink security analysis, privacy/data-flow review, provenance ledger, and canonical Feature/Implementation database writes.

## Integrity

- Candidate-family count assertion: passed.
- SciAgent 203/203 assertion: passed.
- SciAgent candidate 125/125 assertion: passed.
- JSONL output generation: passed.
- Parse diagnostics: **{len(parse_errors)}** non-fatal rows/messages; see `phase9-static-generation-diagnostics.json`.
"""
    write_text(PHASE9 / "PHASE9_STATIC_COMPLETION_SUMMARY.md", completion)
    write_text(PHASE9 / "phase9-static-generation-diagnostics.json", json.dumps({
        "candidate_families": candidate_count,
        "sciagent_skills": skill_count,
        "sciagent_candidates": skill_candidate_count,
        "baseline_tools_parsed": len(tools),
        "provisional_features": len(features),
        "provisional_implementations": len(implementations),
        "commercial_behaviors": len(commercial),
        "validation_clusters": len(validation_queue),
        "parse_errors": parse_errors,
    }, ensure_ascii=False, indent=2, sort_keys=True))

    state = f"""# Phase 9 Research State

状态：**PHASE 9A STATIC RESEARCH COMPLETE; PHASE 9B CODEX VALIDATION READY**

生效日期：`2026-08-24`

研究分支：`{BRANCH}`

## Phase 8

- Batch 001–046：完成；
- external families：2,069／2,069；
- queued repository records：2,161／2,161；
- `DEEP_AUDIT_CANDIDATE`：598；
- 第三方代码运行：0。

## Phase 9A 已完成

- 598／598 个 candidate family 完成 family-level static normalization；
- 203／203 个 SciAgent Skill 有 Phase 9 disposition；
- 125／125 个 SciAgent candidate lead 完成静态 Feature cluster 映射；
- K-Dense／Kuan／BIDS／DataLad 的 21 个详细 capability unit 已纳入总目录；
- 形成 {len(features)} 个 provisional Feature cluster；
- 形成 {len(implementations)} 个 provisional Implementation record；
- 17／17 个已验证 commercial behavior 完成 bounded OSS 静态比较；
- 形成 {len(validation_queue)} 个 Codex validation cluster；
- 已生成 `CURRENT_FEATURE_CATALOG.md` 和 `INTEGRATION_CANDIDATES.md`。

## 当前权威产物

1. `phase-9/PHASE9_STATIC_COMPLETION_SUMMARY.md`
2. `CURRENT_FEATURE_CATALOG.md`
3. `INTEGRATION_CANDIDATES.md`
4. `phase-9/provisional-features.jsonl`
5. `phase-9/provisional-implementations.jsonl`
6. `phase-9/candidate-family-static-normalization.jsonl`
7. `phase-9/sciagent-phase9-all-skills.jsonl`
8. `phase-9/commercial-oss-gap-static.md`
9. `phase-9/codex-phase9-validation-queue.jsonl`
10. `phase-9/CODEX_PHASE9_VALIDATION_QUEUE.md`

## Phase 9B 必须由 Codex 完成

- clone/fetch exact source SHA；
- code／symbol／AST／patch-level semantic dedup；
- characterization tests；
- scientific runtime validation；
- source-to-sink security analysis；
- privacy/data-flow validation；
- copied/adapted provenance ledger；
- canonical `features.jsonl` 和 `implementations.jsonl` 写入；
- final JSONL cross-reference 和 repository-integrity audit。

## 解释规则

Phase 9A 的 `COMPLETE_STATIC_RESEARCH` 不等于 runtime verified。Canonical Feature 和 Implementation 仍为 0，直到 Phase 9B 验证门通过。

License 不作为功能研究淘汰条件；科学、安全、隐私、临床、模型和供应链阻断项继续生效。
"""
    write_text(ROOT / "PHASE_9_STATE.md", state)

    coverage = f"""# Phase 9 Coverage

状态：**PHASE 9A COMPLETE; PHASE 9B READY**

## Discovery and static normalization

| Collection | Complete | Total | Status |
|---|---:|---:|---|
| Phase 8 external families | 2,069 | 2,069 | COMPLETE |
| Phase 8 queued repository records | 2,161 | 2,161 | COMPLETE |
| `DEEP_AUDIT_CANDIDATE` families statically normalized | {candidate_count} | {EXPECTED_FAMILIES} | COMPLETE |
| SciAgent active Skills | {skill_count} | {EXPECTED_SKILLS} | COMPLETE |
| SciAgent source-first candidate leads | {skill_candidate_count} | {EXPECTED_SKILL_CANDIDATES} | COMPLETE |
| Verified commercial behaviors statically compared | {len(commercial)} | 17 | COMPLETE_BOUNDED |
| Provisional Feature clusters | {len(features)} | {len(features)} | COMPLETE_STATIC |
| Provisional Implementation records | {len(implementations)} | {len(implementations)} | COMPLETE_STATIC |
| Codex validation clusters prepared | {len(validation_queue)} | {len(validation_queue)} | READY |

## Runtime and canonical validation

| Collection | Complete | Total | Status |
|---|---:|---:|---|
| Third-party runtime executions | 0 | unknown | CODEX_REQUIRED |
| Characterization-tested Feature clusters | 0 | {len(validation_queue)} | CODEX_REQUIRED |
| Scientific runtime validations | 0 | {len(validation_queue)} | CODEX_REQUIRED |
| Security/privacy validations | 0 | {len(validation_queue)} | CODEX_REQUIRED |
| Canonical Features | 0 | unknown | CODEX_REQUIRED |
| Canonical Implementations | 0 | unknown | CODEX_REQUIRED |

## Completion semantics

Phase 9A is complete because every bounded candidate family and every SciAgent Skill now has a deterministic static Feature/disposition record. Phase 9B is a separate execution and canonicalization phase and must not be inferred as complete from static evidence.
"""
    write_text(ROOT / "PHASE_9_COVERAGE.md", coverage)

    master = f"""# Phase 9 Master Index

状态：**PHASE 9A COMPLETE; PHASE 9B READY**

## Authoritative controls

| File | Status | Purpose |
|---|---|---|
| `PHASE_9_STATE.md` | AUTHORITATIVE | 当前阶段和边界 |
| `PHASE_9_COVERAGE.md` | AUTHORITATIVE | 静态覆盖和 Codex 缺口 |
| `phase-9/PHASE9_STATIC_COMPLETION_SUMMARY.md` | COMPLETE | Phase 9A 完成汇总 |
| `CURRENT_FEATURE_CATALOG.md` | COMPLETE_STATIC | provisional Feature 目录 |
| `INTEGRATION_CANDIDATES.md` | COMPLETE_STATIC | 集成研究优先级 |
| `phase-9/CODEX_PHASE9_VALIDATION_QUEUE.md` | READY | Codex cluster 验证入口 |

## Machine-readable outputs

| File | Rows / status |
|---|---:|
| `phase-9/candidate-family-static-normalization.jsonl` | {candidate_count} |
| `phase-9/sciagent-phase9-all-skills.jsonl` | {skill_count} |
| `phase-9/provisional-features.jsonl` | {len(features)} |
| `phase-9/provisional-implementations.jsonl` | {len(implementations)} |
| `phase-9/commercial-oss-gap-static.jsonl` | {len(commercial)} |
| `phase-9/codex-phase9-validation-queue.jsonl` | {len(validation_queue)} |

## Historical evidence retained

Phase 8 Batch 001–046、Change／Lineage／Evidence、旧控制文件和所有 detailed audit reports 继续保留，不重跑、不删除。

## Canonical databases

`database/features.jsonl` 和 `database/implementations.jsonl` 仍为空。只有 Codex 完成 Phase 9B 验证和 cross-reference 后才允许写入正式 ID。
"""
    write_text(ROOT / "PHASE_9_MASTER_INDEX.md", master)

    readme = f"""# Biomni Public Ecosystem Research Database

当前恢复点：**Phase 9A static research complete; Phase 9B Codex validation ready**。

## Read first

1. `PHASE_9_STATE.md`
2. `PHASE_9_COVERAGE.md`
3. `PHASE_9_MASTER_INDEX.md`
4. `phase-9/PHASE9_STATIC_COMPLETION_SUMMARY.md`
5. `CURRENT_FEATURE_CATALOG.md`
6. `INTEGRATION_CANDIDATES.md`
7. `phase-9/CODEX_PHASE9_VALIDATION_QUEUE.md`
8. `RESEARCH_FIRST_OVERRIDE.md`
9. `methodology/research-first-source-policy.md`

## Current counts

- Phase 8 external families：2,069／2,069；
- Phase 9 candidate families statically normalized：{candidate_count}／598；
- SciAgent Skills：{skill_count}／203；
- Provisional Feature clusters：{len(features)}；
- Provisional Implementation records：{len(implementations)}；
- Canonical Feature／Implementation：0／0；
- Third-party runtime executions：0。

Phase 9A 的静态完成不等于 runtime verification。Codex 应从 `phase-9/codex-phase9-validation-queue.jsonl` 开始，不重跑 Batch 001–046。
"""
    write_text(ROOT / "README.md", readme)


if __name__ == "__main__":
    main()
