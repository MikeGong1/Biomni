# 远程调研 Batch 033

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1413–1462**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 3 |
| 分类 `DATASET_OR_BENCHMARK` | 4 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 21 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 12 |
| 分类 `LOW_INFORMATION_RECHECK` | 7 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 3 |
| 标记 `CHILD_FORK_SURFACE` | 8 |
| 标记 `FORK_LINEAGE_REQUIRED` | 41 |
| 标记 `LICENSE_UNCLEAR` | 22 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1413 | `expfactory/expfactory-experiments`<br>source=`expfactory/expfactory-experiments` | `repo-004807` `yarikoptic/expfactory-experiments`（REPRESENTATIVE；parent=expfactory/expfactory-experiments） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1414 | `expfactory/expfactory`<br>source=`expfactory/expfactory` | `repo-004806` `yarikoptic/expfactory`（REPRESENTATIVE；parent=expfactory/expfactory） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1415 | `expfactory/experiments`<br>source=`expfactory/experiments` | `repo-004805` `yarikoptic/experiments`（REPRESENTATIVE；parent=expfactory/experiments） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1416 | `tuln128/epilegosdnn`<br>source=`tuln128/epiLegosDNN` | `repo-002214` `tuln128/epiLegosDNN`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1417 | `anngvu/sage-skills`<br>source=`anngvu/sage-skills` | `repo-000990` `anngvu/sage-skills`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1418 | `genoml/genoml2`<br>source=`GenoML/genoml2` | `repo-003104` `mkoretsky1/genoml2`（REPRESENTATIVE；parent=GenoML/genoml2） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1419 | `ibt-fmi/cosplay`<br>source=`IBT-FMI/COSplay` | `repo-004611` `yarikoptic/COSplay`（REPRESENTATIVE；parent=IBT-FMI/COSplay） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1420 | `brainhack-princeton/handbook`<br>source=`brainhack-princeton/handbook` | `repo-004922` `yarikoptic/handbook`（REPRESENTATIVE；parent=brainhack-princeton/handbook） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1421 | `brainhack-princeton/handbook-code`<br>source=`brainhack-princeton/handbook-code` | `repo-004924` `yarikoptic/handbook-code`（REPRESENTATIVE；parent=brainhack-princeton/handbook-code） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1422 | `ancplaboldenburg/ancp-bids`<br>source=`ANCPLabOldenburg/ancp-bids` | `repo-004384` `yarikoptic/ancp-bids`（REPRESENTATIVE；parent=ANCPLabOldenburg/ancp-bids） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1423 | `bids-standard/pybids`<br>source=`bids-standard/pybids` | `repo-005397` `yarikoptic/pybids`（REPRESENTATIVE；parent=bids-standard/pybids） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1424 | `balbasty/dandi-io`<br>source=`balbasty/dandi-io` | `repo-004637` `yarikoptic/dandi-io`（REPRESENTATIVE；parent=balbasty/dandi-io） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1425 | `thelabbingproject/pylabber`<br>source=`TheLabbingProject/pylabber` | `repo-005415` `yarikoptic/pylabber`（REPRESENTATIVE；parent=TheLabbingProject/pylabber） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1426 | `afni/afni_ci_test_data`<br>source=`afni/afni_ci_test_data` | `repo-004361` `yarikoptic/afni_ci_test_data`（REPRESENTATIVE；parent=afni/afni_ci_test_data） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1427 | `sage-bionetworks/tumor-deconvolution-challenge-workflow`<br>source=`Sage-Bionetworks/Tumor-Deconvolution-Challenge-Workflow` | `repo-007141` `jaybee84/Tumor-Deconvolution-Challenge-Workflow`（REPRESENTATIVE；parent=Sage-Bionetworks/Tumor-Deconvolution-Challenge-Workflow） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1428 | `leezx/bioinfo-pipelines`<br>source=`leezx/bioinfo-pipelines` | `repo-007177` `leezx/bioinfo-pipelines`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1429 | `mariospapasofokli/databrary`<br>source=`MariosPapasofokli/databrary` | `repo-004658` `yarikoptic/databrary`（REPRESENTATIVE；parent=MariosPapasofokli/databrary） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1430 | `michiyasunaga/qagnn`<br>source=`michiyasunaga/qagnn` | `repo-000853` `michiyasunaga/qagnn`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1431 | `ninglab/ctkg`<br>source=`ninglab/CTKG` | `repo-006837` `tangxuan82/CTKG`（REPRESENTATIVE；parent=ninglab/CTKG） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1432 | `simula-vias/yolo4apnea`<br>source=`simula-vias/Yolo4Apnea` | `repo-006563` `gutendzx/Yolo4Apnea`（REPRESENTATIVE；parent=simula-vias/Yolo4Apnea） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1433 | `dipy/dipy`<br>source=`dipy/dipy` | `repo-004726` `yarikoptic/dipy`（REPRESENTATIVE；parent=dipy/dipy）<br>`repo-007234` `manu-tej/dipy`（MEMBER；parent=dipy/dipy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`CHILD_FORK_SURFACE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1434 | `aarhus-psychiatry-research/timeseriesflattener`<br>source=`Aarhus-Psychiatry-Research/timeseriesflattener` | `repo-005692` `yarikoptic/timeseriesflattener`（REPRESENTATIVE；parent=Aarhus-Psychiatry-Research/timeseriesflattener） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1435 | `conda-forge/datalad-container-feedstock`<br>source=`conda-forge/datalad-container-feedstock` | `repo-004668` `yarikoptic/datalad-container-feedstock`（REPRESENTATIVE；parent=conda-forge/datalad-container-feedstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1436 | `fairdataihub/soda-for-sparc`<br>source=`fairdataihub/SODA-for-SPARC` | `repo-005599` `yarikoptic/SODA-for-SPARC`（REPRESENTATIVE；parent=fairdataihub/SODA-for-SPARC） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1437 | `changwn/bc-crc`<br>source=`changwn/BC-CRC` | `repo-002575` `changwn/BC-CRC`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1438 | `open-minds-lab/mrdataset`<br>source=`Open-Minds-Lab/MRdataset` | `repo-005131` `yarikoptic/MRdataset`（REPRESENTATIVE；parent=Open-Minds-Lab/MRdataset） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1439 | `open-minds-lab/mrqa`<br>source=`Open-Minds-Lab/mrQA` | `repo-005138` `yarikoptic/mrQA`（REPRESENTATIVE；parent=Open-Minds-Lab/mrQA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1440 | `brainlife/ezbids`<br>source=`brainlife/ezbids` | `repo-004810` `yarikoptic/ezbids`（REPRESENTATIVE；parent=brainlife/ezbids） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1441 | `brainlife/warehouse`<br>source=`brainlife/warehouse` | `repo-005748` `yarikoptic/warehouse`（REPRESENTATIVE；parent=brainlife/warehouse） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1442 | `jaybee84/ml-in-rd`<br>source=`jaybee84/ml-in-rd` | `repo-007090` `jaybee84/ml-in-rd`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1443 | `rly/ndx-events`<br>source=`rly/ndx-events` | `repo-005159` `yarikoptic/ndx-events`（REPRESENTATIVE；parent=rly/ndx-events） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1444 | `microsoft/biogpt`<br>source=`microsoft/BioGPT` | `repo-007054` `jaybee84/BioGPT`（REPRESENTATIVE；parent=microsoft/BioGPT） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1445 | `cvmfs/cvmfs`<br>source=`cvmfs/cvmfs` | `repo-004627` `yarikoptic/cvmfs`（REPRESENTATIVE；parent=cvmfs/cvmfs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1446 | `nipreps/niworkflows`<br>source=`nipreps/niworkflows` | `repo-005233` `yarikoptic/niworkflows`（REPRESENTATIVE；parent=nipreps/niworkflows） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1447 | `catalystneuro/neuroconv`<br>source=`catalystneuro/neuroconv` | `repo-005177` `yarikoptic/neuroconv`（REPRESENTATIVE；parent=catalystneuro/neuroconv） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1448 | `neurodatawithoutborders/nwb-schema`<br>source=`NeurodataWithoutBorders/nwb-schema` | `repo-005256` `yarikoptic/nwb-schema`（REPRESENTATIVE；parent=NeurodataWithoutBorders/nwb-schema） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1449 | `garrettmflynn/webnwb`<br>source=`garrettmflynn/webnwb` | `repo-005756` `yarikoptic/webnwb`（REPRESENTATIVE；parent=garrettmflynn/webnwb） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1450 | `cbinyu/bidsphysio`<br>source=`cbinyu/bidsphysio` | `repo-004484` `yarikoptic/bidsphysio`（REPRESENTATIVE；parent=cbinyu/bidsphysio） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1451 | `ccsb-scripps/autodock-vina`<br>source=`ccsb-scripps/AutoDock-Vina` | `repo-007145` `KSUN63/AutoDock-Vina`（REPRESENTATIVE；parent=ccsb-scripps/AutoDock-Vina） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1452 | `leezx/scgrn`<br>source=`leezx/scGRN` | `repo-007202` `leezx/scGRN`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1453 | `helloworldlty/awgan`<br>source=`HelloWorldLTY/AWGAN` | `repo-001256` `HelloWorldLTY/AWGAN`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | 无额外标记 | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1454 | `drorlab/gvp-pytorch`<br>source=`drorlab/gvp-pytorch` | `repo-007155` `KSUN63/gvp-pytorch`（REPRESENTATIVE；parent=drorlab/gvp-pytorch） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1455 | `leezx/consurf-standalone`<br>source=`leezx/ConSurf-StandAlone` | `repo-007185` `leezx/ConSurf-StandAlone`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1456 | `lorenmt/auto-lambda`<br>source=`lorenmt/auto-lambda` | `repo-006938` `Vik-u/auto-lambda`（REPRESENTATIVE；parent=lorenmt/auto-lambda） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1457 | `physiopy/phys2bids`<br>source=`physiopy/phys2bids` | `repo-005331` `yarikoptic/phys2bids`（REPRESENTATIVE；parent=physiopy/phys2bids） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1458 | `nipy/nipy`<br>source=`nipy/nipy` | `repo-005224` `yarikoptic/nipy`（REPRESENTATIVE；parent=nipy/nipy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`CHILD_FORK_SURFACE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1459 | `satijalab/sctransform`<br>source=`satijalab/sctransform` | `repo-001346` `HelloWorldLTY/sctransform`（REPRESENTATIVE；parent=satijalab/sctransform） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1460 | `benmaier/netwulf`<br>source=`benmaier/netwulf` | `repo-005167` `yarikoptic/netwulf`（REPRESENTATIVE；parent=benmaier/netwulf） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1461 | `hamidniknazar/interpretable-sleep-scoring`<br>source=`hamidniknazar/Interpretable-sleep-scoring` | `repo-006503` `gutendzx/Interpretable-sleep-scoring`（REPRESENTATIVE；parent=hamidniknazar/Interpretable-sleep-scoring） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1462 | `thechymera/repsep`<br>source=`TheChymera/RepSeP` | `repo-005506` `yarikoptic/RepSeP`（REPRESENTATIVE；parent=TheChymera/RepSeP） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1413–1462`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-033-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
