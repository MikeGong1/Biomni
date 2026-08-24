# 远程调研 Batch 018

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **663–712**；**50** 个 family；**53** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 53 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 3 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 6 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 22 |
| 分类 `LOW_INFORMATION_RECHECK` | 8 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 7 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 33 |
| 标记 `LICENSE_UNCLEAR` | 24 |
| 标记 `MULTI_MEMBER_FAMILY` | 3 |
| 标记 `RECENT_ACTIVE` | 50 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 663 | `xiaobaben/spiced`<br>source=`xiaobaben/SPICED` | `repo-006545` `gutendzx/SPICED`（REPRESENTATIVE；parent=xiaobaben/SPICED） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 664 | `grll/mcpadapt`<br>source=`grll/mcpadapt` | `repo-001033` `Edison-A-N/mcpadapt`（REPRESENTATIVE；parent=grll/mcpadapt） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 665 | `pointcept/pointtransformerv3`<br>source=`Pointcept/PointTransformerV3` | `repo-007566` `xinwuye/UniDock-PTV3`（REPRESENTATIVE；parent=Pointcept/PointTransformerV3） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 666 | `durrantlab/binana`<br>source=`durrantlab/binana` | `repo-006132` `SongyouZhong/binana`（REPRESENTATIVE；parent=durrantlab/binana） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 667 | `ryanding26/hackaging-team-ryan`<br>source=`ryanDing26/Hackaging-team-Ryan` | `repo-001737` `ryanDing26/Hackaging-team-Ryan`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 668 | `ryanding26/aging-theories`<br>source=`ryanDing26/aging-theories` | `repo-001727` `ryanDing26/aging-theories`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 669 | `sage-bionetworks-workflows/nextflow-infra`<br>source=`Sage-Bionetworks-Workflows/nextflow-infra` | `repo-000984` `anngvu/nextflow-infra`（REPRESENTATIVE；parent=Sage-Bionetworks-Workflows/nextflow-infra）<br>`repo-007091` `jaybee84/nextflow-infra`（MEMBER；parent=Sage-Bionetworks-Workflows/nextflow-infra） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 670 | `datoviz/datoviz`<br>source=`datoviz/datoviz` | `repo-004693` `yarikoptic/datoviz`（REPRESENTATIVE；parent=datoviz/datoviz） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 671 | `tangxuan82/digitaltwin`<br>source=`tangxuan82/DigitalTwin` | `repo-006848` `tangxuan82/DigitalTwin`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 672 | `anthropics/skills`<br>source=`anthropics/skills` | `repo-007043` `Javkhaa/skills`（REPRESENTATIVE；parent=anthropics/skills） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 673 | `spikeinterface/probeinterface`<br>source=`SpikeInterface/probeinterface` | `repo-005368` `yarikoptic/probeinterface`（REPRESENTATIVE；parent=SpikeInterface/probeinterface） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 674 | `cortex-lab/phy`<br>source=`cortex-lab/phy` | `repo-005330` `yarikoptic/phy`（REPRESENTATIVE；parent=cortex-lab/phy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 675 | `sophicle/sensory`<br>source=`sophicle/sensory` | `repo-007298` `sophicle/sensory`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 676 | `hassan-asim/greedoc`<br>source=`Hassan-asim/Greedoc` | `repo-006859` `tangxuan82/Greedoc`（REPRESENTATIVE；parent=Hassan-asim/Greedoc） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 677 | `susheel/synapse-mcp`<br>source=`susheel/synapse-mcp` | `repo-000993` `anngvu/synapse-mcp`（REPRESENTATIVE；parent=susheel/synapse-mcp）<br>`repo-007129` `jaybee84/synapse-mcp`（MEMBER；parent=susheel/synapse-mcp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 678 | `rochefort-lab/fissa`<br>source=`rochefort-lab/fissa` | `repo-004824` `yarikoptic/fissa`（REPRESENTATIVE；parent=rochefort-lab/fissa） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 679 | `kohulan/decimer-image-segmentation`<br>source=`Kohulan/DECIMER-Image-Segmentation` | `repo-006136` `SongyouZhong/DECIMER-Image-Segmentation`（REPRESENTATIVE；parent=Kohulan/DECIMER-Image-Segmentation） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 680 | `deepmodeling/dpdispatcher`<br>source=`deepmodeling/dpdispatcher` | `repo-007411` `Rasic2/dpdispatcher`（REPRESENTATIVE；parent=deepmodeling/dpdispatcher） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 681 | `mosqueralopez/t1dsim_ai`<br>source=`mosqueralopez/T1DSim_AI` | `repo-006898` `tangxuan82/T1DSim_AI`（REPRESENTATIVE；parent=mosqueralopez/T1DSim_AI） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 682 | `yarikoptic/bootstrap_mriqc`<br>source=`yarikoptic/bootstrap_MRIQC` | `repo-004498` `yarikoptic/bootstrap_MRIQC`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 683 | `novonordisk-research/momentumpyclient`<br>source=`novonordisk-research/MomentumPyClient` | `repo-006985` `Vik-u/MomentumPyClient`（REPRESENTATIVE；parent=novonordisk-research/MomentumPyClient） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 684 | `hasanaldhahi/biomni_agent`<br>source=`HasanAldhahi/biomni_agent` | `repo-001097` `HasanAldhahi/biomni_agent`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 685 | `astewartau/dicompare`<br>source=`astewartau/dicompare` | `repo-004721` `yarikoptic/dicompare`（REPRESENTATIVE；parent=astewartau/dicompare） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 686 | `australian-epilepsy-project/protocol_qc`<br>source=`Australian-Epilepsy-Project/protocol_qc` | `repo-005372` `yarikoptic/protocol_qc`（REPRESENTATIVE；parent=Australian-Epilepsy-Project/protocol_qc） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 687 | `kohulan/decimer-image_transformer`<br>source=`Kohulan/DECIMER-Image_Transformer` | `repo-006137` `SongyouZhong/DECIMER-Image_Transformer`（REPRESENTATIVE；parent=Kohulan/DECIMER-Image_Transformer） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 688 | `orbliss/cheminformatics_molecule_property_project`<br>source=`Orbliss/Cheminformatics_molecule_property_project` | `repo-001592` `marcosbolanos/Cheminformatics_molecule_property_project`（REPRESENTATIVE；parent=Orbliss/Cheminformatics_molecule_property_project） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 689 | `vladsavelyev/mcp_biomni`<br>source=`vladsavelyev/mcp_biomni` | `repo-004127` `vladsavelyev/mcp_biomni`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 690 | `pku-yuangroup/prollama`<br>source=`PKU-YuanGroup/ProLLaMA` | `repo-005967` `dabulseco/ProLLaMA`（REPRESENTATIVE；parent=PKU-YuanGroup/ProLLaMA）<br>`repo-006883` `tangxuan82/ProLLaMA`（MEMBER；parent=PKU-YuanGroup/ProLLaMA） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 691 | `leezx/trident`<br>source=`leezx/TRIDENT` | `repo-007208` `leezx/TRIDENT`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | `RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 692 | `halfpipe/halfpipe`<br>source=`HALFpipe/HALFpipe` | `repo-004920` `yarikoptic/HALFpipe`（REPRESENTATIVE；parent=HALFpipe/HALFpipe） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 693 | `pkr2180/periodontal_digital-twin`<br>source=`Pkr2180/PERIODONTAL_DIGITAL-TWIN` | `repo-006881` `tangxuan82/PERIODONTAL_DIGITAL-TWIN`（REPRESENTATIVE；parent=Pkr2180/PERIODONTAL_DIGITAL-TWIN） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 694 | `harrydirk41/protdyn`<br>source=`Harrydirk41/ProTDyn` | `repo-002732` `Harrydirk41/ProTDyn`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 695 | `nigmat-future/gastric-cancer-scrna-seq-analysis-pipeline---gse163558`<br>source=`Nigmat-future/Gastric-Cancer-scRNA-seq-Analysis-Pipeline---GSE163558` | `repo-003183` `Nigmat-future/Gastric-Cancer-scRNA-seq-Analysis-Pipeline---GSE163558`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 696 | `vik-u/synbiokb-agent`<br>source=`Vik-u/SynBioKB-Agent` | `repo-007011` `Vik-u/SynBioKB-Agent`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 697 | `nvidia-bionemo/la-proteina`<br>source=`NVIDIA-BioNeMo/la-proteina` | `repo-006971` `Vik-u/la-proteina`（REPRESENTATIVE；parent=NVIDIA-BioNeMo/la-proteina） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 698 | `kwskws1998/jspsych-experiment`<br>source=`kwskws1998/jspsych-experiment` | `repo-004249` `kwskws1998/jspsych-experiment`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 699 | `mims-harvard/curebench`<br>source=`mims-harvard/CUREBench` | `repo-006311` `Ali-Maq/CUREBench`（REPRESENTATIVE；parent=mims-harvard/CUREBench） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 700 | `broadinstitute/str-analysis`<br>source=`broadinstitute/str-analysis` | `repo-006119` `leizhou69/str-analysis`（REPRESENTATIVE；parent=broadinstitute/str-analysis） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 701 | `th86/pymutualinformation`<br>source=`th86/pymutualinformation` | `repo-002195` `th86/pymutualinformation`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 702 | `nigmat-future/cellhop`<br>source=`Nigmat-future/cellhop` | `repo-003178` `Nigmat-future/cellhop`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 703 | `mickaelleclercq/bioagent`<br>source=`mickaelleclercq/bioAgent` | `repo-001630` `mickaelleclercq/bioAgent`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 704 | `nigmat-future/rverflow`<br>source=`Nigmat-future/rverflow` | `repo-003200` `Nigmat-future/rverflow`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 705 | `reusabledata/reusabledata`<br>source=`reusabledata/reusabledata` | `repo-000946` `andrewsu/reusabledata`（REPRESENTATIVE；parent=reusabledata/reusabledata） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 706 | `neuroboros/neuroboros`<br>source=`neuroboros/neuroboros` | `repo-005172` `yarikoptic/neuroboros`（REPRESENTATIVE；parent=neuroboros/neuroboros） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 707 | `esd-univr/from_scratch_to_twin`<br>source=`esd-univr/from_scratch_to_twin` | `repo-006856` `tangxuan82/from_scratch_to_twin`（REPRESENTATIVE；parent=esd-univr/from_scratch_to_twin） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 708 | `intertwin-eu/itwinai`<br>source=`interTwin-eu/itwinai` | `repo-006868` `tangxuan82/itwinai`（REPRESENTATIVE；parent=interTwin-eu/itwinai） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 709 | `th86/awesome_bioinfo`<br>source=`th86/awesome_bioinfo` | `repo-002145` `th86/awesome_bioinfo`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 710 | `open-retina/open-retina`<br>source=`open-retina/open-retina` | `repo-005276` `yarikoptic/open-retina`（REPRESENTATIVE；parent=open-retina/open-retina） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 711 | `orbliss/virtual-cell-challenge`<br>source=`Orbliss/Virtual-Cell-Challenge` | `repo-001626` `marcosbolanos/Virtual-Cell-Challenge`（REPRESENTATIVE；parent=Orbliss/Virtual-Cell-Challenge） | `EMPTY_OR_MINIMAL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL`、`RECENT_ACTIVE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 712 | `novasky-ai/skyrl`<br>source=`NovaSky-AI/SkyRL` | `repo-001760` `RyanLi1028/Biomni-SkyRL`（REPRESENTATIVE；parent=NovaSky-AI/SkyRL） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `663–712`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-018-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
