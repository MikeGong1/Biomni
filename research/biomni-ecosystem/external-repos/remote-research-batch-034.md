# 远程调研 Batch 034

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1463–1512**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 2 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 16 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 19 |
| 分类 `LOW_INFORMATION_RECHECK` | 6 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 7 |
| 标记 `CHILD_FORK_SURFACE` | 5 |
| 标记 `FORK_LINEAGE_REQUIRED` | 32 |
| 标记 `LICENSE_UNCLEAR` | 24 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1463 | `bmy21/pacs-model`<br>source=`bmy21/pacs-model` | `repo-006784` `drgmk/pacs-model`（REPRESENTATIVE；parent=bmy21/pacs-model） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1464 | `openwdl/wdl`<br>source=`openwdl/wdl` | `repo-005751` `yarikoptic/wdl`（REPRESENTATIVE；parent=openwdl/wdl） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1465 | `kuanlinhuang/vcf2tsv`<br>source=`kuanlinhuang/vcf2tsv` | `repo-001550` `kuanlinhuang/vcf2tsv`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1466 | `adamjtaylor/htan-artist`<br>source=`adamjtaylor/htan-artist` | `repo-002807` `inodb/htan-artist`（REPRESENTATIVE；parent=adamjtaylor/htan-artist） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1467 | `kaistomics/pcasa`<br>source=`kaistomics/PCASA` | `repo-002619` `changwn/PCASA`（REPRESENTATIVE；parent=kaistomics/PCASA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1468 | `vladsavelyev/wdl-workflows`<br>source=`vladsavelyev/wdl-workflows` | `repo-004179` `vladsavelyev/wdl-workflows`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1469 | `broadinstitute/warp`<br>source=`broadinstitute/warp` | `repo-004178` `vladsavelyev/warp`（REPRESENTATIVE；parent=broadinstitute/warp） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1470 | `tijeco/berteome`<br>source=`tijeco/berteome` | `repo-006832` `tangxuan82/berteome`（REPRESENTATIVE；parent=tijeco/berteome） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1471 | `alexj-lee/minimal-esm-training-loop`<br>source=`alexj-lee/minimal-esm-training-loop` | `repo-006274` `alexj-lee/minimal-esm-training-loop`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1472 | `helloworldlty/cvqvae`<br>source=`HelloWorldLTY/CVQVAE` | `repo-001264` `HelloWorldLTY/CVQVAE`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1473 | `marrlab/car_t_targetidentification`<br>source=`marrlab/CAR_T_TargetIdentification` | `repo-002150` `th86/CAR_T_TargetIdentification`（REPRESENTATIVE；parent=marrlab/CAR_T_TargetIdentification） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1474 | `charvijain16/ppml-for-aneurysm-rupture-`<br>source=`Charvijain16/PPML-for-Aneurysm-Rupture-` | `repo-006755` `Charvijain16/PPML-for-Aneurysm-Rupture-`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1475 | `sage-bionetworks/schematic`<br>source=`Sage-Bionetworks/schematic` | `repo-007367` `tschaffter/schematic`（REPRESENTATIVE；parent=Sage-Bionetworks/schematic） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1476 | `siddharthriyer/car_t_stimulation`<br>source=`siddharthriyer/car_t_stimulation` | `repo-002578` `changwn/car_t_stimulation`（REPRESENTATIVE；parent=siddharthriyer/car_t_stimulation） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1477 | `justinaxie/majar`<br>source=`JustinaXie/MAJAR` | `repo-001314` `HelloWorldLTY/MAJAR`（REPRESENTATIVE；parent=JustinaXie/MAJAR） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1478 | `conda-forge/citeproc-py-feedstock`<br>source=`conda-forge/citeproc-py-feedstock` | `repo-004551` `yarikoptic/citeproc-py-feedstock`（REPRESENTATIVE；parent=conda-forge/citeproc-py-feedstock） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1479 | `mkoretsky1/nsqip_reintubation`<br>source=`mkoretsky1/NSQIP_Reintubation` | `repo-003107` `mkoretsky1/NSQIP_Reintubation`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1480 | `deepmreye/deepmreye`<br>source=`DeepMReye/DeepMReye` | `repo-004707` `yarikoptic/DeepMReye`（REPRESENTATIVE；parent=DeepMReye/DeepMReye） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1481 | `jrschmidt2/periodic-nbo`<br>source=`jrschmidt2/periodic-NBO` | `repo-007423` `Rasic2/periodic-NBO`（REPRESENTATIVE；parent=jrschmidt2/periodic-NBO） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1482 | `helloworldlty/open-problems-for-single-cell-2022-silver-medal-solution`<br>source=`HelloWorldLTY/Open-problems-for-single-cell-2022-Silver-medal-solution` | `repo-001324` `HelloWorldLTY/Open-problems-for-single-cell-2022-Silver-medal-solution`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1483 | `prathmesh-ka-github/mental-health`<br>source=`prathmesh-ka-github/Mental-Health` | `repo-001109` `HasanAldhahi/design_clarus`（REPRESENTATIVE；parent=prathmesh-ka-github/Mental-Health） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1484 | `neuronets/nobrainer-zoo`<br>source=`neuronets/nobrainer-zoo` | `repo-005242` `yarikoptic/nobrainer-zoo`（REPRESENTATIVE；parent=neuronets/nobrainer-zoo） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1485 | `shaunporwal/geneplotlab`<br>source=`shaunporwal/geneplotlab` | `repo-007471` `shaunporwal/geneplotlab`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1486 | `lieberinstitute/recount3`<br>source=`LieberInstitute/recount3` | `repo-000942` `andrewsu/recount3`（REPRESENTATIVE；parent=LieberInstitute/recount3） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1487 | `larsonlab/mri-education-resources`<br>source=`LarsonLab/MRI-education-resources` | `repo-002900` `JinL0/MRI-education-resources`（REPRESENTATIVE；parent=LarsonLab/MRI-education-resources） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1488 | `chahat08/brain-tumor-classification`<br>source=`Chahat08/Brain-Tumor-Classification` | `repo-002466` `Chahat08/Brain-Tumor-Classification`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1489 | `little2b/a-deep-learning-based-model-for-predicting-abnormal-liver-function-in-workers-in-the-automotive-manu`<br>source=`little2b/A-deep-learning-based-model-for-predicting-abnormal-liver-function-in-workers-in-the-automotive-manu` | `repo-006123` `little2b/A-deep-learning-based-model-for-predicting-abnormal-liver-function-in-workers-in-the-automotive-manu`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | `LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1490 | `kexinhuang12345/clinicalbert`<br>source=`kexinhuang12345/clinicalBERT` | `repo-001485` `kexinhuang12345/clinicalBERT`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1491 | `sanat-mishra/k562-cell-line-epigenetic-analysis`<br>source=`Sanat-Mishra/K562-cell-line-epigenetic-analysis` | `repo-007447` `Sanat-Mishra/K562-cell-line-epigenetic-analysis`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1492 | `leezx/craci`<br>source=`leezx/CRACI` | `repo-007186` `leezx/CRACI`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1493 | `michealdutt/sleepxai-an-explainable-deep-learning-approach-for-multi-class-sleep-stage-identification`<br>source=`michealdutt/SleepXAI-An-Explainable-Deep-Learning-approach-for-Multi-class-Sleep-Stage-Identification` | `repo-006541` `gutendzx/SleepXAI-An-Explainable-Deep-Learning-approach-for-Multi-class-Sleep-Stage-Identification`（REPRESENTATIVE；parent=michealdutt/SleepXAI-An-Explainable-Deep-Learning-approach-for-Multi-class-Sleep-Stage-Identification） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1494 | `biomed-ai/protac-rl`<br>source=`biomed-AI/PROTAC-RL` | `repo-007200` `leezx/PROTAC-RL`（REPRESENTATIVE；parent=biomed-AI/PROTAC-RL） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1495 | `bids-apps/pymvpa`<br>source=`bids-apps/PyMVPA` | `repo-005420` `yarikoptic/PyMVPA-bids-app`（REPRESENTATIVE；parent=bids-apps/PyMVPA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1496 | `ddsjoberg/gtsummary`<br>source=`ddsjoberg/gtsummary` | `repo-007474` `shaunporwal/gtsummary`（REPRESENTATIVE；parent=ddsjoberg/gtsummary） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1497 | `psychoinformaticslab/pliers`<br>source=`PsychoinformaticsLab/pliers` | `repo-005348` `yarikoptic/pliers`（REPRESENTATIVE；parent=PsychoinformaticsLab/pliers） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1498 | `abigailr13/human_dt`<br>source=`AbigailR13/Human_DT` | `repo-006862` `tangxuan82/Human_DT`（REPRESENTATIVE；parent=AbigailR13/Human_DT） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1499 | `nipreps/qc-book`<br>source=`nipreps/qc-book` | `repo-005460` `yarikoptic/qc-book`（REPRESENTATIVE；parent=nipreps/qc-book） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1500 | `drgmk/dd`<br>source=`drgmk/dd` | `repo-006771` `drgmk/dd`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1501 | `incf/niqc`<br>source=`INCF/niQC` | `repo-005230` `yarikoptic/niQC`（REPRESENTATIVE；parent=INCF/niQC） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1502 | `broadinstitute/gnomad_methods`<br>source=`broadinstitute/gnomad_methods` | `repo-004104` `vladsavelyev/gnomad_methods`（REPRESENTATIVE；parent=broadinstitute/gnomad_methods） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1503 | `nlpsandbox/notebooks`<br>source=`nlpsandbox/notebooks` | `repo-007089` `jaybee84/miRNA_analysis`（REPRESENTATIVE；parent=nlpsandbox/notebooks） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1504 | `agahkarakuzu/oreoni`<br>source=`agahkarakuzu/oreoni` | `repo-005299` `yarikoptic/oreoni`（REPRESENTATIVE；parent=agahkarakuzu/oreoni） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1505 | `jaybee84/microrna_variants`<br>source=`jaybee84/microrna_variants` | `repo-007088` `jaybee84/microrna_variants`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | 无额外标记 | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1506 | `cailab-tamu/sctenifoldknk`<br>source=`cailab-tamu/scTenifoldKnk` | `repo-002637` `changwn/scTenifoldKnk`（REPRESENTATIVE；parent=cailab-tamu/scTenifoldKnk） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1507 | `yarikoptic/hbn_bids-fmriprep_try`<br>source=`yarikoptic/HBN_BIDS-fmriprep_try` | `repo-004931` `yarikoptic/HBN_BIDS-fmriprep_try`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1508 | `broadinstitute/gnomad_qc`<br>source=`broadinstitute/gnomad_qc` | `repo-004105` `vladsavelyev/gnomad_qc`（REPRESENTATIVE；parent=broadinstitute/gnomad_qc） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1509 | `kexinhuang12345/moltrans`<br>source=`kexinhuang12345/MolTrans` | `repo-001508` `kexinhuang12345/MolTrans`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1510 | `yoshitakamo/localcolabfold`<br>source=`YoshitakaMo/localcolabfold` | `repo-006974` `Vik-u/localcolabfold`（REPRESENTATIVE；parent=YoshitakaMo/localcolabfold） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1511 | `ehoogeboom/e3_diffusion_for_molecules`<br>source=`ehoogeboom/e3_diffusion_for_molecules` | `repo-007153` `KSUN63/e3_diffusion_for_molecules`（REPRESENTATIVE；parent=ehoogeboom/e3_diffusion_for_molecules） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1512 | `sanat-mishra/imig-lab`<br>source=`Sanat-Mishra/Imig-Lab` | `repo-007442` `Sanat-Mishra/Imig-Lab`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |

## 完整性边界

- 本文件连续覆盖 orders `1463–1512`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-034-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
