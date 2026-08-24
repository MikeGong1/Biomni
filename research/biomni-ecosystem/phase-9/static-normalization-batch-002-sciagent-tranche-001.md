# Phase 9 静态归一化 Batch 002：SciAgent 候选 Tranche 001

状态：**COMPLETE_STATIC_ONLY**

来源：`jaechang-hits/SciAgent-Skills`

冻结 source head：`a0aac0f4576a550d5316baf6da3d72e53408b3a2`

关联 Change：`change-000081`

Biomni baseline：`400c1f366b96a35ca253e13c9b06c5076af41d65`

## 1. 范围

本批处理 SciAgent per-Skill audit manifest 中按 `audit_order` 最早出现的 20 个 `candidate=true` Skills：

1. `pymc-bayesian-modeling`
2. `statsmodels-statistical-modeling`
3. `napari-image-viewer`
4. `pyimagej-fiji-bridge`
5. `scikit-image-processing`
6. `plotly-interactive-plots`
7. `scientific-visualization`
8. `bwa-mem2-dna-aligner`
9. `pysam-genomic-files`
10. `samtools-bam-processing`
11. `star-rna-seq-aligner`
12. `bakta-genome-annotation`
13. `prokka-genome-annotation`
14. `roary-pangenome`
15. `arboreto-grn-inference`
16. `biopython-molecular-biology`
17. `biopython-sequence-analysis`
18. `bioservices-multi-database`
19. `cbioportal-database`
20. `clinvar-database`

本批没有运行代码、工具、数据库查询、安装程序或数据。它只把 20 个 Skill 文件静态归并成 **17 个 provisional capability clusters**，并与 frozen Biomni baseline 做能力级比较。

## 2. Cluster 结果

| Cluster | Skills／Implementations | Biomni gap | Phase 9 disposition |
|---|---|---|---|
| `analysis.statistics.bayesian_modeling` | PyMC | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `analysis.statistics.classical_models` | statsmodels | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `visualization.bioimage.interactive_viewer` | napari | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `integration.bioimage.imagej_bridge` | PyImageJ/Fiji | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `analysis.bioimage.general_processing` | scikit-image | `PARTIAL_OVERLAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `visualization.interactive.plotly` | Plotly | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `guide.visualization.scientific_reporting` | scientific-visualization | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `pipeline.genomics.dna_short_read_alignment` | BWA-MEM2 | `PARTIAL_OVERLAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `data.genomics.hts_file_processing` | pysam + samtools | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `pipeline.transcriptomics.splice_aware_alignment` | STAR | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `pipeline.microbiology.prokaryotic_annotation` | Bakta + Prokka | `BASELINE_EQUIVALENT_PRESENT` | `SOURCE_FIRST_WITH_REMEDIATION` for Bakta; Prokka duplicate |
| `analysis.microbiology.bacterial_pangenome` | Roary | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `analysis.systems_biology.grn_inference` | Arboreto/GRNBoost2/GENIE3 | `CLEAR_GAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `toolkit.sequence.biopython` | two overlapping Biopython Skills | `PARTIAL_OVERLAP` | one source-first decomposition; one duplicate description |
| `integration.database.multi_service_client` | bioservices | `PARTIAL_OVERLAP` | `SOURCE_FIRST_WITH_REMEDIATION` |
| `database.cbioportal.cancer_genomics_query` | cBioPortal Skill | `BASELINE_EQUIVALENT_PRESENT` | `DUPLICATE_OR_SUPERSEDED` |
| `database.clinvar.variant_evidence_query` | ClinVar Skill | `BASELINE_EQUIVALENT_PRESENT` | `DUPLICATE_OR_SUPERSEDED` |

Cluster-level counts：

- `CLEAR_GAP`：10；
- `PARTIAL_OVERLAP`：4；
- `BASELINE_EQUIVALENT_PRESENT`：3；
- source-first/remediation clusters：15；
- duplicate/superseded clusters：2。

Skill-level disposition：

- `SOURCE_FIRST_WITH_REMEDIATION`：16；
- `DUPLICATE_OR_SUPERSEDED`：4。

## 3. 主要发现

### 3.1 统计建模是明确缺口

Biomni frozen baseline 没有公开的 PyMC 或 statsmodels typed tool。SciAgent 的两个 Skill 可以形成两个独立 Feature：

- Bayesian workflow：prior/likelihood、NUTS/ADVI、R-hat/ESS/divergence、posterior predictive、LOO/WAIC；
- classical statistical modeling：OLS/WLS/GLS、GLM、logit/probit/count、time series、diagnostics。

原 Skill 不能原样依赖：PyMC 指导错误地把 WAIC 当作 problematic LOO 的补救；statsmodels 指导把 diagnostic p-value 和 robust SE 简化成自动规则。Codex 应以官方 API 和受控 fixture 建立 characterization tests。

### 3.2 图像交互、ImageJ bridge 和通用处理应拆开

Biomni 已有 nnUNet、注册、形态分析等任务型图像工具，但没有：

- napari 式交互式多维 viewer；
- PyImageJ/Fiji 宏、Ops、ROI 和 plugin bridge；
- 通用、metadata-aware 的 scikit-image pipeline。

scikit-image 与 Biomni 现有图像处理有部分重叠；napari 和 PyImageJ 属于明确接口/工作流 gap。执行前必须固定 axis/scale metadata，阻止未审插件和首次运行时隐式下载。

### 3.3 可视化不能与统计推断混合

Plotly 和科学制图指南有独立价值，但必须保持：

- plotting 与 inference 分离；
- 不允许示例图自动生成显著性结论；
- HTML 输出明确 self-contained/CDN 和隐私策略；
- 期刊格式要求按目标期刊实时核对。

### 3.4 Genomics 基础设施存在“环境有工具、Agent 无 typed capability”的缺口

Biomni 有比较基因组 pipeline 和丰富环境依赖，但没有独立 exposed capability 来完成：

- BWA-MEM2 short-read alignment；
- pysam SAM/BAM/CRAM/VCF/BCF I/O；
- samtools sort/index/filter/QC；
- STAR splice-aware RNA alignment。

后续应把这些功能封装成 typed、versioned、reference-aware tools，而不是让 Agent 自由拼 shell 命令。

### 3.5 Bakta 和 Prokka 属于同一 Feature 的两个 Implementation

Biomni 已有 `annotate_bacterial_genome`，底层是 Prokka，因此 Prokka Skill 不应产生新 Feature。Bakta 则可以作为同一 `prokaryotic_annotation` Feature 的替代 Implementation，重点比较：

- 数据库 release；
- annotation schema；
- 输出格式；
- fragmented assemblies；
- provenance；
- 速度和一致性。

### 3.6 Roary 和 Arboreto 是新功能，但科学解释必须收紧

- Roary：应作为 bacterial pangenome workflow，而不是简单 presence/absence 结论；annotation consistency、fragmentation、paralog 和 population structure 必须进入合同。
- Arboreto：GRNBoost2/GENIE3 输出是 co-expression importance，不是因果调控。必须保存 seed、TF list、expression preprocessing 和 motif/perturbation validation 状态。

### 3.7 两个 Biopython Skills 高度重复且过宽

`biopython-molecular-biology` 与 `biopython-sequence-analysis` 不能各自成为一个 Feature。它们至少应拆为：

- sequence/file I/O；
- local sequence operations；
- Entrez retrieval；
- local/remote BLAST；
- pairwise/MSA alignment；
- phylogenetic tree handling；
- PDB structure I/O。

其中大部分已经与 Biomni 的分子生物学、数据库、BLAST 和比较基因组能力重叠。Codex 需要做 symbol-level mapping；第二个 Skill 暂视为描述层 duplicate。

### 3.8 bioservices 的增量不是“再增加 40 个数据库 wrapper”

Biomni 已有 40 个 exposed database/API descriptions。bioservices 的潜在增量是：

- 统一 client lifecycle；
- cross-database ID mapping；
- multi-service workflow；
- 标准化错误、timeout、rate limit 和 provenance。

旧 PICR/legacy method signatures 和多服务兼容性不能仅凭文档假设成立。

### 3.9 cBioPortal 和 ClinVar 已有 Biomni 等价能力

Biomni baseline 已暴露 `query_cbioportal` 和 `query_clinvar`。这两个 SciAgent Skills 仅作为 schema、解释边界和测试用例来源；不能创建重复 Feature。

## 4. 下一步

机器可读 Skill→cluster 映射：

`static-normalization-batch-002-manifest.jsonl`

Codex 工作包：

`CODEX_WORKPACK_002_SCIAGENT_TRANCHE_001.md`

后续 GPT Pro 静态批次继续从 SciAgent manifest 的下一个 `candidate=true` Skill 开始，不重复本批 20 条。
