# 远程调研 Batch 013

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **413–462**；**50** 个 family；**60** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 60 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 1 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 9 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 23 |
| 分类 `LOW_INFORMATION_RECHECK` | 7 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 7 |
| 标记 `CHILD_FORK_SURFACE` | 2 |
| 标记 `FORK_LINEAGE_REQUIRED` | 38 |
| 标记 `LICENSE_UNCLEAR` | 27 |
| 标记 `MULTI_MEMBER_FAMILY` | 5 |
| 标记 `RECENT_ACTIVE` | 50 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 413 | `sensein/undata`<br>source=`sensein/undata` | `repo-005714` `yarikoptic/undata`（REPRESENTATIVE；parent=sensein/undata） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 414 | `nigmat-future/pretext-med`<br>source=`Nigmat-future/pretext-med` | `repo-003196` `Nigmat-future/pretext-med`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 415 | `nigmat-future/thrombin-comparison`<br>source=`Nigmat-future/thrombin-comparison` | `repo-003204` `Nigmat-future/thrombin-comparison`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 416 | `mendenlab/twinweaver`<br>source=`MendenLab/TwinWeaver` | `repo-006905` `tangxuan82/TwinWeaver`（REPRESENTATIVE；parent=MendenLab/TwinWeaver） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 417 | `jwohlwend/boltz`<br>source=`jwohlwend/boltz` | `repo-001531` `kuanlinhuang/boltz`（REPRESENTATIVE；parent=jwohlwend/boltz）<br>`repo-001792` `sbonner0/boltz`（MEMBER；parent=jwohlwend/boltz）<br>`repo-001852` `shantanusharma/boltz`（MEMBER；parent=jwohlwend/boltz）<br>`repo-005887` `dabulseco/boltz`（MEMBER；parent=jwohlwend/boltz） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 418 | `inodb/vibe-vep`<br>source=`inodb/vibe-vep` | `repo-002869` `inodb/vibe-vep`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 419 | `genome-nexus/genome-nexus-frontend`<br>source=`genome-nexus/genome-nexus-frontend` | `repo-002799` `inodb/genome-nexus-frontend`（REPRESENTATIVE；parent=genome-nexus/genome-nexus-frontend） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 420 | `neurodatascience/dfc`<br>source=`neurodatascience/dFC` | `repo-004717` `yarikoptic/dFC`（REPRESENTATIVE；parent=neurodatascience/dFC） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 421 | `pieeg-club/pieeg-server`<br>source=`pieeg-club/PiEEG-server` | `repo-005338` `yarikoptic/PiEEG-server`（REPRESENTATIVE；parent=pieeg-club/PiEEG-server） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 422 | `affaan-m/ecc`<br>source=`affaan-m/ECC` | `repo-007036` `Javkhaa/everything-claude-code`（REPRESENTATIVE；parent=affaan-m/ECC） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 423 | `smestern/sciagent`<br>source=`smestern/sciagent` | `repo-005546` `yarikoptic/sciagent`（REPRESENTATIVE；parent=smestern/sciagent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 424 | `eugenehp/bids-rs`<br>source=`eugenehp/bids-rs` | `repo-004466` `yarikoptic/bids-rs`（REPRESENTATIVE；parent=eugenehp/bids-rs） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 425 | `bowang-lab/bioreason`<br>source=`bowang-lab/BioReason` | `repo-002655` `de-grave/BioReason`（REPRESENTATIVE；parent=bowang-lab/BioReason） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 426 | `dwzhu-pku/paperbanana`<br>source=`dwzhu-pku/PaperBanana` | `repo-004201` `alexs42/PaperBanana`（REPRESENTATIVE；parent=dwzhu-pku/PaperBanana）<br>`repo-006994` `Vik-u/PaperBanana`（MEMBER；parent=dwzhu-pku/PaperBanana） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 427 | `k-dense-ai/k-dense-byok`<br>source=`K-Dense-AI/k-dense-byok` | `repo-004193` `alexs42/k-dense-byok`（REPRESENTATIVE；parent=K-Dense-AI/k-dense-byok） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 428 | `wu-yc/labclaw`<br>source=`wu-yc/LabClaw` | `repo-004194` `alexs42/LabClaw`（REPRESENTATIVE；parent=wu-yc/LabClaw） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 429 | `internscience/chemclaw`<br>source=`InternScience/ChemClaw` | `repo-003094` `lulaiao/ChemClaw`（REPRESENTATIVE；parent=InternScience/ChemClaw） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 430 | `marcosbolanos/autorigami-`<br>source=`marcosbolanos/autorigami-` | `repo-001587` `marcosbolanos/autorigami-`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 431 | `karpathy/autoresearch`<br>source=`karpathy/autoresearch` | `repo-001252` `HelloWorldLTY/autoresearch`（REPRESENTATIVE；parent=karpathy/autoresearch）<br>`repo-004417` `yarikoptic/autoresearch`（MEMBER；parent=karpathy/autoresearch）<br>`repo-006110` `leizhou69/K_autoresearch`（MEMBER；parent=karpathy/autoresearch）<br>`repo-007050` `jaybee84/autoresearch`（MEMBER；parent=karpathy/autoresearch）<br>`repo-007176` `leezx/autoresearch`（MEMBER；parent=karpathy/autoresearch） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 432 | `natolambert/colloquium`<br>source=`natolambert/colloquium` | `repo-004191` `alexs42/colloquium`（REPRESENTATIVE；parent=natolambert/colloquium） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 433 | `vincentcchu/mllmcelltype`<br>source=`Vincentcchu/mLLMCellType` | `repo-006401` `Vincentcchu/mLLMCellType`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 434 | `vincentcchu/celltypeagent`<br>source=`Vincentcchu/CellTypeAgent` | `repo-006395` `Vincentcchu/CellTypeAgent`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 435 | `datalad/datalad-extension-template`<br>source=`datalad/datalad-extension-template` | `repo-004673` `yarikoptic/datalad-extension-template`（REPRESENTATIVE；parent=datalad/datalad-extension-template） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 436 | `excalidraw/excalidraw-mcp`<br>source=`excalidraw/excalidraw-mcp` | `repo-001892` `shantanusharma/excalidraw-mcp`（REPRESENTATIVE；parent=excalidraw/excalidraw-mcp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 437 | `sage-bionetworks/sage-monorepo`<br>source=`Sage-Bionetworks/sage-monorepo` | `repo-007365` `tschaffter/sage-monorepo`（REPRESENTATIVE；parent=Sage-Bionetworks/sage-monorepo） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 438 | `con/nwb2bids`<br>source=`con/nwb2bids` | `repo-005258` `yarikoptic/nwb2bids`（REPRESENTATIVE；parent=con/nwb2bids） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 439 | `imagingdatacommons/highdicom`<br>source=`ImagingDataCommons/highdicom` | `repo-004950` `yarikoptic/highdicom`（REPRESENTATIVE；parent=ImagingDataCommons/highdicom） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 440 | `explorerwjy/skills`<br>source=`explorerwjy/skills` | `repo-006071` `explorerwjy/skills`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 441 | `molstar/molstar`<br>source=`molstar/molstar` | `repo-006143` `SongyouZhong/molstar`（REPRESENTATIVE；parent=molstar/molstar） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 442 | `qbrc/scopeviewer`<br>source=`QBRC/ScopeViewer` | `repo-002354` `zhanxw/ScopeViewer`（REPRESENTATIVE；parent=QBRC/ScopeViewer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 443 | `kwskws1998/biomni-obs`<br>source=`kwskws1998/Biomni-Obs` | `repo-004232` `kwskws1998/Biomni-Obs`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 444 | `ebispot/duo`<br>source=`EBISPOT/DUO` | `repo-004771` `yarikoptic/DUO`（REPRESENTATIVE；parent=EBISPOT/DUO） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 445 | `andrewsu/scripps-garibaldi-hpc-skill`<br>source=`andrewsu/scripps-garibaldi-hpc-skill` | `repo-000950` `andrewsu/scripps-garibaldi-hpc-skill`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 446 | `topherchris420/james_library`<br>source=`topherchris420/james_library` | `repo-004994` `yarikoptic/james_library`（REPRESENTATIVE；parent=topherchris420/james_library） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 447 | `machine-perception-robotics-group/mouse-geneformer`<br>source=`machine-perception-robotics-group/Mouse-Geneformer` | `repo-006065` `explorerwjy/Mouse-Geneformer`（REPRESENTATIVE；parent=machine-perception-robotics-group/Mouse-Geneformer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 448 | `gabrielkp/enc`<br>source=`GabrielKP/enc` | `repo-004848` `yarikoptic/GabrielKP-enc`（REPRESENTATIVE；parent=GabrielKP/enc） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 449 | `sbl-sdsc/mcp-proto-okn`<br>source=`sbl-sdsc/mcp-proto-okn` | `repo-000927` `andrewsu/mcp-proto-okn`（REPRESENTATIVE；parent=sbl-sdsc/mcp-proto-okn）<br>`repo-002716` `goodb/mcp-proto-okn`（MEMBER；parent=sbl-sdsc/mcp-proto-okn） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 450 | `con/open-brain-consent`<br>source=`con/open-brain-consent` | `repo-005274` `yarikoptic/open-brain-consent`（REPRESENTATIVE；parent=con/open-brain-consent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 451 | `explorerwjy/geneformer`<br>source=`explorerwjy/Geneformer` | `repo-006058` `explorerwjy/Geneformer`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 452 | `jmiao24/paper2agent`<br>source=`jmiao24/Paper2Agent` | `repo-004199` `alexs42/Paper2Agent`（REPRESENTATIVE；parent=jmiao24/Paper2Agent）<br>`repo-007221` `lishengting/Paper2Agent`（MEMBER；parent=jmiao24/Paper2Agent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 453 | `psychoinformatics-de/datalad-concepts`<br>source=`psychoinformatics-de/datalad-concepts` | `repo-004666` `yarikoptic/datalad-concepts`（REPRESENTATIVE；parent=psychoinformatics-de/datalad-concepts） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 454 | `science-will-win/biomlbench`<br>source=`Science-Will-Win/biomlbench` | `repo-004231` `kwskws1998/biomlbench`（REPRESENTATIVE；parent=Science-Will-Win/biomlbench） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 455 | `marcosbolanos/3dna`<br>source=`marcosbolanos/3dna` | `repo-001582` `marcosbolanos/3dna`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 456 | `datalad/datalad-deprecated`<br>source=`datalad/datalad-deprecated` | `repo-004672` `yarikoptic/datalad-deprecated`（REPRESENTATIVE；parent=datalad/datalad-deprecated） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 457 | `biomedical-signal-processing/sleepyland`<br>source=`biomedical-signal-processing/sleepyland` | `repo-006544` `gutendzx/sleepyland`（REPRESENTATIVE；parent=biomedical-signal-processing/sleepyland） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 458 | `datalad/datalad-container`<br>source=`datalad/datalad-container` | `repo-004667` `yarikoptic/datalad-container`（REPRESENTATIVE；parent=datalad/datalad-container） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 459 | `datalad/datalad-neuroimaging`<br>source=`datalad/datalad-neuroimaging` | `repo-004681` `yarikoptic/datalad-neuroimaging`（REPRESENTATIVE；parent=datalad/datalad-neuroimaging） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 460 | `ji-chartsiri/aico`<br>source=`ji-chartsiri/AICO` | `repo-005795` `yaswanth169/AICO`（REPRESENTATIVE；parent=ji-chartsiri/AICO） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 461 | `edison-a-n/cursor-controller-skill`<br>source=`Edison-A-N/cursor-controller-skill` | `repo-001013` `Edison-A-N/cursor-controller-skill`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 462 | `allenneuraldynamics/aind-ephys-pipeline`<br>source=`AllenNeuralDynamics/aind-ephys-pipeline` | `repo-004369` `yarikoptic/aind-ephys-pipeline`（REPRESENTATIVE；parent=AllenNeuralDynamics/aind-ephys-pipeline） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `413–462`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-013-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
