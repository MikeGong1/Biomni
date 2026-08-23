# Coverage

Status: PARTIAL

## Initialization

- Research branch: COMPLETE (`research/biomni-ecosystem-audit`)
- Branch base verified: COMPLETE (`MikeGong1/Biomni` main `400c1f366b96a35ca253e13c9b06c5076af41d65`)
- Methodology: COMPLETE (scope, evidence, deduplication, security, limitations)
- Structured database foundation: COMPLETE
- Upstream baseline: COMPLETE (`snap-stanford/Biomni` main `400c1f366b96a35ca253e13c9b06c5076af41d65`)

## Biomni upstream archaeology

| Collection | Discovered | Processed/indexed | Deep audited | Pagination | Status |
|---|---:|---:|---:|---|---|
| Branches | 33 | 33 | 0 | exhausted | COMPLETE |
| PRs: open | 38 | 38 | 0 | exhausted | COMPLETE |
| PRs: merged | 111 | 111 | 0 | exhausted | COMPLETE |
| PRs: closed-unmerged | 33 | 33 | 0 | exhausted | COMPLETE |
| Commits | 487 | 487 | 0 | exhausted | COMPLETE |
| Public fork REST snapshot | 683 | 683 | 0 | exhausted | COMPLETE |
| Current Network tree view | 690 | 690 | 0 | full DOM enumerated | COMPLETE |
| Fork identity union | 694 | 694 | 0 | reconciled | COMPLETE |
| Fork unique-change screening | 694 | 694 | 0 | batches 001–028 exhausted | COMPLETE |

All commit batches contain 111 explicit subject-to-PR mappings. Network tree/REST
reconciliation found 679 common, 11 tree-only, and four REST-only identities: the
current tree is complete at 690/690 and the durable union is 694. Fork-branch
inspection, no-unique-change, and substantive unique-change counts use that union.

Fork screening batch 001: 16 no-unique, three PR-lineage classes, three
substantive unique, one format-only, one docs-only, and one non-feature utility.

Fork screening batch 002: 10 no-unique; four Biomni-AD lineage surfaces; two
JHK/kwskws lineage surfaces; three independent substantive unique; two diverged
substantive candidates; one benchmark, one notebook, one format-only, and one
PR-plus-format lineage.

Fork screening batch 003: 19 no-unique, two format-only, one config-only, one
PR-plus-format lineage, one diverged candidate, and one substantive unique.

Fork screening batch 004: 21 no-unique, one unavailable-current, one exact PR
lineage, one format-only, and one non-feature notebook/CI change.

Fork screening batch 005: 17 no-unique, one JHK-derived substantive extension,
three substantive unique, two format-only, and two PR-plus-format lineages.

Fork screening batch 006: 20 no-unique, three format-only, one exact PR lineage,
and one CI-only change.

Fork screening batch 007: 18 no-unique, four substantive unique, one format-only,
and two exact open-PR lineages.

Fork screening batch 008: 17 no-unique, five substantive/derived, one docs-only,
one format-only, and one exact PR-lineage-only repository. Three branch/change
lineages were normalized; one unrelated-history head remains content-unknown.

Fork screening batch 009: 19 no-unique, three substantive, two documentation
classes, and one exact PR lineage. One four-branch substantive lineage was
normalized; shared branch heads were counted once at the change level.

Fork screening batch 010: 17 no-unique, three substantive, three format-only,
one exact PR lineage, and one PR-plus-format lineage. Two nested substantive
branch chains were normalized; shared maintenance heads were counted once.

Fork screening batch 011: 19 no-unique, five substantive repository classes,
and one PR-plus-format lineage. Six changes and two lineages were normalized;
parallel MyGene SHAs were collapsed by identical parent/tree/patch evidence.

Fork screening batch 012: 17 no-unique, five substantive repository classes,
two exact PR lineages, and one reused formatting surface. Seven changes and two
lineages were normalized; one 300-file-capped product DAG remains partial.

Fork screening batch 013: 21 no-unique, one substantive, one documentation-plus-
personal-config class, one reused format surface, and one PR-plus-dependency class.
One diverged execution/provider change was retained.

Fork screening batch 014: 19 no-unique, five substantive repository classes,
and one notebook-only fork. Six changes and two multi-branch lineages were
normalized; three PMK heads remain no-common-ancestor surfaces.

Fork screening batch 015: 16 no-unique, two independent substantive changes,
one substantive alternative DAG, two dependency-only surfaces, one reused
formatting head, one exact PR lineage, one documentation class, and one
notebook-only fork. Three changes and one lineage were normalized.

Fork screening batch 016: 14 no-unique, five substantive repository classes,
four dependency-only fork refs, one configuration stub, and one exact PR lineage.
Five changes and one cross-repository exact-component lineage were normalized;
48 opaque model files were deduplicated against the earlier PMK surface.

Fork screening batch 017: 22 no-unique and three substantive/mixed repository
classes. Three historical changes and two lineages were normalized: an early
registration prototype was linked to its later upstream integration, while three
Synapse code blobs were deduplicated and only the exploratory notebook remained.

Fork screening batch 018: 17 no-unique, five substantive repository classes, two
exact PR lineages, and one empty-net history. Five changes and three lineages were
normalized; a 330-commit chain was fully paginated and omitted critical blobs were
retrieved for the reduced package and VS Code extension audits.

Fork screening batch 019: 21 no-unique, two substantive product lineages, one
exact closed-unmerged PR lineage, and one excluded unattributed experiment. Two
changes and two lineages were normalized. A 322-commit nested chain was fully
paginated; a complete 19,316-item tree and selected immutable blobs closed the
compare-cap gap for Reti, while the exact maximal Streamlit blob proved critical
Synapse profile injection and cross-session credential/data risks.

Fork screening batch 020: 20 no-unique, one historical substantive composite,
one exact-PR-only repository, one upstream patch-equivalent repository, one
image-only bot surface, and one dependency-only bot surface. One change and one
lineage were normalized. Stable patch IDs deduplicated DeepSeek to PR #106 and
the fork streaming hunk to PR #102; canonical history proves its PR #114 revert
and later PR #122/#161 component successors.

Fork screening batch 021: 16 no-unique, three substantive historical prototypes,
two exact-PR-only repositories, three reused-maintenance repositories, and one
non-substantive repository-automation script. Three changes and three lineages
were normalized for parser/self-critic regression, Azure/Bohrium MCP supervision,
and an early ESM embedding prototype conceptually superseded by PR #205.

Fork screening batch 022: 21 no-unique, two README-only repositories, one empty-net
merge history, and one documentation-only repository. No change, lineage, feature,
implementation, or person ID was added. The Chinese guide was statically checked
and found to mix some accurate overview material with systematic inventory/API/
environment errors and unsafe secret-printing guidance.

Fork screening batch 023: 24 repositories expose only upstream-known heads; one
target is currently unavailable through GitHub and remains explicitly unresolved.
No change, lineage, feature, implementation, or person ID was added. All 30 refs
from available repositories were exhausted in one GraphQL page.

Fork screening batch 024: all 25 repositories and 28 branch refs resolved; every
head is already upstream-known. No compare was necessary and no change, lineage,
feature, implementation, or person ID was added.

Fork screening batch 025: 23 repositories expose only upstream-known heads; two
targets are currently unavailable through GitHub and remain explicit limitations.
No compare was necessary and no change, lineage, feature, implementation, or
person ID was added.

Fork screening batch 026: 24 repositories expose only upstream-known heads; one
Organization fork adds a substantive one-commit Docker/uv migration. One change,
one lineage, and one non-owner contributor were normalized. The immutable uv lock
was retrieved, while build-context, unauthenticated Jupyter, dependency coverage,
supply-chain, and license conflicts block direct integration.

Fork screening batch 027: 24 repositories expose only upstream-known heads; one
repository also retains the exact head of already inventoried closed-unmerged PR
#2. No compare was necessary and no change, lineage, feature, implementation, or
person ID was added.

Fork screening batch 028: the terminal 19 repositories and their 19 refs all
resolved to upstream-known heads. No compare was necessary and no canonical ID
was added. All 694 reconciled fork identities have now been processed; four
earlier identities remain explicitly unavailable rather than inferred.

## People and repositories

| Collection | Discovered | Processed/screened | Deep audited | Pagination | Status |
|---|---:|---:|---:|---|---|
| Code-visible GitHub accounts | 159 User-type + 2 Bots; 56 main-history and 26 fork-change raw tuples separately unresolved | 161/161 accounts; all raw tuples preserved without inference | 0 | members/contributors/history/PRs/branches/forks/change-author SHAs exhausted | COMPLETE |
| Canonical accounts with repository status closed | 161 | 51 | 0 | 50 User cursors exhausted + 1 Bot not applicable; 110 accounts pending | PARTIAL |
| Person public repositories | 1895 discovered from processed User accounts; global denominator unknown | 1895 metadata-screened | 0 | all 50 processed User owner connections exhausted; global collection incomplete | PARTIAL |
| snap-stanford public repositories | 92 | 92 | 0 | exhausted | COMPLETE |
| snap-stanford public members | 6 | 6 | 0 | exhausted | COMPLETE |
| Public fork repository identities | 694 | 694 | 0 | reconciled | COMPLETE |

The first 83 human-counted logins plus one bot are the union of public members,
contributors, and 182/182 PR authors. Fork screening added 55 human-counted
substantive owners and seven human-counted non-owner contributors; final exact-SHA
reconciliation added 11 human-counted contributors, three User-type automation
accounts, and one Bot. The canonical total is 161 accounts: 156 human-counted and
five automation/non-human. All 1,791 normalized change SHAs have official author
objects; 96 resolved logins are canonical and 26 no-login raw fork tuples remain
unmapped. The separate 56-tuple frozen-main ledger is also preserved.

Person-repository batch 001 exhausted owner-public-repository cursors for
`person-github-000001`–`000010`: 217 repositories, including three existing
Biomni fork IDs and 214 new IDs. Metadata screening produced 64 HIGH, 56
POSSIBLE, 59 LOW, and 38 IRRELEVANT results. HIGH is a deep-audit queue, not an
integration recommendation; POSSIBLE requires bounded README disambiguation.

Person-repository batch 002 exhausted owner-public-repository cursors for
`person-github-000011`–`000020`: 587 repositories, including seven existing
Biomni fork IDs and 580 new IDs. Metadata screening produced 143 HIGH, 92
POSSIBLE, 121 LOW, and 231 IRRELEVANT results. Cumulative processed-account
coverage is 804 repository relations: 207 HIGH, 148 POSSIBLE, 180 LOW, and 269
IRRELEVANT.

Person-repository batch 004 exhausted `person-github-000032`–`000041`: 500
repositories, eight existing Biomni fork IDs and 492 new IDs. Screening produced
128 HIGH, 70 POSSIBLE, 196 LOW, and 106 IRRELEVANT. Cumulative coverage is 1,509
relations: 387 HIGH, 259 POSSIBLE, 420 LOW, and 443 IRRELEVANT.

Person-repository batch 005 exhausted `person-github-000042`–`000051`: 386
repositories, five existing Biomni fork IDs and 381 new IDs. Screening produced
99 HIGH, 59 POSSIBLE, 79 LOW, and 149 IRRELEVANT. Cumulative coverage is 1,895
relations: 486 HIGH, 318 POSSIBLE, 499 LOW, and 592 IRRELEVANT.

Person-repository batch 003 closed stable IDs `person-github-000021`–`000031`:
10 User cursors yielded 205 repositories, while the intervening Bot was marked
not applicable. Eight existing Biomni lineage IDs were reused and 197 new IDs
allocated. Screening produced 52 HIGH, 41 POSSIBLE, 44 LOW, and 68 IRRELEVANT.
Cumulative coverage is 1,009 relations: 259 HIGH, 189 POSSIBLE, 224 LOW, and 337
IRRELEVANT.

## Commercial

| Collection | Discovered | Verified | Compared to OSS | Reconstruction assessed | Status |
|---|---:|---:|---:|---:|---|
| Public commercial capabilities | 17 grouped behaviors | 17 | 0 | 0 | PARTIAL |

Batch 001 verified 13 grouped Biomni Lab behaviors and four Biomni MCP facts from
official sources. Product-site/search pagination is not provably exhausted; OSS
comparison and reconstruction assessment have not started.

## Completion rule

A bounded collection is `COMPLETE` only when discovered equals processed and
pagination is exhausted. Unknown denominators and unfinished cursors are always
`PARTIAL` or `NOT_STARTED`, never complete.
