# 远程调研 Batch 024

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **963–1012**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 3 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 1 |
| 分类 `DATASET_OR_BENCHMARK` | 2 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 11 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 15 |
| 分类 `LOW_INFORMATION_RECHECK` | 7 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 10 |
| 标记 `ARCHIVED_OR_DISABLED` | 3 |
| 标记 `CHILD_FORK_SURFACE` | 1 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 38 |
| 标记 `LICENSE_UNCLEAR` | 20 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RECENT_ACTIVE` | 20 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 963 | `andybrandt/mcp-simple-pubmed`<br>source=`andybrandt/mcp-simple-pubmed` | `repo-006611` `psknlr/mcp-simple-pubmed`（REPRESENTATIVE；parent=andybrandt/mcp-simple-pubmed） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 964 | `oxpig/immunebuilder`<br>source=`oxpig/ImmuneBuilder` | `repo-002168` `th86/ImmuneBuilder`（REPRESENTATIVE；parent=oxpig/ImmuneBuilder） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 965 | `openproblems-bio/task_batch_integration`<br>source=`openproblems-bio/task_batch_integration` | `repo-001361` `HelloWorldLTY/task_batch_integration`（REPRESENTATIVE；parent=openproblems-bio/task_batch_integration） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 966 | `thiraput01/cibmtr-equity-in-post-hct-survival-predictions`<br>source=`Thiraput01/CIBMTR-Equity-in-post-HCT-Survival-Predictions` | `repo-004046` `Thiraput01/CIBMTR-Equity-in-post-HCT-Survival-Predictions`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 967 | `drgmk/alma_var`<br>source=`drgmk/alma_var` | `repo-006765` `drgmk/alma_var`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 968 | `abhi1117/healthcare`<br>source=`abhi1117/Healthcare` | `repo-006860` `tangxuan82/Healthcare`（REPRESENTATIVE；parent=abhi1117/Healthcare） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 969 | `kexinhuang12345/nextjs-ai-bio-assistant`<br>source=`kexinhuang12345/nextjs-ai-bio-assistant` | `repo-001509` `kexinhuang12345/nextjs-ai-bio-assistant`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 970 | `interstellar-egypt/dbdataset`<br>source=`interstellar-egypt/dbdataset` | `repo-006135` `SongyouZhong/dbdataset`（REPRESENTATIVE；parent=interstellar-egypt/dbdataset） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 971 | `pmagwene/latex-nihbiosketch`<br>source=`pmagwene/latex-nihbiosketch` | `repo-005033` `yarikoptic/latex-nihbiosketch`（REPRESENTATIVE；parent=pmagwene/latex-nihbiosketch） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 972 | `fzj-inm1-bda/siibra-python`<br>source=`FZJ-INM1-BDA/siibra-python` | `repo-005575` `yarikoptic/siibra-python`（REPRESENTATIVE；parent=FZJ-INM1-BDA/siibra-python） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 973 | `microsoft/biomedclip_data_pipeline`<br>source=`microsoft/BiomedCLIP_data_pipeline` | `repo-006471` `gutendzx/BiomedCLIP_data_pipeline`（REPRESENTATIVE；parent=microsoft/BiomedCLIP_data_pipeline） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 974 | `mobaidoctor/polyp-ddpm`<br>source=`mobaidoctor/polyp-ddpm` | `repo-003299` `Rakshitha-Ireddi/polyp-ddpm`（REPRESENTATIVE；parent=mobaidoctor/polyp-ddpm） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 975 | `samarth-kadaba/tcellai`<br>source=`samarth-kadaba/TCellAI` | `repo-003935` `samarth-kadaba/TCellAI`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 976 | `nersc/podman-hpc`<br>source=`NERSC/podman-hpc` | `repo-005353` `yarikoptic/podman-hpc`（REPRESENTATIVE；parent=NERSC/podman-hpc） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 977 | `imprintlab/medical-sam2`<br>source=`ImprintLab/Medical-SAM2` | `repo-006638` `sszhu/Medical-SAM2`（REPRESENTATIVE；parent=ImprintLab/Medical-SAM2） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 978 | `brainlife/amaretti`<br>source=`brainlife/amaretti` | `repo-004382` `yarikoptic/amaretti`（REPRESENTATIVE；parent=brainlife/amaretti） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 979 | `huang-lab/figure-extractor`<br>source=`Huang-lab/figure-extractor` | `repo-002237` `vlln/figure-extractor`（REPRESENTATIVE；parent=Huang-lab/figure-extractor） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 980 | `goodb/pi-team`<br>source=`goodb/pi-team` | `repo-002719` `goodb/pi-team`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED`、`RECENT_ACTIVE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 981 | `tadata-org/fastapi_mcp`<br>source=`tadata-org/fastapi_mcp` | `repo-001020` `Edison-A-N/fastapi_mcp`（REPRESENTATIVE；parent=tadata-org/fastapi_mcp） | `ARCHIVED_OR_DISABLED` | `FORK_LINEAGE_REQUIRED`、`ARCHIVED_OR_DISABLED`、`RECENT_ACTIVE`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 982 | `kalinnonchev/deepcell`<br>source=`KalinNonchev/DeepCell` | `repo-002997` `KalinNonchev/DeepCell`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED`、`RECENT_ACTIVE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 983 | `opencodeiiita/deepsearov`<br>source=`opencodeiiita/DeepSeaROV` | `repo-006185` `23abdul23/DeepSeaROV`（REPRESENTATIVE；parent=opencodeiiita/DeepSeaROV） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 984 | `dark-peak-analytics/sadm-mk2-demo`<br>source=`dark-peak-analytics/sadm-mk2-demo` | `repo-001624` `marcosbolanos/t1diab-sadm-mk2`（REPRESENTATIVE；parent=dark-peak-analytics/sadm-mk2-demo） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 985 | `ali-maq/variant_annontation_projectx`<br>source=`Ali-Maq/Variant_Annontation_ProjectX` | `repo-006369` `Ali-Maq/Variant_Annontation_ProjectX`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 986 | `sarahhyojin/sleepxvit`<br>source=`sarahhyojin/SleepXViT` | `repo-006542` `gutendzx/SleepXViT`（REPRESENTATIVE；parent=sarahhyojin/SleepXViT） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 987 | `ncihtan/htan2-data-model`<br>source=`ncihtan/htan2-data-model` | `repo-000981` `anngvu/htan-linkml`（REPRESENTATIVE；parent=ncihtan/htan2-data-model） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 988 | `bbfrederick/rapidtide`<br>source=`bbfrederick/rapidtide` | `repo-005477` `yarikoptic/rapidtide`（REPRESENTATIVE；parent=bbfrederick/rapidtide） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 989 | `priyanka9991/pipeline-processing-tcga-slides-for-mil`<br>source=`priyanka9991/Pipeline-Processing-TCGA-Slides-for-MIL` | `repo-006160` `zhuyitan/Pipeline-Processing-TCGA-Slides-for-MIL`（REPRESENTATIVE；parent=priyanka9991/Pipeline-Processing-TCGA-Slides-for-MIL） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 990 | `chaselgrove/repronim.org`<br>source=`chaselgrove/repronim.org` | `repo-005503` `yarikoptic/repronim.org`（REPRESENTATIVE；parent=chaselgrove/repronim.org） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 991 | `monarch-initiative/ontogpt`<br>source=`monarch-initiative/ontogpt` | `repo-005271` `yarikoptic/ontogpt`（REPRESENTATIVE；parent=monarch-initiative/ontogpt）<br>`repo-000937` `andrewsu/ontogpt`（MEMBER；parent=monarch-initiative/ontogpt） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 992 | `ourresearch/openalex-gui`<br>source=`ourresearch/openalex-gui` | `repo-005278` `yarikoptic/openalex-gui`（REPRESENTATIVE；parent=ourresearch/openalex-gui） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 993 | `ourresearch/openalex-guts`<br>source=`ourresearch/openalex-guts` | `repo-005279` `yarikoptic/openalex-guts`（REPRESENTATIVE；parent=ourresearch/openalex-guts） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 994 | `helloworldlty/genestrobot`<br>source=`HelloWorldLTY/GenesTroBot` | `repo-001290` `HelloWorldLTY/GenesTroBot`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 995 | `broadinstitute/tangram`<br>source=`broadinstitute/Tangram` | `repo-001358` `HelloWorldLTY/Tangram`（REPRESENTATIVE；parent=broadinstitute/Tangram） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 996 | `brain-bican/bkbit`<br>source=`brain-bican/bkbit` | `repo-004491` `yarikoptic/bkbit`（REPRESENTATIVE；parent=brain-bican/bkbit） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 997 | `genentech/pascient`<br>source=`Genentech/pascient` | `repo-001327` `HelloWorldLTY/pascient`（REPRESENTATIVE；parent=Genentech/pascient） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 998 | `nf-core/nanostring`<br>source=`nf-core/nanostring` | `repo-004136` `vladsavelyev/nanostring`（REPRESENTATIVE；parent=nf-core/nanostring） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 999 | `leezx/computational-epigenetic-target-discovery`<br>source=`leezx/computational-epigenetic-target-discovery` | `repo-007183` `leezx/computational-epigenetic-target-discovery`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1000 | `mrirecon/bart`<br>source=`mrirecon/bart` | `repo-004432` `yarikoptic/bart`（REPRESENTATIVE；parent=mrirecon/bart） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1001 | `sokrypton/colabdesign`<br>source=`sokrypton/ColabDesign` | `repo-003928` `samarth-kadaba/ColabDesign`（REPRESENTATIVE；parent=sokrypton/ColabDesign） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1002 | `lucidrains/enformer-pytorch`<br>source=`lucidrains/enformer-pytorch` | `repo-001281` `HelloWorldLTY/enformer-pytorch`（REPRESENTATIVE；parent=lucidrains/enformer-pytorch） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1003 | `nextflow-io/nextflow`<br>source=`nextflow-io/nextflow` | `repo-004137` `vladsavelyev/nextflow`（REPRESENTATIVE；parent=nextflow-io/nextflow） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1004 | `opencitations/website`<br>source=`opencitations/website` | `repo-005757` `yarikoptic/website`（REPRESENTATIVE；parent=opencitations/website） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1005 | `opencitations/lucinda`<br>source=`opencitations/lucinda` | `repo-005067` `yarikoptic/lucinda`（REPRESENTATIVE；parent=opencitations/lucinda） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1006 | `ksun63/deepdta-pytorch`<br>source=`KSUN63/DeepDTA-Pytorch` | `repo-007149` `KSUN63/DeepDTA-Pytorch`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1007 | `jonbmartin/pulpy`<br>source=`jonbmartin/pulpy` | `repo-005391` `yarikoptic/pulpy`（REPRESENTATIVE；parent=jonbmartin/pulpy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1008 | `churchlab/deep_diversification_aav`<br>source=`churchlab/Deep_diversification_AAV` | `repo-006839` `tangxuan82/Deep_diversification_AAV`（REPRESENTATIVE；parent=churchlab/Deep_diversification_AAV） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1009 | `bids-standard/legacy-validator`<br>source=`bids-standard/legacy-validator` | `repo-005038` `yarikoptic/legacy-bids-validator`（REPRESENTATIVE；parent=bids-standard/legacy-validator） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1010 | `leezx/computational-protac-development`<br>source=`leezx/computational-PROTAC-development` | `repo-007184` `leezx/computational-PROTAC-development`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1011 | `helloworldlty/robustcell`<br>source=`HelloWorldLTY/RobustCell` | `repo-001333` `HelloWorldLTY/RobustCell`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1012 | `intersect-sdk/python-sdk`<br>source=`INTERSECT-SDK/python-sdk` | `repo-005456` `yarikoptic/python-sdk`（REPRESENTATIVE；parent=INTERSECT-SDK/python-sdk） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `963–1012`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-024-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
