# GitHub Queue Credential-Scope Verification

Observed at: `2026-08-23T19:08:47Z`

## Objective

Verify that the shared REST/GraphQL queue can serve ten research workers without
mixing unauthenticated 60/hour state with the authenticated 5,000 allowance,
crossing credential cache boundaries, bypassing shared secondary controls, or
exposing the GitHub credential.

## Defect and review history

The original REST queue reserved every request in one `primary` timestamp list
and let the most recent response replace one limit/remaining/reset tuple. A
later unauthenticated 60/hour response therefore reinterpreted authenticated
events under the smaller limit; the inverse ordering temporarily gave
unauthenticated calls the larger state. GraphQL already failed closed without a
credential but its primary points state was also a singleton.

The first correction used per-token rate buckets. Independent review blocked it:
cache identity did not include the credential, tokens belonging to one GitHub
principal could multiply the local GraphQL allowance, reset updates were not
monotonic, reservations could expire before a slot opened, and actual GraphQL
cost was not reconciled.

The second correction shared authenticated allowance and isolated caches.
Independent review again blocked it because genuinely different principals
could still overwrite one shared header tuple and retry underestimation was only
reported for the final attempt.

The retained design is deliberately narrower and safer:

- request mode for both protocols exits 77 without a credential;
- the first authenticated request pins one full credential SHA-256 to the queue
  state directory;
- any different credential exits 77 before cache lookup, reservation, slot or
  network I/O;
- every worker using the pinned credential shares REST, GraphQL, global,
  per-worker, four-slot and cross-protocol `Retry-After` controls;
- REST and GraphQL cache identity includes the credential fingerprint;
- slots are acquired before the final rate reservation;
- older reset-window responses cannot replace newer state;
- every GraphQL attempt replaces its estimate with returned actual cost, and an
  underestimate on any retry remains visible;
- state and cache metadata files are written atomically with mode 0600.

The fingerprint is a local pseudonymous state/cache identifier. It is not a
credential and cannot authenticate a request, but it is not printed or copied
to canonical evidence.

## Offline verification record

All credential values used below were synthetic fixtures. No GitHub request was
made by these tests.

| Check | REST | GraphQL |
|---|---|---|
| Syntax | `Syntax OK` | `Syntax OK` |
| No credential, valid request arguments | exit `77` | exit `77` |
| State/output files after no-credential request | `0` | `0` |
| Legacy singleton fixture | 147 old timestamps ignored | old singleton points ignored |
| Pinned synthetic credential status | `credential_matches_state=true` | `credential_matches_state=true` |
| Second synthetic credential status | `credential_matches_state=false` | `credential_matches_state=false` |
| Second credential request | exit `77`, no output | exit `77`, no output |
| Shared controls visible | 4 slots, 60/min global, 6/min worker | same |

The pinned fixture's authenticated REST status reported only its one current
request rather than the 147 legacy timestamps. Its GraphQL status reported the
three fixture points under `recent_graphql_reserved_or_actual_points`. A second
synthetic credential could inspect status but could not perform a request or
alter the pinned scope.

Static inspection additionally verified:

- REST requires matching `credential_fingerprint` metadata before sending an
  ETag or accepting 304 body reuse;
- GraphQL includes the fingerprint inside its `input_sha` cache identity;
- `Retry-After` updates the global cross-protocol cooldown;
- response reset epochs update only when not older than stored state;
- each GraphQL reservation has an ID and actual cost replaces the estimate for
  that attempt;
- retry underestimation is OR-accumulated across attempts.

## Approved live smoke record

The final wrappers were run outside the sandbox so the configured macOS
credential helper could be read. Wrapper output was retained only as the
following non-secret fields:

| Protocol | HTTP | Cache | Auth source | Limit | Cost | Underestimated |
|---|---:|---|---|---:|---:|---|
| REST `/rate_limit` | 200 | false | `git-credential` | 5,000/hour | N/A | N/A |
| GraphQL repository/rate query | 200 | false | `git-credential` | 5,000 points/hour | 1 | false |

Final status readback reported:

- `authenticated=true`;
- `credential_matches_state=true`;
- `authenticated_primary_state_shared=true`;
- `credential_cache_isolation=true`;
- REST observed limit 5,000;
- GraphQL observed limit 5,000;
- no active primary or global cooldown.

The final REST meta, GraphQL meta and shared state files were all mode 0600.
Only field names—not the fingerprint value—were recorded in the verification
transcript. The GraphQL meta contains estimate 1, actual cost 1, one attempt and
`cost_underestimated=false`.

Same-credential cache smoke checks also passed: the repeated GraphQL query
returned `cached=true`, while a public repository REST request returned 200 and
then 304 with cached-body reuse. The pinned synthetic second credential exits 77
before either cache path, so it cannot receive the first credential's body.

## GraphQL cache-success integrity correction

Observed at: `2026-08-24T04:07:43Z`

Batch 008 exposed a second cache defect: a large GraphQL query returned HTTP 502
with an HTML body, but the original sidecar recorded only input identity and age.
An identical invocation therefore returned `status=200,cached=true` without a
network request. The failed body was excluded from research evidence.

GraphQL sidecars now record `http_status`, `graphql_errors`, and `successful`.
A cache hit requires all of:

- matching query/variables/credential input SHA;
- age within the cache window;
- `successful=true`;
- `http_status=200`;
- `graphql_errors=false`.

Failure bodies remain mode-0600 diagnostic artifacts but are never returned as
cached success. Re-running the frozen 502 entry after the patch issued three real
attempts and rewrote its sidecar as `http_status=502`, `successful=false` and
three null-cost attempts. A separate small query returned 200/cost 1 with
`successful=true`; only its second invocation returned `cached=true`.

One pre-final live smoke exposed a Ruby block-local `actual_cost` scope error
after the successful response. It was corrected by initializing the value before
the retry loop, then the final smoke passed. The failed pre-final run is not used
as completion evidence.

## Operational rule

This queue state directory is bound to the current Keychain credential. A future
credential rotation must use a new state directory or an explicit reviewed state
transition; it must not silently reuse the existing directory. Sandboxed workers
that cannot read Keychain must preserve an API gap or request approved queue
execution outside the sandbox. They must never fall back to unauthenticated API
traffic or receive the raw token.
