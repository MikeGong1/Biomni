# Public Fork Unique-Change Screening — Batch 006

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One GraphQL query returned all 122 branch refs without pagination. Three new heads
were compared serially; an exact open PR #292 head was not re-compared.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000198 | yangwao/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000199 | ksu-oor-archive/biomni | Organization | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000200 | samartho4/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000201 | ALmandop/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000202 | FuLab-ZhaoSun/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000203 | haiwu00/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000775 | krish240574/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000204 | AR-Shicheng/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000205 | lzyyyan/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000206 | jianghaixu/Biomni-AI- | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000207 | bch9248/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000208 | forkgitss/snap-stanford-Biomni | Organization | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000270 | knowledgesystems/Biomni | Organization | 2 | 1 | 1 | 0 | PR_LINEAGE_ONLY |
| repo-000209 | baoruikang/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000210 | agisota/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000211 | smallelephant9516/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000212 | fgld216/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000213 | Nikolahuang/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000215 | marielacour/Biomni | User | 1 | 0 | 0 | 1 | CI_ONLY |
| repo-000214 | fongchun/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000217 | dragoninmine-pixel/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000218 | hbnubob/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000219 | YumnCYT/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000220 | KaiyanM/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000221 | sharmalabs/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: CI_ONLY=1, FORMAT_ONLY=3, NO_UNIQUE_CHANGE=20, PR_LINEAGE_ONLY=1.

## Findings

- Twenty repositories expose only upstream-known heads.
- ksu-oor-archive and FuLab-ZhaoSun share one pre-commit head; forkgitss has a
  separate pre-commit-only head.
- knowledgesystems has exact open PR #292 (Docker deployment) and no additional
  unique branch change.
- marielacour adds only a generic Python-application GitHub Actions workflow.

## Evidence

- Authenticated GraphQL branch/owner inventory.
- Three serialized compare responses and canonical open-PR head mapping.

## Next action

Continue the next bounded active-fork batch.
