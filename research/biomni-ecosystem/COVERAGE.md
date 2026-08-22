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
| Fork unique-change screening | 694 | 125 | 0 | batches 001–005 complete | PARTIAL |

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

## People and repositories

| Collection | Discovered | Processed/screened | Deep audited | Pagination | Status |
|---|---:|---:|---:|---|---|
| Code-visible people | 98 user logins + 1 bot; 56 raw tuples unresolved | 98 user logins + 1 bot; 56 tuples preserved | 0 | contributor/history/PR authors complete; fork screening partial | PARTIAL |
| Person public repositories | unknown | 0 | 0 | not started | NOT_STARTED |
| snap-stanford public repositories | 92 | 92 | 0 | exhausted | COMPLETE |
| snap-stanford public members | 6 | 6 | 0 | exhausted | COMPLETE |
| Public fork repository identities | 694 | 694 | 0 | reconciled | COMPLETE |

The 98 public user logins are the canonical union of public organization members,
contributors, and all 182 open/merged/closed-unmerged PR authors. One contributor/
PR bot is stored but excluded from the human count; fifteen substantive unique fork
owners have now entered P. Raw commit tuples are not silently mapped to accounts.

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
