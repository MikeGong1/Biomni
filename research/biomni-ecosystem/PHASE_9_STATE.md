# Phase 9 Research State

状态：**AUTHORITATIVE ACTIVE CHECKPOINT**

生效日期：`2026-08-24`

Phase 9 起始提交：`760233424c9039c60f5acb561d54e6fff4e26489`

研究分支：`research/biomni-ecosystem-audit`

## 当前阶段

`Phase 9 — source-first Feature / Implementation normalization`

Phase 8 的外部生态发现和静态仓库审计已经关闭：

- Batch 001–046：完成；
- stable external families：2,069／2,069；
- queued repository records：2,161／2,161；
- `DEEP_AUDIT_CANDIDATE`：598；
- Change：截至 `change-000711`；
- Lineage：截至 `lineage-000223`；
- Evidence：截至 `evidence-000358`；
- 第三方代码运行：0；
- canonical Feature：0；
- canonical Implementation：0。

## 当前解释规则

`RESEARCH_FIRST_OVERRIDE.md` 和
`methodology/research-first-source-policy.md` 是 Phase 9 的控制规则。

- license 不再作为 Feature／Implementation 发现的淘汰条件；
- 原始源码应优先用于理解和研究工作区内的复现／改造；
- 必须保存 repository、commit、PR/branch、file、symbol 和修改 provenance；
- 公开发布和论文配套源码进入单独的 publication review；
- 科学、安全、隐私、临床、模型信任和供应链要求不放宽。

## 控制文件冲突处理

旧的 `STATE.md`、`MASTER_INDEX.md` 和 `COVERAGE.md` 中保留了 Phase 8 执行过程的历史段落，其中部分段落仍写着 Batch 009 `NOT_STARTED` 或旧的队列累计数。

这些历史段落不再作为 Phase 9 当前状态。读取优先级为：

1. `PHASE_9_STATE.md`
2. `PHASE_9_MASTER_INDEX.md`
3. `PHASE_9_COVERAGE.md`
4. `RESEARCH_FIRST_OVERRIDE.md`
5. `methodology/research-first-source-policy.md`
6. 旧控制文件，仅作为历史记录和详细证据索引

后续 Codex 可在本地使用脚本重写旧控制文件并验证所有累计数；在此之前不得从旧段落推断当前队列未完成。

## 当前调研工作

### 已完成

- 建立 source-first 研究规则；
- 建立 13 个高价值 reopening group；
- 建立 Feature taxonomy v0.1；
- 完成 Phase 9 静态归一化 Batch 001：
  - K-Dense／Kuan 12 Skills；
  - BIDS；
  - DataLad；
  - 拆分为 21 个 provisional capability units；
  - 完成 Biomni frozen baseline 静态 gap 分类；
  - 生成 Codex Workpack 001。

### 正在进行

- SciAgent 203 Skills 的 Feature cluster 设计；
- 商业能力发现补全；
- 598 个 candidate family 的语义聚类。

## 下一步

### GPT Pro

1. 按 taxonomy 对 SciAgent 203 Skills 做静态聚类；
2. 优先整理原有 125 个 candidate leads；
3. 继续官方 commercial discovery；
4. 为每个 cluster 生成 provisional capability manifest 和 Codex 验证清单；
5. 审阅 Codex 输出并维护综合目录。

### Codex

1. 执行 `phase-9/CODEX_WORKPACK_001_KDENSE_KUAN.md`；
2. clone/fetch exact source SHA；
3. 进行代码级 diff、AST、patch 和 lineage 比较；
4. 运行 characterization tests；
5. 完成 source-to-sink、安全、隐私和科学验证；
6. 填充 `features.jsonl` 和 `implementations.jsonl`；
7. 生成 attribution ledger；
8. 更新本文件和 Phase 9 coverage。

## 禁止事项

- 不重跑 Batch 001–046；
- 不把静态候选描述为 runtime verified；
- 不把 citation 等同于公开分发授权；
- 不因 license 不明确删除有价值 Feature；
- 不因科研用途忽略安全、隐私或临床风险；
- 不把第三方研究源码直接混入 Biomni 生产目录。
