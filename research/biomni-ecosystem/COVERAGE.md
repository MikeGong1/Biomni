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
| Fork unique-change screening | 694 | 425 | 0 | batches 001–017 complete | PARTIAL |

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

## People and repositories

| Collection | Discovered | Processed/screened | Deep audited | Pagination | Status |
|---|---:|---:|---:|---|---|
| Code-visible people | 131 user logins + 1 bot; 56 raw tuples unresolved | 131 user logins + 1 bot; 56 tuples preserved | 0 | contributor/history/PR authors complete; fork screening partial | PARTIAL |
| Person public repositories | unknown | 0 | 0 | not started | NOT_STARTED |
| snap-stanford public repositories | 92 | 92 | 0 | exhausted | COMPLETE |
| snap-stanford public members | 6 | 6 | 0 | exhausted | COMPLETE |
| Public fork repository identities | 694 | 694 | 0 | reconciled | COMPLETE |

The first 83 user logins are the canonical union of public organization members,
contributors, and all 182 open/merged/closed-unmerged PR authors. Forty-five
additional substantive unique fork owners and three non-owner substantive fork-
branch contributors bring the human account count to 131. One contributor/PR bot
is stored but excluded from that count. Raw commit tuples are not silently mapped
to accounts.

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
