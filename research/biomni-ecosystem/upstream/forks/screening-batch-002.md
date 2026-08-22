# Public Fork Unique-Change Screening — Batch 002

Parent verification: `VERIFIED`. Scope: 11 Network-tree-only forks plus the 14
most recently pushed unscreened REST forks. One serialized GraphQL query returned
all 135 public branch refs with no ref pagination. Twenty-three unique non-PR
heads were compared serially against frozen main; 22 comparisons succeeded and
one unrelated-history branch had no common ancestor.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000776 | zhaoyanh/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000777 | alexs42/Biomni-AD | User | 1 | 0 | 0 | 1 | BIOMNI_AD_LINEAGE |
| repo-000778 | BMDSoftware/Biomni-AD | Organization | 1 | 0 | 0 | 1 | BIOMNI_AD_LINEAGE |
| repo-000779 | MinZhao2011/Biomni-AD | User | 1 | 0 | 0 | 1 | BIOMNI_AD_LINEAGE |
| repo-000780 | joohy-1/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000781 | takuyatakabatake/Biomni_Weave | User | 1 | 0 | 0 | 1 | NOTEBOOK_ONLY |
| repo-000782 | JHK-DEV-Star/Biomni | User | 2 | 0 | 0 | 2 | JHK_AGENT_LINEAGE |
| repo-000783 | kwskws1998/Biomni | User | 1 | 0 | 0 | 1 | JHK_AGENT_LINEAGE |
| repo-000784 | se7esx/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000785 | svamshantanu/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000786 | m-barthel/Biomni | User | 3 | 0 | 1 | 2 | DIVERGED_SUBSTANTIVE_CANDIDATE |
| repo-000529 | Kaimen-Inc/Biomni-AD | Organization | 9 | 1 | 0 | 8 | BIOMNI_AD_LINEAGE |
| repo-000290 | nyu-vis-krueger-group/Biomni | Organization | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000159 | Dandanzzi/Biomni | User | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000453 | Infopathways/Biomni | Organization | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_CANDIDATE |
| repo-000122 | NaveedUrRehman787/Biomni | User | 2 | 1 | 0 | 1 | FORMAT_ONLY |
| repo-000118 | xigyou/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000119 | yy7204/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000120 | Ekkoone/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000121 | BiotechPrivate/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000123 | rvilvendhan/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000124 | KalinNonchev/Biomni | User | 34 | 32 | 1 | 1 | PR_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000129 | explorerwjy/Biomni | User | 34 | 32 | 0 | 2 | BENCHMARK_UNIQUE |
| repo-000133 | little2b/Biomni | User | 33 | 31 | 0 | 2 | SUBSTANTIVE_UNIQUE |
| repo-000125 | jananthan30/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: BENCHMARK_UNIQUE=1, BIOMNI_AD_LINEAGE=4, DIVERGED_SUBSTANTIVE_CANDIDATE=2, FORMAT_ONLY=1, JHK_AGENT_LINEAGE=2, NOTEBOOK_ONLY=1, NO_UNIQUE_CHANGE=10, PR_LINEAGE_PLUS_FORMAT_ONLY=1, SUBSTANTIVE_UNIQUE=3.

## Normalized lineages

### Biomni-AD / AD Workbench lineage

- alexs42 head: 40 unique commits; BMDSoftware/MinZhao exact shared head: 71.
- Those heads are strict subsets of later Kaimen-Inc branch histories.
- Ten observed heads contain a 40-commit common core and a 130-commit union.
- Kaimen `feat/repl-session-isolation` is the latest committed experimental head
  (125 commits) but `biomni-ad` and attribution/data branches retain side commits;
  no single mechanical canonical version is selected yet.
- Capabilities include an AD1 agent, AD data catalogs/downloading, Chainlit UI,
  Docker/fleet deployment, run registry/observability, gateway identity/status,
  lazy data fetching, credentials, session isolation, and optional sign-in.
- License, Alzheimer-data access terms, authentication, workspace isolation,
  secret handling, and deployment security require deep review.

### JHK / kwskws agent-architecture lineage

- JHK main and master each expose 20 unique commits with an 18-commit intersection.
- kwskws main contains both histories and adds three commits (25-commit union).
- Advertised changes include multi-user/parallel architecture, separate planning
  and execution, human approval of plans, token controls, and support-tool changes.

## Other substantive candidates

- `m-barthel/Biomni`: 54 ahead / 87 behind, 35 files; commercial-mode and
  licensing-aware data filters plus model/environment fixes. A separate `vlad`
  branch has no common ancestor; it is excluded from Biomni lineage.
- `nyu-vis-krueger-group/Biomni`: 20 commits/10 files adding a Bioset server,
  plotting explanations, bookmarks, prompts, and image fixes.
- `Dandanzzi/Biomni`: five commits/17 files adding synthetic-lethality and
  organoid synthetic-lethality tools and descriptions.
- `Infopathways/Biomni`: 219 ahead / 132 behind across 101 files; Azure/Gradio
  deployment and a relocated app tree. It remains a diverged candidate pending
  patch-level overlap analysis.
- `explorerwjy/Biomni`: one-commit Eval1 saturation-audit benchmark/scaffold.
- `little2b/Biomni`: two commits/28 files adding a deployable web UI, Docker
  distribution, tests, and skills wrappers.

## Non-substantive and duplicate surfaces

- Ten repositories have only upstream-known heads.
- `takuyatakabatake/Biomni_Weave` adds one Colab notebook while 100 commits behind.
- `NaveedUrRehman787` is an ImgBot image optimization only.
- KalinNonchev has exact PR #312 plus a pre-commit formatting head.
- BMDSoftware and MinZhao share exact head `1be930c4948ed87cb4525c8d51f1f76a0ac7c287`.
- Three active forks share pre-commit head `dee301f00d0557dbe77014a4e0f8824bf48a7813`.

## Identity boundary

- User owners with substantive unique commits enter P.
- Organization owners (BMDSoftware, Kaimen-Inc, nyu-vis-krueger-group,
  Infopathways) remain repository-owner entities and are not assigned person IDs.

## Evidence

- Authenticated GraphQL branch inventory and owner-type responses.
- Serialized compare responses for 23 unique non-PR heads.
- Local SHA comparison against all upstream branches and canonical PR-head tables.

## Next action

Decompose the two multi-repository lineages into features/implementations, perform
security/license deep audits, and continue bounded screening.
