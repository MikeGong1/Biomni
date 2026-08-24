# Codex Phase 9 validation queue

状态：`READY_FOR_LOCAL_CODEX`

该队列承接已经完成的 Phase 9A 静态调研。不要重跑 Batch 001–046，也不要重新发现 598 个 family。

- Validation clusters：91；
- P0／P1／P2／P3：44／1／28／18。

每个 cluster 必须依次完成 exact source freeze、代码级去重、characterization tests、security/privacy/science review、provenance 和 canonical JSONL 校验。

## 前 80 个验证 cluster

| Order | Priority | Feature | Biomni gap | Sources |
|---|---|---|---|---|
| 1 | P0 | agent.orchestration.multi_agent | CLEAR_GAP | 9 |
| 2 | P0 | agent.orchestration.planning_execution | CLEAR_GAP | 2 |
| 3 | P0 | agent.workflow.human_approval | CLEAR_GAP | 1 |
| 4 | P0 | analysis.bioimage.segmentation | CLEAR_GAP | 4 |
| 5 | P0 | analysis.cell_cell_communication | CLEAR_GAP | 2 |
| 6 | P0 | analysis.drug.admet | CLEAR_GAP | 2 |
| 7 | P0 | analysis.drug.sar_selectivity | CLEAR_GAP | 4 |
| 8 | P0 | analysis.pathology.slide | CLEAR_GAP | 5 |
| 9 | P0 | analysis.single_cell.qc_integration | CLEAR_GAP | 39 |
| 10 | P0 | analysis.spatial_transcriptomics.workflow | CLEAR_GAP | 6 |
| 11 | P0 | analysis.statistics.bayesian | CLEAR_GAP | 12 |
| 12 | P0 | analysis.statistics.classical | CLEAR_GAP | 14 |
| 13 | P0 | analysis.statistics.survival | RELATED_OVERLAP_NOT_EQUIVALENT | 7 |
| 14 | P0 | analysis.structure.docking_screening | RELATED_OVERLAP_NOT_EQUIVALENT | 10 |
| 15 | P0 | data.genomics.hts_processing | CLEAR_GAP | 15 |
| 16 | P0 | data.local_cache.database | CLEAR_GAP | 1 |
| 17 | P0 | data.provenance.versioned_research | CLEAR_GAP | 3 |
| 18 | P0 | data.standard.ann_data_omics | RELATED_OVERLAP_NOT_EQUIVALENT | 7 |
| 19 | P0 | data.standard.bids | PARTIAL_OVERLAP | 9 |
| 20 | P0 | database.drug.binding_activity | CLEAR_GAP | 5 |
| 21 | P0 | database.expression_qtl | CLEAR_GAP | 5 |
| 22 | P0 | deployment.api.server | CLEAR_GAP | 9 |
| 23 | P0 | deployment.cloud_hpc.job | CLEAR_GAP | 8 |
| 24 | P0 | deployment.container.environment | CLEAR_GAP | 10 |
| 25 | P0 | design.genomics.crispr | CLEAR_GAP | 4 |
| 26 | P0 | design.protein.sequence | CLEAR_GAP | 5 |
| 27 | P0 | evaluation.benchmark.reproducibility | CLEAR_GAP | 28 |
| 28 | P0 | governance.security_privacy | CLEAR_GAP | 20 |
| 29 | P0 | integration.database.multi_service_client | CLEAR_GAP | 9 |
| 30 | P0 | knowledge.evidence.claim_verification | CLEAR_GAP | 8 |
| 31 | P0 | knowledge.literature.search_retrieval | CLEAR_GAP | 9 |
| 32 | P0 | laboratory.automation.instrument | CLEAR_GAP | 4 |
| 33 | P0 | model.protein.structure_prediction | CLEAR_GAP | 6 |
| 34 | P0 | model.spatial.histology_to_expression | CLEAR_GAP | 0 |
| 35 | P0 | pipeline.genomics.phylogenetics | CLEAR_GAP | 1 |
| 36 | P0 | pipeline.genomics.variant_calling_annotation | CLEAR_GAP | 10 |
| 37 | P0 | simulation.molecular_dynamics | CLEAR_GAP | 8 |
| 38 | P0 | tooling.mcp.client_server | CLEAR_GAP | 26 |
| 39 | P0 | tooling.sandbox.code_execution | CLEAR_GAP | 6 |
| 40 | P0 | tooling.skill.registry_discovery | CLEAR_GAP | 22 |
| 41 | P0 | visualization.scientific.interactive | CLEAR_GAP | 10 |
| 42 | P0 | workflow.drug.regulatory_safety | CLEAR_GAP | 21 |
| 43 | P0 | pipeline.genomics.read_alignment | RELATED_OVERLAP_NOT_EQUIVALENT | 3 |
| 44 | P0 | database.pathway.network | RELATED_OVERLAP_NOT_EQUIVALENT | 5 |
| 45 | P1 | research.reference.unclassified | CLEAR_GAP | 352 |
| 46 | P2 | data.genomics.hts_file_processing | CLEAR_GAP | 2 |
| 47 | P2 | analysis.microbiology.bacterial_pangenome | CLEAR_GAP | 1 |
| 48 | P2 | analysis.statistics.bayesian_modeling | CLEAR_GAP | 1 |
| 49 | P2 | analysis.statistics.classical_models | CLEAR_GAP | 1 |
| 50 | P2 | analysis.systems_biology.grn_inference | CLEAR_GAP | 1 |
| 51 | P2 | guide.visualization.scientific_reporting | CLEAR_GAP | 1 |
| 52 | P2 | integration.bioimage.imagej_bridge | CLEAR_GAP | 1 |
| 53 | P2 | pipeline.transcriptomics.splice_aware_alignment | CLEAR_GAP | 1 |
| 54 | P2 | visualization.bioimage.interactive_viewer | CLEAR_GAP | 1 |
| 55 | P2 | visualization.interactive.plotly | CLEAR_GAP | 1 |
| 56 | P2 | analysis.bindingdb.sar_selectivity | CLEAR_GAP | 0 |
| 57 | P2 | analysis.depmap.cancer_dependency | CLEAR_GAP | 0 |
| 58 | P2 | analysis.molecular_dynamics.trajectory | CLEAR_GAP | 0 |
| 59 | P2 | analysis.scrna.rna_velocity | CLEAR_GAP | 0 |
| 60 | P2 | data_standard.bids.organization_validation | CLEAR_GAP | 0 |
| 61 | P2 | database.gtex.expression_qtl | CLEAR_GAP | 0 |
| 62 | P2 | pipeline.phylogenetics.alignment_tree | CLEAR_GAP | 0 |
| 63 | P2 | simulation.molecular_dynamics.protocol | CLEAR_GAP | 0 |
| 64 | P2 | analysis.single_cell.annotation | BASELINE_EQUIVALENT_PRESENT | 5 |
| 65 | P2 | database.cancer_genomics | BASELINE_EQUIVALENT_PRESENT | 11 |
| 66 | P2 | toolkit.sequence.biopython | PARTIAL_OVERLAP | 2 |
| 67 | P2 | analysis.bioimage.general_processing | PARTIAL_OVERLAP | 1 |
| 68 | P2 | pipeline.genomics.dna_short_read_alignment | PARTIAL_OVERLAP | 1 |
| 69 | P2 | analysis.cbioportal.clinical_survival_workflow | PARTIAL_OVERLAP | 0 |
| 70 | P2 | analysis.jaspar.motif_scan_variant_impact | PARTIAL_OVERLAP | 0 |
| 71 | P2 | analysis.monarch.semantic_similarity_cross_species | PARTIAL_OVERLAP | 0 |
| 72 | P2 | database.variant.population | BASELINE_EQUIVALENT_PRESENT | 4 |
| 73 | P2 | database.bindingdb.affinity_query | RELATED_OVERLAP_NOT_EQUIVALENT | 0 |
| 74 | P3 | database.protein.domain_structure | BASELINE_EQUIVALENT_PRESENT | 3 |
| 75 | P3 | analysis.bioimage.registration | BASELINE_EQUIVALENT_PRESENT | 1 |
| 76 | P3 | analysis.genomics.regulatory_motif | BASELINE_EQUIVALENT_PRESENT | 3 |
| 77 | P3 | database.variant.clinical_evidence | BASELINE_EQUIVALENT_PRESENT | 4 |
| 78 | P3 | data_provenance.datalad.versioned_research_data | CLEAR_GAP | 0 |
| 79 | P3 | interpretation.gnomad.constraint_sv_acmg | CLEAR_GAP | 0 |
| 80 | P3 | analysis.glyco.engineering | BASELINE_EQUIVALENT_PRESENT | 1 |

完整机器队列：`codex-phase9-validation-queue.jsonl`。
