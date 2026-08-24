# Biomni Public Ecosystem Research Database

This directory is the durable, evidence-backed record for the bounded Biomni
ecosystem audit. It stores human-readable research notes beside machine-readable
JSONL records so that later Codex sessions can resume from Git rather than chat
memory.

## Resume protocol

Read these files first, in order:

1. `RESEARCH_FIRST_OVERRIDE.md`
2. `methodology/research-first-source-policy.md`
3. `external-repos/research-first-reopen-manifest.jsonl`
4. `STATE.md`
5. `MASTER_INDEX.md`
6. `COVERAGE.md`
7. the detailed file named by `current_entity` in `STATE.md`

For local Codex continuation, read:

- `CODEX_RESEARCH_FIRST_PROMPT.md`

The research-first overlay supersedes the former license-led candidate-selection
policy, but it does not erase historical scientific, security, privacy, runtime,
lineage or provenance findings. Missing or unclear licensing no longer prevents
Feature/Implementation discovery. Public redistribution and publication review
remain a separate later gate.

## Governing rules

- Research universe and the one-hop people boundary: `methodology/scope.md`
- Claim and source handling: `methodology/evidence-policy.md`
- Unique-change and lineage resolution: `methodology/deduplication-policy.md`
- Research-first source use and provenance: `methodology/research-first-source-policy.md`
- Static-research safety constraints: `methodology/security-policy.md`
- Observability limits: `methodology/limitations.md`

Canonical state, coverage, IDs, feature selection, and JSONL records are managed
by the parent research coordinator. Worker output is provisional until verified
and normalized.
