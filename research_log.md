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

## 2026-08-24 — Authenticated GitHub queue correction

- Experimental hypothesis: A shared REST/GraphQL queue can safely serve ten research workers if unauthenticated state cannot contaminate authenticated allowance and cached bodies cannot cross credentials.
- Observed failure: REST stored authenticated and unauthenticated timestamps plus limits in one singleton bucket; a 60/hour response contaminated prior 5,000/hour state. GraphQL failed closed without a token but still mixed different authenticated tokens.
- Suspected cause: Reservation and response-update functions received only worker identity, not a credential-scoped state key; sandboxed workers also cannot read the macOS Keychain helper.
- Modification: Made REST fail closed without authentication, pinned one credential per state directory, shared its REST/GraphQL allowance across workers, isolated response caches by full credential SHA-256, made reset updates monotonic, moved reservation behind slot acquisition, applied global Retry-After, and reconciled GraphQL actual cost.
- Result change: Offline no-token tests exited 77 without creating state files; a 147-event legacy fixture was ignored and a second synthetic credential exited 77 before cache lookup, rate reservation, slot acquisition or network I/O. Final escalated REST and GraphQL smoke calls used `git-credential`, each reported a 5,000 limit, and wrote mode-0600 state/response/meta files.
- Retained: Yes; surgical queue code/documentation changes and evidence 181 retained. No token or authorization value was written or printed.

## 2026-08-24 — Accelerated external deep audit batch 006

- Experimental hypothesis: A second 50-family shard can sustain ten-agent throughput while parent reverse-identity validation prevents stale order/ID reuse.
- Observed failure: The first reducer accepted five unrelated but valid Biomni repository IDs because it checked only ID existence, not ID-to-queue round trips; it also omitted one ai-nuggets member. Twenty-one substantive families independently failed scientific, security, privacy, provenance, licensing or reproducibility contracts.
- Suspected cause: One worker reused numeric orders from an older fork shard, and the structural reducer harvested literal IDs without comparing the complete canonical repository set for each external queue order.
- Modification: Re-audited the five real OpenFold3/plugin-registry/NSCLC-Agent/TorchGeo/isic-cli families, added parent primary-artifact verification, and enforced G1–G10 exact set, queue round-trip, name/family/member completeness and verifier-identity gates before allocating 26 Changes and 12 Lineages.
- Result change: Fifty families and 64 repository records became `DEEP_AUDITED`; family coverage rose 62→112, unresolved families fell 2,007→1,957, and queued HIGH records fell 2,085→2,021. No Feature/Implementation was allocated and all direct adoption was rejected or deferred.
- Retained: Yes; corrected report, 50-row/64-ID manifest, changes 114–139, lineages 40–51, evidence 182–189, database/control updates, identity-gate failure history and next 50-family shard retained.

## 2026-08-24 — Accelerated external deep audit batch 007

- Experimental hypothesis: Strict database-derived identity sets can sustain another 50-family checkpoint while preserving substantive source-PR and nested-branch evidence without promoting catalog duplicates.
- Observed failure: Nineteen substantive families failed scientific, security, privacy, provenance, licensing or reproducibility contracts; 26 other families were catalog/document/maintenance lineages and five had no bounded unique code. Large external child universes, such as 24,484 superpowers forks, could not be described as globally audited.
- Suspected cause: Metadata screening intentionally maximized recall across catalogs, exact forks and research prototypes, while several source PRs or nondefault branches contained real but unaccepted changes.
- Modification: Ran ten exact-identity MAP and ten independent verifier paths, applied count/scientific/severity/privacy corrections, preserved 28 change components and nine lineages, and explicitly bounded child-fork and API-invisible-ref claims.
- Result change: Fifty families and 53 repository records became `DEEP_AUDITED`; family coverage rose 112→162, unresolved families fell 1,957→1,907, and queued HIGH records fell 2,021→1,968. No Feature/Implementation was allocated and all direct adoption was rejected or deferred.
- Retained: Yes; report, 50-row/53-ID manifest, changes 140–167, lineages 52–60, evidence 190–197, database/control updates and next 50-family shard retained.

## 2026-08-24 — GraphQL cache success-integrity correction

- Experimental hypothesis: A query cache is safe only if cached identity and freshness are combined with proof that the original GraphQL response succeeded.
- Observed failure: A large Batch 008 query returned a 502 HTML body; because its sidecar lacked HTTP/error outcome fields, the next identical call returned false `200 cached=true`.
- Suspected cause: The cache-hit predicate checked only input SHA and age, while metadata was written before HTTP/GraphQL success checks.
- Modification: Added `http_status`, `graphql_errors` and `successful` sidecar fields and required successful HTTP 200/no-errors state before any cache hit; diagnostic failure bodies remain inspectable.
- Result change: The frozen 502 entry made real retry attempts and persisted `successful=false`; a separate cost-1 query returned 200 on first call and `cached=true` only on the second.
- Retained: Yes; surgical queue/README changes, redacted live verification and evidence 198 retained. The invalid cached body was excluded from research evidence.

## 2026-08-24 — Accelerated external deep audit batch 008

- Experimental hypothesis: Success-only API evidence and strict identity gates can sustain a fourth 50-family checkpoint while preserving rejected historical/source-PR changes.
- Observed failure: A GraphQL 502 body exposed the false-cache-success defect and was excluded. Twenty-one substantive families failed scientific, security, privacy, provenance, licensing or reproducibility contracts; one independent repository was a non-biomedical screening false positive.
- Suspected cause: Metadata screening mixed exact forks, catalog rows, historical maintainer branches, scientific prototypes and medical platforms, while the queue cache lacked original-response outcome fields.
- Modification: Corrected and live-verified the GraphQL cache, ran ten MAP/ten verifier paths, enforced 56-row exact identity sets and zero-weight failed API evidence, and normalized 29 changes plus 12 lineages.
- Result change: Fifty families and 56 repository records became `DEEP_AUDITED`; family coverage rose 162→212, unresolved families fell 1,907→1,857, and queued HIGH records fell 1,968→1,912. No Feature/Implementation was allocated and all direct adoption was rejected or deferred.
- Retained: Yes; report, 50-row/56-ID manifest, changes 168–196, lineages 61–72, evidence 199–206, database/control updates, success-only cache evidence and next 50-family shard retained.

## 2026-08-24 — GPT Pro handoff boundary

- Experimental hypothesis: A clean GitHub checkpoint plus an explicit prompt can transfer the remaining long-running audit without replaying completed batches or losing identity/rate-limit invariants.
- Observed failure: N/A; the user requested that Batch 009 not start under the current agent.
- Suspected cause: N/A.
- Modification: Interrupted the sole just-dispatched Batch 009 worker, accepted no Batch 009 MAP result, and set orders 213–262 back to `NOT_STARTED` while preserving completed Batch 008.
- Result change: Canonical coverage remains 212/2,069 external families and 249 deep-audited records; the next agent has an exact unstarted boundary.
- Retained: Yes; authoritative state, coverage, queue boundary and GPT Pro handoff prompt retained.

## 2026-08-24T06:18:57Z — External deep audit Batch 009

- Closed exact queue orders 213–262: 50 families / 52 records.
- Result counts: DEEP_AUDIT_CANDIDATE=13, DOC_METADATA_MAINTENANCE_ONLY=2, NO_UNIQUE_OR_SOURCE_LINEAGE=35.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000207, evidence-000208, evidence-000209, evidence-000210.

## 2026-08-24T06:19:22Z — External deep audit Batch 010

- Closed exact queue orders 263–312: 50 families / 56 records.
- Result counts: DEEP_AUDIT_CANDIDATE=17, DOC_METADATA_MAINTENANCE_ONLY=7, NO_UNIQUE_OR_SOURCE_LINEAGE=26.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000211, evidence-000212, evidence-000213, evidence-000214.

## 2026-08-24T06:19:44Z — External deep audit Batch 011

- Closed exact queue orders 313–362: 50 families / 51 records.
- Result counts: DEEP_AUDIT_CANDIDATE=19, DOC_METADATA_MAINTENANCE_ONLY=1, EMPTY=1, NO_UNIQUE_OR_SOURCE_LINEAGE=29.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000215, evidence-000216, evidence-000217, evidence-000218.

## 2026-08-24T06:20:24Z — External deep audit Batch 012

- Closed exact queue orders 363–412: 50 families / 50 records.
- Result counts: DEEP_AUDIT_CANDIDATE=17, DOC_METADATA_MAINTENANCE_ONLY=3, NO_UNIQUE_OR_SOURCE_LINEAGE=30.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000219, evidence-000220, evidence-000221, evidence-000222.

## 2026-08-24T06:20:57Z — External deep audit Batch 013

- Closed exact queue orders 413–462: 50 families / 60 records.
- Result counts: DEEP_AUDIT_CANDIDATE=13, DOC_METADATA_MAINTENANCE_ONLY=4, NO_UNIQUE_OR_SOURCE_LINEAGE=33.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000223, evidence-000224, evidence-000225, evidence-000226.

## 2026-08-24T06:21:37Z — External deep audit Batch 014

- Closed exact queue orders 463–512: 50 families / 51 records.
- Result counts: DEEP_AUDIT_CANDIDATE=21, DOC_METADATA_MAINTENANCE_ONLY=1, EMPTY=1, NO_UNIQUE_OR_SOURCE_LINEAGE=27.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000227, evidence-000228, evidence-000229, evidence-000230.

## 2026-08-24T06:22:12Z — External deep audit Batch 015

- Closed exact queue orders 513–562: 50 families / 51 records.
- Result counts: DEEP_AUDIT_CANDIDATE=17, DOC_METADATA_MAINTENANCE_ONLY=3, EMPTY=1, NO_UNIQUE_OR_SOURCE_LINEAGE=29.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000231, evidence-000232, evidence-000233, evidence-000234.

## 2026-08-24T06:22:40Z — External deep audit Batch 016

- Closed exact queue orders 563–612: 50 families / 53 records.
- Result counts: DEEP_AUDIT_CANDIDATE=11, DOC_METADATA_MAINTENANCE_ONLY=1, EMPTY=1, NO_UNIQUE_OR_SOURCE_LINEAGE=37.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000235, evidence-000236, evidence-000237, evidence-000238.

## 2026-08-24T06:22:56Z — External deep audit Batch 017

- Closed exact queue orders 613–662: 50 families / 56 records.
- Result counts: DEEP_AUDIT_CANDIDATE=16, DOC_METADATA_MAINTENANCE_ONLY=1, NO_UNIQUE_OR_SOURCE_LINEAGE=33.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000239, evidence-000240, evidence-000241, evidence-000242.

## 2026-08-24T06:23:19Z — External deep audit Batch 018

- Closed exact queue orders 663–712: 50 families / 53 records.
- Result counts: DEEP_AUDIT_CANDIDATE=17, DOC_METADATA_MAINTENANCE_ONLY=3, NO_UNIQUE_OR_SOURCE_LINEAGE=30.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000243, evidence-000244, evidence-000245, evidence-000246.

## 2026-08-24T06:23:51Z — External deep audit Batch 019

- Closed exact queue orders 713–762: 50 families / 52 records.
- Result counts: DEEP_AUDIT_CANDIDATE=6, DOC_METADATA_MAINTENANCE_ONLY=5, EMPTY=1, NO_UNIQUE_OR_SOURCE_LINEAGE=38.
- Static-only review; no third-party code executed; all direct adoption rejected.
- Evidence: evidence-000247, evidence-000248, evidence-000249, evidence-000250.
