# 远程调研 Batch 027

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1113–1162**；**50** 个 family；**52** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 52 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 5 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 20 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 15 |
| 分类 `LOW_INFORMATION_RECHECK` | 1 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 6 |
| 标记 `CHILD_FORK_SURFACE` | 2 |
| 标记 `FORK_LINEAGE_REQUIRED` | 47 |
| 标记 `LICENSE_UNCLEAR` | 20 |
| 标记 `MULTI_MEMBER_FAMILY` | 2 |
| 标记 `RELEASE_SURFACE` | 2 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1113 | `jinworks/cellchat`<br>source=`jinworks/CellChat` | `repo-003054` `Liripo/CellChat`（REPRESENTATIVE；parent=jinworks/CellChat）<br>`repo-007259` `NKalavros/CellChat_ShinyApps`（MEMBER；parent=jinworks/CellChat） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1114 | `molssi/cookiecutter-cms`<br>source=`MolSSI/cookiecutter-cms` | `repo-004600` `yarikoptic/cookiecutter-cms`（REPRESENTATIVE；parent=MolSSI/cookiecutter-cms） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1115 | `seekrcentral/seekr2`<br>source=`seekrcentral/seekr2` | `repo-005560` `yarikoptic/seekr2`（REPRESENTATIVE；parent=seekrcentral/seekr2） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1116 | `bio-xtt/sgsanndatav2`<br>source=`bio-xtt/SgsAnnDataV2` | `repo-003089` `Liripo/SgsAnnDataV2`（REPRESENTATIVE；parent=bio-xtt/SgsAnnDataV2） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1117 | `khanlab/snakebids`<br>source=`khanlab/snakebids` | `repo-005595` `yarikoptic/snakebids`（REPRESENTATIVE；parent=khanlab/snakebids） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1118 | `neuromatchacademy/course-content`<br>source=`NeuromatchAcademy/course-content` | `repo-004614` `yarikoptic/course-content`（REPRESENTATIVE；parent=NeuromatchAcademy/course-content） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1119 | `3dmol/3dmol.js`<br>source=`3dmol/3Dmol.js` | `repo-007400` `Rasic2/3Dmol.js`（REPRESENTATIVE；parent=3dmol/3Dmol.js） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1120 | `alphamind-club/mlpa`<br>source=`alphamind-club/MLPA` | `repo-006876` `tangxuan82/MLPA`（REPRESENTATIVE；parent=alphamind-club/MLPA） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1121 | `maranasgroup/novostoic2.0`<br>source=`maranasgroup/novoStoic2.0` | `repo-006988` `Vik-u/novoStoic2.0`（REPRESENTATIVE；parent=maranasgroup/novoStoic2.0） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1122 | `maranasgroup/enzrank`<br>source=`maranasgroup/EnzRank` | `repo-006957` `Vik-u/EnzRank`（REPRESENTATIVE；parent=maranasgroup/EnzRank） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1123 | `dl4mhealth/contrastive-learning-in-medical-time-series-survey`<br>source=`DL4mHealth/Contrastive-Learning-in-Medical-Time-Series-Survey` | `repo-006483` `gutendzx/Contrastive-Learning-in-Medical-Time-Series-Survey`（REPRESENTATIVE；parent=DL4mHealth/Contrastive-Learning-in-Medical-Time-Series-Survey） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1124 | `fibonaccirabbit/cvan`<br>source=`Fibonaccirabbit/cVAN` | `repo-006486` `gutendzx/cVAN`（REPRESENTATIVE；parent=Fibonaccirabbit/cVAN） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1125 | `sokrypton/rfdiffusion`<br>source=`sokrypton/RFdiffusion` | `repo-006284` `alexj-lee/RFdiffusion`（REPRESENTATIVE；parent=sokrypton/RFdiffusion） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1126 | `jupyterhub/repo2docker-action`<br>source=`jupyterhub/repo2docker-action` | `repo-005492` `yarikoptic/repo2docker-action`（REPRESENTATIVE；parent=jupyterhub/repo2docker-action） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1127 | `pymc-devs/pymc`<br>source=`pymc-devs/pymc` | `repo-001439` `jucor/pymc`（REPRESENTATIVE；parent=pymc-devs/pymc） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1128 | `snap-stanford/gears`<br>source=`snap-stanford/GEARS` | `repo-001287` `HelloWorldLTY/GEARS`（REPRESENTATIVE；parent=snap-stanford/GEARS） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1129 | `tompollard/tableone`<br>source=`tompollard/tableone` | `repo-006646` `sszhu/tableone`（REPRESENTATIVE；parent=tompollard/tableone） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1130 | `dandi/dandi-docs`<br>source=`dandi/dandi-docs` | `repo-004923` `yarikoptic/handbook-1`（REPRESENTATIVE；parent=dandi/dandi-docs） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1131 | `restily/lamprimers-iq`<br>source=`Restily/LAMPrimers-iQ` | `repo-005927` `dabulseco/LAMPrimers-iQ`（REPRESENTATIVE；parent=Restily/LAMPrimers-iQ） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1132 | `alleninstitute/openscope_databook`<br>source=`AllenInstitute/openscope_databook` | `repo-005291` `yarikoptic/openscope_databook`（REPRESENTATIVE；parent=AllenInstitute/openscope_databook） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1133 | `dandi/example-notebooks`<br>source=`dandi/example-notebooks` | `repo-004798` `yarikoptic/example-notebooks-1`（REPRESENTATIVE；parent=dandi/example-notebooks） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1134 | `ccf-tfehlmann/ibdplexus`<br>source=`ccf-tfehlmann/ibdplexus` | `repo-006636` `sszhu/ibdplexus_ss`（REPRESENTATIVE；parent=ccf-tfehlmann/ibdplexus） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1135 | `bids-apps/bids-apps.github.io`<br>source=`bids-apps/bids-apps.github.io` | `repo-004457` `yarikoptic/bids-apps.github.io`（REPRESENTATIVE；parent=bids-apps/bids-apps.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1136 | `afni/afni_proc_simple_bids_app`<br>source=`afni/afni_proc_simple_bids_app` | `repo-004362` `yarikoptic/afni_proc_simple_bids_app`（REPRESENTATIVE；parent=afni/afni_proc_simple_bids_app） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1137 | `repronim/neurodocker`<br>source=`ReproNim/neurodocker` | `repo-005184` `yarikoptic/neurodocker`（REPRESENTATIVE；parent=ReproNim/neurodocker） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1138 | `afni/afni`<br>source=`afni/afni` | `repo-004359` `yarikoptic/afni`（REPRESENTATIVE；parent=afni/afni） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1139 | `drgmk/eccentric-width`<br>source=`drgmk/eccentric-width` | `repo-006774` `drgmk/eccentric-width`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RELEASE_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1140 | `drgmk/alma`<br>source=`drgmk/alma` | `repo-006763` `drgmk/alma`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | 无额外标记 | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1141 | `griffithslab/whobpyt`<br>source=`GriffithsLab/whobpyt` | `repo-005759` `yarikoptic/whobpyt`（REPRESENTATIVE；parent=GriffithsLab/whobpyt） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1142 | `ponnhide/pycircos`<br>source=`ponnhide/pyCircos` | `repo-006786` `drgmk/pyCircos`（REPRESENTATIVE；parent=ponnhide/pyCircos） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1143 | `ronigurvich/peptriever`<br>source=`RoniGurvich/Peptriever` | `repo-006880` `tangxuan82/Peptriever`（REPRESENTATIVE；parent=RoniGurvich/Peptriever） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1144 | `mih/mridefacer`<br>source=`mih/mridefacer` | `repo-005134` `yarikoptic/mridefacer`（REPRESENTATIVE；parent=mih/mridefacer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1145 | `peerherholz/bidsonym`<br>source=`PeerHerholz/BIDSonym` | `repo-004483` `yarikoptic/BIDSonym`（REPRESENTATIVE；parent=PeerHerholz/BIDSonym） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1146 | `miykael/gif_your_nifti`<br>source=`miykael/gif_your_nifti` | `repo-004861` `yarikoptic/gif_your_nifti`（REPRESENTATIVE；parent=miykael/gif_your_nifti） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1147 | `pvandyken/rsbids`<br>source=`pvandyken/rsbids` | `repo-005523` `yarikoptic/rsbids`（REPRESENTATIVE；parent=pvandyken/rsbids） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1148 | `pulse2percept/pulse2percept`<br>source=`pulse2percept/pulse2percept` | `repo-005392` `yarikoptic/pulse2percept`（REPRESENTATIVE；parent=pulse2percept/pulse2percept） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1149 | `openneuropet/pet2bids`<br>source=`openneuropet/PET2BIDS` | `repo-005326` `yarikoptic/PET2BIDS`（REPRESENTATIVE；parent=openneuropet/PET2BIDS） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1150 | `kexinhuang12345/deeppurpose`<br>source=`kexinhuang12345/DeepPurpose` | `repo-001494` `kexinhuang12345/DeepPurpose`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1151 | `nimh-dsst/dsst-defacing-pipeline`<br>source=`nimh-dsst/dsst-defacing-pipeline` | `repo-004765` `yarikoptic/dsst-defacing-pipeline`（REPRESENTATIVE；parent=nimh-dsst/dsst-defacing-pipeline） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1152 | `datalad/datalad-crawler`<br>source=`datalad/datalad-crawler` | `repo-004670` `yarikoptic/datalad-crawler`（REPRESENTATIVE；parent=datalad/datalad-crawler） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1153 | `rthapa84/sleepfm-codebase`<br>source=`rthapa84/sleepfm-codebase` | `repo-006537` `gutendzx/sleepfm-codebase`（REPRESENTATIVE；parent=rthapa84/sleepfm-codebase） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1154 | `amirlivne/pd-l1_predictor`<br>source=`amirlivne/PD-L1_predictor` | `repo-006879` `tangxuan82/PD-L1_predictor`（REPRESENTATIVE；parent=amirlivne/PD-L1_predictor） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1155 | `complete-genomics/dnbseq_complete_wgs`<br>source=`Complete-Genomics/DNBSEQ_Complete_WGS` | `repo-007215` `lishengting/CompleteWGS`（REPRESENTATIVE；parent=Complete-Genomics/DNBSEQ_Complete_WGS） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1156 | `kienerj/pycdxml`<br>source=`kienerj/pycdxml` | `repo-006146` `SongyouZhong/pycdxml`（REPRESENTATIVE；parent=kienerj/pycdxml）<br>`repo-007167` `KSUN63/synthesis-vis`（MEMBER；parent=kienerj/pycdxml） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1157 | `dvwz/atomeyes`<br>source=`dvwz/AtomEyes` | `repo-004408` `yarikoptic/AtomEyes`（REPRESENTATIVE；parent=dvwz/AtomEyes） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1158 | `conda-forge/datalad-feedstock`<br>source=`conda-forge/datalad-feedstock` | `repo-004675` `yarikoptic/datalad-feedstock`（REPRESENTATIVE；parent=conda-forge/datalad-feedstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1159 | `kuhlman-lab/pippack`<br>source=`Kuhlman-Lab/PIPPack` | `repo-007161` `KSUN63/PIPPack`（REPRESENTATIVE；parent=Kuhlman-Lab/PIPPack） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1160 | `magics-lab/dnabert_2`<br>source=`MAGICS-LAB/DNABERT_2` | `repo-007073` `jaybee84/DNABERT_2`（REPRESENTATIVE；parent=MAGICS-LAB/DNABERT_2） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1161 | `gist-ailab/sleepyco`<br>source=`gist-ailab/SleePyCo` | `repo-006543` `gutendzx/SleePyCo`（REPRESENTATIVE；parent=gist-ailab/SleePyCo） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1162 | `bids-standard/bep028_bidsprov`<br>source=`bids-standard/BEP028_BIDSprov` | `repo-004447` `yarikoptic/BEP028_BIDSprov`（REPRESENTATIVE；parent=bids-standard/BEP028_BIDSprov） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1113–1162`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-027-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
