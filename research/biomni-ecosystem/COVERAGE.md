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
| PRs: open | 38 | 38 | 1 | exhausted | COMPLETE |
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
| Canonical accounts with repository status closed | 161 | 161 | 0 | 158 User cursors exhausted + 2 Bots N/A + 1 User unavailable; 0 pending | COMPLETE |
| Person public repositories | 6912 discovered from available processed Users; one unavailable User denominator unknown | 6912 metadata-screened | 0 | all 158 available User owner connections exhausted; one unavailable | PARTIAL |
| External HIGH person-repository records | 2272 | 2272 normalized | 1551 | 111 prior exclusions; external batches 001–033 complete; 573 queued records remain | PARTIAL |
| External HIGH lineage families | 2069 | 2069 normalized | 1462 | stable deterministic queue orders 1–2069; external batches 001–033 complete; 607 not deep-audited | PARTIAL |
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

Person-repository batch 006 exhausted `person-github-000052`–`000061`: 383
repositories, six existing Biomni fork IDs and 377 new IDs. Screening produced
215 HIGH, 20 POSSIBLE, 62 LOW, and 86 IRRELEVANT. Cumulative coverage is 2,278
relations: 701 HIGH, 338 POSSIBLE, 561 LOW, and 678 IRRELEVANT.

Person-repository batch 007 closed `person-github-000062`–`000071`: nine
available Users yielded 190 repositories; lwsinclair remained unavailable. Six
existing IDs were reused and 184 added. Screening produced 85 HIGH, 16 POSSIBLE,
55 LOW, and 34 IRRELEVANT. Cumulative: 786 HIGH, 354 POSSIBLE, 616 LOW, 712
IRRELEVANT.

Person-repository batch 008 exhausted `person-github-000072`–`000081`: all ten
Users were available and yielded 978 repositories across 23 successful GraphQL
pages. Eight existing Biomni IDs were reused and 970 new IDs added. Screening
produced 149 HIGH, 40 POSSIBLE, 609 LOW, and 180 IRRELEVANT. Cumulative: 935
HIGH, 394 POSSIBLE, 1,225 LOW, and 892 IRRELEVANT.

Person-repository batch 009 exhausted `person-github-000082`–`000091`: all ten
Users were available and yielded 1,690 repositories across 39 successful GraphQL
pages. Ten existing fork IDs were reused and 1,680 new IDs added. Screening
produced 676 HIGH, 136 POSSIBLE, 590 LOW, and 288 IRRELEVANT. Cumulative: 1,611
HIGH, 530 POSSIBLE, 1,815 LOW, and 1,180 IRRELEVANT.

Person-repository batch 010 exhausted `person-github-000092`–`000101`: all ten
Users were available and yielded 310 repositories across 11 successful GraphQL
pages. Ten existing fork IDs were reused and 300 new IDs added. Screening
produced 96 HIGH, 31 POSSIBLE, 83 LOW, and 100 IRRELEVANT. Cumulative: 1,707
HIGH, 561 POSSIBLE, 1,898 LOW, and 1,280 IRRELEVANT.

Person-repository batch 011 exhausted `person-github-000102`–`000111`: all ten
Users were available and yielded 266 repositories across ten successful GraphQL
pages. Ten existing fork IDs were reused and 256 new IDs added. Screening
produced 60 HIGH, 17 POSSIBLE, 41 LOW, and 148 IRRELEVANT. Cumulative: 1,767
HIGH, 578 POSSIBLE, 1,939 LOW, and 1,428 IRRELEVANT.

Person-repository batch 012 exhausted `person-github-000112`–`000121`: all ten
Users were available and yielded 269 repositories across 11 successful GraphQL
pages. Ten existing fork IDs were reused and 259 new IDs added. Screening
produced 101 HIGH, 25 POSSIBLE, 74 LOW, and 69 IRRELEVANT. Cumulative: 1,868
HIGH, 603 POSSIBLE, 2,013 LOW, and 1,497 IRRELEVANT.

Person-repository batch 013 exhausted `person-github-000122`–`000131`: all ten
Users were available and yielded 346 repositories across ten successful GraphQL
pages. Seven existing fork IDs were reused and 339 new IDs added. Screening
produced 152 HIGH, 21 POSSIBLE, 61 LOW, and 112 IRRELEVANT. Cumulative: 2,020
HIGH, 624 POSSIBLE, 2,074 LOW, and 1,609 IRRELEVANT.

Person-repository batch 014 exhausted `person-github-000132`–`000141`: all ten
Users were available and yielded 374 repositories across 11 successful GraphQL
pages. Eight existing fork IDs were reused and 366 new IDs added. Screening
produced 203 HIGH, 26 POSSIBLE, 59 LOW, and 86 IRRELEVANT. Cumulative: 2,223
HIGH, 650 POSSIBLE, 2,133 LOW, and 1,695 IRRELEVANT.

Person-repository batch 015 closed `person-github-000142`–`000151`: nine User
connections were exhausted in nine GraphQL pages and yielded 129 repositories;
Copilot was marked not applicable as a Bot. Four existing fork IDs were reused
and 125 new IDs added. Screening produced 38 HIGH, 17 POSSIBLE, 18 LOW, and 56
IRRELEVANT. Cumulative: 2,261 HIGH, 667 POSSIBLE, 2,151 LOW, and 1,751
IRRELEVANT.

Person-repository batch 016 exhausted terminal IDs `person-github-000152`–
`000161`: ten available Users yielded 82 repositories in ten GraphQL pages. One
existing fork ID was reused and 81 new IDs added. Screening produced 11 HIGH,
3 POSSIBLE, 24 LOW, and 44 IRRELEVANT. Final available-User total: 6,912
relations — 2,272 HIGH, 670 POSSIBLE, 2,175 LOW, and 1,795 IRRELEVANT.

Phase 8 normalized all 2,272 HIGH records. The 111 records already carrying a
completed Biomni `fork_screen_status` remain in that prior audit surface; the
remaining 2,161 records collapse to 2,069 external families. Sixty-six duplicate
families contain 158 records, and 513 families contain an in-database independent
source member. Scheduling tiers are A 68, B 911, and C 1,090. The tier is only a
queue heuristic, not an integration score. Static batch 001 inspected ezST,
SciAgent-Skills, and Drug-Discovery-Safety-Skills at immutable heads. ezST is now
deep-audited and resolved as a derived Biomni PR #330 lineage. Drug-Discovery-
Safety-Skills is deep-audited after all 33 authority sources were checked and is
rejected as-is. SciAgent-Skills is deep-audited after all 203 Skills, 327 source
files, 39 PRs and 34 forks were processed; all Skills are rejected as-is. Batch
001 is complete 3/3. Batch 002 resolved queue orders 2–4 by comparing five bounded
forks and all 24 native heads against 592 source heads: two unique heads are
generated artifacts and one is exact open DOC_ONLY Scanpy PR #4311, leaving zero
substantive unique code. Stable queue orders are not renumbered after resolution.
Batch 003 processed seven more bounded forks across K-Dense, Latch and Awesome
Medical AI. Four K-Dense change sets and three lineages preserve the merged Kuan
and BIDS Skills, fork-only API fixes and open DataLad PR; all direct adoption is
rejected. Latch is exact source and the Awesome delta is one DOC_ONLY PR row.
Batch 004 closed three additional awesome-list families: two heads-only deltas
were exact source PR refs and the Pathology fork was a source ancestor. All
bounded contributions were merged/open DOC_ONLY catalog rows; no implementation
or capability ID was added. Accelerated batch 005 then closed exact queue orders
13–62: 50 families and 58 bounded repository records. The result distribution is
22 substantive candidates, 22 no-unique closures, three DOC_ONLY closures and
three empty repositories. Parent reduction allocated 22 Change and four Lineage
IDs, rejected every direct-adoption path, and withheld Feature/Implementation
IDs.

Accelerated batch 006 closed exact queue orders 63–112: 50 families and 64
bounded repository records. The result distribution is 21 substantive
candidates, 26 no-unique/source-lineage closures, and three
DOC/metadata/maintenance-only closures. Parent reduction allocated 26 Change and
12 Lineage IDs, rejected every direct-adoption path, and withheld
Feature/Implementation IDs. Parent validation also caught and reversed a stale
five-order Biomni shard before canonical write and added exact reverse-completeness
identity gates.

Accelerated batch 007 closed exact queue orders 113–162: 50 families and 53
bounded repository records. The result distribution is 19 substantive
candidates, 26 DOC/metadata/maintenance-only and five no-unique/source-lineage
closures. Parent reduction allocated 28 Change and nine Lineage IDs, rejected or
deferred every direct-adoption path, and withheld Feature/Implementation IDs.

Accelerated batch 008 closed exact queue orders 163–212: 50 families and 56
bounded repository records. The result distribution is 21 substantive
candidates, 19 DOC/metadata/maintenance-only, nine no-unique/source-lineage and
one non-biomedical false positive. Parent reduction allocated 29 Change and 12
Lineage IDs, rejected or deferred every direct-adoption path, gave failed
GraphQL/HTTP502 artifacts zero evidence weight, and withheld
Feature/Implementation IDs.

The fifth accelerated checkpoint, queue orders 213–262 (50 families), is
`NOT_STARTED` for GPT Pro handoff. One just-dispatched worker was interrupted at
the user's request before any accepted MAP result; no Batch 009 family enters the
processed numerator. The next agent must derive exact bounded identity sets from
current `repositories.jsonl` before scheduling.

All 161 canonical account statuses are now closed. All 158 available User owner
connections are exhausted, both Bots are not applicable, and lwsinclair remains
explicitly unavailable current. Therefore account-status closure is COMPLETE,
while the public-repository collection remains PARTIAL rather than pretending the
unavailable User has a known repository denominator.

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


## External deep-audit completion ledger

- Batch 009: completed exact queue orders 213–262; cumulative 262/2069 families and 301/2124 queued records.
- Batch 010: completed exact queue orders 263–312; cumulative 312/2069 families and 357/2124 queued records.
- Batch 011: completed exact queue orders 313–362; cumulative 362/2069 families and 408/2124 queued records.
- Batch 012: completed exact queue orders 363–412; cumulative 412/2069 families and 458/2124 queued records.
- Batch 013: completed exact queue orders 413–462; cumulative 462/2069 families and 518/2124 queued records.
- Batch 014: completed exact queue orders 463–512; cumulative 512/2069 families and 569/2124 queued records.
- Batch 015: completed exact queue orders 513–562; cumulative 562/2069 families and 620/2124 queued records.
- Batch 016: completed exact queue orders 563–612; cumulative 612/2069 families and 673/2124 queued records.
- Batch 017: completed exact queue orders 613–662; cumulative 662/2069 families and 729/2124 queued records.
- Batch 018: completed exact queue orders 663–712; cumulative 712/2069 families and 782/2124 queued records.
- Batch 019: completed exact queue orders 713–762; cumulative 762/2069 families and 834/2124 queued records.
- Batch 020: completed exact queue orders 763–812; cumulative 812/2069 families and 885/2124 queued records.
- Batch 021: completed exact queue orders 813–862; cumulative 862/2069 families and 936/2124 queued records.
- Batch 022: completed exact queue orders 863–912; cumulative 912/2069 families and 988/2124 queued records.
- Batch 023: completed exact queue orders 913–962; cumulative 962/2069 families and 1039/2124 queued records.
- Batch 024: completed exact queue orders 963–1012; cumulative 1012/2069 families and 1090/2124 queued records.
- Batch 025: completed exact queue orders 1013–1062; cumulative 1062/2069 families and 1142/2124 queued records.
- Batch 026: completed exact queue orders 1063–1112; cumulative 1112/2069 families and 1195/2124 queued records.
- Batch 027: completed exact queue orders 1113–1162; cumulative 1162/2069 families and 1247/2124 queued records.
- Batch 028: completed exact queue orders 1163–1212; cumulative 1212/2069 families and 1298/2124 queued records.
- Batch 029: completed exact queue orders 1213–1262; cumulative 1262/2069 families and 1349/2124 queued records.
- Batch 030: completed exact queue orders 1263–1312; cumulative 1312/2069 families and 1399/2124 queued records.
- Batch 031: completed exact queue orders 1313–1362; cumulative 1362/2069 families and 1449/2124 queued records.
- Batch 032: completed exact queue orders 1363–1412; cumulative 1412/2069 families and 1500/2124 queued records.
- Batch 033: completed exact queue orders 1413–1462; cumulative 1462/2069 families and 1551/2124 queued records.
