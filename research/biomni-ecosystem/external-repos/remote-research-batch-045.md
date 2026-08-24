# 远程调研 Batch 045

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **2013–2062**；**50** 个 family；**50** 条 bounded repository records。

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
| 分类 `DATASET_OR_BENCHMARK` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 11 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 12 |
| 分类 `LOW_INFORMATION_RECHECK` | 14 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 10 |
| 标记 `CHILD_FORK_SURFACE` | 13 |
| 标记 `FORK_LINEAGE_REQUIRED` | 19 |
| 标记 `LICENSE_UNCLEAR` | 39 |
| 标记 `RELEASE_SURFACE` | 3 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 2013 | `inodb/2014-05-mdopson-viral`<br>source=`inodb/2014-05-mdopson-viral` | `repo-002735` `inodb/2014-05-mdopson-viral`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2014 | `binpro/concoct`<br>source=`BinPro/CONCOCT` | `repo-002778` `inodb/CONCOCT`（REPRESENTATIVE；parent=BinPro/CONCOCT） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2015 | `inodb/2014-09-haspeborg-moose-project`<br>source=`inodb/2014-09-haspeborg-moose-project` | `repo-002739` `inodb/2014-09-haspeborg-moose-project`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2016 | `inodb/2014-11-masmvali-presentation`<br>source=`inodb/2014-11-masmvali-presentation` | `repo-002740` `inodb/2014-11-masmvali-presentation`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | 无额外标记 | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2017 | `yarikoptic/utopia-documents-neuroplugins`<br>source=`yarikoptic/utopia-documents-neuroplugins` | `repo-005721` `yarikoptic/utopia-documents-neuroplugins`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2018 | `inodb/masmvaliweb`<br>source=`inodb/masmvaliweb` | `repo-002821` `inodb/masmvaliweb`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2019 | `inodb/metassemble`<br>source=`inodb/metassemble` | `repo-002825` `inodb/metassemble`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2020 | `chaos/slurm`<br>source=`chaos/slurm` | `repo-002858` `inodb/slurm`（REPRESENTATIVE；parent=chaos/slurm） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2021 | `binpro/concoct-test-data`<br>source=`BinPro/CONCOCT-test-data` | `repo-002779` `inodb/CONCOCT-test-data`（REPRESENTATIVE；parent=BinPro/CONCOCT-test-data） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2022 | `inodb/masmvali-publication`<br>source=`inodb/masmvali-publication` | `repo-002820` `inodb/masmvali-publication`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2023 | `miccheck12/scglims`<br>source=`miccheck12/SCGLIMS` | `repo-002791` `inodb/ETTLIMS`（REPRESENTATIVE；parent=miccheck12/SCGLIMS） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 2024 | `envgen/envgen.github.io`<br>source=`EnvGen/envgen.github.io` | `repo-002789` `inodb/envgen.github.io`（REPRESENTATIVE；parent=EnvGen/envgen.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 2025 | `matplotlib/matplotlib`<br>source=`matplotlib/matplotlib` | `repo-005082` `yarikoptic/matplotlib`（REPRESENTATIVE；parent=matplotlib/matplotlib） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2026 | `neurosynth/neurosynth`<br>source=`neurosynth/neurosynth` | `repo-005197` `yarikoptic/Neurosynth`（REPRESENTATIVE；parent=neurosynth/neurosynth） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2027 | `inodb/masmvali`<br>source=`inodb/masmvali` | `repo-002819` `inodb/masmvali`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2028 | `yarikoptic/nitest-balls1`<br>source=`yarikoptic/nitest-balls1` | `repo-005231` `yarikoptic/nitest-balls1`（REPRESENTATIVE） | `CURATED_CATALOG_OR_DOCS` | `LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 2029 | `inodb/2014-06-favorite-microbe`<br>source=`inodb/2014-06-favorite-microbe` | `repo-002736` `inodb/2014-06-favorite-microbe`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2030 | `tschaffter/jmod`<br>source=`tschaffter/jmod` | `repo-007338` `tschaffter/jmod`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RELEASE_SURFACE`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2031 | `protegeproject/protege`<br>source=`protegeproject/protege` | `repo-005371` `yarikoptic/protege`（REPRESENTATIVE；parent=protegeproject/protege） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2032 | `inodb/2014-06-lims-developers-workshop`<br>source=`inodb/2014-06-lims-developers-workshop` | `repo-002737` `inodb/2014-06-lims-developers-workshop`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2033 | `inodb/2014-5-metagenomics-workshop`<br>source=`inodb/2014-5-metagenomics-workshop` | `repo-002742` `inodb/2014-5-metagenomics-workshop`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2034 | `yarikoptic/pystatsmodels`<br>source=`yarikoptic/pystatsmodels` | `repo-005436` `yarikoptic/pystatsmodels`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2035 | `inodb/bioinfo-outreach`<br>source=`inodb/bioinfo-outreach` | `repo-002751` `inodb/bioinfo-outreach`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2036 | `nikhilrp/biodiscover`<br>source=`nikhilRP/bioDiscover` | `repo-000933` `andrewsu/nobProject`（REPRESENTATIVE；parent=nikhilRP/bioDiscover） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2037 | `th86/tcgafastlane`<br>source=`th86/TCGAfastlane` | `repo-002206` `th86/TCGAfastlane`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2038 | `inodb/2014-3-lims-presentation`<br>source=`inodb/2014-3-lims-presentation` | `repo-002741` `inodb/2014-3-lims-presentation`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | 无额外标记 | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2039 | `zhanxw/spd`<br>source=`zhanxw/SPD` | `repo-002361` `zhanxw/SPD`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `RELEASE_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2040 | `scilifelab/facs`<br>source=`SciLifeLab/facs` | `repo-002792` `inodb/facs`（REPRESENTATIVE；parent=SciLifeLab/facs） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2041 | `tschaffter/libsde`<br>source=`tschaffter/libsde` | `repo-007340` `tschaffter/libsde`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2042 | `ialbert/biostar-central`<br>source=`ialbert/biostar-central` | `repo-004488` `yarikoptic/biostar-central`（REPRESENTATIVE；parent=ialbert/biostar-central） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2043 | `zhanxw/seqminercmd`<br>source=`zhanxw/SeqMinerCmd` | `repo-002357` `zhanxw/SeqMinerCmd`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | 无额外标记 | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2044 | `zhanxw/vcf2geno`<br>source=`zhanxw/vcf2geno` | `repo-002367` `zhanxw/vcf2geno`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2045 | `th86/ezma`<br>source=`th86/ezMA` | `repo-002160` `th86/ezMA`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2046 | `inodb/snakemake-parallel-bwa`<br>source=`inodb/snakemake-parallel-bwa` | `repo-002859` `inodb/snakemake-parallel-bwa`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2047 | `inodb/gefes`<br>source=`inodb/gefes` | `repo-002795` `inodb/gefes`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2048 | `inodb/2013-metagenomics-workshop-gbg`<br>source=`inodb/2013-metagenomics-workshop-gbg` | `repo-002734` `inodb/2013-metagenomics-workshop-gbg`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2049 | `yarikoptic/hrf_estimation`<br>source=`yarikoptic/hrf_estimation` | `repo-004957` `yarikoptic/hrf_estimation`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2050 | `poldrack/pybetaseries`<br>source=`poldrack/pybetaseries` | `repo-005396` `yarikoptic/pybetaseries`（REPRESENTATIVE；parent=poldrack/pybetaseries） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2051 | `xfim/ggmcmc`<br>source=`xfim/ggmcmc` | `repo-001408` `jucor/ggmcmc`（REPRESENTATIVE；parent=xfim/ggmcmc） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2052 | `statgen/libstatgen`<br>source=`statgen/libStatGen` | `repo-002326` `zhanxw/libStatGen`（REPRESENTATIVE；parent=statgen/libStatGen） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2053 | `th86/survivalcluster`<br>source=`th86/SurvivalCluster` | `repo-002204` `th86/SurvivalCluster`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2054 | `th86/progeval`<br>source=`th86/progEval` | `repo-002193` `th86/progEval`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 2055 | `binpro/probin`<br>source=`BinPro/ProBin` | `repo-002843` `inodb/ProBin`（REPRESENTATIVE；parent=BinPro/ProBin） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 2056 | `camdavidsonpilon/probabilistic-programming-and-bayesian-methods-for-hackers`<br>source=`CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers` | `repo-005366` `yarikoptic/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers`（REPRESENTATIVE；parent=CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2057 | `inodb/assembly-workshop`<br>source=`inodb/assembly-workshop` | `repo-002747` `inodb/assembly-workshop`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2058 | `qbilius/psychopy_ext`<br>source=`qbilius/psychopy_ext` | `repo-005383` `yarikoptic/psychopy_ext`（REPRESENTATIVE；parent=qbilius/psychopy_ext） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 2059 | `zhanxw/laser`<br>source=`zhanxw/laser` | `repo-002323` `zhanxw/laser`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2060 | `dib-lab/khmer`<br>source=`dib-lab/khmer` | `repo-002816` `inodb/khmer`（REPRESENTATIVE；parent=dib-lab/khmer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 2061 | `jucor/torch-gsl`<br>source=`jucor/torch-gsl` | `repo-001465` `jucor/torch-gsl`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 2062 | `poldrack/regressioncv`<br>source=`poldrack/regressioncv` | `repo-005488` `yarikoptic/regressioncv`（REPRESENTATIVE；parent=poldrack/regressioncv） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `2013–2062`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-045-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
