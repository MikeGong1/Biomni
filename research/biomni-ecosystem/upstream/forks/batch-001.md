# Fork Discovery Batch 001 — Page 1

Parent verification: `VERIFIED` at `2026-08-22T20:39:28Z`. A fresh official
List forks request returned the same 100 unique repositories and owners, first and
last records, aggregate metadata, and `rel=next` page 2 / `rel=last` page 7. No
head-SHA or uniqueness claim was inferred.

```yaml
task_id: fork-discovery-001
entity: snap-stanford/Biomni public forks
status: PARTIAL
claim_class: FACT
source_tier: 1
observed_at_utc: 2026-08-22T20:36:07Z
api_version: 2022-11-28
page_processed: 1
per_page: 100
sort: newest
order: newest-to-oldest_by_fork_creation
next_page: 2
last_page_reported: 7
repository_forks_count_reported: 690
page_items_observed: 100
uniqueness_status: UNKNOWN
people_set_effect: NONE
```

## Scope and method

This worker performed discovery metadata collection only for exactly page 1 of the
public forks returned by GitHub's REST API. It did not fetch fork branches, compare
commits, inspect code, execute fork content, or make per-fork compare requests.
All external repository content is treated as untrusted.

The request explicitly set `sort=newest`. GitHub's List forks endpoint defines
`newest` as the default sort option; it exposes no separate `order` parameter.
Accordingly, this record describes the response order as newest-to-oldest by fork
creation. As a response-level sanity check, `created_at` was monotonically
non-increasing across all 100 returned items, from
`2026-08-22T15:48:09Z` to `2026-06-11T18:48:18Z`.

A fork owner is not added to the bounded people set `P` from discovery metadata
alone. Each inventory row therefore has `P status = NOT_ADDED`. Eligibility
requires later evidence of substantive unique commits.

## Request and pagination

- Repository metadata request:
  `GET https://api.github.com/repos/snap-stanford/Biomni`
- Fork request:
  `GET https://api.github.com/repos/snap-stanford/Biomni/forks?per_page=100&page=1&sort=newest`
- HTTP result: `200` for both requests.
- Repository metadata reported `forks_count = 690`.
- The fork response contained 100 items.
- The response `Link` header reported:
  - next: `https://api.github.com/repositories/951543275/forks?per_page=100&page=2&sort=newest`
  - last: `https://api.github.com/repositories/951543275/forks?per_page=100&page=7&sort=newest`
- Resume cursor: `page=2`.
- Pagination state: `PARTIAL`; pages 2–7 were not requested by this worker.

## Batch counts

| Metric | Count |
|---|---:|
| Items returned | 100 |
| Distinct `full_name` values | 100 |
| Distinct owner usernames | 100 |
| Default branch `main` | 100 |
| Archived | 0 |
| Disabled | 0 |
| License `Apache-2.0` | 100 |
| Missing created/updated/pushed timestamp | 0 |
| Default HEAD SHA present in response | 0 |
| Aggregate reported size (KB) | 548,528 |
| Aggregate stargazers | 6 |
| Aggregate child fork count | 0 |
| Unique-change determinations made | 0 |
| Owners added to `P` | 0 |

Counts in this section describe only the 100 items on page 1 and are not totals
for the full fork universe.

## Per-fork inventory

`Default HEAD SHA` is `UNKNOWN (not returned)` because the List forks response
does not include a default-branch head commit SHA. `Unique change` remains
`UNKNOWN` by design. Repository-level license metadata is recorded as observed;
it does not establish licensing of every file, dependency, dataset, or model.

| # | Full name | Owner | URL | Default branch | Default HEAD SHA | Created UTC | Updated UTC | Pushed UTC | Archived | Disabled | License | Size KB | Stars | Child forks | Unique change | P status |
|---:|---|---|---|---|---|---|---|---|---:|---:|---|---:|---:|---:|---|---|
| 1 | kdh4win4/Biomni | kdh4win4 | https://github.com/kdh4win4/Biomni | main | UNKNOWN (not returned) | 2026-08-22T15:48:09Z | 2026-08-22T15:48:09Z | 2026-08-17T19:17:40Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 2 | MikeGong1/Biomni | MikeGong1 | https://github.com/MikeGong1/Biomni | main | UNKNOWN (not returned) | 2026-08-22T03:04:08Z | 2026-08-22T03:04:09Z | 2026-08-22T20:32:57Z | false | false | Apache-2.0 | 5494 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 3 | alina-2024/Biomni | alina-2024 | https://github.com/alina-2024/Biomni | main | UNKNOWN (not returned) | 2026-08-22T01:48:20Z | 2026-08-22T01:48:20Z | 2026-08-17T19:17:40Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 4 | gungwang/Biomni | gungwang | https://github.com/gungwang/Biomni | main | UNKNOWN (not returned) | 2026-08-21T20:23:25Z | 2026-08-21T20:23:26Z | 2026-08-17T19:17:40Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 5 | vectorpikachu/Biomni | vectorpikachu | https://github.com/vectorpikachu/Biomni | main | UNKNOWN (not returned) | 2026-08-21T12:44:31Z | 2026-08-21T12:44:31Z | 2026-08-17T19:17:40Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 6 | xero-dotcom/Biomni | xero-dotcom | https://github.com/xero-dotcom/Biomni | main | UNKNOWN (not returned) | 2026-08-21T08:55:52Z | 2026-08-21T08:55:52Z | 2026-08-17T19:17:40Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 7 | Cell-Tool/Biomni-LSA-OS | Cell-Tool | https://github.com/Cell-Tool/Biomni-LSA-OS | main | UNKNOWN (not returned) | 2026-08-20T12:30:35Z | 2026-08-20T12:30:35Z | 2026-08-17T19:17:40Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 8 | palimisis/Biomni | palimisis | https://github.com/palimisis/Biomni | main | UNKNOWN (not returned) | 2026-08-20T08:03:30Z | 2026-08-21T22:03:46Z | 2026-08-21T22:03:28Z | false | false | Apache-2.0 | 5417 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 9 | DotWasi/Biomni | DotWasi | https://github.com/DotWasi/Biomni | main | UNKNOWN (not returned) | 2026-08-20T05:08:54Z | 2026-08-20T05:08:54Z | 2026-08-17T19:17:40Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 10 | QING1105/Biomni | QING1105 | https://github.com/QING1105/Biomni | main | UNKNOWN (not returned) | 2026-08-20T02:59:46Z | 2026-08-20T02:59:46Z | 2026-08-21T17:05:18Z | false | false | Apache-2.0 | 5626 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 11 | tonesky/Biomni | tonesky | https://github.com/tonesky/Biomni | main | UNKNOWN (not returned) | 2026-08-20T01:56:18Z | 2026-08-20T01:56:18Z | 2026-08-17T19:17:40Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 12 | reacher-z/Biomni | reacher-z | https://github.com/reacher-z/Biomni | main | UNKNOWN (not returned) | 2026-08-18T14:15:10Z | 2026-08-18T14:15:10Z | 2026-08-18T15:58:34Z | false | false | Apache-2.0 | 5479 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 13 | Irishaze/Biomni | Irishaze | https://github.com/Irishaze/Biomni | main | UNKNOWN (not returned) | 2026-08-18T12:30:20Z | 2026-08-18T12:30:20Z | 2026-08-18T12:46:08Z | false | false | Apache-2.0 | 5458 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 14 | DawnyWu/Biomni | DawnyWu | https://github.com/DawnyWu/Biomni | main | UNKNOWN (not returned) | 2026-08-17T04:03:41Z | 2026-08-17T04:03:41Z | 2026-08-18T15:24:35Z | false | false | Apache-2.0 | 5605 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 15 | mohsin-shaikh/Biomni | mohsin-shaikh | https://github.com/mohsin-shaikh/Biomni | main | UNKNOWN (not returned) | 2026-08-16T05:56:45Z | 2026-08-16T05:56:45Z | 2026-08-10T18:56:17Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 16 | Mr-Milk/Biomni | Mr-Milk | https://github.com/Mr-Milk/Biomni | main | UNKNOWN (not returned) | 2026-08-15T15:58:49Z | 2026-08-15T15:58:49Z | 2026-08-15T15:58:50Z | false | false | Apache-2.0 | 5443 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 17 | 0xYeah/Biomni | 0xYeah | https://github.com/0xYeah/Biomni | main | UNKNOWN (not returned) | 2026-08-14T07:39:05Z | 2026-08-14T07:39:05Z | 2026-08-10T18:56:17Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 18 | PayFv/Biomni | PayFv | https://github.com/PayFv/Biomni | main | UNKNOWN (not returned) | 2026-08-13T07:50:15Z | 2026-08-20T03:12:10Z | 2026-08-20T03:11:47Z | false | false | Apache-2.0 | 5428 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 19 | kekropian/Biomni | kekropian | https://github.com/kekropian/Biomni | main | UNKNOWN (not returned) | 2026-08-13T00:59:57Z | 2026-08-13T00:59:57Z | 2026-08-10T18:56:17Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 20 | competition-W/Biomni | competition-W | https://github.com/competition-W/Biomni | main | UNKNOWN (not returned) | 2026-08-12T01:39:43Z | 2026-08-12T01:39:43Z | 2026-08-10T18:56:17Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 21 | emmm114/Biomni | emmm114 | https://github.com/emmm114/Biomni | main | UNKNOWN (not returned) | 2026-08-07T10:02:06Z | 2026-08-07T10:02:06Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 22 | febright2025/Biomni | febright2025 | https://github.com/febright2025/Biomni | main | UNKNOWN (not returned) | 2026-08-07T04:09:49Z | 2026-08-07T04:09:49Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 23 | fzxz000/Biomni | fzxz000 | https://github.com/fzxz000/Biomni | main | UNKNOWN (not returned) | 2026-08-06T07:26:25Z | 2026-08-06T07:26:25Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 24 | jianjingkuang/Biomni | jianjingkuang | https://github.com/jianjingkuang/Biomni | main | UNKNOWN (not returned) | 2026-08-05T14:41:07Z | 2026-08-05T14:41:07Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 25 | chenwgm-eng/Biomni | chenwgm-eng | https://github.com/chenwgm-eng/Biomni | main | UNKNOWN (not returned) | 2026-08-05T13:01:24Z | 2026-08-10T06:43:26Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 1 | 0 | UNKNOWN | NOT_ADDED |
| 26 | xigyou/Biomni | xigyou | https://github.com/xigyou/Biomni | main | UNKNOWN (not returned) | 2026-08-05T09:07:08Z | 2026-08-05T09:07:08Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 27 | yy7204/Biomni | yy7204 | https://github.com/yy7204/Biomni | main | UNKNOWN (not returned) | 2026-08-05T01:50:27Z | 2026-08-05T01:50:27Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 28 | Ekkoone/Biomni | Ekkoone | https://github.com/Ekkoone/Biomni | main | UNKNOWN (not returned) | 2026-08-05T01:06:25Z | 2026-08-05T01:07:01Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 1 | 0 | UNKNOWN | NOT_ADDED |
| 29 | BiotechPrivate/Biomni | BiotechPrivate | https://github.com/BiotechPrivate/Biomni | main | UNKNOWN (not returned) | 2026-08-04T17:31:37Z | 2026-08-04T17:31:37Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 30 | NaveedUrRehman787/Biomni | NaveedUrRehman787 | https://github.com/NaveedUrRehman787/Biomni | main | UNKNOWN (not returned) | 2026-08-04T06:03:17Z | 2026-08-04T06:03:18Z | 2026-08-04T06:04:03Z | false | false | Apache-2.0 | 5439 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 31 | rvilvendhan/Biomni | rvilvendhan | https://github.com/rvilvendhan/Biomni | main | UNKNOWN (not returned) | 2026-08-03T21:51:40Z | 2026-08-03T21:51:40Z | 2026-08-03T18:51:48Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 32 | KalinNonchev/Biomni | KalinNonchev | https://github.com/KalinNonchev/Biomni | main | UNKNOWN (not returned) | 2026-08-03T17:36:23Z | 2026-08-03T17:36:24Z | 2026-08-03T18:28:20Z | false | false | Apache-2.0 | 5451 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 33 | jananthan30/Biomni | jananthan30 | https://github.com/jananthan30/Biomni | main | UNKNOWN (not returned) | 2026-08-03T04:15:57Z | 2026-08-03T04:15:57Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 34 | hapi-developer/Biomni | hapi-developer | https://github.com/hapi-developer/Biomni | main | UNKNOWN (not returned) | 2026-08-03T02:27:18Z | 2026-08-03T02:27:18Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 35 | CancerTiN/Biomni | CancerTiN | https://github.com/CancerTiN/Biomni | main | UNKNOWN (not returned) | 2026-08-02T13:42:33Z | 2026-08-02T13:42:34Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 36 | alexandreumatize/Biomni | alexandreumatize | https://github.com/alexandreumatize/Biomni | main | UNKNOWN (not returned) | 2026-08-01T23:05:18Z | 2026-08-01T23:05:18Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 37 | explorerwjy/Biomni | explorerwjy | https://github.com/explorerwjy/Biomni | main | UNKNOWN (not returned) | 2026-08-01T07:43:08Z | 2026-08-01T07:43:08Z | 2026-08-01T07:47:04Z | false | false | Apache-2.0 | 5460 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 38 | arrowifjn/Biomni | arrowifjn | https://github.com/arrowifjn/Biomni | main | UNKNOWN (not returned) | 2026-07-31T13:46:28Z | 2026-07-31T13:46:28Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 39 | zhangqif/Biomni | zhangqif | https://github.com/zhangqif/Biomni | main | UNKNOWN (not returned) | 2026-07-31T08:46:54Z | 2026-07-31T08:46:54Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 40 | super-818/Biomni_learn | super-818 | https://github.com/super-818/Biomni_learn | main | UNKNOWN (not returned) | 2026-07-31T02:51:30Z | 2026-07-31T02:51:30Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 41 | little2b/Biomni | little2b | https://github.com/little2b/Biomni | main | UNKNOWN (not returned) | 2026-07-30T01:58:04Z | 2026-07-30T02:09:12Z | 2026-07-30T02:09:08Z | false | false | Apache-2.0 | 5539 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 42 | vjbaskar/Biomni | vjbaskar | https://github.com/vjbaskar/Biomni | main | UNKNOWN (not returned) | 2026-07-29T09:30:30Z | 2026-07-29T09:30:30Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 43 | xtalgalaxy/Biomni | xtalgalaxy | https://github.com/xtalgalaxy/Biomni | main | UNKNOWN (not returned) | 2026-07-28T14:45:40Z | 2026-07-28T14:45:40Z | 2026-07-27T18:40:30Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 44 | sunshinezhihuo/Biomni | sunshinezhihuo | https://github.com/sunshinezhihuo/Biomni | main | UNKNOWN (not returned) | 2026-07-27T07:54:58Z | 2026-07-27T07:54:59Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 45 | szz00712/Biomni_s | szz00712 | https://github.com/szz00712/Biomni_s | main | UNKNOWN (not returned) | 2026-07-27T07:46:50Z | 2026-07-27T07:46:50Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 46 | 1667857557/Biomni_feng | 1667857557 | https://github.com/1667857557/Biomni_feng | main | UNKNOWN (not returned) | 2026-07-27T03:00:54Z | 2026-08-22T09:56:45Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 47 | zhansh-2025/Biomni | zhansh-2025 | https://github.com/zhansh-2025/Biomni | main | UNKNOWN (not returned) | 2026-07-27T00:09:02Z | 2026-07-27T00:09:02Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 48 | qym7/Biomni | qym7 | https://github.com/qym7/Biomni | main | UNKNOWN (not returned) | 2026-07-26T20:19:55Z | 2026-07-26T20:19:55Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 49 | yepingzhao/Biomni | yepingzhao | https://github.com/yepingzhao/Biomni | main | UNKNOWN (not returned) | 2026-07-26T11:07:34Z | 2026-07-26T11:07:34Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 50 | cerebral-work/biomni | cerebral-work | https://github.com/cerebral-work/biomni | main | UNKNOWN (not returned) | 2026-07-23T18:11:13Z | 2026-07-24T18:41:46Z | 2026-07-24T09:15:16Z | false | false | Apache-2.0 | 5417 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 51 | dragonlhy/Biomni | dragonlhy | https://github.com/dragonlhy/Biomni | main | UNKNOWN (not returned) | 2026-07-23T09:11:05Z | 2026-07-23T09:11:05Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 52 | dming1024/Biomni | dming1024 | https://github.com/dming1024/Biomni | main | UNKNOWN (not returned) | 2026-07-22T01:42:33Z | 2026-07-22T01:42:33Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 53 | jissen706/Biomni | jissen706 | https://github.com/jissen706/Biomni | main | UNKNOWN (not returned) | 2026-07-20T20:19:38Z | 2026-07-20T20:19:38Z | 2026-07-20T20:25:12Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 54 | awmuhtaseb/Biomni | awmuhtaseb | https://github.com/awmuhtaseb/Biomni | main | UNKNOWN (not returned) | 2026-07-20T19:27:33Z | 2026-07-20T19:27:42Z | 2026-07-20T18:45:39Z | false | false | Apache-2.0 | 5441 | 1 | 0 | UNKNOWN | NOT_ADDED |
| 55 | hzhou98/Biomni | hzhou98 | https://github.com/hzhou98/Biomni | main | UNKNOWN (not returned) | 2026-07-20T16:20:47Z | 2026-07-20T16:20:47Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 56 | JimmyXtesla/Biomni | JimmyXtesla | https://github.com/JimmyXtesla/Biomni | main | UNKNOWN (not returned) | 2026-07-20T14:32:44Z | 2026-07-20T14:32:44Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 57 | vitumsowoya/Biomni | vitumsowoya | https://github.com/vitumsowoya/Biomni | main | UNKNOWN (not returned) | 2026-07-20T14:32:42Z | 2026-07-20T14:32:42Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 58 | YiXiHu4ng/Biomni | YiXiHu4ng | https://github.com/YiXiHu4ng/Biomni | main | UNKNOWN (not returned) | 2026-07-20T08:09:37Z | 2026-07-20T08:09:37Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 59 | jhuanglabAI/Biomni | jhuanglabAI | https://github.com/jhuanglabAI/Biomni | main | UNKNOWN (not returned) | 2026-07-19T13:10:00Z | 2026-07-19T13:10:01Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 60 | danhively/biomni | danhively | https://github.com/danhively/biomni | main | UNKNOWN (not returned) | 2026-07-19T04:38:25Z | 2026-07-19T04:38:25Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 61 | leihe2021/Biomni_web | leihe2021 | https://github.com/leihe2021/Biomni_web | main | UNKNOWN (not returned) | 2026-07-19T01:03:33Z | 2026-07-19T01:03:33Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 62 | airbj31/Biomni | airbj31 | https://github.com/airbj31/Biomni | main | UNKNOWN (not returned) | 2026-07-18T00:02:32Z | 2026-07-18T00:02:32Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 63 | ali-saei/Biomni | ali-saei | https://github.com/ali-saei/Biomni | main | UNKNOWN (not returned) | 2026-07-17T08:07:47Z | 2026-07-17T08:07:47Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 64 | Unity-Educational-Formation/Biomni | Unity-Educational-Formation | https://github.com/Unity-Educational-Formation/Biomni | main | UNKNOWN (not returned) | 2026-07-17T00:25:39Z | 2026-07-17T00:25:40Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 65 | yilmaztnr13-collab/Biomni | yilmaztnr13-collab | https://github.com/yilmaztnr13-collab/Biomni | main | UNKNOWN (not returned) | 2026-07-16T13:20:17Z | 2026-07-16T13:20:27Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 1 | 0 | UNKNOWN | NOT_ADDED |
| 66 | moonriver2002/Biomni | moonriver2002 | https://github.com/moonriver2002/Biomni | main | UNKNOWN (not returned) | 2026-07-15T16:11:53Z | 2026-07-15T16:11:53Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 67 | Dandanzzi/Biomni | Dandanzzi | https://github.com/Dandanzzi/Biomni | main | UNKNOWN (not returned) | 2026-07-15T09:20:06Z | 2026-08-13T16:52:31Z | 2026-08-13T16:51:59Z | false | false | Apache-2.0 | 6942 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 68 | yg-326/Biomni1 | yg-326 | https://github.com/yg-326/Biomni1 | main | UNKNOWN (not returned) | 2026-07-15T07:46:10Z | 2026-07-15T07:46:10Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 69 | AmrR101/Biomni | AmrR101 | https://github.com/AmrR101/Biomni | main | UNKNOWN (not returned) | 2026-07-14T19:51:39Z | 2026-07-15T15:45:09Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 1 | 0 | UNKNOWN | NOT_ADDED |
| 70 | rotojp/Biomni | rotojp | https://github.com/rotojp/Biomni | main | UNKNOWN (not returned) | 2026-07-14T14:49:20Z | 2026-07-14T14:50:10Z | 2026-07-14T15:48:43Z | false | false | Apache-2.0 | 5464 | 1 | 0 | UNKNOWN | NOT_ADDED |
| 71 | zhaolm2021/Biomni | zhaolm2021 | https://github.com/zhaolm2021/Biomni | main | UNKNOWN (not returned) | 2026-07-14T12:00:56Z | 2026-07-14T12:00:57Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 72 | ruiafd/Biomni | ruiafd | https://github.com/ruiafd/Biomni | main | UNKNOWN (not returned) | 2026-07-14T07:40:49Z | 2026-07-14T07:40:49Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 73 | stjordanis/Biomni | stjordanis | https://github.com/stjordanis/Biomni | main | UNKNOWN (not returned) | 2026-07-13T22:52:22Z | 2026-07-13T22:52:22Z | 2026-07-13T19:14:42Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 74 | mirrorhealth-dev/Biomni | mirrorhealth-dev | https://github.com/mirrorhealth-dev/Biomni | main | UNKNOWN (not returned) | 2026-07-13T17:29:55Z | 2026-07-13T17:29:55Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 75 | smengmeng30-dev/Biomni | smengmeng30-dev | https://github.com/smengmeng30-dev/Biomni | main | UNKNOWN (not returned) | 2026-07-13T08:01:23Z | 2026-07-13T08:01:23Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 76 | Trismagestus/Biomni | Trismagestus | https://github.com/Trismagestus/Biomni | main | UNKNOWN (not returned) | 2026-07-12T22:50:59Z | 2026-07-12T22:51:00Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 77 | Yijun-Cui/Biomni | Yijun-Cui | https://github.com/Yijun-Cui/Biomni | main | UNKNOWN (not returned) | 2026-07-12T10:24:08Z | 2026-07-12T10:24:08Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 78 | jeevesh415/Biomni | jeevesh415 | https://github.com/jeevesh415/Biomni | main | UNKNOWN (not returned) | 2026-07-12T02:32:10Z | 2026-07-12T02:32:10Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 79 | de-grave/Biomni | de-grave | https://github.com/de-grave/Biomni | main | UNKNOWN (not returned) | 2026-07-11T06:42:59Z | 2026-07-11T06:42:59Z | 2026-07-11T06:55:45Z | false | false | Apache-2.0 | 5471 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 80 | wangdi2016/Biomni | wangdi2016 | https://github.com/wangdi2016/Biomni | main | UNKNOWN (not returned) | 2026-07-11T03:16:21Z | 2026-07-11T03:16:21Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 81 | jyryu3161/Biomni | jyryu3161 | https://github.com/jyryu3161/Biomni | main | UNKNOWN (not returned) | 2026-07-11T00:03:20Z | 2026-07-11T00:03:21Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 82 | Puddin1066/Biomni | Puddin1066 | https://github.com/Puddin1066/Biomni | main | UNKNOWN (not returned) | 2026-07-10T11:38:43Z | 2026-07-10T11:38:43Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 83 | richWmc/Biomni | richWmc | https://github.com/richWmc/Biomni | main | UNKNOWN (not returned) | 2026-07-10T09:42:59Z | 2026-07-10T09:42:59Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 84 | caramelcyy/Biomni | caramelcyy | https://github.com/caramelcyy/Biomni | main | UNKNOWN (not returned) | 2026-07-10T07:48:53Z | 2026-07-10T07:48:53Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 85 | dabulseco/Biomni | dabulseco | https://github.com/dabulseco/Biomni | main | UNKNOWN (not returned) | 2026-07-10T06:55:42Z | 2026-07-19T11:35:52Z | 2026-07-19T11:35:44Z | false | false | Apache-2.0 | 7704 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 86 | hwl26/Biomni | hwl26 | https://github.com/hwl26/Biomni | main | UNKNOWN (not returned) | 2026-07-10T06:11:22Z | 2026-07-10T06:11:23Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 87 | philloidin/Biomni | philloidin | https://github.com/philloidin/Biomni | main | UNKNOWN (not returned) | 2026-07-09T05:20:27Z | 2026-07-09T05:20:28Z | 2026-07-06T18:47:14Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 88 | lokinell/Biomni | lokinell | https://github.com/lokinell/Biomni | main | UNKNOWN (not returned) | 2026-07-06T02:47:31Z | 2026-07-06T02:47:31Z | 2026-06-29T18:39:40Z | false | false | Apache-2.0 | 5440 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 89 | Norton-xia-hub/Biomni | Norton-xia-hub | https://github.com/Norton-xia-hub/Biomni | main | UNKNOWN (not returned) | 2026-07-05T16:06:31Z | 2026-07-05T16:06:32Z | 2026-06-29T18:39:40Z | false | false | Apache-2.0 | 5440 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 90 | mrsirquanzo/Biomni | mrsirquanzo | https://github.com/mrsirquanzo/Biomni | main | UNKNOWN (not returned) | 2026-07-03T01:25:12Z | 2026-07-03T01:25:12Z | 2026-06-29T18:39:40Z | false | false | Apache-2.0 | 5440 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 91 | Alirezahayatimedtech/Biomni | Alirezahayatimedtech | https://github.com/Alirezahayatimedtech/Biomni | main | UNKNOWN (not returned) | 2026-06-26T17:58:24Z | 2026-06-26T17:58:24Z | 2026-06-22T18:45:03Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 92 | termasz/Biomni | termasz | https://github.com/termasz/Biomni | main | UNKNOWN (not returned) | 2026-06-25T17:34:50Z | 2026-06-25T17:34:50Z | 2026-06-22T18:45:03Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 93 | hhg36355-hue/Biomni | hhg36355-hue | https://github.com/hhg36355-hue/Biomni | main | UNKNOWN (not returned) | 2026-06-25T15:09:31Z | 2026-06-25T15:09:31Z | 2026-06-22T18:45:03Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 94 | kewserseid/Biomni | kewserseid | https://github.com/kewserseid/Biomni | main | UNKNOWN (not returned) | 2026-06-22T11:45:34Z | 2026-06-22T11:45:34Z | 2026-06-22T11:51:12Z | false | false | Apache-2.0 | 5517 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 95 | zhikangliu068-lab/Biomni | zhikangliu068-lab | https://github.com/zhikangliu068-lab/Biomni | main | UNKNOWN (not returned) | 2026-06-22T06:47:57Z | 2026-06-22T06:47:57Z | 2026-06-15T18:43:05Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 96 | look4pritam/Biomni | look4pritam | https://github.com/look4pritam/Biomni | main | UNKNOWN (not returned) | 2026-06-22T04:38:41Z | 2026-06-22T04:38:41Z | 2026-06-15T18:43:05Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 97 | ourkofe/Biomni | ourkofe | https://github.com/ourkofe/Biomni | main | UNKNOWN (not returned) | 2026-06-19T06:26:18Z | 2026-06-19T06:26:18Z | 2026-06-15T18:43:05Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 98 | sjiang-lilly/Biomni | sjiang-lilly | https://github.com/sjiang-lilly/Biomni | main | UNKNOWN (not returned) | 2026-06-17T02:02:12Z | 2026-06-17T02:02:12Z | 2026-06-15T18:43:05Z | false | false | Apache-2.0 | 5441 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 99 | Nigmat-future/Biomni | Nigmat-future | https://github.com/Nigmat-future/Biomni | main | UNKNOWN (not returned) | 2026-06-12T08:17:00Z | 2026-06-12T08:17:00Z | 2026-06-12T08:29:54Z | false | false | Apache-2.0 | 5455 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 100 | starboy-3/Biomni | starboy-3 | https://github.com/starboy-3/Biomni | main | UNKNOWN (not returned) | 2026-06-11T18:48:18Z | 2026-06-11T18:48:18Z | 2026-06-11T18:49:22Z | false | false | Apache-2.0 | 5442 | 0 | 0 | UNKNOWN | NOT_ADDED |

## Evidence

1. GitHub repository metadata API (Tier 1, observed
   `2026-08-22T20:36:05Z`):
   https://api.github.com/repos/snap-stanford/Biomni
2. GitHub List forks API page 1 (Tier 1, observed
   `2026-08-22T20:36:07Z`):
   https://api.github.com/repos/snap-stanford/Biomni/forks?per_page=100&page=1&sort=newest
3. Official GitHub REST documentation for List forks and its `sort` parameter
   (Tier 1):
   https://docs.github.com/en/rest/repos/forks?apiVersion=2022-11-28#list-forks
4. Pagination evidence is the page-1 HTTP `Link` header quoted above. It reports
   pages 2 and 7 through `rel="next"` and `rel="last"`.

## Uncertainty and limitations

- This batch is not a complete public-fork inventory; pages 2–7 remain unprocessed.
- GitHub counts and pagination are time-dependent. `forks_count = 690` and the
  seven-page Link header are observations at the stated timestamps, not immutable
  totals.
- No branch list or commit comparison was performed. Ahead/behind state,
  substantive uniqueness, related PRs, duplication, ancestry, and merge status are
  all `UNKNOWN`.
- `pushed_at` is repository metadata and does not itself prove a unique fork
  change; it may reflect inherited or synchronized activity.
- Default-branch head SHAs were absent from this response and remain `UNKNOWN`.
- Public APIs cannot expose private forks, deleted forks, or otherwise
  non-public material.
- Repository license metadata alone does not resolve component-level licensing.

## Next action

Resume bounded discovery at:

`GET https://api.github.com/repos/snap-stanford/Biomni/forks?per_page=100&page=2&sort=newest`

Preserve the same API version, sort, inventory fields, evidence policy, and
`UNKNOWN` uniqueness status. Only after the full public inventory is collected
should a separate screening phase make bounded branch/commit comparisons. Add a
fork owner to `P` only if substantive unique commits are established.
