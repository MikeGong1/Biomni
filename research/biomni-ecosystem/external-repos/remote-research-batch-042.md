# 远程调研 Batch 042

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1863–1912**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 1 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 18 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 16 |
| 分类 `LOW_INFORMATION_RECHECK` | 9 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 3 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `FORK_LINEAGE_REQUIRED` | 31 |
| 标记 `LICENSE_UNCLEAR` | 33 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1863 | `changwn/ranktest`<br>source=`changwn/rankTest` | `repo-002623` `changwn/rankTest`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1864 | `idekerlab/pynbs`<br>source=`idekerlab/pyNBS` | `repo-007106` `jaybee84/pyNBS`（REPRESENTATIVE；parent=idekerlab/pyNBS） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1865 | `zhanxw/bayesslam`<br>source=`zhanxw/BayesSLAM` | `repo-002294` `zhanxw/BayesSLAM`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1866 | `vladsavelyev/venn`<br>source=`vladsavelyev/Venn` | `repo-004174` `vladsavelyev/Venn`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1867 | `umccr/umccrise`<br>source=`umccr/umccrise` | `repo-004172` `vladsavelyev/umccrise`（REPRESENTATIVE；parent=umccr/umccrise） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1868 | `nkalavros/cbioportal-queries`<br>source=`NKalavros/cBioportal-Queries` | `repo-007257` `NKalavros/cBioportal-Queries`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1869 | `drgmk/wtf`<br>source=`drgmk/wtf` | `repo-006795` `drgmk/wtf`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1870 | `astrazeneca-ngs/vardict`<br>source=`AstraZeneca-NGS/VarDict` | `repo-004173` `vladsavelyev/VarDict`（REPRESENTATIVE；parent=AstraZeneca-NGS/VarDict） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1871 | `vladsavelyev/ngs_reporting_testdata`<br>source=`vladsavelyev/NGS_Reporting_TestData` | `repo-004139` `vladsavelyev/NGS_Reporting_TestData`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1872 | `igemsoftware2017/sysu-software-2017`<br>source=`igemsoftware2017/SYSU-Software-2017` | `repo-003159` `Mr-Milk/SYSU-Software-2017`（REPRESENTATIVE；parent=igemsoftware2017/SYSU-Software-2017） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1873 | `leezx/mbsit`<br>source=`leezx/MBSIT` | `repo-007198` `leezx/MBSIT`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1874 | `repronim/reproducible-imaging`<br>source=`ReproNim/reproducible-imaging` | `repo-005496` `yarikoptic/reproducible-imaging`（REPRESENTATIVE；parent=ReproNim/reproducible-imaging） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1875 | `scikit-image/scikit-image`<br>source=`scikit-image/scikit-image` | `repo-005549` `yarikoptic/scikit-image`（REPRESENTATIVE；parent=scikit-image/scikit-image） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1876 | `vladsavelyev/pcgr_predispose`<br>source=`vladsavelyev/pcgr_predispose` | `repo-004143` `vladsavelyev/pcgr_predispose`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1877 | `zhanxw/cromwelldashboard`<br>source=`zhanxw/cromwellDashboard` | `repo-002307` `zhanxw/cromwellDashboard`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1878 | `broadinstitute/cromwell`<br>source=`broadinstitute/cromwell` | `repo-002306` `zhanxw/cromwell`（REPRESENTATIVE；parent=broadinstitute/cromwell） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1879 | `neurodroid/stimfit`<br>source=`neurodroid/stimfit` | `repo-005631` `yarikoptic/stimfit`（REPRESENTATIVE；parent=neurodroid/stimfit） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1880 | `conda-forge/pymvpa2-feedstock`<br>source=`conda-forge/pymvpa2-feedstock` | `repo-005421` `yarikoptic/pymvpa2-feedstock`（REPRESENTATIVE；parent=conda-forge/pymvpa2-feedstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1881 | `explorerwjy/cumc`<br>source=`explorerwjy/CUMC` | `repo-006050` `explorerwjy/CUMC`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1882 | `kuanlinhuang/ad_spi1_project`<br>source=`kuanlinhuang/AD_SPI1_project` | `repo-001522` `kuanlinhuang/AD_SPI1_project`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1883 | `unc-libraries/access-checker`<br>source=`UNC-Libraries/Access-Checker` | `repo-002423` `ahueb/Access-Checker`（REPRESENTATIVE；parent=UNC-Libraries/Access-Checker） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1884 | `allaway/cnf_brousseau_hippo`<br>source=`allaway/cNF_brousseau_hippo` | `repo-007061` `jaybee84/cNF_brousseau_hippo`（REPRESENTATIVE；parent=allaway/cNF_brousseau_hippo） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1885 | `griffithlab/rnaseq_tutorial`<br>source=`griffithlab/rnaseq_tutorial` | `repo-007113` `jaybee84/rnaseq_tutorial`（REPRESENTATIVE；parent=griffithlab/rnaseq_tutorial） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1886 | `ivis-at-bilkent/pathway-mapper`<br>source=`iVis-at-Bilkent/pathway-mapper` | `repo-002840` `inodb/pathway-mapper`（REPRESENTATIVE；parent=iVis-at-Bilkent/pathway-mapper） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1887 | `vladsavelyev/multiqc_az`<br>source=`vladsavelyev/MultiQC_az` | `repo-004131` `vladsavelyev/MultiQC_az`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1888 | `hemberg-lab/scrna.seq.course`<br>source=`hemberg-lab/scRNA.seq.course` | `repo-007124` `jaybee84/scRNA.seq.course`（REPRESENTATIVE；parent=hemberg-lab/scRNA.seq.course） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1889 | `neurolabusc/dcm_qa`<br>source=`neurolabusc/dcm_qa` | `repo-004699` `yarikoptic/dcm_qa`（REPRESENTATIVE；parent=neurolabusc/dcm_qa） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1890 | `uwescience/shablona`<br>source=`uwescience/shablona` | `repo-005568` `yarikoptic/shablona`（REPRESENTATIVE；parent=uwescience/shablona） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1891 | `carmin-org/carmin-api`<br>source=`CARMIN-org/CARMIN-API` | `repo-004535` `yarikoptic/CARMIN-API`（REPRESENTATIVE；parent=CARMIN-org/CARMIN-API） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1892 | `kuanlinhuang/populargenes`<br>source=`kuanlinhuang/PopularGenes` | `repo-001547` `kuanlinhuang/PopularGenes`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1893 | `scitran-apps/dcm2niix`<br>source=`scitran-apps/dcm2niix` | `repo-004698` `yarikoptic/dcm2niix`（REPRESENTATIVE；parent=scitran-apps/dcm2niix） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1894 | `walaj/bxtools`<br>source=`walaj/bxtools` | `repo-004079` `vladsavelyev/bxtools`（REPRESENTATIVE；parent=walaj/bxtools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1895 | `vibansal/hapcut2`<br>source=`vibansal/HapCUT2` | `repo-004113` `vladsavelyev/HapCUT2`（REPRESENTATIVE；parent=vibansal/HapCUT2） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1896 | `bd2kgenomics/dockstore_tool_arriba`<br>source=`BD2KGenomics/dockstore_tool_arriba` | `repo-002594` `changwn/dockstore_tool_arriba`（REPRESENTATIVE；parent=BD2KGenomics/dockstore_tool_arriba） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1897 | `freesurfer/freesurfer`<br>source=`freesurfer/freesurfer` | `repo-004838` `yarikoptic/freesurfer`（REPRESENTATIVE；parent=freesurfer/freesurfer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1898 | `th86/transmeddatasets`<br>source=`th86/transmeddatasets` | `repo-002209` `th86/transmeddatasets`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1899 | `psychoinformatics-de/cbbs-imaging-docs`<br>source=`psychoinformatics-de/cbbs-imaging-docs` | `repo-004538` `yarikoptic/cbbs-imaging-docs`（REPRESENTATIVE；parent=psychoinformatics-de/cbbs-imaging-docs） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1900 | `pmk89/ipysci`<br>source=`PMK89/IpySci` | `repo-006596` `PMK89/IpySci`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1901 | `ncbi-hackathons/gooddoc`<br>source=`NCBI-Hackathons/GoodDoc` | `repo-007081` `jaybee84/GoodDoc`（REPRESENTATIVE；parent=NCBI-Hackathons/GoodDoc） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1902 | `suyashdb/hcp2bids`<br>source=`suyashdb/hcp2bids` | `repo-004933` `yarikoptic/hcp2bids`（REPRESENTATIVE；parent=suyashdb/hcp2bids） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1903 | `chapmanb/cloudbiolinux`<br>source=`chapmanb/cloudbiolinux` | `repo-004085` `vladsavelyev/cloudbiolinux`（REPRESENTATIVE；parent=chapmanb/cloudbiolinux） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1904 | `kuanlinhuang/pdxnatcomm2017`<br>source=`kuanlinhuang/PDXNatComm2017` | `repo-001546` `kuanlinhuang/PDXNatComm2017`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1905 | `explorerwjy/cohortpca`<br>source=`explorerwjy/CohortPCA` | `repo-006049` `explorerwjy/CohortPCA`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1906 | `explorerwjy/genotying_with_dnn`<br>source=`explorerwjy/GenoTying_with_Dnn` | `repo-006059` `explorerwjy/GenoTying_with_Dnn`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1907 | `geneontology/go-site`<br>source=`geneontology/go-site` | `repo-002715` `goodb/go-site`（REPRESENTATIVE；parent=geneontology/go-site）<br>`repo-000915` `andrewsu/go-site`（MEMBER；parent=geneontology/go-site） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1908 | `cole-trapnell-lab/monocle-release`<br>source=`cole-trapnell-lab/monocle-release` | `repo-002179` `th86/monocle-release`（REPRESENTATIVE；parent=cole-trapnell-lab/monocle-release） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1909 | `leffj/mctoolsr`<br>source=`leffj/mctoolsr` | `repo-002336` `zhanxw/mctoolsr`（REPRESENTATIVE；parent=leffj/mctoolsr） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1910 | `minxz/invasive-species-monitoring`<br>source=`MinxZ/Invasive-Species-Monitoring` | `repo-001661` `MinxZ/Invasive-Species-Monitoring`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1911 | `pmeal/openpnm`<br>source=`PMEAL/OpenPNM` | `repo-001571` `lxasqjc/OpenPNM`（REPRESENTATIVE；parent=PMEAL/OpenPNM） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1912 | `nanxstats/logd74`<br>source=`nanxstats/logd74` | `repo-001504` `kexinhuang12345/logd74`（REPRESENTATIVE；parent=nanxstats/logd74） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |

## 完整性边界

- 本文件连续覆盖 orders `1863–1912`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-042-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
