# 远程调研 Batch 035

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1513–1562**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 2 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 4 |
| 分类 `DATASET_OR_BENCHMARK` | 4 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 10 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 20 |
| 分类 `LOW_INFORMATION_RECHECK` | 3 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 7 |
| 标记 `ARCHIVED_OR_DISABLED` | 2 |
| 标记 `CHILD_FORK_SURFACE` | 5 |
| 标记 `FORK_LINEAGE_REQUIRED` | 37 |
| 标记 `LICENSE_UNCLEAR` | 22 |
| 标记 `RELEASE_SURFACE` | 4 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1513 | `cellprofiler/cellprofiler`<br>source=`CellProfiler/CellProfiler` | `repo-002392` `aevo98765/CellProfiler`（REPRESENTATIVE；parent=CellProfiler/CellProfiler） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1514 | `translatorsri/scriptshare`<br>source=`TranslatorSRI/ScriptShare` | `repo-000952` `andrewsu/ScriptShare`（REPRESENTATIVE；parent=TranslatorSRI/ScriptShare） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1515 | `sage-bionetworks/synapsewebclient`<br>source=`Sage-Bionetworks/SynapseWebClient` | `repo-007376` `tschaffter/SynapseWebClient`（REPRESENTATIVE；parent=Sage-Bionetworks/SynapseWebClient） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1516 | `alexj-lee/proteinmpnn`<br>source=`alexj-lee/proteinmpnn` | `repo-006279` `alexj-lee/proteinmpnn`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | 无额外标记 | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1517 | `maranasgroup/kcat-km`<br>source=`maranasgroup/kcat-km` | `repo-006969` `Vik-u/kcat-km`（REPRESENTATIVE；parent=maranasgroup/kcat-km） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1518 | `flatironinstitute/deepfri`<br>source=`flatironinstitute/DeepFRI` | `repo-006954` `Vik-u/DeepFRI`（REPRESENTATIVE；parent=flatironinstitute/DeepFRI） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1519 | `zjufanlab/scdeepsort`<br>source=`ZJUFanLab/scDeepSort` | `repo-001336` `HelloWorldLTY/scDeepSort`（REPRESENTATIVE；parent=ZJUFanLab/scDeepSort） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1520 | `inodb/sufam`<br>source=`inodb/sufam` | `repo-002865` `inodb/sufam`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1521 | `aprilyuge/scaanet`<br>source=`AprilYuge/scAAnet` | `repo-001335` `HelloWorldLTY/scAAnet`（REPRESENTATIVE；parent=AprilYuge/scAAnet） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1522 | `aristoteleo/dynamo-release`<br>source=`aristoteleo/dynamo-release` | `repo-000872` `amehrjou/dynamo-release`（REPRESENTATIVE；parent=aristoteleo/dynamo-release） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1523 | `repronim/repronim.github.io`<br>source=`ReproNim/repronim.github.io` | `repo-005502` `yarikoptic/repronim.github.io`（REPRESENTATIVE；parent=ReproNim/repronim.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1524 | `zskylarli/scrna-bacteria-integration`<br>source=`zskylarli/scrna-bacteria-integration` | `repo-002378` `zskylarli/scrna-bacteria-integration`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | 无额外标记 | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1525 | `nekitmm/dlpacker`<br>source=`nekitmm/DLPacker` | `repo-007151` `KSUN63/DLPacker`（REPRESENTATIVE；parent=nekitmm/DLPacker） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1526 | `mih/datalad-mihextras`<br>source=`mih/datalad-mihextras` | `repo-004680` `yarikoptic/datalad-mihextras`（REPRESENTATIVE；parent=mih/datalad-mihextras） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1527 | `mit-lcp/gossis`<br>source=`MIT-LCP/gossis` | `repo-006801` `fionaxc/gossis`（REPRESENTATIVE；parent=MIT-LCP/gossis） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1528 | `michiyasunaga/linkbert`<br>source=`michiyasunaga/LinkBERT` | `repo-000843` `michiyasunaga/LinkBERT`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1529 | `zskylarli/bacteriagan`<br>source=`zskylarli/bacteriaGAN` | `repo-002372` `zskylarli/bacteriaGAN`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1530 | `chanzuckerberg/cellxgene`<br>source=`chanzuckerberg/cellxgene` | `repo-000901` `andrewsu/cellxgene`（REPRESENTATIVE；parent=chanzuckerberg/cellxgene） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1531 | `helloworldlty/sctransformer`<br>source=`HelloWorldLTY/scTransformer` | `repo-001347` `HelloWorldLTY/scTransformer`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1532 | `broadinstitute/seqr-loading-pipelines`<br>source=`broadinstitute/seqr-loading-pipelines` | `repo-004112` `vladsavelyev/hail-elasticsearch-pipelines`（REPRESENTATIVE；parent=broadinstitute/seqr-loading-pipelines） | `ARCHIVED_OR_DISABLED` | `FORK_LINEAGE_REQUIRED`、`ARCHIVED_OR_DISABLED` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1533 | `genedisco/genedisco`<br>source=`genedisco/genedisco` | `repo-000873` `amehrjou/genedisco`（REPRESENTATIVE；parent=genedisco/genedisco） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1534 | `alexj-lee/harnik-rna-spatial-journalclub`<br>source=`alexj-lee/harnik-rna-spatial-journalclub` | `repo-006268` `alexj-lee/harnik-rna-spatial-journalclub`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | 无额外标记 | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1535 | `rtxteam/rtx`<br>source=`RTXteam/RTX` | `repo-000948` `andrewsu/RTX`（REPRESENTATIVE；parent=RTXteam/RTX） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1536 | `connorcoley/rdchiral`<br>source=`connorcoley/rdchiral` | `repo-007002` `Vik-u/rdchiral`（REPRESENTATIVE；parent=connorcoley/rdchiral） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1537 | `tschaffter/genenetweaver`<br>source=`tschaffter/genenetweaver` | `repo-007329` `tschaffter/genenetweaver`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1538 | `hms-idac/unmicst`<br>source=`HMS-IDAC/UnMicst` | `repo-003163` `Mr-Milk/UnMicst`（REPRESENTATIVE；parent=HMS-IDAC/UnMicst） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1539 | `xiebb123456/automaticcelltypeidentification`<br>source=`xiebb123456/AutomaticCellTypeIdentification` | `repo-003052` `Liripo/AutomaticCellTypeIdentification`（REPRESENTATIVE；parent=xiebb123456/AutomaticCellTypeIdentification） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1540 | `neurodebian/neurodebian`<br>source=`neurodebian/neurodebian` | `repo-005180` `yarikoptic/neurodebian`（REPRESENTATIVE；parent=neurodebian/neurodebian） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1541 | `ao508/htan-data-ingress-documentation-draft`<br>source=`ao508/HTAN-data-ingress-documentation-draft` | `repo-002808` `inodb/HTAN-Data-Ingress-Docs`（REPRESENTATIVE；parent=ao508/HTAN-data-ingress-documentation-draft） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1542 | `ga4gh/gh-openapi-docs`<br>source=`ga4gh/gh-openapi-docs` | `repo-007330` `tschaffter/gh-openapi-docs`（REPRESENTATIVE；parent=ga4gh/gh-openapi-docs） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1543 | `gist-csbl/deepconv-dti`<br>source=`GIST-CSBL/DeepConv-DTI` | `repo-006953` `Vik-u/DeepConv-DTI`（REPRESENTATIVE；parent=GIST-CSBL/DeepConv-DTI） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1544 | `sage-bionetworks/synapse-react-client`<br>source=`Sage-Bionetworks/Synapse-React-Client` | `repo-007372` `tschaffter/Synapse-React-Client`（REPRESENTATIVE；parent=Sage-Bionetworks/Synapse-React-Client） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1545 | `data2health/resource-discovery-api`<br>source=`data2health/resource-discovery-api` | `repo-007361` `tschaffter/resource-discovery-api`（REPRESENTATIVE；parent=data2health/resource-discovery-api） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1546 | `zhanxw/rvtests`<br>source=`zhanxw/rvtests` | `repo-002351` `zhanxw/rvtests`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1547 | `alexarnimueller/smiles_generator`<br>source=`alexarnimueller/SMILES_generator` | `repo-005984` `dabulseco/SMILES_generator`（REPRESENTATIVE；parent=alexarnimueller/SMILES_generator） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1548 | `nccr-synapsy/neurodatapub`<br>source=`NCCR-SYNAPSY/neurodatapub` | `repo-005179` `yarikoptic/neurodatapub`（REPRESENTATIVE；parent=NCCR-SYNAPSY/neurodatapub） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1549 | `openproblems-bio/neurips2021_multimodal_topmethods`<br>source=`openproblems-bio/neurips2021_multimodal_topmethods` | `repo-001323` `HelloWorldLTY/neurips2021_multimodal_topmethods`（REPRESENTATIVE；parent=openproblems-bio/neurips2021_multimodal_topmethods） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1550 | `rordenlab/mricrogl`<br>source=`rordenlab/MRIcroGL` | `repo-005133` `yarikoptic/MRIcroGL`（REPRESENTATIVE；parent=rordenlab/MRIcroGL） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1551 | `inodb/cbioportal-frontend-archive-1`<br>source=`inodb/cbioportal-frontend-archive-1` | `repo-002764` `inodb/cbioportal-frontend-archive-1`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1552 | `data2health/resource-discovery-portal`<br>source=`data2health/resource-discovery-portal` | `repo-007362` `tschaffter/resource-discovery-portal`（REPRESENTATIVE；parent=data2health/resource-discovery-portal） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1553 | `wwxkenmo/bioinfor_researchers_atlas`<br>source=`WWXkenmo/Bioinfor_researchers_atlas` | `repo-001260` `HelloWorldLTY/Bioinfor_researchers_atlas`（REPRESENTATIVE；parent=WWXkenmo/Bioinfor_researchers_atlas） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1554 | `akulikova64/cnn_protein_landscape`<br>source=`akulikova64/CNN_protein_landscape` | `repo-006836` `tangxuan82/CNN_protein_landscape`（REPRESENTATIVE；parent=akulikova64/CNN_protein_landscape） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1555 | `changwn/chip-seq_jizhang`<br>source=`changwn/ChIP-seq_JiZhang` | `repo-002585` `changwn/ChIP-seq_JiZhang`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1556 | `rstudio/rstudio`<br>source=`rstudio/rstudio` | `repo-007289` `NKalavros/rstudio`（REPRESENTATIVE；parent=rstudio/rstudio） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1557 | `helloworldlty/awesome-bioinformatics-papers`<br>source=`HelloWorldLTY/Awesome-Bioinformatics-Papers` | `repo-001253` `HelloWorldLTY/Awesome-Bioinformatics-Papers`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | `LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1558 | `helloworldlty/biae`<br>source=`HelloWorldLTY/BiAE` | `repo-001259` `HelloWorldLTY/BiAE`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1559 | `maranasgroup/steadystate-mfa`<br>source=`maranasgroup/SteadyState-MFA` | `repo-007010` `Vik-u/SteadyState-MFA`（REPRESENTATIVE；parent=maranasgroup/SteadyState-MFA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1560 | `piiq/slicercompose`<br>source=`piiq/SlicerCompose` | `repo-002707` `erhuve/SlicerCompose`（REPRESENTATIVE；parent=piiq/SlicerCompose） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1561 | `theislab/scvelo_notebooks`<br>source=`theislab/scvelo_notebooks` | `repo-007203` `leezx/scvelo_notebooks`（REPRESENTATIVE；parent=theislab/scvelo_notebooks） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1562 | `ncihtan/hdash`<br>source=`ncihtan/hdash` | `repo-002802` `inodb/hdash`（REPRESENTATIVE；parent=ncihtan/hdash） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1513–1562`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-035-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
