# Concurrency, API queue and accelerated scheduling

Observed at: `2026-08-23T17:39:08Z`

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

The first accelerated shard covers stable queue orders 13–62: 50 families split
across available workers. Stable queue order never changes after resolution.

## Worker concurrency

The requested target is ten research workers plus the parent reducer. The current
collaboration service admitted nine non-root workers; the tenth creation returned
`agent thread limit reached`. Completed slots are immediately reused so the queue
stays saturated without claiming unavailable concurrency.

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
  helper and never printed or written.

Authenticated self-tests returned 5,000/hour for both REST and GraphQL. At the
explicit 60/minute request ceiling, sustained REST throughput is at most
3,600/hour, so ten workers average at most 360 requests/hour—one every ten
seconds—not 400/hour.

## Batch inventory and caching

Repository inventory should use GraphQL aliases/connections to fetch many fields
per point. Queries must include `rateLimit { limit cost remaining resetAt }`, cap
each `first:` at 100 and provide a conservative estimated cost. Cursor values are
persisted in per-worker temporary page files.

REST is retained for endpoint-specific facts such as exact PR state, releases and
conditional pagination. REST response sidecars persist URL, ETag, Last-Modified
and check time; a repeated request reuses the prior body on HTTP 304. GraphQL uses
a query+variables SHA-256 cache for five minutes. Git refs/history always use SSH
and local computation rather than API commit-by-commit calls.

## Completion and recovery

A family is complete only when its bounded native refs, source comparison refs,
required PR/release/fork endpoints and substantive static audit are closed. Worker
results remain non-canonical until parent verification. Partial results preserve
the exact order, cursor, cache paths and missing surfaces; interruption resumes
those artifacts rather than restarting discovery.
