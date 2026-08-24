# Public Fork Unique-Change Screening — Batch 016

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 155 branch refs without pagination.
Ten new refs reduced to eight unique SHAs because three forks share one exact
pre-commit head. Eight comparisons were executed serially with a two-second
interval; all succeeded.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000419 | avizipi/Biomni | User | 1 | 0 | 0 | 0 | 1 | CONFIG_STUB_ONLY |
| repo-000425 | Woody-Hu/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000423 | Kuan-Pang/Biomni-pulsar | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000422 | atcgx/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000421 | phdgil/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000430 | ARAMAS-AI/Biomni | Organization | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_FULLSTACK_DUPLICATE_MODELS |
| repo-000507 | ryanDing26/Biomni | User | 3 | 2 | 1 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000450 | redcellengineeringlab/Biomni | Organization | 24 | 23 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_BROKEN_CONTAINER |
| repo-000736 | gitcrunch/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000431 | catherine-langchain/Biomni-Deployment | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_LANGGRAPH_ADAPTER |
| repo-000432 | hplustree/AI_Agentic_Biomni | Organization | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000437 | outout/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000436 | Antior308/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000434 | ArshadJafri/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000433 | CyberGhost007/Biomni | User | 27 | 26 | 0 | 0 | 1 | DEPENDENCY_ONLY_SHARED |
| repo-000429 | AdamZou/Biomni | User | 27 | 26 | 0 | 0 | 1 | DEPENDENCY_ONLY_SHARED |
| repo-000428 | FEI38750/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000427 | zhaoyukoon/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000426 | MGPOCKY/Biomni | User | 27 | 26 | 0 | 0 | 1 | DEPENDENCY_ONLY_SHARED |
| repo-000438 | JING-XINXING/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000474 | moshebeeri/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000527 | Charvijain16/Biomni | User | 2 | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_RCSB_MCP_PROTOTYPE |
| repo-000439 | 11NOel11/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000443 | fionaxc/Biomni | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_SECURE_API_UDN |
| repo-000445 | zhanxw/Biomni | User | 26 | 25 | 0 | 0 | 1 | DEPENDENCY_ONLY_SUPERSEDED |

Classification counts: CONFIG_STUB_ONLY=1, DEPENDENCY_ONLY_SHARED=3,
DEPENDENCY_ONLY_SUPERSEDED=1, DIVERGED_SUBSTANTIVE_BROKEN_CONTAINER=1,
DIVERGED_SUBSTANTIVE_FULLSTACK_DUPLICATE_MODELS=1,
DIVERGED_SUBSTANTIVE_LANGGRAPH_ADAPTER=1,
DIVERGED_SUBSTANTIVE_RCSB_MCP_PROTOTYPE=1,
DIVERGED_SUBSTANTIVE_SECURE_API_UDN=1, EXACT_PR_LINEAGE=1,
NO_UNIQUE_CHANGE=14.

## Substantive candidates

### repo-000430 — ARAMAS-AI/Biomni

- Twenty-two ahead / 87 behind, 93 files. A late commit explicitly reverts to an
  earlier tree, so the final cumulative comparison—not every historical commit—is
  the surviving behavior. It adds a FastAPI/SSE wrapper, React/Vite UI, large
  environment snapshot, documentation, and 48 opaque model artifacts.
- The unauthenticated API exposes `/agent/stream` and `/agent/run`, allows callers
  to choose model, timeout, retrieval, commercial mode, and arbitrary data path,
  and streams thoughts, code, observations, raw steps, and exception text. Global
  temperature mutation races across requests. There is no tenant, quota, request
  bound, tool allowlist, filesystem boundary, or sandbox around Biomni code
  execution.
- CORS combines wildcard origins with credentials. Even with the default loopback
  bind, a malicious browser origin can target localhost; documented production
  binding would expose the same surface directly. Each request constructs a costly
  agent synchronously inside an async path.
- The documented UI/backend pair is not connected in the final tree: Vite fetches
  relative `/agent/stream`, has no development proxy, and runs on a different port.
  The UI also exposes internal reasoning/code while error state is not surfaced
  reliably. Runtime install-on-start, reload mode, ambiguous `.env` location, and
  platform-specific environment pins are not production-ready.
- Sixteen model families each include `.zip`, `config.pkl`, and `model.pt`. Pickle
  and common PyTorch serialization can execute code; no hashes, signatures, model
  cards, training provenance, endpoint definitions, validation, applicability
  domain, or redistribution terms are supplied.
- All 48 paths and Git blob SHAs exactly match the model artifacts already recorded
  in PMK change `change-000047`. They form one component-level duplicate, not 48
  new models. Direction of copying is not proven, although the observed PMK head is
  earlier. Quarantine both copies pending safe serialization and provenance.
- Repository ownership is organizational. All fork commits are attributed to
  `BRama10` / Balaji R; do not infer organizational IP authorization from that.

### repo-000450 — redcellengineeringlab/Biomni

- Fifteen ahead / 87 behind, nine files. Adds an stdin/stdout container wrapper,
  environment image, data-lake bootstrap, and documentation for a proposed HPC/PBS
  deployment. The repository is Organization-owned and fork work is attributed to
  `uylulu`.
- The README claims WebSocket, port 8000, and `/health`, but the code only reads
  stdin and has no network listener. The documented Dockerfile path is wrong, the
  setup command is malformed, `/quit` uses substring membership, exceptions end the
  process without a reliable failure exit, and the return-path can emit nothing.
- The app depends on mutable personal image `uylulu/biomni_env:latest` and an
  unpinned PyPI Biomni that need not match the fork. Images run as root with broad,
  unpinned conda/pip stacks and no digest, lock, SBOM, sandbox, resource limit, or
  secret isolation.
- Read-write data/generated mounts, inherited credentials, unrestricted network,
  and LLM-generated code permit modification or exfiltration. No per-user storage,
  retention, encryption, commercial-mode control, or data-license enforcement is
  implemented. Retain only as a broken container-deployment lead.

### repo-000431 — catherine-langchain/Biomni-Deployment

- Two ahead / 87 behind, three files. Adds a factory returning `A1(...).app`, a
  `langgraph.json` graph entry, and `pandas>=2.1.0`. This is a targeted LangGraph
  deployment adapter, not a complete hosted deployment.
- Graph/server compatibility, graph ID handling, dependency closure, startup data-
  lake behavior, checkpointer semantics, and concurrent initialization are untested.
  Construction can trigger large downloads during server cold start.
- `.env` and a fixed Claude model introduce secret/provider requirements. The patch
  defines no auth, tenant isolation, rate/cost controls, sandbox, egress policy, or
  per-user data storage; platform defaults are unknown. `commercial_mode=False`
  enables non-commercial datasets and is unsafe as a hosted default.
- Both commits are owner-authored by `catherine-langchain`. Retain as a small
  environment/integration candidate requiring secure reimplementation.

### repo-000527 — Charvijain16/Biomni

- One ahead / 190 behind, seven files. Adds a stdio FastMCP server with one
  `rcsb_text_search` tool, configuration, clients, smoke scripts, and a broad
  dependency snapshot. The commit is authored by `Sandora1933`, not the fork owner.
- The tool eagerly materializes every RCSB hit and slices afterward. Negative or
  huge `max_results`, broad queries, and absent timeout/cancellation can cause
  excessive work. It returns IDs without scores, experimental method, organism,
  resolution, assembly, citation, database version, or query provenance.
- Config and clients hard-code a personal Windows Python path, inherit the entire
  environment, and disagree on the default result count. The requirements omit MCP,
  leave `rcsb-searchapi` unpinned, duplicate packages, and include many unrelated
  heavy dependencies. The A1 integration script executes at import and is broken
  against canonical constructor/registry behavior.
- Stdio avoids a listening unauthenticated port, but MCP configuration is a local
  command-execution boundary and copied environment secrets reach the subprocess.
  Search terms leave the environment for RCSB and the natural-language prompt also
  reaches the configured LLM.
- Canonical Biomni already has richer RCSB search/detail/download tools and generic
  MCP import/export. This patch is a narrower unique adapter concept, not an exact
  duplicate. Reimplement minimally only if a dedicated RCSB MCP remains useful.

### repo-000443 — fionaxc/Biomni

- Twenty ahead / 100 behind, 12 files. Adds `SecureChatModel` for a Stanford Health
  Care gateway, provider-specific GPT/Claude/Llama/DeepSeek payload and tool-call
  conversion, configuration propagation, examples, and a UDN rare-disease runner.
  It also removes a bioimaging tool descriptor rather than fixing implementation.
- The model wrapper unconditionally prints complete request payloads and error
  responses. A1 configuration printing can include the subscription key. Patient
  prompts, tool arguments/results, responses, causal-gene labels, and full traces
  are stored as plaintext JSONL/text/CSV without redaction, encryption, access
  control, retention, consent, or governance checks.
- Caller-configurable gateway URLs can send subscription keys to arbitrary hosts;
  HTTPS/hostname is not enforced. Requests have no timeout, retry/backoff,
  cancellation, response-size bound, or rate handling. Tool calls still reach
  Biomni's broad code/network/file executor; a secure LLM gateway does not secure
  downstream tools.
- The UDN evaluation stops the whole loop when the causal gene ranks first, never
  calculates non-top rank correctly, miscounts success, silently drops malformed
  predictions, uses patient IDs in filenames without sanitization, and lacks
  reproducibility, leakage controls, top-k/MRR/calibration, or deidentification
  evidence. It is not a valid diagnostic benchmark or clinical workflow.
- Hard-coded institutional endpoints, shared-filesystem paths, preview API versions,
  VPN/subscription requirements, and PHI/data-use terms make the branch nonportable.
  All raw commits say Fiona Cai but have no linked GitHub login; do not map that real
  name to owner `fionaxc` without stronger evidence.

## Non-substantive and PR-lineage findings

- Fourteen repositories expose only upstream-known heads.
- avizipi adds a one-line mutable `python:3.11` base Dockerfile with no Biomni,
  dependency, copy, command, port, or entrypoint. It is an inert configuration stub.
- CyberGhost007, AdamZou, and MGPOCKY expose the same exact bot-authored pre-commit
  SHA; count it once. zhanxw has a different older Ruff bump. Current-main
  dependency versions supersede both; regenerate rather than cherry-pick.
- ryanDing26 `huggingface_integration` at `e1a9cc33...` is exact open PR #245; no
  duplicate change ID is allocated.

## Identity boundary

- New substantive User owners catherine-langchain, Charvijain16, and fionaxc enter
  P under the fork-owner rule.
- Code-visible User contributors BRama10, uylulu, and Sandora1933 enter P through
  substantive relevant fork branches. They are recorded separately from the
  Organization or non-author owner and do not transfer IP attribution.
- avizipi and the maintenance-only fork owners do not enter through this batch.
  Fiona Cai raw Git tuples remain unmapped to the `fionaxc` account.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 155 refs.
- Eight serialized successful comparisons against frozen main, separated by two
  seconds; local exact-SHA resolution handled upstream and PR heads.
- Exact Git blob comparison proves 48 path-for-path model artifact duplicates
  between ARAMAS and the previously recorded PMK branchcombined surface.

## Next action

Continue the next bounded active-fork batch. Retain five changes and one cross-
repository component-duplicate lineage for security, deployment, MCP, provider,
privacy, scientific-validity, provenance, license, and feature decomposition.
