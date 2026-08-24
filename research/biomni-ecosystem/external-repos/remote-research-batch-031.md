# 远程调研 Batch 031

状态：**REMOTE_METADATA_STATIC_TRIAGE_COMPLETE_NOT_SOURCE_LEVEL_DEEP_AUDIT**

范围：queue orders **1313–1362**；**50** 个 family；**50** 条 bounded repository records。

数据源：`database/repositories.jsonl`，Git blob `85c8c99c5e744f5599849b641609c89686f7aebb`。

方法：仅使用 canonical GitHub 元数据进行确定性 family 聚合、研究类型分层和后续审查优先级标注。未执行被调研仓库的第三方代码、notebook、模型、installer、workflow 或测试；未修改 canonical repository 状态、Evidence、Change、Lineage、Feature 或 Implementation 数据。

该批次的“完成”仅表示**远程元数据静态调研完成**，不等同于源码级 deep audit，也不构成集成、医学、科学有效性或许可证结论。

## 汇总

| 指标 | 数量 |
|---|---:|
| Family | 50 |
| Bounded repository records | 50 |
| Identity note families | 0 |
| 分类 `DATASET_OR_BENCHMARK` | 3 |
| 分类 `EMPTY_OR_MINIMAL` | 1 |
| 分类 `FORK_OR_MIRROR_LINEAGE_LEAD` | 17 |
| 分类 `IMPLEMENTATION_OR_PIPELINE` | 20 |
| 分类 `LOW_INFORMATION_RECHECK` | 3 |
| 分类 `SCIENTIFIC_METHOD_OR_MODEL` | 6 |
| 标记 `EMPTY_OR_MINIMAL` | 1 |
| 标记 `FORK_LINEAGE_REQUIRED` | 46 |
| 标记 `LICENSE_UNCLEAR` | 22 |

## Family 调研表

| Order | Family | Bounded records | 元数据分类 | 风险与边界 | 调研结论 | 后续动作 |
|---:|---|---|---|---|---|---|
| 1313 | `appukuttan-shailesh/ebrains-live-papers`<br>source=`appukuttan-shailesh/ebrains-live-papers` | `repo-004777` `yarikoptic/ebrains-live-papers`（REPRESENTATIVE；parent=appukuttan-shailesh/ebrains-live-papers） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1314 | `neuronets/nobrainer`<br>source=`neuronets/nobrainer` | `repo-005241` `yarikoptic/nobrainer`（REPRESENTATIVE；parent=neuronets/nobrainer） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1315 | `fanchao98/acap`<br>source=`fanchao98/acap` | `repo-001583` `marcosbolanos/acap`（REPRESENTATIVE；parent=fanchao98/acap） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1316 | `project-monai/tutorials`<br>source=`Project-MONAI/tutorials` | `repo-002693` `erhuve/monai_tutorials`（REPRESENTATIVE；parent=Project-MONAI/tutorials） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1317 | `rasic2/gvaspremote`<br>source=`Rasic2/GVaspRemote` | `repo-007418` `Rasic2/GVaspRemote`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1318 | `netneurolab/neuromaps`<br>source=`netneurolab/neuromaps` | `repo-005190` `yarikoptic/neuromaps`（REPRESENTATIVE；parent=netneurolab/neuromaps） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1319 | `emadeldeen24/adast`<br>source=`emadeldeen24/ADAST` | `repo-006465` `gutendzx/ADAST`（REPRESENTATIVE；parent=emadeldeen24/ADAST） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1320 | `brainglobe/brainglobe-atlasapi`<br>source=`brainglobe/brainglobe-atlasapi` | `repo-004451` `yarikoptic/bg-atlasapi`（REPRESENTATIVE；parent=brainglobe/brainglobe-atlasapi） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1321 | `graylab/igfold`<br>source=`Graylab/IgFold` | `repo-006864` `tangxuan82/IgFold`（REPRESENTATIVE；parent=Graylab/IgFold） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1322 | `dattalab/moseq2-viz`<br>source=`dattalab/moseq2-viz` | `repo-005127` `yarikoptic/moseq2-viz`（REPRESENTATIVE；parent=dattalab/moseq2-viz） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1323 | `opensourcebrain/dandiarchiveshowcase`<br>source=`OpenSourceBrain/DANDIArchiveShowcase` | `repo-004642` `yarikoptic/DANDIArchiveShowcase`（REPRESENTATIVE；parent=OpenSourceBrain/DANDIArchiveShowcase） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1324 | `scverse/anndata`<br>source=`scverse/anndata` | `repo-004386` `yarikoptic/anndata`（REPRESENTATIVE；parent=scverse/anndata） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1325 | `minkaixu/geoldm`<br>source=`MinkaiXu/GeoLDM` | `repo-007154` `KSUN63/GeoLDM`（REPRESENTATIVE；parent=MinkaiXu/GeoLDM） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1326 | `aws-samples/mirth-connect-on-aws`<br>source=`aws-samples/mirth-connect-on-aws` | `repo-006440` `chaudhariatul/mirth-connect-on-aws`（REPRESENTATIVE；parent=aws-samples/mirth-connect-on-aws） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1327 | `cunningham-lab/neurocaas`<br>source=`cunningham-lab/neurocaas` | `repo-005173` `yarikoptic/neurocaas`（REPRESENTATIVE；parent=cunningham-lab/neurocaas） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1328 | `oist/optinist`<br>source=`oist/optinist` | `repo-005297` `yarikoptic/optinist`（REPRESENTATIVE；parent=oist/optinist） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1329 | `serena2z/medical-datasets`<br>source=`serena2z/medical-datasets` | `repo-001818` `serena2z/medical-datasets`（REPRESENTATIVE） | `DATASET_OR_BENCHMARK` | `LICENSE_UNCLEAR` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1330 | `ccc-members/hcp_compliant_processor`<br>source=`CCC-members/HCP_compliant_processor` | `repo-004934` `yarikoptic/HCP_compliant_processor`（REPRESENTATIVE；parent=CCC-members/HCP_compliant_processor） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1331 | `ccc-members/ciftistorm-esi`<br>source=`CCC-members/CiftiStorm-ESI` | `repo-004548` `yarikoptic/CiftiStorm`（REPRESENTATIVE；parent=CCC-members/CiftiStorm-ESI） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1332 | `bids-standard/awesome-bids`<br>source=`bids-standard/awesome-bids` | `repo-004418` `yarikoptic/awesome-bids`（REPRESENTATIVE；parent=bids-standard/awesome-bids） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1333 | `donders-institute/data-streamer`<br>source=`Donders-Institute/data-streamer` | `repo-004656` `yarikoptic/data-streamer`（REPRESENTATIVE；parent=Donders-Institute/data-streamer） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1334 | `donders-institute/dicom-dataflow`<br>source=`Donders-Institute/dicom-dataflow` | `repo-004719` `yarikoptic/dicom-dataflow`（REPRESENTATIVE；parent=Donders-Institute/dicom-dataflow） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1335 | `citation-file-format/citation-file-format`<br>source=`citation-file-format/citation-file-format` | `repo-004549` `yarikoptic/citation-file-format`（REPRESENTATIVE；parent=citation-file-format/citation-file-format） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1336 | `humanbrainproject/openminds`<br>source=`HumanBrainProject/openMINDS` | `repo-005286` `yarikoptic/openMINDS-1`（REPRESENTATIVE；parent=HumanBrainProject/openMINDS） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1337 | `scipy/scipy`<br>source=`scipy/scipy` | `repo-005551` `yarikoptic/scipy`（REPRESENTATIVE；parent=scipy/scipy） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1338 | `andrewsu/bte_metakg_viz`<br>source=`andrewsu/BTE_metakg_viz` | `repo-000898` `andrewsu/BTE_metakg_viz`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1339 | `multiqc/test-data`<br>source=`MultiQC/test-data` | `repo-004134` `vladsavelyev/MultiQC_TestData`（REPRESENTATIVE；parent=MultiQC/test-data） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1340 | `peyrachelab/pynacollada`<br>source=`PeyracheLab/pynacollada` | `repo-005422` `yarikoptic/pynacollada`（REPRESENTATIVE；parent=PeyracheLab/pynacollada） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1341 | `joker-jerome/utmost`<br>source=`Joker-Jerome/UTMOST` | `repo-001368` `HelloWorldLTY/UTMOST`（REPRESENTATIVE；parent=Joker-Jerome/UTMOST） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1342 | `mouseland/suite2p`<br>source=`MouseLand/suite2p` | `repo-005640` `yarikoptic/suite2p`（REPRESENTATIVE；parent=MouseLand/suite2p） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1343 | `leezx/crc-hub`<br>source=`leezx/CRC-hub` | `repo-007187` `leezx/CRC-hub`（REPRESENTATIVE） | `LOW_INFORMATION_RECHECK` | `LICENSE_UNCLEAR` | 元数据不足以稳定区分实现、研究资产或文档；需要读取 README 与文件树后再分类。 | `VERIFY_METADATA` |
| 1344 | `genome-nexus/genome-nexus-annotation-pipeline`<br>source=`genome-nexus/genome-nexus-annotation-pipeline` | `repo-002797` `inodb/genome-nexus-annotation-pipeline`（REPRESENTATIVE；parent=genome-nexus/genome-nexus-annotation-pipeline） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1345 | `aws-samples/healthlake-imaging-to-dicom-python-module`<br>source=`aws-samples/healthlake-imaging-to-dicom-python-module` | `repo-006432` `chaudhariatul/healthlake-imaging-to-dicom-python-module`（REPRESENTATIVE；parent=aws-samples/healthlake-imaging-to-dicom-python-module） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1346 | `inria-empenn/narps_open_pipelines`<br>source=`Inria-Empenn/narps_open_pipelines` | `repo-005151` `yarikoptic/narps_open_pipelines`（REPRESENTATIVE；parent=Inria-Empenn/narps_open_pipelines） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1347 | `cbica/nichart`<br>source=`CBICA/niCHART` | `repo-005208` `yarikoptic/niCHART`（REPRESENTATIVE；parent=CBICA/niCHART） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1348 | `vision-cair/minigpt-4`<br>source=`Vision-CAIR/MiniGPT-4` | `repo-001821` `serena2z/SkinGPT-4`（REPRESENTATIVE；parent=Vision-CAIR/MiniGPT-4） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1349 | `neurolibre/roboneuro-gem`<br>source=`neurolibre/roboneuro-gem` | `repo-005519` `yarikoptic/roboneuro-gem`（REPRESENTATIVE；parent=neurolibre/roboneuro-gem） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1350 | `neurolibre/full-stack-server`<br>source=`neurolibre/full-stack-server` | `repo-004844` `yarikoptic/full-stack-server`（REPRESENTATIVE；parent=neurolibre/full-stack-server） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1351 | `rxn4chemistry/rxn4chemistry`<br>source=`rxn4chemistry/rxn4chemistry` | `repo-007006` `Vik-u/rxn4chemistry`（REPRESENTATIVE；parent=rxn4chemistry/rxn4chemistry） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1352 | `ndar/nda-tools`<br>source=`NDAR/nda-tools` | `repo-005155` `yarikoptic/nda-tools`（REPRESENTATIVE；parent=NDAR/nda-tools） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1353 | `unisalento-idalab-iotcourse-2022-2023/wot-digital-twin-healtcare-heart-failure-machine-learning`<br>source=`UniSalento-IDALab-IoTCourse-2022-2023/WoT-Digital-Twin-Healtcare-Heart-Failure-Machine-Learning` | `repo-006909` `tangxuan82/WoT-Digital-Twin-Healtcare-Heart-Failure-Machine-Learning`（REPRESENTATIVE；parent=UniSalento-IDALab-IoTCourse-2022-2023/WoT-Digital-Twin-Healtcare-Heart-Failure-Machine-Learning） | `SCIENTIFIC_METHOD_OR_MODEL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示生物医学方法、模型或分析代码；科学有效性、复现性与许可仍需源码级核验。 | `SOURCE_DAG_COMPARISON` |
| 1354 | `researchhub/researchhub-web`<br>source=`ResearchHub/researchhub-web` | `repo-005509` `yarikoptic/researchhub-web`（REPRESENTATIVE；parent=ResearchHub/researchhub-web） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1355 | `psychoinformatics-de/knowledge-base`<br>source=`psychoinformatics-de/knowledge-base` | `repo-005019` `yarikoptic/knowledge-base`（REPRESENTATIVE；parent=psychoinformatics-de/knowledge-base） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1356 | `allenneuraldynamics/aind-data-schema`<br>source=`AllenNeuralDynamics/aind-data-schema` | `repo-004367` `yarikoptic/aind-data-schema`（REPRESENTATIVE；parent=AllenNeuralDynamics/aind-data-schema） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1357 | `mlco2/codecarbon`<br>source=`mlco2/codecarbon` | `repo-004576` `yarikoptic/codecarbon`（REPRESENTATIVE；parent=mlco2/codecarbon） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1358 | `pennlinc/cubids`<br>source=`PennLINC/CuBIDS` | `repo-004626` `yarikoptic/CuBIDS`（REPRESENTATIVE；parent=PennLINC/CuBIDS） | `DATASET_OR_BENCHMARK` | `FORK_LINEAGE_REQUIRED` | 元数据指向数据集、评测或基准资产；需要本地核验数据来源、访问条件、任务定义与许可证。 | `PRIORITY_LOCAL_CODEX_STATIC_REVIEW` |
| 1359 | `unfmontreal/dcm2bids`<br>source=`UNFmontreal/Dcm2Bids` | `repo-004697` `yarikoptic/Dcm2Bids`（REPRESENTATIVE；parent=UNFmontreal/Dcm2Bids） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1360 | `ismrmrd/ismrmrd`<br>source=`ismrmrd/ismrmrd` | `repo-004992` `yarikoptic/ismrmrd`（REPRESENTATIVE；parent=ismrmrd/ismrmrd） | `FORK_OR_MIRROR_LINEAGE_LEAD` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | bounded 记录属于 fork 或镜像家族；当前只能确认 lineage 线索，独有变更需本地 DAG 比较。 | `SOURCE_DAG_COMPARISON` |
| 1361 | `pulseq/pulseq`<br>source=`pulseq/pulseq` | `repo-005393` `yarikoptic/pulseq`（REPRESENTATIVE；parent=pulseq/pulseq） | `IMPLEMENTATION_OR_PIPELINE` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR` | 元数据显示存在工具、代理、MCP、流程或软件实现面；应优先进行源码级静态审查。 | `SOURCE_DAG_COMPARISON` |
| 1362 | `datalad/shrinky`<br>source=`datalad/shrinky` | `repo-005574` `yarikoptic/shrinky`（REPRESENTATIVE；parent=datalad/shrinky） | `EMPTY_OR_MINIMAL` | `FORK_LINEAGE_REQUIRED`、`LICENSE_UNCLEAR`、`EMPTY_OR_MINIMAL` | 记录为空或缺少可固定的默认头；当前没有足够静态证据支持功能判断。 | `DEFER_LOW_INFORMATION` |

## 完整性边界

- 本文件连续覆盖 orders `1313–1362`，共 `50` 个 family。
- 机器可读记录位于 `remote-research-batch-031-manifest.jsonl`，每个 family 一行。
- 本批没有把任何 family 标记为 canonical `DEEP_AUDITED`。
- Fork 独有变更、历史 ancestry、patch-id、PR lineage、源码安全、数据隐私、科学复现、模型权利和许可证兼容性仍需本地 Codex 按 `next_action` 继续核验。
