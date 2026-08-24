# Commercial vs OSS static gap — bounded Phase 9A comparison

状态：**COMPLETE FOR THE 17 VERIFIED BEHAVIORS IN COMMERCIAL DISCOVERY 001**

本比较只覆盖已经由官方来源验证的 17 个公开行为。商业内部实现仍为 `UNKNOWN`，产品站点的全局发现也仍是 bounded/partial。

- Biomni baseline 或 OSS 等价能力存在：0；
- OSS 候选存在，但 Biomni 为 gap／partial：15；
- 未匹配到 OSS cluster：2；
- 静态比较不确定：0。

| # | Commercial behavior | Static result | Related Feature keys |
|---|---|---|---|
| 1 | commercial.integrated_biology_environment | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | workspace.integrated.research, agent.orchestration.planning_execution |
| 2 | commercial.large_tool_catalog | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | tooling.skill.registry_discovery, integration.database.multi_service_client |
| 3 | commercial.free_pro_service_tiers | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | deployment.cloud_hpc.job |
| 4 | commercial.foundation_model_design | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | design.protein.sequence, agent.orchestration.planning_execution |
| 5 | commercial.agent_managed_gpu_training | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | deployment.cloud_hpc.job, evaluation.benchmark.reproducibility |
| 6 | commercial.managed_sandboxes | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | tooling.sandbox.code_execution, deployment.cloud_hpc.job |
| 7 | commercial.esmc_integration | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | design.protein.sequence |
| 8 | commercial.esmfold2_integration | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | model.protein.structure_prediction |
| 9 | commercial.boltz_structure_affinity | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | model.protein.structure_prediction, analysis.structure.docking_screening |
| 10 | commercial.external_agent_mcp | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | tooling.mcp.client_server |
| 11 | commercial.desktop_client | COMMERCIAL_BEHAVIOR_WITHOUT_MATCHED_OSS_CLUSTER | workspace.integrated.research |
| 12 | commercial.mobile_client | COMMERCIAL_BEHAVIOR_WITHOUT_MATCHED_OSS_CLUSTER | workspace.integrated.research |
| 13 | commercial.autonomous_method_development | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | agent.orchestration.planning_execution, evaluation.benchmark.reproducibility |
| 14 | commercial.enterprise_dedicated_infrastructure | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | governance.security_privacy, deployment.cloud_hpc.job |
| 15 | commercial.custom_agents_priority_support | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | agent.orchestration.multi_agent |
| 16 | commercial.proprietary_data_deployment | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | analysis.single_cell.qc_integration, governance.security_privacy |
| 17 | commercial.cross_device_everywhere | OSS_CANDIDATE_PRESENT_BIOMNI_GAP_OR_PARTIAL | workspace.integrated.research, tooling.mcp.client_server |

机器可读版本：`phase-9/commercial-oss-gap-static.jsonl`。
