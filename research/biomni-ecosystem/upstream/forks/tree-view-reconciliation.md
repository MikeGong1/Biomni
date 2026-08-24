# Fork Tree View Reconciliation

Observed at: `2026-08-22T21:36:20Z`

Evidence classification: repository links and set arithmetic are `FACT`; the
reason for membership differences between surfaces is `UNKNOWN`.

The GitHub Network tree view at
https://github.com/snap-stanford/Biomni/network/members exposes 690 distinct
fork repository links after excluding the upstream repository. Exhausted REST
`List forks` pagination had produced 683 distinct links.

## Set reconciliation

| Measure | Count |
|---|---:|
| Current Network tree links | 690 |
| Earlier REST snapshot links | 683 |
| Intersection | 679 |
| Tree-only | 11 |
| REST-only | 4 |
| Union of observed identities | 694 |
| Net tree minus REST count | 7 |

The requested seven-count gap is therefore not seven identities that can be
selected directly. Correct recovery requires adding all 11 tree-only identities
and retaining four earlier REST-only identities with a current-tree-absent marker.

## Tree-only identities added

| Repository ID | Repository |
|---|---|
| `repo-000776` | `zhaoyanh/Biomni` |
| `repo-000777` | `alexs42/Biomni-AD` |
| `repo-000778` | `BMDSoftware/Biomni-AD` |
| `repo-000779` | `MinZhao2011/Biomni-AD` |
| `repo-000780` | `joohy-1/Biomni` |
| `repo-000781` | `takuyatakabatake/Biomni_Weave` |
| `repo-000782` | `JHK-DEV-Star/Biomni` |
| `repo-000783` | `kwskws1998/Biomni` |
| `repo-000784` | `se7esx/Biomni` |
| `repo-000785` | `svamshantanu/Biomni` |
| `repo-000786` | `m-barthel/Biomni` |

## Earlier REST-only identities absent from current tree

| Repository ID | Repository |
|---|---|
| `repo-000156` | `Unity-Educational-Formation/Biomni` |
| `repo-000639` | `smartyhouses/Biomni` |
| `repo-000656` | `AdamBear/Biomni` |
| `repo-000661` | `kira-offgrid/Biomni` |

No identity was deleted from history, and no cause was inferred. Possible causes
such as deletion, visibility change, detachment, rename, or snapshot timing remain
unproven. Current public-tree coverage is 690/690; the durable union contains 694
repository identities.
