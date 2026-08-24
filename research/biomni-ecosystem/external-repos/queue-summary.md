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

Scheduling now uses complexity-aware checkpoints rather than three families per
commit: 30–100 obvious fork-only/no-unique/DOC_ONLY families, 10–20 medium
families, and focused multi-worker review only after substantive code survives
DAG normalization. External deep-audit batches are complete through Batch 029.
The next unstarted shard is orders 1263–1312. REST and
GraphQL traffic uses the shared limiter in
`methodology/concurrency-and-rate-limits.md`; Git history uses SSH/local analysis.

## Audit progress

Three apparent independent-source A-tier families were selected near the head of
the queue for the first static batch. Static audit resolved ezST to the Biomni PR
#330 lineage, and authority-source audit closed/rejected Drug-Discovery-Safety-
Skills; full corpus/branch/PR/fork audit closed/rejected SciAgent-Skills. Batch
002 then resolved the three earlier fork-only families against their upstream
source DAGs. Batch 003 resolved K-Dense, Latch and Awesome Medical AI fork
families and retained four substantive K-Dense change sets. Batch 004 closed
three awesome-list fork families as DOC_ONLY source-PR/catalog history.

| Queue order | Repository | Immutable head | Audit status |
|---:|---|---|---|
| 1 | `QING1105/ezST` | `427792f0bbf2564dbf124b4444ffdb07cc400a25` | DEEP_AUDITED; DERIVED PR #330 LINEAGE |
| 2 | `shantanusharma/bionemo-framework` + `dabulseco/bionemo-recipes` | `30202cac91e2c23a958bf9bdeff59288f261b9bb` / `648f4d983392d0c38f2d2da18dea0479cdc650b2` | DEEP_AUDITED; SOURCE HISTORY + GENERATED DOC DEPLOYMENT; NO SUBSTANTIVE UNIQUE CODE |
| 3 | `KalinNonchev/ClawBio` | `c2c0754ba09e68c1e21edc79a63fa112ed47fd9e` | DEEP_AUDITED; SOURCE HISTORY + STALE GENERATED BENCHMARK; NO SUBSTANTIVE UNIQUE CODE |
| 4 | `KalinNonchev/scanpy` + `Mr-Milk/scanpy` | `b863ce0477f4afbce1fd5ebc267cc897854c8099` / `532d7b14c8e0d615def56438755a545af92c64d5` | DEEP_AUDITED; SOURCE ANCESTORS + OPEN DOC_ONLY PR #4311; NO SUBSTANTIVE UNIQUE CODE |
| 5 | `jaechang-hits/SciAgent-Skills` | `a0aac0f4576a550d5316baf6da3d72e53408b3a2` | DEEP_AUDITED; REJECT ALL AS-IS |
| 6 | five `K-Dense-AI/scientific-agent-skills` forks | source/fork DAG in batch manifest | DEEP_AUDITED; FOUR SUBSTANTIVE CHANGE SETS; REJECT DIRECT |
| 7 | `shantanusharma/latch` | `3f31cad1851b7ac7bfa08a4cb2bab8f9850547b8` | DEEP_AUDITED; EXACT SOURCE MAIN; NO UNIQUE CODE |
| 8 | `JinL0/Drug-Discovery-Safety-Skills` | `89364d8ea0bfd1393c51df750198ce086e0ebb84` | DEEP_AUDITED; REJECT AS-IS |
| 9 | `reacher-z/awesome-medical-ai` | `2c07fb87e498548eae357b64f1e9b2797ccf28ba` | DEEP_AUDITED; OPEN DOC_ONLY PR #2; NO IMPLEMENTATION |
| 10 | `reacher-z/Awesome-LLM-Agents-Scientific-Discovery` | `3e079cd88b573556eba8bc0ef899ba7cee10ddf9` | DEEP_AUDITED; MERGED CLAWBENCH + OPEN DR. CLAW DOC_ONLY PRS |
| 11 | `reacher-z/awesome-ai-for-science-skills` | `710783a792e200207e841f8b3171dd5c849a6563` | DEEP_AUDITED; EXACT SOURCE MAIN + OPEN DR. CLAW DOC_ONLY PR |
| 12 | `KalinNonchev/Awesome-Pathology-Agents` | `fac3ae861c814750559b6722d0388e2f9890b483` | DEEP_AUDITED; SOURCE ANCESTOR + MERGED DOC_ONLY OWNER PR HISTORY |

Queue orders remain stable historical scheduling identifiers and are not
renumbered after lineage resolution. Batches 001–004 are complete at twelve
deep-audited families: one derived-lineage resolution, two independent
rejections, seven fork/source no-capability or DOC_ONLY catalog closures, one
DOC_ONLY medical catalog closure, and one substantive K-Dense family. **2,057**
families are not yet deep-audited. Detailed evidence is in the four batch reports
and their linked manifests.

## Reproducibility boundary

Queue construction used only canonical Phase 7 metadata and deterministic family,
priority, and order predicates. GitHub acquisition for batches 001–004 was
serialized; subsequent parallel acquisition uses one bounded shared queue.
Repository code and notebooks were decoded and inspected statically, never
executed. Batch 002–003 source repositories were
lineage anchors only: their out-of-scope fork networks and full scientific/runtime
content were not deep-audited. Mutable metadata and unprocessed queue families
remain explicitly unresolved.


## Canonical completion ledger after accelerated batches

- Batch 009: orders 213–262 complete; cumulative **262/2,069 families** and **301/2,124 queued records**; **1807 families** remain.
- Batch 010: orders 263–312 complete; cumulative **312/2,069 families** and **357/2,124 queued records**; **1757 families** remain.
- Batch 011: orders 313–362 complete; cumulative **362/2,069 families** and **408/2,124 queued records**; **1707 families** remain.
- Batch 012: orders 363–412 complete; cumulative **412/2,069 families** and **458/2,124 queued records**; **1657 families** remain.
- Batch 013: orders 413–462 complete; cumulative **462/2,069 families** and **518/2,124 queued records**; **1607 families** remain.
- Batch 014: orders 463–512 complete; cumulative **512/2,069 families** and **569/2,124 queued records**; **1557 families** remain.
- Batch 015: orders 513–562 complete; cumulative **562/2,069 families** and **620/2,124 queued records**; **1507 families** remain.
- Batch 016: orders 563–612 complete; cumulative **612/2,069 families** and **673/2,124 queued records**; **1457 families** remain.
- Batch 017: orders 613–662 complete; cumulative **662/2,069 families** and **729/2,124 queued records**; **1407 families** remain.
- Batch 018: orders 663–712 complete; cumulative **712/2,069 families** and **782/2,124 queued records**; **1357 families** remain.
- Batch 019: orders 713–762 complete; cumulative **762/2,069 families** and **834/2,124 queued records**; **1307 families** remain.
- Batch 020: orders 763–812 complete; cumulative **812/2,069 families** and **885/2,124 queued records**; **1257 families** remain.
- Batch 021: orders 813–862 complete; cumulative **862/2,069 families** and **936/2,124 queued records**; **1207 families** remain.
- Batch 022: orders 863–912 complete; cumulative **912/2,069 families** and **988/2,124 queued records**; **1157 families** remain.
- Batch 023: orders 913–962 complete; cumulative **962/2,069 families** and **1039/2,124 queued records**; **1107 families** remain.
- Batch 024: orders 963–1012 complete; cumulative **1012/2,069 families** and **1090/2,124 queued records**; **1057 families** remain.
- Batch 025: orders 1013–1062 complete; cumulative **1062/2,069 families** and **1142/2,124 queued records**; **1007 families** remain.
- Batch 026: orders 1063–1112 complete; cumulative **1112/2,069 families** and **1195/2,124 queued records**; **957 families** remain.
- Batch 027: orders 1113–1162 complete; cumulative **1162/2,069 families** and **1247/2,124 queued records**; **907 families** remain.
- Batch 028: orders 1163–1212 complete; cumulative **1212/2,069 families** and **1298/2,124 queued records**; **857 families** remain.
- Batch 029: orders 1213–1262 complete; cumulative **1262/2,069 families** and **1349/2,124 queued records**; **807 families** remain.
