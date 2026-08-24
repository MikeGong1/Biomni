# Phase 9 Master Index

状态：**ACTIVE AUTHORITATIVE OVERLAY**

## 控制文件

| 文件 | 状态 | 用途 |
|---|---|---|
| `PHASE_9_STATE.md` | ACTIVE | 当前权威恢复点 |
| `PHASE_9_COVERAGE.md` | ACTIVE | Phase 9 覆盖率 |
| `PHASE_9_MASTER_INDEX.md` | ACTIVE | 当前索引 |
| `RESEARCH_FIRST_OVERRIDE.md` | ACTIVE | source-first 决策覆盖 |
| `methodology/research-first-source-policy.md` | ACTIVE | Feature/Implementation 研究方法 |
| `CODEX_RESEARCH_FIRST_PROMPT.md` | ACTIVE | 全局 Codex continuation |
| `STATE.md` | HISTORICAL_DETAIL | Phase 8 历史日志；部分旧状态段落已被本文件覆盖 |
| `MASTER_INDEX.md` | HISTORICAL_DETAIL | 旧全量索引；顶部旧累计数不再是当前状态 |
| `COVERAGE.md` | HISTORICAL_DETAIL | Phase 8 过程覆盖；以 `PHASE_9_COVERAGE.md` 为当前累计数 |

## Phase 8 关闭证据

| 文件 | 状态 | 内容 |
|---|---|---|
| `external-repos/FINAL_COMPLETION_SUMMARY.md` | COMPLETE | 2,069 family／2,161 record／Batch 001–046 |
| `external-repos/deep-audit-batch-001.md` 至 `deep-audit-batch-046.md` | COMPLETE | 仓库级静态审计 |
| `database/repositories.jsonl` | ACTIVE | repository identity 和 queue state |
| `database/changes.jsonl` | ACTIVE | Change 至 `change-000711` |
| `database/lineages.jsonl` | ACTIVE | Lineage 至 `lineage-000223` |
| `database/evidence.jsonl` | ACTIVE | Evidence 至 `evidence-000358` |
| `database/features.jsonl` | EMPTY | Phase 9 待填充 |
| `database/implementations.jsonl` | EMPTY | Phase 9 待填充 |

## Phase 9 方法和队列

| 文件 | 状态 | 内容 |
|---|---|---|
| `phase-9/feature-taxonomy-v001.md` | ACTIVE_PROVISIONAL | Feature 分类和 identity 规则 |
| `external-repos/research-first-reopen-manifest.jsonl` | ACTIVE | 第一批 13 个 reopening group |

## Static normalization Batch 001

| 文件 | 状态 | 内容 |
|---|---|---|
| `phase-9/static-normalization-batch-001-kuan-kdense.md` | COMPLETE_STATIC_ONLY | K-Dense/Kuan 12 Skills、BIDS、DataLad；21 capability units |
| `phase-9/static-normalization-batch-001-manifest.jsonl` | COMPLETE_STATIC_ONLY | 21-row machine-readable manifest |
| `phase-9/CODEX_WORKPACK_001_KDENSE_KUAN.md` | READY | 代码级比较、验证和 canonical normalization |

## Static normalization Batch 002

| 文件 | 状态 | 内容 |
|---|---|---|
| `phase-9/static-normalization-batch-002-sciagent-tranche-001.md` | COMPLETE_STATIC_ONLY | SciAgent 首批 20 个 candidate Skills；17 capability clusters |
| `phase-9/static-normalization-batch-002-manifest.jsonl` | COMPLETE_STATIC_ONLY | 20-row Skill→cluster mapping |
| `phase-9/CODEX_WORKPACK_002_SCIAGENT_TRANCHE_001.md` | READY | statistics、bioimage、genomics、microbiology、database cluster 验证 |

## 当前静态覆盖

- statically normalized candidate families：2／598；
- statically normalized SciAgent candidate Skills：20／125；
- statically normalized provisional capability clusters/units：38；
- canonical Features：0；
- canonical Implementations：0；
- third-party runtime executions：0。

## 下一批静态研究

1. SciAgent 剩余 105 个 candidate leads；
2. SciAgent 78 个 no-near-term entries 的 reference/archive 分类；
3. ChatSpatial／DeepSpot-M；
4. ezST；
5. Aquila-next；
6. gnomAD_DB；
7. 其余 598 candidates 的 cluster 化；
8. commercial vs OSS gap。
