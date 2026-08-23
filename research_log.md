# Research Log

## 2026-08-23 — SciAgent-Skills ecosystem deep audit

- Experimental hypothesis: SciAgent-Skills may contain independently useful, integration-ready scientific capabilities beyond Biomni's frozen baseline.
- Observed failure: Static review found material cross-domain scientific errors, unreproducible benchmark claims, unsafe instruction and supply-chain surfaces, and incomplete provenance across the 203-Skill corpus; three fork variants also lacked sufficient correctness, runtime, privacy, license, or integration evidence.
- Suspected cause: The corpus is an instruction-generation collection assembled from heterogeneous tools and services without a uniform executable validation, provenance, or safety contract.
- Modification: Froze and normalized the source branch/PR DAG, all 203 active Skills and 85 ancillary files, and all 34 public forks; retained only 125 bounded clean-room requirement leads and seven change/two lineage records.
- Result change: External deep-audit batch 001 advanced from 2 complete plus 1 partial to 3/3 complete; SciAgent-Skills is now `DEEP_AUDITED` and rejected as-is with no Feature/Implementation allocation.
- Retained: Yes; research-only database, manifests, detailed report, coverage, index, and resume-state updates retained.

## 2026-08-24 — External fork-only families batch 002

- Experimental hypothesis: Five high-relevance BioNeMo, ClawBio, and Scanpy forks may contain substantive capabilities absent from their authoritative upstream sources.
- Observed failure: All default histories were exact source tips or source ancestors; the three apparent unique heads reduced to two generated artifacts and one exact open DOC_ONLY upstream PR ref.
- Suspected cause: Metadata-only screening correctly favored recall but treated recently pushed forks and generated branches as potential independent implementations before Git DAG normalization.
- Modification: Froze all native refs and bounded fork PR/release/child-fork surfaces, compared them against full source ref unions, statically inspected three deltas, and independently verified the DAG and native tag counts.
- Result change: Queue orders 2–4 and five repository records moved from `NOT_STARTED` to `DEEP_AUDITED`/no-substantive-unique; unresolved family count fell from 2,066 to 2,063 with no new canonical capability IDs.
- Retained: Yes; detailed batch report, five-row lineage manifest, five evidence records, repository/entity status changes, control-ledger updates, and the tag auto-follow correction retained.

## 2026-08-24 — External fork families batch 003

- Experimental hypothesis: Seven K-Dense, Latch, and medical-AI forks may expose independent scientific capabilities or safer successors absent from their source repositories.
- Observed failure: Latch was exact source, the medical-AI delta was one catalog row, and most K-Dense refs were source history/PRs; the substantive Kuan, BIDS, and DataLad content contained material scientific, privacy, execution, deletion, supply-chain, version-identity, and provenance blockers.
- Suspected cause: Metadata screening conflated recently pushed fork refs and same-name releases with independent capability, while instruction corpora lacked uniform executable scientific/security validation.
- Modification: Froze and normalized 15 heads, 170 tags, 674 source PR refs, bounded PR/release/child-fork surfaces, 12 Kuan Skills, BIDS PR 125, DataLad PR 227, two fork API patches, and minor documentation/environment deltas.
- Result change: Seven repository records and three families became `DEEP_AUDITED`; four changes and three lineages were retained, unresolved family count fell from 2,063 to 2,060, and no Feature/Implementation was allocated.
- Retained: Yes; batch report, two machine manifests, evidence 163–168, changes 88–91, lineages 33–35, database/control updates, and same-name tag collision warnings retained.

## 2026-08-24 — Awesome-list fork families batch 004

- Experimental hypothesis: Three high-relevance awesome-list forks may contain independent biomedical-agent, scientific-Skill, or pathology implementations.
- Observed failure: Every delta was a README catalog row already represented by a merged/open source PR; the Pathology fork itself was only a source ancestor.
- Suspected cause: Metadata screening correctly recognized domain-rich descriptions but could not distinguish curated links from executable implementations or source PR refs.
- Modification: Froze six mirrors, six fork heads, 29 source pull refs, bounded endpoints, five relevant PR histories, current outbound identities, official ClawBench paper metadata, and license/person boundaries.
- Result change: Three repository records/families became `DEEP_AUDITED`; unresolved family count fell from 2,060 to 2,057, with no new Repository, Person, Change, Lineage, Feature, or Implementation ID.
- Retained: Yes; batch report, three-row manifest, evidence 169–173, corrected ClawBench catalog facts, merged Pathology owner-PR history, and duplicate Dr. Claw lead normalization retained.

## 2026-08-24 — Accelerated scheduler and shared GitHub API queue

- Experimental hypothesis: Phase 8 throughput is constrained primarily by three-family scheduling and repeated per-repository REST requests, not the authenticated GitHub allowance.
- Observed failure: At three families per checkpoint, 2,060 pending families implied roughly 687 batches; the service also admitted nine non-root workers rather than the requested ten.
- Suspected cause: Prior checkpoints coupled all workers to one small family set and used REST for inventory fields that GraphQL can batch.
- Modification: Added a shared four-slot queue with 60/min global and six/min/worker limits, authenticated REST/GraphQL rate tracking, GraphQL point headroom, ETag/304 and query-hash caches, cursor-friendly pages, and a complexity-aware 50-family shard across orders 13–62.
- Result change: Live self-tests returned REST and GraphQL limits of 5,000/hour; GraphQL cost 1 and cache hit, REST 200 then 304. Nine admitted workers now own multiple independent families with slot rotation.
- Retained: Yes; methodology, queue scripts, runtime evidence 174, index/state/coverage/queue documentation, and research log retained. No token or credential material retained.

## 2026-08-24 — Accelerated external deep audit batch 005

- Experimental hypothesis: Moving from three-family checkpoints to 50 mutually independent families can materially increase Phase 8 throughput without exhausting GitHub limits or weakening evidence quality.
- Observed failure: Twenty-two substantive candidates all failed at least one material scientific, security, privacy, provenance, licensing, runtime or reproducibility contract; 28 other families reduced to source/PR history, documentation-only content or empty repositories.
- Suspected cause: Metadata-first screening intentionally maximized recall and could not distinguish independent capabilities from source refs, generated/catalog content, incomplete research prototypes or unsafe wrappers.
- Modification: Audited exact queue orders 13–62 through shared REST/GraphQL limits and local SSH/DAG analysis, applied eight independent verifier shards, allocated one composite Change per substantive family and only four evidence-supported Lineages.
- Result change: Fifty families and 58 repository records became `DEEP_AUDITED`; family coverage rose 12→62, unresolved families fell 2,057→2,007, and queued HIGH records fell 2,143→2,085. No Feature/Implementation was allocated and all direct adoption was rejected.
- Retained: Yes; report, 50-row canonical manifest, changes 92–113, lineages 36–39, evidence 175–180, repository/entity/control updates and next 50-family shard retained.
