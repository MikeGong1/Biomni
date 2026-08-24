# 远程调研 Batch 023

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **913–962**；**50** 个 family；**51** 条 bounded repository records。

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
| 分类 `EMPTY_OR_MINIMAL` | 2 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 19 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 17 |
| 分类 `LOW_INFORMATION_RECHECK` | 1 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 6 |
| 标记 `EMPTY_OR_MINIMAL` | 2 |
| 标记 `FORK_LINEAGE_REQUIRED` | 42 |
| 标记 `LICENSE_UNCLEAR` | 20 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RECENT_ACTIVE` | 50 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 913 | `flatironinstitute/neurosift`<br>source=`flatironinstitute/neurosift` | `repo-005192` `yarikoptic/neurosift`（REPRESENTATIVE；parent=flatironinstitute/neurosift） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 914 | `dandi/llm-analysis`<br>source=`dandi/llm-analysis` | `repo-005057` `yarikoptic/llm-analysis`（REPRESENTATIVE；parent=dandi/llm-analysis） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 915 | `catalystneuro/dandi_llms`<br>source=`catalystneuro/dandi_llms` | `repo-004639` `yarikoptic/dandi_llms`（REPRESENTATIVE；parent=catalystneuro/dandi_llms） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 916 | `geoheil/molgrapher`<br>source=`geoHeil/MolGrapher` | `repo-001677` `nevergreendd/MolGrapher`（REPRESENTATIVE；parent=geoHeil/MolGrapher） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 917 | `molecule-generator-collection/chatchemts`<br>source=`molecule-generator-collection/ChatChemTS` | `repo-005891` `dabulseco/ChatChemTS`（REPRESENTATIVE；parent=molecule-generator-collection/ChatChemTS） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 918 | `brianhie/efficient-evolution`<br>source=`brianhie/efficient-evolution` | `repo-001536` `kuanlinhuang/efficient-evolution`（REPRESENTATIVE；parent=brianhie/efficient-evolution） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 919 | `mkoretsky1/drugbank_indexing`<br>source=`mkoretsky1/drugbank_indexing` | `repo-003102` `mkoretsky1/drugbank_indexing`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 920 | `databiosphere/dsub`<br>source=`DataBiosphere/dsub` | `repo-004766` `yarikoptic/dsub`（REPRESENTATIVE；parent=DataBiosphere/dsub） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 921 | `osfclient/osfclient`<br>source=`osfclient/osfclient` | `repo-005301` `yarikoptic/osfclient`（REPRESENTATIVE；parent=osfclient/osfclient） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 922 | `bioconductor/biocedam`<br>source=`Bioconductor/biocEDAM` | `repo-000974` `anngvu/biocEDAM`（REPRESENTATIVE；parent=Bioconductor/biocEDAM） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 923 | `ayushmaniar/telomere_analysis_cse280a`<br>source=`Ayushmaniar/telomere_analysis_cse280a` | `repo-002454` `Ayushmaniar/telomere_analysis_cse280a`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 924 | `joe-lin-tech/emg2qwerty`<br>source=`joe-lin-tech/emg2qwerty` | `repo-007528` `HNO333333/247-project`（REPRESENTATIVE；parent=joe-lin-tech/emg2qwerty） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 925 | `bids-standard/bids2nda`<br>source=`bids-standard/bids2nda` | `repo-004475` `yarikoptic/BIDS2NDA`（REPRESENTATIVE；parent=bids-standard/bids2nda） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 926 | `vandermeerlab/mvdmlab_npx_to_nwb`<br>source=`vandermeerlab/mvdmlab_npx_to_nwb` | `repo-005142` `yarikoptic/mvdmlab_npx_to_nwb`（REPRESENTATIVE；parent=vandermeerlab/mvdmlab_npx_to_nwb） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 927 | `genentech/reglm`<br>source=`Genentech/regLM` | `repo-001332` `HelloWorldLTY/regLM`（REPRESENTATIVE；parent=Genentech/regLM） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 928 | `labstreaminglayer/pylsl`<br>source=`labstreaminglayer/pylsl` | `repo-005418` `yarikoptic/pylsl`（REPRESENTATIVE；parent=labstreaminglayer/pylsl） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 929 | `chatmol/gromacs_copilot`<br>source=`ChatMol/gromacs_copilot` | `repo-006964` `Vik-u/gromacs_copilot`（REPRESENTATIVE；parent=ChatMol/gromacs_copilot） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 930 | `nipy/heudiconv`<br>source=`nipy/heudiconv` | `repo-004946` `yarikoptic/heudiconv`（REPRESENTATIVE；parent=nipy/heudiconv） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 931 | `neurodebian/dockerfiles`<br>source=`neurodebian/dockerfiles` | `repo-004739` `yarikoptic/dockerfiles`（REPRESENTATIVE；parent=neurodebian/dockerfiles） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 932 | `openneuroorg/openneuro`<br>source=`OpenNeuroOrg/openneuro` | `repo-005288` `yarikoptic/openneuro`（REPRESENTATIVE；parent=OpenNeuroOrg/openneuro） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 933 | `priyanka9991/mutation_interpolation`<br>source=`priyanka9991/Mutation_Interpolation` | `repo-006158` `zhuyitan/Mutation_Interpolation`（REPRESENTATIVE；parent=priyanka9991/Mutation_Interpolation） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 934 | `niivue/niivue-vscode`<br>source=`niivue/niivue-vscode` | `repo-005219` `yarikoptic/niivue-vscode`（REPRESENTATIVE；parent=niivue/niivue-vscode） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 935 | `donders-institute/bidscoin`<br>source=`Donders-Institute/bidscoin` | `repo-004479` `yarikoptic/bidscoin`（REPRESENTATIVE；parent=Donders-Institute/bidscoin） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 936 | `napari/docs`<br>source=`napari/docs` | `repo-004746` `yarikoptic/docs-5`（REPRESENTATIVE；parent=napari/docs） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 937 | `marcosbolanos/ped-t1d-model`<br>source=`marcosbolanos/ped-t1d-model` | `repo-001613` `marcosbolanos/ped-t1d-model`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 938 | `mobaidoctor/med-ddpm`<br>source=`mobaidoctor/med-ddpm` | `repo-005835` `yaswanth169/med-ddpm`（REPRESENTATIVE；parent=mobaidoctor/med-ddpm） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 939 | `hed-standard/hed-specification`<br>source=`hed-standard/hed-specification` | `repo-004942` `yarikoptic/hed-specification`（REPRESENTATIVE；parent=hed-standard/hed-specification） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 940 | `mahmoodlab/trident`<br>source=`mahmoodlab/TRIDENT` | `repo-001712` `Pidem/TRIDENT`（REPRESENTATIVE；parent=mahmoodlab/TRIDENT） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 941 | `div0-space/vistacare.ai`<br>source=`div0-space/vistacare.ai` | `repo-007398` `div0-space/vistacare.ai`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL`、`RECENT_ACTIVE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 942 | `phewas/phewas`<br>source=`PheWAS/PheWAS` | `repo-006642` `sszhu/PheWAS`（REPRESENTATIVE；parent=PheWAS/PheWAS） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 943 | `mathonco/valis`<br>source=`MathOnco/valis` | `repo-005726` `yarikoptic/valis`（REPRESENTATIVE；parent=MathOnco/valis） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 944 | `auto-pi-lot/autopilot`<br>source=`auto-pi-lot/autopilot` | `repo-004416` `yarikoptic/autopilot`（REPRESENTATIVE；parent=auto-pi-lot/autopilot） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 945 | `priyanka9991/digital_pathology_feature-extraction`<br>source=`priyanka9991/Digital_Pathology_feature-extraction` | `repo-006153` `zhuyitan/Digital_Pathology_feature-extraction`（REPRESENTATIVE；parent=priyanka9991/Digital_Pathology_feature-extraction） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 946 | `deeplabcut/deeplabcut`<br>source=`DeepLabCut/DeepLabCut` | `repo-004706` `yarikoptic/DeepLabCut`（REPRESENTATIVE；parent=DeepLabCut/DeepLabCut）<br>`repo-007232` `manu-tej/DeepLabCut`（MEMBER；parent=DeepLabCut/DeepLabCut） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 947 | `priyanka9991/pdxnet_preprocessing_wsitools`<br>source=`priyanka9991/pdxnet_preprocessing_WSITools` | `repo-006159` `zhuyitan/pdxnet_preprocessing_WSITools`（REPRESENTATIVE；parent=priyanka9991/pdxnet_preprocessing_WSITools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 948 | `repronim/reproman`<br>source=`ReproNim/reproman` | `repo-005501` `yarikoptic/ReproNim`（REPRESENTATIVE；parent=ReproNim/reproman） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 949 | `knuedd/datalad-slurm`<br>source=`knuedd/datalad-slurm` | `repo-004685` `yarikoptic/datalad-slurm`（REPRESENTATIVE；parent=knuedd/datalad-slurm） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 950 | `div0-space/medical-data-fusion`<br>source=`div0-space/medical-data-fusion` | `repo-007391` `div0-space/medical-data-fusion`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL`、`RECENT_ACTIVE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 951 | `quarto-dev/quarto`<br>source=`quarto-dev/quarto` | `repo-005466` `yarikoptic/quarto`（REPRESENTATIVE；parent=quarto-dev/quarto） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 952 | `epam/miew`<br>source=`epam/miew` | `repo-005941` `dabulseco/miew`（REPRESENTATIVE；parent=epam/miew） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 953 | `dandi/dandi-cli`<br>source=`dandi/dandi-cli` | `repo-004635` `yarikoptic/dandi-cli`（REPRESENTATIVE；parent=dandi/dandi-cli） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 954 | `devindesilva/doctorassist`<br>source=`DevinDeSilva/DoctorAssist` | `repo-006010` `DevinDeSilva/DoctorAssist`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 955 | `zhuyitan/drug_screening_data_processing`<br>source=`zhuyitan/Drug_Screening_Data_Processing` | `repo-006154` `zhuyitan/Drug_Screening_Data_Processing`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 956 | `openlists/electrophysiologydata`<br>source=`openlists/ElectrophysiologyData` | `repo-004784` `yarikoptic/ElectrophysiologyData`（REPRESENTATIVE；parent=openlists/ElectrophysiologyData） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 957 | `nkalavros/deepseekclinvar`<br>source=`NKalavros/DeepSeekClinVar` | `repo-007264` `NKalavros/DeepSeekClinVar`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 958 | `psych-ds/psych-ds`<br>source=`psych-ds/psych-DS` | `repo-005381` `yarikoptic/psych-DS`（REPRESENTATIVE；parent=psych-ds/psych-DS） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 959 | `repronim/segstats_jsonld`<br>source=`ReproNim/segstats_jsonld` | `repo-005562` `yarikoptic/segstats_jsonld`（REPRESENTATIVE；parent=ReproNim/segstats_jsonld） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 960 | `phewas/phecodex`<br>source=`PheWAS/PhecodeX` | `repo-006641` `sszhu/PhecodeX`（REPRESENTATIVE；parent=PheWAS/PhecodeX） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 961 | `lingxusb/plasmidgpt`<br>source=`lingxusb/PlasmidGPT` | `repo-005965` `dabulseco/PlasmidGPT`（REPRESENTATIVE；parent=lingxusb/PlasmidGPT） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 962 | `cpernet/metaprivbids`<br>source=`CPernet/metaprivBIDS` | `repo-005096` `yarikoptic/metaprivBIDS`（REPRESENTATIVE；parent=CPernet/metaprivBIDS） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `913–962`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-023-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
