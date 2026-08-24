# Public Fork Unique-Change Screening — Batch 013

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 91 branch refs without pagination.
Four new unique SHAs were compared serially and all succeeded. One exact open-PR
head and one previously screened formatting head were not re-compared.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000666 | thadada/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000347 | szxcool/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000349 | liuchuanyi/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000352 | staskh/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000353 | geobio/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000354 | kitoti/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000355 | akotlar/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY_REUSED |
| repo-000356 | Nimbus-Discovery-Inc/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000357 | juliaseungjoobaek/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000358 | JulieOnIsland/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000359 | hgim01/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000360 | manolaz/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000362 | stevewithjobs/Biomni_molecule | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000363 | seijung-k/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000364 | JCupe17/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000366 | HendricksJudy/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000368 | qurh/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000370 | samalt-os/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000373 | rwbaber/Biomni | User | 2 | 0 | 0 | 2 | DOC_PLUS_PERSONAL_CONFIG |
| repo-000487 | menggf/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000374 | yarikoptic/Biomni | User | 34 | 32 | 1 | 1 | PR_LINEAGE_PLUS_DEPENDENCY_ONLY |
| repo-000301 | gutendzx/Biomni | User | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE |
| repo-000371 | biochemi/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000375 | ngshasan/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000549 | shantanusharma/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: DIVERGED_SUBSTANTIVE=1, DOC_PLUS_PERSONAL_CONFIG=1,
FORMAT_ONLY_REUSED=1, NO_UNIQUE_CHANGE=21,
PR_LINEAGE_PLUS_DEPENDENCY_ONLY=1.

## Substantive candidate

### repo-000301 — gutendzx/Biomni

- `main`: ten ahead / nine behind, four files, with merge base
  `c36e39f9202863bc7b0665563e74e97723862fa5`.
- Adds configurable execution working directories for Python/R/bash, UUID/default
  thread IDs, recursion limits, namespace clearing, parse-error changes, Bedrock
  provider ordering, and GLM→Google Vertex/OpenAI-compatible routing through ADC.
- The working-directory feature is not filesystem isolation. Python/R/bash retain
  absolute paths, `..`, symlinks, environment variables, and arbitrary `chdir`;
  bash inherits the full environment. Process-global `os.chdir`, `sys.stdout`,
  persistent namespace, and plot state race across concurrent sessions. Namespace
  clear affects every instance and thread.
- Invalid working-directory early returns can leave global stdout redirected. UUID
  graph threads improve the prior fixed ID but do not isolate files, variables,
  prompts, logs, or shared A1 state. Caller-provided IDs can still collide.
- `go()` uses the configured recursion limit while `go_stream()` remains fixed at
  500. GLM substring detection precedes Custom routing and can misroute unrelated
  models; Gemini API-key behavior is replaced by broad-scope ADC/Vertex credentials,
  with undeclared dependency, missing-project, token-handling, and startup-side-
  effect risks.
- The ten commits are attributed to `shuhanx61` and `HNO333333`, not the fork
  owner. The User owner enters P under the fork-owner boundary without receiving
  commit authorship.
- Preliminary type: `REFACTOR` / execution and provider infrastructure.

## Non-substantive and PR-lineage findings

- Twenty-one repositories expose only upstream-known heads.
- rwbaber `main` adds a generated five-line PATH script with a private workstation
  absolute path; it is non-portable personal configuration with PATH-precedence
  risk. Its other branch adds six bot-generated gap-analysis Markdown files only.
- akotlar exposes an exact previously screened pre-commit formatting head.
- yarikoptic adds one Ruff pre-commit version bump; its other distinct branch is
  exact open PR #275. No change ID is allocated for either maintenance surface.

## Identity boundary

- New substantive User owner gutendzx enters P, while commit attribution remains
  with shuhanx61 and HNO333333.
- rwbaber's owner-specific changes are documentation/personal configuration.
- yarikoptic was already in P as a PR author; maintenance and exact PR surfaces do
  not create a new identity or change.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 91 refs.
- Four serialized comparisons against frozen main, all successful.
- Local exact-SHA comparison against upstream, PRs, screened heads, and changes.

## Next action

Continue the next bounded active-fork batch. Retain the gutendzx change for
security, concurrency, provider, license, and current-main applicability audit.
