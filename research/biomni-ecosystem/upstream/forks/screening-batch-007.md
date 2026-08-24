# Public Fork Unique-Change Screening — Batch 007

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 60 branch refs without pagination. Five
new heads were compared serially; exact open PR #293 and #299 heads were not
re-compared.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000222 | Patiskey/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000249 | SongyouZhong/Biomni-Agent | User | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000223 | kingopps/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000224 | antass/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000225 | xinh03/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000226 | beiyongGit/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000318 | DevinDeSilva/Biomni | User | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000227 | r-siddiqi/Biomni | User | 2 | 1 | 1 | 0 | PR_LINEAGE_ONLY |
| repo-000444 | Vincentcchu/Biomni | User | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000745 | matheus-rech/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000228 | nine-sarayut/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000229 | MengQiuchen/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000230 | crazysummerW/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000231 | Adyavasaaya/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000268 | yohyoh-wang/Biomni | User | 2 | 1 | 1 | 0 | PR_LINEAGE_ONLY |
| repo-000234 | averyself/Biomni | User | 2 | 1 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000694 | M-Hakmi/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000232 | mbrues/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000233 | shangyugong/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000235 | YangXu32/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000236 | milliomics/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000237 | github-dongpyo/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000238 | SalinaW/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000239 | YingjieQu/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000240 | er-hanlhn/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: FORMAT_ONLY=1, NO_UNIQUE_CHANGE=18,
PR_LINEAGE_ONLY=2, SUBSTANTIVE_UNIQUE=4.

## Substantive unique candidates

### repo-000249 — SongyouZhong/Biomni-Agent

- `main`: one commit, 26 files, 0 behind.
- Adds a FastAPI REST/WebSocket agent gateway, a separate Python-execution
  service, container/runtime manifests, clients, tests, and architecture notes.
  Existing REPL and lab-automation execution is redirected to the new service.
- Security: both services bind to `0.0.0.0`; no authentication or authorization
  is visible; request fields can set path, model endpoint, and API key; the
  execution service accepts arbitrary Python and keeps a process-global namespace.
  Container and network isolation claims therefore require adversarial review.
- Preliminary type: `FEATURE` / execution infrastructure.

### repo-000318 — DevinDeSilva/Biomni

- `main`: four commits, 12 files, 0 behind.
- Instruments system-prompt construction, LLM generation, tool execution, and
  critique stages with a provenance graph layer backed by `expl_annotator`, and
  persists provenance after agent runs.
- The patch also removes `pyproject.toml` and commits PDFs/configuration artifacts.
  Runtime coupling, captured-data sensitivity, dependency licensing, and graph
  correctness require deep review.
- Preliminary type: `FEATURE` / observability.

### repo-000444 — Vincentcchu/Biomni

- `main`: three commits, 58 files, 0 behind.
- Adds per-stage LLM token/cost accounting, callback propagation, run-metric JSON
  export, and a batch single-cell annotation workflow with result cleanup.
- The same head commits notebooks, figures, local-path outputs, and a large
  environment/tool snapshot containing binaries and third-party data. Capability
  code must be separated from generated artifacts; supply-chain, data provenance,
  fixed price assumptions, and privacy exposure require deep review.
- Preliminary type: `FEATURE` / observability and workflow automation.

### repo-000234 — averyself/Biomni

- `gh200-optimized`: one commit, 27 files, 0 behind.
- Adds staged Linux aarch64/GH200 environments, llama.cpp reasoning-message
  compatibility, a Tavily/Google model-agnostic web-search path, and related
  documentation and agent robustness changes.
- Architecture-specific package availability, external scraping behavior,
  committed benchmark datasets, dependencies, and licenses require deep review.
- Preliminary type: `ENVIRONMENT` / model-runtime compatibility.

## Non-substantive and lineage findings

- Eighteen repositories expose only upstream-known heads.
- beiyongGit has one two-commit pre-commit autoupdate/format branch.
- r-siddiqi's distinct branch is exact open PR #299; yohyoh-wang's is exact open
  PR #293. Canonical PR records are reused and no duplicate change IDs are made.

## Identity boundary

- The four User owners with substantive unique changes enter P.
- beiyongGit is excluded because the only unique change is automated formatting.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 60 refs.
- Five serialized compare responses against frozen main, all with merge base
  `400c1f366b96a35ca253e13c9b06c5076af41d65`.
- Canonical open-PR head mapping for #293 and #299.

## Next action

Continue the next bounded active-fork batch while retaining these four candidates
for later security, license, feature-decomposition, and integration audits.
