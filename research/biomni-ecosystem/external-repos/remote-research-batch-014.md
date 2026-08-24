# 远程调研 Batch 014

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **463–512**；**50** 个 family；**51** 条 bounded repository records。

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
| 分类 `DATASET_OR_BENCHMARK` | 1 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 11 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 23 |
| 分类 `LOW_INFORMATION_RECHECK` | 7 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 6 |
| 标记 `CHILD_FORK_SURFACE` | 5 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 33 |
| 标记 `LICENSE_UNCLEAR` | 24 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RECENT_ACTIVE` | 50 |
| 标记 `RELEASE_SURFACE` | 2 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 463 | `r-siddiqi/hofstadter`<br>source=`r-siddiqi/Hofstadter` | `repo-003219` `r-siddiqi/Hofstadter`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 464 | `empriselab/feeding-deployment`<br>source=`empriselab/feeding-deployment` | `repo-005821` `yaswanth169/feeding-deployment`（REPRESENTATIVE；parent=empriselab/feeding-deployment） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 465 | `jucor/claude-code-lsp-skill`<br>source=`jucor/claude-code-lsp-skill` | `repo-001391` `jucor/claude-code-lsp-skill`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 466 | `yang-ai-lab/hearts`<br>source=`yang-ai-lab/HEARTS` | `repo-006500` `gutendzx/HEARTS`（REPRESENTATIVE；parent=yang-ai-lab/HEARTS） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 467 | `castacks/airstack`<br>source=`castacks/AirStack` | `repo-005796` `yaswanth169/AirStack`（REPRESENTATIVE；parent=castacks/AirStack） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 468 | `yang-ai-lab/sleeplm`<br>source=`yang-ai-lab/SleepLM` | `repo-006540` `gutendzx/SleepLM`（REPRESENTATIVE；parent=yang-ai-lab/SleepLM） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 469 | `yang-ai-lab/osf-open-sleep-fm`<br>source=`yang-ai-lab/OSF-Open-Sleep-FM` | `repo-006518` `gutendzx/OSF-Open-Sleep-FM`（REPRESENTATIVE；parent=yang-ai-lab/OSF-Open-Sleep-FM） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 470 | `nipy/nipype`<br>source=`nipy/nipype` | `repo-005228` `yarikoptic/nipype`（REPRESENTATIVE；parent=nipy/nipype） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 471 | `jissen706/magellan`<br>source=`jissen706/Magellan` | `repo-002933` `jissen706/Magellan`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 472 | `coleam00/excalidraw-diagram-skill`<br>source=`coleam00/excalidraw-diagram-skill` | `repo-004802` `yarikoptic/excalidraw-diagram-skill`（REPRESENTATIVE；parent=coleam00/excalidraw-diagram-skill） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 473 | `snap-stanford/pulsar`<br>source=`snap-stanford/PULSAR` | `repo-003301` `Rakshitha-Ireddi/PULSAR`（REPRESENTATIVE；parent=snap-stanford/PULSAR） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 474 | `kuanlinhuang/biomni-lite`<br>source=`kuanlinhuang/Biomni-Lite` | `repo-001529` `kuanlinhuang/Biomni-Lite`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 475 | `guxiao0822/cardiac-sensing-fm`<br>source=`guxiao0822/Cardiac-Sensing-FM` | `repo-006478` `gutendzx/Cardiac-Sensing-FM`（REPRESENTATIVE；parent=guxiao0822/Cardiac-Sensing-FM） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 476 | `syt2/zotero-scipdf`<br>source=`syt2/zotero-scipdf` | `repo-001478` `jucor/zotero-scipdf`（REPRESENTATIVE；parent=syt2/zotero-scipdf） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 477 | `zskylarli/cellocate`<br>source=`zskylarli/cellocate` | `repo-002374` `zskylarli/cellocate`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 478 | `joncarter1/wav2sleep`<br>source=`joncarter1/wav2sleep` | `repo-006558` `gutendzx/wav2sleep`（REPRESENTATIVE；parent=joncarter1/wav2sleep） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 479 | `thsa/datawarrior`<br>source=`thsa/datawarrior` | `repo-007147` `KSUN63/datawarrior`（REPRESENTATIVE；parent=thsa/datawarrior） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 480 | `vik-u/bioagenthub_crawler`<br>source=`Vik-u/BioAgentHub_Crawler` | `repo-006942` `Vik-u/BioAgentHub_Crawler`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 481 | `genbio-ai/modelgenerator`<br>source=`genbio-ai/ModelGenerator` | `repo-005837` `yaswanth169/ModelGenerator`（REPRESENTATIVE；parent=genbio-ai/ModelGenerator） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 482 | `hogenesch/jtk_cycle2`<br>source=`hogenesch/JTK_Cycle2` | `repo-000920` `andrewsu/JTK_Cycle2`（REPRESENTATIVE；parent=hogenesch/JTK_Cycle2） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 483 | `mfcovington/jtk-cycle`<br>source=`mfcovington/jtk-cycle` | `repo-000919` `andrewsu/jtk-cycle`（REPRESENTATIVE；parent=mfcovington/jtk-cycle） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 484 | `nipoppy/nipoppy`<br>source=`nipoppy/nipoppy` | `repo-005222` `yarikoptic/nipoppy`（REPRESENTATIVE；parent=nipoppy/nipoppy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 485 | `liripo/cellranger_learn`<br>source=`Liripo/cellranger_learn` | `repo-003055` `Liripo/cellranger_learn`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 486 | `zpforlove/resp-agent`<br>source=`zpforlove/Resp-Agent` | `repo-006528` `gutendzx/Resp-Agent`（REPRESENTATIVE；parent=zpforlove/Resp-Agent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 487 | `celltype/celltype-agent`<br>source=`celltype/celltype-agent` | `repo-004185` `alexs42/Celltype_cli`（REPRESENTATIVE；parent=celltype/celltype-agent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 488 | `zhanxw/seqminer`<br>source=`zhanxw/seqminer` | `repo-002356` `zhanxw/seqminer`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 489 | `kuanlinhuang/biomni_ad_ada_entries`<br>source=`kuanlinhuang/Biomni_AD_ADA_entries` | `repo-001530` `kuanlinhuang/Biomni_AD_ADA_entries`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 490 | `de-grave/openonco-mcp`<br>source=`de-grave/openonco-mcp` | `repo-002666` `de-grave/openonco-mcp`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 491 | `deepchem/deepchem`<br>source=`deepchem/deepchem` | `repo-001875` `shantanusharma/deepchem`（REPRESENTATIVE；parent=deepchem/deepchem） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 492 | `charmoniumq/probe`<br>source=`charmoniumQ/PROBE` | `repo-005367` `yarikoptic/PROBE`（REPRESENTATIVE；parent=charmoniumQ/PROBE） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 493 | `vik-u/bioagenthub`<br>source=`Vik-u/BioAgentHub` | `repo-006941` `Vik-u/BioAgentHub`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 494 | `datalad-handbook/book`<br>source=`datalad-handbook/book` | `repo-004497` `yarikoptic/book`（REPRESENTATIVE；parent=datalad-handbook/book） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 495 | `anam-org/metaxy`<br>source=`anam-org/metaxy` | `repo-005097` `yarikoptic/metaxy`（REPRESENTATIVE；parent=anam-org/metaxy） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 496 | `arise-initiative/robomimic`<br>source=`ARISE-Initiative/robomimic` | `repo-005853` `yaswanth169/robomimic`（REPRESENTATIVE；parent=ARISE-Initiative/robomimic） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 497 | `chahat08/zarr_rechunker`<br>source=`Chahat08/Zarr_Rechunker` | `repo-002571` `Chahat08/Zarr_Rechunker`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL`、`RECENT_ACTIVE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 498 | `explorerwjy/ephyssumstats`<br>source=`explorerwjy/EphysSumStats` | `repo-006053` `explorerwjy/EphysSumStats`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 499 | `humathe/av-dar`<br>source=`HuMathe/av-dar` | `repo-005799` `yaswanth169/av-dar`（REPRESENTATIVE；parent=HuMathe/av-dar） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 500 | `hasanaldhahi/cross-precision-llm-deployment-biomni`<br>source=`HasanAldhahi/cross-precision-llm-deployment-biomni` | `repo-001104` `HasanAldhahi/cross-precision-llm-deployment-biomni`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 501 | `dabulseco/wbcd_ml_app`<br>source=`dabulseco/WBCD_ml_app` | `repo-005992` `dabulseco/WBCD_ml_app`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 502 | `pointcept/pointcept`<br>source=`Pointcept/Pointcept` | `repo-007565` `xinwuye/UniDock-Pointcept`（REPRESENTATIVE；parent=Pointcept/Pointcept） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 503 | `jimmc414/kosmos`<br>source=`jimmc414/Kosmos` | `repo-005021` `yarikoptic/Kosmos`（REPRESENTATIVE；parent=jimmc414/Kosmos）<br>`repo-006970` `Vik-u/Kosmos`（MEMBER；parent=jimmc414/Kosmos） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 504 | `th86/drugdevagent`<br>source=`th86/DrugDevAgent` | `repo-002156` `th86/DrugDevAgent`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 505 | `gersteinlab/cellforge`<br>source=`gersteinlab/CellForge` | `repo-001262` `HelloWorldLTY/CellForge`（REPRESENTATIVE；parent=gersteinlab/CellForge） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 506 | `gisetia/mcp-agent-base`<br>source=`gisetia/mcp-agent-base` | `repo-002823` `inodb/mcp-agent-base`（REPRESENTATIVE；parent=gisetia/mcp-agent-base） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 507 | `bcm-neurosurgery/ndx-wearables`<br>source=`BCM-Neurosurgery/ndx-wearables` | `repo-005161` `yarikoptic/ndx-wearables`（REPRESENTATIVE；parent=BCM-Neurosurgery/ndx-wearables） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 508 | `ali-maq/medgemma-kaggle-2026`<br>source=`Ali-Maq/medgemma-kaggle-2026` | `repo-006336` `Ali-Maq/medgemma-kaggle-2026`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 509 | `stanfordvl/curobo`<br>source=`StanfordVL/curobo` | `repo-005812` `yaswanth169/curobo`（REPRESENTATIVE；parent=StanfordVL/curobo） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 510 | `openscience-collective/osa`<br>source=`OpenScience-Collective/osa` | `repo-005300` `yarikoptic/osa`（REPRESENTATIVE；parent=OpenScience-Collective/osa） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 511 | `idptools/finches`<br>source=`idptools/finches` | `repo-006854` `tangxuan82/finches`（REPRESENTATIVE；parent=idptools/finches） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 512 | `lupantech/agentflow`<br>source=`lupantech/AgentFlow` | `repo-006934` `Vik-u/AgentFlow`（REPRESENTATIVE；parent=lupantech/AgentFlow） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `463–512`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-014-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
