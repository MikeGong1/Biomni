# 远程调研 Batch 026

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1063–1112**；**50** 个 family；**53** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 53 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 1 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 4 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 17 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 16 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 8 |
| 标记 `ARCHIVED_OR_DISABLED` | 1 |
| 标记 `CHILD_FORK_SURFACE` | 4 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 44 |
| 标记 `LICENSE_UNCLEAR` | 18 |
| 标记 `MULTI_MEMBER_FAMILY` | 3 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1063 | `yarikoptic/datalad-core`<br>source=`yarikoptic/datalad-core` | `repo-004669` `yarikoptic/datalad-core`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1064 | `helloworldlty/awesome-dna-language-modelling`<br>source=`HelloWorldLTY/Awesome-DNA-Language-Modelling` | `repo-001255` `HelloWorldLTY/Awesome-DNA-Language-Modelling`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | `LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1065 | `katabigroup/radiosleep`<br>source=`katabigroup/radiosleep` | `repo-006525` `gutendzx/radiosleep`（REPRESENTATIVE；parent=katabigroup/radiosleep） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1066 | `nipreps/nipreps.github.io`<br>source=`nipreps/nipreps.github.io` | `repo-005223` `yarikoptic/nipreps.github.io`（REPRESENTATIVE；parent=nipreps/nipreps.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1067 | `seltepu/updated-drugmap-parser`<br>source=`seltepu/Updated-DrugMAP-Parser` | `repo-000964` `andrewsu/Updated-DrugMAP-Parser`（REPRESENTATIVE；parent=seltepu/Updated-DrugMAP-Parser） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1068 | `repronim/simple2_nidm_examples`<br>source=`ReproNim/simple2_NIDM_examples` | `repo-005578` `yarikoptic/simple2_NIDM_examples`（REPRESENTATIVE；parent=ReproNim/simple2_NIDM_examples） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1069 | `alexandrovteam/spacem`<br>source=`alexandrovteam/SpaceM` | `repo-006791` `drgmk/SpaceM`（REPRESENTATIVE；parent=alexandrovteam/SpaceM） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1070 | `dandi/dandisets-linkml-status-tools`<br>source=`dandi/dandisets-linkml-status-tools` | `repo-004645` `yarikoptic/dandisets-linkml-status-tools`（REPRESENTATIVE；parent=dandi/dandisets-linkml-status-tools） | `EMPTY_OR_MINIMAL` | `FORK_LINEAGE_REQUIRED`、`EMPTY_OR_MINIMAL` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 1071 | `pinellolab/epinformer`<br>source=`pinellolab/EPInformer` | `repo-001283` `HelloWorldLTY/EPInformer`（REPRESENTATIVE；parent=pinellolab/EPInformer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1072 | `ome/ngff`<br>source=`ome/ngff` | `repo-005202` `yarikoptic/ngff`（REPRESENTATIVE；parent=ome/ngff） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1073 | `ncatstranslator/translatortechnicaldocumentation`<br>source=`NCATSTranslator/TranslatorTechnicalDocumentation` | `repo-000963` `andrewsu/TranslatorTechnicalDocumentation`（REPRESENTATIVE；parent=NCATSTranslator/TranslatorTechnicalDocumentation） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1074 | `biothings/biothings_explorer`<br>source=`biothings/biothings_explorer` | `repo-002426` `ahueb/biothings_explorer`（REPRESENTATIVE；parent=biothings/biothings_explorer）<br>`repo-000897` `andrewsu/biothings_explorer`（MEMBER；parent=biothings/biothings_explorer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1075 | `simula-complex/medet`<br>source=`Simula-COMPLEX/MeDeT` | `repo-006874` `tangxuan82/MeDeT`（REPRESENTATIVE；parent=Simula-COMPLEX/MeDeT） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1076 | `childmindresearch/bids2table`<br>source=`childmindresearch/bids2table` | `repo-004477` `yarikoptic/bids2table`（REPRESENTATIVE；parent=childmindresearch/bids2table） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1077 | `genomicsstandardsconsortium/mixs`<br>source=`GenomicsStandardsConsortium/mixs` | `repo-005108` `yarikoptic/mixs`（REPRESENTATIVE；parent=GenomicsStandardsConsortium/mixs） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1078 | `tiroshlab/3ca`<br>source=`tiroshlab/3ca` | `repo-007169` `leezx/3ca`（REPRESENTATIVE；parent=tiroshlab/3ca） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1079 | `brainlife/docs`<br>source=`brainlife/docs` | `repo-004743` `yarikoptic/docs-2`（REPRESENTATIVE；parent=brainlife/docs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1080 | `openjournals/joss`<br>source=`openjournals/joss` | `repo-004998` `yarikoptic/joss`（REPRESENTATIVE；parent=openjournals/joss） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1081 | `mr-milk/spatialtis`<br>source=`Mr-Milk/SpatialTis` | `repo-003153` `Mr-Milk/SpatialTis`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1082 | `sage-bionetworks-workflows/nf-synapse`<br>source=`Sage-Bionetworks-Workflows/nf-synapse` | `repo-007095` `jaybee84/nf-synapse`（REPRESENTATIVE；parent=Sage-Bionetworks-Workflows/nf-synapse） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1083 | `wheretrue/biobear`<br>source=`wheretrue/biobear` | `repo-003053` `Liripo/biobear`（REPRESENTATIVE；parent=wheretrue/biobear） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1084 | `saraaghamiri/digital-twins-in-healthcare`<br>source=`SaraAghamiri/Digital-Twins-in-Healthcare` | `repo-006846` `tangxuan82/Digital-Twins-in-Healthcare`（REPRESENTATIVE；parent=SaraAghamiri/Digital-Twins-in-Healthcare） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1085 | `magics-lab/dnabert_s`<br>source=`MAGICS-LAB/DNABERT_S` | `repo-001276` `HelloWorldLTY/DNABERT_S`（REPRESENTATIVE；parent=MAGICS-LAB/DNABERT_S）<br>`repo-007074` `jaybee84/DNABERT_S`（MEMBER；parent=MAGICS-LAB/DNABERT_S） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1086 | `sage-bionetworks/scicomp-provisioner`<br>source=`Sage-Bionetworks/scicomp-provisioner` | `repo-007122` `jaybee84/scicomp-provisioner`（REPRESENTATIVE；parent=Sage-Bionetworks/scicomp-provisioner） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1087 | `vector-engineering/fit4function`<br>source=`vector-engineering/fit4function` | `repo-006855` `tangxuan82/fit4function`（REPRESENTATIVE；parent=vector-engineering/fit4function） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1088 | `frederikkemarin/bend`<br>source=`frederikkemarin/BEND` | `repo-001258` `HelloWorldLTY/BEND`（REPRESENTATIVE；parent=frederikkemarin/BEND） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1089 | `kosonocky/bits-to-binders-resources`<br>source=`kosonocky/bits-to-binders-resources` | `repo-002148` `th86/bits-to-binders-resources`（REPRESENTATIVE；parent=kosonocky/bits-to-binders-resources） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1090 | `pku-yuangroup/taxdiff`<br>source=`PKU-YuanGroup/TaxDiff` | `repo-006899` `tangxuan82/TaxDiff`（REPRESENTATIVE；parent=PKU-YuanGroup/TaxDiff） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1091 | `inria-empenn/reproducibility-biblio`<br>source=`Inria-Empenn/reproducibility-biblio` | `repo-005495` `yarikoptic/reproducibility-biblio`（REPRESENTATIVE；parent=Inria-Empenn/reproducibility-biblio） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1092 | `wieluk/psychopy_linux_installer`<br>source=`wieluk/psychopy_linux_installer` | `repo-005384` `yarikoptic/psychopy_linux_installer`（REPRESENTATIVE；parent=wieluk/psychopy_linux_installer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1093 | `physiopy/physioqc`<br>source=`physiopy/physioqc` | `repo-005337` `yarikoptic/physioqc`（REPRESENTATIVE；parent=physiopy/physioqc） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1094 | `biagent-dev/bia`<br>source=`biagent-dev/bia` | `repo-006391` `Vincentcchu/bia`（REPRESENTATIVE；parent=biagent-dev/bia） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1095 | `openjournals/buffy`<br>source=`openjournals/buffy` | `repo-004520` `yarikoptic/buffy`（REPRESENTATIVE；parent=openjournals/buffy） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1096 | `siavashre/crisprcatch`<br>source=`siavashre/CRISPRCATCH` | `repo-006385` `siavashre/CRISPRCATCH`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1097 | `dandi/s3-log-extraction`<br>source=`dandi/s3-log-extraction` | `repo-004640` `yarikoptic/dandi_s3_log_parser`（REPRESENTATIVE；parent=dandi/s3-log-extraction） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1098 | `bulik/ldsc`<br>source=`bulik/ldsc` | `repo-001308` `HelloWorldLTY/ldsc`（REPRESENTATIVE；parent=bulik/ldsc）<br>`repo-006062` `explorerwjy/ldsc`（MEMBER；parent=bulik/ldsc） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1099 | `sanat-mishra/sheltzer-lab-fusions-analysis`<br>source=`Sanat-Mishra/Sheltzer-Lab-Fusions-Analysis` | `repo-007453` `Sanat-Mishra/Sheltzer-Lab-Fusions-Analysis`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1100 | `neurodatawithoutborders/nwbinspector`<br>source=`NeurodataWithoutBorders/nwbinspector` | `repo-005260` `yarikoptic/nwbinspector`（REPRESENTATIVE；parent=NeurodataWithoutBorders/nwbinspector） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1101 | `martinjzhang/scdrs`<br>source=`martinjzhang/scDRS` | `repo-001337` `HelloWorldLTY/scDRS`（REPRESENTATIVE；parent=martinjzhang/scDRS） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1102 | `evanpeikon/blast`<br>source=`evanpeikon/BLAST` | `repo-005886` `dabulseco/BLAST`（REPRESENTATIVE；parent=evanpeikon/BLAST） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1103 | `bids-standard/bids-starter-kit`<br>source=`bids-standard/bids-starter-kit` | `repo-004469` `yarikoptic/bids-starter-kit`（REPRESENTATIVE；parent=bids-standard/bids-starter-kit） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1104 | `oshlack/jaffa`<br>source=`Oshlack/JAFFA` | `repo-007446` `Sanat-Mishra/JAFFA`（REPRESENTATIVE；parent=Oshlack/JAFFA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1105 | `repronim/reproschema-ui`<br>source=`ReproNim/reproschema-ui` | `repo-005504` `yarikoptic/reproschema-ui`（REPRESENTATIVE；parent=ReproNim/reproschema-ui） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1106 | `helixonprotein/omegafold`<br>source=`HeliXonProtein/OmegaFold` | `repo-006275` `alexj-lee/OmegaFold`（REPRESENTATIVE；parent=HeliXonProtein/OmegaFold） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1107 | `leezx/bt2m`<br>source=`leezx/bt2m` | `repo-007178` `leezx/bt2m`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | 无额外标记 | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1108 | `luwei0917/dynamicbind`<br>source=`luwei0917/DynamicBind` | `repo-007152` `KSUN63/DynamicBind`（REPRESENTATIVE；parent=luwei0917/DynamicBind） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1109 | `spack/spack`<br>source=`spack/spack` | `repo-004159` `vladsavelyev/spack`（REPRESENTATIVE；parent=spack/spack） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1110 | `shintarominami/pydssp`<br>source=`ShintaroMinami/PyDSSP` | `repo-006280` `alexj-lee/PyDSSP`（REPRESENTATIVE；parent=ShintaroMinami/PyDSSP） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1111 | `dpeerlab/spectra`<br>source=`dpeerlab/spectra` | `repo-002862` `inodb/spectra`（REPRESENTATIVE；parent=dpeerlab/spectra） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1112 | `camaralab/cajal`<br>source=`CamaraLab/CAJAL` | `repo-004531` `yarikoptic/CAJAL`（REPRESENTATIVE；parent=CamaraLab/CAJAL） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1063–1112`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-026-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
