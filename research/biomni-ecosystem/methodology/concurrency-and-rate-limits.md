# Concurrency, API queue and accelerated scheduling

Observed at: `2026-08-23T19:08:47Z`

## Scheduling unit

The unit is an external repository **family**: one normalized source plus all
bounded person-repository members assigned to that source. It is not one file,
one GitHub page or one worker.

Phase 8 no longer schedules only three families per checkpoint. The default
checkpoint targets are:

- 30–100 families when metadata and Git prove fork-only/no-unique, awesome-list,
  DOC_ONLY or source-ancestor closure;
- 10–20 medium-complexity families;
- dedicated multi-worker review only after a family exposes substantive code.

The first accelerated shard closed stable queue orders 13–62. The second covers
orders 63–112, again as 50 mutually exclusive family assignments. Stable queue
order never changes after resolution.

## Worker concurrency

The target is ten non-root research workers plus the parent reducer. Batch 005
initially used nine admitted workers with completed slots rotated. Batch 006 uses
ten non-root workers on ten five-family shards; completed MAP slots immediately
rotate into independent VERIFY or structural REDUCE work.

Workers may independently use SSH Git, local DAG traversal, diff, patch-id and
static inspection. The parent alone writes stable IDs, canonical database files,
coverage, index and state.

## Shared GitHub request queue

All GitHub REST and GraphQL requests use the scripts under
`workers/github-api-queue/`. Direct worker calls to `api.github.com` are not
allowed.

Shared controls:

- four in-flight request locks;
- 60 requests/minute globally;
- six requests/minute per worker;
- REST primary-limit/reset tracking and `Retry-After` cooldown;
- GraphQL point tracking with 20% primary headroom;
- credentials read only from `GITHUB_TOKEN`, `GH_TOKEN` or the Git credential
  helper and never printed or written;
- REST and GraphQL request modes fail closed with exit 77 when no authenticated
  credential is available;
- one authenticated credential is pinned per queue state directory; a different
  credential fails closed with exit 77 rather than sharing or replacing its
  primary state;
- all workers using the pinned credential share one REST primary bucket, one
  GraphQL points bucket, global/per-worker counters, `Retry-After`, and the four
  concurrency locks;
- REST and GraphQL response caches are isolated by a full SHA-256 credential
  fingerprint, which is never printed and cannot be used for authentication.

Authenticated self-tests returned 5,000/hour for both REST and GraphQL. At the
explicit 60/minute request ceiling, sustained REST throughput is at most
3,600/hour, so ten workers average at most 360 requests/hour—one every ten
seconds—not 400/hour.

### Credential-state correction

The original REST wrapper used one singleton `primary` list and one set of
limit/remaining/reset fields. An unauthenticated 60/hour response could therefore
reinterpret earlier authenticated timestamps under the smaller limit, while an
authenticated response could temporarily let unauthenticated calls escape the
48/hour local cap. GraphQL already rejected missing credentials, but different
authenticated tokens shared one points bucket.

The corrected wrappers ignore those un-attributable legacy singleton fields,
pin one full credential SHA-256 per state directory, and record all workers for
that credential in conservative shared REST/GraphQL buckets. A different
credential fails before cache lookup, rate reservation or network I/O. Cache
identity also includes the full fingerprint. The fingerprint is a local
pseudonymous state/cache key, not an authentication secret; it is never printed
and state/meta files are mode 0600. On this macOS host
the Keychain helper is unavailable inside the managed sandbox but available
through the approved escalated/root path; workers must use that path or preserve
an explicit API gap rather than fall back to unauthenticated traffic.

The request slot is acquired before the final rate reservation so queued work
cannot start on an expired reservation. Response updates cannot replace a newer
reset window with an older one, `Retry-After` creates a cross-protocol global
cooldown, and GraphQL replaces each estimated reservation with the returned
actual cost while surfacing any underestimate.

Offline validation showed: both protocols exit 77 without a credential and add
no state file; a legacy fixture with 147 singleton timestamps does not enter the
authenticated bucket; the pinned synthetic credential sees the shared allowance
while a second credential exits 77 before I/O. Credential-cache separation is
also enforced in both code paths. Approved live smoke requests reported
`auth_source=git-credential`, REST
`rate_limit=5000`, and GraphQL `rate_limit=5000` with actual cost 1. The retained
redacted verification record documents exit codes, state boundaries and output
fields without credential values.

## Batch inventory and caching

Repository inventory should use GraphQL aliases/connections to fetch many fields
per point. Queries must include `rateLimit { limit cost remaining resetAt }`, cap
each `first:` at 100 and provide a conservative estimated cost. Cursor values are
persisted in per-worker temporary page files.

REST is retained for endpoint-specific facts such as exact PR state, releases and
conditional pagination. REST response sidecars persist URL, credential
fingerprint, ETag, Last-Modified and check time; a repeated request reuses the
prior body on HTTP 304 only for that credential. GraphQL includes the credential
fingerprint in its query+variables SHA-256 cache identity for five minutes. Git
refs/history always use SSH and local computation rather than API
commit-by-commit calls.

## Completion and recovery

A family is complete only when its bounded native refs, source comparison refs,
required PR/release/fork endpoints and substantive static audit are closed. Worker
results remain non-canonical until parent verification. Partial results preserve
the exact order, cursor, cache paths and missing surfaces; interruption resumes
those artifacts rather than restarting discovery.
