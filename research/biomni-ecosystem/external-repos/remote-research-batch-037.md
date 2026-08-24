# 远程调研 Batch 037

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1613–1662**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 2 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 1 |
| 分类 `DATASET_OR_BENCHMARK` | 1 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 13 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 13 |
| 分类 `LOW_INFORMATION_RECHECK` | 6 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 13 |
| 标记 `ARCHIVED_OR_DISABLED` | 2 |
| 标记 `CHILD_FORK_SURFACE` | 11 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 33 |
| 标记 `LICENSE_UNCLEAR` | 22 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1613 | `leezx/varianttogene`<br>source=`leezx/VariantToGene` | `repo-007210` `leezx/VariantToGene`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1614 | `repronim/reproseed`<br>source=`ReproNim/reproseed` | `repo-005505` `yarikoptic/reproseed`（REPRESENTATIVE；parent=ReproNim/reproseed） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1615 | `brainhackorg/brainhack_jupyter_book`<br>source=`brainhackorg/brainhack_jupyter_book` | `repo-004506` `yarikoptic/brainhack_jupyter_book`（REPRESENTATIVE；parent=brainhackorg/brainhack_jupyter_book） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1616 | `nlpsandbox/nlpsandbox-schemas`<br>source=`nlpsandbox/nlpsandbox-schemas` | `repo-007346` `tschaffter/nlpsandbox-schemas`（REPRESENTATIVE；parent=nlpsandbox/nlpsandbox-schemas） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1617 | `r3fang/snapatac`<br>source=`r3fang/SnapATAC` | `repo-002639` `changwn/SnapATAC`（REPRESENTATIVE；parent=r3fang/SnapATAC） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1618 | `nf-osi/research`<br>source=`nf-osi/research` | `repo-007111` `jaybee84/research`（REPRESENTATIVE；parent=nf-osi/research） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1619 | `zethson/guide-seq-container`<br>source=`Zethson/guide-seq-container` | `repo-002279` `Zethson/guide-seq-container`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1620 | `datalad/metadata-model`<br>source=`datalad/metadata-model` | `repo-005094` `yarikoptic/metadata-model`（REPRESENTATIVE；parent=datalad/metadata-model） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1621 | `borgwardtlab/mgp-tcn`<br>source=`BorgwardtLab/mgp-tcn` | `repo-001701` `Pidem/mgp-tcn`（REPRESENTATIVE；parent=BorgwardtLab/mgp-tcn） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1622 | `spine-generic/data-multi-subject`<br>source=`spine-generic/data-multi-subject` | `repo-004652` `yarikoptic/data-multi-subject`（REPRESENTATIVE；parent=spine-generic/data-multi-subject） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1623 | `cri-iatlas/iatlas.api.client`<br>source=`CRI-iAtlas/iatlas.api.client` | `repo-007083` `jaybee84/iatlas.api.client`（REPRESENTATIVE；parent=CRI-iAtlas/iatlas.api.client） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1624 | `repronim/testkraken`<br>source=`ReproNim/testkraken` | `repo-005682` `yarikoptic/testkraken`（REPRESENTATIVE；parent=ReproNim/testkraken） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1625 | `sbu-bmi/u24_lymphocyte`<br>source=`SBU-BMI/u24_lymphocyte` | `repo-006906` `tangxuan82/u24_lymphocyte`（REPRESENTATIVE；parent=SBU-BMI/u24_lymphocyte） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1626 | `vik-u/enzymepromiscuityclassification`<br>source=`Vik-u/EnzymePromiscuityClassification` | `repo-006959` `Vik-u/EnzymePromiscuityClassification`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL`、`CHILD_FORK_SURFACE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 1627 | `jiwoongbio/metaprism`<br>source=`jiwoongbio/MetaPrism` | `repo-002339` `zhanxw/MetaPrism`（REPRESENTATIVE；parent=jiwoongbio/MetaPrism） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1628 | `shuangj00/bayessmiles`<br>source=`shuangj00/BayesSMILES` | `repo-002295` `zhanxw/BayesSMILES`（REPRESENTATIVE；parent=shuangj00/BayesSMILES） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1629 | `zhanxw/bayessmiles_web`<br>source=`zhanxw/BayesSMILES_web` | `repo-002296` `zhanxw/BayesSMILES_web`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1630 | `astropy/astropy`<br>source=`astropy/astropy` | `repo-005999` `DevinDeSilva/astropy`（REPRESENTATIVE；parent=astropy/astropy） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1631 | `sigven/cacao`<br>source=`sigven/cacao` | `repo-004080` `vladsavelyev/cacao`（REPRESENTATIVE；parent=sigven/cacao） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1632 | `vladsavelyev/oviraptor`<br>source=`vladsavelyev/oviraptor` | `repo-004141` `vladsavelyev/oviraptor`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1633 | `catalystneuro/roiextractors`<br>source=`catalystneuro/roiextractors` | `repo-005520` `yarikoptic/roiextractors`（REPRESENTATIVE；parent=catalystneuro/roiextractors） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1634 | `vladsavelyev/ngs_utils`<br>source=`vladsavelyev/NGS_Utils` | `repo-004140` `vladsavelyev/NGS_Utils`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1635 | `zhanxw/mb-gan`<br>source=`zhanxw/MB-GAN` | `repo-002333` `zhanxw/MB-GAN`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1636 | `zethson/igem_tuebingen_website`<br>source=`Zethson/igem_tuebingen_website` | `repo-002280` `Zethson/igem_tuebingen_website`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1637 | `scverse/cellrank`<br>source=`scverse/cellrank` | `repo-002583` `changwn/cellrank`（REPRESENTATIVE；parent=scverse/cellrank） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1638 | `kexinhuang12345/moldesigner-public`<br>source=`kexinhuang12345/MolDesigner-Public` | `repo-001507` `kexinhuang12345/MolDesigner-Public`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1639 | `zexuansun/dtf-drug-synergy`<br>source=`ZexuanSun/DTF-Drug-Synergy` | `repo-002595` `changwn/DTF-Drug-Synergy`（REPRESENTATIVE；parent=ZexuanSun/DTF-Drug-Synergy） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1640 | `snap-stanford/mars`<br>source=`snap-stanford/mars` | `repo-002612` `changwn/mars`（REPRESENTATIVE；parent=snap-stanford/mars） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1641 | `ncihtan/hsim`<br>source=`ncihtan/hsim` | `repo-002806` `inodb/hsim`（REPRESENTATIVE；parent=ncihtan/hsim） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1642 | `drgmk/pandeia-disks`<br>source=`drgmk/pandeia-disks` | `repo-006785` `drgmk/pandeia-disks`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1643 | `hisashin/ninjapcr`<br>source=`hisashin/NinjaPCR` | `repo-007280` `NKalavros/NinjaPCR`（REPRESENTATIVE；parent=hisashin/NinjaPCR） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1644 | `kexinhuang12345/caster`<br>source=`kexinhuang12345/CASTER` | `repo-001483` `kexinhuang12345/CASTER`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1645 | `kexinhuang12345/scgnn`<br>source=`kexinhuang12345/scGNN` | `repo-001516` `kexinhuang12345/scGNN`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | 无额外标记 | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1646 | `sigven/cpsr`<br>source=`sigven/cpsr` | `repo-004090` `vladsavelyev/cpsr`（REPRESENTATIVE；parent=sigven/cpsr） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1647 | `sigven/pcgr`<br>source=`sigven/pcgr` | `repo-004142` `vladsavelyev/pcgr`（REPRESENTATIVE；parent=sigven/pcgr） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1648 | `nf-osi/nf_data_curator`<br>source=`nf-osi/NF_data_curator` | `repo-007096` `jaybee84/NF_data_curator`（REPRESENTATIVE；parent=nf-osi/NF_data_curator） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1649 | `wjawaid/enrichr`<br>source=`wjawaid/enrichR` | `repo-002599` `changwn/enrichR`（REPRESENTATIVE；parent=wjawaid/enrichR） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1650 | `leezx/moduleselection`<br>source=`leezx/ModuleSelection` | `repo-007199` `leezx/ModuleSelection`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1651 | `sage-bionetworks/synapsepythonclient`<br>source=`Sage-Bionetworks/synapsePythonClient` | `repo-007375` `tschaffter/synapsePythonClient`（REPRESENTATIVE；parent=Sage-Bionetworks/synapsePythonClient） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1652 | `papenfusslab/gridss`<br>source=`PapenfussLab/gridss` | `repo-004107` `vladsavelyev/gridss`（REPRESENTATIVE；parent=PapenfussLab/gridss） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1653 | `diogocamacho/druid`<br>source=`diogocamacho/druid` | `repo-007075` `jaybee84/druid`（REPRESENTATIVE；parent=diogocamacho/druid） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1654 | `mgi-tech-bioinformatics/stlfr_v1.3`<br>source=`MGI-tech-bioinformatics/stLFR_V1.3` | `repo-007225` `lishengting/stLFR_V1.3`（REPRESENTATIVE；parent=MGI-tech-bioinformatics/stLFR_V1.3） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1655 | `broadinstitute/seqr`<br>source=`broadinstitute/seqr` | `repo-004155` `vladsavelyev/seqr`（REPRESENTATIVE；parent=broadinstitute/seqr） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1656 | `broadinstitute/gnomad-browser`<br>source=`broadinstitute/gnomad-browser` | `repo-004103` `vladsavelyev/gnomad-browser`（REPRESENTATIVE；parent=broadinstitute/gnomad-browser） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1657 | `vladsavelyev/reference_data`<br>source=`vladsavelyev/reference_data` | `repo-004148` `vladsavelyev/reference_data`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1658 | `leezx/ti`<br>source=`leezx/TI` | `repo-007206` `leezx/TI`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1659 | `explorerwjy/braindisorders`<br>source=`explorerwjy/BrainDisorders` | `repo-006047` `explorerwjy/BrainDisorders`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1660 | `sage-bionetworks/jhu-biobank`<br>source=`Sage-Bionetworks/JHU-biobank` | `repo-007084` `jaybee84/JHU-biobank`（REPRESENTATIVE；parent=Sage-Bionetworks/JHU-biobank） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1661 | `kexinhuang12345/drugdataresource`<br>source=`kexinhuang12345/DrugDataResource` | `repo-001496` `kexinhuang12345/DrugDataResource`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `CHILD_FORK_SURFACE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1662 | `nidm-terms/terms`<br>source=`NIDM-Terms/terms` | `repo-005656` `yarikoptic/terms`（REPRESENTATIVE；parent=NIDM-Terms/terms） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1613–1662`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-037-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
