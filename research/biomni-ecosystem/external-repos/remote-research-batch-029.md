# 远程调研 Batch 029

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1213–1262**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 1 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 2 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 18 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 16 |
| 分类 `LOW_INFORMATION_RECHECK` | 2 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 8 |
| 标记 `ARCHIVED_OR_DISABLED` | 1 |
| 标记 `CHILD_FORK_SURFACE` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 44 |
| 标记 `LICENSE_UNCLEAR` | 21 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1213 | `dynamicslab/databook_matlab`<br>source=`dynamicslab/databook_matlab` | `repo-005903` `dabulseco/databook_matlab`（REPRESENTATIVE；parent=dynamicslab/databook_matlab） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1214 | `zenodraft/metadata-schema-zenodo`<br>source=`zenodraft/metadata-schema-zenodo` | `repo-005095` `yarikoptic/metadata-schema-zenodo`（REPRESENTATIVE；parent=zenodraft/metadata-schema-zenodo） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1215 | `facebookresearch/esm`<br>source=`facebookresearch/esm` | `repo-006960` `Vik-u/esm`（REPRESENTATIVE；parent=facebookresearch/esm）<br>`repo-001796` `sbonner0/esm`（MEMBER；parent=facebookresearch/esm） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1216 | `gold-standard-phantoms/bids-pydantic`<br>source=`gold-standard-phantoms/bids-pydantic` | `repo-004465` `yarikoptic/bids-pydantic`（REPRESENTATIVE；parent=gold-standard-phantoms/bids-pydantic） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1217 | `linkml/schemasheets`<br>source=`linkml/schemasheets` | `repo-005544` `yarikoptic/schemasheets`（REPRESENTATIVE；parent=linkml/schemasheets） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1218 | `mawa00006/biosensors`<br>source=`mawa00006/Biosensors` | `repo-007552` `sphia-g/Biosensors`（REPRESENTATIVE；parent=mawa00006/Biosensors） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1219 | `zarr-developers/zarr-specs`<br>source=`zarr-developers/zarr-specs` | `repo-005779` `yarikoptic/zarr-specs`（REPRESENTATIVE；parent=zarr-developers/zarr-specs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1220 | `mr-milk/imc-analysis-pipeline`<br>source=`Mr-Milk/IMC-Analysis-Pipeline` | `repo-003126` `Mr-Milk/IMC-Analysis-Pipeline`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1221 | `juliacamps/cardiac-digital-twin-purkinje`<br>source=`juliacamps/Cardiac-Digital-Twin-Purkinje` | `repo-006834` `tangxuan82/Cardiac-Digital-Twin-Purkinje`（REPRESENTATIVE；parent=juliacamps/Cardiac-Digital-Twin-Purkinje） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1222 | `dandi/dandidav`<br>source=`dandi/dandidav` | `repo-004643` `yarikoptic/dandidav`（REPRESENTATIVE；parent=dandi/dandidav） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1223 | `ome/ome-ngff-validator`<br>source=`ome/ome-ngff-validator` | `repo-005267` `yarikoptic/ome-ngff-validator`（REPRESENTATIVE；parent=ome/ome-ngff-validator） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1224 | `highskyno1/mimo_doa`<br>source=`highskyno1/MIMO_DOA` | `repo-006509` `gutendzx/MIMO_DOA`（REPRESENTATIVE；parent=highskyno1/MIMO_DOA） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1225 | `aplbrain/benchmark-metadata`<br>source=`aplbrain/BENCHMARK-Metadata` | `repo-004444` `yarikoptic/BENCHMARK-Metadata`（REPRESENTATIVE；parent=aplbrain/BENCHMARK-Metadata） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1226 | `cbi-pitt/brainpi`<br>source=`CBI-PITT/BrAinPI` | `repo-004510` `yarikoptic/BrAinPI`（REPRESENTATIVE；parent=CBI-PITT/BrAinPI） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1227 | `liripo/scport`<br>source=`Liripo/scPort` | `repo-003084` `Liripo/scPort`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1228 | `wt12318/car-toner`<br>source=`wt12318/CAR-Toner` | `repo-002577` `changwn/CAR-Toner`（REPRESENTATIVE；parent=wt12318/CAR-Toner） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1229 | `ncbi/icn3d`<br>source=`ncbi/icn3d` | `repo-004964` `yarikoptic/icn3d`（REPRESENTATIVE；parent=ncbi/icn3d） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1230 | `google-deepmind/alphafold`<br>source=`google-deepmind/alphafold` | `repo-004379` `yarikoptic/alphafold`（REPRESENTATIVE；parent=google-deepmind/alphafold） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1231 | `datalad/datalad-metalad`<br>source=`datalad/datalad-metalad` | `repo-004679` `yarikoptic/datalad-metalad`（REPRESENTATIVE；parent=datalad/datalad-metalad） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1232 | `idea-research/grounded-segment-anything`<br>source=`IDEA-Research/Grounded-Segment-Anything` | `repo-006429` `chaudhariatul/Grounded-SAM`（REPRESENTATIVE；parent=IDEA-Research/Grounded-Segment-Anything） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1233 | `zhigroup/pytorch_ehr`<br>source=`ZhiGroup/pytorch_ehr` | `repo-002196` `th86/pytorch_ehr`（REPRESENTATIVE；parent=ZhiGroup/pytorch_ehr） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1234 | `dattalab/moseq2-app`<br>source=`dattalab/moseq2-app` | `repo-005126` `yarikoptic/moseq2-app`（REPRESENTATIVE；parent=dattalab/moseq2-app） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1235 | `dynamicslab/databook_python`<br>source=`dynamicslab/databook_python` | `repo-005904` `dabulseco/databook_python`（REPRESENTATIVE；parent=dynamicslab/databook_python） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1236 | `incatools/ontology-access-kit`<br>source=`INCATools/ontology-access-kit` | `repo-005272` `yarikoptic/ontology-access-kit`（REPRESENTATIVE；parent=INCATools/ontology-access-kit） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1237 | `translatorsri/benchmarks`<br>source=`TranslatorSRI/Benchmarks` | `repo-000894` `andrewsu/Benchmarks`（REPRESENTATIVE；parent=TranslatorSRI/Benchmarks） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1238 | `cccofficial/combinatorial_signaling_motif_libraries`<br>source=`CCCofficial/combinatorial_signaling_motif_libraries` | `repo-002587` `changwn/combinatorial_signaling_motif_libraries`（REPRESENTATIVE；parent=CCCofficial/combinatorial_signaling_motif_libraries） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1239 | `devindesilva/druggableprotienprediction`<br>source=`DevinDeSilva/DruggableProtienPrediction` | `repo-006011` `DevinDeSilva/DruggableProtienPrediction`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1240 | `talmolab/sleap`<br>source=`talmolab/sleap` | `repo-005590` `yarikoptic/sleap`（REPRESENTATIVE；parent=talmolab/sleap） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1241 | `spm/spm`<br>source=`spm/spm` | `repo-005618` `yarikoptic/spm`（REPRESENTATIVE；parent=spm/spm） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1242 | `monk1337/resp`<br>source=`monk1337/resp` | `repo-006757` `Charvijain16/resp`（REPRESENTATIVE；parent=monk1337/resp） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1243 | `neurodatawithoutborders/pynwb`<br>source=`NeurodataWithoutBorders/pynwb` | `repo-005425` `yarikoptic/pynwb`（REPRESENTATIVE；parent=NeurodataWithoutBorders/pynwb） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1244 | `recess-eu-project/benchscofi`<br>source=`RECeSS-EU-Project/benchscofi` | `repo-007052` `jaybee84/benchscofi`（REPRESENTATIVE；parent=RECeSS-EU-Project/benchscofi） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1245 | `adaptivemotorcontrollab/amadeusgpt`<br>source=`AdaptiveMotorControlLab/AmadeusGPT` | `repo-004380` `yarikoptic/AmadeusGPT`（REPRESENTATIVE；parent=AdaptiveMotorControlLab/AmadeusGPT） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1246 | `mr-milk/spatialentropy`<br>source=`Mr-Milk/SpatialEntropy` | `repo-003152` `Mr-Milk/SpatialEntropy`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1247 | `mr-milk/aquila`<br>source=`Mr-Milk/Aquila` | `repo-003112` `Mr-Milk/Aquila`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1248 | `nipy/nitime`<br>source=`nipy/nitime` | `repo-005232` `yarikoptic/nitime`（REPRESENTATIVE；parent=nipy/nitime） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1249 | `dmd/rapidtide-cloud`<br>source=`dmd/rapidtide-cloud` | `repo-005478` `yarikoptic/rapidtide-cloud`（REPRESENTATIVE；parent=dmd/rapidtide-cloud） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1250 | `nf-core/rnaseq`<br>source=`nf-core/rnaseq` | `repo-004151` `vladsavelyev/rnaseq`（REPRESENTATIVE；parent=nf-core/rnaseq） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1251 | `pydicom/pylibjpeg-libjpeg`<br>source=`pydicom/pylibjpeg-libjpeg` | `repo-005417` `yarikoptic/pylibjpeg-libjpeg`（REPRESENTATIVE；parent=pydicom/pylibjpeg-libjpeg） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1252 | `public-neuro/public-neuro.github.io`<br>source=`Public-nEUro/Public-nEUro.github.io` | `repo-005387` `yarikoptic/Public-nEUro.github.io`（REPRESENTATIVE；parent=Public-nEUro/Public-nEUro.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1253 | `pquochuy/xsleepnet`<br>source=`pquochuy/xsleepnet` | `repo-006562` `gutendzx/xsleepnet`（REPRESENTATIVE；parent=pquochuy/xsleepnet） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1254 | `neurovault/neurovault`<br>source=`NeuroVault/NeuroVault` | `repo-005198` `yarikoptic/NeuroVault`（REPRESENTATIVE；parent=NeuroVault/NeuroVault） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1255 | `smeisler/fsub_extractor`<br>source=`smeisler/fsub_extractor` | `repo-004842` `yarikoptic/fsub_extractor`（REPRESENTATIVE；parent=smeisler/fsub_extractor） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1256 | `nilearn/nilearn`<br>source=`nilearn/nilearn` | `repo-005220` `yarikoptic/nilearn`（REPRESENTATIVE；parent=nilearn/nilearn） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1257 | `hazyresearch/hyena-dna`<br>source=`HazyResearch/hyena-dna` | `repo-001932` `shantanusharma/hyena-dna`（REPRESENTATIVE；parent=HazyResearch/hyena-dna） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1258 | `rly/ndx-structured-behavior`<br>source=`rly/ndx-structured-behavior` | `repo-005158` `yarikoptic/ndx-beadl`（REPRESENTATIVE；parent=rly/ndx-structured-behavior） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1259 | `little2b/the-rf-gsea-method`<br>source=`little2b/the-RF-GSEA-Method` | `repo-006127` `little2b/the-RF-GSEA-Method`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1260 | `zenodo/zenodo`<br>source=`zenodo/zenodo` | `repo-005782` `yarikoptic/zenodo`（REPRESENTATIVE；parent=zenodo/zenodo） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1261 | `jonescompneurolab/hnn-core`<br>source=`jonescompneurolab/hnn-core` | `repo-004955` `yarikoptic/hnn-core`（REPRESENTATIVE；parent=jonescompneurolab/hnn-core） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1262 | `dandi/zarr_checksum`<br>source=`dandi/zarr_checksum` | `repo-005781` `yarikoptic/zarr_checksum`（REPRESENTATIVE；parent=dandi/zarr_checksum） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1213–1262`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-029-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
