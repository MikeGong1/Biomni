# 远程调研 Batch 028

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1163–1212**；**50** 个 family；**51** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 51 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 1 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 5 |
| 分类 `DATASET_OR_BENCHMARK` | 6 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 17 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 16 |
| 分类 `LOW_INFORMATION_RECHECK` | 1 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 4 |
| 标记 `ARCHIVED_OR_DISABLED` | 1 |
| 标记 `CHILD_FORK_SURFACE` | 2 |
| 标记 `FORK_LINEAGE_REQUIRED` | 47 |
| 标记 `LICENSE_UNCLEAR` | 18 |
| 标记 `MULTI_MEMBER_FAMILY` | 1 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1163 | `scalableminds/webknossos`<br>source=`scalableminds/webknossos` | `repo-005755` `yarikoptic/webknossos`（REPRESENTATIVE；parent=scalableminds/webknossos） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1164 | `omegaiota/diffcloth`<br>source=`omegaiota/DiffCloth` | `repo-003251` `Rakshitha-Ireddi/DiffCloth`（REPRESENTATIVE；parent=omegaiota/DiffCloth） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1165 | `newhorizonsinlanguagescience/newhorizonsinlanguagescience.github.io`<br>source=`newhorizonsinlanguagescience/newhorizonsinlanguagescience.github.io` | `repo-005200` `yarikoptic/newhorizonsinlanguagescience.github.io`（REPRESENTATIVE；parent=newhorizonsinlanguagescience/newhorizonsinlanguagescience.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1166 | `bjing2016/alphaflow`<br>source=`bjing2016/alphaflow` | `repo-007144` `KSUN63/alphaflow`（REPRESENTATIVE；parent=bjing2016/alphaflow） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1167 | `con/journals`<br>source=`con/journals` | `repo-005388` `yarikoptic/publishers`（REPRESENTATIVE；parent=con/journals） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1168 | `tum-traffic-dataset/tum-traffic-dataset-dev-kit`<br>source=`tum-traffic-dataset/tum-traffic-dataset-dev-kit` | `repo-001240` `HasanAldhahi/tum-traffic-dataset-dev-kit`（REPRESENTATIVE；parent=tum-traffic-dataset/tum-traffic-dataset-dev-kit） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1169 | `satijalab/seurat-wrappers`<br>source=`satijalab/seurat-wrappers` | `repo-002380` `zskylarli/seurat-wrappers`（REPRESENTATIVE；parent=satijalab/seurat-wrappers） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1170 | `scverse/scanpy-tutorials`<br>source=`scverse/scanpy-tutorials` | `repo-003149` `Mr-Milk/scanpy-tutorials`（REPRESENTATIVE；parent=scverse/scanpy-tutorials） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1171 | `cudmore/sanpy`<br>source=`cudmore/SanPy` | `repo-005535` `yarikoptic/SanPy`（REPRESENTATIVE；parent=cudmore/SanPy） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1172 | `npacore/awesome-neuroimaging`<br>source=`NPACore/awesome-neuroimaging` | `repo-004420` `yarikoptic/awesome-neuroimaging`（REPRESENTATIVE；parent=NPACore/awesome-neuroimaging） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1173 | `griffithlab/civic-v2`<br>source=`griffithlab/civic-v2` | `repo-004553` `yarikoptic/civic-v2`（REPRESENTATIVE；parent=griffithlab/civic-v2） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1174 | `zrqiao/neuralplexer`<br>source=`zrqiao/NeuralPLexer` | `repo-007160` `KSUN63/NeuralPLexer`（REPRESENTATIVE；parent=zrqiao/NeuralPLexer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1175 | `brainlife/abcd-spec`<br>source=`brainlife/abcd-spec` | `repo-004350` `yarikoptic/abcd-spec`（REPRESENTATIVE；parent=brainlife/abcd-spec） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1176 | `p2p-ld/nwb-linkml`<br>source=`p2p-ld/nwb-linkml` | `repo-005255` `yarikoptic/nwb-linkml`（REPRESENTATIVE；parent=p2p-ld/nwb-linkml） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1177 | `sage-bionetworks-challenges/sample-model-templates`<br>source=`Sage-Bionetworks-Challenges/sample-model-templates` | `repo-007118` `jaybee84/sample-model-templates`（REPRESENTATIVE；parent=Sage-Bionetworks-Challenges/sample-model-templates） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1178 | `gigascience/paper-bray2017`<br>source=`gigascience/paper-bray2017` | `repo-002217` `tuln128/paper-bray2017`（REPRESENTATIVE；parent=gigascience/paper-bray2017） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1179 | `allenai/s2orc-doc2json`<br>source=`allenai/s2orc-doc2json` | `repo-001667` `MinxZ/s2orc-doc2json`（REPRESENTATIVE；parent=allenai/s2orc-doc2json） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1180 | `zenodraft/zenodraft`<br>source=`zenodraft/zenodraft` | `repo-005784` `yarikoptic/zenodraft`（REPRESENTATIVE；parent=zenodraft/zenodraft） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1181 | `dpeerlab/envi`<br>source=`dpeerlab/ENVI` | `repo-001282` `HelloWorldLTY/ENVI`（REPRESENTATIVE；parent=dpeerlab/ENVI） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1182 | `npacore/reproin-namer`<br>source=`NPACore/reproin-namer` | `repo-005498` `yarikoptic/reproin-namer`（REPRESENTATIVE；parent=NPACore/reproin-namer） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1183 | `gdcc/easydataverse`<br>source=`gdcc/easyDataverse` | `repo-004776` `yarikoptic/easyDataverse`（REPRESENTATIVE；parent=gdcc/easyDataverse） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1184 | `gdcc/pydataverse`<br>source=`gdcc/pyDataverse` | `repo-005404` `yarikoptic/pyDataverse`（REPRESENTATIVE；parent=gdcc/pyDataverse） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1185 | `satijalab/azimuth`<br>source=`satijalab/azimuth` | `repo-002988` `KalinNonchev/azimuth`（REPRESENTATIVE；parent=satijalab/azimuth） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1186 | `omicsml/dance`<br>source=`OmicsML/dance` | `repo-001266` `HelloWorldLTY/dance`（REPRESENTATIVE；parent=OmicsML/dance） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1187 | `ohdsi/commondatamodel`<br>source=`OHDSI/CommonDataModel` | `repo-004584` `yarikoptic/CommonDataModel`（REPRESENTATIVE；parent=OHDSI/CommonDataModel） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1188 | `mkoretsky1/snp_metrics_db`<br>source=`mkoretsky1/snp_metrics_db` | `repo-003110` `mkoretsky1/snp_metrics_db`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1189 | `mkoretsky1/cloud_genotools`<br>source=`mkoretsky1/cloud_genotools` | `repo-003101` `mkoretsky1/cloud_genotools`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1190 | `neurodatawithoutborders/lindi`<br>source=`NeurodataWithoutBorders/lindi` | `repo-005043` `yarikoptic/lindi`（REPRESENTATIVE；parent=NeurodataWithoutBorders/lindi） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1191 | `nextflow-io/awesome-nextflow`<br>source=`nextflow-io/awesome-nextflow` | `repo-004071` `vladsavelyev/awesome-nextflow`（REPRESENTATIVE；parent=nextflow-io/awesome-nextflow） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1192 | `sccn/labstreaminglayer`<br>source=`sccn/labstreaminglayer` | `repo-005026` `yarikoptic/labstreaminglayer`（REPRESENTATIVE；parent=sccn/labstreaminglayer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1193 | `ncbi/medcpt`<br>source=`ncbi/MedCPT` | `repo-002174` `th86/MedCPT`（REPRESENTATIVE；parent=ncbi/MedCPT） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1194 | `sdtc-cpmed/scdrugprio`<br>source=`SDTC-CPMed/scDrugPrio` | `repo-006886` `tangxuan82/scDrugPrio`（REPRESENTATIVE；parent=SDTC-CPMed/scDrugPrio） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1195 | `walaj/cyftools`<br>source=`walaj/cyftools` | `repo-002781` `inodb/cyftools`（REPRESENTATIVE；parent=walaj/cyftools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1196 | `marieoestreich/pro-gene-gen`<br>source=`MarieOestreich/PRO-GENE-GEN` | `repo-007103` `jaybee84/PRO-GENE-GEN`（REPRESENTATIVE；parent=MarieOestreich/PRO-GENE-GEN） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1197 | `google/deepsomatic`<br>source=`google/deepsomatic` | `repo-007071` `jaybee84/deepsomatic`（REPRESENTATIVE；parent=google/deepsomatic） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1198 | `nf-core/tools`<br>source=`nf-core/tools` | `repo-004168` `vladsavelyev/tools`（REPRESENTATIVE；parent=nf-core/tools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1199 | `neurodatawithoutborders/nwb_hackathons`<br>source=`NeurodataWithoutBorders/nwb_hackathons` | `repo-005259` `yarikoptic/nwb_hackathons`（REPRESENTATIVE；parent=NeurodataWithoutBorders/nwb_hackathons） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1200 | `templateflow/python-client`<br>source=`templateflow/python-client` | `repo-005446` `yarikoptic/python-client`（REPRESENTATIVE；parent=templateflow/python-client） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1201 | `neurobagel/query-tool`<br>source=`neurobagel/query-tool` | `repo-005469` `yarikoptic/query-tool`（REPRESENTATIVE；parent=neurobagel/query-tool） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1202 | `google-deepmind/alphamissense`<br>source=`google-deepmind/alphamissense` | `repo-007048` `jaybee84/alphamissense`（REPRESENTATIVE；parent=google-deepmind/alphamissense） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1203 | `mjvolk3/zendron`<br>source=`Mjvolk3/Zendron` | `repo-007015` `Vik-u/Zendron`（REPRESENTATIVE；parent=Mjvolk3/Zendron） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1204 | `ontozoo/ontobee`<br>source=`OntoZoo/ontobee` | `repo-005270` `yarikoptic/ontobee`（REPRESENTATIVE；parent=OntoZoo/ontobee） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1205 | `nipy/nibabel`<br>source=`nipy/nibabel` | `repo-005204` `yarikoptic/nibabel`（REPRESENTATIVE；parent=nipy/nibabel） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1206 | `datajoint/element-interface`<br>source=`datajoint/element-interface` | `repo-004785` `yarikoptic/element-interface`（REPRESENTATIVE；parent=datajoint/element-interface） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1207 | `cosanlab/py-feat`<br>source=`cosanlab/py-feat` | `repo-005394` `yarikoptic/py-feat`（REPRESENTATIVE；parent=cosanlab/py-feat） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1208 | `tschaffter/squid`<br>source=`tschaffter/squid` | `repo-007370` `tschaffter/squid`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1209 | `datalad-handbook/course`<br>source=`datalad-handbook/course` | `repo-004613` `yarikoptic/course`（REPRESENTATIVE；parent=datalad-handbook/course） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1210 | `manubot/manubot`<br>source=`manubot/manubot` | `repo-002330` `zhanxw/manubot`（REPRESENTATIVE；parent=manubot/manubot） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1211 | `aces/eeg2bids`<br>source=`aces/EEG2BIDS` | `repo-004780` `yarikoptic/EEG2BIDS`（REPRESENTATIVE；parent=aces/EEG2BIDS） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1212 | `snakemake/snakemake`<br>source=`snakemake/snakemake` | `repo-005596` `yarikoptic/snakemake`（REPRESENTATIVE；parent=snakemake/snakemake）<br>`repo-004158` `vladsavelyev/snakemake`（MEMBER；parent=snakemake/snakemake） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`MULTI_MEMBER_FAMILY`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1163–1212`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-028-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
