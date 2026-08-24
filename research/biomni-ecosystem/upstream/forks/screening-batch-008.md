# Public Fork Unique-Change Screening — Batch 008

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 78 branch refs without pagination.
Seventeen new heads were compared serially: 16 succeeded and one unrelated-history
head had no common ancestor. Seven exact PR heads and one previously screened head
were not re-compared. One additional serialized same-repository comparison resolved
the vladsavelyev branch relationship.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000241 | Benjamin0119/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000242 | stsking/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000243 | hjanime/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000367 | siavashre/amplicon-repo-agentai | User | 5 | 0 | 1 | 4 | SUBSTANTIVE_LINEAGE |
| repo-000251 | Bailuga666/Biomni | User | 1 | 0 | 0 | 1 | DOC_ONLY |
| repo-000244 | aixintiankong/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000245 | mnhuda/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000246 | fengzhongjingmo-debug/Bioagent | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000247 | hellodavid-design/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000248 | HinVec/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000250 | zetingli-bio/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000252 | yangluom/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000737 | JaylanLiu/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000634 | lxasqjc/Biomni | User | 7 | 3 | 4 | 0 | PR_LINEAGE_ONLY |
| repo-000449 | vladsavelyev/Biomni | User | 5 | 0 | 2 | 3 | DIVERGED_DERIVED_EXTENSION |
| repo-000377 | BenaroyaResearch/Biomni | Organization | 3 | 0 | 0 | 3 | SUBSTANTIVE_UNIQUE |
| repo-000378 | wpr7280/MyBiomni | User | 5 | 1 | 0 | 4 | SUBSTANTIVE_LINEAGE |
| repo-000331 | XxxKrabs/BioMNI | User | 2 | 0 | 0 | 2 | SUBSTANTIVE_PLUS_UNRELATED_HEAD |
| repo-000253 | fjkiani/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000254 | RitzSCHA-Bio-Tech/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000255 | josephzsun/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000256 | AshokGaire3/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000257 | yak-liu-NEU/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000258 | Sun-Yanbo/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000259 | antonychigz-boop/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: DIVERGED_DERIVED_EXTENSION=1, DOC_ONLY=1,
FORMAT_ONLY=1, NO_UNIQUE_CHANGE=17, PR_LINEAGE_ONLY=1,
SUBSTANTIVE_LINEAGE=2, SUBSTANTIVE_PLUS_UNRELATED_HEAD=1,
SUBSTANTIVE_UNIQUE=1.

## Substantive and derived candidates

### repo-000367 — siavashre/amplicon-repo-agentai

- Four non-PR heads form an 85-commit non-linear union; closed-unmerged PR #279
  is also present as an exact fifth branch head.
- `main` (one commit) is contained in every developed branch.
  `amplicon_refactor` (58 commits) is contained in `amplicon_merged` (60).
  `amplicon_table` (81) shares 56 commits with `amplicon_merged`, retains 25
  side commits, and lacks four commits from the renamed branch.
- The union adds amplicon table, cycle, gene, graph, structural-variant, and gene-
  coordinate tools; CCLE/TCGA/PCAWG-oriented know-how/data; benchmarking and
  token logging; Gradio/Hugging Face deployment; interactive clarification,
  table/plot rendering, timeouts, and per-thread REPL isolation.
- Security/license: some demos bind to `0.0.0.0` and use public sharing; full
  questions, generated code, observations, and answers can be logged. Bundled
  archives, pickles, PDFs, datasets, and redistributed cancer-data artifacts
  require provenance and license review. No branch is selected as canonical yet.

### repo-000449 — vladsavelyev/Biomni

- Both new heads are 87 behind and contain all 54 commits already normalized as
  `change-000006` from m-barthel/Biomni. They are derived extensions, not a new
  copy of that base change.
- `fix/use-chatbedrockconverse` adds one distinct SHA; `main` adds three different
  SHAs. A direct branch comparison reports main ahead 3 / behind 1, so neither
  tip contains the other. Their ChatBedrockConverse patches may be equivalent,
  but that is not established by SHA or subject alone.
- Main also adds Bedrock-client dependency injection and changes the commercial
  data allowlist. The latter re-enables entries previously annotated as
  proprietary, non-commercial, or requiring a commercial license; the commit
  subject's reference to legal review is not itself legal evidence.
- Security/license: the inherited lineage includes generated-code execution,
  timeouts that do not terminate worker threads, Docker/network activity, and a
  mutable GitHub PR dependency. Patch equivalence and data terms require deep audit.

### repo-000377 — BenaroyaResearch/Biomni

- `main` (one commit) is a strict subset of `startup` (four), which is a strict
  subset of `dependencies` (seven); one seven-commit `ENVIRONMENT` change is
  retained rather than three duplicate branch changes.
- Adds Docker/devcontainer/GHCR setup, launchers, conda/R dependency installation,
  and plotting verification.
- Security: optional global SSL-verification disabling, unverified remote install
  pipelines, mutable dependencies/actions, and passwordless sudo require review.
- The owner is an Organization and does not enter the person universe.

### repo-000378 — wpr7280/MyBiomni

- A strict branch chain is proven: `deploy` (44 commits) ⊂
  `rebrand-warphelix` (49) ⊂ `ami-biomni` (54) ⊂
  `feature/skill-system` (58).
- The lineage adds a Java/Vue/MySQL admin and conversation platform, authentication,
  quotas, exports, AWS Marketplace AMI deployment, WarpHelix branding, persistent
  multi-turn context, and a filesystem-backed Skills/Know-How management layer.
- GitHub returned exactly its 300-file compare cap for every developed branch;
  file inventories are therefore lower bounds and the candidate remains pending
  full-tree audit.
- Security/license: visible defaults include database/JWT fallbacks, credentialed
  wildcard CORS, and verbose request/token logging. Private-key detection is
  removed, while large vendored/generated surfaces lack reviewable patches.
  Code provenance, trademarks, marketplace terms, secrets, and auth boundaries
  require deep audit.

### repo-000331 — XxxKrabs/BioMNI

- `main`: four commits, 27 files, 0 behind. Adds a BixBench task/runner, database
  and literature changes, launch scripts, web-search helpers, and committed results.
- `DiscoverOS` has no common ancestor with frozen Biomni main. Its content and
  relationship are `UNKNOWN`; it is retained as an unrelated-history lead and is
  not merged into the BixBench change.
- Security/benchmark integrity: archive extraction uses `extractall()` without
  visible member-path validation. Defined strict-mode path/code checks have no
  visible runner call sites, so they are not treated as a security boundary.
  Committed result files and benchmark/data licenses require deep review.

## Non-substantive and PR-lineage findings

- Seventeen repositories expose only upstream-known heads.
- Bailuga666 adds eight generated-looking Chinese code-navigation documents only.
- zetingli-bio has a two-commit pre-commit dependency/format update only.
- lxasqjc's four distinct branches exactly match open PR #235/#236 and
  closed-unmerged PR #80/#35; no duplicate change IDs are created.
- vladsavelyev also exposes exact open PR #228, exact closed-unmerged PR #296,
  and one already-screened `change-000006` head.

## Identity boundary

- New substantive User owners siavashre, wpr7280, and XxxKrabs enter P.
- vladsavelyev was already in P as a PR author; the fork relationship is appended
  to that existing identity rather than creating a duplicate person.
- BenaroyaResearch is an Organization. Bailuga666 and zetingli-bio do not enter P
  because their only unique changes are documentation or automated maintenance.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 78 refs.
- Seventeen serialized comparisons against frozen main plus one serialized
  same-repository lineage comparison.
- Local exact-SHA comparison against the upstream DAG, canonical open/closed PR
  heads, prior screened heads, and canonical change commit sets.
- Commit-set membership establishes the three lineages above; semantic patch
  equivalence and large-file contents remain unresolved where stated.

## Next action

Continue the next bounded active-fork batch. Retain the five change candidates and
three lineages for feature decomposition, full-tree, license, and security audits.
