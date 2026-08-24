# Phase 9 Feature Taxonomy v0.1

状态：`ACTIVE_PROVISIONAL`

用途：将仓库级 Change／Lineage 转换为可比较的科学 Agent Feature 和具体 Implementation。

## 1. Feature 的定义

Feature 表示用户能够观察到的稳定能力，不等同于仓库、文件、Skill、API endpoint 或 UI 页面。

Feature 应用一句话描述：

> 在明确输入、约束和输出条件下，系统能够完成什么科学或工程任务。

同一个 Feature 可以有多个 Implementation；同一个 Skill 也可以拆成多个 Feature。

## 2. Implementation 的定义

Implementation 表示某个 Feature 的具体实现，包括：

- source repository 和 immutable commit；
- branch／PR／tag；
- files 和 symbols；
- tool/API/model/data dependencies；
- 输入输出合同；
- lineage；
- copied／adapted／wrapped／translated／rewritten 状态；
- scientific、安全、隐私和 runtime 状态。

## 3. 一级分类

### A. Agent Core 与 Orchestration

- planning；
- tool selection；
- multi-agent routing；
- supervisor/worker graph；
- human approval gate；
- retry/repair；
- memory/session；
- trace/provenance。

### B. Tool、Skill 与 MCP 基础设施

- Skill registry；
- tool schema；
- dynamic tool loading；
- MCP client/server；
- plugin discovery；
- tool permission；
- sandbox execution。

### C. 文献、知识与证据

- literature search；
- full-text retrieval；
- citation graph；
- evidence extraction；
- claim verification；
- regulatory source tracking。

### D. 科学数据库与检索

- protein/structure database；
- variant/population database；
- cancer genomics；
- expression/QTL；
- drug/compound/binding；
- phenotype/disease；
- pathway/ontology；
- clinical trials/labels。

### E. Genomics、Transcriptomics 与 Epigenomics

- sequence operations；
- variant calling/annotation；
- comparative genomics；
- phylogenetics；
- bulk RNA-seq；
- ChIP/ATAC/Hi-C；
- motif analysis；
- genome editing design。

### F. Single-cell 与 Spatial Omics

- QC/preprocessing；
- integration/embedding；
- cell-type annotation；
- RNA velocity；
- spatial domains；
- deconvolution；
- cell-cell communication；
- histology-to-expression。

### G. Protein、Structural Biology 与 Biophysics

- structure retrieval/prediction；
- domain annotation；
- molecular dynamics；
- docking；
- disorder；
- protein design；
- glycoengineering。

### H. Drug Discovery 与 Pharmacology

- target discovery；
- binding/SAR/selectivity；
- virtual screening；
- ADMET；
- PBPK/PK；
- safety/regulatory；
- repurposing。

### I. Bioimaging、Pathology 与 Visualization

- image I/O；
- segmentation；
- registration；
- tracking；
- pathology slide analysis；
- 2D/3D visualization；
- publication graphics。

### J. Statistics、Modeling 与 Evaluation

- statistical modeling；
- Bayesian analysis；
- survival analysis；
- benchmark；
- uncertainty；
- reproducibility；
- model comparison。

### K. Data Engineering、Standards 与 Provenance

- data ingestion；
- local cache；
- schema conversion；
- BIDS/AnnData/VCF 等标准；
- versioned data；
- workflow provenance；
- artifact catalog；
- export。

### L. Deployment、Workspace 与 Interface

- CLI/API；
- Web UI；
- notebook；
- Docker/uv/Conda；
- cloud/HPC；
- multi-user workspace；
- job management。

### M. Safety、Privacy 与 Governance

- authentication/authorization；
- secret handling；
- PHI/PII control；
- data egress；
- model/checkpoint trust；
- destructive-operation approval；
- publication review。

### N. Laboratory Automation

- robot protocol；
- liquid handling；
- instrument control；
- calibration；
- operator approval；
- biosafety/waste。

## 4. Feature identity rules

以下情况通常是同一 Feature：

- 同一数据库的不同 wrapper，只是参数或 UI 不同；
- 同一分析方法的 CLI、Python 和 MCP 封装；
- fork 中没有新增可观察行为；
- 文档更新但实现合同不变。

以下情况通常应拆成不同 Feature：

- query 与 downstream statistical interpretation；
- data acquisition 与 clinical decision；
- model inference 与 visualization；
- simulation execution 与 trajectory analysis；
- motif detection 与 sequence engineering；
- source management 与 destructive publish/drop；
- UI 本身新增了审批、协作或 provenance 工作流。

## 5. Biomni gap 分类

- `BASELINE_EQUIVALENT_PRESENT`：Biomni 已有等价能力；
- `PARTIAL_OVERLAP`：Biomni 有部分能力，但缺少重要行为；
- `RELATED_OVERLAP_NOT_EQUIVALENT`：有相关工具，但数据源或合同不同；
- `CLEAR_GAP`：冻结基线中没有相应 exposed capability；
- `UNKNOWN_REQUIRES_CODE_COMPARE`：当前证据不足。

## 6. Research disposition

- `SOURCE_FIRST_RESEARCH_CANDIDATE`
- `SOURCE_FIRST_WITH_REMEDIATION`
- `REFERENCE_ONLY_BLOCKED`
- `DUPLICATE_OR_SUPERSEDED`
- `PUBLICATION_REVIEW_REQUIRED`

license 不用于功能分数，但必须保留在 provenance。科学、安全、隐私、临床和 runtime 风险独立决定是否可以依赖或执行。

## 7. Canonical ID 分配条件

Feature ID：

- capability statement 稳定；
- 至少一个可观察 Implementation；
- 已完成当前 cluster 的 semantic dedup；
- 与 Biomni baseline 有明确关系。

Implementation ID：

- immutable source identity；
- files/symbols；
- 行为合同；
- lineage；
- scientific/security/privacy/runtime 状态；
- provenance 字段；
- copied/adapted/wrapped/rewritten 状态。

## 8. 当前应用顺序

1. K-Dense／Kuan 12 Skills、BIDS、DataLad；
2. SciAgent 203 Skills；
3. ChatSpatial／DeepSpot-M；
4. ezST；
5. Aquila-next；
6. gnomAD_DB；
7. 其余 598 个 `DEEP_AUDIT_CANDIDATE` family。
