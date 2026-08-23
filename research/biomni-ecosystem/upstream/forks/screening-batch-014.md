# Public Fork Unique-Change Screening — Batch 014

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 69 branch refs without pagination.
Eighteen new unique SHAs were compared serially: 15 succeeded and three heads had
no common ancestor with frozen main.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000600 | PMK89/Biomni | User | 11 | 0 | 0 | 11 | DIVERGED_SUBSTANTIVE_DAG_PLUS_UNRELATED |
| repo-000396 | shaneholloman/biomni-agent | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000709 | stanley-fork/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000376 | Niraj288/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000379 | shaileshchaudhary11/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000380 | guoshunhao-creator/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000547 | sszhu/Biomni | User | 2 | 0 | 0 | 2 | DIVERGED_SUBSTANTIVE_DAG |
| repo-000385 | hanlin-yang/BioAiSaaS | User | 33 | 31 | 0 | 2 | DIVERGED_SUBSTANTIVE_PLUS_FORMAT_ONLY |
| repo-000420 | slinnarsson/Biomni | User | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE |
| repo-000381 | BlueOrbit/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000383 | mengsong-econ/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000384 | simon2036/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000386 | yikuide-lab/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000468 | CuriousCaliBoi/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000392 | drgmk/Biomni | User | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE |
| repo-000387 | kimdn/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000388 | cs-shali/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000389 | zhouhr3/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000390 | aslansd/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000393 | ishaniray1/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000394 | cyf08/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000395 | nevergreendd/Biomni | User | 2 | 2 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000398 | scarlet46/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000399 | anirisaihan/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000401 | mmetalab/Biomni_Drug | User | 1 | 0 | 0 | 1 | NOTEBOOK_ONLY |

Classification counts: DIVERGED_SUBSTANTIVE=2,
DIVERGED_SUBSTANTIVE_DAG=1, DIVERGED_SUBSTANTIVE_DAG_PLUS_UNRELATED=1,
DIVERGED_SUBSTANTIVE_PLUS_FORMAT_ONLY=1, NOTEBOOK_ONLY=1,
NO_UNIQUE_CHANGE=19.

## Substantive candidates

### repo-000600 — PMK89/Biomni

- The comparable UI/OSP family forms a 48-commit union over seven heads.
  `main` is contained in OSP/tool/docker and `branchcombined`; several OSP heads
  retain side commits, so no single observed head contains the full union.
- `branchcombined` also contains the recoverable 22-commit Amine history even
  though direct comparisons of `amine-branch` and `amine-pmk` have no common
  ancestor. `ui_tool` remains opaque/no-common-ancestor.
- A separate `esqlabs_tools_integration` branch is a disjoint 19-commit lineage.
  It adds a second app/package, per-user/chat files, file explorer, literature
  downloads, PBPK workflow, PK-Sim/OSPSuite-R execution, source annotations,
  multi-turn behavior, and tests.
- Critical security/privacy findings across the families include fail-open Entra
  auth, public default session key, trusted proxy-header spoofing, unauthenticated
  uploads or complete ESQ app, collapse to `default_user`, stored XSS via
  `innerHTML`, global mutable agents/stdout/chat paths, plaintext prompts/thoughts,
  arbitrary-path downloads/writes, SSRF, zip/delete hazards, and exposed tool/code
  execution. No head is integration-ready.
- PBPK/snapshot success is scientifically unsafe: placeholder parameters, stale or
  broadly matched outputs, file existence treated as validity, weak units/provenance/
  solver checks, and self-generated attribution markers can yield plausible but
  invalid simulations. Binary models, snapshots, datasets, full text, and PK-Sim/
  OSPSuite terms require provenance/license review.
- Owner attribution is mixed with Max Koenig and Mohamed Amine Kina; their work is
  not reassigned to PMK89.

### repo-000547 — sszhu/Biomni

- `conda_r` and `main` share nine commits and retain two versus one side commits,
  producing a 12-commit union. Both are 9 behind.
- Adds IAM/default-chain Bedrock setup, an unwired client manager, micromamba+uv
  environment migration, dependency/runtime tests, and cloud backup/restore.
  `conda_r` moves more R/Python packages to conda but setup still force-installs
  NumPy through uv, undercutting claimed reproducibility.
- Critical risks: `curl | sh`, TLS-verification fallbacks, mutable VCS dependencies,
  mixed/unpinned channels, tolerated partial installs, persistent shell changes,
  and unsafe remote tar extraction without member/symlink/digest checks. Backup
  captures all `data` directories to ambient cloud credentials without PHI/genomic
  exclusions, client-side encryption, or retention policy.
- Bedrock IAM is directionally safer than bearer tokens, but advertised centralized
  retry/config logic is not wired into `get_llm`; account/ARN logging and role scope
  require review.

### repo-000385 — hanlin-yang/BioAiSaaS

- `main`: seven ahead / nine behind, 50 files. Adds Pylint CI, frontend guides,
  broad Biomni→BioAiSaaS replacement, and references to an external Lovable UI.
- No frontend implementation is present. Renamed imports/package commands/assets,
  S3 paths, endpoints, and `bioaisaas` package do not exist in the diff; the head is
  statically non-runnable and claims unsupported capabilities.
- Rebranding alters citation/project attribution and removes Stanford references.
  Public Codespace/CORS advice is especially risky because the backend executes
  generated code with broad privileges and retains a guessable access code.
  External frontend rights and generated/rebranded content require review.
- A separate pre-commit branch is bot-only maintenance.
- Preliminary type: `REFACTOR` / broken rebrand candidate.

### repo-000420 — slinnarsson/Biomni

- Six ahead / 19 behind, 12 files. Adds an ARM64 Anaconda Docker image and an
  unauthenticated FastAPI streaming adapter while removing OpenMM/PyStan support.
- Any network caller can select provider/model and invoke a tool/code-capable A1.
  There is no auth, tenant/rate/cost isolation, TLS, request bound, or tool limit;
  production uses reload and builds a new expensive agent per request.
- `COPY .` lacks a visible `.dockerignore`; build-time data download can embed
  secrets or restricted datasets in image layers. Unverified Anaconda/uv installers,
  mutable dependencies, root image layers, and ARM64-only artifacts add supply-
  chain and redistribution risk. Capability degradation is not surfaced safely.
- Preliminary type: `ENVIRONMENT` / HTTP adapter.

### repo-000392 — drgmk/Biomni

- Ten ahead / nine behind, 11 files. Replaces the environment/resource catalog with
  an scRNA-oriented subset, adds QC/clustering guides, environment splits, and
  package/CLI/R checks.
- Guides contain broken names/APIs, fragile universal thresholds, scaling before
  HVG selection, automatic Harmony advice, non-reproducible/partial tests, missing
  dependencies, and inconsistent environment claims. Wholesale resource removal is
  not integration-ready.
- PATH-based binary tests and dynamic imports execute discovered code; mixed
  unpinned conda/pip/R stacks are weakly reproducible. Cell-level, receptor, sample,
  and clinical metadata lack privacy guidance. Guide CC BY attribution does not
  resolve dependency/database terms.
- Preliminary type: `ENVIRONMENT` / scRNA specialization.

## Non-substantive findings

- Nineteen repositories expose only upstream-known heads.
- mmetalab adds one exploratory notebook only. Its stored run fails on Gradio API
  incompatibility, leaks a local path in traceback, and performs no drug analysis.
- hanlin-yang's second head is a bot-only pre-commit update.
- PMK `amine-branch`, `amine-pmk`, and `ui_tool` return no-common-ancestor; the first
  two are only related through ancestry recovered from `branchcombined`.

## Identity boundary

- New substantive User owners PMK89, sszhu, hanlin-yang, slinnarsson, and drgmk
  enter P. Mixed contributors and bot commits retain their own attribution.
- mmetalab's only unique change is a notebook; Organization-only/upstream-only
  surfaces do not add people.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 69 refs.
- Eighteen serialized comparisons: 15 successful and three no-common-ancestor.
- Local commit-set analysis establishes the 48-commit PMK UI/OSP union, independent
  19-commit ESQlabs line, and 12-commit sszhu branch union.

## Next action

Continue the next bounded active-fork batch. Retain six changes and two lineages
for full-tree, security, license, scientific-validity, and feature decomposition.
