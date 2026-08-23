# External deep audit batch 002 — fork-only family resolution

Observed at: `2026-08-23T16:09:14Z`

Batch status: **COMPLETE — STATIC_ONLY**

## Canonical decision

Queue orders 2–4 contain five repositories from the bounded person-repository
universe, but every repository is a fork whose authoritative source owner is
outside the code-visible people boundary. The correct question is therefore not
whether the three large upstream projects are useful. It is whether these five
bounded forks add a substantive change that was not already present upstream.

The answer is **no substantive unique code capability in all three families**:

| Queue | Family source | Bounded repositories | Decision |
|---:|---|---:|---|
| 2 | `NVIDIA-BioNeMo/bionemo-recipes` | 2 | exact/one-behind source histories plus a generated MkDocs deployment |
| 3 | `ClawBio/ClawBio` | 1 | stale source history plus an inherited generated benchmark snapshot |
| 4 | `scverse/scanpy` | 2 | source ancestors plus one DOC_ONLY open upstream PR (#4311) |

All five repository records are `DEEP_AUDITED` for this bounded fork-lineage
question and leave the external queue as
`RESOLVED_FORK_LINEAGE_NO_SUBSTANTIVE_UNIQUE_CODE`. The three upstream sources
remain **out-of-scope lineage anchors, not deep-audited repository entities**.
Their 1,198 reported forks were not added to the bounded universe. No Repository,
Person, Change, Lineage, Feature, or Implementation ID is allocated by this batch.

## Acquisition and coverage boundary

Acquisition was serialized. Eight current repository metadata documents and the
five bounded Git mirrors were frozen without using a user token. Three source
mirrors were fetched only as comparison anchors. All mirrors passed
`git fsck --connectivity-only`; repository code, notebooks, tests, workflows,
installers and scientific programs were never executed.

| Surface | BioNeMo source / forks | ClawBio source / fork | Scanpy source / forks |
|---|---:|---:|---:|
| Source public heads | 497 | 19 | 76 |
| Source public tags | 21 | 9 | 102 |
| Bounded fork heads | 3 | 18 | 3 |
| Bounded fork native tags | 0 | 9 | 0 |
| Bounded fork PRs | 0 | 0 | 0 |
| Bounded fork releases | 0 | 0 | 0 |
| Bounded fork child forks | 0 | 0 | 0 |
| Fork-only commits relative to source heads/tags | 1 | 1 | 1 |
| Fork-only commits relative to all public source refs, including PR refs | 1 | 1 | 0 |

GitHub metadata reports 177 BioNeMo, 257 ClawBio and 764 Scanpy source forks.
Those source-side networks are outside `R`: the source owners are not members of
`P`, and the queue entities are only the five already-bounded forks. Source Git
heads/tags were nevertheless fully mirrored so deleted/default-branch assumptions
would not hide a relation.

The fork PR and release endpoints each returned an empty first page. Each fork
metadata record reports zero child forks. Source PR lookup was then restricted to
the three fork-only heads; two had no matching PR and one exactly matched Scanpy
PR #4311. The independent verifier also found its exact SHA under the source's
public `refs/pull/4311/head`; it is unique only relative to source heads/tags, not
relative to all public source refs.

### Tag-count correction

Fetching source refs into a fork mirror caused Git's tag auto-follow behavior to
copy source tags into local `refs/tags`. Two independent workers consequently
reported 21 BioNeMo and 102 Scanpy fork tags after contamination. Parent
verification used direct remote `git ls-remote --heads --tags` and the pre-fetch
clone inventory. The native bounded-fork counts are authoritative:

- `shantanusharma/bionemo-framework`: 2 heads, **0 tags**;
- `dabulseco/bionemo-recipes`: 1 head, **0 tags**;
- `KalinNonchev/ClawBio`: 18 heads, **9 tags**;
- `KalinNonchev/scanpy`: 1 head, **0 tags**;
- `Mr-Milk/scanpy`: 2 heads, **0 tags**.

This correction is why the compact manifest records remote-native tags rather
than post-fetch local tag namespaces.

## Queue order 2 — BioNeMo

### Default histories

The source default head is
`30202cac91e2c23a958bf9bdeff59288f261b9bb` (1,003 commits, 1,224 files).

- `shantanusharma/bionemo-framework` main is the exact same commit and tree:
  ahead 0, behind 0.
- `dabulseco/bionemo-recipes` main is
  `648f4d983392d0c38f2d2da18dea0479cdc650b2`: ahead 0, behind 1.
  The sole missing source commit is the CI repair `30202cac...`; its tree still
  contains 1,224 files.

Neither default history contains a fork-only commit.

### Generated `gh-pages` root

The sole fork-only SHA is
`016de8ab5e43466117e8e7210b1224ca96eb4d78` on the shantanusharma `gh-pages`
branch. It is an orphan/root commit authored and committed by
`github-actions[bot]` with subject
`Deployed 30202ca with MkDocs version: 1.6.1`.

The source has its own orphan `gh-pages` root
`76a175a132b74661ae950effb4a9c40e46c6f08d` with the same subject and source SHA.
Both trees have exactly 1,006 files. Only `sitemap.xml` and its gzip form differ;
the XML difference is 127 build-date substitutions from 2026-08-20 to
2026-08-23. The source workflow explicitly runs `mkdocs build --strict` followed
by `mkdocs gh-deploy --force`.

Of the deployment's 1,006 blobs, 834 are already byte-identical to blobs in the
source tree. The remaining 172 are HTML/JavaScript/CSS/search/sitemap build
artifacts. The copied `.py`, shell, YAML, model documentation and scientific
figures are source documentation assets, not new fork implementations or results.

The deployed site has inherited external JavaScript/font requests and does not
copy the source's top-level Apache-2.0 and third-party notice files into the
deployment root. It also retains old `bionemo-framework` links. These are
attribution/site hygiene observations, not fork-only scientific capability.

Disposition: **generated deployment equivalent; no Change ID**.

## Queue order 3 — ClawBio

The source default head is
`5ca937c18aa78bea939c88105ebdb4cf657b4235` (1,296 commits, 1,456 files). The fork
main `c2c0754ba09e68c1e21edc79a63fa112ed47fd9e` is an upstream ancestor, ahead 0
and behind 95. Across 18 fork heads:

- 15 are exact source heads;
- main and `skill/population-equity-auditor` are source-head ancestors;
- all nine native tags are exact source tag objects;
- only `bot/refresh-benchmark-leaderboard` diverges.

The divergent SHA
`6091df66cb11d0ebdca3633c3c5b94552dcc3e0f` predates the fork's creation. It was
authored by the upstream maintainer, committed by `github-actions[bot]`, and says
the source workflow auto-generated it. It changes only
`bench_runs/latest/aggregate_report.json` and `benchmarks.html` (+123/-75).

The current source branch SHA
`adbaf1fdceba8c9fb4647abe04bc9f3b44a9901d` is a newer run of the same template.
It reports the same 160/182 passing, 87.9% pass rate, one harness error and the
same blocking skills. The 27-line-per-side tree difference updates dates, target
commit, wall clock, Python/platform and nested provenance values. This audit did
not run `clawbio_bench`; the score and scientific/safety claims remain repository
claims, not independently reproduced facts.

The snapshot adds no code, workflow, dependency, test or license logic. The fork
metadata's MIT label must not be generalized to current source Skills, models,
weights or datasets that carry separate terms.

Disposition: **inherited stale generated benchmark snapshot; no Change ID**.

## Queue order 4 — Scanpy

The source default head is
`e6269f5850ba17ca46ad49e86f9e19eb81c33a10` (3,869 commits, 894 files).

- `KalinNonchev/scanpy` master
  `b863ce0477f4afbce1fd5ebc267cc897854c8099` is a source-history ancestor,
  ahead 0 and behind 720.
- `Mr-Milk/scanpy` master
  `532d7b14c8e0d615def56438755a545af92c64d5` is a source-history ancestor,
  ahead 0 and behind 2.
- neither fork has a native tag, PR, release or child fork.

The sole fork-only SHA is
`fedc93ed29d0215822b43894809c8c0b27ffdb8f`. It exactly matches the head of open,
non-draft upstream Scanpy PR #4311, `docs: update 'Plotting with Marsilea' in
how-to`. It changes only
`docs/how-to/plotting-with-marsilea.ipynb` (+1,063/-328); no Scanpy package,
runtime, dependency, CI or test file changes.

Static notebook parsing found 47 cells (20 code, 27 Markdown) versus 33 cells in
the parent. It updates examples to Marsilea 0.8.1 and `anndata.acc.A`, repairs
tracksplot/stacked-violin examples, and adds board composition and
`annotate_stats`. Saved outputs include 13 PNGs and no saved error, but the
notebook was not re-executed in this audit. One significance example treats cells
as independent observations; the notebook itself prominently discloses the
pseudoreplication limitation and recommends formal differential-analysis p-values.

The PR has no human approval in the frozen review surface. A bot could not review
the notebook; a Codecov comment reports successful checks, which is retained only
as external CI evidence. Current source heads do not contain the commit, matching
notebook blob or `annotate_stats` delta.

Disposition: **exact open upstream PR #4311, DOC_ONLY; no independent fork Change
or Feature ID and no direct adoption**. Recheck only if the PR merges, closes or
is materially rewritten.

## Scientific, security and license boundary

No fork-only runtime path, model, scientific algorithm, tool, dependency,
credential flow, shell path or file-mutation behavior was found. BioNeMo and
ClawBio unique commits are generated outputs; Scanpy's unique commit is a saved
documentation notebook. Static inspection does not validate the inherited
upstream projects or any benchmark/model claim.

BioNeMo's source license is stored under `LICENSE/license.txt` with separate
third-party notices; GitHub metadata therefore returns no SPDX identifier. ClawBio
has an MIT root with explicit per-Skill and third-party carve-outs. Scanpy uses
BSD-3-Clause. No license finding turns a generated or DOC_ONLY fork delta into an
integration candidate.

## Persistent records

The five-row machine reduction is
`deep-audit-batch-002-lineage-manifest.jsonl` (SHA-256
`9492776ca7d9993fa5eda095ad4e6ffb9e6a510bf51865d952ca6c75b0742172`). Primary
evidence is `evidence-000158`–`evidence-000162`. The detailed report, manifest and
repository status fields preserve exact source/fork SHAs and relationships without
expanding the people universe or claiming that the three upstream sources were
fully audited.
