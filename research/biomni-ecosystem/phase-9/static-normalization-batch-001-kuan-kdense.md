# Phase 9 静态归一化 Batch 001：K-Dense／Kuan Skills、BIDS 与 DataLad

状态：**COMPLETE_STATIC_ONLY**

研究分支：`research/biomni-ecosystem-audit`

冻结 Biomni 基线：`400c1f366b96a35ca253e13c9b06c5076af41d65`

## 1. 范围

本批处理以下已存在的 Change：

- `change-000088`：Kuan PR #75 的 12-Skill bundle；
- `change-000089`：Kuan fork-only API 修复历史，用于 lineage 和当前实现选择；
- `change-000090`：BIDS PR #125 及当前 K-Dense successor；
- `change-000091`：DataLad PR #227。

本批没有重新执行 Batch 001–046，没有运行第三方代码、installer、notebook、模型、容器或服务，也没有创建 canonical Feature／Implementation ID。

本批把 14 个仓库级 Skill／change surface 拆成 **21 个 provisional capability units**。这些记录是 Phase 9 的静态功能归一化输入，不是运行验证或最终集成结论。

## 2. 证据基础

主要来源：

- K-Dense family 静态审计和 lineage 结论；
- 12-row Kuan Skill manifest；
- Biomni frozen baseline 的 224 个 exposed tool schema；
- Biomni `database`、`glycoengineering`、`biophysics` 和 `genomics` tool descriptions；
- source-first override 和 Phase 9 研究策略。

当前 K-Dense source successor：`390f5146bf3c1877cf15636a3dd7b775e4f0f185`

历史 Kuan PR #75 head：`7f94783fab51a468f9a4b08472e8c49111b21fcd`

BIDS PR #125 head：`75f688228a6c1d7387db81347117a3fd27b53de4`

DataLad PR #227 head：`997202b7d481c40ca5e22e197077846fc9adc2048e`

## 3. Biomni gap 结果

21 个 provisional capability units 的静态比较结果：

- Biomni 基线已有等价能力：**6**
- Biomni 只有部分重叠：**4**
- Biomni 有相关数据库能力，但不是等价实现：**1**
- Biomni 明确缺少对应能力：**10**

研究 disposition：

- `DUPLICATE_OR_SUPERSEDED`：**6**
- `SOURCE_FIRST_WITH_REMEDIATION`：**11**
- `REFERENCE_ONLY_BLOCKED`：**4**

## 4. Provisional capability matrix

| # | Provisional Feature | Source Skill | Biomni 状态 | 研究 disposition | 能力 |
|---:|---|---|---|---|---|
| 1 | `database.bindingdb.affinity_query` | `bindingdb-database` | `RELATED_OVERLAP_NOT_EQUIVALENT` | `SOURCE_FIRST_WITH_REMEDIATION` | 查询 BindingDB 的蛋白—配体结合数据，并按靶点、配体或亲和力条件检索。 |
| 2 | `analysis.bindingdb.sar_selectivity` | `bindingdb-database` | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 对 BindingDB 批量数据执行 SAR、选择性和多靶点活性比较。 |
| 3 | `database.cbioportal.cancer_genomics_query` | `cbioportal-database` | `BASELINE_EQUIVALENT_PRESENT` | `DUPLICATE_OR_SUPERSEDED` | 查询 cBioPortal 的癌症研究、突变、拷贝数和临床数据。 |
| 4 | `analysis.cbioportal.clinical_survival_workflow` | `cbioportal-database` | `PARTIAL_OVERLAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 把 cBioPortal 查询结果组织成队列比较、临床变量和生存分析工作流。 |
| 5 | `analysis.depmap.cancer_dependency` | `depmap` | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 执行 Chronos 基因依赖、选择性依赖、共依赖和生物标志物分析。 |
| 6 | `analysis.glyco.motif_detection` | `glycoengineering` | `BASELINE_EQUIVALENT_PRESENT` | `DUPLICATE_OR_SUPERSEDED` | 扫描 N-糖基化 sequon，并给出启发式 O-糖基化热点。 |
| 7 | `design.glyco.sequence_engineering` | `glycoengineering` | `PARTIAL_OVERLAP` | `REFERENCE_ONLY_BLOCKED` | 提出增加、移除或调整糖基化位点的蛋白序列编辑方案。 |
| 8 | `database.gnomad.population_frequency` | `gnomad-database` | `BASELINE_EQUIVALENT_PRESENT` | `DUPLICATE_OR_SUPERSEDED` | 查询 gnomAD 的基因和变异人群频率信息。 |
| 9 | `interpretation.gnomad.constraint_sv_acmg` | `gnomad-database` | `CLEAR_GAP` | `REFERENCE_ONLY_BLOCKED` | 把 gnomAD constraint、LoF、SV 和频率结果用于变异解释辅助。 |
| 10 | `database.gtex.expression_qtl` | `gtex-database` | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 查询 GTEx 的组织表达、eQTL、sQTL 和 eGene 信息。 |
| 11 | `database.interpro.domain_annotation` | `interpro-database` | `BASELINE_EQUIVALENT_PRESENT` | `DUPLICATE_OR_SUPERSEDED` | 查询蛋白结构域、家族、位点、GO 和 domain architecture。 |
| 12 | `database.jaspar.matrix_query` | `jaspar-database` | `BASELINE_EQUIVALENT_PRESENT` | `DUPLICATE_OR_SUPERSEDED` | 查询 JASPAR 转录因子矩阵与元数据。 |
| 13 | `analysis.jaspar.motif_scan_variant_impact` | `jaspar-database` | `PARTIAL_OVERLAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 将 JASPAR PFM/PWM 用于双链序列扫描和变异影响评分。 |
| 14 | `simulation.molecular_dynamics.protocol` | `molecular-dynamics` | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 用 OpenMM 建立、最小化、平衡并运行分子动力学模拟。 |
| 15 | `analysis.molecular_dynamics.trajectory` | `molecular-dynamics` | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 用 MDAnalysis 计算 RMSD、RMSF、接触和轨迹摘要。 |
| 16 | `database.monarch.phenotype_association` | `monarch-database` | `BASELINE_EQUIVALENT_PRESENT` | `DUPLICATE_OR_SUPERSEDED` | 查询 phenotype—gene—disease 关联和 HPO 实体。 |
| 17 | `analysis.monarch.semantic_similarity_cross_species` | `monarch-database` | `PARTIAL_OVERLAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 执行表型语义相似度和跨物种 phenotype 映射。 |
| 18 | `pipeline.phylogenetics.alignment_tree` | `phylogenetics` | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 组织 MAFFT/TrimAl、IQ-TREE/FastTree 和 ETE3 的系统发育分析流程。 |
| 19 | `analysis.scrna.rna_velocity` | `scvelo` | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 执行 scVelo 的预处理、随机/动力学 RNA velocity、latent time 和 driver 分析。 |
| 20 | `data_standard.bids.organization_validation` | `bids` | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` | 组织 BIDS 命名、PyBIDS 查询、验证、DICOM 转换、metadata/events/participants、derivatives 和 BIDS Apps。 |
| 21 | `data_provenance.datalad.versioned_research_data` | `datalad` | `CLEAR_GAP` | `REFERENCE_ONLY_BLOCKED` | 用 DataLad/git-annex 管理科研数据、内容获取、rerun provenance、containers、siblings 和发布。 |

## 5. 主要结论

### 5.1 可以直接归入 Biomni 现有能力族的项目

以下能力在 Biomni frozen baseline 中已有 exposed tool：

- cBioPortal query；
- N/O glycosylation motif 分析；
- gnomAD 基因/变异查询；
- InterPro domain query；
- JASPAR matrix query；
- Monarch phenotype association query。

这些外部 Skills 不应被创建为新的 Feature。后续 Codex 只需检查它们是否带来更好的 schema、输入验证、字段覆盖或结果解释；没有实质增量时仅保留 lineage 和文档证据。

### 5.2 值得新增 Feature 的明确 gap

本批发现的高价值 gap 包括：

- DepMap cancer dependency analysis；
- GTEx expression/eQTL/sQTL query；
- Molecular dynamics protocol；
- Molecular dynamics trajectory analysis；
- Phylogenetics pipeline；
- scVelo RNA velocity；
- BIDS organization/validation；
- DataLad research-data provenance；
- BindingDB SAR/selectivity；
- gnomAD constraint/SV evidence extraction。

这些 gap 仍需要 Codex 在 exact source SHA 上执行源码冻结、characterization tests、安全检查和科学验证，之后才能分配 canonical Feature／Implementation ID。

### 5.3 必须拆开的混合 Skills

以下 Skill 不能作为单一 Feature：

- BindingDB：query 与 SAR/selectivity analysis 分开；
- cBioPortal：database query 与 clinical/survival workflow 分开；
- Glycoengineering：motif detection 与 sequence engineering 分开；
- gnomAD：population query 与 clinical interpretation 分开；
- JASPAR：matrix query 与 motif scan/variant impact 分开；
- Molecular dynamics：simulation protocol 与 trajectory analysis 分开；
- Monarch：association query 与 semantic similarity/cross-species 分开。

### 5.4 不应因为 license 被排除，但仍不能直接运行的项目

- Glycoengineering sequence design：科学约束不足；
- gnomAD clinical interpretation：历史 LoF/ACMG 逻辑错误；
- DataLad：存在 rerun、container、drop、publish 和 credential 风险。

这些项目保留为 `REFERENCE_ONLY_BLOCKED`，阻断原因是科学、安全或数据治理，而不是 license。

## 6. 后续 Codex 验收门

每个 provisional capability 在进入 canonical database 前必须满足：

1. exact repository、commit、branch/PR 和 file/symbol provenance；
2. 与 Biomni baseline 的代码级比较；
3. 最小 characterization test；
4. source-to-sink 安全审查；
5. 隐私和数据外传审查；
6. 科学方法和单位/schema 合同；
7. 依赖、模型、数据、API 版本固定；
8. Feature semantic dedup；
9. Implementation relationship 和状态；
10. JSONL cross-reference 校验。

机器可读记录：

`static-normalization-batch-001-manifest.jsonl`

Codex 工作包：

`CODEX_WORKPACK_001_KDENSE_KUAN.md`
