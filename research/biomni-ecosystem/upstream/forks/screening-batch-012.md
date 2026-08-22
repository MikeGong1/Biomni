# Public Fork Unique-Change Screening — Batch 012

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 67 branch refs without pagination.
Nine new unique SHAs were compared serially and all succeeded. Three exact PR
heads and one previously screened formatting head were not re-compared.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000333 | psknlr/Biomni | User | 2 | 1 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000325 | randomrisk/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000326 | kedarkolluri-tw/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000327 | ProximaMonkey/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000329 | stevenWZ/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000330 | datnoor/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000334 | IMPF-AI/BiomniV2 | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000338 | Rakshitha-Ireddi/Biomni | User | 2 | 1 | 1 | 0 | PR_LINEAGE_ONLY |
| repo-000342 | vb-dbrks/Biomni-on-dbrks | User | 2 | 2 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000335 | vidhidhaduk05/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000336 | aurora-bio/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000337 | yenklabs/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000339 | jhjeonkaist/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000340 | yzjie6/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000341 | MPebworthEpana/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000343 | asdfefbhjy/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY_REUSED |
| repo-000344 | Aether-Saint/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000346 | Paraschamoli/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000351 | katalyzeAI/Biomni | Organization | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000361 | Pidem/Biomni | User | 2 | 2 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000473 | jay2610/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000541 | MinxZ/dleader_agent | User | 4 | 0 | 1 | 3 | DIVERGED_SUBSTANTIVE_LINEAGE_PLUS_PR |
| repo-000372 | CiaranMccarthy1/Biomni-neuroscience | User | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000565 | Edison-A-N/Biomni | User | 4 | 1 | 0 | 3 | SUBSTANTIVE_MULTI_BRANCH |
| repo-000369 | yaswanth169/Biomni | User | 1 | 0 | 1 | 0 | PR_LINEAGE_ONLY |

Classification counts: DIVERGED_SUBSTANTIVE_LINEAGE_PLUS_PR=1,
FORMAT_ONLY_REUSED=1, NO_UNIQUE_CHANGE=17, PR_LINEAGE_ONLY=2,
SUBSTANTIVE_MULTI_BRANCH=1, SUBSTANTIVE_UNIQUE=3.

## Substantive candidates

### repo-000333 — psknlr/Biomni

- One commit, one file, 0 behind. The Custom/OpenAI-compatible GPT-5 path strips
  unsupported `stop` and `temperature` fields from the outgoing request payload.
- This is a narrow compatibility fix, but detection depends on the model string
  starting with `gpt-5`; arbitrary Azure deployment names still take the old path.
  No Azure auth/API-version behavior or targeted tests are added.
- The commit is attributed to the `claude` account, not the fork owner. Owner entry
  into P does not alter authorship.
- Preliminary type: `BUG_FIX`.

### repo-000351 — katalyzeAI/Biomni

- Six commits, 37 files, 0 behind. Adds Docker, an internal FastAPI invoke/stream
  service, AWS ECS Fargate/EBS/ECR/Secrets Manager/Terraform deployment, and a
  Tailscale subnet router.
- Security: API and Gradio rely on network/Tailscale placement rather than app
  authentication. Tailnet or VPC callers can invoke a code-executing agent using
  service credentials; the data volume is read-write, egress is unrestricted,
  full steps/errors can be returned, and rate/tenant/request controls are absent.
- Secret values passed to Terraform secret versions remain in Terraform state;
  the active backend is local. Placeholder values plus `ignore_changes` complicate
  rotation. Internal HTTP remains possible after Tailscale terminates at the router.
- Deployment correctness is unverified: snapshot creation lacks a usable instance
  profile/robust NVMe handling and command polling, uses fixed sleeps, and can
  snapshot incomplete data. Tailscale uses `curl | sh`; images, AMIs, packages,
  ECR tags, and data artifacts are mutable or lack provenance/SBOM/license review.
- The owner is an Organization and does not enter P.
- Preliminary type: `ENVIRONMENT` / cloud infrastructure.

### repo-000541 — MinxZ/dleader_agent

- Three heads form a 103-commit DAG. `gradio-test` (14 commits) is contained in
  `image_agent` (100). Historical `main` has an overlapping five-commit stem plus
  three side commits. The exact preprocessing PR #155 is contained in both
  developed branches and is not duplicated as a new change.
- Post-PR work adds QSPR/AutoML preprocessing/modeling and Gradio workflows.
  `image_agent` expands into a multi-user FastAPI/Gradio product with queues,
  sessions, S3/Mongo hybrid storage, sharing/deletion/ZIP, templates/meta-agent,
  PDF/image reports, RNA/Modal integrations, and large package reorganization.
- GitHub returned exactly its 300-file compare cap for `image_agent`; the observed
  310-file union is incomplete and implementation claims remain pending full-tree
  audit. The branch is 233 behind.
- High risks include unauthenticated/IDOR-prone user/session APIs, wildcard CORS,
  public shares/direct artifact URLs, path/ZIP/symlink handling, pickle/joblib model
  loading, stale local/S3/Mongo copies, unconstrained queues/uploads/model fitting,
  and extensive PHI/genomic data and external-service exposure.
- Scientific defects include broken fold-scaler persistence, averaging class labels,
  non-stratified/random chemical CV, hard-label ROC AUC, preprocessing leakage, and
  strong ASO claims without experimental/genome-wide validation. Package/data/model
  provenance and upstream attribution require deep review. No head is canonical.
- Preliminary type: `FEATURE` / product and scientific-workflow lineage.

### repo-000372 — CiaranMccarthy1/Biomni-neuroscience

- One commit, five files, 0 behind. Adds spike-train and calcium analysis, synthetic
  spike generation, Allen Brain Atlas metadata, and three evaluation tasks.
- Critical integration defect: `biomni/task/__init__.py` imports `.neuro_eval`, but
  the added module is `biomni/tool/neuro_eval.py`; importing the task package fails.
- Allen queries use plaintext HTTP and live, non-reproducible ground truth. Other
  scientific concerns include fragile dF/F baselines, undercounted bursts, exact-
  equality evaluation despite tolerance comments, unreliable transposition,
  time-seeded evaluation, empty feature indexing, and incomplete tool registration.
  The commit also changes the global default model to vague `gemini`.
- Preliminary type: `FEATURE` / neuroscience tools and benchmark candidate.

### repo-000565 — Edison-A-N/Biomni

- Two sibling textification branches share merge base `b5ad0c7b...` but no feature
  commits. The recursive branch formats nested object/array fields; the later
  two-commit branch prints raw `properties`/`items` dictionaries. They are
  `alternative_to`, not duplicates or a proven supersession.
- Recursive formatting is richer but misses top-level arrays and schema constructs;
  raw dictionaries cover top-level fields but are noisy and can amplify huge or
  adversarial schema text. Both require redesign/tests before integration.
- A separate five-commit branch adds an OpenAI-shaped FastAPI streaming server.
  It uses only the last user message, ignores conversation/tool semantics, counts
  characters as tokens, blocks async workers with synchronous agent calls, and
  overstates OpenAI compatibility.
- The server binds to `0.0.0.0` with reload, no auth/TLS/rate/concurrency/resource
  isolation, and exposes a code-capable agent plus configured MCP tools. Anonymous
  callers could trigger costly execution with filesystem/network/credential access.
  Biomedical privacy, cancellation, retention, dependency, and image provenance
  remain unreviewed.
- Edison-A-N was already in P; fork relations are appended without a new person.
- Preliminary types: two textification changes and one `FEATURE` server change.

## Non-substantive and PR-lineage findings

- Seventeen repositories expose only upstream-known heads.
- asdfefbhjy exposes one exact previously screened pre-commit formatting head.
- Rakshitha-Ireddi's distinct branch is exact open PR #281.
- MinxZ's preprocessing branch is exact closed-unmerged PR #155.
- yaswanth169's sole branch is exact open PR #278.

## Identity boundary

- New substantive User owners psknlr and CiaranMccarthy1 enter P.
- MinxZ and Edison-A-N were already in P as contributors/PR authors; fork relations
  are merged into their existing identities.
- katalyzeAI is an Organization. Exact PR or reused formatting surfaces do not add
  new person identities.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 67 refs.
- Nine serialized comparisons against frozen main, all successful.
- Local exact-SHA, commit-set, PR inclusion, file-union, and patch analysis proves
  the Minx DAG and Edison alternative implementations.

## Next action

Continue the next bounded active-fork batch. Retain seven changes and two lineages
for full-tree, security, license, scientific-validity, and feature decomposition.
