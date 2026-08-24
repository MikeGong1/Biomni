# 远程调研 Batch 040

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1763–1812**；**50** 个 family；**50** 条 bounded repository records。

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
| 分类 `DATASET_OR_BENCHMARK` | 4 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 15 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 19 |
| 分类 `LOW_INFORMATION_RECHECK` | 6 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 4 |
| 标记 `ARCHIVED_OR_DISABLED` | 2 |
| 标记 `CHILD_FORK_SURFACE` | 5 |
| 标记 `FORK_LINEAGE_REQUIRED` | 38 |
| 标记 `LICENSE_UNCLEAR` | 25 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1763 | `rescience/ten-years`<br>source=`ReScience/ten-years` | `repo-005653` `yarikoptic/ten-years`（REPRESENTATIVE；parent=ReScience/ten-years） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1764 | `nkalavros/mdpr-full`<br>source=`NKalavros/mdpr-full` | `repo-007276` `NKalavros/mdpr-full`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1765 | `genome-nexus/genome-nexus-cli`<br>source=`genome-nexus/genome-nexus-cli` | `repo-002798` `inodb/genome-nexus-cli`（REPRESENTATIVE；parent=genome-nexus/genome-nexus-cli） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1766 | `kexinhuang12345/espf`<br>source=`kexinhuang12345/ESPF` | `repo-001497` `kexinhuang12345/ESPF`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1767 | `sanat-mishra/analysing-synonymous-mutations.`<br>source=`Sanat-Mishra/Analysing-Synonymous-Mutations.` | `repo-007436` `Sanat-Mishra/Analysing-Synonymous-Mutations.`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1768 | `pymvpa/pymvpa`<br>source=`PyMVPA/PyMVPA` | `repo-005419` `yarikoptic/PyMVPA`（REPRESENTATIVE；parent=PyMVPA/PyMVPA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1769 | `nkalavros/thyroid-cancer-a-bioinformatics-approach`<br>source=`NKalavros/thyroid-cancer-a-bioinformatics-approach` | `repo-007296` `NKalavros/thyroid-cancer-a-bioinformatics-approach`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1770 | `garethjones210/exocomet_hunt_tess_sector_results`<br>source=`garethjones210/exocomet_hunt_TESS_sector_results` | `repo-006776` `drgmk/exocomet_hunt_TESS_sector_results`（REPRESENTATIVE；parent=garethjones210/exocomet_hunt_TESS_sector_results） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1771 | `garethjones210/exocomet_hunt`<br>source=`garethjones210/exocomet_hunt` | `repo-006775` `drgmk/exocomet_hunt`（REPRESENTATIVE；parent=garethjones210/exocomet_hunt） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1772 | `matthiaskoenig/brendapy`<br>source=`matthiaskoenig/brendapy` | `repo-006947` `Vik-u/brendapy`（REPRESENTATIVE；parent=matthiaskoenig/brendapy） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1773 | `vladsavelyev/targqc`<br>source=`vladsavelyev/TargQC` | `repo-004164` `vladsavelyev/TargQC`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1774 | `miykael/nipype_tutorial`<br>source=`miykael/nipype_tutorial` | `repo-005229` `yarikoptic/nipype_tutorial`（REPRESENTATIVE；parent=miykael/nipype_tutorial） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1775 | `changwn/atac_integrity`<br>source=`changwn/ATAC_integrity` | `repo-002572` `changwn/ATAC_integrity`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1776 | `neuronets/kwyk`<br>source=`neuronets/kwyk` | `repo-005022` `yarikoptic/kwyk`（REPRESENTATIVE；parent=neuronets/kwyk） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1777 | `changwn/mtct`<br>source=`changwn/MTCT` | `repo-002617` `changwn/MTCT`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1778 | `aabaker99/cdom`<br>source=`aabaker99/cdom` | `repo-007057` `jaybee84/cdom`（REPRESENTATIVE；parent=aabaker99/cdom） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1779 | `openneurodatasets/ds000164`<br>source=`OpenNeuroDatasets/ds000164` | `repo-004761` `yarikoptic/ds000164`（REPRESENTATIVE；parent=OpenNeuroDatasets/ds000164） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1780 | `sage-bionetworks/sandbox-provisioner`<br>source=`Sage-Bionetworks/sandbox-provisioner` | `repo-007120` `jaybee84/sandbox-provisioner`（REPRESENTATIVE；parent=Sage-Bionetworks/sandbox-provisioner） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1781 | `sage-bionetworks/rare-disease-workflows`<br>source=`Sage-Bionetworks/rare-disease-workflows` | `repo-007110` `jaybee84/rare-disease-workflows`（REPRESENTATIVE；parent=Sage-Bionetworks/rare-disease-workflows） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1782 | `nf-osi/nf-hackathon-2019`<br>source=`nf-osi/nf-hackathon-2019` | `repo-007094` `jaybee84/nf-hackathon-2019`（REPRESENTATIVE；parent=nf-osi/nf-hackathon-2019） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1783 | `asncd/mimosca`<br>source=`asncd/MIMOSCA` | `repo-002118` `shengyongniu/MIMOSCA`（REPRESENTATIVE；parent=asncd/MIMOSCA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1784 | `mskcc/cbsp-hackathon`<br>source=`mskcc/cbsp-hackathon` | `repo-002771` `inodb/cbsp-hackathon`（REPRESENTATIVE；parent=mskcc/cbsp-hackathon） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1785 | `datajoint-company/najafi-2018-nwb`<br>source=`datajoint-company/najafi-2018-nwb` | `repo-005148` `yarikoptic/najafi-2018-nwb`（REPRESENTATIVE；parent=datajoint-company/najafi-2018-nwb） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1786 | `multiqc/megaqc`<br>source=`MultiQC/MegaQC` | `repo-004128` `vladsavelyev/MegaQC`（REPRESENTATIVE；parent=MultiQC/MegaQC） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1787 | `cbioportal/oncoprintjs`<br>source=`cBioPortal/oncoprintjs` | `repo-002838` `inodb/oncoprintjs`（REPRESENTATIVE；parent=cBioPortal/oncoprintjs） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1788 | `illumina/manta`<br>source=`Illumina/manta` | `repo-004125` `vladsavelyev/manta`（REPRESENTATIVE；parent=Illumina/manta） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1789 | `jaybee84/sage-workflows-sandbox`<br>source=`jaybee84/sage-workflows-sandbox` | `repo-007117` `jaybee84/sage-workflows-sandbox`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1790 | `sage-bionetworks/nfresources`<br>source=`Sage-Bionetworks/nfResources` | `repo-007098` `jaybee84/nfResources`（REPRESENTATIVE；parent=Sage-Bionetworks/nfResources） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1791 | `nbeliy/eegbidscreator`<br>source=`nbeliy/eegBidsCreator` | `repo-004781` `yarikoptic/eegBidsCreator`（REPRESENTATIVE；parent=nbeliy/eegBidsCreator） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1792 | `miykael/fmriflows`<br>source=`miykael/fmriflows` | `repo-004833` `yarikoptic/fmriflows`（REPRESENTATIVE；parent=miykael/fmriflows） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1793 | `sgosline/nexus`<br>source=`sgosline/NEXUS` | `repo-007092` `jaybee84/NEXUS`（REPRESENTATIVE；parent=sgosline/NEXUS） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1794 | `xunzhizhang/tcr_explorer`<br>source=`xunzhizhang/TCR_explorer` | `repo-002362` `zhanxw/TCR_explorer`（REPRESENTATIVE；parent=xunzhizhang/TCR_explorer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1795 | `astrazeneca-ngs/simple_sv_annotation`<br>source=`AstraZeneca-NGS/simple_sv_annotation` | `repo-004157` `vladsavelyev/simple_sv_annotation`（REPRESENTATIVE；parent=AstraZeneca-NGS/simple_sv_annotation） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1796 | `sage-bionetworks/genie`<br>source=`Sage-Bionetworks/Genie` | `repo-007080` `jaybee84/Genie`（REPRESENTATIVE；parent=Sage-Bionetworks/Genie） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1797 | `yy6linda/mortality_prediction_docker_model`<br>source=`yy6linda/mortality_prediction_docker_model` | `repo-007342` `tschaffter/mortality_prediction_docker_model`（REPRESENTATIVE；parent=yy6linda/mortality_prediction_docker_model） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1798 | `xunzhizhang/tcr_explorer_package`<br>source=`xunzhizhang/TCR_explorer_package` | `repo-002363` `zhanxw/TCR_explorer_package`（REPRESENTATIVE；parent=xunzhizhang/TCR_explorer_package） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1799 | `knowledgesystems/signal`<br>source=`knowledgesystems/signal` | `repo-002832` `inodb/msk-insight`（REPRESENTATIVE；parent=knowledgesystems/signal） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1800 | `manu-tej/kinect2`<br>source=`manu-tej/Kinect2` | `repo-007243` `manu-tej/Kinect2`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1801 | `mskcc/vcf2maf`<br>source=`mskcc/vcf2maf` | `repo-002868` `inodb/vcf2maf`（REPRESENTATIVE；parent=mskcc/vcf2maf） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1802 | `n1zea144/biogene-backend`<br>source=`n1zea144/biogene-backend` | `repo-002750` `inodb/biogene-backend`（REPRESENTATIVE；parent=n1zea144/biogene-backend） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1803 | `sage-bionetworks/synapseannotations`<br>source=`Sage-Bionetworks/synapseAnnotations` | `repo-007131` `jaybee84/synapseAnnotations`（REPRESENTATIVE；parent=Sage-Bionetworks/synapseAnnotations） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1804 | `vladsavelyev/cawdor`<br>source=`vladsavelyev/cawdor` | `repo-004081` `vladsavelyev/cawdor`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1805 | `sage-bionetworks/synapser`<br>source=`Sage-Bionetworks/synapser` | `repo-007133` `jaybee84/synapser`（REPRESENTATIVE；parent=Sage-Bionetworks/synapser） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1806 | `cbioportal/session-service`<br>source=`cBioPortal/session-service` | `repo-002856` `inodb/session-service`（REPRESENTATIVE；parent=cBioPortal/session-service） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1807 | `shengyongniu/rseqtu`<br>source=`shengyongniu/rSeqTU` | `repo-002125` `shengyongniu/rSeqTU`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1808 | `ding-lab/birdseed2vcf`<br>source=`ding-lab/birdseed2vcf` | `repo-002299` `zhanxw/birdseed2vcf`（REPRESENTATIVE；parent=ding-lab/birdseed2vcf） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1809 | `vladsavelyev/umcaw`<br>source=`vladsavelyev/umcaw` | `repo-004171` `vladsavelyev/umcaw`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1810 | `alleninstitute/scrattch.hicat`<br>source=`AllenInstitute/scrattch.hicat` | `repo-007123` `jaybee84/scrattch.hicat`（REPRESENTATIVE；parent=AllenInstitute/scrattch.hicat） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1811 | `maayanlab/zika-rnaseq-pipeline`<br>source=`MaayanLab/Zika-RNAseq-Pipeline` | `repo-007143` `jaybee84/Zika-RNAseq-Pipeline`（REPRESENTATIVE；parent=MaayanLab/Zika-RNAseq-Pipeline） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1812 | `nf-core/sarek`<br>source=`nf-core/sarek` | `repo-004152` `vladsavelyev/Sarek`（REPRESENTATIVE；parent=nf-core/sarek） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1763–1812`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-040-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
