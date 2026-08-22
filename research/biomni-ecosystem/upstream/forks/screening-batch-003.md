# Public Fork Unique-Change Screening — Batch 003

Parent verification: `VERIFIED`. Scope: the 25 most recently pushed unscreened REST forks.
One serialized GraphQL query returned all 123 branch refs with no ref pagination.
Six new unique heads were compared serially; one pre-commit head was reused from
batch 002 by exact SHA and was not requested again.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Other heads | Screening status |
|---|---|---|---:|---:|---:|---:|---|
| repo-000126 | hapi-developer/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000127 | CancerTiN/Biomni | User | 33 | 32 | 0 | 1 | FORMAT_ONLY |
| repo-000128 | alexandreumatize/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000130 | arrowifjn/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000131 | zhangqif/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000132 | super-818/Biomni_learn | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000134 | vjbaskar/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000135 | xtalgalaxy/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000142 | cerebral-work/biomni | Organization | 1 | 0 | 0 | 1 | CONFIG_ONLY |
| repo-000440 | leizhou69/Biomni_Rpts_Ds | User | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_CANDIDATE |
| repo-000145 | jissen706/Biomni | User | 34 | 32 | 1 | 1 | PR_LINEAGE_PLUS_FORMAT_ONLY |
| repo-000136 | sunshinezhihuo/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000137 | szz00712/Biomni_s | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000138 | 1667857557/Biomni_feng | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000139 | zhansh-2025/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000140 | qym7/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000141 | yepingzhao/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000143 | dragonlhy/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000144 | dming1024/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000146 | awmuhtaseb/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000177 | dabulseco/Biomni | User | 1 | 0 | 0 | 1 | SUBSTANTIVE_UNIQUE |
| repo-000162 | rotojp/Biomni | User | 34 | 32 | 0 | 2 | FORMAT_ONLY |
| repo-000147 | hzhou98/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000148 | JimmyXtesla/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000149 | vitumsowoya/Biomni | User | 1 | 1 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: CONFIG_ONLY=1, DIVERGED_SUBSTANTIVE_CANDIDATE=1, FORMAT_ONLY=2, NO_UNIQUE_CHANGE=19, PR_LINEAGE_PLUS_FORMAT_ONLY=1, SUBSTANTIVE_UNIQUE=1.

## Substantive findings

- `leizhou69/Biomni_Rpts_Ds`: eight ahead / nine behind; model-route updates,
  output-directory support, local data-lake behavior, tool-observation message fix,
  and an explicit migration/archive path. Retained as diverged candidate.
- `dabulseco/Biomni`: three commits adding Ollama-first local/cloud routing, a
  Streamlit UI, shared UI/REPL code, and numerous generated Chikungunya/nanobody
  artifacts. Code, data provenance, artifact licenses, and UI exposure need review.

## Non-substantive and lineage findings

- Nineteen repositories expose only upstream-known heads.
- CancerTiN reuses exact pre-commit head from batch 002; rotojp has ImgBot plus
  another pre-commit-only head.
- cerebral-work changes only `.gitignore` custody-store configuration.
- jissen706 has exact open PR #308 plus a pre-commit-only head; no duplicate change
  record is created.

## Evidence

- Authenticated GraphQL branch/owner inventory.
- Six serialized compare responses and one exact-SHA reuse from batch 002.
- Local SHA comparison against all upstream branches and canonical PR heads.

## Next action

Continue active-fork screening; deep-audit the two retained changes later.
