# 远程调研 Batch 011

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **313–362**；**50** 个 family；**51** 条 bounded repository records。

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
| 分类 `DATASET_OR_BENCHMARK` | 1 |
| 分类 `EMPTY_OR_MINIMAL` | 2 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 11 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 22 |
| 分类 `LOW_INFORMATION_RECHECK` | 6 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 6 |
| 标记 `CHILD_FORK_SURFACE` | 7 |
| 标记 `EMPTY_OR_MINIMAL` | 2 |
| 标记 `FORK_LINEAGE_REQUIRED` | 32 |
| 标记 `LICENSE_UNCLEAR` | 26 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RECENT_ACTIVE` | 50 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 313 | `liripo/ai-skills`<br>source=`Liripo/ai-skills` | `repo-003050` `Liripo/ai-skills`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 314 | `pariskang/taotcm-hermes-skillbank`<br>source=`pariskang/TaoTCM-Hermes-SkillBank` | `repo-006625` `psknlr/TaoTCM-Hermes-SkillBank`（REPRESENTATIVE；parent=pariskang/TaoTCM-Hermes-SkillBank） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 315 | `dataarctech/bayesian-agent`<br>source=`DataArcTech/Bayesian-Agent` | `repo-006939` `Vik-u/Bayesian-Agent`（REPRESENTATIVE；parent=DataArcTech/Bayesian-Agent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 316 | `ai4protein/prosst`<br>source=`ai4protein/ProSST` | `repo-001617` `marcosbolanos/ProSST`（REPRESENTATIVE；parent=ai4protein/ProSST） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 317 | `anthropics/claude-ai-mcp`<br>source=`anthropics/claude-ai-mcp` | `repo-002656` `de-grave/claude-ai-mcp`（REPRESENTATIVE；parent=anthropics/claude-ai-mcp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 318 | `stanford-crfm/helm`<br>source=`stanford-crfm/helm` | `repo-001930` `shantanusharma/helm`（REPRESENTATIVE；parent=stanford-crfm/helm）<br>`repo-006433` `chaudhariatul/helm`（MEMBER；parent=stanford-crfm/helm） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 319 | `pyro-ppl/pyro`<br>source=`pyro-ppl/pyro` | `repo-004028` `starboy-3/pyro`（REPRESENTATIVE；parent=pyro-ppl/pyro） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 320 | `reacher-z/wlha`<br>source=`reacher-z/wlha` | `repo-003914` `reacher-z/wlha`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 321 | `datalad/datalad-fuse`<br>source=`datalad/datalad-fuse` | `repo-004676` `yarikoptic/datalad-fuse`（REPRESENTATIVE；parent=datalad/datalad-fuse） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 322 | `pidem/hclsbenchmarks`<br>source=`Pidem/HCLSBenchmarks` | `repo-001696` `Pidem/HCLSBenchmarks`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL`、`RECENT_ACTIVE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 323 | `obophenotype/brain_data_standards_ontologies`<br>source=`obophenotype/brain_data_standards_ontologies` | `repo-004504` `yarikoptic/brain_data_standards_ontologies`（REPRESENTATIVE；parent=obophenotype/brain_data_standards_ontologies） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 324 | `samarth-kadaba/a-very-questionable-scheme-for-gradient-descent`<br>source=`samarth-kadaba/A-Very-Questionable-Scheme-for-Gradient-Descent` | `repo-003922` `samarth-kadaba/A-Very-Questionable-Scheme-for-Gradient-Descent`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 325 | `cbioportal/cbioportal-core`<br>source=`cBioPortal/cbioportal-core` | `repo-002761` `inodb/cbioportal-core`（REPRESENTATIVE；parent=cBioPortal/cbioportal-core） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 326 | `guardians-infrastructure/beacon-v2-nci`<br>source=`GUARDIANS-infrastructure/beacon-v2-nci` | `repo-002653` `de-grave/beacon-v2-nci`（REPRESENTATIVE；parent=GUARDIANS-infrastructure/beacon-v2-nci） | `EMPTY_OR_MINIMAL` | `FORK_LINEAGE_REQUIRED`、`EMPTY_OR_MINIMAL`、`RECENT_ACTIVE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 327 | `scripps-cbb/aws_claude_skill`<br>source=`scripps-cbb/AWS_Claude_Skill` | `repo-002712` `goodb/AWS_Claude_Skill`（REPRESENTATIVE；parent=scripps-cbb/AWS_Claude_Skill） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 328 | `vlln/pdffigures2-zig`<br>source=`vlln/pdffigures2-zig` | `repo-002256` `vlln/pdffigures2-zig`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 329 | `gxl-ai/paperclip`<br>source=`GXL-ai/paperclip` | `repo-001545` `kuanlinhuang/paperclip`（REPRESENTATIVE；parent=GXL-ai/paperclip） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 330 | `cellprofiling/subcellportable`<br>source=`CellProfiling/SubCellPortable` | `repo-007434` `samutiti/SubCellNuc`（REPRESENTATIVE；parent=CellProfiling/SubCellPortable） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 331 | `ancplaboldenburg/bids-manager`<br>source=`ANCPLabOldenburg/BIDS-Manager` | `repo-004463` `yarikoptic/BIDS-Manager`（REPRESENTATIVE；parent=ANCPLabOldenburg/BIDS-Manager） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 332 | `dandi/dandi-archive`<br>source=`dandi/dandi-archive` | `repo-004634` `yarikoptic/dandi-archive`（REPRESENTATIVE；parent=dandi/dandi-archive） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 333 | `anoushkajain/unitrefine`<br>source=`anoushkajain/UnitRefine` | `repo-005715` `yarikoptic/UnitRefine`（REPRESENTATIVE；parent=anoushkajain/UnitRefine） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 334 | `rordenlab/bids-validator-rs`<br>source=`rordenlab/bids-validator-rs` | `repo-004474` `yarikoptic/bids-validator-rs`（REPRESENTATIVE；parent=rordenlab/bids-validator-rs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 335 | `jbwexler/bids-mosaic`<br>source=`jbwexler/bids-mosaic` | `repo-004464` `yarikoptic/bids-mosaic`（REPRESENTATIVE；parent=jbwexler/bids-mosaic） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 336 | `biocompute-objects/bco_documentation`<br>source=`biocompute-objects/BCO_Documentation` | `repo-004440` `yarikoptic/BCO_Documentation`（REPRESENTATIVE；parent=biocompute-objects/BCO_Documentation） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 337 | `irishaze/agentic-rag`<br>source=`Irishaze/agentic-rag` | `repo-004206` `Irishaze/agentic-rag`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 338 | `shengyongniu/mergedna`<br>source=`shengyongniu/mergedna` | `repo-002117` `shengyongniu/mergedna`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 339 | `cpernet/bids_minimize`<br>source=`CPernet/BIDS_minimize` | `repo-004478` `yarikoptic/BIDS_minimize`（REPRESENTATIVE；parent=CPernet/BIDS_minimize） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 340 | `cbioportal/cbioportal-docker-compose`<br>source=`cBioPortal/cbioportal-docker-compose` | `repo-002762` `inodb/cbioportal-docker-compose`（REPRESENTATIVE；parent=cBioPortal/cbioportal-docker-compose） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 341 | `spikeinterface/spikeinterface-gui`<br>source=`SpikeInterface/spikeinterface-gui` | `repo-005617` `yarikoptic/spikeinterface-gui`（REPRESENTATIVE；parent=SpikeInterface/spikeinterface-gui） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 342 | `datalad/datalad-catalog`<br>source=`datalad/datalad-catalog` | `repo-004665` `yarikoptic/datalad-catalog`（REPRESENTATIVE；parent=datalad/datalad-catalog） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 343 | `openneuroorg/onvoc-widget`<br>source=`OpenNeuroOrg/onvoc-widget` | `repo-005273` `yarikoptic/onvoc-widget`（REPRESENTATIVE；parent=OpenNeuroOrg/onvoc-widget） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 344 | `cygnusb/coros-mcp`<br>source=`cygnusb/coros-mcp` | `repo-004284` `PayFv/coros-mcp`（REPRESENTATIVE；parent=cygnusb/coros-mcp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 345 | `researai/autofigure`<br>source=`ResearAI/AutoFigure` | `repo-002224` `vlln/AutoFigure`（REPRESENTATIVE；parent=ResearAI/AutoFigure） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 346 | `songyouzhong/image2smile`<br>source=`SongyouZhong/Image2Smile` | `repo-006139` `SongyouZhong/Image2Smile`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 347 | `zhao-group/primer_design_and_worklists`<br>source=`Zhao-Group/Primer_Design_and_Worklists` | `repo-006997` `Vik-u/Primer_Design_and_Worklists`（REPRESENTATIVE；parent=Zhao-Group/Primer_Design_and_Worklists） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 348 | `vlln/pdffigures-mcp-server`<br>source=`vlln/pdffigures-mcp-server` | `repo-002255` `vlln/pdffigures-mcp-server`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 349 | `marcosbolanos/fitness-landscapes`<br>source=`marcosbolanos/fitness-landscapes` | `repo-001597` `marcosbolanos/fitness-landscapes`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 350 | `nwb-extensions/nwbep-review`<br>source=`nwb-extensions/nwbep-review` | `repo-005164` `yarikoptic/nep-review`（REPRESENTATIVE；parent=nwb-extensions/nwbep-review） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 351 | `helloworldlty/ukbiolm`<br>source=`HelloWorldLTY/UKBioLM` | `repo-001365` `HelloWorldLTY/UKBioLM`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 352 | `helloworldlty/spemo`<br>source=`HelloWorldLTY/spEMO` | `repo-001351` `HelloWorldLTY/spEMO`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 353 | `phenixace/molvibench-open`<br>source=`phenixace/MolViBench-open` | `repo-006983` `Vik-u/MolViBench-open`（REPRESENTATIVE；parent=phenixace/MolViBench-open） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 354 | `jissen706/electricity-magnetism-simulations`<br>source=`jissen706/Electricity-Magnetism-Simulations` | `repo-002930` `jissen706/Electricity-Magnetism-Simulations`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 355 | `accelerationconsortium/matterix`<br>source=`AccelerationConsortium/Matterix` | `repo-006975` `Vik-u/Matterix`（REPRESENTATIVE；parent=AccelerationConsortium/Matterix） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 356 | `grobidorg/grobid`<br>source=`grobidOrg/grobid` | `repo-004911` `yarikoptic/grobid`（REPRESENTATIVE；parent=grobidOrg/grobid） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 357 | `bids-flux/bids-flux-docs`<br>source=`BIDS-flux/BIDS-flux-docs` | `repo-004461` `yarikoptic/BIDS-flux-docs`（REPRESENTATIVE；parent=BIDS-flux/BIDS-flux-docs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 358 | `ayushmaniar/powerpoint-mcp`<br>source=`Ayushmaniar/powerpoint-mcp` | `repo-002449` `Ayushmaniar/powerpoint-mcp`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 359 | `goodb/saw-rnaseq-dogfood`<br>source=`goodb/saw-rnaseq-dogfood` | `repo-002720` `goodb/saw-rnaseq-dogfood`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 360 | `vincentcchu/cell_agents`<br>source=`Vincentcchu/cell_agents` | `repo-006394` `Vincentcchu/cell_agents`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 361 | `vincentcchu/celltypeeval`<br>source=`Vincentcchu/CellTypeEval` | `repo-006396` `Vincentcchu/CellTypeEval`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 362 | `helloworldlty/hygieia`<br>source=`HelloWorldLTY/hygieia` | `repo-001304` `HelloWorldLTY/hygieia`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |

## 完整性边界

- 本文件连续覆盖 orders `313–362`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-011-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
