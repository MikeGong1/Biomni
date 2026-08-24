# Public Fork Unique-Change Screening — Batch 023

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query resolved 24 repositories
and returned all 30 branch refs without pagination. Every resolved branch head is
already in the frozen upstream OID set. One target, `kira-offgrid/Biomni`, returned
GitHub `NOT_FOUND` and no repository object. No new head, exact PR head, reused
screened head, or compare request exists in this batch.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000617 | fabiodr/Biomni | User | 4 | 4 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000616 | stanleys12/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000614 | rajdeepmondaldotcom/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000613 | Oncorithms/Biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000611 | ashishakkumar/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000610 | statikMan/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000609 | bhengubv/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000608 | nrfernando/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000606 | just4jc/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000605 | vinay1506/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000604 | amir-tmbk/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000603 | not-a-feature/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000601 | shuxiangzhang/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000622 | shiminli957/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000621 | kasulemoses/ellipkom-Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000620 | Elckat0704/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000619 | amitmalda/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000618 | ALEXuH/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000659 | Thiraput01/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000642 | Ginylil/forked-snap-stanford-Biomni | Organization | 3 | 3 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000773 | bkbonde/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000661 | kira-offgrid/Biomni | UNKNOWN | 0 | 0 | 0 | 0 | 0 | UNAVAILABLE_CURRENT |
| repo-000689 | himanshu-zetta/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000688 | SelfAwareApps/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000687 | wangling03/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: NO_UNIQUE_CHANGE=24 and UNAVAILABLE_CURRENT=1.

## Findings

- All 30 refs exposed by the 24 available repositories exactly match commits
  already indexed in the frozen upstream universe. No fork-specific diff remains
  to compare or normalize.
- GraphQL returned `NOT_FOUND` for `kira-offgrid/Biomni`. Public evidence does not
  distinguish deletion, renaming, transfer, visibility change, or another cause.
  The repository is therefore recorded only as `UNAVAILABLE_CURRENT`; it is not
  silently classified as no-unique-change and no historical content is inferred.
- The prior REST inventory remains valid historical evidence that this identity was
  public at its observation time. Current unavailability prevents branch inspection,
  so the entry remains an explicit coverage limitation rather than a completed code
  assertion.

## Identity boundary

- No new person enters P. Available repositories contain only upstream-known heads;
  the unavailable repository supplies no current branch authorship evidence.
- Organization owners remain repositories, not person records.

## Evidence and limits

- Target IDs and names exactly match the next 25 unscreened active identities in the
  canonical repository database. All 24 returned `nameWithOwner` values match their
  targets; all returned `refs.totalCount` values equal their node counts and every
  `hasNextPage` is false.
- `30 upstream + 0 PR + 0 screened + 0 new = 30` closes the available branch set.
  No compare request was needed or made.
- Public GitHub cannot expose private, deleted, renamed-without-redirect, or local
  unpushed work. `UNAVAILABLE_CURRENT` does not claim which condition applies.

## Next action

Continue the next bounded active-fork batch. This batch produces no new change,
lineage, implementation, feature, or person ID.
