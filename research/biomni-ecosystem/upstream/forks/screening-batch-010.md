# Public Fork Unique-Change Screening — Batch 010

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 224 branch refs without pagination.
Eleven new branch refs reduced to eight unique SHAs because two pre-commit heads
were shared across forks. All eight unique heads were compared serially and
succeeded. Two exact open-PR heads were not re-compared. One additional cost-1
GraphQL query recovered three complete text blobs omitted from compare patches.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000286 | MoiraClimentGispert/Biomni | User | 34 | 32 | 1 | 1 | PR_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000294 | agutmanstein-scale/Biomni | User | 35 | 32 | 0 | 3 | SUBSTANTIVE_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000281 | shdsadhsadha/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000282 | daishaoxing/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000284 | MrPhil/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000285 | alexandercarlis2-dotcom/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000287 | Schaudge/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000288 | giangtools/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000289 | hchyang/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000397 | 23abdul23/Biomni | User | 35 | 32 | 0 | 3 | SUBSTANTIVE_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000679 | Ali-Maq/Biomni_Replica | User | 2 | 1 | 0 | 1 | DIVERGED_SUBSTANTIVE |
| repo-000732 | aevo98765/Biomni | User | 2 | 1 | 1 | 0 | PR_LINEAGE_ONLY |
| repo-000291 | mountainleaf/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000292 | jtnedoctor/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000293 | m-muqiao/labmate | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000295 | div0-space/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000296 | huseyincavusbi/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000297 | penelopenelope/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000298 | Qanatpharma/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000299 | martinBCCDC/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000300 | AlaiaS/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000302 | sagechant/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000303 | nbahti/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000304 | noelsomdalen/Biomni_2 | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000305 | animesh/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |

Classification counts: DIVERGED_SUBSTANTIVE=1, FORMAT_ONLY=3,
NO_UNIQUE_CHANGE=17, PR_LINEAGE_ONLY=1, PR_LINEAGE_PLUS_FORMAT_ONLY=1,
SUBSTANTIVE_LINEAGE_PLUS_FORMAT_ONLY=2.

## Substantive candidates

### repo-000294 — agutmanstein-scale/Biomni

- `scale-deployment` (six commits) is an exact prefix/subset of
  `model-selector-reasoning` (ten); the latter is the complete observed head.
- Adds a FastAPI MCP-compatible tool/chat server, NDJSON streaming with heartbeats,
  reasoning/tool/result trajectories, pooled ReAct/A1 agents, GPT-5/custom-proxy
  routing, tool-schema sanitization, Docker images, S3/ECR/DevBox workflows, and a
  live-server tool/schema test harness.
- Security: the server binds to `0.0.0.0`, exposes tool and generated Python/R/bash
  execution without visible authentication or authorization, uses broad CORS,
  returns raw reasoning/tool arguments/results, reuses mutable agents and a constant
  thread ID, and exposes environment/path diagnostics. Blocking tool calls occur
  inside async handlers; disconnected streams do not cancel worker threads.
- Deployment scripts transfer broad source trees, export AWS credentials to a
  remote shell, and download executable environment/tool tarballs without hashes,
  signatures, SBOMs, or provenance verification. Scale-specific infrastructure
  identifiers and artifact redistribution require generalization and license review.
- Preliminary type: `FEATURE` / infrastructure and multi-model serving.

### repo-000397 — 23abdul23/Biomni

- `docker_bio` (three commits) is an exact ancestor/subset of `biomni_improve`
  (five). The maximal head reports 220 changed paths, but much of the large diff is
  mode/line-ending or patchless churn; it remains pending full-tree audit.
- Verified text surfaces add Docker setup, prompt budgeting/truncation, compact
  retrieval/config knobs, a prompt-suite runner, and eight read/list tools for
  text, CSV, Excel, PDF, DOCX, biological text, inspection, and directory listing.
- A dedicated GraphQL Blob check recovered the compare-omitted tools as complete
  text. `_safe_path()` expands and resolves arbitrary caller paths but imposes no
  workspace boundary, so the agent can read or enumerate any process-accessible
  file/directory. No write/delete operation is present in that module.
- Security/correctness: the container runs as root, downloads latest Miniforge
  without a checksum, copies the full build context, and starts reload-enabled
  Uvicorn on `0.0.0.0`. Import-time `.env` loading expands ambient trust; the test
  runner auto-approves execution by default and persists full prompts/logs/results;
  character-based prompt truncation can cut schemas or safety instructions.
- Central `a1.py` integration is patch-omitted because of diff size, so advertised
  pause/approval/early-stop behavior is a candidate rather than verified runtime fact.
- Preliminary type: `REFACTOR` / execution and prompt infrastructure.

### repo-000679 — Ali-Maq/Biomni_Replica

- One branch: eight ahead / 466 behind, 134 files, with merge base
  `31d466d0586d8ce16ec3dc130ca7fde4d8608a05`.
- Adds 15 `.claude` Skills, 74 CLI scripts, 13 reference assets, three MCP services,
  an Agent-SDK orchestrator, shared utilities, smoke tests, and extensive hybrid
  Skills+MCP/GPU architecture documentation.
- This is a prototype, not verified scientific functionality. Several GPU model
  services return fixed placeholder values; a CRISPR fallback can generate random
  sequence yet report success; documented MCP tool counts exceed implementations;
  dependency-heavy tests are skipped; and package extras omit imported dependencies.
- Security: the orchestrator grants Bash/Read/Write with `acceptEdits`, encourages
  package installation, launches MCP subprocesses, and exposes an unauthenticated
  GPU HTTP service on `0.0.0.0` with caller-controlled paths. External APIs may
  receive sensitive scientific inputs and often lack timeouts/output limits.
- All eight commits are attributed to the `claude` GitHub account rather than the
  fork owner. The User owner still enters P under the project’s fork-owner boundary,
  but authorship is not reassigned. Code/model/data/API terms remain unresolved.
- Preliminary type: `FEATURE` / Skills and MCP architecture candidate.

## Non-substantive and PR-lineage findings

- Seventeen repositories expose only upstream-known heads.
- MoiraClimentGispert and giangtools share one exact bot-only pre-commit head.
- agutmanstein-scale, div0-space, and animesh share a second exact pre-commit head.
- 23abdul23 has a separate stale one-commit pre-commit branch, nine behind.
- MoiraClimentGispert's other head is exact open PR #288; aevo98765's is exact
  open PR #286. Canonical PR records are reused and no duplicate changes created.

## Identity boundary

- New substantive User owners agutmanstein-scale, 23abdul23, and Ali-Maq enter P.
- MoiraClimentGispert and aevo98765 were already in P as PR authors; their exact
  PR surfaces do not create new person or change IDs.
- Bot-only shared maintenance does not establish owner entry for giangtools,
  div0-space, or animesh.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 224 refs.
- Eight serialized comparisons against frozen main, all successful.
- One authenticated GraphQL Blob query for three complete 23abdul text files.
- Local exact-SHA comparison against upstream, PRs, prior heads, and changes;
  commit-set membership proves the two substantive branch chains.

## Next action

Continue the next bounded active-fork batch. Retain the three changes and two
lineages for security, license, scientific-validity, and feature decomposition.
