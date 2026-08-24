# 远程调研 Batch 038

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1663–1712**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 2 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 13 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 20 |
| 分类 `LOW_INFORMATION_RECHECK` | 7 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 5 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `FORK_LINEAGE_REQUIRED` | 40 |
| 标记 `LICENSE_UNCLEAR` | 20 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1663 | `waymentsteelelab/arnie`<br>source=`WaymentSteeleLab/arnie` | `repo-007254` `NKalavros/arnie`（REPRESENTATIVE；parent=WaymentSteeleLab/arnie） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1664 | `sage-bionetworks/portals`<br>source=`Sage-Bionetworks/portals` | `repo-007356` `tschaffter/portals`（REPRESENTATIVE；parent=Sage-Bionetworks/portals） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1665 | `tanaka-group/eczemanet`<br>source=`Tanaka-Group/EczemaNet` | `repo-001061` `evolu8/EczemaNet`（REPRESENTATIVE；parent=Tanaka-Group/EczemaNet） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1666 | `hartwigmedical/hmftools`<br>source=`hartwigmedical/hmftools` | `repo-004115` `vladsavelyev/hmftools`（REPRESENTATIVE；parent=hartwigmedical/hmftools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1667 | `waldronlab/cbioportaldata`<br>source=`waldronlab/cBioPortalData` | `repo-002768` `inodb/cBioPortalData`（REPRESENTATIVE；parent=waldronlab/cBioPortalData）<br>`repo-001388` `jucor/cBioPortalData`（MEMBER；parent=waldronlab/cBioPortalData） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1668 | `dcan-labs/nda-abcd-s3-downloader`<br>source=`DCAN-Labs/nda-abcd-s3-downloader` | `repo-005154` `yarikoptic/nda-abcd-s3-downloader`（REPRESENTATIVE；parent=DCAN-Labs/nda-abcd-s3-downloader） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1669 | `mic-dkfz/niicat`<br>source=`MIC-DKFZ/niicat` | `repo-005214` `yarikoptic/niicat`（REPRESENTATIVE；parent=MIC-DKFZ/niicat） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1670 | `drgmk/ni`<br>source=`drgmk/ni` | `repo-006783` `drgmk/ni`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1671 | `dandi/redirector`<br>source=`dandi/redirector` | `repo-005486` `yarikoptic/redirector`（REPRESENTATIVE；parent=dandi/redirector） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1672 | `mingyi-wang/somatic-combiner`<br>source=`mingyi-wang/somatic-combiner` | `repo-007126` `jaybee84/somatic-combiner`（REPRESENTATIVE；parent=mingyi-wang/somatic-combiner） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1673 | `data2health/nlp-sandbox`<br>source=`data2health/nlp-sandbox` | `repo-007345` `tschaffter/nlp-sandbox`（REPRESENTATIVE；parent=data2health/nlp-sandbox） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1674 | `yarikoptic/mriqc-sample1`<br>source=`yarikoptic/mriqc-sample1` | `repo-005136` `yarikoptic/mriqc-sample1`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1675 | `lxasqjc/foveation-for-segmentation-of-mega-pixel-histology-images`<br>source=`lxasqjc/Foveation-for-Segmentation-of-Mega-pixel-Histology-Images` | `repo-001560` `lxasqjc/Foveation-for-Segmentation-of-Mega-pixel-Histology-Images`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1676 | `mc2-center/csbc-pson-dcc`<br>source=`mc2-center/csbc-pson-dcc` | `repo-007066` `jaybee84/csbc-pson-dcc`（REPRESENTATIVE；parent=mc2-center/csbc-pson-dcc） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1677 | `kotfic/i2b2_evaluation_scripts`<br>source=`kotfic/i2b2_evaluation_scripts` | `repo-007337` `tschaffter/i2b2_evaluation_scripts`（REPRESENTATIVE；parent=kotfic/i2b2_evaluation_scripts） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`CHILD_FORK_SURFACE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1678 | `rocker-org/rocker-versioned`<br>source=`rocker-org/rocker-versioned` | `repo-007363` `tschaffter/rocker-versioned`（REPRESENTATIVE；parent=rocker-org/rocker-versioned） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1679 | `datalad-datasets/ohbm2020-posters`<br>source=`datalad-datasets/ohbm2020-posters` | `repo-005263` `yarikoptic/ohbm2020-posters`（REPRESENTATIVE；parent=datalad-datasets/ohbm2020-posters） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1680 | `jkiang13/synapseshinyapp`<br>source=`jkiang13/SynapseShinyApp` | `repo-007134` `jaybee84/SynapseShinyApp`（REPRESENTATIVE；parent=jkiang13/SynapseShinyApp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1681 | `leezx/wgs_pipeline_bestpractice`<br>source=`leezx/WGS_Pipeline_BestPractice` | `repo-007213` `leezx/WGS_Pipeline_BestPractice`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1682 | `greenelab/tdm`<br>source=`greenelab/TDM` | `repo-001640` `mickaelleclercq/TDM`（REPRESENTATIVE；parent=greenelab/TDM） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1683 | `sage-bionetworks/synapseforms`<br>source=`Sage-Bionetworks/synapseforms` | `repo-007132` `jaybee84/synapseforms`（REPRESENTATIVE；parent=Sage-Bionetworks/synapseforms） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1684 | `taylor-lab/hotspots`<br>source=`taylor-lab/hotspots` | `repo-002805` `inodb/hotspots`（REPRESENTATIVE；parent=taylor-lab/hotspots） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1685 | `alfredyewang/wevar`<br>source=`alfredyewang/WEVar` | `repo-002650` `changwn/WEVar`（REPRESENTATIVE；parent=alfredyewang/WEVar） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1686 | `sanat-mishra/multisample-vcf---pedia`<br>source=`Sanat-Mishra/Multisample-VCF---PEDIA` | `repo-007450` `Sanat-Mishra/Multisample-VCF---PEDIA`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1687 | `camdavidsonpilon/lifelines`<br>source=`CamDavidsonPilon/lifelines` | `repo-000874` `amehrjou/lifelines`（REPRESENTATIVE；parent=CamDavidsonPilon/lifelines） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1688 | `ashtonteng/biomedical-graph-visualizer`<br>source=`ashtonteng/biomedical-graph-visualizer` | `repo-000896` `andrewsu/biomedical-graph-visualizer`（REPRESENTATIVE；parent=ashtonteng/biomedical-graph-visualizer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1689 | `immunogenomics/harmony`<br>source=`immunogenomics/harmony` | `repo-007270` `NKalavros/harmony`（REPRESENTATIVE；parent=immunogenomics/harmony） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1690 | `yarikoptic/bids-app-dummy`<br>source=`yarikoptic/bids-app-dummy` | `repo-004456` `yarikoptic/bids-app-dummy`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1691 | `kevinblighe/e-mtab-6141`<br>source=`kevinblighe/E-MTAB-6141` | `repo-002596` `changwn/E-MTAB-6141`（REPRESENTATIVE；parent=kevinblighe/E-MTAB-6141） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1692 | `openvax/pyensembl`<br>source=`openvax/pyensembl` | `repo-004147` `vladsavelyev/pyensembl`（REPRESENTATIVE；parent=openvax/pyensembl） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1693 | `crazyhottommy/scatacseq-analysis-notes`<br>source=`crazyhottommy/scATACseq-analysis-notes` | `repo-002631` `changwn/scATACseq-analysis-notes`（REPRESENTATIVE；parent=crazyhottommy/scATACseq-analysis-notes） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1694 | `yy6linda/covid_diagnosis_baseline`<br>source=`yy6linda/COVID_diagnosis_baseline` | `repo-007310` `tschaffter/COVID_diagnosis_baseline`（REPRESENTATIVE；parent=yy6linda/COVID_diagnosis_baseline） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1695 | `soroushchehresa/awesome-coronavirus`<br>source=`soroushchehresa/awesome-coronavirus` | `repo-007302` `tschaffter/awesome-coronavirus`（REPRESENTATIVE；parent=soroushchehresa/awesome-coronavirus） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1696 | `kexinhuang12345/skipgnn`<br>source=`kexinhuang12345/SkipGNN` | `repo-001517` `kexinhuang12345/SkipGNN`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1697 | `getzlab/scrinvex`<br>source=`getzlab/scrinvex` | `repo-007291` `NKalavros/scrinvex`（REPRESENTATIVE；parent=getzlab/scrinvex） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1698 | `yarikoptic/heudiconv-testdata`<br>source=`yarikoptic/heudiconv-testdata` | `repo-004948` `yarikoptic/heudiconv-testdata`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1699 | `vladsavelyev/gridss-purple-linx`<br>source=`vladsavelyev/gridss-purple-linx` | `repo-004108` `vladsavelyev/gridss-purple-linx`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1700 | `multiqc/multiqc_bcbio`<br>source=`MultiQC/MultiQC_bcbio` | `repo-004132` `vladsavelyev/MultiQC_bcbio`（REPRESENTATIVE；parent=MultiQC/MultiQC_bcbio） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1701 | `bcbio/bcbio-nextgen`<br>source=`bcbio/bcbio-nextgen` | `repo-004073` `vladsavelyev/bcbio-nextgen`（REPRESENTATIVE；parent=bcbio/bcbio-nextgen） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1702 | `wang-cankun/rna-seq-pipeline`<br>source=`Wang-Cankun/RNA-seq-pipeline` | `repo-002626` `changwn/RNA-seq-pipeline`（REPRESENTATIVE；parent=Wang-Cankun/RNA-seq-pipeline） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1703 | `hkmztrk/deepdta`<br>source=`hkmztrk/DeepDTA` | `repo-007148` `KSUN63/DeepDTA`（REPRESENTATIVE；parent=hkmztrk/DeepDTA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1704 | `bioimagesuiteweb/bisweb`<br>source=`bioimagesuiteweb/bisweb` | `repo-004490` `yarikoptic/bisweb`（REPRESENTATIVE；parent=bioimagesuiteweb/bisweb） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1705 | `ncatstranslator/relay`<br>source=`NCATSTranslator/Relay` | `repo-000943` `andrewsu/Relay`（REPRESENTATIVE；parent=NCATSTranslator/Relay） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1706 | `pedia-charite/pedia-workflow`<br>source=`PEDIA-Charite/PEDIA-workflow` | `repo-007451` `Sanat-Mishra/PEDIA-workflow`（REPRESENTATIVE；parent=PEDIA-Charite/PEDIA-workflow） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1707 | `maximilianh/cellbrowser`<br>source=`maximilianh/cellBrowser` | `repo-002773` `inodb/cellBrowser`（REPRESENTATIVE；parent=maximilianh/cellBrowser） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1708 | `tridesclous/tridesclous`<br>source=`tridesclous/tridesclous` | `repo-005707` `yarikoptic/tridesclous`（REPRESENTATIVE；parent=tridesclous/tridesclous） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1709 | `namphuon/vifi`<br>source=`namphuon/ViFi` | `repo-004176` `vladsavelyev/ViFi`（REPRESENTATIVE；parent=namphuon/ViFi） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1710 | `hoffmangroup/polyidus`<br>source=`hoffmangroup/polyidus` | `repo-004145` `vladsavelyev/polyidus`（REPRESENTATIVE；parent=hoffmangroup/polyidus） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1711 | `zwang-lab/trftarget`<br>source=`ZWang-Lab/tRFtarget` | `repo-002649` `changwn/tRFTarget`（REPRESENTATIVE；parent=ZWang-Lab/tRFtarget） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1712 | `changwn/icps`<br>source=`changwn/ICPS` | `repo-002601` `changwn/ICPS`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |

## 完整性边界

- 本文件连续覆盖 orders `1663–1712`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-038-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
