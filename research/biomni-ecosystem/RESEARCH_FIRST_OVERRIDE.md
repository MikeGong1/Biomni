# Research-first source-use override

Effective UTC: `2026-08-24`

Status: **ACTIVE PLANNING OVERLAY**

This file changes how the completed Phase 8 evidence is prioritized for the user's current research goal: learning from Biomni and the surrounding ecosystem to build a separate scientific agent system.

It does **not** erase or rewrite the historical Batch 001–046 findings. The existing Change, Lineage, Evidence, security, privacy, scientific-validity and provenance records remain the source of truth for what was observed. This overlay changes only the downstream research-selection policy.

## Superseding research decision

1. The 598 families classified as `DEEP_AUDIT_CANDIDATE` are reopened as a source-first research queue.
2. `LICENSE_UNCLEAR`, missing root license, mixed component licenses, non-commercial terms or unresolved provenance must no longer exclude a candidate from Feature or Implementation discovery.
3. Historical labels such as `CLEAN_ROOM_ONLY`, `REJECT_DIRECT_ADOPTION` and `REJECT_AS_IS` remain valid warnings about direct release or production adoption, but they are not research-discovery blockers.
4. For private research and prototyping, the preferred sequence is now:

   `inspect original source → preserve exact provenance → reproduce or adapt the implementation in a research workspace → validate behavior → normalize Feature/Implementation`

   This replaces the former clean-room-first sequence.
5. License and provenance remain recorded as metadata. They are not used as negative scientific or functional scores.
6. Public redistribution, publication of copied source, product release or relicensing remains a separate later review gate. Academic citation and source-code permission are recorded separately.
7. Security, privacy, scientific correctness, clinical validity, data governance, model trust and supply-chain findings are **not relaxed** by this override.

## New research dispositions

- `SOURCE_FIRST_RESEARCH_CANDIDATE`: original implementation should be inspected and may be reproduced in a research-only workspace with exact attribution.
- `SOURCE_FIRST_WITH_REMEDIATION`: source is valuable, but identified scientific, security, privacy or runtime defects must be fixed before reliance.
- `REFERENCE_ONLY_BLOCKED`: preserve architecture or interface ideas, but do not run or reuse the implementation until critical non-license blockers are resolved.
- `DUPLICATE_OR_SUPERSEDED`: keep provenance, but normalize to the stronger/current implementation.
- `PUBLICATION_REVIEW_REQUIRED`: candidate can be researched now; redistribution and article-associated software release require a later targeted review.

## Immediate priority queue

### P0 — largest likely capability recovery

1. `jaechang-hits/SciAgent-Skills`, changes `change-000081`–`change-000087`
   - 203 active scientific Skills.
   - 125 previously retained reconstruction leads.
   - Reopen for per-Skill source extraction, Feature normalization and implementation comparison.
2. `K-Dense-AI/scientific-agent-skills` and `kuanlinhuang/claude-scientific-skills`, changes `change-000088`–`change-000091`
   - 12-Skill bundle plus BIDS and DataLad designs.
   - Reopen for source-level decomposition rather than license-led rejection.
3. `KalinNonchev/ChatSpatial` / DeepSpot-M, `change-000093`
   - Reopen the histology-to-spatial-expression workflow for source-first study.
   - Preserve the existing scale, privacy, cancellation and model-trust findings as remediation requirements.

### P1 — high-value systems and data-tool designs

4. `QING1105/ezST`, `change-000077`–`change-000078`
   - Five-stage spatial-transcriptomics workflow, human gates, loader and packaging patterns.
5. `Mr-Milk/Aquila-next`, `change-000092`
   - Full spatial single-cell platform: ingestion, catalog, browser workspace, Rust/FastAPI analysis services and visualization.
6. `KalinNonchev/gnomAD_DB`, `change-000096`
   - Local population-frequency cache/database design.
   - Separate code implementation value from gnomAD data terms and provenance.

### P2 — valuable only with stronger remediation

7. `samutiti/Biomni`, `change-000074`: local/remote ESM embedding precursor.
8. `Ali-Maq/Biomni_Replica`, `change-000032`: large multi-domain scientific Skill implementation set.
9. `PMK89/Biomni`, `change-000047`–`change-000048`: snapshot, PBPK and workflow designs.
10. `standardmodelbio/Biomni`, `change-000075`: Docker/uv environment design.
11. `Rasic2/Biomni`, `change-000073`: Azure/MCP/LangGraph supervisor prototype.
12. `cvxluo/reti`, `change-000070`: medical-genetics product architecture; reference only until clinical, privacy and security blockers are resolved.

The complete machine-readable reopening set is stored in:

`external-repos/research-first-reopen-manifest.jsonl`

The governing method is stored in:

`methodology/research-first-source-policy.md`

The local Codex continuation instructions are stored in:

`CODEX_RESEARCH_FIRST_PROMPT.md`

## Next action

Do not rerun Batch 001–046 discovery. Start Feature and Implementation normalization from the reopened source-first queue, beginning with SciAgent-Skills and the K-Dense scientific skill lineages. Use the existing immutable repository, commit, file and lineage evidence as the provenance ledger, then perform scientific, security and runtime validation independently from license classification.
