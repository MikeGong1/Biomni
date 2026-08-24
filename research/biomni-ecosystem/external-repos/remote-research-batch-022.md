# 远程调研 Batch 022

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **863–912**；**50** 个 family；**52** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 52 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 3 |
| 分类 `DATASET_OR_BENCHMARK` | 4 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 12 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 22 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 8 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 44 |
| 标记 `LICENSE_UNCLEAR` | 21 |
| 标记 `MULTI_MEMBER_FAMILY` | 2 |
| 标记 `RECENT_ACTIVE` | 50 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 863 | `deng-guifeng/lpsgm`<br>source=`Deng-GuiFeng/LPSGM` | `repo-006507` `gutendzx/LPSGM`（REPRESENTATIVE；parent=Deng-GuiFeng/LPSGM） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 864 | `conda-forge/heudiconv-feedstock`<br>source=`conda-forge/heudiconv-feedstock` | `repo-004947` `yarikoptic/heudiconv-feedstock`（REPRESENTATIVE；parent=conda-forge/heudiconv-feedstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 865 | `shaunporwal/dicom-mcp`<br>source=`shaunporwal/DICOM-MCP` | `repo-007468` `shaunporwal/DICOM-MCP`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 866 | `gcorso/diffdock`<br>source=`gcorso/DiffDock` | `repo-006956` `Vik-u/DiffDock`（REPRESENTATIVE；parent=gcorso/DiffDock）<br>`repo-007150` `KSUN63/DiffDock`（MEMBER；parent=gcorso/DiffDock） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 867 | `knowledge-graph-hub/knowledge-graph-hub.github.io`<br>source=`Knowledge-Graph-Hub/knowledge-graph-hub.github.io` | `repo-000923` `andrewsu/knowledge-graph-hub.github.io`（REPRESENTATIVE；parent=Knowledge-Graph-Hub/knowledge-graph-hub.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 868 | `cbica/nichart_project`<br>source=`CBICA/NiChart_Project` | `repo-005209` `yarikoptic/NiChart_Project`（REPRESENTATIVE；parent=CBICA/NiChart_Project） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 869 | `ibm/materials`<br>source=`IBM/materials` | `repo-002409` `aevo98765/materials`（REPRESENTATIVE；parent=IBM/materials） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 870 | `ryanding26/diabetes-classifier`<br>source=`ryanDing26/Diabetes-Classifier` | `repo-001732` `ryanDing26/Diabetes-Classifier`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 871 | `fdu-harry/xsleepfusion`<br>source=`fdu-harry/XSleepFusion` | `repo-006561` `gutendzx/XSleepFusion`（REPRESENTATIVE；parent=fdu-harry/XSleepFusion） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 872 | `mad-lab-fau/sleep_analysis`<br>source=`mad-lab-fau/sleep_analysis` | `repo-006534` `gutendzx/sleep_analysis`（REPRESENTATIVE；parent=mad-lab-fau/sleep_analysis） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 873 | `scholarly-python-package/scholarly`<br>source=`scholarly-python-package/scholarly` | `repo-005545` `yarikoptic/scholarly`（REPRESENTATIVE；parent=scholarly-python-package/scholarly） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 874 | `benevolentai/molbert`<br>source=`BenevolentAI/MolBERT` | `repo-007157` `KSUN63/MolBERT`（REPRESENTATIVE；parent=BenevolentAI/MolBERT） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 875 | `colinvdb/bmat`<br>source=`ColinVDB/BMAT` | `repo-004495` `yarikoptic/BMAT`（REPRESENTATIVE；parent=ColinVDB/BMAT） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 876 | `talmolab/sleap-io`<br>source=`talmolab/sleap-io` | `repo-005591` `yarikoptic/sleap-io`（REPRESENTATIVE；parent=talmolab/sleap-io） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 877 | `tmglncc/cartmath`<br>source=`tmglncc/CARTmath` | `repo-002582` `changwn/CARTmath`（REPRESENTATIVE；parent=tmglncc/CARTmath） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 878 | `cdluc3/dmptool`<br>source=`CDLUC3/dmptool` | `repo-004735` `yarikoptic/dmptool-1`（REPRESENTATIVE；parent=CDLUC3/dmptool） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 879 | `ncatstranslator/translatorengineering`<br>source=`NCATSTranslator/TranslatorEngineering` | `repo-000962` `andrewsu/TranslatorArchitecture`（REPRESENTATIVE；parent=NCATSTranslator/TranslatorEngineering） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 880 | `smithanarasimhamurthy/digitaltwin`<br>source=`SmithaNarasimhamurthy/digitaltwin` | `repo-006849` `tangxuan82/digitaltwin2`（REPRESENTATIVE；parent=SmithaNarasimhamurthy/digitaltwin） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 881 | `nickzren/hetionet`<br>source=`nickzren/hetionet` | `repo-001800` `sbonner0/hetionet`（REPRESENTATIVE；parent=nickzren/hetionet） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 882 | `inveniosoftware/invenio-app-rdm`<br>source=`inveniosoftware/invenio-app-rdm` | `repo-004982` `yarikoptic/invenio-app-rdm`（REPRESENTATIVE；parent=inveniosoftware/invenio-app-rdm） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 883 | `nationalgenomicsinfrastructure/multiqc_ngi`<br>source=`NationalGenomicsInfrastructure/MultiQC_NGI` | `repo-004133` `vladsavelyev/MultiQC_NGI`（REPRESENTATIVE；parent=NationalGenomicsInfrastructure/MultiQC_NGI） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 884 | `ali-maq/clinvar-query-system`<br>source=`Ali-Maq/clinvar-query-system` | `repo-006307` `Ali-Maq/clinvar-query-system`（REPRESENTATIVE） | `EMPTY_OR_MINIMAL` | `LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL`、`RECENT_ACTIVE` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 885 | `digitalslidearchive/digital_slide_archive`<br>source=`DigitalSlideArchive/digital_slide_archive` | `repo-004723` `yarikoptic/digital_slide_archive`（REPRESENTATIVE；parent=DigitalSlideArchive/digital_slide_archive） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 886 | `ali-maq/civic-benchmark-dataset-creation`<br>source=`Ali-Maq/civic-benchmark-dataset-creation` | `repo-006302` `Ali-Maq/civic-benchmark-dataset-creation`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 887 | `fairsharing/fairsharing.github.io`<br>source=`FAIRsharing/fairsharing.github.io` | `repo-004814` `yarikoptic/fairsharing.github.io`（REPRESENTATIVE；parent=FAIRsharing/fairsharing.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 888 | `sbhakim/ansr-dt`<br>source=`sbhakim/ansr-dt` | `repo-006829` `tangxuan82/ansr-dt`（REPRESENTATIVE；parent=sbhakim/ansr-dt） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 889 | `jackkuo666/pubmed-mcp-server`<br>source=`JackKuo666/PubMed-MCP-Server` | `repo-006617` `psknlr/PubMed-MCP-Server`（REPRESENTATIVE；parent=JackKuo666/PubMed-MCP-Server） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 890 | `griffithlab/civic-docs`<br>source=`griffithlab/civic-docs` | `repo-006303` `Ali-Maq/civic-docs_api`（REPRESENTATIVE；parent=griffithlab/civic-docs） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 891 | `incf-nidash/pynidm`<br>source=`incf-nidash/PyNIDM` | `repo-005424` `yarikoptic/PyNIDM`（REPRESENTATIVE；parent=incf-nidash/PyNIDM） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 892 | `shaunporwal/dicom-viewer`<br>source=`shaunporwal/dicom-viewer` | `repo-007469` `shaunporwal/dicom-viewer`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 893 | `juliacamps/cardiac-digital-twin`<br>source=`juliacamps/Cardiac-Digital-Twin` | `repo-006833` `tangxuan82/Cardiac-Digital-Twin`（REPRESENTATIVE；parent=juliacamps/Cardiac-Digital-Twin） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 894 | `darkroaster/pubmearch`<br>source=`Darkroaster/pubmearch` | `repo-006616` `psknlr/pubmearch`（REPRESENTATIVE；parent=Darkroaster/pubmearch） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 895 | `openags/paper-search-mcp`<br>source=`openags/paper-search-mcp` | `repo-006614` `psknlr/paper-search-mcp`（REPRESENTATIVE；parent=openags/paper-search-mcp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 896 | `ohbm/ossig`<br>source=`ohbm/ossig` | `repo-005304` `yarikoptic/ossig`（REPRESENTATIVE；parent=ohbm/ossig） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 897 | `anjany/verse`<br>source=`anjany/verse` | `repo-005732` `yarikoptic/verse`（REPRESENTATIVE；parent=anjany/verse） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 898 | `ohbm/hackathon2025`<br>source=`ohbm/hackathon2025` | `repo-004917` `yarikoptic/hackathon2025`（REPRESENTATIVE；parent=ohbm/hackathon2025） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 899 | `niivue/ipyniivue`<br>source=`niivue/ipyniivue` | `repo-004987` `yarikoptic/ipyniivue`（REPRESENTATIVE；parent=niivue/ipyniivue） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 900 | `niivue/brain2print`<br>source=`niivue/brain2print` | `repo-004503` `yarikoptic/brain2print`（REPRESENTATIVE；parent=niivue/brain2print） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 901 | `qiicr/dcmqi`<br>source=`QIICR/dcmqi` | `repo-004701` `yarikoptic/dcmqi`（REPRESENTATIVE；parent=QIICR/dcmqi） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 902 | `wonderwhy-er/desktopcommandermcp`<br>source=`wonderwhy-er/DesktopCommanderMCP` | `repo-004716` `yarikoptic/DesktopCommanderMCP`（REPRESENTATIVE；parent=wonderwhy-er/DesktopCommanderMCP） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 903 | `jxzb1988/mmqtl`<br>source=`jxzb1988/MMQTL` | `repo-004273` `MikeGong1/MMQTL-sourcecode`（REPRESENTATIVE；parent=jxzb1988/MMQTL） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 904 | `pydicom/dicom-validator`<br>source=`pydicom/dicom-validator` | `repo-004720` `yarikoptic/dicom-validator`（REPRESENTATIVE；parent=pydicom/dicom-validator） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 905 | `amir-hofo/eegnet`<br>source=`Amir-Hofo/EEGNet` | `repo-004238` `kwskws1998/EEGNet`（REPRESENTATIVE；parent=Amir-Hofo/EEGNet） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 906 | `allysonlister/swo`<br>source=`allysonlister/swo` | `repo-005645` `yarikoptic/swo`（REPRESENTATIVE；parent=allysonlister/swo）<br>`repo-007371` `tschaffter/swo`（MEMBER；parent=allysonlister/swo） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`MULTI_MEMBER_FAMILY`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 907 | `fairplus/the-fair-cookbook`<br>source=`FAIRplus/the-fair-cookbook` | `repo-005687` `yarikoptic/the-fair-cookbook`（REPRESENTATIVE；parent=FAIRplus/the-fair-cookbook） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 908 | `vinnysha/grandhack-cardiosense`<br>source=`VinnySha/GrandHack-CardioSense` | `repo-007500` `VinnySha/GrandHack-CardioSense`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 909 | `niivue/niivue`<br>source=`niivue/niivue` | `repo-005217` `yarikoptic/niivue`（REPRESENTATIVE；parent=niivue/niivue） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 910 | `yyzharry/vlm-fairness`<br>source=`YyzHarry/vlm-fairness` | `repo-006556` `gutendzx/vlm-fairness`（REPRESENTATIVE；parent=YyzHarry/vlm-fairness） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 911 | `theislab/atlas-feature-selection-benchmark`<br>source=`theislab/atlas-feature-selection-benchmark` | `repo-003051` `Liripo/atlas-feature-selection-benchmark`（REPRESENTATIVE；parent=theislab/atlas-feature-selection-benchmark） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`RECENT_ACTIVE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 912 | `magland/neurosift-mcps`<br>source=`magland/neurosift-mcps` | `repo-005194` `yarikoptic/neurosift-mcps`（REPRESENTATIVE；parent=magland/neurosift-mcps） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`RECENT_ACTIVE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `863–912`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-022-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
