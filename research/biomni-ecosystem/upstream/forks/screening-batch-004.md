# Public Fork Unique-Change Screening — Batch 004

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST identities.
GraphQL returned 89 branch refs across 24 currently resolvable repositories; the
earlier REST-only Unity-Educational-Formation repository is now NOT_FOUND, matching
its current-tree-absent marker. Three new heads were compared serially.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000150 | YiXiHu4ng/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000151 | jhuanglabAI/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000152 | danhively/biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000153 | leihe2021/Biomni_web | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000154 | airbj31/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000155 | ali-saei/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000156 | Unity-Educational-Formation/Biomni | UNKNOWN | 0 | 0 | 0 | 0 | UNAVAILABLE_CURRENT |
| repo-000157 | yilmaztnr13-collab/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000158 | moonriver2002/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000160 | yg-326/Biomni1 | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000161 | AmrR101/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000163 | zhaolm2021/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000164 | ruiafd/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000165 | stjordanis/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000705 | birdpilot/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000171 | de-grave/Biomni | User | 2 | 1 | 1 | 0 | PR_LINEAGE_ONLY |
| repo-000345 | chronicgiardia/Biomni | User | 33 | 31 | 0 | 2 | NOTEBOOK_CI_ONLY |
| repo-000166 | mirrorhealth-dev/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000167 | smengmeng30-dev/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000168 | Trismagestus/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000169 | Yijun-Cui/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000170 | jeevesh415/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000172 | wangdi2016/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000173 | jyryu3161/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000174 | Puddin1066/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: FORMAT_ONLY=1, NOTEBOOK_CI_ONLY=1, NO_UNIQUE_CHANGE=21, PR_LINEAGE_ONLY=1, UNAVAILABLE_CURRENT=1.

## Findings

- Twenty repositories expose only upstream-known heads.
- de-grave has exact open PR #306 and no separate change.
- CancerTiN and jissen706 carry pre-commit formatting heads; jissen706 also has
  exact open PR #308.
- chronicgiardia adds a Django CI workflow and an unrelated py4cytoscape Colab
  notebook; retained as non-feature notebook/CI material.
- Unity-Educational-Formation is unavailable in current GraphQL and remains a
  historical REST-only identity rather than being silently deleted.

## Evidence

- Authenticated GraphQL branch/owner response, including the NOT_FOUND object.
- Three serialized compare responses plus exact reuse of a screened format head.

## Next action

Continue the next bounded active-fork batch.
