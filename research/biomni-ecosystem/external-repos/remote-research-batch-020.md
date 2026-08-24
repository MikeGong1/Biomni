# 远程调研 Batch 020

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **763–812**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `DATASET_OR_BENCHMARK` | 2 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 11 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 23 |
| 分类 `LOW_INFORMATION_RECHECK` | 5 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 9 |
| 标记 `CHILD_FORK_SURFACE` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 42 |
| 标记 `LICENSE_UNCLEAR` | 22 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RECENT_ACTIVE` | 50 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 763 | `zhuangzx1127/ressleepnet`<br>source=`zhuangzx1127/ResSleepNet` | `repo-006529` `gutendzx/ResSleepNet`（REPRESENTATIVE；parent=zhuangzx1127/ResSleepNet） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 764 | `mims-harvard/txagent`<br>source=`mims-harvard/TxAgent` | `repo-006368` `Ali-Maq/TxAgent`（REPRESENTATIVE；parent=mims-harvard/TxAgent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 765 | `dreem-organization/dreem-learning-open`<br>source=`Dreem-Organization/dreem-learning-open` | `repo-006492` `gutendzx/dreem-learning-open`（REPRESENTATIVE；parent=Dreem-Organization/dreem-learning-open） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 766 | `graph-and-geometric-learning/stpath`<br>source=`Graph-and-Geometric-Learning/STPath` | `repo-001356` `HelloWorldLTY/STPath`（REPRESENTATIVE；parent=Graph-and-Geometric-Learning/STPath） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 767 | `s-ccs/lslautobids`<br>source=`s-ccs/LSLAutoBIDS` | `repo-005066` `yarikoptic/LSLAutoBIDS`（REPRESENTATIVE；parent=s-ccs/LSLAutoBIDS） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 768 | `kaczmarj/mako`<br>source=`kaczmarj/MAKO` | `repo-006871` `tangxuan82/MAKO`（REPRESENTATIVE；parent=kaczmarj/MAKO） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 769 | `nkalavros/dspyedam`<br>source=`NKalavros/DSPyEDAM` | `repo-007267` `NKalavros/DSPyEDAM`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 770 | `salhik/biomni_tests`<br>source=`SALhik/Biomni_tests` | `repo-001780` `SALhik/Biomni_tests`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 771 | `helloworldlty/superglue`<br>source=`HelloWorldLTY/SuperGLUE` | `repo-001357` `HelloWorldLTY/SuperGLUE`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 772 | `internscience/internagent`<br>source=`InternScience/InternAgent` | `repo-001305` `HelloWorldLTY/InternAgent`（REPRESENTATIVE；parent=InternScience/InternAgent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 773 | `helloworldlty/dnaclip`<br>source=`HelloWorldLTY/DNACLIP` | `repo-001277` `HelloWorldLTY/DNACLIP`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 774 | `physicell-models/grammar_samples`<br>source=`PhysiCell-Models/grammar_samples` | `repo-001298` `HelloWorldLTY/grammar_samples`（REPRESENTATIVE；parent=PhysiCell-Models/grammar_samples） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 775 | `yxwucq/scextract`<br>source=`yxwucq/scExtract` | `repo-006404` `Vincentcchu/scExtract`（REPRESENTATIVE；parent=yxwucq/scExtract） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 776 | `xiaobaben/brainuicl`<br>source=`xiaobaben/BrainUICL` | `repo-006474` `gutendzx/BrainUICL`（REPRESENTATIVE；parent=xiaobaben/BrainUICL） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 777 | `terryso/claude-code-playwright-mcp-test`<br>source=`terryso/claude-code-playwright-mcp-test` | `repo-004559` `yarikoptic/claude-code-playwright-mcp-test`（REPRESENTATIVE；parent=terryso/claude-code-playwright-mcp-test） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 778 | `rosettacommons/rfdiffusion`<br>source=`RosettaCommons/RFdiffusion` | `repo-002197` `th86/RFdiffusion`（REPRESENTATIVE；parent=RosettaCommons/RFdiffusion）<br>`repo-007003` `Vik-u/RFdiffusion`（MEMBER；parent=RosettaCommons/RFdiffusion） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 779 | `nkalavros/scmedaltpy`<br>source=`NKalavros/scMEDALTpy` | `repo-007290` `NKalavros/scMEDALTpy`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 780 | `andem25/server-dt-smart-home-health`<br>source=`andem25/Server-DT-Smart-Home-Health` | `repo-006891` `tangxuan82/Server-DT-Smart-Home-Health`（REPRESENTATIVE；parent=andem25/Server-DT-Smart-Home-Health） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 781 | `ml2health/ml2clinicaltrials`<br>source=`ML2Health/ML2ClinicalTrials` | `repo-002119` `shengyongniu/ML2ClinicalTrials`（REPRESENTATIVE；parent=ML2Health/ML2ClinicalTrials） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 782 | `aeon-toolkit/aeon`<br>source=`aeon-toolkit/aeon` | `repo-004358` `yarikoptic/aeon`（REPRESENTATIVE；parent=aeon-toolkit/aeon） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 783 | `fieldtrip/fieldtrip`<br>source=`fieldtrip/fieldtrip` | `repo-004818` `yarikoptic/fieldtrip`（REPRESENTATIVE；parent=fieldtrip/fieldtrip） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 784 | `physiopy/prep4phys`<br>source=`physiopy/prep4phys` | `repo-005362` `yarikoptic/prep4phys`（REPRESENTATIVE；parent=physiopy/prep4phys） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 785 | `biocypher/biochatter`<br>source=`biocypher/biochatter` | `repo-005883` `dabulseco/biochatter`（REPRESENTATIVE；parent=biocypher/biochatter） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 786 | `codemeta/codemeta`<br>source=`codemeta/codemeta` | `repo-004577` `yarikoptic/codemeta`（REPRESENTATIVE；parent=codemeta/codemeta） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 787 | `patchouli-m/sequencingcancerfinder`<br>source=`Patchouli-M/SequencingCancerFinder` | `repo-003017` `KalinNonchev/SequencingCancerFinder`（REPRESENTATIVE；parent=Patchouli-M/SequencingCancerFinder） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 788 | `antibodyengineers/2024-antibodies-and-ai`<br>source=`AntibodyEngineers/2024-Antibodies-and-AI` | `repo-005862` `dabulseco/2024-Antibodies-and-AI`（REPRESENTATIVE；parent=AntibodyEngineers/2024-Antibodies-and-AI） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 789 | `helloworldlty/muse-gnn`<br>source=`HelloWorldLTY/MuSe-GNN` | `repo-001319` `HelloWorldLTY/MuSe-GNN`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 790 | `fdu-harry/apnea-interact-xplainer`<br>source=`fdu-harry/Apnea-Interact-Xplainer` | `repo-006466` `gutendzx/Apnea-Interact-Xplainer`（REPRESENTATIVE；parent=fdu-harry/Apnea-Interact-Xplainer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 791 | `oloff2005/human_digital_twin`<br>source=`Oloff2005/Human_Digital_twin` | `repo-006861` `tangxuan82/Human_Digital_twin`（REPRESENTATIVE；parent=Oloff2005/Human_Digital_twin） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 792 | `broadinstitute/cellpainting-gallery`<br>source=`broadinstitute/cellpainting-gallery` | `repo-007557` `xinwuye/cellpainting-gallery`（REPRESENTATIVE；parent=broadinstitute/cellpainting-gallery） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 793 | `marcosbolanos/case-lucis`<br>source=`marcosbolanos/Case-Lucis` | `repo-001591` `marcosbolanos/Case-Lucis`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 794 | `australian-imaging-service/pipelines`<br>source=`Australian-Imaging-Service/pipelines` | `repo-005342` `yarikoptic/pipelines`（REPRESENTATIVE；parent=Australian-Imaging-Service/pipelines） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 795 | `antimatter15/reverse-engineering-gemma-3n`<br>source=`antimatter15/reverse-engineering-gemma-3n` | `repo-006357` `Ali-Maq/reverse-engineering-gemma-3n`（REPRESENTATIVE；parent=antimatter15/reverse-engineering-gemma-3n） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 796 | `sage-bionetworks-it/openchallenges`<br>source=`Sage-Bionetworks-IT/openchallenges` | `repo-007353` `tschaffter/openchallenges-aws-cdk`（REPRESENTATIVE；parent=Sage-Bionetworks-IT/openchallenges） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 797 | `openssbd/bdz`<br>source=`openssbd/bdz` | `repo-004441` `yarikoptic/bdz`（REPRESENTATIVE；parent=openssbd/bdz） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 798 | `vandijklab/cell2sentence`<br>source=`vandijklab/cell2sentence` | `repo-006299` `Ali-Maq/cell2sentence`（REPRESENTATIVE；parent=vandijklab/cell2sentence） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 799 | `yuty2009/sleepgpt`<br>source=`yuty2009/sleepgpt` | `repo-006538` `gutendzx/sleepgpt`（REPRESENTATIVE；parent=yuty2009/sleepgpt） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 800 | `docling-project/docling-mcp`<br>source=`docling-project/docling-mcp` | `repo-002397` `aevo98765/docling-mcp`（REPRESENTATIVE；parent=docling-project/docling-mcp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 801 | `oraios/serena`<br>source=`oraios/serena` | `repo-005565` `yarikoptic/serena`（REPRESENTATIVE；parent=oraios/serena） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 802 | `ohba-analysis/osl-dynamics`<br>source=`OHBA-analysis/osl-dynamics` | `repo-005302` `yarikoptic/osl-dynamics`（REPRESENTATIVE；parent=OHBA-analysis/osl-dynamics） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 803 | `garciadias/neuroharmony`<br>source=`garciadias/Neuroharmony` | `repo-005187` `yarikoptic/Neuroharmony`（REPRESENTATIVE；parent=garciadias/Neuroharmony） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 804 | `repronim/reproinventory`<br>source=`ReproNim/ReproInventory` | `repo-005499` `yarikoptic/ReproInventory`（REPRESENTATIVE；parent=ReproNim/ReproInventory） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 805 | `marcosbolanos/frenchpharmakg`<br>source=`marcosbolanos/FrenchPharmaKG` | `repo-001598` `marcosbolanos/FrenchPharmaKG`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 806 | `andrewjahn/andysbrainbook`<br>source=`andrewjahn/AndysBrainBook` | `repo-004385` `yarikoptic/AndysBrainBook`（REPRESENTATIVE；parent=andrewjahn/AndysBrainBook） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 807 | `cmd-ntrf/jupyter-lmod`<br>source=`cmd-ntrf/jupyter-lmod` | `repo-005002` `yarikoptic/jupyter-lmod`（REPRESENTATIVE；parent=cmd-ntrf/jupyter-lmod） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 808 | `neurodesk/example-notebooks`<br>source=`neurodesk/example-notebooks` | `repo-004797` `yarikoptic/example-notebooks`（REPRESENTATIVE；parent=neurodesk/example-notebooks） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 809 | `pathintegral-institute/mcp.science`<br>source=`pathintegral-institute/mcp.science` | `repo-002116` `shengyongniu/mcp.science`（REPRESENTATIVE；parent=pathintegral-institute/mcp.science） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 810 | `neurostuff/neurostore`<br>source=`neurostuff/neurostore` | `repo-005195` `yarikoptic/neurostore`（REPRESENTATIVE；parent=neurostuff/neurostore） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 811 | `wheelocklab/networklevelanalysis`<br>source=`WheelockLab/NetworkLevelAnalysis` | `repo-005165` `yarikoptic/NetworkLevelAnalysis`（REPRESENTATIVE；parent=WheelockLab/NetworkLevelAnalysis） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 812 | `executeautomation/mcp-playwright`<br>source=`executeautomation/mcp-playwright` | `repo-005084` `yarikoptic/mcp-playwright`（REPRESENTATIVE；parent=executeautomation/mcp-playwright） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `763–812`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-020-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
