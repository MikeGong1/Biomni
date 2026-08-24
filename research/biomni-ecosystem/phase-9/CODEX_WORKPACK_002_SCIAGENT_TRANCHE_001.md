# Codex Workpack 002：SciAgent Candidate Tranche 001

状态：`READY_FOR_LOCAL_CODEX`

## 目标

验证 `static-normalization-batch-002-manifest.jsonl` 中的 20 个 SciAgent candidate Skills，并把 17 个 provisional capability clusters 转换为正式 Feature／Implementation 或明确的 duplicate/reject 记录。

不要重跑 Phase 8，也不要把 SciAgent 整个 instruction corpus 当成一个 Implementation。

## 固定身份

SciAgent source：

`jaechang-hits/SciAgent-Skills@a0aac0f4576a550d5316baf6da3d72e53408b3a2`

Change：

`change-000081`

Biomni baseline：

`MikeGong1/Biomni@400c1f366b96a35ca253e13c9b06c5076af41d65`

## 读取顺序

1. `PHASE_9_STATE.md`
2. `methodology/research-first-source-policy.md`
3. `phase-9/feature-taxonomy-v001.md`
4. `phase-9/static-normalization-batch-002-sciagent-tranche-001.md`
5. `phase-9/static-normalization-batch-002-manifest.jsonl`
6. `external-repos/sciagent-skills.md`
7. `external-repos/sciagent-skill-audit-manifest.jsonl`
8. `database/changes.jsonl`
9. `database/lineages.jsonl`

## 执行边界

- clone exact SHA 到隔离目录；
- 所有 shell、database、plugin、ImageJ、alignment、annotation 和 visualization 路径默认不可信；
- 禁止使用患者数据、未发表序列或生产凭据；
- 只使用小型公开/合成 fixtures；
- 复制代码或模板时记录 file、symbol、commit 和修改；
- 未实际执行的测试不得标记为通过；
- 不把第三方源码放入 Biomni production path。

## Cluster A：Statistics

### `analysis.statistics.bayesian_modeling`

- 检查 PyMC 当前 API；
- 建立正常、divergent、weak-identification 三类 fixture；
- 验证 R-hat、ESS、divergence、prior/posterior predictive；
- 验证 LOO/WAIC 适用条件；
- 禁止不可信 pickle。

### `analysis.statistics.classical_models`

- 为 OLS、GLM、logit/count、SARIMAX 建立最小 fixture；
- 明确 design matrix、missingness、family/link 和 likelihood；
- 诊断不能机械转成“自动使用 robust SE”；
- AIC/BIC/LR 仅在可比模型上启用。

## Cluster B：Bioimage and Visualization

### napari

- 隔离 plugin environment；
- 禁止自动安装社区插件；
- 使用 OME-TIFF/NIfTI fixtures 检查 axis、scale、labels 和 screenshot；
- viewer 属于 review interface，不替代 quantitative validation。

### PyImageJ/Fiji

- 固定 Fiji/ImageJ 和 plugin 版本；
- 禁止首次运行隐式网络下载；
- 测试 array↔ImageJ axis round trip；
- macros/commands 必须 allowlist；
- GUI 与 headless 分开测试。

### scikit-image

- 使用 8-bit、16-bit、multichannel 和 3D fixtures；
- 显式保存 axis、dtype、physical scale；
- segmentation 需要 ground-truth metrics；
- 不把 pixel overlap 自动解释为 cell colocalization。

### Plotly 与 scientific visualization

- plotting 与 statistical inference 解耦；
- HTML 输出测试 self-contained、CDN 和 escaping；
- 不允许自动生成显著性星号；
- 期刊模板必须标记版本和检索日期。

## Cluster C：Genomics Infrastructure

### BWA-MEM2

- 固定 reference FASTA、index digest 和 read-group contract；
- 使用小型 synthetic paired FASTQ；
- 检查 primary/supplementary、unmapped、duplicate 和 alt-contig 行为；
- 输出 BAM 与 reference provenance 绑定。

### pysam + samtools

- 同一 Feature 下保留 Python API 和 CLI 两个 Implementation；
- 测试 coordinate conventions、sort/index、pileup、filter、CRAM reference；
- 所有写入使用临时目录；
- 检查 filter 是否静默丢弃记录。

### STAR

- 固定 genome/annotation release；
- 构建微型 splice fixture；
- 验证 junction、multimapping、chimeric 和 two-pass 行为；
- 不把 generic defaults 作为所有 RNA-seq assay 的通用配置。

## Cluster D：Microbiology and Systems Biology

### Bakta + Prokka

- 归入同一 `prokaryotic_annotation` Feature；
- Biomni Prokka 为 baseline Implementation；
- Bakta 为 candidate alternative Implementation；
- 对同一小型 bacterial assembly 比较 features、product names、format 和 provenance；
- 固定数据库 release。

### Roary

- 仅使用小型公开/合成 GFF3；
- 比较 annotation inconsistency、fragmentation、paralog 和 identity thresholds；
- 不把 presence/absence association 表述为因果。

### Arboreto

- 使用有已知调控结构的 synthetic expression fixture；
- 固定 seed、TF list 和 preprocessing；
- 比较 GRNBoost2/GENIE3；
- 输出必须明确为 importance/co-expression，而不是 causal regulation。

## Cluster E：Sequence and Database Infrastructure

### Biopython

把两个 Skill 拆为最小单元：

- sequence/file I/O；
- local sequence operations；
- Entrez；
- BLAST；
- alignment；
- phylogeny；
- PDB I/O。

逐项映射 Biomni 现有 tools。高度重复的第二个 Skill 不得生成重复 Implementation。

### bioservices

- 不为每个已有数据库创建重复 Feature；
- 只评估 unified client lifecycle、cross-database mapping、error/timeout/rate-limit/provenance；
- 建立离线 mocked compatibility tests；
- 禁止把 legacy PICR 或未验证 method 当成当前合同。

### cBioPortal 和 ClinVar

- 与 Biomni `query_cbioportal`、`query_clinvar` 做实现级比较；
- 默认归入现有 Feature；
- 只有发现字段、schema、privacy 或 evidence-contract 实质增量时才创建新 Implementation；
- 禁止自动临床结论。

## 必须输出

- `phase-9/validation-batch-002.md`
- `phase-9/validation-batch-002-manifest.jsonl`
- characterization tests 和 fixtures
- provenance ledger
- 更新 `features.jsonl`
- 更新 `implementations.jsonl`
- 更新 `PHASE_9_STATE.md`
- 更新 `PHASE_9_COVERAGE.md`

## 完成门

- 20 Skills 全部得到最终 disposition；
- 17 cluster 全部完成 semantic dedup；
- 2 个 Biopython Skills 不重复计数；
- pysam 和 samtools 作为同一 Feature 的不同 Implementation；
- Bakta 和 Prokka 作为同一 Feature 的不同 Implementation；
- cBioPortal 和 ClinVar 与 baseline 对齐；
- 运行结果、失败和未运行项均如实记录；
- JSONL cross-reference 和 ID 唯一性通过。
