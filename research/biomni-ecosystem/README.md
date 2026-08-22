# Biomni Public Ecosystem Research Database

This directory is the durable, evidence-backed record for the bounded Biomni
ecosystem audit. It stores human-readable research notes beside machine-readable
JSONL records so that later Codex sessions can resume from Git rather than chat
memory.

## Resume protocol

Read these files first, in order:

1. `STATE.md`
2. `MASTER_INDEX.md`
3. `COVERAGE.md`
4. the detailed file named by `current_entity` in `STATE.md`

## Governing rules

- Research universe and the one-hop people boundary: `methodology/scope.md`
- Claim and source handling: `methodology/evidence-policy.md`
- Unique-change and lineage resolution: `methodology/deduplication-policy.md`
- Static-research safety constraints: `methodology/security-policy.md`
- Observability limits: `methodology/limitations.md`

Canonical state, coverage, IDs, feature selection, and JSONL records are managed
by the parent research coordinator. Worker output is provisional until verified
and normalized.
