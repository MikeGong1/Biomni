# Public Fork Unique-Change Screening — Batch 015

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 135 branch refs without pagination.
Twelve new unique SHAs were compared serially with a two-second interval; all
comparisons succeeded.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000424 | tangxuan82/Biomni | User | 2 | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_BUG_FIX |
| repo-000575 | PabloPauling/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000402 | Asritha0606/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000403 | user01010011/Biomni | User | 33 | 32 | 0 | 0 | 1 | DEPENDENCY_ONLY |
| repo-000550 | LucasArg00/Biomni | User | 1 | 0 | 0 | 0 | 1 | NOTEBOOK_ONLY_UNRELATED |
| repo-000405 | hotkeehotkee/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000406 | seanhellwig/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000746 | sphilius/Biomni | User | 3 | 1 | 0 | 0 | 2 | DOCS_AND_CONCEPTS_ONLY |
| repo-000407 | WongLoki/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000408 | ibukunoluwayomi/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000409 | renatlb/biomni_fork | User | 32 | 31 | 0 | 0 | 1 | DEPENDENCY_ONLY_SUPERSEDED |
| repo-000469 | svamintgit/Biomni | Organization | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000410 | CodeSharingPartially/Biomni_e1 | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000411 | xudonglu26-blip/Biomni | User | 32 | 31 | 0 | 1 | 0 | FORMAT_ONLY_REUSED |
| repo-000435 | Vik-u/Biomni | User | 1 | 0 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_LOCAL_WRAPPER |
| repo-000413 | gordian-biotechnology/Biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000414 | Yar-Cov/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000665 | moikartik/Biomni | User | 5 | 0 | 0 | 0 | 5 | DIVERGED_SUBSTANTIVE_ALTERNATIVE_DAG_PLUS_DOC |
| repo-000415 | scchess/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000416 | scholarLW/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000599 | rlancemartin/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000489 | sidsoc12/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000417 | drguyang/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000481 | igor-sadalski/Biomni | User | 9 | 8 | 1 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000418 | tpfeng/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: DEPENDENCY_ONLY=1, DEPENDENCY_ONLY_SUPERSEDED=1,
DIVERGED_SUBSTANTIVE_ALTERNATIVE_DAG_PLUS_DOC=1,
DIVERGED_SUBSTANTIVE_BUG_FIX=1, DIVERGED_SUBSTANTIVE_LOCAL_WRAPPER=1,
DOCS_AND_CONCEPTS_ONLY=1, EXACT_PR_LINEAGE=1, FORMAT_ONLY_REUSED=1,
NOTEBOOK_ONLY_UNRELATED=1, NO_UNIQUE_CHANGE=16.

## Substantive candidates

### repo-000424 — tangxuan82/Biomni

- Two commits, two ahead / nine behind, modify only `biomni/agent/a1.py`.
  Untagged model output is wrapped as `<solution>...</solution>` to avoid a parser
  error.
- The guard checks `<execution>` although the established action tag is
  `<execute>`, and it is case-sensitive while the downstream regex is not. A valid
  `<execute>` response can therefore be nested inside `<solution>` and treated as
  final output instead of being executed. The comment also says `<think>` while
  the code creates `<solution>`.
- Silently converting every malformed response to a final answer can hide missing
  tool calls and prematurely finish evidence-sensitive biomedical work. Reuse only
  as a bug report/design lead: normalize the exact tags case-insensitively, preserve
  observable protocol errors, and test valid, malformed, and plain-text responses.
- Both commits are owner-authored by tangxuan82 / Jiaowei Tang.

### repo-000435 — Vik-u/Biomni

- Five ahead / 17 behind. The first two commits add a local Ollama CLI, a Gradio
  chat wrapper, tutorial, and documentation; three later commits are redundant
  merge topology with no distinct feature work.
- The wrappers provide one-shot and multi-turn local-model examples, loopback
  binding by default, environment overrides, and a fallback when the requested
  port is unavailable. This is a narrower independent alternative to the earlier
  dabulseco Ollama surface, not an exact duplicate.
- A global A1 instance is shared by Gradio sessions. If the server-name override
  exposes the unauthenticated app, callers share state and a code/tool-capable
  agent. Full history is concatenated without a bound, the CLI prints prompts and
  complete transcripts, and the prompt asks for reasoning-like content.
- Empty expected-data directories and disabled retrieval do not prove execution is
  sandboxed or scientific resources are available. Local model XML/tool compliance,
  biomedical quality, concurrency, and failure behavior are untested. Ollama,
  `gpt-oss:20b`, and Mistral versions/licenses are not pinned or documented.
- Reuse only as a loopback-only developer example after per-session agent state,
  authentication/isolation, bounded history, safe tool policy, and model/provenance
  documentation. Feature work is owner-authored by Vik-u / Vikas Upadhyay.

### repo-000665 — moikartik/Biomni

- Five heads form one eight-commit union. `main` is a four-commit documentation
  chain ending at `73e52952dd0450b7399c8d3d66a2b8480c4eb0bf`; four React heads are pairwise
  siblings, each exactly one commit beyond that head. They are alternatives, not
  sequential revisions and not four independent feature families.
- `main` adds only a 233-line architecture analysis. It is uncited and 466 commits
  behind; claims about tool/data counts, checksums, isolation, caching, providers,
  and reliability require current-source verification. Multiprocessing timeouts are
  not a security sandbox.
- The `3fa5` branch is the least-incomplete viewer: React 18/TypeScript, three
  bundled notebooks, routes, GFM Markdown, syntax-highlighted code, streams,
  errors, text, images, and HTML output. It lacks tests/lockfile and has weak fetch
  errors, wrong rich-output precedence/JPEG handling, and unsanitized HTML.
- The `46bf` branch has a safer typed/static design and lockfile but omits the
  imported `src/data/notebooks` module, so it is statically non-buildable. The
  `6500` branch has stronger status/cancellation/grid behavior but omits its imported
  notebook manifest and also renders unsanitized HTML. The larger `d4ae` branch is
  likely closest to runnable, but eagerly bundles notebooks and stored outputs,
  uses both raw Markdown HTML and `dangerouslySetInnerHTML`, lacks tests/lockfile,
  and makes unsupported production/security/performance claims.
- Stored tutorial output exposes cluster and temporary paths, provider/model
  identity, third-party response content, and a full agent trace. Its CRISPR plan is
  an educational model output, not validated evidence: acute/chronic stimulation is
  confounded, proximal TCR essentials dominate, and controls, replicates, analysis,
  multiplicity, and validation are missing. Notebook, model-output, Reactome/data,
  and package provenance/licensing require separate review.
- Retain one lineage, not four copies. If a viewer is needed, start from `3fa5`,
  port `6500` loader/error ideas and selected `d4ae` interactions, keep one canonical
  notebook source, strip stored traces, and sanitize or sandbox HTML. React tips are
  Cursor Agent-authored with Kartik co-authorship; the shared documentation chain is
  primarily owner-authored by moikartik / Kartik.

## Non-substantive and PR-lineage findings

- Sixteen repositories expose only upstream-known heads.
- user01010011 and renatlb each have a bot-only pre-commit update from the same
  parent. The former selects Biome/Ruff 2.3.7/0.14.6; the latter selects the older
  2.3.4/0.14.4 pair. Frozen main already uses 2.3.10/0.14.11, so neither is a
  current runtime capability and the older branch is superseded.
- xudonglu26-blip exposes a previously screened pre-commit formatting head; it is
  not re-compared or re-counted.
- igor-sadalski `geneformer_embeddings` at `91244ff6...` is exact open PR #231;
  no duplicate change ID is allocated.
- LucasArg00 adds only a 2,261-line Colab notebook whose compare patch is absent.
  Its title suggests semi-structured data engineering, but cells, outputs, secrets,
  dependencies, data rights, and Biomni relevance are not inspectable from the
  authorized artifact, so it is excluded.
- sphilius exposes two independent documentation branches from an old 0.0.2 head:
  one stale AI-assistant guide and one bot-authored concept/biomechanics set. The
  guide incorrectly calls Biomni MIT-licensed, makes unsupported roadmap/authorship
  promises, and omits execution-sandbox/privacy controls. The concepts provide no
  implementation or validation and include out-of-scope ideas. Neither is counted
  as a capability change or owner-authored substantive contribution.

## Identity boundary

- New substantive User owners tangxuan82, Vik-u, and moikartik enter P.
- sphilius, LucasArg00, user01010011, and renatlb do not enter through
  documentation, notebook, or bot-only maintenance surfaces.
- Commit attribution remains with the observed authors and co-authors; Cursor
  Agent, Claude, and Jules work is not silently reassigned to fork owners.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 135 refs.
- Twelve serialized successful comparisons against frozen main, separated by two
  seconds; local exact-SHA resolution handled upstream, PR, and screened heads.
- Exact parent membership proves the eight-commit moikartik union: one four-commit
  documentation prefix plus four single-commit sibling viewer alternatives.

## Next action

Continue the next bounded active-fork batch. Retain three changes and one lineage
for parser correctness, local-agent isolation, frontend security, notebook
provenance, scientific validity, license review, and feature decomposition.
