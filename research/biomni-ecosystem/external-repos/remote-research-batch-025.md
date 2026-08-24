# 远程调研 Batch 025

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1013–1062**；**50** 个 family；**52** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 52 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 1 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 16 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 21 |
| 分类 `LOW_INFORMATION_RECHECK` | 2 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 7 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `FORK_LINEAGE_REQUIRED` | 42 |
| 标记 `LICENSE_UNCLEAR` | 25 |
| 标记 `MULTI_MEMBER_FAMILY` | 2 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1013 | `linkml/pyshex`<br>source=`linkml/PyShEx` | `repo-005433` `yarikoptic/PyShEx`（REPRESENTATIVE；parent=linkml/PyShEx） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1014 | `chahat08/cse564_final_project`<br>source=`Chahat08/CSE564_Final_Project` | `repo-002478` `Chahat08/CSE564_Final_Project`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1015 | `getzze/statannotations`<br>source=`getzze/statannotations` | `repo-006645` `sszhu/statannotations`（REPRESENTATIVE；parent=getzze/statannotations） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1016 | `siavashre/om2bfb`<br>source=`siavashre/OM2BFB` | `repo-006387` `siavashre/OM2BFB`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1017 | `deepmodeling/apex`<br>source=`deepmodeling/APEX` | `repo-007404` `Rasic2/APEX`（REPRESENTATIVE；parent=deepmodeling/APEX） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1018 | `marcosbolanos/meshtree`<br>source=`marcosbolanos/MeshTree` | `repo-001606` `marcosbolanos/MeshTree`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1019 | `yttrilab/b-soid`<br>source=`YttriLab/B-SOID` | `repo-004426` `yarikoptic/B-SOID`（REPRESENTATIVE；parent=YttriLab/B-SOID） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1020 | `keyingkuang/med-real2sim`<br>source=`keyingkuang/Med-Real2Sim` | `repo-006873` `tangxuan82/Med-Real2Sim`（REPRESENTATIVE；parent=keyingkuang/Med-Real2Sim） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1021 | `vocalpy/vocalpy`<br>source=`vocalpy/vocalpy` | `repo-005741` `yarikoptic/vocalpy`（REPRESENTATIVE；parent=vocalpy/vocalpy） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1022 | `jucor/krippendorff`<br>source=`jucor/krippendorff` | `repo-001418` `jucor/krippendorff`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1023 | `aramis-lab/clinica`<br>source=`aramis-lab/clinica` | `repo-004573` `yarikoptic/clinica`（REPRESENTATIVE；parent=aramis-lab/clinica） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1024 | `arcanaframework/arcana`<br>source=`ArcanaFramework/arcana` | `repo-004400` `yarikoptic/arcana`（REPRESENTATIVE；parent=ArcanaFramework/arcana） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1025 | `ianevskialeksandr/sc-type`<br>source=`IanevskiAleksandr/sc-type` | `repo-003081` `Liripo/sc-type`（REPRESENTATIVE；parent=IanevskiAleksandr/sc-type） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1026 | `marcosbolanos/kaggle_medicalpremiums`<br>source=`marcosbolanos/kaggle_medicalPremiums` | `repo-001600` `marcosbolanos/kaggle_medicalPremiums`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1027 | `gsh150801/ai-drug-design`<br>source=`gsh150801/AI-drug-design` | `repo-007173` `leezx/AI-Drug-Discovery-Design`（REPRESENTATIVE；parent=gsh150801/AI-drug-design） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1028 | `datacite/schema`<br>source=`datacite/schema` | `repo-005540` `yarikoptic/schema`（REPRESENTATIVE；parent=datacite/schema） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1029 | `theislab/task-dge-perturbation-prediction-analysis`<br>source=`theislab/task-dge-perturbation-prediction-analysis` | `repo-001360` `HelloWorldLTY/task-dge-perturbation-prediction-analysis`（REPRESENTATIVE；parent=theislab/task-dge-perturbation-prediction-analysis） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1030 | `jannisborn/paperscraper`<br>source=`jannisborn/paperscraper` | `repo-005315` `yarikoptic/paperscraper`（REPRESENTATIVE；parent=jannisborn/paperscraper） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1031 | `bowang-lab/orthrus`<br>source=`bowang-lab/Orthrus` | `repo-001326` `HelloWorldLTY/Orthrus`（REPRESENTATIVE；parent=bowang-lab/Orthrus） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1032 | `bids-standard/bids-schema`<br>source=`bids-standard/bids-schema` | `repo-004467` `yarikoptic/bids-schema`（REPRESENTATIVE；parent=bids-standard/bids-schema） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1033 | `nf-core/variantbenchmarking`<br>source=`nf-core/variantbenchmarking` | `repo-003210` `PabloCabaleiro/variantbenchmarking`（REPRESENTATIVE；parent=nf-core/variantbenchmarking） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1034 | `lujiarui/esmdiff`<br>source=`lujiarui/esmdiff` | `repo-006961` `Vik-u/esmdiff`（REPRESENTATIVE；parent=lujiarui/esmdiff） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1035 | `genentech/grelu`<br>source=`Genentech/gReLU` | `repo-001299` `HelloWorldLTY/gReLU`（REPRESENTATIVE；parent=Genentech/gReLU） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1036 | `athms/learning-from-brains`<br>source=`athms/learning-from-brains` | `repo-005037` `yarikoptic/learning-from-brains`（REPRESENTATIVE；parent=athms/learning-from-brains） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1037 | `aplbrain/neuvue-app`<br>source=`aplbrain/neuvue-app` | `repo-005199` `yarikoptic/neuvue-app`（REPRESENTATIVE；parent=aplbrain/neuvue-app） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1038 | `nipreps/mriqc`<br>source=`nipreps/mriqc` | `repo-005135` `yarikoptic/mriqc`（REPRESENTATIVE；parent=nipreps/mriqc） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1039 | `helloworldlty/geneverse`<br>source=`HelloWorldLTY/Geneverse` | `repo-001291` `HelloWorldLTY/Geneverse`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1040 | `sqaiyy/cimsleepnet`<br>source=`SQAIYY/CIMSleepNet` | `repo-006479` `gutendzx/CIMSleepNet`（REPRESENTATIVE；parent=SQAIYY/CIMSleepNet） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1041 | `quarto-dev/quarto-cli`<br>source=`quarto-dev/quarto-cli` | `repo-005467` `yarikoptic/quarto-cli`（REPRESENTATIVE；parent=quarto-dev/quarto-cli） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1042 | `sulab/drugmechdb`<br>source=`SuLab/DrugMechDB` | `repo-002427` `ahueb/DrugMechDB`（REPRESENTATIVE；parent=SuLab/DrugMechDB）<br>`repo-000909` `andrewsu/DrugMechDB`（MEMBER；parent=SuLab/DrugMechDB） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1043 | `stuchalk/scidata`<br>source=`stuchalk/scidata` | `repo-005547` `yarikoptic/scidata`（REPRESENTATIVE；parent=stuchalk/scidata）<br>`repo-002721` `goodb/scidata`（MEMBER；parent=stuchalk/scidata） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1044 | `borchlab/screpertoire`<br>source=`BorchLab/scRepertoire` | `repo-003085` `Liripo/scRepertoire`（REPRESENTATIVE；parent=BorchLab/scRepertoire） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1045 | `hed-standard/hed-python`<br>source=`hed-standard/hed-python` | `repo-004940` `yarikoptic/hed-python`（REPRESENTATIVE；parent=hed-standard/hed-python） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1046 | `openproblems-bio/openproblems`<br>source=`openproblems-bio/openproblems` | `repo-001325` `HelloWorldLTY/openproblems`（REPRESENTATIVE；parent=openproblems-bio/openproblems） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1047 | `cortex-lab/allenccf`<br>source=`cortex-lab/allenCCF` | `repo-004376` `yarikoptic/allenCCF`（REPRESENTATIVE；parent=cortex-lab/allenCCF） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1048 | `datalad/datalad-extensions`<br>source=`datalad/datalad-extensions` | `repo-004674` `yarikoptic/datalad-extensions`（REPRESENTATIVE；parent=datalad/datalad-extensions） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1049 | `luoxiao12/dance`<br>source=`luoxiao12/DANCE` | `repo-001267` `HelloWorldLTY/DANCE_NIPS2024`（REPRESENTATIVE；parent=luoxiao12/DANCE） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1050 | `liyuesen/druggpt`<br>source=`LIYUESEN/druggpt` | `repo-006850` `tangxuan82/druggpt`（REPRESENTATIVE；parent=LIYUESEN/druggpt） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1051 | `fanglu0411/sgs`<br>source=`fanglu0411/sgs` | `repo-003088` `Liripo/sgs`（REPRESENTATIVE；parent=fanglu0411/sgs） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1052 | `junjunlab/scrnatoolvis`<br>source=`junjunlab/scRNAtoolVis` | `repo-003086` `Liripo/scRNAtoolVis`（REPRESENTATIVE；parent=junjunlab/scRNAtoolVis） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1053 | `paquiteau/patch-denoising`<br>source=`paquiteau/patch-denoising` | `repo-005320` `yarikoptic/patch-denoising`（REPRESENTATIVE；parent=paquiteau/patch-denoising） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1054 | `ncihtan/htan_missing_manual`<br>source=`ncihtan/htan_missing_manual` | `repo-002809` `inodb/htan_missing_manual`（REPRESENTATIVE；parent=ncihtan/htan_missing_manual） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1055 | `ucla-vmg/noncontactapneadetection`<br>source=`UCLA-VMG/NonContactApneaDetection` | `repo-006515` `gutendzx/NonContactApneaDetection`（REPRESENTATIVE；parent=UCLA-VMG/NonContactApneaDetection） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1056 | `samuel-marsh/sccustomize`<br>source=`samuel-marsh/scCustomize` | `repo-003082` `Liripo/scCustomize`（REPRESENTATIVE；parent=samuel-marsh/scCustomize） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1057 | `xcompass-ai/genecompass`<br>source=`xCompass-AI/GeneCompass` | `repo-001289` `HelloWorldLTY/GeneCompass`（REPRESENTATIVE；parent=xCompass-AI/GeneCompass） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1058 | `rasic2/gvaspweb`<br>source=`Rasic2/GVaspWeb` | `repo-007419` `Rasic2/GVaspWeb`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1059 | `biolink/information-resource-registry`<br>source=`biolink/information-resource-registry` | `repo-000918` `andrewsu/information-resource-registry`（REPRESENTATIVE；parent=biolink/information-resource-registry） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`CHILD_FORK_SURFACE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1060 | `bowang-lab/scgpt`<br>source=`bowang-lab/scGPT` | `repo-003083` `Liripo/scGPT`（REPRESENTATIVE；parent=bowang-lab/scGPT） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1061 | `jsunn-y/alde`<br>source=`jsunn-y/ALDE` | `repo-002212` `tuln128/alde_forked`（REPRESENTATIVE；parent=jsunn-y/ALDE） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1062 | `yarikoptic/2024-incf-poster`<br>source=`yarikoptic/2024-incf-poster` | `repo-004343` `yarikoptic/2024-incf-poster`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |

## 完整性边界

- 本文件连续覆盖 orders `1013–1062`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-025-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
