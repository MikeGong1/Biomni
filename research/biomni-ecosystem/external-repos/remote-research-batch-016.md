# 远程调研 Batch 016

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **563–612**；**50** 个 family；**53** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 53 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 2 |
| 分类 `DATASET_OR_BENCHMARK` | 7 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 11 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 17 |
| 分类 `LOW_INFORMATION_RECHECK` | 5 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 7 |
| 标记 `CHILD_FORK_SURFACE` | 1 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 40 |
| 标记 `LICENSE_UNCLEAR` | 25 |
| 标记 `MULTI_MEMBER_FAMILY` | 2 |
| 标记 `RECENT_ACTIVE` | 50 |
| 标记 `RELEASE_SURFACE` | 2 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 563 | `clbarnes/ozx-tck`<br>source=`clbarnes/ozx-tck` | `repo-005309` `yarikoptic/ozx-tck`（REPRESENTATIVE；parent=clbarnes/ozx-tck） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 564 | `timescale/pg-aiguide`<br>source=`timescale/pg-aiguide` | `repo-005961` `dabulseco/pg-aiguide`（REPRESENTATIVE；parent=timescale/pg-aiguide） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 565 | `steipete/claude-code-mcp`<br>source=`steipete/claude-code-mcp` | `repo-004558` `yarikoptic/claude-code-mcp`（REPRESENTATIVE；parent=steipete/claude-code-mcp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 566 | `hed-standard/hed-lsp`<br>source=`hed-standard/hed-lsp` | `repo-004939` `yarikoptic/hed-lsp`（REPRESENTATIVE；parent=hed-standard/hed-lsp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 567 | `papersgpt/papersgpt-for-zotero`<br>source=`papersgpt/papersgpt-for-zotero` | `repo-005316` `yarikoptic/papersgpt-for-zotero`（REPRESENTATIVE；parent=papersgpt/papersgpt-for-zotero） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 568 | `marcosbolanos/mlbionetw`<br>source=`marcosbolanos/mlbionetw` | `repo-001607` `marcosbolanos/mlbionetw`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 569 | `datalad/datalad-next`<br>source=`datalad/datalad-next` | `repo-004682` `yarikoptic/datalad-next`（REPRESENTATIVE；parent=datalad/datalad-next） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 570 | `songyouzhong/admetexttracter`<br>source=`SongyouZhong/AdmetExttracter` | `repo-006129` `SongyouZhong/AdmetExttracter`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 571 | `idptools/starling`<br>source=`idptools/starling` | `repo-006893` `tangxuan82/starling`（REPRESENTATIVE；parent=idptools/starling） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 572 | `aplbrain/bbqs-ember-data-model`<br>source=`aplbrain/BBQS-EMBER-Data-Model` | `repo-004438` `yarikoptic/BBQS-EMBER-Data-Model`（REPRESENTATIVE；parent=aplbrain/BBQS-EMBER-Data-Model） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 573 | `nipreps/fmriprep`<br>source=`nipreps/fmriprep` | `repo-004834` `yarikoptic/fmriprep`（REPRESENTATIVE；parent=nipreps/fmriprep） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 574 | `yahskapar/personal-health-insights-agent`<br>source=`yahskapar/personal-health-insights-agent` | `repo-006520` `gutendzx/personal-health-insights-agent`（REPRESENTATIVE；parent=yahskapar/personal-health-insights-agent） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 575 | `li-group/scchat`<br>source=`li-group/scChat` | `repo-006403` `Vincentcchu/scChat`（REPRESENTATIVE；parent=li-group/scChat） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 576 | `sakanaai/ai-scientist`<br>source=`SakanaAI/AI-Scientist` | `repo-001831` `shantanusharma/AI-Scientist`（REPRESENTATIVE；parent=SakanaAI/AI-Scientist） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 577 | `siavashre/omkar`<br>source=`siavashre/OMKar` | `repo-006388` `siavashre/OMKar`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 578 | `mahmoodlab/hest`<br>source=`mahmoodlab/HEST` | `repo-003003` `KalinNonchev/HEST`（REPRESENTATIVE；parent=mahmoodlab/HEST） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 579 | `annotation-garden/hedit`<br>source=`Annotation-Garden/HEDit` | `repo-004943` `yarikoptic/HEDit`（REPRESENTATIVE；parent=Annotation-Garden/HEDit） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 580 | `bgi-hangzhouai/genos`<br>source=`BGI-HangzhouAI/Genos` | `repo-007217` `lishengting/Genos`（REPRESENTATIVE；parent=BGI-HangzhouAI/Genos） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 581 | `poldrack/bettercodebetterscience`<br>source=`poldrack/BetterCodeBetterScience` | `repo-004450` `yarikoptic/BetterCodeBetterScience`（REPRESENTATIVE；parent=poldrack/BetterCodeBetterScience） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 582 | `som-shahlab/femr`<br>source=`som-shahlab/femr` | `repo-006427` `chaudhariatul/femr`（REPRESENTATIVE；parent=som-shahlab/femr） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 583 | `beehiveinnovations/pal-mcp-server`<br>source=`BeehiveInnovations/pal-mcp-server` | `repo-004198` `alexs42/pal-mcp-server`（REPRESENTATIVE；parent=BeehiveInnovations/pal-mcp-server） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 584 | `mahmoodlab/titan`<br>source=`mahmoodlab/TITAN` | `repo-006448` `chaudhariatul/TITAN`（REPRESENTATIVE；parent=mahmoodlab/TITAN） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 585 | `prov-gigatime/gigatime`<br>source=`prov-gigatime/GigaTIME` | `repo-001292` `HelloWorldLTY/GigaTIME`（REPRESENTATIVE；parent=prov-gigatime/GigaTIME） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 586 | `pubmedqa/pubmedqa`<br>source=`pubmedqa/pubmedqa` | `repo-006444` `chaudhariatul/pubmedqa`（REPRESENTATIVE；parent=pubmedqa/pubmedqa） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 587 | `drgmk/vis-r`<br>source=`drgmk/vis-r` | `repo-006794` `drgmk/vis-r`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 588 | `hanjiechen/challengeclinicalqa`<br>source=`HanjieChen/ChallengeClinicalQA` | `repo-006423` `chaudhariatul/ChallengeClinicalQA`（REPRESENTATIVE；parent=HanjieChen/ChallengeClinicalQA） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 589 | `aghie/head-qa`<br>source=`aghie/head-qa` | `repo-006431` `chaudhariatul/head-qa`（REPRESENTATIVE；parent=aghie/head-qa） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 590 | `glee4810/ehrsql`<br>source=`glee4810/EHRSQL` | `repo-006426` `chaudhariatul/EHRSQL`（REPRESENTATIVE；parent=glee4810/EHRSQL） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 591 | `ncbi-nlp/medcalc-bench`<br>source=`ncbi-nlp/MedCalc-Bench` | `repo-006436` `chaudhariatul/MedCalc-Bench`（REPRESENTATIVE；parent=ncbi-nlp/MedCalc-Bench） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 592 | `chahat08/stereocell`<br>source=`Chahat08/StereoCell` | `repo-002549` `Chahat08/StereoCell`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 593 | `harmonizedmri/pulceq`<br>source=`HarmonizedMRI/PulCeq` | `repo-005390` `yarikoptic/PulCeq`（REPRESENTATIVE；parent=HarmonizedMRI/PulCeq） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 594 | `nigmat-future/mcp-manager`<br>source=`Nigmat-future/MCP-manager` | `repo-003186` `Nigmat-future/MCP-manager`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 595 | `muisedestiny/zotero-gpt`<br>source=`MuiseDestiny/zotero-gpt` | `repo-005788` `yarikoptic/zotero-gpt`（REPRESENTATIVE；parent=MuiseDestiny/zotero-gpt） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 596 | `ruuderesearch/sleepbench`<br>source=`RuudeResearch/SleepBench` | `repo-006535` `gutendzx/SleepBench`（REPRESENTATIVE；parent=RuudeResearch/SleepBench） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 597 | `ihtsdo/sct-browser-frontend`<br>source=`IHTSDO/sct-browser-frontend` | `repo-005556` `yarikoptic/sct-browser-frontend`（REPRESENTATIVE；parent=IHTSDO/sct-browser-frontend） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 598 | `lestropie/ip-freely`<br>source=`Lestropie/IP-freely` | `repo-004985` `yarikoptic/IP-freely`（REPRESENTATIVE；parent=Lestropie/IP-freely） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 599 | `nigmat-future/medinterprint`<br>source=`Nigmat-future/MedInterprint` | `repo-003187` `Nigmat-future/MedInterprint`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 600 | `msdllcpapers/ovo`<br>source=`MSDLLCpapers/ovo` | `repo-006993` `Vik-u/ovo`（REPRESENTATIVE；parent=MSDLLCpapers/ovo） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 601 | `sdean-group/stochastic-node-dmd`<br>source=`sdean-group/Stochastic-NODE-DMD` | `repo-003318` `Rakshitha-Ireddi/Stochastic-NODE-DMD`（REPRESENTATIVE；parent=sdean-group/Stochastic-NODE-DMD） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 602 | `neurolabusc/niivue-binder`<br>source=`neurolabusc/niivue-binder` | `repo-005218` `yarikoptic/niivue-binder`（REPRESENTATIVE；parent=neurolabusc/niivue-binder） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 603 | `leezx/wetlab`<br>source=`leezx/WetLab` | `repo-007212` `leezx/WetLab`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 604 | `harsha-simhadri/big-ann-benchmarks`<br>source=`harsha-simhadri/big-ann-benchmarks` | `repo-006422` `chaudhariatul/big-ann-benchmarks`（REPRESENTATIVE；parent=harsha-simhadri/big-ann-benchmarks） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 605 | `duecredit/duecredit`<br>source=`duecredit/duecredit` | `repo-004769` `yarikoptic/duecredit`（REPRESENTATIVE；parent=duecredit/duecredit） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 606 | `future-house/robin`<br>source=`Future-House/robin` | `repo-006116` `leizhou69/robin`（REPRESENTATIVE；parent=Future-House/robin）<br>`repo-002124` `shengyongniu/robin`（MEMBER；parent=Future-House/robin） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 607 | `robotic-decision-making-lab/pybravo`<br>source=`Robotic-Decision-Making-Lab/pybravo` | `repo-006999` `Vik-u/pybravo`（REPRESENTATIVE；parent=Robotic-Decision-Making-Lab/pybravo） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 608 | `vik-u/petaseagent`<br>source=`Vik-u/PETaseAgent` | `repo-006996` `Vik-u/PETaseAgent`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL`、`RECENT_ACTIVE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 609 | `biomap-research/scfoundation`<br>source=`biomap-research/scFoundation` | `repo-006887` `tangxuan82/scFoundation`（REPRESENTATIVE；parent=biomap-research/scFoundation）<br>`repo-001340` `HelloWorldLTY/scFoundation`（MEMBER；parent=biomap-research/scFoundation）<br>`repo-007121` `jaybee84/scFoundation`（MEMBER；parent=biomap-research/scFoundation） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 610 | `google-health/consumer-health-research`<br>source=`Google-Health/consumer-health-research` | `repo-006482` `gutendzx/consumer-health-research`（REPRESENTATIVE；parent=Google-Health/consumer-health-research） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 611 | `microsoft/cleavenet`<br>source=`microsoft/cleavenet` | `repo-005896` `dabulseco/cleavenet`（REPRESENTATIVE；parent=microsoft/cleavenet） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 612 | `songyouzhong/ai_retrosynthetic_analysis`<br>source=`SongyouZhong/AI_Retrosynthetic_Analysis` | `repo-006130` `SongyouZhong/AI_Retrosynthetic_Analysis`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |

## 完整性边界

- 本文件连续覆盖 orders `563–612`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-016-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
