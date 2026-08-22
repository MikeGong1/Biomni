# Public Fork Unique-Change Screening — Batch 011

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 96 branch refs without pagination.
Ten new unique SHAs were compared serially and all succeeded. Three exact open-PR
heads were not re-compared.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000306 | robertpark1228/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000307 | informationsea/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000308 | pravalika5/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000309 | Jiadalee/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000310 | sunxinti/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000311 | erima2020/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000312 | AndreRui/biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000313 | sg3451/Biomni_AI_code | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000314 | lakshmikc/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000315 | Noone-Dash/biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000316 | ddunun/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000317 | Zhao-Xiaodan/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000350 | goodb/Biomni | User | 34 | 32 | 1 | 1 | PR_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000719 | amanapte/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000332 | larryinx/Biomni | User | 2 | 0 | 0 | 2 | SUBSTANTIVE_LINEAGE |
| repo-000319 | ghar1821/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000320 | HealthVivo/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000321 | jxshi/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000322 | 3280069445/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000323 | Beifang/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000324 | Charles1DENG/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000348 | llmsc-security-test/Biomni | Organization | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000391 | andrewsu/Biomni | User | 5 | 0 | 2 | 3 | SUBSTANTIVE_PATCH_DEDUP_PLUS_PR_LINEAGES |
| repo-000328 | ZN-Sellena2000/Biomni | User | 33 | 31 | 0 | 2 | SUBSTANTIVE_PLUS_FORMAT_ONLY |
| repo-000400 | chaudhariatul/Biomni | User | 2 | 1 | 0 | 1 | DIVERGED_SUBSTANTIVE |

Classification counts: DIVERGED_SUBSTANTIVE=1, NO_UNIQUE_CHANGE=19,
PR_LINEAGE_PLUS_FORMAT_ONLY=1, SUBSTANTIVE_LINEAGE=1,
SUBSTANTIVE_PATCH_DEDUP_PLUS_PR_LINEAGES=1, SUBSTANTIVE_PLUS_FORMAT_ONLY=1,
SUBSTANTIVE_UNIQUE=1.

## Substantive candidates

### repo-000332 — larryinx/Biomni

- `virtual-organ-tool` (three commits) is a strict subset of `main` (five).
  The maximal head adds PrimeKG entity/neighborhood/path queries, DeepDR molecule
  ranking, SQLite wet-lab result CRUD, pinned environment snapshots, and
  Docker/Apptainer packaging.
- Critical blocker: the Anthropic path hard-codes a non-provider plaintext HTTP
  proxy. Prompts, research data, and likely authorization material can therefore
  be redirected to a fixed third party without transport security. No part of
  this lineage is integration-ready until that behavior is removed and audited.
- Other security/privacy risks include arbitrary local CSV/SQLite/model/config
  paths, dynamic import and invocation of a configured scoring callable, plaintext
  sample/operator/instrument records, agent-callable update/delete, unbounded graph
  caching, and root container execution.
- Scientific validity is unverified: DeepDR interfaces are guessed, scores lack
  provenance/calibration/uncertainty controls, PrimeKG identifiers may collapse
  across entity types, graph traversal reverses directed edges, and wet-lab values,
  units, replicates, and timestamps are weakly validated. No focused tests exist.
- The substantive commits are attributed to `xinwuye`, not the fork owner. The
  User owner enters P by the project’s fork-owner boundary without reassignment of
  commit authorship.
- Preliminary type: `FEATURE` / virtual-organ data and workflow tooling.

### repo-000348 — llmsc-security-test/Biomni

- `main`: two commits, six added files, 0 behind. Adds non-root Docker packaging,
  Gradio and alternate MCP entrypoints, lifecycle scripts, dependencies, and a
  tutorial/probe client; no new scientific algorithm is present.
- Runtime wiring is internally inconsistent: Docker selects the Gradio entrypoint
  on port 7860 while the invocation script publishes 11260 as an MCP service. The
  alternate MCP entrypoint is not selected by the Dockerfile.
- Both Gradio and the alternate MCP path bind to `0.0.0.0` without visible auth or
  TLS. Gradio disables verification and exposes a code-capable agent; the MCP path
  exposes database tools. Dependencies are largely unpinned and no hashes/SBOM are
  supplied. The tutorial conflates HTTP and stdio transports and is not reliable
  validation.
- The owner is an Organization and does not enter P.
- Preliminary type: `ENVIRONMENT`.

### repo-000391 — andrewsu/Biomni

- `add-phewas-tool`: one commit adding `query_phewas`, batch querying, and tool
  schemas for the BioThings PheWAS service.
- `feature/add-mygene-query-tool` and `main` have different commit SHAs but the
  same parent, tree SHA, file blobs, patches, message, author, and author time.
  They are one MyGene change with two exact patch-equivalent surfaces.
- PheWAS accepts caller/LLM-generated endpoints without host/scheme validation,
  creating SSRF risk; its REST helper lacks a timeout and it conditionally unpickles
  a local schema. Natural-language clinical/genetic prompts leave the process for
  an LLM and public API. Scientific associations must not be interpreted as causal
  or clinical recommendations.
- MyGene is lower risk but exports identifiers/symbols, accepts unbounded batches,
  returns raw upstream content, exposes exception text, and adds an external API/
  dependency whose terms and aggregated annotations require review.
- Exact PR branches #276 and #277 are retained separately as canonical PR lineages.
  The owner was already in P; its fork relations are appended without a new person.
- Preliminary types: two `FEATURE` changes.

### repo-000328 — ZN-Sellena2000/Biomni

- `main`: one commit, three files, 0 behind. Adds optional callback handlers to
  `go()` and `go_stream()` for tracing/observability, rebrands prompts as “Aigen
  R0,” and adds tool-selection explanation instructions.
- Callbacks can receive prompts, model messages, tool arguments/results, and
  biomedical data; no privacy/redaction policy accompanies the feature. Prompt
  rebranding and duplicated explanation instructions may alter behavior and are
  not independently valuable.
- A separate two-commit pre-commit branch is maintenance/format-only.
- Preliminary type: `FEATURE` / observability callback support.

### repo-000400 — chaudhariatul/Biomni

- `dev-branch-20260218-172116`: one commit, two files, 1 ahead / 9 behind.
- Adds Amazon Nova Lite v2 Bedrock routing via `ChatBedrockConverse`, reasoning
  controls, and a 16,000-token default reasoning budget, while changing global
  defaults from Claude/auto-source to Nova/Bedrock.
- Risks: a paid external provider becomes the default; AWS region silently defaults
  to `us-east-1`; non-Bedrock model overrides can be misrouted unless source is also
  changed; reasoning budgets are unbounded; and the exact request schema/model
  availability is runtime-unverified. Cost, privacy, data residency, and nine-
  commit divergence require review.
- The commit is attributed to `kiro-agent`, not the fork owner. Owner entry into P
  does not change commit attribution.
- Preliminary type: `FEATURE` / model-provider integration.

## Non-substantive and PR-lineage findings

- Nineteen repositories expose only upstream-known heads.
- goodb's new head is a one-commit pre-commit version bump; its other distinct head
  is exact open PR #280.
- ZN-Sellena2000's second head is a bot-only dependency/format branch.
- andrewsu's `biothings_tools` and lazy-import branches are exact open PR #277 and
  #276; no duplicate changes are allocated for those surfaces.

## Identity boundary

- New substantive User owners larryinx, ZN-Sellena2000, and chaudhariatul enter P.
- andrewsu was already in P as a contributor/PR author; its fork relationship is
  appended to the existing identity.
- llmsc-security-test and HealthVivo are Organizations. goodb's only non-PR unique
  head is maintenance and does not create a new person relationship.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 96 refs.
- Ten serialized comparisons against frozen main, all successful.
- Local exact-SHA and final-tree comparison against upstream, PRs, prior heads,
  and canonical changes; this proves the larry chain and MyGene patch equivalence.

## Next action

Continue the next bounded active-fork batch. Retain six changes and two lineages
for security, license, scientific-validity, and feature decomposition.
