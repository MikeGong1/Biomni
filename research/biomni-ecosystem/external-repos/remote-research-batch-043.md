# 远程调研 Batch 043

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1913–1962**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `CURATED_CATALOG_OR_DOCS` | 3 |
| 分类 `DATASET_OR_BENCHMARK` | 2 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 19 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 14 |
| 分类 `LOW_INFORMATION_RECHECK` | 6 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 5 |
| 标记 `CHILD_FORK_SURFACE` | 3 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 36 |
| 标记 `LICENSE_UNCLEAR` | 32 |
| 标记 `RELEASE_SURFACE` | 1 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1913 | `chuckyee/cardiac-segmentation`<br>source=`chuckyee/cardiac-segmentation` | `repo-001079` `evolu8/SweepNet`（REPRESENTATIVE；parent=chuckyee/cardiac-segmentation） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1914 | `shengyongniu/bulk_rna_seq_count_base`<br>source=`shengyongniu/bulk_RNA_seq_count_base` | `repo-002105` `shengyongniu/bulk_RNA_seq_count_base`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1915 | `repronim/module-fair-data`<br>source=`ReproNim/module-FAIR-data` | `repo-005121` `yarikoptic/module-FAIR-data`（REPRESENTATIVE；parent=ReproNim/module-FAIR-data） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1916 | `drgmk/alma-radmc-visibility-modelling`<br>source=`drgmk/ALMA-RADMC-visibility-modelling` | `repo-006764` `drgmk/ALMA-RADMC-visibility-modelling`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | `LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1917 | `alleninstitute/rnaseq_cluster`<br>source=`AllenInstitute/RNAseq_cluster` | `repo-007112` `jaybee84/RNAseq_cluster`（REPRESENTATIVE；parent=AllenInstitute/RNAseq_cluster） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1918 | `alleninstitute/agedbrain`<br>source=`AllenInstitute/agedbrain` | `repo-007047` `jaybee84/agedbrain`（REPRESENTATIVE；parent=AllenInstitute/agedbrain） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1919 | `hammerlab/concordance`<br>source=`hammerlab/concordance` | `repo-004087` `vladsavelyev/concordance`（REPRESENTATIVE；parent=hammerlab/concordance） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1920 | `repronim/module-template`<br>source=`ReproNim/module-template` | `repo-005039` `yarikoptic/lesson-template`（REPRESENTATIVE；parent=ReproNim/module-template） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1921 | `repronim/module-dataprocessing`<br>source=`ReproNim/module-dataprocessing` | `repo-005120` `yarikoptic/module-dataprocessing`（REPRESENTATIVE；parent=ReproNim/module-dataprocessing） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1922 | `repronim/module-stats`<br>source=`ReproNim/module-stats` | `repo-005124` `yarikoptic/module-stats`（REPRESENTATIVE；parent=ReproNim/module-stats） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1923 | `medtalkwashu/medtallk`<br>source=`medtalkwashu/medtallk` | `repo-001544` `kuanlinhuang/medtallk`（REPRESENTATIVE；parent=medtalkwashu/medtallk） | `EMPTY_OR_MINIMAL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |
| 1924 | `flywheel-io/gears`<br>source=`flywheel-io/gears` | `repo-004856` `yarikoptic/gears`（REPRESENTATIVE；parent=flywheel-io/gears） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1925 | `djow2019/membrane-protein-mining`<br>source=`djow2019/Membrane-Protein-Mining` | `repo-000928` `andrewsu/Membrane-Protein-Mining`（REPRESENTATIVE；parent=djow2019/Membrane-Protein-Mining） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1926 | `vandermeerlab/papers`<br>source=`vandermeerlab/papers` | `repo-005314` `yarikoptic/papers`（REPRESENTATIVE；parent=vandermeerlab/papers） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1927 | `adamds/biomine`<br>source=`AdamDS/BioMine` | `repo-001528` `kuanlinhuang/BioMine`（REPRESENTATIVE；parent=AdamDS/BioMine） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1928 | `brentp/goleft`<br>source=`brentp/goleft` | `repo-004106` `vladsavelyev/goleft`（REPRESENTATIVE；parent=brentp/goleft） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1929 | `yarikoptic/ds000114--demo-bet`<br>source=`yarikoptic/ds000114--demo-bet` | `repo-004760` `yarikoptic/ds000114--demo-bet`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1930 | `repronim/module-reproducible-basics`<br>source=`ReproNim/module-reproducible-basics` | `repo-005123` `yarikoptic/module-reproducible-basics`（REPRESENTATIVE；parent=ReproNim/module-reproducible-basics） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1931 | `obofoundry/obofoundry.github.io`<br>source=`OBOFoundry/OBOFoundry.github.io` | `repo-000934` `andrewsu/OBOFoundry.github.io`（REPRESENTATIVE；parent=OBOFoundry/OBOFoundry.github.io） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1932 | `roryk/ipython-cluster-helper`<br>source=`roryk/ipython-cluster-helper` | `repo-004116` `vladsavelyev/ipython-cluster-helper`（REPRESENTATIVE；parent=roryk/ipython-cluster-helper） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1933 | `cgratton/dartmouthmind_tutorial`<br>source=`cgratton/DartmouthMIND_tutorial` | `repo-004649` `yarikoptic/DartmouthMIND_tutorial`（REPRESENTATIVE；parent=cgratton/DartmouthMIND_tutorial） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1934 | `drgmk/classifier`<br>source=`drgmk/classifier` | `repo-006770` `drgmk/classifier`（REPRESENTATIVE） | `SCIENTIFIC_METHOD_OR_MODEL` | 无额外标记 | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1935 | `nih-fmrif/nimh_repro_2017_08`<br>source=`nih-fmrif/NIMH_repro_2017_08` | `repo-005221` `yarikoptic/nimh_repro_wrkshpAug2017`（REPRESENTATIVE；parent=nih-fmrif/NIMH_repro_2017_08） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1936 | `drgmk/imorbel`<br>source=`drgmk/imorbel` | `repo-006782` `drgmk/imorbel`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1937 | `cdluc3/dmptool_v2`<br>source=`CDLUC3/dmptool_v2` | `repo-004734` `yarikoptic/dmptool`（REPRESENTATIVE；parent=CDLUC3/dmptool_v2） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1938 | `scikit-image/skimage-tutorials`<br>source=`scikit-image/skimage-tutorials` | `repo-007125` `jaybee84/skimage-tutorials`（REPRESENTATIVE；parent=scikit-image/skimage-tutorials） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1939 | `drgmk/hd116434_51eri_excess`<br>source=`drgmk/hd116434_51eri_excess` | `repo-006780` `drgmk/hd116434_51eri_excess`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1940 | `mrokhfrooz/openpnm-examples`<br>source=`mrokhfrooz/OpenPNM-Examples` | `repo-001572` `lxasqjc/OpenPNM-Examples`（REPRESENTATIVE；parent=mrokhfrooz/OpenPNM-Examples） | `CURATED_CATALOG_OR_DOCS` | `FORK_LINEAGE_REQUIRED` | 主要表现为目录、论文清单或文档资源；可用于发现外部线索，但不视为可直接集成实现。 | `CATALOG_LEAD_ONLY` |
| 1941 | `neurodata/m2g`<br>source=`neurodata/m2g` | `repo-005157` `yarikoptic/ndmg`（REPRESENTATIVE；parent=neurodata/m2g） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1942 | `astrazeneca-ngs/exac_browser`<br>source=`AstraZeneca-NGS/exac_browser` | `repo-004098` `vladsavelyev/exac_browser`（REPRESENTATIVE；parent=AstraZeneca-NGS/exac_browser） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1943 | `scilifelab/genologics`<br>source=`SciLifeLab/genologics` | `repo-004101` `vladsavelyev/genologics`（REPRESENTATIVE；parent=SciLifeLab/genologics） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1944 | `goodb/beacons`<br>source=`goodb/beacons` | `repo-002713` `goodb/beacons`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1945 | `jiwoongbio/fmap`<br>source=`jiwoongbio/FMAP` | `repo-002314` `zhanxw/FMAP`（REPRESENTATIVE；parent=jiwoongbio/FMAP） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1946 | `igvteam/igv`<br>source=`igvteam/igv` | `repo-002112` `shengyongniu/igv`（REPRESENTATIVE；parent=igvteam/igv） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1947 | `daisyburr/bidsonsetswhichfear`<br>source=`daisyburr/BIDSonsetsWhichFear` | `repo-004482` `yarikoptic/BIDSonsetsWhichFear`（REPRESENTATIVE；parent=daisyburr/BIDSonsetsWhichFear） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1948 | `ding-lab/hotspot3d`<br>source=`ding-lab/hotspot3d` | `repo-001541` `kuanlinhuang/hotspot3d`（REPRESENTATIVE；parent=ding-lab/hotspot3d） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`RELEASE_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1949 | `najoshi/sickle`<br>source=`najoshi/sickle` | `repo-007294` `NKalavros/sickle`（REPRESENTATIVE；parent=najoshi/sickle） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1950 | `yoelk/instrumentino`<br>source=`yoelk/instrumentino` | `repo-006595` `PMK89/instrumentino`（REPRESENTATIVE；parent=yoelk/instrumentino） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1951 | `jonathansick/ads_bibdesk`<br>source=`jonathansick/ads_bibdesk` | `repo-006762` `drgmk/ads_bibdesk`（REPRESENTATIVE；parent=jonathansick/ads_bibdesk） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1952 | `diseaseontology/pathogentransmissionontology`<br>source=`DiseaseOntology/PathogenTransmissionOntology` | `repo-000940` `andrewsu/PathogenTransmissionOntology`（REPRESENTATIVE；parent=DiseaseOntology/PathogenTransmissionOntology） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1953 | `th86/arduinogooglesheetairqualitymonitor`<br>source=`th86/ArduinoGoogleSheetAirQualityMonitor` | `repo-002141` `th86/ArduinoGoogleSheetAirQualityMonitor`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1954 | `zhanxw/ancestry`<br>source=`zhanxw/ancestry` | `repo-002286` `zhanxw/ancestry`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1955 | `datalad/ds000114`<br>source=`datalad/ds000114` | `repo-004759` `yarikoptic/ds000114`（REPRESENTATIVE；parent=datalad/ds000114） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1956 | `drgmk/rzpsc`<br>source=`drgmk/rzpsc` | `repo-006787` `drgmk/rzpsc`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1957 | `inodb/biorhino-tools`<br>source=`inodb/biorhino-tools` | `repo-002752` `inodb/biorhino-tools`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1958 | `shengyongniu/argmap`<br>source=`shengyongniu/ARGMap` | `repo-002102` `shengyongniu/ARGMap`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1959 | `tschaffter/dm-docker`<br>source=`tschaffter/dm-docker` | `repo-007320` `tschaffter/dm-docker`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR`、`CHILD_FORK_SURFACE` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1960 | `mvdoc/global2017`<br>source=`mvdoc/global2017` | `repo-004889` `yarikoptic/global2017`（REPRESENTATIVE；parent=mvdoc/global2017） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1961 | `inodb/react-tooltip-test`<br>source=`inodb/react-tooltip-test` | `repo-002850` `inodb/react-tooltip-test`（REPRESENTATIVE） | `IMPLEMENTATION_OR_PIPELINE` | `LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1962 | `glumpy/glumpy`<br>source=`glumpy/glumpy` | `repo-004893` `yarikoptic/glumpy`（REPRESENTATIVE；parent=glumpy/glumpy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |

## 完整性边界

- 本文件连续覆盖 orders `1913–1962`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-043-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
