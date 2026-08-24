# Phase 9A static research completion summary

Completed by bounded repository-evidence analysis.

Status: **COMPLETE_STATIC_RESEARCH**

## Coverage

- Phase 8 external families retained: **2,069 / 2,069**.
- Phase 9 candidate families statically normalized: **598 / 598**.
- SciAgent active Skills assigned a Phase 9 disposition: **203 / 203**.
- SciAgent source-first candidate Skills: **125 / 125**.
- Provisional Feature clusters: **91**.
- Provisional Implementation records: **801**.
- Commercial behaviors compared against the static OSS catalog: **17 / 17**.
- Codex validation clusters prepared: **91**.
- Third-party runtime executions: **0**.
- Canonical Feature IDs allocated: **0**.
- Canonical Implementation IDs allocated: **0**.

## Family-level static gap distribution

| Biomni gap | Families |
|---|---|
| BASELINE_EQUIVALENT_PRESENT | 75 |
| CLEAR_GAP | 469 |
| PARTIAL_OVERLAP | 9 |
| RELATED_OVERLAP_NOT_EQUIVALENT | 45 |

## Family-level research disposition

| Disposition | Families |
|---|---|
| DUPLICATE_OR_SUPERSEDED | 73 |
| REFERENCE_ONLY_BLOCKED | 32 |
| SOURCE_FIRST_WITH_REMEDIATION | 493 |

## SciAgent disposition

| Disposition | Skills |
|---|---|
| DUPLICATE_OR_SUPERSEDED | 30 |
| REFERENCE_ARCHIVE_NO_NEAR_TERM | 78 |
| REFERENCE_ONLY_BLOCKED | 10 |
| SOURCE_FIRST_WITH_REMEDIATION | 85 |

## Provisional Feature distribution

| Biomni gap | Features |
|---|---|
| BASELINE_EQUIVALENT_PRESENT | 18 |
| CLEAR_GAP | 59 |
| PARTIAL_OVERLAP | 8 |
| RELATED_OVERLAP_NOT_EQUIVALENT | 6 |

Priority: P0 44, P1 1, P2 28, P3 18.

## Completion boundary

Phase 9A is the complete GPT Pro/static-research layer. It uses existing immutable identity, Change, Lineage, Phase 8 static findings, SciAgent per-Skill audit and the frozen Biomni baseline. It does not claim runtime correctness.

Phase 9B remains Codex-required validation: exact source checkout, symbol-level comparison, characterization tests, scientific validation, source-to-sink security analysis, privacy/data-flow review, provenance ledger, and canonical Feature/Implementation database writes.

## Integrity

- Candidate-family count assertion: passed.
- SciAgent 203/203 assertion: passed.
- SciAgent candidate 125/125 assertion: passed.
- JSONL output generation: passed.
- Parse diagnostics: **0** non-fatal rows/messages; see `phase9-static-generation-diagnostics.json`.
