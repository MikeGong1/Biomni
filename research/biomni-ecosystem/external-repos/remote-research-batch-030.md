# 远程调研 Batch 030

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1263–1312**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 2 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 19 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 19 |
| 分类 `LOW_INFORMATION_RECHECK` | 3 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 4 |
| 标记 `CHILD_FORK_SURFACE` | 2 |
| 标记 `FORK_LINEAGE_REQUIRED` | 46 |
| 标记 `LICENSE_UNCLEAR` | 20 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1263 | `flatironinstitute/caiman`<br>source=`flatironinstitute/CaImAn` | `repo-004530` `yarikoptic/CaImAn`（REPRESENTATIVE；parent=flatironinstitute/CaImAn） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1264 | `scratchrealm/pc-spike-sorting`<br>source=`scratchrealm/pc-spike-sorting` | `repo-005322` `yarikoptic/pc-spike-sorting`（REPRESENTATIVE；parent=scratchrealm/pc-spike-sorting） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1265 | `gallantlab/pycortex`<br>source=`gallantlab/pycortex` | `repo-005399` `yarikoptic/pycortex`（REPRESENTATIVE；parent=gallantlab/pycortex） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1266 | `gallantlab/himalaya`<br>source=`gallantlab/himalaya` | `repo-004951` `yarikoptic/himalaya`（REPRESENTATIVE；parent=gallantlab/himalaya） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1267 | `flatironinstitute/dendro-old`<br>source=`flatironinstitute/dendro-old` | `repo-004711` `yarikoptic/dendro`（REPRESENTATIVE；parent=flatironinstitute/dendro-old） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1268 | `jonescompneurolab/hnn`<br>source=`jonescompneurolab/hnn` | `repo-004954` `yarikoptic/hnn`（REPRESENTATIVE；parent=jonescompneurolab/hnn） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1269 | `changwn/scfea`<br>source=`changwn/scFEA` | `repo-002634` `changwn/scFEA`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1270 | `pennsieve/pennsieve-app-2`<br>source=`Pennsieve/pennsieve-app-2` | `repo-005324` `yarikoptic/pennsieve-app`（REPRESENTATIVE；parent=Pennsieve/pennsieve-app-2） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1271 | `slideflow/slideflow`<br>source=`slideflow/slideflow` | `repo-003151` `Mr-Milk/slideflow`（REPRESENTATIVE；parent=slideflow/slideflow） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1272 | `helloworldlty/tangram_v2`<br>source=`HelloWorldLTY/Tangram_v2` | `repo-001359` `HelloWorldLTY/Tangram_v2`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1273 | `pyslurm/pyslurm`<br>source=`PySlurm/pyslurm` | `repo-005434` `yarikoptic/pyslurm`（REPRESENTATIVE；parent=PySlurm/pyslurm） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1274 | `ishaanadarsh/medstream-analytics`<br>source=`IshaanAdarsh/MedStream-Analytics` | `repo-006875` `tangxuan82/MedStream-Analytics`（REPRESENTATIVE；parent=IshaanAdarsh/MedStream-Analytics） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1275 | `klacourse/moda_gc`<br>source=`klacourse/MODA_GC` | `repo-006510` `gutendzx/MODA_GC`（REPRESENTATIVE；parent=klacourse/MODA_GC） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1276 | `psych-ds/example-datasets`<br>source=`psych-ds/example-datasets` | `repo-004796` `yarikoptic/example-datasets`（REPRESENTATIVE；parent=psych-ds/example-datasets） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1277 | `leezx/exp_protocols`<br>source=`leezx/Exp_protocols` | `repo-007192` `leezx/Exp_protocols`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1278 | `pasta-eln/pasta-eln`<br>source=`PASTA-ELN/pasta-eln` | `repo-005319` `yarikoptic/pasta-eln`（REPRESENTATIVE；parent=PASTA-ELN/pasta-eln） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1279 | `psychopy/psychopy`<br>source=`psychopy/psychopy` | `repo-002697` `erhuve/psychopy`（REPRESENTATIVE；parent=psychopy/psychopy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1280 | `ncfrey/litmatter`<br>source=`ncfrey/litmatter` | `repo-006973` `Vik-u/litmatter`（REPRESENTATIVE；parent=ncfrey/litmatter） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1281 | `hasanaldhahi/trentino_weather_climate_change`<br>source=`HasanAldhahi/Trentino_weather_climate_change` | `repo-001239` `HasanAldhahi/Trentino_weather_climate_change`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1282 | `debeshjha/resunetplusplus-with-crf-and-tta`<br>source=`DebeshJha/ResUNetPlusPlus-with-CRF-and-TTA` | `repo-006530` `gutendzx/ResUNetPlusPlus-with-CRF-and-TTA`（REPRESENTATIVE；parent=DebeshJha/ResUNetPlusPlus-with-CRF-and-TTA） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1283 | `satijalab/seurat-object`<br>source=`satijalab/seurat-object` | `repo-002379` `zskylarli/seurat-object`（REPRESENTATIVE；parent=satijalab/seurat-object） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1284 | `multiqc/multiqc`<br>source=`MultiQC/MultiQC` | `repo-004130` `vladsavelyev/MultiQC`（REPRESENTATIVE；parent=MultiQC/MultiQC） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1285 | `repronim/repromon`<br>source=`ReproNim/repromon` | `repo-005500` `yarikoptic/repromon`（REPRESENTATIVE；parent=ReproNim/repromon） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1286 | `janelia-flyem/dvid`<br>source=`janelia-flyem/dvid` | `repo-004773` `yarikoptic/dvid`（REPRESENTATIVE；parent=janelia-flyem/dvid） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1287 | `openemr/openemr-on-ecs`<br>source=`openemr/openemr-on-ecs` | `repo-006434` `chaudhariatul/host-openemr-on-aws-fargate`（REPRESENTATIVE；parent=openemr/openemr-on-ecs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1288 | `neurolearn/neurolearn-web`<br>source=`neurolearn/neurolearn-web` | `repo-005189` `yarikoptic/neurolearn-web`（REPRESENTATIVE；parent=neurolearn/neurolearn-web） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1289 | `ibm/molformer`<br>source=`IBM/molformer` | `repo-002344` `zhanxw/molformer`（REPRESENTATIVE；parent=IBM/molformer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1290 | `dcan-labs/bibsnet`<br>source=`DCAN-Labs/BIBSnet` | `repo-004527` `yarikoptic/CABINET`（REPRESENTATIVE；parent=DCAN-Labs/BIBSnet） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1291 | `neurolang/neurolang`<br>source=`NeuroLang/NeuroLang` | `repo-005188` `yarikoptic/NeuroLang`（REPRESENTATIVE；parent=NeuroLang/NeuroLang） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1292 | `teichlab/bbknn`<br>source=`Teichlab/bbknn` | `repo-006635` `sszhu/bbknn`（REPRESENTATIVE；parent=Teichlab/bbknn） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1293 | `lbm-epfl/pesto`<br>source=`LBM-EPFL/PeSTo` | `repo-006882` `tangxuan82/PeSTo`（REPRESENTATIVE；parent=LBM-EPFL/PeSTo） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1294 | `workflowscommunity/workflowscommunity.github.io`<br>source=`workflowscommunity/workflowscommunity.github.io` | `repo-005763` `yarikoptic/workflowscommunity.github.io`（REPRESENTATIVE；parent=workflowscommunity/workflowscommunity.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1295 | `datalad/datalad-dataverse`<br>source=`datalad/datalad-dataverse` | `repo-004671` `yarikoptic/datalad-dataverse`（REPRESENTATIVE；parent=datalad/datalad-dataverse） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1296 | `microsoft/x-decoder`<br>source=`microsoft/X-Decoder` | `repo-003915` `reacher-z/X-Decoder`（REPRESENTATIVE；parent=microsoft/X-Decoder） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1297 | `bbillot/synthseg`<br>source=`BBillot/SynthSeg` | `repo-005646` `yarikoptic/SynthSeg`（REPRESENTATIVE；parent=BBillot/SynthSeg） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1298 | `modelseed/modelseeddatabase`<br>source=`ModelSEED/ModelSEEDDatabase` | `repo-006980` `Vik-u/ModelSEEDDatabase`（REPRESENTATIVE；parent=ModelSEED/ModelSEEDDatabase） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1299 | `karissawhiting/oncokbr`<br>source=`karissawhiting/oncokbR` | `repo-002837` `inodb/oncokbR`（REPRESENTATIVE；parent=karissawhiting/oncokbR） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1300 | `ohif/viewers`<br>source=`OHIF/Viewers` | `repo-005736` `yarikoptic/Viewers`（REPRESENTATIVE；parent=OHIF/Viewers） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1301 | `aws-samples/aws-healthimaging-samples`<br>source=`aws-samples/aws-healthimaging-samples` | `repo-006419` `chaudhariatul/aws-healthimaging-samples`（REPRESENTATIVE；parent=aws-samples/aws-healthimaging-samples） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1302 | `emadeldeen24/attnsleep`<br>source=`emadeldeen24/AttnSleep` | `repo-006467` `gutendzx/AttnSleep`（REPRESENTATIVE；parent=emadeldeen24/AttnSleep） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1303 | `scverse/squidpy`<br>source=`scverse/squidpy` | `repo-001353` `HelloWorldLTY/squidpy`（REPRESENTATIVE；parent=scverse/squidpy） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1304 | `hed-standard/ctagger`<br>source=`hed-standard/CTagger` | `repo-004624` `yarikoptic/CTagger`（REPRESENTATIVE；parent=hed-standard/CTagger） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1305 | `hed-standard/hed-examples`<br>source=`hed-standard/hed-examples` | `repo-004938` `yarikoptic/hed-examples`（REPRESENTATIVE；parent=hed-standard/hed-examples） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1306 | `hed-standard/hed-schemas`<br>source=`hed-standard/hed-schemas` | `repo-004941` `yarikoptic/hed-schemas`（REPRESENTATIVE；parent=hed-standard/hed-schemas） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1307 | `incf-nidash/nidmresults`<br>source=`incf-nidash/nidmresults` | `repo-005212` `yarikoptic/nidmresults`（REPRESENTATIVE；parent=incf-nidash/nidmresults） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1308 | `datajoint/datajoint-tutorials`<br>source=`datajoint/datajoint-tutorials` | `repo-004663` `yarikoptic/datajoint-tutorials`（REPRESENTATIVE；parent=datajoint/datajoint-tutorials） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1309 | `grandjeanlab/incf_preclinical`<br>source=`grandjeanlab/INCF_preclinical` | `repo-004974` `yarikoptic/INCF_preclinical`（REPRESENTATIVE；parent=grandjeanlab/INCF_preclinical） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1310 | `datajoint/datajoint-docs`<br>source=`datajoint/datajoint-docs` | `repo-004661` `yarikoptic/datajoint-docs`（REPRESENTATIVE；parent=datajoint/datajoint-docs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1311 | `emadeldeen24/eval_ssl_ssc`<br>source=`emadeldeen24/eval_ssl_ssc` | `repo-006495` `gutendzx/eval_ssl_ssc`（REPRESENTATIVE；parent=emadeldeen24/eval_ssl_ssc） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1312 | `neuroinformatics-unit/datashuttle`<br>source=`neuroinformatics-unit/datashuttle` | `repo-004691` `yarikoptic/datashuttle`（REPRESENTATIVE；parent=neuroinformatics-unit/datashuttle） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1263–1312`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-030-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
