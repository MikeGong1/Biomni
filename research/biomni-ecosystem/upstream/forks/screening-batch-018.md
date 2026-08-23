# Public Fork Unique-Change Screening — Batch 018

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 67 branch refs without pagination.
Six new unique SHAs were compared serially with a two-second interval; all
comparisons succeeded. The 330-commit lishengting comparison was exhausted over
four additional serialized pages. Five KSUN and eleven manu-tej omitted text blobs
were retrieved serially and inspected statically; no source was executed.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000477 | 1091240098/Biomni | User | 1 | 0 | 0 | 0 | 1 | EMPTY_NET_CHANGE |
| repo-000472 | KSUN63/Biomni | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_BROKEN_MINIMAL_REPACKAGE |
| repo-000476 | Biographica/Biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000475 | kec1510/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000471 | yxgu2353/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000483 | manu-tej/Biomni | User | 20 | 19 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_VSCODE_EXTENSION_REPLACEMENT |
| repo-000757 | zhangchenhaobest/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000519 | amehrjou/Biomni | User | 4 | 3 | 1 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000522 | junidude/Biomni_sj | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000484 | changwn/Biomni | User | 2 | 1 | 1 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000511 | dabinj96/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000570 | marcosbolanos/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000486 | shubhampachori12110095/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000485 | chmun0726/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000482 | 1AakashK/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000480 | TLux-ui/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000479 | Genereux-akotenou/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000490 | leezx/Biomni | User | 2 | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_OLLAMA_INVALID_ADMET |
| repo-000602 | lishengting/Biomni | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_PRODUCT_DAG |
| repo-000492 | mosabutey/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000491 | XuningFan/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000488 | abelaleb/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000493 | SALhik/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000500 | NKalavros/Biomni | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_INSTITUTIONAL_GATEWAY |
| repo-000497 | hojae-m-choi/Biomni | User | 19 | 19 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: DIVERGED_SUBSTANTIVE_BROKEN_MINIMAL_REPACKAGE=1,
DIVERGED_SUBSTANTIVE_INSTITUTIONAL_GATEWAY=1,
DIVERGED_SUBSTANTIVE_OLLAMA_INVALID_ADMET=1,
DIVERGED_SUBSTANTIVE_PRODUCT_DAG=1,
DIVERGED_SUBSTANTIVE_VSCODE_EXTENSION_REPLACEMENT=1,
EMPTY_NET_CHANGE=1, EXACT_PR_LINEAGE=2, NO_UNIQUE_CHANGE=17.

## Substantive candidates

### repo-000472 — KSUN63/Biomni

- One ahead / 167 behind. The `minimal` commit intentionally creates a roughly
  34-file “Biomni-DrugDiscovery” distribution by removing 94 paths and keeping A1,
  config/LLM/retrieval, database/literature/pharmacology/support tools, plus a guide,
  environment, examples, and modified package metadata.
- This is destructive and internally inconsistent. All schema pickles are removed
  while surviving database functions still open them. Broad tools, tasks, tests,
  setup scripts, API documentation, and tutorials disappear, but the retained
  `utils.py` still exposes Python, Bash, R, dynamic imports, pickle loading, network,
  and arbitrary file/code execution.
- The inspected environment installs `biomni` from pip, so examples may exercise the
  published package rather than this reduced fork. Dependencies are broadly ranged;
  local metadata renames the project while preserving upstream authors/homepage.
  No test proves registry/import consistency or a clean local build.
- The guide advertises ADMET, docking, binding, interaction severity, clinical
  recommendations, repurposing, and optimization without validation or clinical
  limitations. Many advertised database operations fail after schema removal.
- Owner/author `KSUN63` is directly attributable. Retain only as a historical
  removal/repackaging attempt; reject upstream integration and rebuild any minimal
  edition with explicit extras, registry allowlists, required schemas, tests, and
  license/scientific boundaries.

### repo-000483 — manu-tej/Biomni

- Twenty-eight ahead / 167 behind, linear history, 240 changed paths. It replaces
  upstream Biomni with a VS Code extension: 116 additions, 122 deletions, two
  modifications. The Python/tool/environment tree and Apache license are removed.
- The intended families are extension/sidebar/commands, file detection/grammars,
  settings and SecretStorage, MCP/WebSocket/provider code, genomics/database tools,
  results/export/workflow, molecular/network/results webviews, tests/build/CI, and
  extensive generated documentation. Preserve them as one provenance DAG, not 28
  separate changes.
- Exact blobs contradict the product claims. `BiomniMcpClient` never connects and
  simulates health/tools/results; provider tool discovery is simulated and its
  WebSocket is never connected. The bundled Python server is stdio-only, prints to
  stdout before JSON-RPC, is excluded from the VSIX, and cannot interoperate with the
  TypeScript WebSocket transport.
- Genomics calls use incompatible tool names and silently fall back to plausible-
  looking fixed BLAST, annotation, UniProt, PDB, and AlphaFold mock results. Those
  values are not marked mock and can be persisted/exported as scientific output.
- SecretStorage itself stores values safely, but `MessageHandler` bypasses it:
  webview-supplied API keys are written plaintext to global VS Code settings and
  returned to the webview. Dynamic webview commands execute arbitrary VS Code
  command IDs/arguments. Imported workflows execute arbitrary JavaScript/conditions
  with `new Function` and arbitrary VS Code commands without a trust schema or
  allowlist.
- Results are concatenated into `innerHTML`; CSP blocks external scripts but allows
  inline styles, and injected inline handlers are both unsafe and expected to be
  nonfunctional under the CSP. Webview file validation can open arbitrary readable
  text paths and returns fabricated validation/analysis scores. Persistence/export
  lacks demonstrated encryption, workspace isolation, formula neutralization,
  quotas, retention, or biomedical privacy controls.
- Manifest commands/activation IDs conflict; many of 74 settings are unwired;
  claimed VS Code MCP APIs are incompatible with the declared 1.90 API; CI release
  conditions are mutually impossible. README capabilities exceed surviving source.
- Default plaintext local transport has no authentication/TLS/tool confirmation.
  The final tree has no license grant, while README claims MIT and copied upstream
  assets/code require Apache attribution. Owner `manu-tej` authored all commits,
  with multiple Claude co-author trailers that must be preserved.
- Retain as a unique VS Code UX concept only. Secure clean-room design must use one
  real standard MCP transport, SecretStorage end-to-end, no mock-as-success or
  `new Function`, bounded workspace access, sanitizing DOM construction, provenance-
  labelled results, validated science, reproducible packaging, and an actual license.

### repo-000490 — leezx/Biomni

- Ten ahead / 186 behind, 11 files. It normalizes an Ollama `/v1` base URL, mutates
  stop sequences, expands the global A1 prompt/parser, forces all ADMET tasks through
  a new `predict_admet_properties_simple`, and commits tests plus synthetic result
  artifacts.
- The “MPNN” function performs no parsing or model inference. It counts uppercase
  characters and ring digits in raw strings, ignores the model argument, and derives
  solubility, absorption, metabolism, clearance, toxicity, and development advice
  from fixed thresholds. Aromatic atoms, chlorine, charges, `%10`, salts and invalid
  strings are mishandled. Numerical/clinical claims have no data, calibration,
  uncertainty, model card, or applicability domain.
- Global prompts ban RDKit, DeepPurpose and pandas; lexical checks are bypassable and
  misclassify unrelated “compound” code. Auto-closing truncated execute tags can run
  incomplete code. Debug logs expose prompts, model output and generated code.
- Tests catch errors without failing. The unexecuted notebook manually embeds exact
  ADMET values, labels them hallucinated twice, then relabels them actual; stored text
  and CSV repeat unsupported claims and conflict with the heuristic.
- This is an independent conceptual sibling—not a proven derivative—of dabulseco
  `change-000013` and Vik-u `change-000054`. Retain historical provenance but reject
  the heuristic, global ADMET prompt, artifacts and branch integration. Only tested
  URL normalization and task-neutral parser recovery are potential design leads.

### repo-000602 — lishengting/Biomni

- Three hundred thirty ahead / 268 behind. Four serialized compare pages recover
  all 330 unique commits and the exact head; the connected DAG has 328 one-parent
  commits and two merges. Final net diff is 37 files, +9,532/-196. The 2,773-line
  Gradio file lacks a patch, so its final auth/path/escaping behavior remains unknown.
- Surviving families include multi-provider A1/database configuration; stop/stream/
  logging/token instrumentation; iterative Gradio session/workspace/upload/download
  UI; four Dockerfiles and two deploy flows; environment/model/S3 checks; LibreOffice
  document conversion; and scientific/data/model maintenance. This is one long
  repository lineage requiring decomposition, not 330 features.
- API key, provider and base URL are copied into process-global environment/module
  state. Concurrent sessions can overwrite each other's provider and credentials.
  NodeLogger and default-on database debugging print full responses, tool arguments/
  outputs, endpoints, parameters, headers, bodies and questions; keys and PHI can
  enter logs and downloadable exports.
- Docker Compose exposes six Jupyter/Gradio variants on `0.0.0.0`; Jupyter explicitly
  uses empty token/password, wildcard origin and root allowance. Writable source,
  scripts, notebooks, downloads and results are mounted beside a code-capable agent.
  This is direct unauthenticated arbitrary-code execution to any reachable caller.
- Session chronology includes process-wide `chdir`, symlinks, file moves/scans,
  backups and download links. Missing final Gradio source prevents proving path or
  tenant isolation. Verified utilities also use unconstrained arbitrary document
  paths, unsanitized `ZipFile.extractall`, configurable download destinations and
  native LibreOffice parsing without sandbox/size controls.
- Supply chain uses latest installers, unpinned conda/pip/R/Bioconductor packages,
  multiple mirrors/trusted hosts, plaintext HOMER download, no-check-certificate,
  unpinned Git clones and unsigned archives/binaries. Scientific tests tolerate
  model/prediction failures; file-size/ZIP checks are not cryptographic identity;
  PubMed retries silently broaden queries.
- Owner/author `lishengting` accounts for all 330 commits. Retain one historical
  product lineage for decomposition, but do not integrate the exposed deployment or
  mutable global/session design.

### repo-000500 — NKalavros/Biomni

- Five ahead / 200 behind, two files. Replaces ordinary Anthropic and Custom paths
  with an NYU/Kong-specific Claude endpoint and adds a top-level live smoke script.
- Normal Anthropic routing ignores caller model/base URL, concatenates an unchecked
  `BASE_ENDPOINT`, reads a dedicated environment key and uses a questionable gateway
  version header. The nested custom adapter also hard-codes route/model, collapses
  tool/system/message roles, lacks native tools/streaming/async/metadata, and returns
  transport failures as successful `AIMessage("Request failed: ...")` content.
- The endpoint need not be HTTPS or allowlisted. Complete payloads are printed;
  attacker-controlled endpoints or redirects can receive the key and biomedical
  conversation. There is no retry/backoff, cancellation, response bound or
  institutional privacy policy. The final commit records a real production hostname
  and 504 failure.
- `minor_unit_test.py` has no tests/assertions/mocks, executes live agents/models at
  import time, can incur downloads, code execution and cost, and demonstrates failure
  rather than validation.
- This is an independent institutional-gateway alternative to larryinx
  `change-000033` and fionaxc `change-000060`. Preserve owner/author NKalavros
  attribution, reject the implementation, and use a separately named, HTTPS-
  allowlisted provider with structured failures and mocked contracts if needed.

## Non-substantive and PR-lineage findings

- Seventeen repositories expose only upstream-known heads.
- 1091240098 has three ahead commits that add, edit, then delete a YAML file; the
  final tree has zero changed files. It is an indexed empty-net history, not a
  substantive change or person-set entry.
- amehrjou `eval-reasoning-trace-local@56e6272...` is exact open PR #177.
- changwn `fix-AWSbedrock-emptyMessage@1ff2629...` is exact open PR #182.
  Neither PR surface receives a duplicate change ID.

## Identity boundary

- New substantive User owners/authors KSUN63, manu-tej, leezx, lishengting and
  NKalavros enter P.
- Existing PR authors amehrjou and changwn remain represented by their PR records.
  1091240098 and upstream-only owners do not enter through this batch.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 67 refs.
- Six serialized comparisons against frozen main, all successful; exact PR #177 and
  #182 heads were resolved locally.
- Four additional compare pages prove the complete 330-commit lishengting DAG.
- Five KSUN and eleven manu-tej Git blobs close critical omitted-patch gaps and prove
  the minimal-package and extension findings without executing source.
- Cross-repository semantic comparison establishes Ollama and institutional-gateway
  alternatives only; no patch or ancestry identity is claimed.

## Next action

Continue the next bounded active-fork batch. Retain five changes and three lineages
for extension/MCP security, scientific integrity, deployment exposure, provider/
Ollama comparison, privacy, license, supply chain, and feature decomposition.
