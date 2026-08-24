# 远程调研 Batch 041

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1813–1862**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `ARCHIVED_OR_DISABLED` | 1 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 1 |
| 分类 `DATASET_OR_BENCHMARK` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 15 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 17 |
| 分类 `LOW_INFORMATION_RECHECK` | 10 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 5 |
| 标记 `ARCHIVED_OR_DISABLED` | 1 |
| 标记 `CHILD_FORK_SURFACE` | 8 |
| 标记 `FORK_LINEAGE_REQUIRED` | 32 |
| 标记 `LICENSE_UNCLEAR` | 30 |
| 标记 `RELEASE_SURFACE` | 3 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1813 | `jaybee84/trap_dashboard`<br>source=`jaybee84/TRAP_Dashboard` | `repo-007140` `jaybee84/TRAP_Dashboard`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1814 | `arq5x/lumpy-sv`<br>source=`arq5x/lumpy-sv` | `repo-004122` `vladsavelyev/lumpy-sv`（REPRESENTATIVE；parent=arq5x/lumpy-sv） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1815 | `yarikoptic/gearificator`<br>source=`yarikoptic/gearificator` | `repo-004854` `yarikoptic/gearificator`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1816 | `nkalavros/gene-expression-and-mutation-associations`<br>source=`NKalavros/Gene-Expression-and-Mutation-Associations` | `repo-007269` `NKalavros/Gene-Expression-and-Mutation-Associations`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1817 | `devangliya/markandrecapture`<br>source=`DevangLiya/MarkAndRecapture` | `repo-007448` `Sanat-Mishra/MarkAndRecapture`（REPRESENTATIVE；parent=DevangLiya/MarkAndRecapture） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1818 | `nuriaqueralt/ngly1-neo4j-guides`<br>source=`NuriaQueralt/ngly1-neo4j-guides` | `repo-000932` `andrewsu/ngly1-neo4j-guides`（REPRESENTATIVE；parent=NuriaQueralt/ngly1-neo4j-guides） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1819 | `christofferflensburg/superfreq`<br>source=`ChristofferFlensburg/superFreq` | `repo-004161` `vladsavelyev/superFreq`（REPRESENTATIVE；parent=ChristofferFlensburg/superFreq） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1820 | `pfern/osodos`<br>source=`Pfern/OSODOS` | `repo-005303` `yarikoptic/OSODOS`（REPRESENTATIVE；parent=Pfern/OSODOS） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1821 | `sanat-mishra/population-growth-models`<br>source=`Sanat-Mishra/Population-Growth-Models` | `repo-007452` `Sanat-Mishra/Population-Growth-Models`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1822 | `shuangj00/bmda`<br>source=`shuangj00/BMDA` | `repo-002340` `zhanxw/MicrobiomeBayesDiff`（REPRESENTATIVE；parent=shuangj00/BMDA） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1823 | `cancerdatasci/ceres`<br>source=`cancerdatasci/ceres` | `repo-007058` `jaybee84/ceres`（REPRESENTATIVE；parent=cancerdatasci/ceres） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1824 | `ychae/synapsedocs`<br>source=`ychae/synapseDocs` | `repo-007374` `tschaffter/synapseDocs`（REPRESENTATIVE；parent=ychae/synapseDocs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1825 | `kidozh/digital_twin_by_gan`<br>source=`kidozh/digital_twin_by_GAN` | `repo-006847` `tangxuan82/digital_twin_by_GAN`（REPRESENTATIVE；parent=kidozh/digital_twin_by_GAN） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1826 | `lch14forever/microbiomeviz`<br>source=`lch14forever/microbiomeViz` | `repo-002342` `zhanxw/microbiomeViz`（REPRESENTATIVE；parent=lch14forever/microbiomeViz） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1827 | `mr-milk/bioinformatics-programming-homework`<br>source=`Mr-Milk/bioinformatics-programming-homework` | `repo-003115` `Mr-Milk/bioinformatics-programming-homework`（REPRESENTATIVE） | `ARCHIVED_OR_DISABLED` | `LICENSE_UNCLEAR`、`ARCHIVED_OR_DISABLED`、`CHILD_FORK_SURFACE` | 全部 bounded 记录已归档或禁用；保留为历史线索，后续仅在本地需要时核验来源与许可证。 | `DEFER_LOW_INFORMATION` |
| 1828 | `jaybee84/gene_exp_viewer`<br>source=`jaybee84/Gene_Exp_Viewer` | `repo-007079` `jaybee84/Gene_Exp_Viewer`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1829 | `markpkcollier/neuralturingmachine`<br>source=`MarkPKCollier/NeuralTuringMachine` | `repo-007279` `NKalavros/NeuralTuringMachine`（REPRESENTATIVE；parent=MarkPKCollier/NeuralTuringMachine） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1830 | `sequana/sequana`<br>source=`sequana/sequana` | `repo-004156` `vladsavelyev/sequana`（REPRESENTATIVE；parent=sequana/sequana） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1831 | `yarikoptic/gearificated-nipype`<br>source=`yarikoptic/gearificated-nipype` | `repo-004853` `yarikoptic/gearificated-nipype`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`RELEASE_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1832 | `genome/joinx`<br>source=`genome/joinx` | `repo-004117` `vladsavelyev/joinx`（REPRESENTATIVE；parent=genome/joinx） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1833 | `drgmk/hd98800_alma_c5`<br>source=`drgmk/hd98800_alma_c5` | `repo-006781` `drgmk/hd98800_alma_c5`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1834 | `datalad/datalad-revolution`<br>source=`datalad/datalad-revolution` | `repo-004683` `yarikoptic/datalad-revolution`（REPRESENTATIVE；parent=datalad/datalad-revolution） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1835 | `jacksonloper/markov-link-method`<br>source=`jacksonloper/markov-link-method` | `repo-007087` `jaybee84/markov-link-method`（REPRESENTATIVE；parent=jacksonloper/markov-link-method） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1836 | `flywheel-io/exchange`<br>source=`flywheel-io/exchange` | `repo-004803` `yarikoptic/exchange`（REPRESENTATIVE；parent=flywheel-io/exchange） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1837 | `mrtrix3/mrtrix3`<br>source=`MRtrix3/mrtrix3` | `repo-005139` `yarikoptic/mrtrix3`（REPRESENTATIVE；parent=MRtrix3/mrtrix3） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1838 | `oncokb/oncokb`<br>source=`oncokb/oncokb` | `repo-002835` `inodb/oncokb`（REPRESENTATIVE；parent=oncokb/oncokb） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1839 | `oncokb/oncokb-public`<br>source=`oncokb/oncokb-public` | `repo-002836` `inodb/oncokb-public`（REPRESENTATIVE；parent=oncokb/oncokb-public） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1840 | `machenslab/dpca`<br>source=`machenslab/dPCA` | `repo-007237` `manu-tej/dPCA`（REPRESENTATIVE；parent=machenslab/dPCA） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1841 | `drgmk/feb-accel`<br>source=`drgmk/feb-accel` | `repo-006777` `drgmk/feb-accel`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1842 | `kexinhuang12345/mitotic_spindle`<br>source=`kexinhuang12345/mitotic_spindle` | `repo-001505` `kexinhuang12345/mitotic_spindle`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1843 | `repronim/simple_workflow`<br>source=`ReproNim/simple_workflow` | `repo-005581` `yarikoptic/simple_workflow`（REPRESENTATIVE；parent=ReproNim/simple_workflow） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1844 | `greghope667/comet_project`<br>source=`greghope667/comet_project` | `repo-006766` `drgmk/automated_exocomet_hunt`（REPRESENTATIVE；parent=greghope667/comet_project） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1845 | `brentp/cyvcf2`<br>source=`brentp/cyvcf2` | `repo-004092` `vladsavelyev/cyvcf2`（REPRESENTATIVE；parent=brentp/cyvcf2） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`RELEASE_SURFACE` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1846 | `bids-standard/bids-stats-model-schema`<br>source=`bids-standard/bids-stats-model-schema` | `repo-004481` `yarikoptic/BidsModelSchema`（REPRESENTATIVE；parent=bids-standard/bids-stats-model-schema） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1847 | `sanat-mishra/iiser-mohali`<br>source=`Sanat-Mishra/IISER-Mohali` | `repo-007441` `Sanat-Mishra/IISER-Mohali`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1848 | `templateflow/tpl-mni152nlin2009casym`<br>source=`templateflow/tpl-MNI152NLin2009cAsym` | `repo-005702` `yarikoptic/tpl-MNI152NLin2009cAsym`（REPRESENTATIVE；parent=templateflow/tpl-MNI152NLin2009cAsym） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1849 | `zhanxw/rvtests-docker`<br>source=`zhanxw/rvtests-docker` | `repo-002352` `zhanxw/rvtests-docker`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1850 | `th86/gislkit`<br>source=`th86/gislkit` | `repo-002166` `th86/gislkit`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1851 | `ahboujelben/numscal-basic`<br>source=`ahboujelben/numSCAL-basic` | `repo-001569` `lxasqjc/numSCAL_basic`（REPRESENTATIVE；parent=ahboujelben/numSCAL-basic） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1852 | `drgmk/cb_2018`<br>source=`drgmk/cb_2018` | `repo-006769` `drgmk/cb_2018`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1853 | `openneuroorg/datalad-service`<br>source=`OpenNeuroOrg/datalad-service` | `repo-004684` `yarikoptic/datalad-service`（REPRESENTATIVE；parent=OpenNeuroOrg/datalad-service） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1854 | `whole-tale/whole-tale`<br>source=`whole-tale/whole-tale` | `repo-005760` `yarikoptic/whole-tale`（REPRESENTATIVE；parent=whole-tale/whole-tale） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1855 | `mtazzari/uvplot`<br>source=`mtazzari/uvplot` | `repo-006793` `drgmk/uvplot`（REPRESENTATIVE；parent=mtazzari/uvplot） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1856 | `shengyongniu/bulk_rna_seq_tophat`<br>source=`shengyongniu/bulk_rna_seq_tophat` | `repo-002106` `shengyongniu/bulk_rna_seq_tophat`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1857 | `shengyongniu/bulk_atac_seq`<br>source=`shengyongniu/bulk_ATAC_seq` | `repo-002104` `shengyongniu/bulk_ATAC_seq`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1858 | `sbb-gh/deeper-image-quality-transfer-training-low-memory-neural-networks-for-3d-images`<br>source=`sbb-gh/Deeper-Image-Quality-Transfer-Training-Low-Memory-Neural-Networks-for-3D-Images` | `repo-001557` `lxasqjc/Deeper-Image-Quality-Transfer-Training-Low-Memory-Neural-Networks-for-3D-Images`（REPRESENTATIVE；parent=sbb-gh/Deeper-Image-Quality-Transfer-Training-Low-Memory-Neural-Networks-for-3D-Images） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1859 | `andrewsu/applied-bioinformatics_homeworks`<br>source=`andrewsu/Applied-Bioinformatics_Homeworks` | `repo-000893` `andrewsu/Applied-Bioinformatics_Homeworks`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1860 | `sulab/applied-bioinformatics`<br>source=`SuLab/Applied-Bioinformatics` | `repo-000892` `andrewsu/Applied-Bioinformatics`（REPRESENTATIVE；parent=SuLab/Applied-Bioinformatics） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1861 | `wenchichou/eqtl`<br>source=`wenchichou/eQTL` | `repo-002109` `shengyongniu/eQTL`（REPRESENTATIVE；parent=wenchichou/eQTL） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1862 | `shengyongniu/seqtu`<br>source=`shengyongniu/SeqTU` | `repo-002126` `shengyongniu/SeqTU`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |

## 完整性边界

- 本文件连续覆盖 orders `1813–1862`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-041-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
