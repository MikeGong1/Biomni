# 远程调研 Batch 039

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1713–1762**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 1 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 3 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 15 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 15 |
| 分类 `LOW_INFORMATION_RECHECK` | 7 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 5 |
| 标记 `ARCHIVED_OR_DISABLED` | 1 |
| 标记 `CHILD_FORK_SURFACE` | 2 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 39 |
| 标记 `LICENSE_UNCLEAR` | 31 |
| 标记 `RELEASE_SURFACE` | 2 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1713 | `cssegisanddata/covid-19`<br>source=`CSSEGISandData/COVID-19` | `repo-007513` `hannes-brt/COVID-19`（REPRESENTATIVE；parent=CSSEGISandData/COVID-19） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1714 | `shahcompbio/mira-graphql`<br>source=`shahcompbio/mira-graphql` | `repo-002827` `inodb/mira-graphql`（REPRESENTATIVE；parent=shahcompbio/mira-graphql） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1715 | `shahcompbio/mira-react`<br>source=`shahcompbio/mira-react` | `repo-002828` `inodb/mira-react`（REPRESENTATIVE；parent=shahcompbio/mira-react） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1716 | `shahcompbio/es-loaders`<br>source=`shahcompbio/es-loaders` | `repo-002790` `inodb/es-loaders`（REPRESENTATIVE；parent=shahcompbio/es-loaders） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1717 | `kieranrcampbell/r-workshop-march-2019`<br>source=`kieranrcampbell/r-workshop-march-2019` | `repo-002848` `inodb/r-workshop-march-2019`（REPRESENTATIVE；parent=kieranrcampbell/r-workshop-march-2019） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1718 | `ieee8023/covid-chestxray-dataset`<br>source=`ieee8023/covid-chestxray-dataset` | `repo-007063` `jaybee84/covid-chestxray-dataset`（REPRESENTATIVE；parent=ieee8023/covid-chestxray-dataset） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1719 | `yulab-smu/microbiotaprocess`<br>source=`YuLab-SMU/MicrobiotaProcess` | `repo-002343` `zhanxw/MicrobiotaProcess`（REPRESENTATIVE；parent=YuLab-SMU/MicrobiotaProcess） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1720 | `pschwllr/moleculartransformer`<br>source=`pschwllr/MolecularTransformer` | `repo-006981` `Vik-u/MolecularTransformer`（REPRESENTATIVE；parent=pschwllr/MolecularTransformer） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1721 | `manubot/rootstock`<br>source=`manubot/rootstock` | `repo-007114` `jaybee84/rootstock`（REPRESENTATIVE；parent=manubot/rootstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1722 | `dandi/dandi-about`<br>source=`dandi/dandi-about` | `repo-004638` `yarikoptic/dandi.github.io`（REPRESENTATIVE；parent=dandi/dandi-about） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1723 | `inodb/revmut`<br>source=`inodb/revmut` | `repo-002852` `inodb/revmut`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1724 | `shahcompbio/spectrum-viz-website`<br>source=`shahcompbio/spectrum-viz-website` | `repo-002863` `inodb/spectrum-viz-website`（REPRESENTATIVE；parent=shahcompbio/spectrum-viz-website） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1725 | `irrationone/cellassign`<br>source=`Irrationone/cellassign` | `repo-002772` `inodb/cellassign`（REPRESENTATIVE；parent=Irrationone/cellassign） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1726 | `jayurbain/ctsi-mcw-deid`<br>source=`jayurbain/ctsi-mcw-deid` | `repo-007312` `tschaffter/ctsi-mcw-deid`（REPRESENTATIVE；parent=jayurbain/ctsi-mcw-deid） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1727 | `alleninstitute/allensdk`<br>source=`AllenInstitute/AllenSDK` | `repo-004377` `yarikoptic/AllenSDK`（REPRESENTATIVE；parent=AllenInstitute/AllenSDK） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1728 | `isb-cgc/readthedocs`<br>source=`isb-cgc/readthedocs` | `repo-002851` `inodb/readthedocs`（REPRESENTATIVE；parent=isb-cgc/readthedocs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1729 | `sun-lab/scrnaseq_pipelines`<br>source=`Sun-lab/scRNAseq_pipelines` | `repo-002636` `changwn/scRNAseq_pipelines`（REPRESENTATIVE；parent=Sun-lab/scRNAseq_pipelines） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1730 | `javkhaa/rna_seq_analysis`<br>source=`Javkhaa/rna_seq_analysis` | `repo-007041` `Javkhaa/rna_seq_analysis`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1731 | `nygenome/conpair`<br>source=`nygenome/Conpair` | `repo-004089` `vladsavelyev/Conpair`（REPRESENTATIVE；parent=nygenome/Conpair） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1732 | `nf-osi/kairos`<br>source=`nf-osi/kairos` | `repo-007085` `jaybee84/kairos`（REPRESENTATIVE；parent=nf-osi/kairos） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1733 | `jefworks/mudan`<br>source=`JEFworks/MUDAN` | `repo-007278` `NKalavros/MUDAN`（REPRESENTATIVE；parent=JEFworks/MUDAN） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1734 | `servicenow/highres-net`<br>source=`ServiceNow/HighRes-net` | `repo-001414` `jucor/HighRes-net`（REPRESENTATIVE；parent=ServiceNow/HighRes-net） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1735 | `datalad-datasets/human-connectome-project-openaccess`<br>source=`datalad-datasets/human-connectome-project-openaccess` | `repo-004962` `yarikoptic/human-connectome-project-openaccess`（REPRESENTATIVE；parent=datalad-datasets/human-connectome-project-openaccess） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1736 | `kexinhuang12345/drug-bert`<br>source=`kexinhuang12345/drug-bert` | `repo-001495` `kexinhuang12345/drug-bert`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 1737 | `flyyuan/chinese-medical-qa-data`<br>source=`flyyuan/Chinese-Medical-QA-Data` | `repo-002584` `changwn/Chinese-Medical-QA-Data`（REPRESENTATIVE；parent=flyyuan/Chinese-Medical-QA-Data） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1738 | `conda-forge/pynwb-feedstock`<br>source=`conda-forge/pynwb-feedstock` | `repo-005426` `yarikoptic/pynwb-feedstock`（REPRESENTATIVE；parent=conda-forge/pynwb-feedstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1739 | `vladsavelyev/clearup`<br>source=`vladsavelyev/ClearUp` | `repo-004084` `vladsavelyev/ClearUp`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1740 | `jaybee84/nf_landscapepaper_2019-1`<br>source=`jaybee84/NF_LandscapePaper_2019-1` | `repo-007097` `jaybee84/NF_LandscapePaper_2019-1`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1741 | `midnighter/brenda-parser`<br>source=`Midnighter/BRENDA-Parser` | `repo-006945` `Vik-u/BRENDA-Parser`（REPRESENTATIVE；parent=Midnighter/BRENDA-Parser） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1742 | `mareesat/gwa_tutorial`<br>source=`MareesAT/GWA_tutorial` | `repo-007196` `leezx/GWA_tutorial`（REPRESENTATIVE；parent=MareesAT/GWA_tutorial） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1743 | `zethson/mhcboost`<br>source=`Zethson/MHCBoost` | `repo-002282` `Zethson/MHCBoost`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1744 | `jiahuei/report-nips-style`<br>source=`jiahuei/report-nips-style` | `repo-006355` `Ali-Maq/report-nips-style`（REPRESENTATIVE；parent=jiahuei/report-nips-style） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1745 | `mne-tools/mne-bids-pipeline`<br>source=`mne-tools/mne-bids-pipeline` | `repo-005115` `yarikoptic/mne-study-template`（REPRESENTATIVE；parent=mne-tools/mne-bids-pipeline） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1746 | `gatk-workflows/gatk4-jupyter-notebook-tutorials`<br>source=`gatk-workflows/gatk4-jupyter-notebook-tutorials` | `repo-007194` `leezx/gatk4-jupyter-notebook-tutorials`（REPRESENTATIVE；parent=gatk-workflows/gatk4-jupyter-notebook-tutorials） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1747 | `manu-tej/fish_counter`<br>source=`manu-tej/Fish_counter` | `repo-007240` `manu-tej/Fish_counter`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1748 | `sage-bionetworks/synapse-repository-services`<br>source=`Sage-Bionetworks/Synapse-Repository-Services` | `repo-007373` `tschaffter/Synapse-Repository-Services`（REPRESENTATIVE；parent=Sage-Bionetworks/Synapse-Repository-Services） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1749 | `encode-dcc/atac-seq-pipeline`<br>source=`ENCODE-DCC/atac-seq-pipeline` | `repo-007175` `leezx/atac-seq-pipeline`（REPRESENTATIVE；parent=ENCODE-DCC/atac-seq-pipeline） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1750 | `encode-dcc/chip-seq-pipeline2`<br>source=`ENCODE-DCC/chip-seq-pipeline2` | `repo-007180` `leezx/chip-seq-pipeline2`（REPRESENTATIVE；parent=ENCODE-DCC/chip-seq-pipeline2） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1751 | `repronim/reproin`<br>source=`ReproNim/reproin` | `repo-005497` `yarikoptic/reproin`（REPRESENTATIVE；parent=ReproNim/reproin） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1752 | `flatironinstitute/spikeforest2`<br>source=`flatironinstitute/spikeforest2` | `repo-005615` `yarikoptic/spikeforest2`（REPRESENTATIVE；parent=flatironinstitute/spikeforest2） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1753 | `cbioportal/clinical-timeline`<br>source=`cBioPortal/clinical-timeline` | `repo-002775` `inodb/clinical-timeline`（REPRESENTATIVE；parent=cBioPortal/clinical-timeline） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1754 | `spikeinterface/spikeinterface`<br>source=`SpikeInterface/spikeinterface` | `repo-005616` `yarikoptic/spikeinterface`（REPRESENTATIVE；parent=SpikeInterface/spikeinterface） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1755 | `explorerwjy/spark_genomics`<br>source=`explorerwjy/spark_genomics` | `repo-006073` `explorerwjy/spark_genomics`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | 无额外标记 | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1756 | `ccpbiosim/fesetup`<br>source=`CCPBioSim/fesetup` | `repo-007268` `NKalavros/fesetup`（REPRESENTATIVE；parent=CCPBioSim/fesetup） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1757 | `repronim/module-intro`<br>source=`ReproNim/module-intro` | `repo-005122` `yarikoptic/module-intro`（REPRESENTATIVE；parent=ReproNim/module-intro） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1758 | `mickaelleclercq/mirdup`<br>source=`mickaelleclercq/mirdup` | `repo-001636` `mickaelleclercq/mirdup`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1759 | `yarikoptic/allen-neuropixels-try1`<br>source=`yarikoptic/allen-neuropixels-try1` | `repo-004375` `yarikoptic/allen-neuropixels-try1`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1760 | `biothings/biothings_explorer_archived`<br>source=`biothings/biothings_explorer_archived` | `repo-000899` `andrewsu/bte_schema`（REPRESENTATIVE；parent=biothings/biothings_explorer_archived） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1761 | `linguisticexplorer/linguistic-explorer`<br>source=`linguisticexplorer/Linguistic-Explorer` | `repo-006334` `Ali-Maq/Linguistic-Explorer`（REPRESENTATIVE；parent=linguisticexplorer/Linguistic-Explorer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1762 | `andrewsu/translator-hackathon-20190917`<br>source=`andrewsu/translator-hackathon-20190917` | `repo-000961` `andrewsu/translator-hackathon-20190917`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |

## 完整性边界

- 本文件连续覆盖 orders `1713–1762`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-039-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
