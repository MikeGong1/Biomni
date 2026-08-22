# Public Fork Unique-Change Screening — Batch 005

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One authenticated GraphQL query returned all 189 branch refs without pagination.
Eight unique non-PR heads were compared serially.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000175 | richWmc/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000176 | caramelcyy/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000178 | hwl26/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000179 | philloidin/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000365 | Science-Will-Win/Biomni | Organization | 1 | 0 | 0 | 1 | JHK_DERIVED_SUBSTANTIVE |
| repo-000180 | lokinell/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000181 | Norton-xia-hub/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000182 | mrsirquanzo/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000216 | zhuyitan/Biomni | User | 2 | 0 | 0 | 2 | SUBSTANTIVE_UNIQUE |
| repo-000183 | Alirezahayatimedtech/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000184 | termasz/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000185 | hhg36355-hue/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000186 | kewserseid/Biomni | User | 2 | 1 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000187 | zhikangliu068-lab/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000188 | look4pritam/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000189 | ourkofe/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000190 | sjiang-lilly/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000191 | Nigmat-future/Biomni | User | 34 | 32 | 1 | 1 | PR_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000192 | starboy-3/Biomni | User | 34 | 32 | 1 | 1 | PR_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000193 | SnehanshnC/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000194 | jwert-aws/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000195 | matt783/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000412 | vetcoders/Biomni | Organization | 33 | 31 | 0 | 2 | SUBSTANTIVE_UNIQUE |
| repo-000196 | maxwellfet928/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000197 | molmin-2/Biomni | Organization | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: FORMAT_ONLY=2, JHK_DERIVED_SUBSTANTIVE=1, NO_UNIQUE_CHANGE=17, PR_LINEAGE_PLUS_FORMAT_ONLY=2, SUBSTANTIVE_UNIQUE=3.

## Substantive findings

- Science-Will-Win contains the complete 25-commit JHK/kwskws lineage and adds
  five commits for RAGAS, ExpeL experiment mode, graph memory, and answer fixes.
- zhuyitan main strictly contains its iterative_coding branch: nine unique commits
  adding TCGA retrieval/assembly scripts and a converter/code-agent workflow.
- kewserseid adds a Rejuve assistant layer with API, RAG, hypothesis generation,
  annotation/graph tooling, Redis/Qdrant/Mongo storage, auth, and frontend.
- vetcoders adds a portal with authentication, database, agent API, sharing,
  Docker deployment, tests, and error/locking fixes.

## Lineage and non-substantive findings

- Nigmat-future and starboy-3 expose exact open PR heads plus one shared pre-commit
  head; SnehanshnC shares the same format head without a PR head.
- look4pritam is pre-commit-only; vetcoders also has a stale divergent pre-commit
  branch that is not a separate feature.
- Seventeen repositories expose only upstream-known heads.

## Risks

- TCGA/GDC scripts include a bundled gdc-client path and extensive generated test
  material; binary provenance, controlled-data terms, and code execution require review.
- Rejuve and vetcoders add network services, authentication, persistent stores,
  web search, uploads/sharing, and deployment surfaces requiring threat models.

## Next action

Update JHK lineage, retain four changes, and continue bounded screening.
