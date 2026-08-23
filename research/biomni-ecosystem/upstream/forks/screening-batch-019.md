# Public Fork Unique-Change Screening — Batch 019

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query returned all 73 branch
refs without pagination. Eight new unique head SHAs were compared serially with
a two-second interval. The three long cvxluo comparisons were exhausted over
four serialized pages each. A complete recursive cvxluo tree, 15 selected core
blobs, and the exact maximal Jaybee Streamlit blob were retrieved by immutable
SHA and inspected statically; no source, package, notebook, dataset, or server
was executed.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000496 | TaufiaHussain/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000495 | krudo-taco/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000494 | antonthieme/Biomni_demo | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000499 | linc0301/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000501 | bioMate-AI/Biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000502 | RecSys-tm4c/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000504 | AIxBio/Biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000503 | Jayluci4/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000646 | shengyongniu/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000505 | IamSolomonChika/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000518 | dusadvarshit/Biomni | User | 2 | 1 | 0 | 0 | 1 | DIVERGED_EXCLUDED_UNATTRIBUTED_EXPERIMENT |
| repo-000506 | biorevgrowth/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000510 | lwsinclair/Biomni | User | 21 | 20 | 1 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000528 | jaybee84/Biomni | User | 4 | 0 | 0 | 0 | 4 | DIVERGED_SUBSTANTIVE_SYNAPSE_STREAMLIT_LINEAGE |
| repo-000714 | JunhuiLi1017/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000512 | vlln/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000514 | hershman/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000513 | ahmadyan/Biomni | User | 20 | 20 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000509 | hidekiugajin/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000508 | davide-raciti/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000532 | tuln128/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000517 | IfraSa/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000516 | vectorwembanyama/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000515 | josh28x/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000523 | cvxluo/reti | User | 3 | 0 | 0 | 0 | 3 | DIVERGED_SUBSTANTIVE_MEDICAL_GENETICS_PRODUCT_DAG |

Classification counts: NO_UNIQUE_CHANGE=21, EXACT_PR_LINEAGE=1,
DIVERGED_EXCLUDED_UNATTRIBUTED_EXPERIMENT=1,
DIVERGED_SUBSTANTIVE_SYNAPSE_STREAMLIT_LINEAGE=1, and
DIVERGED_SUBSTANTIVE_MEDICAL_GENETICS_PRODUCT_DAG=1.

## Substantive candidates

### repo-000528 — jaybee84/Biomni

- Four visible heads collapse to one 15-commit DAG. Both side branches are
  merged into `main`; `main@a78cdfb...` is a strict ancestor of maximal
  `fix-streamlit-aws-bedrock-integration@6e5693c...`. Retain one change and one
  lineage, not four changes.
- The product is a Streamlit wrapper around a code-capable Biomni A1 agent,
  Anthropic/Bedrock configuration, named Synapse profiles, chat/log exports,
  visualizations, a notebook, a launcher, devcontainer metadata, and a locked
  local editable app environment.
- The exact 2,409-line maximal app has a critical direct injection. A user-entered
  Synapse profile is interpolated into Python source, executed with `exec()`, and
  then prepended to the agent prompt. A profile containing a quote and Python
  payload can execute arbitrary server-process code before A1 runs.
- Streamlit session state keeps agents and Synapse clients separate, but keys,
  bearer tokens, region/source flags, imported modules, working directory, data
  paths, and outputs are process-global. One user can silently inherit another
  user's credential; token prefixes are displayed; there is no logout or key
  clearing; concurrent sessions can overwrite provider state and files.
- Any accessible `.env` path can be read and every parsed key is written into the
  global environment. Generated output paths can make the app open and serve any
  process-readable image. It scans shared CWD images and can attach another
  session's or stale figure to the current result. Full traces, agent output, and
  chat can be downloaded; the purported PDF is unescaped HTML without CSP.
- There is no application authentication. Although the provided config binds to
  loopback, it disables both XSRF and CORS. Port forwarding, a reverse proxy, or an
  address change makes profile injection, shared credentials, and unrestricted
  A1/Synapse operations remotely reachable.
- Synapse access uses a server-side named profile, so browser users inherit that
  credential's ACLs rather than presenting individual identity/DUC evidence.
  Unrestricted generated code can download, upload, update, or delete when the
  profile permits. There is no method allowlist, confirmation, per-session root,
  entity version/hash, retention, deidentification, or controlled-data policy.
- Bedrock selection is not truthful or reliable: Sonnet 4 silently maps to Claude
  3.5 Sonnet v2, one Haiku date differs, other choices are unmapped, the connection
  test does not call AWS, and root packaging omits `langchain-aws`. Python, README,
  launcher, requirements, uv, and devcontainer modes disagree.
- Scientific prompts treat top-expression plots and LLM-resolved schema conflicts
  as evidence without cohort design, drug-response labels, QC, confounder control,
  statistics, or external validation. Shared/stale figures and false model labels
  further invalidate provenance.
- Owner `jaybee84` has substantive merge/document/upload commits. Contributor
  `tschaffter` authors the maximal devcontainer/dependency/Bedrock delta. Three
  foundational app commits remain attributable only to an unlinked EC2 identity;
  do not silently assign them to the owner.
- Preserve as one historical Synapse/Streamlit concept lineage only. A clean-room
  design needs per-user Synapse authorization, DUC checks, isolated secrets and
  workspaces, a bounded Synapse interface, sandboxed execution, authenticated web
  access, real Bedrock model mapping, sanitized exports, and complete data/model/
  tool provenance.

### repo-000523 — cvxluo/reti

- The three heads form an exact strict chain:
  `hardcoded@4ff5689...` (319 commits) is a subset of `main@56e7ae1...`
  (320), which is a subset of `cvxluo/agent-changes@92503d7...` (322).
  Count the terminal union once.
- All three commit lists were fully paginated. The compare API exposes only 300
  files, 298 under committed `api/node_modules`; later pages contain no additional
  files. The non-truncated recursive maximal tree instead contains 19,316 items,
  proving the compare list is capped and unrepresentative.
- The tree contains an Express/OpenAI API, Next.js frontend, copied old Biomni/Flask
  app, multimodal phenotype and ASR routes, ClinVar/PubMed/Biomni tool calls, IGV
  views, a standalone gene-checker MCP, 2,232 vendored node_modules items, and
  16,890 diagnosis-tree items. Diagnosis includes two transformed 8,207-case
  phenopacket collections and a roughly 63 MB phenotype-to-gene map.
- The Express service normally listens on all interfaces, reflects arbitrary CORS
  origins, and has no authentication, authorization, rate/cost limits, timeout,
  session ownership, TLS, or audit policy. Any reachable caller can spend the
  OpenAI key, upload clinical media, read committed case variants, and indirectly
  prompt a local code/tool-capable Biomni server.
- Clinical notes, photographs, audio, conversation history, HPO results, variants,
  and tool outputs are sent to OpenAI or logged without consent, deidentification,
  retention, residency, or processor policy. Rare-disease case/publication/family
  combinations can be reidentifiable; consent, source extraction, correction,
  redistribution, ontology version, and licensing are not established.
- The active agent mandates `rank_genes_from_hpo`, but does not register or handle
  that tool and forces the final response after one tool round. The local ranker is
  dead in the active flow and uses a simplistic exact-match inverse-frequency sum,
  without ontology propagation, inheritance, variants, evidence quality, negative
  phenotypes, calibration, or benchmark validation.
- `Chat2` calls a route commented out by the server. Image upload accepts arbitrary
  MIME content in memory; audio accepts octet-stream/extension claims; ASR returns a
  fabricated zero-duration segment. IGV reads only the first variant of the first
  three files, assumes hg38, combines positions across chromosomes incorrectly,
  and its apparent upload control only logs a filename.
- Commit evidence explicitly records a hardcoded answer and fake timer in every
  retained head. The README's “AI medical geneticist” claim is unsupported by any
  diagnostic cohort, sensitivity/specificity, calibration, clinician adjudication,
  evidence grading, or regulatory boundary. Demo behavior is not clinical evidence.
- Root-level new product code has no root license; the copied Biomni subtree retains
  Apache-2.0, but that does not license original Reti code or establish permission
  for case data, HPO mappings, publication-derived content, committed node_modules,
  external services, or their attribution requirements.
- Direct substantive accounts are owner `cvxluo`, backend/agent contributor
  `sophicle`, and frontend/IGV contributor `VinnySha`. README also credits John
  Yang and commits preserve his raw name/email, but no GitHub login is proven; keep
  that attribution unresolved rather than inventing an account mapping.
- Retain only the terminal head as one historical product lineage. Do not merge it.
  Potential concepts—reviewed HPO extraction, evidence-aware prioritization,
  phenopacket visualization, multimodal intake, and bounded orchestration—require
  independent reimplementation after privacy, security, clinical, provenance, data,
  dependency, and licensing review.

## Excluded, no-unique, and PR-lineage findings

- Twenty-one repositories expose only upstream-known heads.
- `lwsinclair:add-mseep-badge@79680db...` is exact closed-unmerged PR #151 and
  receives no duplicate change ID.
- `dusadvarshit:vd_experiments@1086fe9...` is three ahead / 248 behind. Its first
  two commits cancel to the exact merge-base tree. The surviving unlinked `Ubuntu`
  EC2 commit adds a new per-instance Anthropic limiter, removes pLAnnotate from the
  environment while leaving its tool advertised, changes ignore rules, and rewrites
  a notebook whose patch is omitted.
- That limiter creates a fresh 0.1-request/second bucket with burst size ten for
  every LLM object. It neither coordinates credentials/processes nor honors 429/
  `Retry-After`, token quotas, retry/backoff, or concurrency. No controlled runs,
  metrics, assertions, model/version control, or scientific validation exist.
  The omitted notebook also cannot be cleared for secrets, privacy, or provenance.
  Exclude the branch and do not add the owner through a canceled tree change.

## Identity boundary

- New substantive User accounts `jaybee84`, `tschaffter`, `cvxluo`, `sophicle`,
  and `VinnySha` enter P with direct branch/commit evidence.
- `EC2 Default User`, `Ubuntu`, and John Yang's raw Git identity remain unmapped.
  Preserve their evidence and do not assign their commits to nearby repository
  owners.
- Upstream-only, exact-PR-only, and excluded-experiment owners do not enter through
  this batch.

## Evidence and limits

- Authenticated GraphQL branch/owner inventory covered 25 repositories and 73 refs.
- Eight serialized comparisons against frozen main succeeded; twelve additional
  serialized compare pages prove all 319/320/322 cvxluo commit sets and exact heads.
- One complete recursive tree proves 19,316 maximal cvxluo items. Fifteen immutable
  core blobs close first-party API/frontend gaps but do not cover the hardcoded
  Chat source or MCP internals; those remain explicitly limited.
- The exact maximal Jaybee Streamlit blob proves the profile injection, secret and
  filesystem behavior, session/global boundary, export path, and scientific/
  operational limitations. Surrounding files prove the lineage, launcher, package,
  devcontainer, and Bedrock inconsistencies.

## Next action

Continue the next bounded active-fork batch. Retain two changes and two lineages
for historical decomposition; both are integration-blocked. Carry forward the
Jaybee authentication/privacy/RCE and Reti security/clinical/data/license work as
explicit unresolved lineages rather than production candidates.
