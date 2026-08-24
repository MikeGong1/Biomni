# Current Feature Catalog — Phase 9A static research

状态：**PROVISIONAL STATIC CATALOG COMPLETE**

本目录由 Phase 8 的 598 个 `DEEP_AUDIT_CANDIDATE` family、SciAgent 203 个 active Skills、K-Dense／Kuan／BIDS／DataLad 的详细静态拆解和 frozen Biomni baseline 自动归一化生成。

它不是 runtime-verified catalog。正式 `feature-*` 和 `implementation-*` ID 仍需 Codex 在隔离环境完成代码级去重、测试和 cross-reference 后分配。

## 汇总

- Provisional Features：**91**
- P0／P1／P2／P3：**44／1／28／18**
- CLEAR_GAP：**59**
- PARTIAL_OVERLAP：**8**
- BASELINE_EQUIVALENT_PRESENT：**18**

## 领域分布

| Domain | Features |
|---|---|
| agent-core | 3 |
| analysis | 13 |
| bioimaging | 4 |
| data | 1 |
| data-standards | 4 |
| data_provenance | 1 |
| data_standard | 1 |
| database | 8 |
| deployment-interface | 3 |
| design | 1 |
| drug-discovery | 3 |
| genomics | 7 |
| guide | 1 |
| integration | 1 |
| interpretation | 1 |
| laboratory-automation | 1 |
| literature-evidence | 2 |
| pipeline | 4 |
| protein-structure | 5 |
| research | 1 |
| safety-governance | 1 |
| scientific-database | 9 |
| simulation | 1 |
| single-cell-spatial | 5 |
| statistics-evaluation | 4 |
| tool-skill-mcp | 3 |
| toolkit | 1 |
| visualization | 2 |

## Provisional Feature 列表

| ID | Priority | Feature key | Biomni gap | Families | SciAgent Skills | Capability |
|---|---|---|---|---|---|---|
| pfeature-000001 | P0 | agent.orchestration.multi_agent | CLEAR_GAP | 11 | 0 | 协调多个专门 Agent、supervisor 与 worker 完成科研任务。 |
| pfeature-000002 | P0 | agent.orchestration.planning_execution | CLEAR_GAP | 2 | 1 | 把科研目标拆成计划、工具调用和可恢复执行步骤。 |
| pfeature-000003 | P0 | agent.workflow.human_approval | CLEAR_GAP | 1 | 0 | 在关键科研步骤设置人工检查、调整、跳过和批准门。 |
| pfeature-000007 | P0 | analysis.bioimage.segmentation | CLEAR_GAP | 2 | 3 | 对显微、病理或医学图像执行分割和定量。 |
| pfeature-000009 | P0 | analysis.cell_cell_communication | CLEAR_GAP | 1 | 1 | 推断细胞间配体—受体通信及其条件差异。 |
| pfeature-000011 | P0 | analysis.drug.admet | CLEAR_GAP | 2 | 1 | 预测或分析化合物 ADMET、毒性和药代性质。 |
| pfeature-000012 | P0 | analysis.drug.sar_selectivity | CLEAR_GAP | 4 | 1 | 比较 SAR、选择性、多靶点活性和 assay 证据。 |
| pfeature-000020 | P0 | analysis.pathology.slide | CLEAR_GAP | 4 | 1 | 处理病理 whole-slide image、tile、组织区域和病理模型推理。 |
| pfeature-000023 | P0 | analysis.single_cell.qc_integration | CLEAR_GAP | 31 | 9 | 执行单细胞 QC、标准化、降维、批次整合和 embedding。 |
| pfeature-000024 | P0 | analysis.spatial_transcriptomics.workflow | CLEAR_GAP | 12 | 0 | 执行空间转录组加载、QC、区域、空间基因、去卷积和下游分析。 |
| pfeature-000025 | P0 | analysis.statistics.bayesian | CLEAR_GAP | 9 | 4 | 执行 Bayesian 建模、采样诊断、预测检验和模型比较。 |
| pfeature-000027 | P0 | analysis.statistics.classical | CLEAR_GAP | 15 | 4 | 执行回归、GLM、time-series、mixed effects 和诊断。 |
| pfeature-000029 | P0 | analysis.statistics.survival | RELATED_OVERLAP_NOT_EQUIVALENT | 5 | 2 | 执行 censoring-aware survival、competing risks 和时间事件评估。 |
| pfeature-000030 | P0 | analysis.structure.docking_screening | RELATED_OVERLAP_NOT_EQUIVALENT | 5 | 6 | 执行 docking、virtual screening 和结构基础候选排序。 |
| pfeature-000033 | P0 | data.genomics.hts_processing | CLEAR_GAP | 9 | 6 | 读写、排序、索引、过滤和检查 SAM/BAM/CRAM/VCF/BCF。 |
| pfeature-000034 | P0 | data.local_cache.database | CLEAR_GAP | 1 | 0 | 把大型科学数据库构建为可版本化的本地缓存和快速查询层。 |
| pfeature-000035 | P0 | data.provenance.versioned_research | CLEAR_GAP | 4 | 0 | 对科研数据、运行命令、容器和发布建立版本化 provenance。 |
| pfeature-000036 | P0 | data.standard.ann_data_omics | RELATED_OVERLAP_NOT_EQUIVALENT | 8 | 2 | 管理 AnnData、MuData 或组学矩阵 schema、坐标和 provenance。 |
| pfeature-000037 | P0 | data.standard.bids | PARTIAL_OVERLAP | 9 | 0 | 组织和验证 BIDS 数据、metadata、derivatives 和 BIDS Apps。 |
| pfeature-000044 | P0 | database.drug.binding_activity | CLEAR_GAP | 1 | 4 | 查询药物、化合物、靶点、结合亲和力和生物活性数据。 |
| pfeature-000045 | P0 | database.expression_qtl | CLEAR_GAP | 1 | 4 | 查询组织表达、eQTL、sQTL、eGene 或公共表达数据。 |
| pfeature-000056 | P0 | deployment.api.server | CLEAR_GAP | 10 | 3 | 通过 API、FastAPI、Rust、MCP 或 Web 服务暴露科研计算。 |
| pfeature-000057 | P0 | deployment.cloud_hpc.job | CLEAR_GAP | 10 | 3 | 调度云端、GPU、HPC、sandbox 和并发科学任务。 |
| pfeature-000058 | P0 | deployment.container.environment | CLEAR_GAP | 13 | 2 | 使用 Docker、uv、Conda 或可复现环境配置科研工具链。 |
| pfeature-000059 | P0 | design.genomics.crispr | CLEAR_GAP | 2 | 2 | 设计或评估 CRISPR guide、编辑位点和脱靶风险。 |
| pfeature-000061 | P0 | design.protein.sequence | CLEAR_GAP | 4 | 2 | 生成、优化或筛选具有目标性质的蛋白序列。 |
| pfeature-000062 | P0 | evaluation.benchmark.reproducibility | CLEAR_GAP | 20 | 11 | 构建可复现 benchmark、golden fixtures、误差分析和回归测试。 |
| pfeature-000063 | P0 | governance.security_privacy | CLEAR_GAP | 11 | 10 | 控制认证、secret、PHI/PII、数据外传和危险操作。 |
| pfeature-000066 | P0 | integration.database.multi_service_client | CLEAR_GAP | 2 | 8 | 统一管理多个生物数据库客户端、ID mapping、错误、限速和 provenance。 |
| pfeature-000068 | P0 | knowledge.evidence.claim_verification | CLEAR_GAP | 3 | 6 | 从来源中提取证据、核对主张并保存引用链。 |
| pfeature-000069 | P0 | knowledge.literature.search_retrieval | CLEAR_GAP | 8 | 2 | 检索论文、摘要、全文和相关文献。 |
| pfeature-000070 | P0 | laboratory.automation.instrument | CLEAR_GAP | 0 | 4 | 控制实验机器人、液体处理、仪器、校准和人工批准。 |
| pfeature-000071 | P0 | model.protein.structure_prediction | CLEAR_GAP | 3 | 3 | 预测、检索或比较蛋白三维结构和复合物。 |
| pfeature-000072 | P0 | model.spatial.histology_to_expression | CLEAR_GAP | 1 | 0 | 根据病理图像预测空间基因表达或空间分子表型。 |
| pfeature-000074 | P0 | pipeline.genomics.phylogenetics | CLEAR_GAP | 0 | 1 | 组织序列比对、修剪、树推断、支持度和系统发育可视化。 |
| pfeature-000077 | P0 | pipeline.genomics.variant_calling_annotation | CLEAR_GAP | 8 | 4 | 执行变异检测、标准化、过滤和功能注释。 |
| pfeature-000082 | P0 | simulation.molecular_dynamics | CLEAR_GAP | 5 | 4 | 配置并运行分子动力学模拟，分析轨迹、稳定性和相互作用。 |
| pfeature-000084 | P0 | tooling.mcp.client_server | CLEAR_GAP | 42 | 0 | 通过 MCP 发现、调用或暴露科研工具。 |
| pfeature-000085 | P0 | tooling.sandbox.code_execution | CLEAR_GAP | 4 | 5 | 在隔离环境中执行 Python、R、shell 或 notebook 科研代码。 |
| pfeature-000086 | P0 | tooling.skill.registry_discovery | CLEAR_GAP | 1 | 21 | 注册、检索、选择和加载科学 Skills 或工具。 |
| pfeature-000090 | P0 | visualization.scientific.interactive | CLEAR_GAP | 8 | 4 | 生成可交互科学图形、3D 可视化和可追溯导出。 |
| pfeature-000091 | P0 | workflow.drug.regulatory_safety | CLEAR_GAP | 11 | 13 | 组织药物发现安全、法规来源和 stage-gate 决策支持。 |
| pfeature-000076 | P0 | pipeline.genomics.read_alignment | RELATED_OVERLAP_NOT_EQUIVALENT | 2 | 1 | 执行 DNA 或 RNA reads 的参考比对并保存 reference provenance。 |
| pfeature-000051 | P0 | database.pathway.network | RELATED_OVERLAP_NOT_EQUIVALENT | 2 | 3 | 查询 pathway、interaction、gene set 和生物网络数据库。 |
| pfeature-000081 | P1 | research.reference.unclassified | CLEAR_GAP | 348 | 4 | Bulk RNA-seq DE with PyDESeq2: load counts, normalize, fit negative binomial models, Wald test (BH-FDR), LFC shrinkage, volcano/MA plots. Use for two-group comparisons, multi-factor designs with batch correction, multiple contrasts. |
| pfeature-000032 | P2 | data.genomics.hts_file_processing | CLEAR_GAP | 0 | 2 | Read/write SAM/BAM/CRAM, VCF/BCF, FASTA/FASTQ. Region queries, pileup, variant filtering, read groups. Python htslib wrapper exposing samtools/bcftools CLI. Use STAR/BWA for alignment; GATK/DeepVariant for variant calling. |
| pfeature-000017 | P2 | analysis.microbiology.bacterial_pangenome | CLEAR_GAP | 0 | 1 | Compute the bacterial pan-genome from Prokka/Bakta GFF3 annotations with Roary's CD-HIT + BLAST + MCL clustering pipeline. Builds gene presence/absence matrices, core/soft-core/shell/cloud partitions, multi-FASTA core gene alignments (with `-e`), and a pan-genome reference. Use Panaroo for higher-accuracy pan-genomes from highly fragmented assemblies, PIRATE for paralog-aware clustering, or PPanGGOLiN for graph-based partitioning. |
| pfeature-000026 | P2 | analysis.statistics.bayesian_modeling | CLEAR_GAP | 0 | 1 | priors and likelihoods; NUTS/ADVI; R-hat/ESS/divergence diagnostics; prior/posterior predictive checks; LOO/WAIC comparison; hierarchical/logistic/GP models |
| pfeature-000028 | P2 | analysis.statistics.classical_models | CLEAR_GAP | 0 | 1 | OLS/WLS/GLS; GLM; logit/probit/count models; ARIMA/SARIMAX; diagnostics; formula API; power and mixed effects |
| pfeature-000031 | P2 | analysis.systems_biology.grn_inference | CLEAR_GAP | 0 | 1 | GRN inference from expression via GRNBoost2 (gradient boosting) or GENIE3 (Random Forest). Load matrix, filter by TFs, infer TF-target-importance links, save network. Dask-parallelized to single-cell scale. Core SCENIC component. |
| pfeature-000064 | P2 | guide.visualization.scientific_reporting | CLEAR_GAP | 0 | 1 | chart selection; color accessibility; composition; journal formatting; statistical annotation principles |
| pfeature-000065 | P2 | integration.bioimage.imagej_bridge | CLEAR_GAP | 0 | 1 | Headless/GUI Fiji initialization, macros, Ops, plugins, ROI/results and array conversion |
| pfeature-000080 | P2 | pipeline.transcriptomics.splice_aware_alignment | CLEAR_GAP | 0 | 1 | Splice-aware RNA-seq aligner producing sorted BAM and splice junction tables. Builds genome index, runs two-pass alignment for better junctions. Outputs sorted BAM, junctions (SJ.out.tab), stats (Log.final.out), optional gene counts. Use Salmon for fast pseudoalignment; STAR when a BAM is needed for variant calling, IGV, or ENCODE pipelines. |
| pfeature-000088 | P2 | visualization.bioimage.interactive_viewer | CLEAR_GAP | 0 | 1 | Interactive multidimensional image, label, point, shape and track viewing plus screenshots |
| pfeature-000089 | P2 | visualization.interactive.plotly | CLEAR_GAP | 0 | 1 | Plotly Express; graph objects; heatmaps; 3D; subplots; HTML/static export; interactive controls |
| pfeature-000004 | P2 | analysis.bindingdb.sar_selectivity | CLEAR_GAP | 0 | 0 | 对 BindingDB 批量数据执行 SAR、选择性和多靶点活性比较。 |
| pfeature-000010 | P2 | analysis.depmap.cancer_dependency | CLEAR_GAP | 0 | 0 | 执行 Chronos 基因依赖、选择性依赖、共依赖和生物标志物分析。 |
| pfeature-000018 | P2 | analysis.molecular_dynamics.trajectory | CLEAR_GAP | 0 | 0 | 用 MDAnalysis 计算 RMSD、RMSF、接触和轨迹摘要。 |
| pfeature-000021 | P2 | analysis.scrna.rna_velocity | CLEAR_GAP | 0 | 0 | 执行 scVelo 的预处理、随机/动力学 RNA velocity、latent time 和 driver 分析。 |
| pfeature-000039 | P2 | data_standard.bids.organization_validation | CLEAR_GAP | 0 | 0 | 组织 BIDS 命名、PyBIDS 查询、验证、DICOM 转换、metadata/events/participants、derivatives 和 BIDS Apps。 |
| pfeature-000047 | P2 | database.gtex.expression_qtl | CLEAR_GAP | 0 | 0 | 查询 GTEx 的组织表达、eQTL、sQTL 和 eGene 信息。 |
| pfeature-000079 | P2 | pipeline.phylogenetics.alignment_tree | CLEAR_GAP | 0 | 0 | 组织 MAFFT/TrimAl、IQ-TREE/FastTree 和 ETE3 的系统发育分析流程。 |
| pfeature-000083 | P2 | simulation.molecular_dynamics.protocol | CLEAR_GAP | 0 | 0 | 用 OpenMM 建立、最小化、平衡并运行分子动力学模拟。 |
| pfeature-000022 | P2 | analysis.single_cell.annotation | BASELINE_EQUIVALENT_PRESENT | 6 | 0 | 使用 marker、reference 或模型完成单细胞类型注释。 |
| pfeature-000041 | P2 | database.cancer_genomics | BASELINE_EQUIVALENT_PRESENT | 9 | 2 | 查询癌症基因组、突变、CNA、表达和临床队列信息。 |
| pfeature-000087 | P2 | toolkit.sequence.biopython | PARTIAL_OVERLAP | 0 | 2 | Molecular biology toolkit: sequence manipulation, FASTA/GenBank/PDB I/O, NCBI Entrez, BLAST automation, pairwise/MSA alignment, Bio.PDB, phylogenetic trees. Use for batch processing, custom pipelines, format conversion, PubMed/GenBank queries. For quick gene lookups use gget; for multi-service REST APIs use bioservices. |
| pfeature-000005 | P2 | analysis.bioimage.general_processing | PARTIAL_OVERLAP | 0 | 1 | Scientific image I/O, filtering, segmentation, morphology, measurement and features |
| pfeature-000073 | P2 | pipeline.genomics.dna_short_read_alignment | PARTIAL_OVERLAP | 0 | 1 | Fast short-read DNA aligner for WGS/WES/ChIP-seq. 2× faster BWA-MEM successor; outputs SAM/BAM with read group headers for GATK. Primary plus supplementary records for chimeric reads. Use STAR for RNA-seq splice-aware alignment; Bowtie2 is a comparable alternative. |
| pfeature-000008 | P2 | analysis.cbioportal.clinical_survival_workflow | PARTIAL_OVERLAP | 0 | 0 | 把 cBioPortal 查询结果组织成队列比较、临床变量和生存分析工作流。 |
| pfeature-000016 | P2 | analysis.jaspar.motif_scan_variant_impact | PARTIAL_OVERLAP | 0 | 0 | 将 JASPAR PFM/PWM 用于双链序列扫描和变异影响评分。 |
| pfeature-000019 | P2 | analysis.monarch.semantic_similarity_cross_species | PARTIAL_OVERLAP | 0 | 0 | 执行表型语义相似度和跨物种 phenotype 映射。 |
| pfeature-000055 | P2 | database.variant.population | BASELINE_EQUIVALENT_PRESENT | 2 | 2 | 查询人群遗传变异、频率、constraint 和结构变异证据。 |
| pfeature-000040 | P2 | database.bindingdb.affinity_query | RELATED_OVERLAP_NOT_EQUIVALENT | 0 | 0 | 查询 BindingDB 的蛋白—配体结合数据，并按靶点、配体或亲和力条件检索。 |
| pfeature-000053 | P3 | database.protein.domain_structure | BASELINE_EQUIVALENT_PRESENT | 0 | 3 | 查询蛋白结构域、家族、位点、序列和结构数据库。 |
| pfeature-000006 | P3 | analysis.bioimage.registration | BASELINE_EQUIVALENT_PRESENT | 0 | 1 | 对医学或显微图像执行刚性、仿射或形变配准。 |
| pfeature-000013 | P3 | analysis.genomics.regulatory_motif | BASELINE_EQUIVALENT_PRESENT | 0 | 3 | 执行 TF motif 查询、序列扫描、富集和变异影响分析。 |
| pfeature-000054 | P3 | database.variant.clinical_evidence | BASELINE_EQUIVALENT_PRESENT | 0 | 4 | 查询 ClinVar、dbSNP 或其他变异临床证据，并保留冲突和版本信息。 |
| pfeature-000038 | P3 | data_provenance.datalad.versioned_research_data | CLEAR_GAP | 0 | 0 | 用 DataLad/git-annex 管理科研数据、内容获取、rerun provenance、containers、siblings 和发布。 |
| pfeature-000067 | P3 | interpretation.gnomad.constraint_sv_acmg | CLEAR_GAP | 0 | 0 | 把 gnomAD constraint、LoF、SV 和频率结果用于变异解释辅助。 |
| pfeature-000014 | P3 | analysis.glyco.engineering | BASELINE_EQUIVALENT_PRESENT | 1 | 0 | 检测、解释或工程化蛋白糖基化位点。 |
| pfeature-000052 | P3 | database.phenotype.disease_ontology | BASELINE_EQUIVALENT_PRESENT | 0 | 2 | 查询 phenotype、disease、ontology、gene association 和跨物种映射。 |
| pfeature-000075 | P3 | pipeline.genomics.prokaryotic_annotation | BASELINE_EQUIVALENT_PRESENT | 0 | 2 | 对细菌或古菌基因组执行结构与功能注释。 |
| pfeature-000060 | P3 | design.glyco.sequence_engineering | PARTIAL_OVERLAP | 0 | 0 | 提出增加、移除或调整糖基化位点的蛋白序列编辑方案。 |
| pfeature-000078 | P3 | pipeline.microbiology.prokaryotic_annotation | BASELINE_EQUIVALENT_PRESENT | 0 | 2 | Annotate bacterial and archaeal genomes and plasmids with Bakta's Prodigal/HMM/diamond pipeline. Identifies CDS, ncRNA, tRNA, rRNA, tmRNA, sORFs, CRISPR arrays, oriC/oriV/oriT, and gaps against a curated UniRef-derived database. Produces NCBI-compatible GFF3, GenBank, EMBL, JSON, FASTA, TSV, and a circular genome plot. Use Prokka for legacy pipelines or non-bacterial kingdoms; PGAP for NCBI GenBank submission. |
| pfeature-000042 | P3 | database.cbioportal.cancer_genomics_query | BASELINE_EQUIVALENT_PRESENT | 0 | 1 | 查询 cBioPortal 的癌症研究、突变、拷贝数和临床数据。 |
| pfeature-000043 | P3 | database.clinvar.variant_evidence_query | BASELINE_EQUIVALENT_PRESENT | 0 | 1 | Query NCBI ClinVar via E-utilities for variant clinical significance, pathogenicity, disease associations. Search by gene/rsID/condition/review status; returns ClinSig, submitter data, conditions, HGVS. For GWAS use gwas-database; for variant consequence prediction use Ensembl VEP. |
| pfeature-000015 | P3 | analysis.glyco.motif_detection | BASELINE_EQUIVALENT_PRESENT | 0 | 0 | 扫描 N-糖基化 sequon，并给出启发式 O-糖基化热点。 |
| pfeature-000046 | P3 | database.gnomad.population_frequency | BASELINE_EQUIVALENT_PRESENT | 0 | 0 | 查询 gnomAD 的基因和变异人群频率信息。 |
| pfeature-000048 | P3 | database.interpro.domain_annotation | BASELINE_EQUIVALENT_PRESENT | 0 | 0 | 查询蛋白结构域、家族、位点、GO 和 domain architecture。 |
| pfeature-000049 | P3 | database.jaspar.matrix_query | BASELINE_EQUIVALENT_PRESENT | 0 | 0 | 查询 JASPAR 转录因子矩阵与元数据。 |
| pfeature-000050 | P3 | database.monarch.phenotype_association | BASELINE_EQUIVALENT_PRESENT | 0 | 0 | 查询 phenotype—gene—disease 关联和 HPO 实体。 |

机器可读版本：`phase-9/provisional-features.jsonl`。
