# Public Fork Unique-Change Screening — Batch 024

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query resolved all 25
repositories and returned all 28 branch refs without pagination or errors. Every
branch head is already present in the frozen upstream OID set. There are no exact
PR heads, previously screened heads, new heads, or compare requests in this batch.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000686 | nivir/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000685 | shmohammadi86/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000684 | ShantanuNair/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000683 | webclinic017/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000682 | inoue0426/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000681 | saadnaseem/Biomni_SN | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000680 | RalfBarkow/snap-stanford-Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000678 | lyz19990914/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000677 | jdstamp/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000676 | N-damo/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000675 | Synthetic-Intelligence-Alchemist/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000674 | ashtonomy/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000673 | gmh5225/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000672 | xhli2/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000671 | LuyiTian/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000670 | Jibbscript/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000669 | vovanduc/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000668 | cprakashagr/biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000667 | supercoderl/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000664 | demondi/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000663 | PelumiSamuel1234/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000662 | dammanhdungvn/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000660 | AMVamsi/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000658 | Donjae-Wang/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000657 | enricoilha/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification count: NO_UNIQUE_CHANGE=25.

## Findings

- The 25 repositories expose 28 refs but only upstream-known commit identities.
  Multiple public branches in gmh5225, cprakashagr, and Donjae-Wang do not add a
  distinct fork change because their heads are already indexed upstream commits.
- All returned `refs.totalCount` values equal their node counts and every
  `hasNextPage` is false. No unresolved repository, missing ref page, or compare
  surface remains in this bounded batch.

## Identity boundary

- No new person enters P. Repository ownership without substantive unique fork
  authorship is insufficient under the project boundary.

## Evidence and limits

- Target IDs and names exactly match the next 25 unscreened active identities in
  the canonical repository database. All 25 returned `nameWithOwner` values match
  their targets.
- `28 upstream + 0 PR + 0 screened + 0 new = 28` closes the branch set. No compare
  request was needed or made.
- Public GitHub cannot expose private, deleted, or local unpushed work; conclusions
  are limited to the public branch surfaces observed at the recorded time.

## Next action

Continue the next bounded active-fork batch. This batch produces no new change,
lineage, implementation, feature, or person ID.
