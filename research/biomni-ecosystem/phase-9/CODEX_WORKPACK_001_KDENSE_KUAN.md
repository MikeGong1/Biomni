# Codex Workpack 001：K-Dense／Kuan、BIDS 与 DataLad

状态：`READY_FOR_LOCAL_CODEX`

## 目标

把 `static-normalization-batch-001-manifest.jsonl` 中的 21 个 provisional capability units 转换为经过代码级比较和最小运行验证的 Feature／Implementation cluster。

不要重跑 Batch 001–046。

## 固定身份

Biomni baseline：

`MikeGong1/Biomni@400c1f366b96a35ca253e13c9b06c5076af41d65`

K-Dense current source：

`K-Dense-AI/scientific-agent-skills@390f5146bf3c1877cf15636a3dd7b775e4f0f185`

Kuan historical PR bundle：

`kuanlinhuang/claude-scientific-skills@7f94783fab51a468f9a4b08472e8c49111b21fcd`

BIDS historical PR：

`yarikoptic/claude-scientific-skills@75f688228a6c1d7387db81347117a3fd27b53de4`

DataLad PR：

`K-Dense-AI/scientific-agent-skills@997202b7d481c40ca5e22e197077846fc9adc2048e`

## 读取顺序

1. `research/biomni-ecosystem/PHASE_9_STATE.md`
2. `research/biomni-ecosystem/methodology/research-first-source-policy.md`
3. `research/biomni-ecosystem/phase-9/static-normalization-batch-001-kuan-kdense.md`
4. `research/biomni-ecosystem/phase-9/static-normalization-batch-001-manifest.jsonl`
5. `research/biomni-ecosystem/external-repos/deep-audit-batch-003.md`
6. `research/biomni-ecosystem/external-repos/deep-audit-batch-003-kuan-skill-manifest.jsonl`
7. `research/biomni-ecosystem/database/changes.jsonl`
8. `research/biomni-ecosystem/database/lineages.jsonl`

## 执行原则

- 在隔离目录 clone 所有 source；
- checkout exact SHA；
- 不把第三方源码直接放进 `biomni/` 生产目录；
- 复制源码时保留原文件、commit、symbol、修改记录和 attribution；
- 先写 characterization tests，再改代码；
- license 只作为 provenance 字段，不作为 Feature 淘汰条件；
- 科学、安全、隐私、临床、模型和供应链阻断项不得降级；
- 不得宣称未实际执行的测试。

## Cluster 划分

### Cluster A：已有 Biomni 等价能力

- `database.cbioportal.cancer_genomics_query`
- `analysis.glyco.motif_detection`
- `database.gnomad.population_frequency`
- `database.interpro.domain_annotation`
- `database.jaspar.matrix_query`
- `database.monarch.phenotype_association`

任务：

1. 比较外部 source 与 Biomni 对应实现；
2. 检查字段覆盖、schema、分页、timeout、输入验证和 provenance；
3. 没有实质行为增量时标记 `DUPLICATE_OR_SUPERSEDED`；
4. 有实质增量时创建同一 Feature 下的新 Implementation。

### Cluster B：数据库和证据 gap

- `database.bindingdb.affinity_query`
- `analysis.bindingdb.sar_selectivity`
- `analysis.depmap.cancer_dependency`
- `database.gtex.expression_qtl`
- `interpretation.gnomad.constraint_sv_acmg`
- `analysis.cbioportal.clinical_survival_workflow`
- `analysis.monarch.semantic_similarity_cross_species`

任务：

1. 固定 API/release/schema；
2. 创建 typed response；
3. 增加 timeout、重试、速率限制和查询隐私提示；
4. 对统计和解释逻辑建立黄金 fixture；
5. gnomAD clinical interpretation 只允许证据抽取，不允许自动临床结论。

### Cluster C：计算与组学 workflow gap

- `simulation.molecular_dynamics.protocol`
- `analysis.molecular_dynamics.trajectory`
- `pipeline.phylogenetics.alignment_tree`
- `analysis.scrna.rna_velocity`
- `analysis.jaspar.motif_scan_variant_impact`
- `design.glyco.sequence_engineering`

任务：

1. 固定工具版本；
2. 生成最小离线 fixture；
3. 检查单位、坐标、方向、随机种子和输出覆盖；
4. 与官方 reference workflow 对比；
5. 任何设计或解释输出必须标记为候选，不得自动升级为生物学结论。

### Cluster D：科研数据标准与 provenance

- `data_standard.bids.organization_validation`
- `data_provenance.datalad.versioned_research_data`

任务：

1. BIDS 以官方 schema 为唯一事实源；
2. DICOM 进入任何 BIDS workflow 前设置 PHI gate；
3. DataLad 默认禁用 `rerun`、container execution、`drop`、publish；
4. 只在临时 fixture repository 中测试；
5. 所有 destructive／publication 行为需要逐目标确认。

## 必须输出

- `research/biomni-ecosystem/phase-9/validation-batch-001.md`
- `research/biomni-ecosystem/phase-9/validation-batch-001-manifest.jsonl`
- 更新后的 `database/features.jsonl`
- 更新后的 `database/implementations.jsonl`
- source attribution/provenance ledger
- characterization tests
- 每个 Feature 的 Biomni gap 结论
- 更新 `PHASE_9_STATE.md` 和 `PHASE_9_COVERAGE.md`

## Canonical ID 门

只有满足以下条件才分配正式 ID：

- capability statement 稳定；
- source identity 和 files/symbols 完整；
- 当前 cluster 已做 semantic dedup；
- Biomni overlap 已确认；
- 至少完成静态 contract test；可运行实现还需最小 characterization test；
- security/science/privacy/runtime 状态明确；
- JSONL round-trip 和 cross-reference 通过。

## 完成定义

本 workpack 完成时：

- 21 个 provisional capability 全部有最终 disposition；
- 重复能力归入现有 Feature；
- gap 能力创建 Feature；
- 每个有效 source 创建或拒绝 Implementation；
- 所有非 license 阻断项仍清晰可见；
- 没有第三方源码污染 Biomni 生产目录。
