# 远程调研 Batch 032

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1363–1412**；**50** 个 family；**51** 条 bounded repository records。

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
| 分类 `DATASET_OR_BENCHMARK` | 2 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 14 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 27 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 4 |
| 标记 `ARCHIVED_OR_DISABLED` | 1 |
| 标记 `CHILD_FORK_SURFACE` | 2 |
| 标记 `FORK_LINEAGE_REQUIRED` | 45 |
| 标记 `LICENSE_UNCLEAR` | 21 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1363 | `nipype/pydra`<br>source=`nipype/pydra` | `repo-005405` `yarikoptic/pydra`（REPRESENTATIVE；parent=nipype/pydra） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1364 | `neurodesk/neurocommand`<br>source=`neurodesk/neurocommand` | `repo-005175` `yarikoptic/neurocommand`（REPRESENTATIVE；parent=neurodesk/neurocommand） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1365 | `flywheel-apps/bids-fmriprep`<br>source=`flywheel-apps/bids-fmriprep` | `repo-004462` `yarikoptic/bids-fmriprep`（REPRESENTATIVE；parent=flywheel-apps/bids-fmriprep） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1366 | `neurolibre/docs.neurolibre.org`<br>source=`neurolibre/docs.neurolibre.org` | `repo-004750` `yarikoptic/docs.neurolibre.org`（REPRESENTATIVE；parent=neurolibre/docs.neurolibre.org） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1367 | `leezx/cut-run-pipeline`<br>source=`leezx/cut-run-pipeline` | `repo-007189` `leezx/cut-run-pipeline`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1368 | `open-ephys-plugins/nwb-zarr-format`<br>source=`open-ephys-plugins/nwb-zarr-format` | `repo-005257` `yarikoptic/nwb-zarr-format`（REPRESENTATIVE；parent=open-ephys-plugins/nwb-zarr-format） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1369 | `open-ephys-plugins/nwb-format`<br>source=`open-ephys-plugins/nwb-format` | `repo-005254` `yarikoptic/nwb-format`（REPRESENTATIVE；parent=open-ephys-plugins/nwb-format） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1370 | `futianfan/clinical-trial-outcome-prediction`<br>source=`futianfan/clinical-trial-outcome-prediction` | `repo-001643` `MintaYLu/clinical-trial-outcome-prediction`（REPRESENTATIVE；parent=futianfan/clinical-trial-outcome-prediction） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1371 | `futianfan/mimosa`<br>source=`futianfan/MIMOSA` | `repo-001647` `MintaYLu/MIMOSA`（REPRESENTATIVE；parent=futianfan/MIMOSA） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1372 | `datalad/datalad.org`<br>source=`datalad/datalad.org` | `repo-004687` `yarikoptic/datalad.org`（REPRESENTATIVE；parent=datalad/datalad.org） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1373 | `ibt-fmi/samri`<br>source=`IBT-FMI/SAMRI` | `repo-005534` `yarikoptic/SAMRI`（REPRESENTATIVE；parent=IBT-FMI/SAMRI） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1374 | `vitessce/vitesscer`<br>source=`vitessce/vitessceR` | `repo-003093` `Liripo/vitessceR`（REPRESENTATIVE；parent=vitessce/vitessceR） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1375 | `psychtoolbox-3/psychtoolbox-3`<br>source=`Psychtoolbox-3/Psychtoolbox-3` | `repo-005385` `yarikoptic/Psychtoolbox-3`（REPRESENTATIVE；parent=Psychtoolbox-3/Psychtoolbox-3） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1376 | `gbook/squirrel`<br>source=`gbook/squirrel` | `repo-005622` `yarikoptic/squirrel`（REPRESENTATIVE；parent=gbook/squirrel） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1377 | `psychoinformatics-de/datalad-tabby`<br>source=`psychoinformatics-de/datalad-tabby` | `repo-004686` `yarikoptic/datalad-tabby`（REPRESENTATIVE；parent=psychoinformatics-de/datalad-tabby） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1378 | `neurolibre/inara`<br>source=`neurolibre/inara` | `repo-004972` `yarikoptic/inara`（REPRESENTATIVE；parent=neurolibre/inara） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1379 | `gbook/nidb`<br>source=`gbook/nidb` | `repo-005210` `yarikoptic/nidb`（REPRESENTATIVE；parent=gbook/nidb） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1380 | `imagingdatacommons/libdicom`<br>source=`ImagingDataCommons/libdicom` | `repo-005040` `yarikoptic/libdicom`（REPRESENTATIVE；parent=ImagingDataCommons/libdicom） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1381 | `snakemake/snakemake-workflow-catalog`<br>source=`snakemake/snakemake-workflow-catalog` | `repo-004138` `vladsavelyev/nextflow-workflow-catalog`（REPRESENTATIVE；parent=snakemake/snakemake-workflow-catalog） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1382 | `py-why/causal-learn`<br>source=`py-why/causal-learn` | `repo-004537` `yarikoptic/causal-learn`（REPRESENTATIVE；parent=py-why/causal-learn） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1383 | `neuroscout/neuroscout`<br>source=`neuroscout/neuroscout` | `repo-005191` `yarikoptic/neuroscout`（REPRESENTATIVE；parent=neuroscout/neuroscout） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1384 | `biolink/biolink-model`<br>source=`biolink/biolink-model` | `repo-000895` `andrewsu/biolink-model`（REPRESENTATIVE；parent=biolink/biolink-model）<br>`repo-004487` `yarikoptic/biolink-model`（MEMBER；parent=biolink/biolink-model） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1385 | `higlass/higlass`<br>source=`higlass/higlass` | `repo-007037` `Javkhaa/higlass`（REPRESENTATIVE；parent=higlass/higlass） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1386 | `jerryji1993/dnabert`<br>source=`jerryji1993/DNABERT` | `repo-007072` `jaybee84/DNABERT`（REPRESENTATIVE；parent=jerryji1993/DNABERT） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1387 | `juliaio/zarr.jl`<br>source=`JuliaIO/Zarr.jl` | `repo-005780` `yarikoptic/Zarr.jl`（REPRESENTATIVE；parent=JuliaIO/Zarr.jl） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1388 | `neurodesk/neurocontainers`<br>source=`neurodesk/neurocontainers` | `repo-005176` `yarikoptic/neurocontainers`（REPRESENTATIVE；parent=neurodesk/neurocontainers） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1389 | `neurodesk/neurodesktop`<br>source=`neurodesk/neurodesktop` | `repo-005183` `yarikoptic/neurodesktop`（REPRESENTATIVE；parent=neurodesk/neurodesktop） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1390 | `datajoint/datajoint-python`<br>source=`datajoint/datajoint-python` | `repo-004662` `yarikoptic/datajoint-python`（REPRESENTATIVE；parent=datajoint/datajoint-python） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1391 | `tomaroberts/nii2dcm`<br>source=`tomaroberts/nii2dcm` | `repo-005213` `yarikoptic/nii2dcm`（REPRESENTATIVE；parent=tomaroberts/nii2dcm） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1392 | `esdalmaijer/bibliobanana`<br>source=`esdalmaijer/bibliobanana` | `repo-004452` `yarikoptic/bibliobanana`（REPRESENTATIVE；parent=esdalmaijer/bibliobanana） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1393 | `karissawhiting/cbioportalr`<br>source=`karissawhiting/cbioportalR` | `repo-002769` `inodb/cbioportalR`（REPRESENTATIVE；parent=karissawhiting/cbioportalR） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1394 | `neurobagel/documentation`<br>source=`neurobagel/documentation` | `repo-004751` `yarikoptic/documentation`（REPRESENTATIVE；parent=neurobagel/documentation） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1395 | `elabftw/elabftw`<br>source=`elabftw/elabftw` | `repo-004782` `yarikoptic/elabftw`（REPRESENTATIVE；parent=elabftw/elabftw） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1396 | `berquist/chargemol`<br>source=`berquist/chargemol` | `repo-007409` `Rasic2/CM5-charge`（REPRESENTATIVE；parent=berquist/chargemol） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1397 | `neurobagel/api`<br>source=`neurobagel/api` | `repo-004396` `yarikoptic/api`（REPRESENTATIVE；parent=neurobagel/api） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1398 | `neurobagel/bagel-cli`<br>source=`neurobagel/bagel-cli` | `repo-004430` `yarikoptic/bagel-cli`（REPRESENTATIVE；parent=neurobagel/bagel-cli） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1399 | `lorenfranklab/spyglass`<br>source=`LorenFrankLab/spyglass` | `repo-005620` `yarikoptic/spyglass`（REPRESENTATIVE；parent=LorenFrankLab/spyglass） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1400 | `vladsavelyev/bedanno`<br>source=`vladsavelyev/bedanno` | `repo-004075` `vladsavelyev/bedanno`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1401 | `networkx/networkx`<br>source=`networkx/networkx` | `repo-005166` `yarikoptic/networkx`（REPRESENTATIVE；parent=networkx/networkx） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1402 | `vladsavelyev/bed_annotation`<br>source=`vladsavelyev/bed_annotation` | `repo-004074` `vladsavelyev/bed_annotation`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1403 | `ome/ome-zarr-py`<br>source=`ome/ome-zarr-py` | `repo-005268` `yarikoptic/ome-zarr-py`（REPRESENTATIVE；parent=ome/ome-zarr-py） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1404 | `cornerstonejs/cornerstone3d`<br>source=`cornerstonejs/cornerstone3D` | `repo-006128` `m-barthel/cornerstone3D-beta`（REPRESENTATIVE；parent=cornerstonejs/cornerstone3D） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1405 | `hbclab/nibetaseries`<br>source=`HBClab/NiBetaSeries` | `repo-005205` `yarikoptic/NiBetaSeries`（REPRESENTATIVE；parent=HBClab/NiBetaSeries） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1406 | `tschaffter/rstudio`<br>source=`tschaffter/rstudio` | `repo-007364` `tschaffter/rstudio`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1407 | `citation-style-language/styles`<br>source=`citation-style-language/styles` | `repo-007408` `Rasic2/citation-style-language-styles`（REPRESENTATIVE；parent=citation-style-language/styles） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1408 | `sczzz3/ehrdiff`<br>source=`sczzz3/EHRDiff` | `repo-002311` `zhanxw/ehrdiff`（REPRESENTATIVE；parent=sczzz3/EHRDiff） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1409 | `zhuyitan/ckd_progression_prediction`<br>source=`zhuyitan/CKD_Progression_Prediction` | `repo-006151` `zhuyitan/CKD_Progression_Prediction`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1410 | `neurobagel/legacy_annotation_tool`<br>source=`neurobagel/legacy_annotation_tool` | `repo-004389` `yarikoptic/annotation_tool`（REPRESENTATIVE；parent=neurobagel/legacy_annotation_tool） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1411 | `bids-standard/stats-models`<br>source=`bids-standard/stats-models` | `repo-005627` `yarikoptic/stats-models`（REPRESENTATIVE；parent=bids-standard/stats-models） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1412 | `alleninstitute/openai_tools`<br>source=`AllenInstitute/openai_tools` | `repo-007100` `jaybee84/openai_tools`（REPRESENTATIVE；parent=AllenInstitute/openai_tools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1363–1412`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-032-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
