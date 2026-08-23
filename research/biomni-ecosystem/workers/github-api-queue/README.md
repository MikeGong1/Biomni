# Shared GitHub API queue

This research-only wrapper is the single allowed GitHub REST path for parallel
external-repository workers.

Limits:

- 4 concurrent in-flight requests;
- 60 requests/minute globally;
- 6 requests/minute per worker;
- fail-closed REST and GraphQL requests when no authenticated credential is
  available;
- one authenticated GitHub credential pinned per queue state directory; a
  different credential fails closed with exit 77;
- one conservative REST bucket and one GraphQL point bucket shared by all workers
  using that pinned credential;
- response caches isolated by the full SHA-256 fingerprint of the active
  credential, without storing or printing the credential;
- 80% primary-limit headroom if an authenticated credential unexpectedly reports
  a 60/hour limit;
- `Retry-After` and primary reset cooldowns are shared through a locked state
  file.

The wrapper reads a token only from `GITHUB_TOKEN`, `GH_TOKEN`, or the Git
credential helper. It never writes or prints the token. Queue state contains
timestamps, GitHub rate-limit counters, and the pinned credential's full
SHA-256 fingerprint under `/private/tmp/biomni-github-api-queue` by default. The
fingerprint cannot authenticate a request; state, response bodies and metadata
are written mode 0600.

On macOS the credential helper may be unavailable inside the managed sandbox.
Workers must then stop on exit 77 or run the wrapper through the approved
escalated/root path; they must never fall back to unauthenticated GitHub API
traffic or copy the credential into queue state. Changing credentials requires a
new queue state directory; do not reuse a state directory across principals.

Example:

```text
ruby research/biomni-ecosystem/workers/github-api-queue/gh_api_queue.rb \
  order13 https://api.github.com/repos/OWNER/REPO /private/tmp/order13/repo.json
```

Git-over-SSH clone/fetch, local DAG work and static inspection do not use this
REST queue. Workers must not call `curl https://api.github.com/...` directly.

Batch inventory should use `gh_graphql_queue.rb`. Its input is a JSON file with
`query`, `variables`, and a conservative `estimated_cost`. Queries must request a
top-level `rateLimit { limit cost remaining resetAt }`; every `first:` is capped
at 100. GraphQL shares the same four in-flight locks and request/minute limits,
while reserving 20% of the separate 5,000-point GraphQL budget.

```text
ruby research/biomni-ecosystem/workers/github-api-queue/gh_graphql_queue.rb \
  shard-a /private/tmp/shard-a/query.json /private/tmp/shard-a/page-001.json
```

REST responses persist credential-bound `ETag`/`Last-Modified` sidecars and reuse
cached bodies on 304 only for the same credential fingerprint. GraphQL responses
use a credential-bound query+variables SHA-256 cache for five minutes.
Cursor variables and one stable output path per page provide incremental resume.

At 60/minute the global ceiling is 3,600/hour. Ten workers therefore average at
most 360/hour each (one request per ten seconds), not 400/hour each. The 4,000/hour
arithmetic from an 80% authenticated primary allowance remains above the explicit
3,600/hour global ceiling.
