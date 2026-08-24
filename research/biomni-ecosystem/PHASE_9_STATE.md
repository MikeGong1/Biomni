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

## Phase 9 当前覆盖

- statically normalized candidate families：2／598；
- statically normalized provisional capability clusters/units：38；
- canonical Features：0；
- canonical Implementations：0；
- characterization-tested capabilities：0；
- third-party runtime executions：0。

## 已完成的 Phase 9 调研

### 控制和方法

- 建立 source-first 研究规则；
- 建立 13 个高价值 reopening group；
- 建立 Feature taxonomy v0.1；
- 建立独立 Phase 9 State、Coverage 和 Master Index；
- 更新 README，使 Phase 9 文件优先于旧 Phase 8 过程段落。

### Static normalization Batch 001

范围：K-Dense／Kuan 12 Skills、BIDS、DataLad。

结果：

- 14 个 source surfaces；
- 21 个 provisional capability units；
- 10 个明确 Biomni gap；
- 4 个 partial overlap；
- 1 个 related but non-equivalent overlap；
- 6 个 baseline-equivalent；
- 已生成 `CODEX_WORKPACK_001_KDENSE_KUAN.md`。

### Static normalization Batch 002

范围：SciAgent manifest 中最早的 20 个 `candidate=true` Skills。

结果：

- 20 个 Skills；
- 17 个 capability clusters；
- 10 个明确 Biomni gap；
- 4 个 partial overlap；
- 3 个 baseline-equivalent；
- 16 个 source-first/remediation Skill；
- 4 个 duplicate/superseded Skill；
- 已生成 `CODEX_WORKPACK_002_SCIAGENT_TRANCHE_001.md`。

重要归并：

- pysam 与 samtools：同一 HTS processing Feature 的两个 Implementation；
- Bakta 与 Prokka：同一 prokaryotic annotation Feature 的两个 Implementation；
- 两个 Biopython Skills：高度重叠，需拆分后去重；
- cBioPortal 和 ClinVar：与 Biomni baseline 对齐，不创建重复 Feature。

## 正在进行

- SciAgent 剩余 105 个 candidate leads 的静态归一化；
- SciAgent 78 个 no-near-term entries 的 reference/archive 分类；
- 商业能力发现补全；
- 598 个 candidate family 的语义聚类。

## 下一步

### GPT Pro

1. 从 SciAgent manifest 下一个未处理的 `candidate=true` Skill 继续；
2. 按 15–25 Skill 一批生成 Skill→cluster manifest；
3. 继续官方 commercial discovery；
4. 为 ChatSpatial、ezST、Aquila-next 和 gnomAD_DB 建立静态 capability decomposition；
5. 审阅 Codex 输出并维护综合目录。

### Codex

1. 执行 `phase-9/CODEX_WORKPACK_001_KDENSE_KUAN.md`；
2. 执行 `phase-9/CODEX_WORKPACK_002_SCIAGENT_TRANCHE_001.md`；
3. clone/fetch exact source SHA；
4. 进行代码级 diff、AST、patch 和 lineage 比较；
5. 运行 characterization tests；
6. 完成 source-to-sink、安全、隐私和科学验证；
7. 填充 `features.jsonl` 和 `implementations.jsonl`；
8. 生成 attribution ledger；
9. 更新本文件和 Phase 9 coverage。

## 禁止事项

- 不重跑 Batch 001–046；
- 不把静态候选描述为 runtime verified；
- 不把 citation 等同于公开分发授权；
- 不因 license 不明确删除有价值 Feature；
- 不因科研用途忽略安全、隐私或临床风险；
- 不把第三方研究源码直接混入 Biomni 生产目录。
