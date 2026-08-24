# 远程调研 Batch 015

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **513–562**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 17 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 20 |
| 分类 `LOW_INFORMATION_RECHECK` | 4 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 6 |
| 标记 `CHILD_FORK_SURFACE` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 32 |
| 标记 `LICENSE_UNCLEAR` | 21 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RECENT_ACTIVE` | 50 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 513 | `modelcontextprotocol/inspector`<br>source=`modelcontextprotocol/inspector` | `repo-001025` `Edison-A-N/inspector`（REPRESENTATIVE；parent=modelcontextprotocol/inspector） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 514 | `akariasai/openscholar`<br>source=`AkariAsai/OpenScholar` | `repo-005290` `yarikoptic/OpenScholar`（REPRESENTATIVE；parent=AkariAsai/OpenScholar） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 515 | `microsoft/mu-protein`<br>source=`microsoft/Mu-Protein` | `repo-006986` `Vik-u/mu-protein`（REPRESENTATIVE；parent=microsoft/Mu-Protein） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 516 | `aim-kannlab/brainiac`<br>source=`AIM-KannLab/BrainIAC` | `repo-006473` `gutendzx/BrainIAC`（REPRESENTATIVE；parent=AIM-KannLab/BrainIAC） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 517 | `pkudigitalhealth/ecgfounder`<br>source=`PKUDigitalHealth/ECGFounder` | `repo-006494` `gutendzx/ECGFounder`（REPRESENTATIVE；parent=PKUDigitalHealth/ECGFounder） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 518 | `se4bio/mcp-agent-base`<br>source=`se4bio/mcp-agent-base` | `repo-002824` `inodb/mcp-agent-base-1`（REPRESENTATIVE；parent=se4bio/mcp-agent-base） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 519 | `baranzinilab/spoke_genelab`<br>source=`BaranziniLab/spoke_genelab` | `repo-002724` `goodb/spoke_genelab`（REPRESENTATIVE；parent=BaranziniLab/spoke_genelab） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 520 | `jissen706/abdominal-symprom-clarify-bot`<br>source=`jissen706/Abdominal-Symprom-Clarify-Bot` | `repo-002924` `jissen706/Abdominal-Symprom-Clarify-Bot`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 521 | `jissen706/aliquot-first-class-tracker`<br>source=`jissen706/aliquot-first-class-tracker` | `repo-002925` `jissen706/aliquot-first-class-tracker`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 522 | `ohdsi/cohortgenerator`<br>source=`OHDSI/CohortGenerator` | `repo-006309` `Ali-Maq/CohortGenerator`（REPRESENTATIVE；parent=OHDSI/CohortGenerator） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 523 | `stanford-oval/storm`<br>source=`stanford-oval/storm` | `repo-003320` `Rakshitha-Ireddi/storm`（REPRESENTATIVE；parent=stanford-oval/storm） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 524 | `leezx/vibe-researching`<br>source=`leezx/Vibe-Researching` | `repo-007211` `leezx/Vibe-Researching`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 525 | `rakshitha-ireddi/cryogem`<br>source=`Rakshitha-Ireddi/CRYOGEM` | `repo-003244` `Rakshitha-Ireddi/CRYOGEM`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 526 | `haoranshao/pertbench`<br>source=`HaoranShao/PertBench` | `repo-001328` `HelloWorldLTY/PertBench`（REPRESENTATIVE；parent=HaoranShao/PertBench） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 527 | `sparontologies/cito`<br>source=`SPAROntologies/cito` | `repo-004552` `yarikoptic/cito`（REPRESENTATIVE；parent=SPAROntologies/cito） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 528 | `dabulseco/geoprompt`<br>source=`dabulseco/GeoPrompt` | `repo-005918` `dabulseco/GeoPrompt`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 529 | `jaechang-hits/standigm_paper_citation`<br>source=`jaechang-hits/standigm_paper_citation` | `repo-002882` `jaechang-hits/standigm_paper_citation`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 530 | `leizhou69/rcl-identifier`<br>source=`leizhou69/RCL-identifier` | `repo-006114` `leizhou69/RCL-identifier`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 531 | `guestrin-lab/deepscholar`<br>source=`guestrin-lab/deepscholar` | `repo-005816` `yaswanth169/deepscholar`（REPRESENTATIVE；parent=guestrin-lab/deepscholar） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 532 | `kylenevergivesup/weather-mcp-server`<br>source=`KyleNeverGivesUp/weather-mcp-server` | `repo-003048` `KyleNeverGivesUp/weather-mcp-server`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 533 | `jim-bo/cbio-agent-null`<br>source=`jim-bo/cbio-agent-null` | `repo-002757` `inodb/cbio-agent-null`（REPRESENTATIVE；parent=jim-bo/cbio-agent-null） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 534 | `gagneurlab/mmsplice_mtsplice`<br>source=`gagneurlab/MMSplice_MTSplice` | `repo-001665` `MinxZ/MMSplice_MTSplice`（REPRESENTATIVE；parent=gagneurlab/MMSplice_MTSplice） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 535 | `opengeos/lidar`<br>source=`opengeos/lidar` | `repo-001954` `shantanusharma/lidar`（REPRESENTATIVE；parent=opengeos/lidar） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 536 | `neuroml/documentation`<br>source=`NeuroML/Documentation` | `repo-004753` `yarikoptic/Documentation-2`（REPRESENTATIVE；parent=NeuroML/Documentation） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 537 | `schuetzgroup/fret-analysis`<br>source=`schuetzgroup/fret-analysis` | `repo-004840` `yarikoptic/fret-analysis`（REPRESENTATIVE；parent=schuetzgroup/fret-analysis） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 538 | `alexmikhalev/claude-code-continuous-learning-skill`<br>source=`AlexMikhalev/claude-code-continuous-learning-skill` | `repo-004189` `alexs42/Claudeception`（REPRESENTATIVE；parent=AlexMikhalev/claude-code-continuous-learning-skill） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 539 | `dabulseco/dna_mutation_sonification`<br>source=`dabulseco/dna_mutation_sonification` | `repo-005908` `dabulseco/dna_mutation_sonification`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 540 | `biplabendu/abcd-dictionary-chatbot`<br>source=`biplabendu/abcd-dictionary-chatbot` | `repo-004349` `yarikoptic/abcd-dictionary-chatbot`（REPRESENTATIVE；parent=biplabendu/abcd-dictionary-chatbot） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 541 | `the-swarm-corporation/ai-coscientist`<br>source=`The-Swarm-Corporation/AI-CoScientist` | `repo-007172` `leezx/AI-CoScientist`（REPRESENTATIVE；parent=The-Swarm-Corporation/AI-CoScientist） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 542 | `th86/opencode-st`<br>source=`th86/OpenCode-ST` | `repo-002188` `th86/OpenCode-ST`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 543 | `nbdc-datahub/nbdctoolsdata`<br>source=`nbdc-datahub/NBDCtoolsData` | `repo-005153` `yarikoptic/NBDCtoolsData`（REPRESENTATIVE；parent=nbdc-datahub/NBDCtoolsData） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 544 | `hanlin-yang/evo2-mcp`<br>source=`hanlin-yang/evo2-MCP` | `repo-006568` `hanlin-yang/evo2-MCP`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 545 | `lordxx505/sleepgpt`<br>source=`LordXX505/SleepGPT` | `repo-006539` `gutendzx/SleepGPT1`（REPRESENTATIVE；parent=LordXX505/SleepGPT） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 546 | `th86/opencode-tcrseq-ml-pipeline`<br>source=`th86/OpenCode-TCRSeq-ML-pipeline` | `repo-002189` `th86/OpenCode-TCRSeq-ML-pipeline`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 547 | `nvidia-bionemo/rnapro`<br>source=`NVIDIA-BioNeMo/RNAPro` | `repo-002048` `shantanusharma/RNAPro`（REPRESENTATIVE；parent=NVIDIA-BioNeMo/RNAPro） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 548 | `mercure-imaging/mercure`<br>source=`mercure-imaging/mercure` | `repo-005091` `yarikoptic/mercure`（REPRESENTATIVE；parent=mercure-imaging/mercure） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 549 | `charvijain16/autonomous_loop_ai_science_discovery`<br>source=`Charvijain16/Autonomous_loop_AI_Science_Discovery` | `repo-006743` `Charvijain16/Autonomous_loop_AI_Science_Discovery`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 550 | `guylu/gluformer`<br>source=`Guylu/GluFormer` | `repo-006498` `gutendzx/GluFormer_Nature`（REPRESENTATIVE；parent=Guylu/GluFormer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 551 | `ggit12/anndictionary`<br>source=`ggit12/anndictionary` | `repo-006390` `Vincentcchu/anndictionary`（REPRESENTATIVE；parent=ggit12/anndictionary） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 552 | `scverse/spatialdata-io`<br>source=`scverse/spatialdata-io` | `repo-003091` `Liripo/spatialdata-io`（REPRESENTATIVE；parent=scverse/spatialdata-io） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 553 | `translatorsri/testharness`<br>source=`TranslatorSRI/TestHarness` | `repo-000959` `andrewsu/TestHarness`（REPRESENTATIVE；parent=TranslatorSRI/TestHarness） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 554 | `hannesstark/boltzgen`<br>source=`HannesStark/boltzgen` | `repo-001590` `marcosbolanos/boltzgen`（REPRESENTATIVE；parent=HannesStark/boltzgen）<br>`repo-006944` `Vik-u/boltzgen`（MEMBER；parent=HannesStark/boltzgen） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 555 | `vik-u/momentum_process_scriptgen`<br>source=`Vik-u/Momentum_Process_ScriptGen` | `repo-006984` `Vik-u/Momentum_Process_ScriptGen`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 556 | `insilicomedicine/dora`<br>source=`insilicomedicine/DORA` | `repo-001882` `shantanusharma/DORA`（REPRESENTATIVE；parent=insilicomedicine/DORA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 557 | `xulabs/aitom`<br>source=`xulabs/aitom` | `repo-005797` `yaswanth169/aitom`（REPRESENTATIVE；parent=xulabs/aitom） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 558 | `jissen706/pytorch-medical-image-classification-project`<br>source=`jissen706/PyTorch-Medical-Image-Classification-Project` | `repo-002936` `jissen706/PyTorch-Medical-Image-Classification-Project`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 559 | `helloworldlty/drugplayground`<br>source=`HelloWorldLTY/drugplayground` | `repo-001278` `HelloWorldLTY/drugplayground`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 560 | `kylenevergivesup/mcp-server-kyle`<br>source=`KyleNeverGivesUp/mcp-server-kyle` | `repo-003042` `KyleNeverGivesUp/mcp-server-kyle`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 561 | `othmanadi/planning-with-files`<br>source=`OthmanAdi/planning-with-files` | `repo-001436` `jucor/planning-with-files`（REPRESENTATIVE；parent=OthmanAdi/planning-with-files） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 562 | `hanlin-yang/bioaisaas-main`<br>source=`hanlin-yang/BioAiSaaS-main` | `repo-006567` `hanlin-yang/BioAiSaaS-main`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |

## 完整性边界

- 本文件连续覆盖 orders `513–562`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-015-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
