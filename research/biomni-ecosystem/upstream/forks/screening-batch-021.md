# Public Fork Unique-Change Screening — Batch 021

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query returned all 59 branch
refs without pagination. Local precedence-aware resolution found 49 upstream
heads, three exact PR heads, three previously screened heads, and four new SHAs.
Four serialized comparisons succeeded; the largest was four commits and six files,
so no compare pagination or omitted-text retrieval was required. No fork source,
script, model, dependency, network endpoint, or test was executed.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000553 | Sanat-Mishra/Biomni_Dev | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_BROKEN_PARSER_SELF_CRITIC_REGRESSION |
| repo-000552 | neurogenia/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000554 | adibgpt/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000567 | Rasic2/Biomni | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_AZURE_MCP_SUPERVISOR_PROTOTYPE |
| repo-000583 | thesteganos/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000558 | hubahu/Biomni_GuiY | User | 1 | 0 | 0 | 0 | 1 | NON_SUBSTANTIVE_REPOSITORY_AUTOMATION |
| repo-000561 | samutiti/Biomni | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_ESM_PROTOTYPE_SUPERSEDED |
| repo-000563 | HasanAldhahi/Biomni | User | 11 | 10 | 0 | 1 | 0 | REUSED_SCREENED_MAINTENANCE_HEAD |
| repo-000566 | JiayuanDing100/Biomni | User | 10 | 9 | 0 | 1 | 0 | REUSED_SCREENED_MAINTENANCE_HEAD |
| repo-000564 | koyilee/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000562 | chenfengMeng2021/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000560 | Richardczl98/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000559 | lorettarehm/Biome | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000557 | elon00/Biomni999 | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000556 | andrewj-jung/Biomni | User | 10 | 9 | 0 | 1 | 0 | REUSED_SCREENED_MAINTENANCE_HEAD |
| repo-000568 | Harrisonzsh/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000700 | PLippmann/Biomni | User | 3 | 3 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000571 | GhostAnderson/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000572 | pyoos/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000641 | Shindevrp/Biomni | User | 3 | 1 | 2 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000598 | JinL0/Biomni | User | 2 | 1 | 1 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000582 | Minenhlekonnect/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000581 | litwinowicz/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000580 | Ramtinhoss/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000579 | lexyurk/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: NO_UNIQUE_CHANGE=16, EXACT_PR_LINEAGE=2,
REUSED_SCREENED_MAINTENANCE_HEAD=3,
NON_SUBSTANTIVE_REPOSITORY_AUTOMATION=1,
DIVERGED_SUBSTANTIVE_BROKEN_PARSER_SELF_CRITIC_REGRESSION=1,
DIVERGED_SUBSTANTIVE_AZURE_MCP_SUPERVISOR_PROTOTYPE=1, and
DIVERGED_SUBSTANTIVE_ESM_PROTOTYPE_SUPERSEDED=1.

## Retained historical changes

### repo-000553 — Sanat-Mishra/Biomni_Dev

- Two owner-authored commits form a strict linear chain, two ahead / 350 behind,
  modifying `biomni/agent/a1.py` and `biomni/llm.py`.
- Final `llm.py` contains literal nested Git conflict markers around
  `os.environ['OPENAI_API_KEY']=""`. Conflict markers are invalid Python syntax,
  so importing the package fails before the intended agent behavior is reachable.
  If resolved toward that assignment, it would also overwrite the process API key
  with an empty value at import time.
- The parser experiment correctly notices that retry corrections are HumanMessages,
  not AI messages. It permits three correction messages and falls back on the next
  malformed response by replacing the model output with a generic tagged solution.
  This bounds the formerly ineffective counter, but hides the failed response and
  can convert an evidence/tool-use failure into an ordinary-looking final answer.
- The new correction explicitly requests model “thinking and reasoning.” The system
  prompt also tells the code-capable agent to run `pip install` for missing modules.
  There is no package allowlist, pin, hash, approval, environment isolation, or
  license check, so this increases supply-chain and environment-mutation risk.
- The branch reverses the critical naming fix from merged PR #94: it renames nested
  `execute_self_critic` back to `self_critic`, colliding with the boolean function
  parameter. The function definition rebinds that name, so `if self_critic:` becomes
  truthy even when the caller disabled self-critique. This is a semantic regression,
  not formatting.
- The parser surface originates in merged PR #59 and is conceptually adjacent to
  `change-000053` and the parser component of `change-000066`, but there is no SHA,
  tree, or patch identity. Retain one broken historical change/lineage as a design
  warning; reject direct integration and rebuild a typed, observable retry protocol
  with explicit failure state and tests.
- No tests, dependency declarations, or documentation support the change. Owner and
  both commit author/committer logins are `Sanat-Mishra`; add that GitHub account to P.

### repo-000567 — Rasic2/Biomni

- Four owner-authored commits form one linear chain, four ahead / 379 behind, with
  six files. Retain one architecture prototype, not four changes.
- A1 unconditionally forces `source="AzureOpenAI"`. Default Claude names are then
  treated as Azure deployments, and caller `base_url`/`api_key` no longer control
  the provider. This breaks the existing multi-provider and Custom contracts; the
  later canonical Azure support is more complete.
- `demo.py` has no main guard. Importing it can initialize A1, download the data
  lake, invoke a paid model, and run an ADMET task. It is a live side-effect script,
  not a test.
- `demo-mcp.py` hard-codes two plaintext Bohrium SSE services (`dpa` and `smiles`),
  binds their remotely supplied tools to Azure, and creates specialist/supervisor
  LangGraph graphs. The SMILES graph mistakenly connects `dpa_llm_node`; its DPA
  tool calls are then routed to the SMILES tool executor. Both tool-node functions
  return new `ToolNode` objects rather than executing them and returning state.
- The deployment descriptor installs only the local project and loads `.env`, while
  project metadata does not declare the MCP adapter, supervisor, LangGraph, or Azure
  dependency closure. A clean deployment is not reproducible or reliably importable.
- Plain HTTP, no authentication headers or service identity, opaque remote tool
  schemas/results, and no allowlist/approval/output sanitization create interception,
  MCP tool-injection, and confused-deputy risks. Complete conversations go to Azure;
  tool arguments go to Bohrium; outputs return to Azure. There is no data
  classification, deidentification, residency, retention, or egress policy.
- The remote services' source, data, models, availability, version, scientific
  contracts, license, and terms are UNKNOWN. The one ADMET prompt supplies no model,
  endpoint, units, applicability domain, calibration, uncertainty, or validation.
- This is an independent conceptual alternative to existing MCP, LangGraph, Azure,
  and multi-agent candidates; no copy/ancestry identity is established. Retain one
  security/runtime/science-blocked single-repository lineage. Only the configured
  specialist-plus-supervisor idea merits clean-room comparison.
- Repository code retains Apache-2.0, but third-party services/dependencies require
  separate review. `Rasic2` authored and committed all four changes; add the account
  to P without inferring a real identity from its raw email.

### repo-000561 — samutiti/Biomni

- Two owner-authored commits form a strict linear chain, two ahead / 377 behind,
  adding 112 lines to `biomni/tool/database.py` for local and remote ESM embeddings.
- `query_esm()` accepts a raw sequence or fetches a UniProt FASTA, loads a named
  `fair-esm` model, mean-pools residue embeddings, and optionally returns per-residue
  tensors. `query_esm_remote()` posts the complete raw sequence to a fixed
  `https://api.esmatlas.com/fetch_embedding` path and assumes two JSON fields.
- The hostname/path and docstring are code facts. Whether this is an official,
  currently supported Meta API and whether the assumed schema is valid are UNKNOWN;
  no request was made and no product claim is accepted from the docstring.
- The fork does not update package/environment dependencies or
  `tool_description/database.py`. `read_module2api()` builds the tool inventory from
  descriptions, so these functions are unregistered prototypes. `esm` and Torch
  are imported at module top level without declared dependencies, so either missing
  package breaks the whole database module in a clean environment; NumPy and SeqIO
  imports are unused.
- Local execution reloads the default 650M model on every call, uses no cache/device
  selection/length limit/timeout/budget/OOM recovery, and returns non-JSON-serializable
  tensors. Empty sequences can mean-pool an empty slice. Non-`t33` model names always
  request layer 12, which is absent in smaller models and non-final in many larger
  models. Model/layer, alphabet, type, case, and response shapes are not validated.
- UniProt GET and ESM Atlas POST have no timeout or response bound. The remote path
  sends proprietary or patient-derived protein sequences to a third party and then
  repeats them in results, without opt-in, privacy/retention terms, classification,
  or local-only policy. This is a privacy/IP blocker, not evidence that a leak occurred.
- No model/checkpoint digest, package version, layer/device/dtype, accession version,
  pooling provenance, test, numeric reference, or shape check supports scientific
  reproducibility. ESM code, weights/training data, UniProt reuse, and API/output
  terms are not licensed merely by the repository's Apache-2.0 license.
- The fork predates upstream PR #205 by about seven weeks. PR #205 later adds a
  registered, dependency-installed, device/batch/length/OOM-aware Ensembl-isoform
  ESM tool. It does not provide the fork's raw-sequence, direct-UniProt, or remote
  path. Record conceptual precedence/partial supersession only: no ancestry,
  patch identity, copy direction, or shared authorship is proven.
- Retain one historical ESM change and one cross-surface lineage; use the frozen
  upstream implementation as the local gene-embedding baseline, but separately
  correct its remaining timeout/model-layer/license gaps. Do not reuse the unverified
  remote endpoint without official contract, privacy, and terms evidence.
- `samutiti` authored and committed both changes; add the GitHub account to P.

## Excluded and deduplicated findings

- `hubahu/Biomni_GuiY` adds only `sync_to_repo.sh`; it is repository automation,
  not a Biomni or scientific capability. From any current directory it stages all
  additions/modifications/deletions, commits, and pushes the current branch without
  diff review, tests, secret scan, or remote/branch allowlist. It can accidentally
  publish credentials, data, or unrelated work. Commit failure—including hook
  rejection—is swallowed and an existing commit may still be pushed. It uses no
  force push or hard-coded credential, but remains unsafe and is excluded.
- HasanAldhahi, JiayuanDing100, and andrewj-jung expose the same
  `pre-commit-ci-update-config@9fd4d14...` already audited in batch 020. It is one
  obsolete bot maintenance head, not three new changes or people.
- Shindevrp `Bidirectional_MCP@266d5b2...` and
  `mcp-get_rna_seq_archs4@5e45725...` are exact closed-unmerged PR #51 and #36.
  JinL0 `jin/adding_missing_dep@fbccf55...` is exact closed-unmerged PR #71.
  These PR surfaces receive no duplicate change IDs.
- Sixteen repositories expose only upstream-known heads.

## Identity boundary

- New substantive User owners/authors `Sanat-Mishra`, `Rasic2`, and `samutiti`
  enter P. Their GitHub logins are sufficient; real-name claims remain unverified.
- `hubahu` does not enter through a non-substantive repository utility.
- Exact PR authors, the reused-head source owner/bot, and upstream-only owners are
  already represented or do not enter through this batch.

## Evidence and limits

- Authenticated GraphQL branch/owner inventory covered 25 repositories and all
  59 refs. Four serialized comparisons against the frozen base were complete.
- Local PR inventories resolve three exact PR heads; canonical repository records
  prove the three reused refs share one already screened bot head.
- Static patches prove the conflict markers, parser/self-critic behavior, complete
  Rasic graph/deployment wiring, repository automation, and ESM implementations.
- Canonical Git history proves PR #59/#94 surfaces and merged PR #205 chronology.
  Cross-repository parser, MCP, and ESM relations without patch identity are marked
  conceptual, not derivation.

## Next action

Continue the next bounded active-fork batch. Retain three changes and three
lineages for historical provenance; all are blocked from direct integration by
runtime, security, privacy, scientific, dependency, or lineage evidence.
