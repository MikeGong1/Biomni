# 远程调研 Batch 012

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **363–412**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 4 |
| 分类 `DATASET_OR_BENCHMARK` | 6 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 13 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 20 |
| 分类 `LOW_INFORMATION_RECHECK` | 4 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 3 |
| 标记 `CHILD_FORK_SURFACE` | 2 |
| 标记 `FORK_LINEAGE_REQUIRED` | 34 |
| 标记 `LICENSE_UNCLEAR` | 24 |
| 标记 `RECENT_ACTIVE` | 50 |
| 标记 `RELEASE_SURFACE` | 5 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 363 | `facebookresearch/neuroai`<br>source=`facebookresearch/neuroai` | `repo-005171` `yarikoptic/neuroai`（REPRESENTATIVE；parent=facebookresearch/neuroai） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 364 | `evoscientist/evoscientist`<br>source=`EvoScientist/EvoScientist` | `repo-006108` `leizhou69/EvoS`（REPRESENTATIVE；parent=EvoScientist/EvoScientist） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 365 | `nigmat-future/20260426-circuit-icb-pan-cancer-immune-checkpoint-blockade-resistance-cell-state-atlas`<br>source=`Nigmat-future/20260426-circuit-icb-pan-cancer-immune-checkpoint-blockade-resistance-cell-state-atlas` | `repo-003167` `Nigmat-future/20260426-circuit-icb-pan-cancer-immune-checkpoint-blockade-resistance-cell-state-atlas`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 366 | `averyself/wmdp-agentic-eval`<br>source=`averyself/wmdp-agentic-eval` | `repo-006370` `averyself/wmdp-agentic-eval`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 367 | `bennokr/makeprov`<br>source=`bennokr/makeprov` | `repo-005073` `yarikoptic/makeprov`（REPRESENTATIVE；parent=bennokr/makeprov） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 368 | `cbioportal/cbioportal-cell-explorer`<br>source=`cBioPortal/cbioportal-cell-explorer` | `repo-002760` `inodb/cbioportal-cell-explorer`（REPRESENTATIVE；parent=cBioPortal/cbioportal-cell-explorer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 369 | `ome/ngff-spec`<br>source=`ome/ngff-spec` | `repo-005203` `yarikoptic/ngff-spec`（REPRESENTATIVE；parent=ome/ngff-spec） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 370 | `quantum-visualizations/qmsolve`<br>source=`quantum-visualizations/qmsolve` | `repo-007396` `div0-space/qmsolve-playful`（REPRESENTATIVE；parent=quantum-visualizations/qmsolve） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 371 | `pennlinc/babs`<br>source=`PennLINC/babs` | `repo-004427` `yarikoptic/babs`（REPRESENTATIVE；parent=PennLINC/babs） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 372 | `stellarium/stellarium`<br>source=`Stellarium/stellarium` | `repo-006599` `PMK89/stellarium`（REPRESENTATIVE；parent=Stellarium/stellarium） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 373 | `andrewsu/calibr-briefing`<br>source=`andrewsu/calibr-briefing` | `repo-000900` `andrewsu/calibr-briefing`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 374 | `conda-forge/dandi-feedstock`<br>source=`conda-forge/dandi-feedstock` | `repo-004636` `yarikoptic/dandi-feedstock`（REPRESENTATIVE；parent=conda-forge/dandi-feedstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 375 | `pangaea-data-publisher/fuji`<br>source=`pangaea-data-publisher/fuji` | `repo-004843` `yarikoptic/fuji`（REPRESENTATIVE；parent=pangaea-data-publisher/fuji） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 376 | `nigmat-future/publishable-research-orchestrator`<br>source=`Nigmat-future/publishable-research-orchestrator` | `repo-003197` `Nigmat-future/publishable-research-orchestrator`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 377 | `multica-ai/andrej-karpathy-skills`<br>source=`multica-ai/andrej-karpathy-skills` | `repo-005876` `dabulseco/andrej-karpathy-skills`（REPRESENTATIVE；parent=multica-ai/andrej-karpathy-skills） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 378 | `cbioportal/cancerhotspots`<br>source=`cBioPortal/cancerhotspots` | `repo-002755` `inodb/cancerhotspots`（REPRESENTATIVE；parent=cBioPortal/cancerhotspots） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 379 | `mri-lab-graz/prism-studio`<br>source=`MRI-Lab-Graz/prism-studio` | `repo-005364` `yarikoptic/prism-studio`（REPRESENTATIVE；parent=MRI-Lab-Graz/prism-studio） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 380 | `bids-standard/bids-examples`<br>source=`bids-standard/bids-examples` | `repo-004460` `yarikoptic/BIDS-examples`（REPRESENTATIVE；parent=bids-standard/bids-examples） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 381 | `neurolabusc/dcm_validate`<br>source=`neurolabusc/dcm_validate` | `repo-004700` `yarikoptic/dcm_validate`（REPRESENTATIVE；parent=neurolabusc/dcm_validate） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 382 | `brainiak/rt-cloud`<br>source=`brainiak/rt-cloud` | `repo-005525` `yarikoptic/rt-cloud`（REPRESENTATIVE；parent=brainiak/rt-cloud） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 383 | `yohyoh-wang/stargate-flowjo-plugin`<br>source=`yohyoh-wang/staRgate-flowjo-plugin` | `repo-005861` `yohyoh-wang/staRgate-flowjo-plugin`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 384 | `jissen706/timbre`<br>source=`jissen706/Timbre` | `repo-002941` `jissen706/Timbre`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 385 | `norrisjamie23/localising_soz_from_spes`<br>source=`norrisjamie23/Localising_SOZ_from_SPES` | `repo-003106` `mkoretsky1/Localising_SOZ_from_SPES`（REPRESENTATIVE；parent=norrisjamie23/Localising_SOZ_from_SPES） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 386 | `ali-maq/civic-extraction-agent`<br>source=`Ali-Maq/civic-extraction-agent` | `repo-006304` `Ali-Maq/civic-extraction-agent`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 387 | `ali-maq/oncocite-langchain`<br>source=`Ali-Maq/oncocite-langchain` | `repo-006341` `Ali-Maq/oncocite-langchain`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 388 | `kalinnonchev/pathology-hooknet-tls-pytorch`<br>source=`KalinNonchev/pathology-hooknet-tls-pytorch` | `repo-003013` `KalinNonchev/pathology-hooknet-tls-pytorch`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 389 | `nigmat-future/pad-to-vibe`<br>source=`Nigmat-future/pad-to-vibe` | `repo-003194` `Nigmat-future/pad-to-vibe`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 390 | `researai/deepscientist`<br>source=`ResearAI/DeepScientist` | `repo-006105` `leizhou69/DeepS`（REPRESENTATIVE；parent=ResearAI/DeepScientist） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 391 | `genome-nexus/genome-nexus`<br>source=`genome-nexus/genome-nexus` | `repo-002796` `inodb/genome-nexus`（REPRESENTATIVE；parent=genome-nexus/genome-nexus） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 392 | `genome-nexus/genome-nexus-importer`<br>source=`genome-nexus/genome-nexus-importer` | `repo-002800` `inodb/genome-nexus-importer`（REPRESENTATIVE；parent=genome-nexus/genome-nexus-importer） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 393 | `rsflinn/autism-brain-explorer`<br>source=`rsflinn/autism-brain-explorer` | `repo-003919` `rsflinn/autism-brain-explorer`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 394 | `mickaelleclercq/autofigure-edit`<br>source=`mickaelleclercq/AutoFigure-Edit` | `repo-001629` `mickaelleclercq/AutoFigure-Edit`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 395 | `rasic2/gvasp`<br>source=`Rasic2/gvasp` | `repo-007417` `Rasic2/gvasp`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 396 | `psknlr/drug_agent`<br>source=`psknlr/drug_agent` | `repo-006608` `psknlr/drug_agent`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 397 | `openneurodatasets/ds000113`<br>source=`OpenNeuroDatasets/ds000113` | `repo-004758` `yarikoptic/ds000113`（REPRESENTATIVE；parent=OpenNeuroDatasets/ds000113） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 398 | `cisco-ai-defense/skill-scanner`<br>source=`cisco-ai-defense/skill-scanner` | `repo-005585` `yarikoptic/skill-scanner`（REPRESENTATIVE；parent=cisco-ai-defense/skill-scanner） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 399 | `inodb/cbiopubkb`<br>source=`inodb/cbiopubkb` | `repo-002770` `inodb/cbiopubkb`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 400 | `gero-science/harvest`<br>source=`gero-science/HARVEST` | `repo-000917` `andrewsu/HARVEST`（REPRESENTATIVE；parent=gero-science/HARVEST） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 401 | `bytedance/protenix`<br>source=`bytedance/Protenix` | `repo-001684` `PabloPauling/Protenix`（REPRESENTATIVE；parent=bytedance/Protenix） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 402 | `travisvn/awesome-claude-skills`<br>source=`travisvn/awesome-claude-skills` | `repo-002874` `jaechang-hits/awesome-claude-skills`（REPRESENTATIVE；parent=travisvn/awesome-claude-skills） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 403 | `rohitg00/awesome-claude-code-toolkit`<br>source=`rohitg00/awesome-claude-code-toolkit` | `repo-002873` `jaechang-hits/awesome-claude-code-toolkit`（REPRESENTATIVE；parent=rohitg00/awesome-claude-code-toolkit） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 404 | `telefonica-scientific-research/gaze_reward`<br>source=`Telefonica-Scientific-Research/gaze_reward` | `repo-004246` `kwskws1998/gaze_reward`（REPRESENTATIVE；parent=Telefonica-Scientific-Research/gaze_reward） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 405 | `neuro-d3/neurod3`<br>source=`Neuro-D3/neurod3` | `repo-005178` `yarikoptic/neurod3`（REPRESENTATIVE；parent=Neuro-D3/neurod3） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 406 | `punkpeye/awesome-mcp-servers`<br>source=`punkpeye/awesome-mcp-servers` | `repo-002652` `de-grave/awesome-mcp-servers`（REPRESENTATIVE；parent=punkpeye/awesome-mcp-servers） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 407 | `zocomputer/skills`<br>source=`zocomputer/skills` | `repo-002706` `erhuve/skills`（REPRESENTATIVE；parent=zocomputer/skills） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 408 | `cmu-delphi/delphi-epidata`<br>source=`cmu-delphi/delphi-epidata` | `repo-005817` `yaswanth169/delphi-epidata`（REPRESENTATIVE；parent=cmu-delphi/delphi-epidata） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 409 | `k-dense-ai/claude-scientific-writer`<br>source=`K-Dense-AI/claude-scientific-writer` | `repo-004563` `yarikoptic/claude-scientific-writer`（REPRESENTATIVE；parent=K-Dense-AI/claude-scientific-writer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 410 | `ohbm/hackathon2026`<br>source=`ohbm/hackathon2026` | `repo-004918` `yarikoptic/hackathon2026`（REPRESENTATIVE；parent=ohbm/hackathon2026） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 411 | `snowlightpath/extended-mind`<br>source=`SnowLightPath/extended-mind` | `repo-002136` `SnowLightPath/extended-mind`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 412 | `voltagent/awesome-agent-skills`<br>source=`VoltAgent/awesome-agent-skills` | `repo-004183` `alexs42/awesome-claude-skills`（REPRESENTATIVE；parent=VoltAgent/awesome-agent-skills） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |

## 完整性边界

- 本文件连续覆盖 orders `363–412`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-012-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
