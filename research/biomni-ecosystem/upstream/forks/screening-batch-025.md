# Public Fork Unique-Change Screening — Batch 025

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query resolved 23 repositories
and returned all 24 branch refs without pagination. Every resolved branch head is
already present in the frozen upstream OID set. `AdamBear/Biomni` and
`smartyhouses/Biomni` returned GitHub `NOT_FOUND`; neither produces a repository
object, branch inventory, or inferred current-content claim.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000656 | AdamBear/Biomni | UNKNOWN | 0 | 0 | 0 | 0 | 0 | UNAVAILABLE_CURRENT |
| repo-000655 | lamardealmaker/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000653 | dangnammta/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000652 | fuxiaoyi/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000650 | anilyagiz/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000649 | omidvarnia/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000648 | AngeAnjara/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000647 | jonasspezia/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000645 | bwhmore/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000644 | asdlei99/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000643 | ACNoCodeApps/Biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000640 | europower90/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000639 | smartyhouses/Biomni | UNKNOWN | 0 | 0 | 0 | 0 | 0 | UNAVAILABLE_CURRENT |
| repo-000638 | saifjishan/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000637 | GRoberson/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000636 | CLIC-Ethiopia/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000635 | alatbaja/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000632 | titolindj/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000631 | hbcbh1999/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000630 | Keppler55B/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000629 | Arianit94/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000628 | RonotS/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000627 | BrunoScaglione/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000626 | kelvinrrivera/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000625 | SandeepRed/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: NO_UNIQUE_CHANGE=23 and UNAVAILABLE_CURRENT=2.

## Findings

- All 24 refs exposed by the 23 available repositories exactly match commits
  already indexed in the frozen upstream universe. No fork-specific diff remains
  to compare or normalize.
- GitHub returned `NOT_FOUND` for `AdamBear/Biomni` and
  `smartyhouses/Biomni`. Public evidence cannot distinguish deletion, renaming,
  transfer, visibility change, or another cause. Both remain explicit
  `UNAVAILABLE_CURRENT` limitations rather than no-unique assertions.
- The earlier REST inventory remains historical evidence that each identity was
  public at its observation time. It does not establish current availability or
  reveal inaccessible branch content.

## Identity boundary

- No new person enters P. Available repositories contain only upstream-known
  heads; unavailable repositories provide no current branch authorship evidence.
- Organization ownership does not create a person record.

## Evidence and limits

- Target IDs, names, and order match the next 25 canonical unscreened active fork
  identities. All 23 returned names match their targets; all returned ref counts
  equal node counts and every `hasNextPage` is false.
- `24 upstream + 0 PR + 0 screened + 0 new = 24` closes the available branch set.
  No compare request was needed or made.
- `UNAVAILABLE_CURRENT` does not state which inaccessible-repository condition
  applies and does not claim that historical code lacked unique changes.

## Next action

Continue the next bounded active-fork batch. This batch produces no new change,
lineage, implementation, feature, or person ID.
