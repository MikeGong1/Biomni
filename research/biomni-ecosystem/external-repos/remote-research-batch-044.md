# 远程调研 Batch 044

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1963–2012**；**50** 个 family；**50** 条 bounded repository records。

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
| 分类 `CURATED_CATALOG_OR_DOCS` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 16 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 22 |
| 分类 `LOW_INFORMATION_RECHECK` | 6 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 4 |
| 标记 `ARCHIVED_OR_DISABLED` | 1 |
| 标记 `CHILD_FORK_SURFACE` | 9 |
| 标记 `FORK_LINEAGE_REQUIRED` | 33 |
| 标记 `LICENSE_UNCLEAR` | 31 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1963 | `contextlab/dartmouth-openbci-hackathon`<br>source=`ContextLab/Dartmouth-OpenBCI-Hackathon` | `repo-004648` `yarikoptic/Dartmouth-OpenBCI-Hackathon`（REPRESENTATIVE；parent=ContextLab/Dartmouth-OpenBCI-Hackathon） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1964 | `openbci-archive/openbci_python`<br>source=`openbci-archive/OpenBCI_Python` | `repo-005280` `yarikoptic/OpenBCI_Python`（REPRESENTATIVE；parent=openbci-archive/OpenBCI_Python） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1965 | `statsmodels/statsmodels`<br>source=`statsmodels/statsmodels` | `repo-005628` `yarikoptic/statsmodels`（REPRESENTATIVE；parent=statsmodels/statsmodels） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1966 | `konradjk/exac_browser`<br>source=`konradjk/exac_browser` | `repo-006054` `explorerwjy/exac_browser`（REPRESENTATIVE；parent=konradjk/exac_browser） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1967 | `inodb/dicom-flask-uploader`<br>source=`inodb/dicom-flask-uploader` | `repo-002786` `inodb/dicom-flask-uploader`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1968 | `th86/biosearch`<br>source=`th86/BioSearch` | `repo-002147` `th86/BioSearch`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1969 | `pughlab/cbioportal-octane-overlay`<br>source=`pughlab/cbioportal-octane-overlay` | `repo-002767` `inodb/cbioportal-octane-overlay`（REPRESENTATIVE；parent=pughlab/cbioportal-octane-overlay） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1970 | `pydicom/pydicom`<br>source=`pydicom/pydicom` | `repo-002845` `inodb/pydicom`（REPRESENTATIVE；parent=pydicom/pydicom） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1971 | `inodb/pdx-data-hub`<br>source=`inodb/pdx-data-hub` | `repo-002841` `inodb/pdx-data-hub`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1972 | `pablocabaleiro/projectzebra`<br>source=`PabloCabaleiro/ProjectZebra` | `repo-003209` `PabloCabaleiro/ProjectZebra`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1973 | `mwaskom/seaborn`<br>source=`mwaskom/seaborn` | `repo-005557` `yarikoptic/seaborn`（REPRESENTATIVE；parent=mwaskom/seaborn） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1974 | `explorerwjy/rosalind`<br>source=`explorerwjy/rosalind` | `repo-006069` `explorerwjy/rosalind`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1975 | `andrewsu/cvd_mining`<br>source=`andrewsu/CVD_mining` | `repo-000905` `andrewsu/CVD_mining`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1976 | `inodb/cbioportal-frontend-test`<br>source=`inodb/cbioportal-frontend-test` | `repo-002765` `inodb/cbioportal-frontend-test`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1977 | `sulab/repurposing-drugs-on-hetnet-fiting-model-`<br>source=`SuLab/Repurposing-drugs-on-hetnet-fiting-model-` | `repo-000945` `andrewsu/Repurposing-drugs-on-hetnet-fiting-model-`（REPRESENTATIVE；parent=SuLab/Repurposing-drugs-on-hetnet-fiting-model-） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1978 | `bids-apps/example`<br>source=`bids-apps/example` | `repo-004795` `yarikoptic/example`（REPRESENTATIVE；parent=bids-apps/example） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1979 | `trungdong/prov`<br>source=`trungdong/prov` | `repo-005373` `yarikoptic/prov`（REPRESENTATIVE；parent=trungdong/prov） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1980 | `rdevon/cortex_old`<br>source=`rdevon/cortex_old` | `repo-004610` `yarikoptic/cortex`（REPRESENTATIVE；parent=rdevon/cortex_old） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1981 | `aces/loris`<br>source=`aces/Loris` | `repo-005062` `yarikoptic/Loris`（REPRESENTATIVE；parent=aces/Loris） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1982 | `ndar/nda_aws_token_generator`<br>source=`NDAR/nda_aws_token_generator` | `repo-005156` `yarikoptic/nda_aws_token_generator`（REPRESENTATIVE；parent=NDAR/nda_aws_token_generator） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1983 | `yarikoptic/neural-coding`<br>source=`yarikoptic/Neural-coding` | `repo-005168` `yarikoptic/Neural-coding`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1984 | `zhanxw/anno`<br>source=`zhanxw/anno` | `repo-002287` `zhanxw/anno`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1985 | `davidaknowles/leafcutter`<br>source=`davidaknowles/leafcutter` | `repo-002324` `zhanxw/leafcutter`（REPRESENTATIVE；parent=davidaknowles/leafcutter） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1986 | `datacite/content-resolver`<br>source=`datacite/content-resolver` | `repo-004595` `yarikoptic/content-resolver`（REPRESENTATIVE；parent=datacite/content-resolver） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1987 | `idekerlab/tsri-lecture`<br>source=`idekerlab/tsri-lecture` | `repo-002725` `goodb/tsri-lecture`（REPRESENTATIVE；parent=idekerlab/tsri-lecture） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1988 | `incf-nidash/nidm-specs`<br>source=`incf-nidash/nidm-specs` | `repo-005211` `yarikoptic/nidm`（REPRESENTATIVE；parent=incf-nidash/nidm-specs） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1989 | `knowledgefutures/pubpub`<br>source=`knowledgefutures/pubpub` | `repo-005389` `yarikoptic/pubpub`（REPRESENTATIVE；parent=knowledgefutures/pubpub） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1990 | `oborel/obo-relations`<br>source=`oborel/obo-relations` | `repo-002717` `goodb/obo-relations`（REPRESENTATIVE；parent=oborel/obo-relations） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1991 | `andrewsu/abcb`<br>source=`andrewsu/ABCB` | `repo-000886` `andrewsu/ABCB`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1992 | `zhanxw/checkvcf`<br>source=`zhanxw/checkVCF` | `repo-002303` `zhanxw/checkVCF`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1993 | `pysam-developers/pysam`<br>source=`pysam-developers/pysam` | `repo-007525` `hannes-brt/pysam`（REPRESENTATIVE；parent=pysam-developers/pysam） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1994 | `jkutner/cbioportal-buildpack`<br>source=`jkutner/cbioportal-buildpack` | `repo-002759` `inodb/cbioportal-buildpack`（REPRESENTATIVE；parent=jkutner/cbioportal-buildpack） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1995 | `th86/scumikit`<br>source=`th86/SCUMIKit` | `repo-002198` `th86/SCUMIKit`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1996 | `pyhrf/pyhrf`<br>source=`pyhrf/pyhrf` | `repo-005412` `yarikoptic/pyhrf`（REPRESENTATIVE；parent=pyhrf/pyhrf） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1997 | `mvdoc/reprclust`<br>source=`mvdoc/reprclust` | `repo-005494` `yarikoptic/reprclust`（REPRESENTATIVE；parent=mvdoc/reprclust） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1998 | `psi-lab/bento-seq`<br>source=`PSI-Lab/BENTO-Seq` | `repo-007508` `hannes-brt/BENTO-Seq`（REPRESENTATIVE；parent=PSI-Lab/BENTO-Seq） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1999 | `astronomy-software-index/2015-workshop`<br>source=`astronomy-software-index/2015-workshop` | `repo-004342` `yarikoptic/2015-workshop`（REPRESENTATIVE；parent=astronomy-software-index/2015-workshop） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2000 | `aligners/funcnorm`<br>source=`aligners/funcnorm` | `repo-004845` `yarikoptic/funcnorm`（REPRESENTATIVE；parent=aligners/funcnorm） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2001 | `tomkellygenetics/wikipathways_geneset_r`<br>source=`TomKellyGenetics/WikiPathways_GeneSet_R` | `repo-001551` `kuanlinhuang/WikiPathways_GeneSet_R`（REPRESENTATIVE；parent=TomKellyGenetics/WikiPathways_GeneSet_R） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2002 | `martinpyka/neurosvg`<br>source=`MartinPyka/NeuroSVG` | `repo-005196` `yarikoptic/NeuroSVG`（REPRESENTATIVE；parent=MartinPyka/NeuroSVG） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2003 | `arokem/att_ss`<br>source=`arokem/att_ss` | `repo-007049` `jaybee84/att_ss`（REPRESENTATIVE；parent=arokem/att_ss） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2004 | `niknafs/ngstools`<br>source=`Niknafs/NGSTools` | `repo-002833` `inodb/NGSTools`（REPRESENTATIVE；parent=Niknafs/NGSTools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2005 | `broadinstitute/picard`<br>source=`broadinstitute/picard` | `repo-002842` `inodb/picard`（REPRESENTATIVE；parent=broadinstitute/picard） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2006 | `inodb/2015-04-13-verse-virusfinder-presentation`<br>source=`inodb/2015-04-13-verse-virusfinder-presentation` | `repo-002744` `inodb/2015-04-13-verse-virusfinder-presentation`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2007 | `yarikoptic/hcp-neurodebian`<br>source=`yarikoptic/hcp-neurodebian` | `repo-004932` `yarikoptic/hcp-neurodebian`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2008 | `inodb/snakemake-workflows`<br>source=`inodb/snakemake-workflows` | `repo-002861` `inodb/snakemake-workflows`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2009 | `genome/genome`<br>source=`genome/genome` | `repo-001537` `kuanlinhuang/genome`（REPRESENTATIVE；parent=genome/genome） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 2010 | `zhanxw/linkageanalyzer`<br>source=`zhanxw/LinkageAnalyzer` | `repo-002327` `zhanxw/LinkageAnalyzer`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2011 | `natverse/nat`<br>source=`natverse/nat` | `repo-005152` `yarikoptic/nat`（REPRESENTATIVE；parent=natverse/nat） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2012 | `vladsavelyev/az_orthofinder`<br>source=`vladsavelyev/AZ_Orthofinder` | `repo-004072` `vladsavelyev/AZ_Orthofinder`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |

## 完整性边界

- 本文件连续覆盖 orders `1963–2012`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-044-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
