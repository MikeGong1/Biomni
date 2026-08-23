# Public Fork Unique-Change Screening — Batch 027

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query resolved all 25
repositories and returned all 26 branch refs without pagination or errors.
Twenty-five heads are already present in the frozen upstream OID set; the
remaining head is an exact, previously inventoried closed-unmerged PR head.
There are no previously screened or new heads and no compare request was needed.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000715 | ngoldbla/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000713 | ryan-castner/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000712 | owenhowell1/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000711 | Chaojie-Wang/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000710 | HemanthIITJ/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000708 | happydog45/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000735 | robertsousasantos/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000759 | ONERAI/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000733 | Limsym/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000731 | xueyunlong12589/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000730 | xcxtx8/Biomni_cx | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000756 | erhuve/Biomni | User | 2 | 1 | 1 | 0 | 0 | EXACT_PR_LINEAGE |
| repo-000760 | mitultiwari/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000758 | truong128/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000755 | exosome/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000754 | standardgalactic/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000753 | lw3259111/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000752 | jinlimed/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000751 | Jayoel/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000750 | 54457616/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000749 | sunilchem/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000748 | sunnyrajshrestha/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000747 | shameer/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000744 | SSunkara/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000743 | iMufan0824/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: NO_UNIQUE_CHANGE=24 and EXACT_PR_LINEAGE=1.

## Findings

- `erhuve/Biomni:docs/erhuve/readme-typo@5cddda2...` exactly matches the
  already inventoried head of closed-unmerged PR #2. The PR is a README-only
  typo correction and is retained only as PR lineage, not as a new fork change.
- Every other branch head is an exact frozen-upstream commit identity. Shared
  timestamps and repeated default heads across the older forks do not create
  independent change records.
- No comparison, blob retrieval, dependency installation, package execution,
  notebook execution, or test run was necessary.

## Identity boundary

- No new person enters P. `erhuve` is already normalized as
  `person-github-000053` through the complete PR-author inventory; upstream-only
  fork ownership is insufficient for adding the other 24 owners.

## Evidence and limits

- Target IDs and names exactly match the next 25 unscreened active identities in
  canonical repository order. All returned `nameWithOwner` values match targets.
- All `refs.totalCount` values equal returned node counts and every
  `hasNextPage` is false. `25 upstream + 1 PR + 0 screened + 0 new = 26` closes
  the public branch set for this bounded batch.
- Public GitHub cannot expose private, deleted, or local unpushed work; conclusions
  are limited to the public branch surfaces observed at the recorded time.

## Next action

Screen the terminal 19 observed fork identities. This batch produces no new
change, lineage, implementation, feature, or person ID.
