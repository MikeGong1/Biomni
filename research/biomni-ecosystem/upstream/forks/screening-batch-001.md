# Public Fork Unique-Change Screening — Batch 001

Parent verification: `VERIFIED`. Scope is the newest 25 REST-discovered forks
(`repo-000093`–`repo-000117`). One serialized GraphQL query returned all 268
public branch refs with no ref pagination. Branch-head OIDs were compared locally
against all upstream branch/DAG commits; only seven unique non-PR heads required
serialized REST compare requests.

## Coverage and classifications

| Repository ID | Fork | Branches | Upstream-known heads | Exact PR heads | Other unique heads | Screening status |
|---|---|---:|---:|---:|---:|---|
| repo-000093 | kdh4win4/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000094 | MikeGong1/Biomni | 35 | 33 | 0 | 2 | SUBSTANTIVE_UNIQUE |
| repo-000095 | alina-2024/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000096 | gungwang/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000097 | vectorpikachu/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000098 | xero-dotcom/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000099 | Cell-Tool/Biomni-LSA-OS | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000100 | palimisis/Biomni | 1 | 0 | 0 | 1 | NON_FEATURE_UTILITY |
| repo-000101 | DotWasi/Biomni | 33 | 33 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000102 | QING1105/Biomni | 38 | 33 | 5 | 0 | PR_LINEAGE_ONLY |
| repo-000103 | tonesky/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000104 | reacher-z/Biomni | 42 | 33 | 9 | 0 | PR_LINEAGE_ONLY |
| repo-000105 | Irishaze/Biomni | 34 | 33 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000106 | DawnyWu/Biomni | 2 | 1 | 0 | 1 | DOC_ONLY |
| repo-000107 | mohsin-shaikh/Biomni | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000108 | Mr-Milk/Biomni | 34 | 32 | 1 | 1 | PR_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000109 | 0xYeah/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000110 | PayFv/Biomni | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000111 | kekropian/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000112 | competition-W/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000113 | emmm114/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000114 | febright2025/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000115 | fzxz000/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000116 | jianjingkuang/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000117 | chenwgm-eng/Biomni | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: DOC_ONLY=1, FORMAT_ONLY=1, NON_FEATURE_UTILITY=1, NO_UNIQUE_CHANGE=16, PR_LINEAGE_ONLY=2, PR_LINEAGE_PLUS_FORMAT_ONLY=1, SUBSTANTIVE_UNIQUE=3.

## Substantive unique candidates

### repo-000094 — MikeGong1/Biomni

- `integration/codex-chatgpt-work-mcp`: 17 commits, six files, 0 behind.
- Adds official-data-lake manifests/transfer workflows and a BindingDB runtime
  recovery workflow. The separate research branch changes only research records.
- Security/operations: GitHub Actions perform external downloads, parallel jobs,
  and artifact uploads; provenance, data terms, artifact retention, and supply
  chain behavior require deep review.
- Preliminary type: `ENVIRONMENT` / scientific infrastructure.

### repo-000105 — Irishaze/Biomni

- `add-vascular-biomaterials-tool`: two commits, four files, 0 behind.
- Adds a 628-line vascular-biomaterials module plus four exposed tool schemas:
  scaffold degradation kinetics, graft compliance/safety, thrombosis-risk
  estimation, and multilayer graft design reporting.
- Includes a follow-up 100x compliance unit-conversion fix. Scientific validity,
  simplified-model assumptions, tests, and component licenses require deep audit.
- Preliminary type: `FEATURE`.

### repo-000110 — PayFv/Biomni

- `main`: one commit, ten files, 0 behind.
- Adds a FastAPI plan/step job API, on-disk session/result store, runtime, and
  launch script for external orchestration such as Mastra.
- Security: launch defaults to `0.0.0.0`; no authentication/authorization is
  visible in the added API surface, while agent execution and session files are
  exposed. Treat as high-risk until threat-modelled.
- Preliminary type: `FEATURE` / infrastructure.

## Non-feature and lineage findings

- `palimisis/Biomni`: one 13-line personal data-fetch helper that reuses existing
  S3 download utilities; retained as `NON_FEATURE_UTILITY`.
- `DawnyWu/Biomni`: four Chinese architecture/ecosystem notes only (`DOC_ONLY`).
- `mohsin-shaikh/Biomni` and `Mr-Milk/Biomni` share exact head
  `1f67177642eb488a57ac103147013ac3a6ec65ba`, a pre-commit update/format patch.
- QING1105 and reacher-z unknown heads map exactly to existing open or
  closed-unmerged PR heads; no duplicate change IDs are created.
- Sixteen repositories expose only upstream-known branch heads.

## Evidence

- GraphQL branch inventory response cached from one authenticated, cost-1 request.
- Seven serialized compare responses against frozen main, all with merge base
  `400c1f366b96a35ca253e13c9b06c5076af41d65`.
- Canonical PR-head mappings: `upstream/prs/open-inventory.md` and
  `upstream/prs/closed-unmerged-inventory.md`.

## Next action

Deep-audit the three substantive unique changes; continue screening the next
bounded fork batch without adding owners unless substantive uniqueness is proven.
