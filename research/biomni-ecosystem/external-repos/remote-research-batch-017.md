# 远程调研 Batch 017

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **613–662**；**50** 个 family；**56** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 56 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 2 |
| 分类 `DATASET_OR_BENCHMARK` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 12 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 21 |
| 分类 `LOW_INFORMATION_RECHECK` | 5 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 9 |
| 标记 `CHILD_FORK_SURFACE` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 38 |
| 标记 `LICENSE_UNCLEAR` | 20 |
| 标记 `MULTI_MEMBER_FAMILY` | 4 |
| 标记 `RECENT_ACTIVE` | 50 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 613 | `edison-a-n/mcp-garden`<br>source=`Edison-A-N/mcp-garden` | `repo-001032` `Edison-A-N/mcp-garden`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 614 | `ibm/mcp`<br>source=`IBM/mcp` | `repo-002410` `aevo98765/mcp`（REPRESENTATIVE；parent=IBM/mcp） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 615 | `cantinilab/scprint`<br>source=`cantinilab/scPRINT` | `repo-006889` `tangxuan82/scPRINT`（REPRESENTATIVE；parent=cantinilab/scPRINT） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 616 | `martinpacesa/bindcraft`<br>source=`martinpacesa/BindCraft` | `repo-001589` `marcosbolanos/BindCraft`（REPRESENTATIVE；parent=martinpacesa/BindCraft）<br>`repo-002146` `th86/BindCraft`（MEMBER；parent=martinpacesa/BindCraft）<br>`repo-003924` `samarth-kadaba/BindCraft`（MEMBER；parent=martinpacesa/BindCraft） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 617 | `aertslab/scenicplus`<br>source=`aertslab/scenicplus` | `repo-007388` `b-snel/scenicplus`（REPRESENTATIVE；parent=aertslab/scenicplus） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 618 | `python-ai-solutions/agentic-neurodata-conversion`<br>source=`Python-AI-Solutions/agentic-neurodata-conversion` | `repo-004364` `yarikoptic/agentic-neurodata-conversion`（REPRESENTATIVE；parent=Python-AI-Solutions/agentic-neurodata-conversion） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 619 | `mouseland/facemap`<br>source=`MouseLand/facemap` | `repo-004811` `yarikoptic/facemap`（REPRESENTATIVE；parent=MouseLand/facemap） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 620 | `samarth-kadaba/car-tpa`<br>source=`samarth-kadaba/CAR-TPA` | `repo-003925` `samarth-kadaba/CAR-TPA`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 621 | `erikhartman/fk-rfdiffusion`<br>source=`ErikHartman/FK-RFdiffusion` | `repo-006963` `Vik-u/fk-rfdiffusion`（REPRESENTATIVE；parent=ErikHartman/FK-RFdiffusion） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 622 | `helloworldlty/baitsao`<br>source=`HelloWorldLTY/BAITSAO` | `repo-001257` `HelloWorldLTY/BAITSAO`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 623 | `nigmat-future/agenticbioanalysis`<br>source=`Nigmat-future/AgenticBioAnalysis` | `repo-003169` `Nigmat-future/AgenticBioAnalysis`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 624 | `zotero/zotero-google-docs-integration`<br>source=`zotero/zotero-google-docs-integration` | `repo-005787` `yarikoptic/zotero-google-docs-integration`（REPRESENTATIVE；parent=zotero/zotero-google-docs-integration） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 625 | `qpdcdp/synthpert`<br>source=`qpdcdp/SynthPert` | `repo-006897` `tangxuan82/SynthPert`（REPRESENTATIVE；parent=qpdcdp/SynthPert） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 626 | `neuroailab/spelkebench`<br>source=`neuroailab/SpelkeBench` | `repo-003314` `Rakshitha-Ireddi/SpelkeBench`（REPRESENTATIVE；parent=neuroailab/SpelkeBench） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 627 | `qwenlm/qwen-agent`<br>source=`QwenLM/Qwen-Agent` | `repo-006354` `Ali-Maq/Qwen-Agent`（REPRESENTATIVE；parent=QwenLM/Qwen-Agent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 628 | `regro-cf-autotick-bot/wsidata-feedstock`<br>source=`regro-cf-autotick-bot/wsidata-feedstock` | `repo-003166` `Mr-Milk/wsidata-feedstock`（REPRESENTATIVE；parent=regro-cf-autotick-bot/wsidata-feedstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 629 | `allenneuraldynamics/aind-ephys-curation`<br>source=`AllenNeuralDynamics/aind-ephys-curation` | `repo-004368` `yarikoptic/aind-ephys-curation`（REPRESENTATIVE；parent=AllenNeuralDynamics/aind-ephys-curation） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 630 | `zotero/zotero-connectors`<br>source=`zotero/zotero-connectors` | `repo-005786` `yarikoptic/zotero-connectors`（REPRESENTATIVE；parent=zotero/zotero-connectors） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 631 | `jinl0/fastmcpcloud-test`<br>source=`JinL0/fastmcpcloud-test` | `repo-002890` `JinL0/fastmcpcloud-test`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 632 | `physiopy/physiopy.github.io`<br>source=`physiopy/physiopy.github.io` | `repo-005336` `yarikoptic/physiopy.github.io`（REPRESENTATIVE；parent=physiopy/physiopy.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 633 | `mag05270/agents-zhongyi`<br>source=`mag05270/agents-zhongyi` | `repo-006600` `psknlr/agents-zhongyi`（REPRESENTATIVE；parent=mag05270/agents-zhongyi） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 634 | `sokrypton/colabfold`<br>source=`sokrypton/ColabFold` | `repo-006104` `leizhou69/ColabFold`（REPRESENTATIVE；parent=sokrypton/ColabFold）<br>`repo-002152` `th86/ColabFold`（MEMBER；parent=sokrypton/ColabFold） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 635 | `novonordisk-research/langpert`<br>source=`novonordisk-research/LangPert` | `repo-006870` `tangxuan82/LangPert`（REPRESENTATIVE；parent=novonordisk-research/LangPert） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 636 | `ryanding26/histopath`<br>source=`ryanDing26/HistoPath` | `repo-001738` `ryanDing26/HistoPath`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 637 | `nkalavros/popscalescrnaseq`<br>source=`NKalavros/PopScalescRNAseq` | `repo-007284` `NKalavros/PopScalescRNAseq`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 638 | `nvidia-bionemo-blueprints/generative-virtual-screening`<br>source=`NVIDIA-BioNeMo-blueprints/generative-virtual-screening` | `repo-001917` `shantanusharma/generative-virtual-screening`（REPRESENTATIVE；parent=NVIDIA-BioNeMo-blueprints/generative-virtual-screening） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 639 | `gerstung-lab/delphi`<br>source=`gerstung-lab/Delphi` | `repo-001274` `HelloWorldLTY/Delphi`（REPRESENTATIVE；parent=gerstung-lab/Delphi） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 640 | `czi-ai/transcriptformer`<br>source=`czi-ai/transcriptformer` | `repo-006902` `tangxuan82/transcriptformer`（REPRESENTATIVE；parent=czi-ai/transcriptformer）<br>`repo-007139` `jaybee84/transcriptformer`（MEMBER；parent=czi-ai/transcriptformer） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 641 | `google-deepmind/alphagenome`<br>source=`google-deepmind/alphagenome` | `repo-006100` `leizhou69/alphagenome`（REPRESENTATIVE；parent=google-deepmind/alphagenome）<br>`repo-005875` `dabulseco/alphagenome`（MEMBER；parent=google-deepmind/alphagenome）<br>`repo-006292` `Ali-Maq/alphagenome`（MEMBER；parent=google-deepmind/alphagenome） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 642 | `vik-u/brenda_agent`<br>source=`Vik-u/Brenda_Agent` | `repo-006946` `Vik-u/Brenda_Agent`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 643 | `microsoft/ai4g-flood`<br>source=`microsoft/ai4g-flood` | `repo-006936` `Vik-u/ai4g-flood`（REPRESENTATIVE；parent=microsoft/ai4g-flood） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 644 | `ali-maq/civic_database_documenation-`<br>source=`Ali-Maq/CIvic_database_documenation-` | `repo-006305` `Ali-Maq/CIvic_database_documenation-`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 645 | `uio-bmi/predict-airr`<br>source=`uio-bmi/predict-airr` | `repo-002192` `th86/predict-airr`（REPRESENTATIVE；parent=uio-bmi/predict-airr） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 646 | `manojgithub1/synapses-emergency-healthcare-system`<br>source=`ManojGitHub1/Synapses-Emergency-Healthcare-System` | `repo-006894` `tangxuan82/Synapses-Emergency-Healthcare-System`（REPRESENTATIVE；parent=ManojGitHub1/Synapses-Emergency-Healthcare-System） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 647 | `openai/evals`<br>source=`openai/evals` | `repo-001889` `shantanusharma/evals`（REPRESENTATIVE；parent=openai/evals） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 648 | `ryanding26/emdna-gpu`<br>source=`ryanDing26/emDNA-GPU` | `repo-001735` `ryanDing26/emDNA-GPU`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 649 | `oncologymodelinggroup/tumortwin`<br>source=`OncologyModelingGroup/TumorTwin` | `repo-006903` `tangxuan82/TumorTwin`（REPRESENTATIVE；parent=OncologyModelingGroup/TumorTwin） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 650 | `zou-group/cellvoyager`<br>source=`zou-group/CellVoyager` | `repo-006102` `leizhou69/CellVoyager`（REPRESENTATIVE；parent=zou-group/CellVoyager） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 651 | `buffalo-ontology-group/mri_ontology`<br>source=`Buffalo-Ontology-Group/MRI_Ontology` | `repo-005132` `yarikoptic/MRI_Ontology`（REPRESENTATIVE；parent=Buffalo-Ontology-Group/MRI_Ontology） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 652 | `physiopy/physiopy-repository-template`<br>source=`physiopy/physiopy-repository-template` | `repo-005335` `yarikoptic/physiopy-repository-template`（REPRESENTATIVE；parent=physiopy/physiopy-repository-template） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 653 | `learncheme/learncheme.github.io`<br>source=`LearnChemE/LearnChemE.github.io` | `repo-005930` `dabulseco/LearnChemE.github.io`（REPRESENTATIVE；parent=LearnChemE/LearnChemE.github.io） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 654 | `gtpash/dt4co`<br>source=`gtpash/dt4co` | `repo-006851` `tangxuan82/dt4co`（REPRESENTATIVE；parent=gtpash/dt4co） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 655 | `aertslab/pyscenic`<br>source=`aertslab/pySCENIC` | `repo-003078` `Liripo/pySCENIC`（REPRESENTATIVE；parent=aertslab/pySCENIC） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 656 | `mouseland/cellpose`<br>source=`MouseLand/cellpose` | `repo-007430` `samutiti/cellpose_batchable`（REPRESENTATIVE；parent=MouseLand/cellpose） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 657 | `styx-api/niwrap`<br>source=`styx-api/niwrap` | `repo-005234` `yarikoptic/niwrap`（REPRESENTATIVE；parent=styx-api/niwrap） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 658 | `vlln/paper2report`<br>source=`vlln/paper2report` | `repo-002251` `vlln/paper2report`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 659 | `benjam11n/twinai`<br>source=`Benjam11n/TwinAI` | `repo-006904` `tangxuan82/TwinAI`（REPRESENTATIVE；parent=Benjam11n/TwinAI） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 660 | `ali-maq/oncocite`<br>source=`Ali-Maq/OncoCITE` | `repo-006340` `Ali-Maq/OncoCITE`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 661 | `qsong-github/spaim`<br>source=`QSong-github/SpaIM` | `repo-001350` `HelloWorldLTY/SpaIM`（REPRESENTATIVE；parent=QSong-github/SpaIM） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 662 | `idptools/idpcolab`<br>source=`idptools/idpcolab` | `repo-006863` `tangxuan82/idpcolab`（REPRESENTATIVE；parent=idptools/idpcolab） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `613–662`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-017-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
