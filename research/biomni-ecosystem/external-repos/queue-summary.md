# External repository deep-audit queue

Observed at: `2026-08-23T12:01:41Z`

Status: **PARTIAL** — queue normalization is complete; deep audit is not.

## Bounded input and exclusion

The Phase 8 input is the **2,272** person-repository records classified
`HIGH_RELEVANCE` by the metadata-only Phase 7 screen. This label is a recall-first
audit lead, not an integration recommendation.

Of those records, **111** already carry `fork_screen_status` from the completed
Biomni fork/lineage audit and are excluded from this separate external queue as
`EXCLUDED_ALREADY_SCREENED_BIOMNI_LINEAGE`. The guard also checked upstream and
fork-discovery identifiers, but those predicates added no records beyond the 111
with `fork_screen_status`. Most are named Biomni; four differently named records
are `amplicon-repo-agentai`, `BioAiSaaS`, `reti`, and `dleader_agent`. They remain
in the canonical repository database and are not discarded.

The remaining **2,161** records form the external deep-audit queue.

## Family normalization

Each queued record receives one deterministic family key:

- for a non-Biomni GitHub fork with a known parent, use the parent's `full_name`;
- otherwise use the repository's own `full_name`;
- normalize the selected string with ASCII lowercase.

This yields **2,069 unique families**. There are **66** multi-member families
containing **158** records, or 92 records beyond one representative per family.
The other 2,003 families are singletons. **513** families contain an independent
source repository already represented in the database; the remainder currently
have only fork members in the bounded person-repository universe.

The machine-readable queue is stored on each member record in
`database/repositories.jsonl`. Family representatives are deterministic database
representatives, not assertions that a fork is the authoritative upstream source.

## Scheduling priority

Priority is only a scheduling heuristic. It is not a quality, safety, novelty,
license, scientific-validity, or integration score.

- **C**: archived or disabled; otherwise proceed to the rules below.
- **A**: `pushed_at >= 2025-01-01`, combined metadata contains at least one direct
  domain signal (`bioinformatics`, `biomedical`, `drug discovery`, `single-cell`,
  `spatial transcript`, `clinical`, `protein`, `omics`, `genom`, `patholog`,
  `lab automation`, `crispr`, or `perturb`) and at least one implementation
  surface (`agent`, `skill`, `tool`, `platform`, `pipeline`, `workflow`,
  `database`, `framework`, `mcp`, or `analysis`). Matching is case-insensitive;
  punctuation variants of `single-cell` are accepted. The sole `analysis` token
  in `seandavi/awesome-single-cell` describes a curated software directory rather
  than an implementation surface, so that family is explicitly scheduled as B.
- **B**: not A/C and `pushed_at >= 2025-01-01`.
- **C**: all remaining families.

Family counts are **A 68**, **B 911**, and **C 1,090**. Ordering is deterministic:
tier A/B/C, then latest family `pushed_at` descending, then ASCII-lowercased family
key ascending. Orders are contiguous from 1 through 2,069.

## Audit progress

Three apparent independent-source A-tier families were selected near the head of
the queue for the first static batch. Static audit resolved ezST to the Biomni PR
#330 lineage, and authority-source audit closed/rejected Drug-Discovery-Safety-
Skills; SciAgent-Skills remains PARTIAL.

| Queue order | Repository | Immutable head | Audit status |
|---:|---|---|---|
| 1 | `QING1105/ezST` | `427792f0bbf2564dbf124b4444ffdb07cc400a25` | DEEP_AUDITED; DERIVED PR #330 LINEAGE |
| 5 | `jaechang-hits/SciAgent-Skills` | `a0aac0f4576a550d5316baf6da3d72e53408b3a2` | PARTIAL |
| 8 | `JinL0/Drug-Discovery-Safety-Skills` | `89364d8ea0bfd1393c51df750198ce086e0ebb84` | DEEP_AUDITED; REJECT AS-IS |

Queue orders remain stable historical scheduling identifiers and are not
renumbered after lineage resolution. The result is two deep-audited families—one
derived-lineage resolution and one independent rejection—and 2,067 families not
yet deep-audited. Detailed evidence and unresolved gaps are in
`deep-audit-batch-001.md`, `ezst.md`, and `drug-discovery-safety-skills.md`.

## Reproducibility boundary

Queue construction used only canonical Phase 7 metadata and deterministic family,
priority, and order predicates. GitHub acquisition for batch 001 was serialized
with bounded requests; repository code was decoded and inspected statically, never
executed. Mutable metadata, uncaptured sources, uninspected branches/forks, and
scientific or regulatory claims remain explicitly unresolved.
