# Public Fork Unique-Change Screening — Batch 028

Parent verification: `VERIFIED`. Scope: terminal 19 active unscreened fork
identities. One serialized authenticated GraphQL query resolved every repository
and returned all 19 branch refs without pagination or errors. Every head is
already present in the frozen upstream OID set. No PR, previously screened, new,
or compare target exists in this batch.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000742 | gpertea/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000741 | 410aaaa/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000740 | imeMFK01/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000739 | zhanglabxmu/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000738 | gyori-andris/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000734 | Takeya1/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000774 | hubayirp/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000772 | mzabolocki/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000771 | BioInfo/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000770 | Manish-GenAI/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000769 | Josephrp/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000768 | BalmDeveloper/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000767 | GGenomics/Biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000766 | fraware/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000765 | omni2023/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000764 | ivorobyev/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000763 | HengL2022/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000762 | OtterLawyer/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000761 | tomchapin/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification count: NO_UNIQUE_CHANGE=19.

## Findings

- The six newest terminal targets all retain upstream head `d043e97...`; the
  remaining 13 retain upstream head `67e542a...`. Exact commit identity, rather
  than repeated timestamps or repository age, is the classification basis.
- `GGenomics` is an Organization; the other 18 owners are User accounts. Owner
  type does not affect branch classification and upstream-only ownership does not
  establish a substantive contribution.
- No comparison, blob retrieval, dependency installation, package execution,
  notebook execution, or test run was necessary.

## Identity boundary

- No new person enters P. The Organization is not a person, and the User owners
  have no substantive unique fork authorship in this bounded batch.

## Evidence and limits

- Target IDs and names exactly match all 19 identities left unscreened after
  batch 027. All returned `nameWithOwner` values match their targets.
- Every `refs.totalCount` equals its returned node count and every `hasNextPage`
  is false. `19 upstream + 0 PR + 0 screened + 0 new = 19` closes the terminal
  public branch set.
- The durable 694-identity union is now processed 694/694. Four identities remain
  explicitly `UNAVAILABLE_CURRENT` from earlier batches because GitHub no longer
  returns a public repository object; completion means every observed identity
  was processed with its limitation preserved, not that inaccessible code was
  reconstructed or silently classified.
- Public GitHub cannot expose private, deleted, or local unpushed work. Screening
  is complete for the reconciled public identity universe observed by this study.

## Next action

Proceed from identity screening to the pending people merge and lineage/feature
decomposition. This batch adds no change, lineage, implementation, feature, or
person ID.
