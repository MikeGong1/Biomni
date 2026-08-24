# Integration Candidates — Phase 9A static research

状态：**STATIC PRIORITIZATION COMPLETE; CODEX VALIDATION REQUIRED**

本文件只给出研究与验证优先级。它不表示第三方实现已经安全、科学正确或可直接并入生产代码。

P0／P1 非重复候选 Feature：**45**。

| Priority | Feature | Biomni gap | Recommended next action | Families | Skills |
|---|---|---|---|---|---|
| P0 | agent.orchestration.multi_agent | CLEAR_GAP | VALIDATE_AND_ADAPT | 11 | 0 |
| P0 | agent.orchestration.planning_execution | CLEAR_GAP | VALIDATE_AND_ADAPT | 2 | 1 |
| P0 | agent.workflow.human_approval | CLEAR_GAP | VALIDATE_AND_ADAPT | 1 | 0 |
| P0 | analysis.bioimage.segmentation | CLEAR_GAP | VALIDATE_AND_ADAPT | 2 | 3 |
| P0 | analysis.cell_cell_communication | CLEAR_GAP | VALIDATE_AND_ADAPT | 1 | 1 |
| P0 | analysis.drug.admet | CLEAR_GAP | VALIDATE_AND_ADAPT | 2 | 1 |
| P0 | analysis.drug.sar_selectivity | CLEAR_GAP | VALIDATE_AND_ADAPT | 4 | 1 |
| P0 | analysis.pathology.slide | CLEAR_GAP | VALIDATE_AND_ADAPT | 4 | 1 |
| P0 | analysis.single_cell.qc_integration | CLEAR_GAP | VALIDATE_AND_ADAPT | 31 | 9 |
| P0 | analysis.spatial_transcriptomics.workflow | CLEAR_GAP | VALIDATE_AND_ADAPT | 12 | 0 |
| P0 | analysis.statistics.bayesian | CLEAR_GAP | VALIDATE_AND_ADAPT | 9 | 4 |
| P0 | analysis.statistics.classical | CLEAR_GAP | VALIDATE_AND_ADAPT | 15 | 4 |
| P0 | analysis.statistics.survival | RELATED_OVERLAP_NOT_EQUIVALENT | VALIDATE_AND_ADAPT | 5 | 2 |
| P0 | analysis.structure.docking_screening | RELATED_OVERLAP_NOT_EQUIVALENT | VALIDATE_AND_ADAPT | 5 | 6 |
| P0 | data.genomics.hts_processing | CLEAR_GAP | VALIDATE_AND_ADAPT | 9 | 6 |
| P0 | data.local_cache.database | CLEAR_GAP | VALIDATE_AND_ADAPT | 1 | 0 |
| P0 | data.provenance.versioned_research | CLEAR_GAP | VALIDATE_AND_ADAPT | 4 | 0 |
| P0 | data.standard.ann_data_omics | RELATED_OVERLAP_NOT_EQUIVALENT | VALIDATE_AND_ADAPT | 8 | 2 |
| P0 | data.standard.bids | PARTIAL_OVERLAP | VALIDATE_AND_ADAPT | 9 | 0 |
| P0 | database.drug.binding_activity | CLEAR_GAP | VALIDATE_AND_ADAPT | 1 | 4 |
| P0 | database.expression_qtl | CLEAR_GAP | VALIDATE_AND_ADAPT | 1 | 4 |
| P0 | deployment.api.server | CLEAR_GAP | VALIDATE_AND_ADAPT | 10 | 3 |
| P0 | deployment.cloud_hpc.job | CLEAR_GAP | VALIDATE_AND_ADAPT | 10 | 3 |
| P0 | deployment.container.environment | CLEAR_GAP | VALIDATE_AND_ADAPT | 13 | 2 |
| P0 | design.genomics.crispr | CLEAR_GAP | VALIDATE_AND_ADAPT | 2 | 2 |
| P0 | design.protein.sequence | CLEAR_GAP | VALIDATE_AND_ADAPT | 4 | 2 |
| P0 | evaluation.benchmark.reproducibility | CLEAR_GAP | VALIDATE_AND_ADAPT | 20 | 11 |
| P0 | governance.security_privacy | CLEAR_GAP | VALIDATE_AND_ADAPT | 11 | 10 |
| P0 | integration.database.multi_service_client | CLEAR_GAP | VALIDATE_AND_ADAPT | 2 | 8 |
| P0 | knowledge.evidence.claim_verification | CLEAR_GAP | VALIDATE_AND_ADAPT | 3 | 6 |
| P0 | knowledge.literature.search_retrieval | CLEAR_GAP | VALIDATE_AND_ADAPT | 8 | 2 |
| P0 | laboratory.automation.instrument | CLEAR_GAP | REFERENCE_ONLY_UNTIL_REMEDIATED | 0 | 4 |
| P0 | model.protein.structure_prediction | CLEAR_GAP | VALIDATE_AND_ADAPT | 3 | 3 |
| P0 | model.spatial.histology_to_expression | CLEAR_GAP | VALIDATE_AND_ADAPT | 1 | 0 |
| P0 | pipeline.genomics.phylogenetics | CLEAR_GAP | VALIDATE_AND_ADAPT | 0 | 1 |
| P0 | pipeline.genomics.variant_calling_annotation | CLEAR_GAP | VALIDATE_AND_ADAPT | 8 | 4 |
| P0 | simulation.molecular_dynamics | CLEAR_GAP | VALIDATE_AND_ADAPT | 5 | 4 |
| P0 | tooling.mcp.client_server | CLEAR_GAP | VALIDATE_AND_ADAPT | 42 | 0 |
| P0 | tooling.sandbox.code_execution | CLEAR_GAP | VALIDATE_AND_ADAPT | 4 | 5 |
| P0 | tooling.skill.registry_discovery | CLEAR_GAP | VALIDATE_AND_ADAPT | 1 | 21 |
| P0 | visualization.scientific.interactive | CLEAR_GAP | VALIDATE_AND_ADAPT | 8 | 4 |
| P0 | workflow.drug.regulatory_safety | CLEAR_GAP | VALIDATE_AND_ADAPT | 11 | 13 |
| P0 | pipeline.genomics.read_alignment | RELATED_OVERLAP_NOT_EQUIVALENT | VALIDATE_AND_ADAPT | 2 | 1 |
| P0 | database.pathway.network | RELATED_OVERLAP_NOT_EQUIVALENT | VALIDATE_AND_ADAPT | 2 | 3 |
| P1 | research.reference.unclassified | CLEAR_GAP | VALIDATE_AND_ADAPT | 348 | 4 |

详细验证顺序见 `phase-9/codex-phase9-validation-queue.jsonl` 和 `phase-9/CODEX_PHASE9_VALIDATION_QUEUE.md`。
