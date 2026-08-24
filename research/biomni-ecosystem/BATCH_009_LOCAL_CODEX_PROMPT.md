# Local Codex continuation prompt — Batch 009 and later

Continue the Biomni ecosystem audit from the GitHub remote. Do not restart completed work.

## Repository checkpoint

- Repository: `MikeGong1/Biomni`
- Branch: `research/biomni-ecosystem-audit`
- Audit subtree: `research/biomni-ecosystem/`
- Remote recovery was based on pre-handoff head `264ccf16d0f05a0bde49b2ad543ffe4f2b0e5ced`
- Canonical `repositories.jsonl` blob observed by the remote pass: `892a1adf1c9e28af288cbd5e1fdad511efc12185`
- Batch 001–008 are complete.
- Canonical completed progress remains 212 / 2,069 families.
- Batch 009 is `NOT_STARTED` for canonical purposes.
- Batch 009 scope is exact queue orders 213–262: 50 families / 52 repository records.

## Read first

1. `research/biomni-ecosystem/STATE.md`
2. `research/biomni-ecosystem/GPT_PRO_HANDOFF_PROMPT.md`
3. `research/biomni-ecosystem/external-repos/deep-audit-batch-009-remote-recovery.md`
4. `research/biomni-ecosystem/external-repos/deep-audit-batch-009-recovery-manifest.jsonl`
5. Batch 008 report and manifest
6. queue, identity-gate and methodology files referenced by the main handoff prompt

## Mandatory startup checks

```bash
git fetch origin research/biomni-ecosystem-audit
git switch research/biomni-ecosystem-audit
git pull --ff-only
git status --short --branch
git log -3 --oneline
```

Use the latest remote branch as authority. The recovery manifest is not canonical and must be verified against `database/repositories.jsonl`.

## Task A — finish Batch 009

1. Extract all canonical records with `external_deep_audit_queue_order` in 213–262.
2. Assert exactly 50 orders, 50 family keys, 52 repository records, one representative per family, and matching member counts.
3. Resolve recovery placeholders for orders:
   `215, 228, 235, 240, 252, 253, 260`.
4. Resolve the second member of order `258`.
5. Correct any recovered mapping that disagrees with canonical data.
6. Pin immutable heads and exhaust the bounded static evidence surfaces for each family.
7. For forks, compare source and fork DAGs, refs, unique commits, patch/content groups and PR lineage.
8. Review source text for correctness, scientific validity, security, privacy, provenance, supply chain, licensing and integration suitability.
9. Do not execute third-party code, notebooks, installers, workflows, models, containers or tests.
10. Produce the final Batch 009 report and final manifest using the Batch 008 schema and permitted result classes.
11. Run the exact identity, count, reverse-member, representative, evidence and canonical round-trip gates.
12. Only after all gates pass, update canonical databases, indexes, coverage, state, queue summary and `research_log.md`, then commit and push.

Never mark a family `DEEP_AUDITED` from metadata or identity recovery alone. Never allocate Feature or Implementation IDs without validated, retained capability evidence.

## Task B — continue later batches

After Batch 009 is fully committed and verified:

- Batch 010: 263–312
- Batch 011: 313–362
- continue in stable 50-family windows;
- Batch 045: 2013–2062
- Batch 046: 2063–2069

For every batch, use the same static-only policy, final report/manifest pair, canonical round-trip checks and commit/push discipline. Stop only on a concrete capability or evidence blocker; record partial work without inflating completion counters.
