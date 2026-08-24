# 远程调研 Batch 036

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1563–1612**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 5 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 1 |
| 分类 `DATASET_OR_BENCHMARK` | 4 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 13 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 17 |
| 分类 `LOW_INFORMATION_RECHECK` | 4 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 5 |
| 标记 `ARCHIVED_OR_DISABLED` | 5 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 36 |
| 标记 `LICENSE_UNCLEAR` | 20 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RELEASE_SURFACE` | 2 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1563 | `kexinhuang12345/ml-genomics-resources`<br>source=`kexinhuang12345/ml-genomics-resources` | `repo-001506` `kexinhuang12345/ml-genomics-resources`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1564 | `aevo98765/in-silico-proteome`<br>source=`aevo98765/in-silico-proteome` | `repo-002406` `aevo98765/in-silico-proteome`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1565 | `cnr-ibba/shiny-server`<br>source=`cnr-ibba/shiny-server` | `repo-006359` `Ali-Maq/shiny-server`（REPRESENTATIVE；parent=cnr-ibba/shiny-server） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1566 | `yulab-smu/microbiomeprofiler`<br>source=`YuLab-SMU/MicrobiomeProfiler` | `repo-002341` `zhanxw/MicrobiomeProfiler`（REPRESENTATIVE；parent=YuLab-SMU/MicrobiomeProfiler） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1567 | `pablocabaleiro/projecteyeliner`<br>source=`PabloCabaleiro/ProjectEyeliner` | `repo-003208` `PabloCabaleiro/ProjectEyeliner`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1568 | `dreem-organization/dreem-learning-evaluation`<br>source=`Dreem-Organization/dreem-learning-evaluation` | `repo-006491` `gutendzx/dreem-learning-evaluation`（REPRESENTATIVE；parent=Dreem-Organization/dreem-learning-evaluation） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1569 | `devindesilva/pneaumonia_prediction_using_chest_xrays`<br>source=`DevinDeSilva/Pneaumonia_prediction_using_chest_xrays` | `repo-006032` `DevinDeSilva/Pneaumonia_prediction_using_chest_xrays`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1570 | `broadinstitute/gatk-sv`<br>source=`broadinstitute/gatk-sv` | `repo-004100` `vladsavelyev/gatk-sv`（REPRESENTATIVE；parent=broadinstitute/gatk-sv） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1571 | `theislab/scib`<br>source=`theislab/scib` | `repo-001342` `HelloWorldLTY/scib`（REPRESENTATIVE；parent=theislab/scib） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1572 | `broadinstitute/wot`<br>source=`broadinstitute/wot` | `repo-000884` `amehrjou/wot`（REPRESENTATIVE；parent=broadinstitute/wot） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1573 | `yeolab/eclipdemux`<br>source=`YeoLab/eclipdemux` | `repo-007439` `Sanat-Mishra/eclipdemux`（REPRESENTATIVE；parent=YeoLab/eclipdemux） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1574 | `deeprob/enzyme-promiscuity-prediction`<br>source=`deeprob/Enzyme-Promiscuity-Prediction` | `repo-006958` `Vik-u/Enzyme-Promiscuity-Prediction`（REPRESENTATIVE；parent=deeprob/Enzyme-Promiscuity-Prediction） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1575 | `mr-milk/neighborhood_analysis`<br>source=`Mr-Milk/neighborhood_analysis` | `repo-003141` `Mr-Milk/neighborhood_analysis`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `ARCHIVED_OR_DISABLED`、`RELEASE_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1576 | `bostongene/kassandra`<br>source=`BostonGene/Kassandra` | `repo-002606` `changwn/Kassandra`（REPRESENTATIVE；parent=BostonGene/Kassandra） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1577 | `pennlinc/hbn_bids`<br>source=`PennLINC/HBN_BIDS` | `repo-004930` `yarikoptic/HBN_BIDS`（REPRESENTATIVE；parent=PennLINC/HBN_BIDS） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1578 | `sacdallago/bio_embeddings`<br>source=`sacdallago/bio_embeddings` | `repo-006940` `Vik-u/bio_embeddings`（REPRESENTATIVE；parent=sacdallago/bio_embeddings） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1579 | `psyinfra/niiview`<br>source=`psyinfra/niiview` | `repo-005216` `yarikoptic/niiview`（REPRESENTATIVE；parent=psyinfra/niiview） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1580 | `jaybee84/nf-covid-response`<br>source=`jaybee84/NF-COVID-response` | `repo-007093` `jaybee84/NF-COVID-response`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1581 | `clemessien/neuroner-phi-annotator-example`<br>source=`clemEssien/NeuroNer-Phi-Annotator-Example` | `repo-007343` `tschaffter/neuro-ner-phi-annotator`（REPRESENTATIVE；parent=clemEssien/NeuroNer-Phi-Annotator-Example） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1582 | `nf-core/configs`<br>source=`nf-core/configs` | `repo-003119` `Mr-Milk/configs`（REPRESENTATIVE；parent=nf-core/configs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1583 | `sydneybiox/scjoint`<br>source=`SydneyBioX/scJoint` | `repo-001343` `HelloWorldLTY/scJoint`（REPRESENTATIVE；parent=SydneyBioX/scJoint） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1584 | `kipoi/kipoiseq`<br>source=`kipoi/kipoiseq` | `repo-003006` `KalinNonchev/kipoiseq`（REPRESENTATIVE；parent=kipoi/kipoiseq） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1585 | `aamini/chemprop`<br>source=`aamini/chemprop` | `repo-001484` `kexinhuang12345/chemprop`（REPRESENTATIVE；parent=aamini/chemprop） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1586 | `ncihtan/schematic`<br>source=`ncihtan/schematic` | `repo-002854` `inodb/schematic`（REPRESENTATIVE；parent=ncihtan/schematic） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1587 | `di2ag/chp_metadata`<br>source=`di2ag/chp_metadata` | `repo-000902` `andrewsu/chp_metadata`（REPRESENTATIVE；parent=di2ag/chp_metadata） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1588 | `ncatstranslator/minihackathons`<br>source=`NCATSTranslator/minihackathons` | `repo-000931` `andrewsu/minihackathons`（REPRESENTATIVE；parent=NCATSTranslator/minihackathons） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1589 | `jaybee84/synapse_analytical_utils`<br>source=`jaybee84/synapse_analytical_utils` | `repo-007130` `jaybee84/synapse_analytical_utils`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1590 | `alexslemonade/openpbta-analysis`<br>source=`AlexsLemonade/OpenPBTA-analysis` | `repo-007101` `jaybee84/OpenPBTA-analysis`（REPRESENTATIVE；parent=AlexsLemonade/OpenPBTA-analysis） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1591 | `manubot/catalog`<br>source=`manubot/catalog` | `repo-007056` `jaybee84/catalog`（REPRESENTATIVE；parent=manubot/catalog） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1592 | `dandi/dandiarchive-legacy`<br>source=`dandi/dandiarchive-legacy` | `repo-004641` `yarikoptic/dandiarchive`（REPRESENTATIVE；parent=dandi/dandiarchive-legacy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1593 | `admin-ch/covidcertificate-documents`<br>source=`admin-ch/CovidCertificate-Documents` | `repo-007311` `tschaffter/CovidCertificate-Documents`（REPRESENTATIVE；parent=admin-ch/CovidCertificate-Documents） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1594 | `zhuyitan/enhanced_coxen`<br>source=`zhuyitan/Enhanced_COXEN` | `repo-006155` `zhuyitan/Enhanced_COXEN`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1595 | `sanat-mishra/transcistor-2.0`<br>source=`Sanat-Mishra/Transcistor-2.0` | `repo-007454` `Sanat-Mishra/Transcistor-2.0`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1596 | `sage-bionetworks-challenges/challenge-analysis-old`<br>source=`Sage-Bionetworks-Challenges/challenge-analysis-old` | `repo-007309` `tschaffter/challenge-analysis`（REPRESENTATIVE；parent=Sage-Bionetworks-Challenges/challenge-analysis-old）<br>`repo-007059` `jaybee84/challenge-analysis`（MEMBER；parent=Sage-Bionetworks-Challenges/challenge-analysis-old） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1597 | `bids-standard/bids-statsmodels-design-synthesizer`<br>source=`bids-standard/bids-statsmodels-design-synthesizer` | `repo-004470` `yarikoptic/bids-statsmodels-design-synthesizer`（REPRESENTATIVE；parent=bids-standard/bids-statsmodels-design-synthesizer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1598 | `openneurodatasets/ds003647`<br>source=`OpenNeuroDatasets/ds003647` | `repo-004763` `yarikoptic/ds003647`（REPRESENTATIVE；parent=OpenNeuroDatasets/ds003647） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1599 | `mr-milk/circdraw`<br>source=`Mr-Milk/circDraw` | `repo-003117` `Mr-Milk/circDraw`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1600 | `google/ehr-predictions`<br>source=`google/ehr-predictions` | `repo-001402` `jucor/ehr-predictions`（REPRESENTATIVE；parent=google/ehr-predictions） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1601 | `datapplab/pathview`<br>source=`datapplab/pathview` | `repo-002618` `changwn/pathview`（REPRESENTATIVE；parent=datapplab/pathview） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1602 | `mr-milk/circdraw-py`<br>source=`Mr-Milk/circDraw-py` | `repo-003118` `Mr-Milk/circDraw-py`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1603 | `explorerwjy/ml_genomics`<br>source=`explorerwjy/ML_genomics` | `repo-006064` `explorerwjy/ML_genomics`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1604 | `spikeinterface/spikeextractors`<br>source=`SpikeInterface/spikeextractors` | `repo-005614` `yarikoptic/spikeextractors`（REPRESENTATIVE；parent=SpikeInterface/spikeextractors） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1605 | `hail-is/hail`<br>source=`hail-is/hail` | `repo-004110` `vladsavelyev/hail`（REPRESENTATIVE；parent=hail-is/hail） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1606 | `mr-milk/spatialtis-tutorial`<br>source=`Mr-Milk/SpatialTis-Tutorial` | `repo-003155` `Mr-Milk/SpatialTis-Tutorial`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1607 | `juexinwang/scgnn`<br>source=`juexinwang/scGNN` | `repo-002635` `changwn/scGNN`（REPRESENTATIVE；parent=juexinwang/scGNN） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1608 | `mr-milk/kmexpress`<br>source=`Mr-Milk/KMexpress` | `repo-003128` `Mr-Milk/KMexpress`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1609 | `artemsokolov/synextra`<br>source=`ArtemSokolov/synExtra` | `repo-007135` `jaybee84/synExtra`（REPRESENTATIVE；parent=ArtemSokolov/synExtra） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1610 | `genome-nexus/annotation-tools`<br>source=`genome-nexus/annotation-tools` | `repo-002746` `inodb/annotation-tools`（REPRESENTATIVE；parent=genome-nexus/annotation-tools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1611 | `hubentu/somaticcombiner_docker`<br>source=`hubentu/SomaticCombiner_docker` | `repo-007127` `jaybee84/SomaticCombiner_docker`（REPRESENTATIVE；parent=hubentu/SomaticCombiner_docker） | `EMPTY_OR_MINIMAL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 1612 | `zy26/ictd`<br>source=`zy26/ICTD` | `repo-002602` `changwn/ICTD`（REPRESENTATIVE；parent=zy26/ICTD） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`RELEASE_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1563–1612`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-036-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
