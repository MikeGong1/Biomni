# 远程调研 Batch 010

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **263–312**；**50** 个 family；**56** 条 bounded repository records。

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
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 12 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 19 |
| 分类 `LOW_INFORMATION_RECHECK` | 9 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 5 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `FORK_LINEAGE_REQUIRED` | 30 |
| 标记 `LICENSE_UNCLEAR` | 29 |
| 标记 `MULTI_MEMBER_FAMILY` | 3 |
| 标记 `RECENT_ACTIVE` | 50 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 263 | `katarinayuan/awesome-single-cell-foundation`<br>source=`KatarinaYuan/awesome-single-cell-foundation` | `repo-002976` `KalinNonchev/awesome-single-cell-foundation`（REPRESENTATIVE；parent=KatarinaYuan/awesome-single-cell-foundation） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 264 | `juntaic7/awesome-single-cell-foundation-models`<br>source=`juntaic7/Awesome-Single-Cell-Foundation-Models` | `repo-002977` `KalinNonchev/Awesome-Single-Cell-Foundation-Models`（REPRESENTATIVE；parent=juntaic7/Awesome-Single-Cell-Foundation-Models） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 265 | `con/git-annex`<br>source=`con/git-annex` | `repo-004677` `yarikoptic/datalad-git-annex`（REPRESENTATIVE；parent=con/git-annex） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 266 | `mindsdb/mindshub`<br>source=`mindsdb/mindshub` | `repo-001975` `shantanusharma/mindsdb`（REPRESENTATIVE；parent=mindsdb/mindshub） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 267 | `vlln/paperutils`<br>source=`vlln/paperutils` | `repo-002252` `vlln/paperutils`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 268 | `vlln/skit`<br>source=`vlln/skit` | `repo-002262` `vlln/skit`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE`、`RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 269 | `vlln/mineru-api-skill`<br>source=`vlln/mineru-api-skill` | `repo-002247` `vlln/mineru-api-skill`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 270 | `vlln/background-task-skill`<br>source=`vlln/background-task-skill` | `repo-002227` `vlln/background-task-skill`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 271 | `noone-dash/md-lab`<br>source=`Noone-Dash/md-lab` | `repo-006976` `Vik-u/md-lab`（REPRESENTATIVE；parent=Noone-Dash/md-lab） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 272 | `nkalavros/headlessagents-rankings`<br>source=`NKalavros/headlessagents-rankings` | `repo-007271` `NKalavros/headlessagents-rankings`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 273 | `pariskang/bone-bioinformetics`<br>source=`pariskang/Bone-Bioinformetics` | `repo-006603` `psknlr/Bone-Bioinformetics`（REPRESENTATIVE；parent=pariskang/Bone-Bioinformetics） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 274 | `nvidia-bionemo/proteina-complexa`<br>source=`NVIDIA-BioNeMo/Proteina-Complexa` | `repo-001804` `sbonner0/Proteina-Complexa`（REPRESENTATIVE；parent=NVIDIA-BioNeMo/Proteina-Complexa） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 275 | `synthetic-sciences/openscience`<br>source=`synthetic-sciences/openscience` | `repo-002667` `de-grave/openscience`（REPRESENTATIVE；parent=synthetic-sciences/openscience） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 276 | `manu-tej/ai-scientists`<br>source=`manu-tej/ai-scientists` | `repo-007226` `manu-tej/ai-scientists`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 277 | `claimbound/claimbound-evidence`<br>source=`ClaimBound/claimbound-evidence` | `repo-004555` `yarikoptic/claimbound-evidence`（REPRESENTATIVE；parent=ClaimBound/claimbound-evidence） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 278 | `freedomintelligence/openclaw-medical-skills`<br>source=`FreedomIntelligence/OpenClaw-Medical-Skills` | `repo-002665` `de-grave/OpenClaw-Medical-Skills`（REPRESENTATIVE；parent=FreedomIntelligence/OpenClaw-Medical-Skills） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 279 | `akhiliyengar/simvault`<br>source=`akhiliyengar/SimVault` | `repo-007009` `Vik-u/SimVault`（REPRESENTATIVE；parent=akhiliyengar/SimVault） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 280 | `kwskws1998/masked_ae_atari_and_cognitive_task`<br>source=`kwskws1998/masked_ae_atari_and_cognitive_task` | `repo-004251` `kwskws1998/masked_ae_atari_and_cognitive_task`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 281 | `helloworldlty/lamdna`<br>source=`HelloWorldLTY/LAMDNA` | `repo-001307` `HelloWorldLTY/LAMDNA`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 282 | `andrewsu/dn-meta-analysis`<br>source=`andrewsu/DN-meta-analysis` | `repo-000908` `andrewsu/DN-meta-analysis`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 283 | `bettercodebetterscience/book`<br>source=`BetterCodeBetterScience/book` | `repo-004439` `yarikoptic/bcbs-book`（REPRESENTATIVE；parent=BetterCodeBetterScience/book） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 284 | `bettercodebetterscience/bettercode`<br>source=`BetterCodeBetterScience/bettercode` | `repo-004449` `yarikoptic/bettercode`（REPRESENTATIVE；parent=BetterCodeBetterScience/bettercode） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 285 | `frink-okn/okn-registry`<br>source=`frink-okn/okn-registry` | `repo-000936` `andrewsu/okn-registry`（REPRESENTATIVE；parent=frink-okn/okn-registry） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 286 | `shengyongniu/multimodal-rag`<br>source=`shengyongniu/multimodal-rag` | `repo-002120` `shengyongniu/multimodal-rag`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 287 | `helloworldlty/depression_detection`<br>source=`HelloWorldLTY/depression_detection` | `repo-001275` `HelloWorldLTY/depression_detection`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 288 | `huang-lab/fastvep`<br>source=`Huang-lab/fastVEP` | `repo-002793` `inodb/fastVEP`（REPRESENTATIVE；parent=Huang-lab/fastVEP） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 289 | `drgmk/sdf`<br>source=`drgmk/sdf` | `repo-006790` `drgmk/sdf`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 290 | `vlln/subagents-skill`<br>source=`vlln/subagents-skill` | `repo-002263` `vlln/subagents-skill`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 291 | `cbioportal/datahub`<br>source=`cBioPortal/datahub` | `repo-002783` `inodb/datahub`（REPRESENTATIVE；parent=cBioPortal/datahub）<br>`repo-007070` `jaybee84/datahub`（MEMBER；parent=cBioPortal/datahub） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 292 | `latchbio/biosecbench-refusal`<br>source=`latchbio/biosecbench-refusal` | `repo-006943` `Vik-u/biosecbench-refusal`（REPRESENTATIVE；parent=latchbio/biosecbench-refusal） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 293 | `medarc-ai/medmarks`<br>source=`MedARC-AI/medmarks` | `repo-001700` `Pidem/medmarks`（REPRESENTATIVE；parent=MedARC-AI/medmarks）<br>`repo-003281` `Rakshitha-Ireddi/med-lm-envs`（MEMBER；parent=MedARC-AI/medmarks） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 294 | `vlln/skills-source`<br>source=`vlln/skills-source` | `repo-002261` `vlln/skills-source`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 295 | `vlln/remote-exec-skill`<br>source=`vlln/remote-exec-skill` | `repo-002260` `vlln/remote-exec-skill`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 296 | `vlln/autofigure-skill`<br>source=`vlln/autofigure-skill` | `repo-002225` `vlln/autofigure-skill`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 297 | `vlln/quay-skill`<br>source=`vlln/quay-skill` | `repo-002258` `vlln/quay-skill`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 298 | `cbioportal/cbioportal-navigator`<br>source=`cBioPortal/cbioportal-navigator` | `repo-002766` `inodb/cbioportal-navigator`（REPRESENTATIVE；parent=cBioPortal/cbioportal-navigator） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 299 | `rejuve-bio/ai-assistant`<br>source=`rejuve-bio/AI-Assistant` | `repo-006079` `kewserseid/AI-Assistant`（REPRESENTATIVE；parent=rejuve-bio/AI-Assistant） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 300 | `canlab/canlabcore`<br>source=`canlab/CanlabCore` | `repo-004534` `yarikoptic/CanlabCore`（REPRESENTATIVE；parent=canlab/CanlabCore） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 301 | `allenneuraldynamics/authorshipextractor`<br>source=`AllenNeuralDynamics/AuthorshipExtractor` | `repo-004414` `yarikoptic/AuthorshipExtractor`（REPRESENTATIVE；parent=AllenNeuralDynamics/AuthorshipExtractor） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 302 | `nvidia-bionemo/bionemo-agent-toolkit`<br>source=`NVIDIA-BioNeMo/bionemo-agent-toolkit` | `repo-002654` `de-grave/bionemo-agent-toolkit`（REPRESENTATIVE；parent=NVIDIA-BioNeMo/bionemo-agent-toolkit） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 303 | `lancelot-xie/supergoal`<br>source=`Lancelot-Xie/Supergoal` | `repo-006380` `Lancelot-Xie/Supergoal`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 304 | `avivsinai/langfuse-mcp`<br>source=`avivsinai/langfuse-mcp` | `repo-001028` `Edison-A-N/langfuse-mcp`（REPRESENTATIVE；parent=avivsinai/langfuse-mcp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 305 | `cbioportal/oncotree`<br>source=`cBioPortal/oncotree` | `repo-002839` `inodb/oncotree`（REPRESENTATIVE；parent=cBioPortal/oncotree） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 306 | `arcinstitute/evo2`<br>source=`ArcInstitute/evo2` | `repo-001890` `shantanusharma/evo2`（REPRESENTATIVE；parent=ArcInstitute/evo2）<br>`repo-001285` `HelloWorldLTY/evo2`（MEMBER；parent=ArcInstitute/evo2）<br>`repo-005913` `dabulseco/evo2`（MEMBER；parent=ArcInstitute/evo2）<br>`repo-006267` `alexj-lee/evo2`（MEMBER；parent=ArcInstitute/evo2）<br>`repo-006962` `Vik-u/evo2`（MEMBER；parent=ArcInstitute/evo2） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 307 | `vik-u/molecule-name-lookup`<br>source=`Vik-u/molecule-name-lookup` | `repo-006982` `Vik-u/molecule-name-lookup`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 308 | `nipreps/petprep`<br>source=`nipreps/petprep` | `repo-005327` `yarikoptic/petprep`（REPRESENTATIVE；parent=nipreps/petprep） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 309 | `bcmcpher/my-skills`<br>source=`bcmcpher/my-skills` | `repo-005143` `yarikoptic/my-skills`（REPRESENTATIVE；parent=bcmcpher/my-skills） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 310 | `robacon/mobspy`<br>source=`ROBACON/mobspy` | `repo-005117` `yarikoptic/mobspy`（REPRESENTATIVE；parent=ROBACON/mobspy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 311 | `harrydirk41/conformflow`<br>source=`Harrydirk41/ConformFlow` | `repo-002726` `Harrydirk41/ConformFlow`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 312 | `stanfordnlp/pyvene`<br>source=`stanfordnlp/pyvene` | `repo-004030` `starboy-3/pyvene`（REPRESENTATIVE；parent=stanfordnlp/pyvene） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `263–312`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-010-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
