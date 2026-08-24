# Local Codex continuation: research-first Feature and Implementation normalization

Repository: `MikeGong1/Biomni`

Branch: `research/biomni-ecosystem-audit`

## Objective

Do not rerun external-repository discovery or Batch 001–046. Phase 8 already covers 2,069 families and 2,161 queued repository records.

Continue from the completed evidence and convert the high-value source implementations into a normalized scientific-agent capability catalog. The user's current purpose is private, non-commercial research and development of a separate agent system.

The governing policy is now source-first:

- original source should be inspected before proposing a rewrite;
- missing, unclear, mixed or non-commercial license status does not exclude a Feature or Implementation from the research catalog;
- preserve exact repository, commit, file and symbol provenance for every copied or adapted implementation;
- keep public redistribution/publication review separate from current research selection;
- do not relax scientific, security, privacy, clinical, model-trust or supply-chain requirements.

## Read first

1. `research/biomni-ecosystem/RESEARCH_FIRST_OVERRIDE.md`
2. `research/biomni-ecosystem/methodology/research-first-source-policy.md`
3. `research/biomni-ecosystem/external-repos/research-first-reopen-manifest.jsonl`
4. `research/biomni-ecosystem/STATE.md`
5. `research/biomni-ecosystem/MASTER_INDEX.md`
6. `research/biomni-ecosystem/database/changes.jsonl`
7. `research/biomni-ecosystem/database/lineages.jsonl`
8. the detailed files referenced by the selected Change records.

## Non-negotiable boundaries

- Never claim a test, model run, scientific reproduction or vulnerability proof that was not actually performed.
- Do not execute untrusted third-party installers, workflows, notebooks, model weights or scripts outside an isolated environment.
- Do not use patient, controlled, proprietary or identifiable data during initial validation.
- Preserve original evidence; add overlays and normalized records rather than deleting historical findings.
- Do not merge copied research code into Biomni production paths during this phase. Keep source snapshots, patches and prototypes in a clearly separated research workspace.

## Work queue

### Stage A — P0 source-first extraction

Process in this order:

1. SciAgent-Skills: `change-000081`–`change-000087`
   - Decompose all 203 active Skills.
   - Start from the 125 previously retained leads.
   - Create one provisional capability record per coherent Skill behavior, not per file.
2. K-Dense/Kuan skills: `change-000088`–`change-000091`
   - Decompose the 12-Skill bundle, BIDS and DataLad.
   - Keep database/API/service terms separate from implementation value.
3. ChatSpatial/DeepSpot-M: `change-000093`
   - Extract model integration, checkpoint provenance, tiling, inference and AnnData output as separate implementation units.

### Stage B — P1 platform and data-tool extraction

4. ezST: `change-000077`–`change-000078`
5. Aquila-next: `change-000092`
6. gnomAD_DB: `change-000096`
7. Ali-Maq/Biomni_Replica: `change-000032`
8. PMK89/Biomni: `change-000047`–`change-000048`

### Stage C — constrained references

9. samutiti ESM precursor: `change-000074`
10. standardmodelbio Docker/uv: `change-000075`
11. Rasic2 Azure/MCP/LangGraph: `change-000073`
12. cvxluo/reti: `change-000070`
13. Drug-Discovery-Safety-Skills: `change-000079`–`change-000080`

Then cluster and process the remaining 598 `DEEP_AUDIT_CANDIDATE` families.

## Required per-implementation record

For every implementation retained, record:

- provisional Feature key;
- provisional Implementation key;
- capability statement in one sentence;
- repository full name and canonical repository ID;
- immutable commit SHA;
- branch/PR/tag surface;
- exact files and symbols;
- lineage and derived-from relationships;
- source status: copied, adapted, wrapped, translated or rewritten;
- license/provenance observations as metadata;
- related paper, data, model and API/service sources;
- Biomni equivalent or gap;
- scientific-validation status;
- security and privacy status;
- runtime-test status;
- publication-review flag;
- recommended disposition.

## Source-first prototype rule

When a source implementation is the fastest way to understand behavior:

1. freeze the exact source SHA;
2. copy only the smallest coherent unit into a research-only workspace;
3. retain original headers/notices and add an attribution record;
4. document every modification;
5. add characterization tests before redesign;
6. compare with Biomni and semantic duplicates;
7. decide whether the final research implementation remains copied/adapted or is later replaced.

Do not use `clean-room` as the default simply because license metadata is unclear.

## Feature normalization

Use behavioral equivalence, not repository identity.

Examples:

- multiple PubMed wrappers may be one literature-search Feature with several Implementations;
- multiple MCP servers may represent different Features if their tool contracts or orchestration semantics differ;
- a UI alone is not a new scientific Feature unless it adds a material workflow capability;
- a fork with no unique behavior remains lineage evidence, not a new Implementation;
- a broken implementation may still be cataloged as an Implementation with status `REFERENCE_ONLY_BLOCKED`.

Create Feature and Implementation IDs only after semantic deduplication for the current cluster. Do not wait for all 598 candidates before persisting a completed cluster.

## Validation sequence

For each cluster:

1. static source and contract review;
2. provenance capture;
3. semantic comparison with Biomni;
4. source-to-sink security analysis;
5. privacy/data-flow analysis;
6. scientific-method review;
7. dependency/model/data/service review;
8. isolated characterization tests when feasible;
9. Feature/Implementation normalization;
10. commit the completed cluster with its report and machine-readable records.

## Expected outputs

- `CURRENT_FEATURE_CATALOG.md`
- `INTEGRATION_CANDIDATES.md`
- populated Feature and Implementation JSONL records;
- a source-attribution/provenance ledger;
- per-cluster validation reports;
- a publication-review queue separate from the research-priority queue;
- updated `STATE.md`, `MASTER_INDEX.md` and `COVERAGE.md` after each completed cluster.

## Completion definition

This phase is complete when:

- all 598 candidate families have been assigned to a normalized Feature, marked duplicate/superseded, or retained as a documented reference-only implementation;
- all 203 SciAgent Skills and all K-Dense/Kuan bounded Skills have explicit dispositions;
- every copied or adapted research implementation has exact provenance;
- license status no longer causes a capability to disappear from the Feature catalog;
- critical scientific, security and privacy blockers remain visible and are not confused with license concerns;
- `CURRENT_FEATURE_CATALOG.md` and `INTEGRATION_CANDIDATES.md` are internally consistent with the databases.
