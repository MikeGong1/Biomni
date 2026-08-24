# Fork Discovery Batch 003 — Page 3

Parent verification: `VERIFIED` at `2026-08-22T20:58:55Z`. A fresh official
page-3 request returned the same 100 unique repositories, boundaries, aggregates,
and prev=2 / next=4 / last=7 pagination. There is no full-name overlap with the
200 canonical page-1/2 records. Uniqueness remains `UNKNOWN`.

```yaml
task_id: fork-discovery-003
entity: snap-stanford/Biomni public forks
status: PARTIAL
claim_class: FACT
source_tier: 1
observed_at_utc: 2026-08-22T20:47:10Z
api_version: 2022-11-28
page_processed: 3
per_page: 100
sort: newest
order: newest-to-oldest_by_fork_creation
previous_page: 2
next_page: 4
last_page_reported: 7
repository_forks_count_reported: 690
page_items_observed: 100
cumulative_pages_observed: 3
cumulative_items_observed: 300
uniqueness_status: UNKNOWN
people_set_effect: NONE
```

## Scope and method

This worker collected discovery metadata for exactly page 3 of the public forks
returned by GitHub's REST API. It did not fetch branches, compare commits, inspect
or execute fork code, or make per-fork compare requests. External repository
content remains untrusted.

The request explicitly set `sort=newest`; the endpoint has no separate
`order` parameter. The page-3 `created_at` sequence was monotonically
non-increasing across all 100 items, from `2026-03-06T22:51:34Z` to
`2025-12-10T22:15:23Z`.

The 100 page-3 `full_name` values were compared with all 200 distinct names in
the parent-verified canonical files `upstream/forks/batch-001.md` and
`upstream/forks/batch-002.md`; overlap was zero. This is a continuity check
between time-stamped snapshots, not a substitute for exhausting pagination.

Discovery metadata alone does not place a fork owner in the bounded people set
`P`. Every row records `P status = NOT_ADDED`; eligibility requires later
evidence of substantive unique commits.

## Request and pagination

- Repository metadata request:
  `GET https://api.github.com/repos/snap-stanford/Biomni`
- Fork request:
  `GET https://api.github.com/repos/snap-stanford/Biomni/forks?per_page=100&page=3&sort=newest`
- HTTP result: `200` for both requests.
- Repository metadata reported `forks_count = 690`.
- The page-3 response contained 100 items.
- The response `Link` header reported:
  - previous:
    `https://api.github.com/repositories/951543275/forks?per_page=100&page=2&sort=newest`
  - next:
    `https://api.github.com/repositories/951543275/forks?per_page=100&page=4&sort=newest`
  - last:
    `https://api.github.com/repositories/951543275/forks?per_page=100&page=7&sort=newest`
  - first:
    `https://api.github.com/repositories/951543275/forks?per_page=100&page=1&sort=newest`
- Resume cursor: `page=4`.
- Pagination state: `PARTIAL`; pages 4–7 were not requested by this worker.

## Batch counts

| Metric | Count |
|---|---:|
| Items returned on page 3 | 100 |
| Distinct `full_name` values on page 3 | 100 |
| Distinct owner usernames on page 3 | 100 |
| Canonical names checked from pages 1–2 | 200 |
| Overlap with canonical pages 1–2 | 0 |
| Cumulative items observed across pages 1–3 | 300 |
| Default branch `main` | 100 |
| Archived | 0 |
| Disabled | 0 |
| License `Apache-2.0` | 100 |
| Missing created/updated/pushed timestamp | 0 |
| Default HEAD SHA present in response | 0 |
| Aggregate reported size (KB) | 780,670 |
| Aggregate stargazers | 1 |
| Aggregate child fork count | 2 |
| Unique-change determinations made | 0 |
| Owners added to `P` | 0 |

Page-level aggregates describe only page 3. The cumulative item count uses three
observed pages; repository metadata remains the source for the current reported
total of 690 forks.

## Per-fork inventory

Rows 201–300 represent positions in the explicitly newest-sorted paginated
response. `Default HEAD SHA` is `UNKNOWN (not returned)` because the List
forks response does not include a default-branch head commit SHA. `Unique
change` remains `UNKNOWN`. Repository license metadata does not establish
licensing for every file, dependency, dataset, or model.

| # | Full name | Owner | URL | Default branch | Default HEAD SHA | Created UTC | Updated UTC | Pushed UTC | Archived | Disabled | License | Size KB | Stars | Child forks | Unique change | P status |
|---:|---|---|---|---|---|---|---|---|---:|---:|---|---:|---:|---:|---|---|
| 201 | m-muqiao/labmate | m-muqiao | https://github.com/m-muqiao/labmate | main | UNKNOWN (not returned) | 2026-03-06T22:51:34Z | 2026-03-06T22:51:34Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 202 | agutmanstein-scale/Biomni | agutmanstein-scale | https://github.com/agutmanstein-scale/Biomni | main | UNKNOWN (not returned) | 2026-03-06T19:52:37Z | 2026-03-06T19:52:37Z | 2026-03-11T01:44:24Z | false | false | Apache-2.0 | 6141 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 203 | div0-space/Biomni | div0-space | https://github.com/div0-space/Biomni | main | UNKNOWN (not returned) | 2026-03-06T17:25:42Z | 2026-03-06T17:25:42Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 204 | huseyincavusbi/Biomni | huseyincavusbi | https://github.com/huseyincavusbi/Biomni | main | UNKNOWN (not returned) | 2026-03-06T16:11:58Z | 2026-03-06T16:11:59Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 205 | penelopenelope/Biomni | penelopenelope | https://github.com/penelopenelope/Biomni | main | UNKNOWN (not returned) | 2026-03-06T12:02:09Z | 2026-03-06T12:02:09Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 206 | Qanatpharma/Biomni | Qanatpharma | https://github.com/Qanatpharma/Biomni | main | UNKNOWN (not returned) | 2026-03-06T09:14:44Z | 2026-03-06T09:14:44Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 207 | martinBCCDC/Biomni | martinBCCDC | https://github.com/martinBCCDC/Biomni | main | UNKNOWN (not returned) | 2026-03-06T00:59:52Z | 2026-03-06T00:59:53Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 208 | AlaiaS/Biomni | AlaiaS | https://github.com/AlaiaS/Biomni | main | UNKNOWN (not returned) | 2026-03-06T00:44:59Z | 2026-03-06T00:44:59Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 209 | gutendzx/Biomni | gutendzx | https://github.com/gutendzx/Biomni | main | UNKNOWN (not returned) | 2026-03-05T10:28:13Z | 2026-03-09T23:57:47Z | 2026-01-19T19:56:32Z | false | false | Apache-2.0 | 5945 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 210 | sagechant/Biomni | sagechant | https://github.com/sagechant/Biomni | main | UNKNOWN (not returned) | 2026-03-04T16:58:37Z | 2026-03-04T16:58:38Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 211 | nbahti/Biomni | nbahti | https://github.com/nbahti/Biomni | main | UNKNOWN (not returned) | 2026-03-04T14:15:03Z | 2026-03-04T14:15:03Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 212 | noelsomdalen/Biomni_2 | noelsomdalen | https://github.com/noelsomdalen/Biomni_2 | main | UNKNOWN (not returned) | 2026-03-04T11:12:08Z | 2026-03-04T11:12:09Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 213 | animesh/Biomni | animesh | https://github.com/animesh/Biomni | main | UNKNOWN (not returned) | 2026-03-04T08:31:36Z | 2026-03-04T08:31:37Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 214 | robertpark1228/Biomni | robertpark1228 | https://github.com/robertpark1228/Biomni | main | UNKNOWN (not returned) | 2026-03-04T05:39:56Z | 2026-03-04T05:39:56Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 215 | informationsea/Biomni | informationsea | https://github.com/informationsea/Biomni | main | UNKNOWN (not returned) | 2026-03-04T02:20:34Z | 2026-03-04T02:20:34Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 216 | pravalika5/Biomni | pravalika5 | https://github.com/pravalika5/Biomni | main | UNKNOWN (not returned) | 2026-03-03T21:00:05Z | 2026-03-03T21:00:05Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 217 | Jiadalee/Biomni | Jiadalee | https://github.com/Jiadalee/Biomni | main | UNKNOWN (not returned) | 2026-03-03T20:58:47Z | 2026-03-03T20:58:47Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 218 | sunxinti/Biomni | sunxinti | https://github.com/sunxinti/Biomni | main | UNKNOWN (not returned) | 2026-03-03T20:02:15Z | 2026-03-03T20:02:16Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 219 | erima2020/Biomni | erima2020 | https://github.com/erima2020/Biomni | main | UNKNOWN (not returned) | 2026-03-03T19:33:50Z | 2026-03-03T19:33:50Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 220 | AndreRui/biomni | AndreRui | https://github.com/AndreRui/biomni | main | UNKNOWN (not returned) | 2026-03-03T18:08:30Z | 2026-03-03T18:08:30Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 221 | sg3451/Biomni_AI_code | sg3451 | https://github.com/sg3451/Biomni_AI_code | main | UNKNOWN (not returned) | 2026-03-03T15:50:28Z | 2026-03-03T15:50:28Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 222 | lakshmikc/Biomni | lakshmikc | https://github.com/lakshmikc/Biomni | main | UNKNOWN (not returned) | 2026-03-03T13:55:51Z | 2026-03-03T13:55:51Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 223 | Noone-Dash/biomni | Noone-Dash | https://github.com/Noone-Dash/biomni | main | UNKNOWN (not returned) | 2026-03-03T11:29:49Z | 2026-03-03T11:29:49Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 224 | ddunun/Biomni | ddunun | https://github.com/ddunun/Biomni | main | UNKNOWN (not returned) | 2026-03-03T11:29:25Z | 2026-03-03T11:29:26Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 225 | Zhao-Xiaodan/Biomni | Zhao-Xiaodan | https://github.com/Zhao-Xiaodan/Biomni | main | UNKNOWN (not returned) | 2026-03-03T07:24:05Z | 2026-03-03T07:24:06Z | 2026-03-02T18:55:28Z | false | false | Apache-2.0 | 6033 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 226 | DevinDeSilva/Biomni | DevinDeSilva | https://github.com/DevinDeSilva/Biomni | main | UNKNOWN (not returned) | 2026-03-02T22:31:34Z | 2026-05-04T06:56:11Z | 2026-05-04T06:56:03Z | false | false | Apache-2.0 | 5742 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 227 | ghar1821/Biomni | ghar1821 | https://github.com/ghar1821/Biomni | main | UNKNOWN (not returned) | 2026-02-27T04:49:13Z | 2026-02-27T04:49:14Z | 2026-02-23T18:45:57Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 228 | HealthVivo/Biomni | HealthVivo | https://github.com/HealthVivo/Biomni | main | UNKNOWN (not returned) | 2026-02-26T05:58:21Z | 2026-02-26T05:58:21Z | 2026-02-23T18:45:57Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 229 | jxshi/Biomni | jxshi | https://github.com/jxshi/Biomni | main | UNKNOWN (not returned) | 2026-02-26T04:22:05Z | 2026-02-26T04:22:05Z | 2026-02-23T18:45:57Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 230 | 3280069445/Biomni | 3280069445 | https://github.com/3280069445/Biomni | main | UNKNOWN (not returned) | 2026-02-25T01:12:40Z | 2026-02-25T01:12:40Z | 2026-02-23T18:45:57Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 231 | Beifang/Biomni | Beifang | https://github.com/Beifang/Biomni | main | UNKNOWN (not returned) | 2026-02-24T19:48:56Z | 2026-02-24T19:48:56Z | 2026-02-23T18:45:57Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 232 | Charles1DENG/Biomni | Charles1DENG | https://github.com/Charles1DENG/Biomni | main | UNKNOWN (not returned) | 2026-02-24T13:52:37Z | 2026-02-24T13:52:37Z | 2026-02-23T18:45:57Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 233 | randomrisk/Biomni | randomrisk | https://github.com/randomrisk/Biomni | main | UNKNOWN (not returned) | 2026-02-21T06:25:14Z | 2026-02-21T06:25:15Z | 2026-02-16T18:29:21Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 234 | kedarkolluri-tw/Biomni | kedarkolluri-tw | https://github.com/kedarkolluri-tw/Biomni | main | UNKNOWN (not returned) | 2026-02-20T17:46:22Z | 2026-02-20T17:46:22Z | 2026-02-16T18:29:21Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 235 | ProximaMonkey/Biomni | ProximaMonkey | https://github.com/ProximaMonkey/Biomni | main | UNKNOWN (not returned) | 2026-02-20T15:02:11Z | 2026-02-20T15:02:11Z | 2026-02-16T18:29:21Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 236 | ZN-Sellena2000/Biomni | ZN-Sellena2000 | https://github.com/ZN-Sellena2000/Biomni | main | UNKNOWN (not returned) | 2026-02-20T09:06:37Z | 2026-02-20T09:06:45Z | 2026-02-20T09:06:39Z | false | false | Apache-2.0 | 6118 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 237 | stevenWZ/Biomni | stevenWZ | https://github.com/stevenWZ/Biomni | main | UNKNOWN (not returned) | 2026-02-20T03:42:43Z | 2026-02-20T03:42:43Z | 2026-02-16T18:29:21Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 238 | datnoor/Biomni | datnoor | https://github.com/datnoor/Biomni | main | UNKNOWN (not returned) | 2026-02-19T18:40:35Z | 2026-02-19T18:40:35Z | 2026-02-16T18:29:21Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 239 | XxxKrabs/BioMNI | XxxKrabs | https://github.com/XxxKrabs/BioMNI | main | UNKNOWN (not returned) | 2026-02-18T08:39:50Z | 2026-02-25T13:18:05Z | 2026-04-07T08:08:01Z | false | false | Apache-2.0 | 5643 | 1 | 0 | UNKNOWN | NOT_ADDED |
| 240 | larryinx/Biomni | larryinx | https://github.com/larryinx/Biomni | main | UNKNOWN (not returned) | 2026-02-18T05:13:51Z | 2026-02-26T20:32:45Z | 2026-02-26T20:32:34Z | false | false | Apache-2.0 | 6188 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 241 | psknlr/Biomni | psknlr | https://github.com/psknlr/Biomni | main | UNKNOWN (not returned) | 2026-02-18T01:45:36Z | 2026-02-18T01:45:36Z | 2026-02-18T01:57:37Z | false | false | Apache-2.0 | 6082 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 242 | IMPF-AI/BiomniV2 | IMPF-AI | https://github.com/IMPF-AI/BiomniV2 | main | UNKNOWN (not returned) | 2026-02-18T01:36:20Z | 2026-02-18T01:36:20Z | 2026-02-16T18:29:21Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 243 | vidhidhaduk05/Biomni | vidhidhaduk05 | https://github.com/vidhidhaduk05/Biomni | main | UNKNOWN (not returned) | 2026-02-13T22:43:03Z | 2026-02-13T22:43:03Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 244 | aurora-bio/Biomni | aurora-bio | https://github.com/aurora-bio/Biomni | main | UNKNOWN (not returned) | 2026-02-13T19:19:03Z | 2026-02-13T19:19:03Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 245 | yenklabs/Biomni | yenklabs | https://github.com/yenklabs/Biomni | main | UNKNOWN (not returned) | 2026-02-13T18:53:38Z | 2026-02-13T18:53:38Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 246 | Rakshitha-Ireddi/Biomni | Rakshitha-Ireddi | https://github.com/Rakshitha-Ireddi/Biomni | main | UNKNOWN (not returned) | 2026-02-13T18:00:11Z | 2026-02-13T18:00:11Z | 2026-02-13T18:21:49Z | false | false | Apache-2.0 | 6124 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 247 | jhjeonkaist/Biomni | jhjeonkaist | https://github.com/jhjeonkaist/Biomni | main | UNKNOWN (not returned) | 2026-02-13T01:12:08Z | 2026-02-13T01:12:08Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 248 | yzjie6/Biomni | yzjie6 | https://github.com/yzjie6/Biomni | main | UNKNOWN (not returned) | 2026-02-12T01:56:01Z | 2026-02-12T01:56:01Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 249 | MPebworthEpana/Biomni | MPebworthEpana | https://github.com/MPebworthEpana/Biomni | main | UNKNOWN (not returned) | 2026-02-11T22:19:56Z | 2026-02-11T22:19:56Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 250 | vb-dbrks/Biomni-on-dbrks | vb-dbrks | https://github.com/vb-dbrks/Biomni-on-dbrks | main | UNKNOWN (not returned) | 2026-02-11T11:56:00Z | 2026-02-11T11:56:00Z | 2026-02-11T13:52:30Z | false | false | Apache-2.0 | 6081 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 251 | asdfefbhjy/Biomni | asdfefbhjy | https://github.com/asdfefbhjy/Biomni | main | UNKNOWN (not returned) | 2026-02-11T01:37:16Z | 2026-02-11T01:37:16Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 252 | Aether-Saint/Biomni | Aether-Saint | https://github.com/Aether-Saint/Biomni | main | UNKNOWN (not returned) | 2026-02-10T17:49:19Z | 2026-02-10T17:49:19Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 253 | chronicgiardia/Biomni | chronicgiardia | https://github.com/chronicgiardia/Biomni | main | UNKNOWN (not returned) | 2026-02-10T08:38:54Z | 2026-07-09T08:33:24Z | 2026-07-09T08:33:00Z | false | false | Apache-2.0 | 5767 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 254 | Paraschamoli/Biomni | Paraschamoli | https://github.com/Paraschamoli/Biomni | main | UNKNOWN (not returned) | 2026-02-10T08:13:26Z | 2026-02-10T08:13:26Z | 2026-02-09T23:38:01Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 255 | szxcool/Biomni | szxcool | https://github.com/szxcool/Biomni | main | UNKNOWN (not returned) | 2026-02-08T09:53:33Z | 2026-02-08T09:53:39Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 256 | llmsc-security-test/Biomni | llmsc-security-test | https://github.com/llmsc-security-test/Biomni | main | UNKNOWN (not returned) | 2026-02-08T08:31:25Z | 2026-04-25T07:42:30Z | 2026-02-23T16:09:03Z | false | false | Apache-2.0 | 6087 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 257 | liuchuanyi/Biomni | liuchuanyi | https://github.com/liuchuanyi/Biomni | main | UNKNOWN (not returned) | 2026-02-07T07:51:22Z | 2026-02-07T07:51:22Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 258 | goodb/Biomni | goodb | https://github.com/goodb/Biomni | main | UNKNOWN (not returned) | 2026-02-06T22:36:17Z | 2026-02-06T22:36:17Z | 2026-03-01T06:02:33Z | false | false | Apache-2.0 | 6111 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 259 | katalyzeAI/Biomni | katalyzeAI | https://github.com/katalyzeAI/Biomni | main | UNKNOWN (not returned) | 2026-02-06T15:13:45Z | 2026-02-09T16:38:25Z | 2026-02-09T16:38:34Z | false | false | Apache-2.0 | 6119 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 260 | staskh/Biomni | staskh | https://github.com/staskh/Biomni | main | UNKNOWN (not returned) | 2026-02-05T08:07:35Z | 2026-02-05T08:07:35Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 261 | geobio/Biomni | geobio | https://github.com/geobio/Biomni | main | UNKNOWN (not returned) | 2026-02-05T01:52:10Z | 2026-02-05T01:52:10Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 262 | kitoti/Biomni | kitoti | https://github.com/kitoti/Biomni | main | UNKNOWN (not returned) | 2026-02-05T01:42:07Z | 2026-02-05T01:42:07Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 263 | akotlar/Biomni | akotlar | https://github.com/akotlar/Biomni | main | UNKNOWN (not returned) | 2026-02-04T23:38:55Z | 2026-02-04T23:38:55Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 264 | Nimbus-Discovery-Inc/Biomni | Nimbus-Discovery-Inc | https://github.com/Nimbus-Discovery-Inc/Biomni | main | UNKNOWN (not returned) | 2026-02-04T20:47:12Z | 2026-02-04T20:47:12Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 265 | juliaseungjoobaek/Biomni | juliaseungjoobaek | https://github.com/juliaseungjoobaek/Biomni | main | UNKNOWN (not returned) | 2026-02-04T18:34:11Z | 2026-02-04T18:34:11Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 266 | JulieOnIsland/Biomni | JulieOnIsland | https://github.com/JulieOnIsland/Biomni | main | UNKNOWN (not returned) | 2026-02-04T16:53:26Z | 2026-02-04T16:53:26Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 267 | hgim01/Biomni | hgim01 | https://github.com/hgim01/Biomni | main | UNKNOWN (not returned) | 2026-02-04T07:02:03Z | 2026-02-04T07:02:03Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 268 | manolaz/Biomni | manolaz | https://github.com/manolaz/Biomni | main | UNKNOWN (not returned) | 2026-02-04T00:49:08Z | 2026-02-04T00:49:08Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 269 | Pidem/Biomni | Pidem | https://github.com/Pidem/Biomni | main | UNKNOWN (not returned) | 2026-02-03T17:20:03Z | 2026-02-03T17:20:04Z | 2026-02-03T17:20:28Z | false | false | Apache-2.0 | 6082 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 270 | stevewithjobs/Biomni_molecule | stevewithjobs | https://github.com/stevewithjobs/Biomni_molecule | main | UNKNOWN (not returned) | 2026-02-03T14:02:34Z | 2026-07-16T16:13:44Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 271 | seijung-k/Biomni | seijung-k | https://github.com/seijung-k/Biomni | main | UNKNOWN (not returned) | 2026-02-03T00:22:07Z | 2026-02-03T00:22:07Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 272 | JCupe17/Biomni | JCupe17 | https://github.com/JCupe17/Biomni | main | UNKNOWN (not returned) | 2026-02-02T13:28:30Z | 2026-02-02T13:28:30Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 273 | Science-Will-Win/Biomni | Science-Will-Win | https://github.com/Science-Will-Win/Biomni | main | UNKNOWN (not returned) | 2026-02-02T03:26:50Z | 2026-07-04T12:40:10Z | 2026-07-04T12:40:02Z | false | false | Apache-2.0 | 5576 | 0 | 2 | UNKNOWN | NOT_ADDED |
| 274 | HendricksJudy/Biomni | HendricksJudy | https://github.com/HendricksJudy/Biomni | main | UNKNOWN (not returned) | 2026-02-01T19:58:04Z | 2026-02-01T19:58:04Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 275 | siavashre/amplicon-repo-agentai | siavashre | https://github.com/siavashre/amplicon-repo-agentai | main | UNKNOWN (not returned) | 2026-01-31T00:42:33Z | 2026-02-02T23:42:03Z | 2026-04-17T23:29:57Z | false | false | Apache-2.0 | 179398 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 276 | qurh/Biomni | qurh | https://github.com/qurh/Biomni | main | UNKNOWN (not returned) | 2026-01-30T01:09:32Z | 2026-01-30T01:09:33Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 277 | yaswanth169/Biomni | yaswanth169 | https://github.com/yaswanth169/Biomni | main | UNKNOWN (not returned) | 2026-01-27T19:18:50Z | 2026-01-27T19:25:02Z | 2026-01-27T19:24:58Z | false | false | Apache-2.0 | 6099 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 278 | samalt-os/Biomni | samalt-os | https://github.com/samalt-os/Biomni | main | UNKNOWN (not returned) | 2026-01-26T23:21:10Z | 2026-01-26T23:21:10Z | 2026-01-26T18:39:02Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 279 | biochemi/Biomni | biochemi | https://github.com/biochemi/Biomni | main | UNKNOWN (not returned) | 2026-01-25T18:46:09Z | 2026-01-25T18:46:09Z | 2026-01-19T18:50:08Z | false | false | Apache-2.0 | 6109 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 280 | CiaranMccarthy1/Biomni-neuroscience | CiaranMccarthy1 | https://github.com/CiaranMccarthy1/Biomni-neuroscience | main | UNKNOWN (not returned) | 2026-01-24T15:40:33Z | 2026-01-31T23:00:51Z | 2026-01-31T23:00:46Z | false | false | Apache-2.0 | 6090 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 281 | rwbaber/Biomni | rwbaber | https://github.com/rwbaber/Biomni | main | UNKNOWN (not returned) | 2026-01-23T17:39:22Z | 2026-01-25T12:29:15Z | 2026-01-25T12:29:10Z | false | false | Apache-2.0 | 6125 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 282 | yarikoptic/Biomni | yarikoptic | https://github.com/yarikoptic/Biomni | main | UNKNOWN (not returned) | 2026-01-20T21:21:18Z | 2026-01-20T21:21:18Z | 2026-01-21T03:04:56Z | false | false | Apache-2.0 | 6115 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 283 | ngshasan/Biomni | ngshasan | https://github.com/ngshasan/Biomni | main | UNKNOWN (not returned) | 2026-01-20T17:43:09Z | 2026-01-20T17:43:09Z | 2026-01-19T18:50:08Z | false | false | Apache-2.0 | 6109 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 284 | Niraj288/Biomni | Niraj288 | https://github.com/Niraj288/Biomni | main | UNKNOWN (not returned) | 2026-01-18T03:28:15Z | 2026-01-18T03:28:15Z | 2026-01-15T04:23:43Z | false | false | Apache-2.0 | 6107 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 285 | BenaroyaResearch/Biomni | BenaroyaResearch | https://github.com/BenaroyaResearch/Biomni | main | UNKNOWN (not returned) | 2026-01-16T18:20:12Z | 2026-03-09T23:56:06Z | 2026-04-08T16:55:29Z | false | false | Apache-2.0 | 5435 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 286 | wpr7280/MyBiomni | wpr7280 | https://github.com/wpr7280/MyBiomni | main | UNKNOWN (not returned) | 2026-01-16T07:56:14Z | 2026-01-16T07:56:14Z | 2026-04-08T06:55:27Z | false | false | Apache-2.0 | 8264 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 287 | shaileshchaudhary11/Biomni | shaileshchaudhary11 | https://github.com/shaileshchaudhary11/Biomni | main | UNKNOWN (not returned) | 2026-01-15T05:00:16Z | 2026-01-15T05:00:16Z | 2026-01-15T04:23:43Z | false | false | Apache-2.0 | 6047 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 288 | guoshunhao-creator/Biomni | guoshunhao-creator | https://github.com/guoshunhao-creator/Biomni | main | UNKNOWN (not returned) | 2026-01-13T02:07:06Z | 2026-01-13T02:07:06Z | 2026-01-12T18:34:53Z | false | false | Apache-2.0 | 6047 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 289 | BlueOrbit/Biomni | BlueOrbit | https://github.com/BlueOrbit/Biomni | main | UNKNOWN (not returned) | 2026-01-07T13:32:46Z | 2026-01-07T13:32:46Z | 2025-12-22T18:26:50Z | false | false | Apache-2.0 | 6004 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 290 | KyleNeverGivesUp/Biomni | KyleNeverGivesUp | https://github.com/KyleNeverGivesUp/Biomni | main | UNKNOWN (not returned) | 2026-01-06T15:22:59Z | 2026-03-14T22:52:41Z | 2026-03-14T22:52:37Z | false | false | Apache-2.0 | 5810 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 291 | mengsong-econ/Biomni | mengsong-econ | https://github.com/mengsong-econ/Biomni | main | UNKNOWN (not returned) | 2026-01-06T01:57:16Z | 2026-01-06T01:57:16Z | 2025-12-22T18:26:50Z | false | false | Apache-2.0 | 6004 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 292 | simon2036/Biomni | simon2036 | https://github.com/simon2036/Biomni | main | UNKNOWN (not returned) | 2026-01-03T01:33:37Z | 2026-01-03T01:33:38Z | 2025-12-22T18:26:50Z | false | false | Apache-2.0 | 6004 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 293 | hanlin-yang/BioAiSaaS | hanlin-yang | https://github.com/hanlin-yang/BioAiSaaS | main | UNKNOWN (not returned) | 2026-01-02T14:55:40Z | 2026-01-02T17:02:41Z | 2026-01-02T17:02:37Z | false | false | Apache-2.0 | 6022 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 294 | yikuide-lab/Biomni | yikuide-lab | https://github.com/yikuide-lab/Biomni | main | UNKNOWN (not returned) | 2025-12-23T00:54:00Z | 2025-12-23T00:54:00Z | 2025-12-22T18:26:50Z | false | false | Apache-2.0 | 6004 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 295 | kimdn/Biomni | kimdn | https://github.com/kimdn/Biomni | main | UNKNOWN (not returned) | 2025-12-21T15:00:26Z | 2025-12-21T15:00:26Z | 2025-12-15T18:42:16Z | false | false | Apache-2.0 | 6004 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 296 | cs-shali/Biomni | cs-shali | https://github.com/cs-shali/Biomni | main | UNKNOWN (not returned) | 2025-12-17T13:26:28Z | 2025-12-17T13:26:28Z | 2025-12-15T18:42:16Z | false | false | Apache-2.0 | 6004 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 297 | zhouhr3/Biomni | zhouhr3 | https://github.com/zhouhr3/Biomni | main | UNKNOWN (not returned) | 2025-12-16T13:35:57Z | 2025-12-16T13:35:57Z | 2025-12-15T18:42:16Z | false | false | Apache-2.0 | 6004 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 298 | aslansd/Biomni | aslansd | https://github.com/aslansd/Biomni | main | UNKNOWN (not returned) | 2025-12-11T18:00:54Z | 2025-12-11T18:00:54Z | 2025-12-08T18:45:36Z | false | false | Apache-2.0 | 6003 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 299 | andrewsu/Biomni | andrewsu | https://github.com/andrewsu/Biomni | main | UNKNOWN (not returned) | 2025-12-11T17:56:18Z | 2026-01-23T19:17:37Z | 2026-02-22T02:14:30Z | false | false | Apache-2.0 | 6302 | 0 | 0 | UNKNOWN | NOT_ADDED |
| 300 | drgmk/Biomni | drgmk | https://github.com/drgmk/Biomni | main | UNKNOWN (not returned) | 2025-12-10T22:15:23Z | 2025-12-17T22:28:59Z | 2025-12-17T22:28:55Z | false | false | Apache-2.0 | 5785 | 0 | 0 | UNKNOWN | NOT_ADDED |

## Evidence

1. GitHub repository metadata API (Tier 1, observed
   `2026-08-22T20:47:08Z`):
   https://api.github.com/repos/snap-stanford/Biomni
2. GitHub List forks API page 3 (Tier 1, observed
   `2026-08-22T20:47:10Z`):
   https://api.github.com/repos/snap-stanford/Biomni/forks?per_page=100&page=3&sort=newest
3. Official GitHub REST documentation for List forks and `sort` (Tier 1):
   https://docs.github.com/en/rest/repos/forks?apiVersion=2022-11-28#list-forks
4. Parent-verified canonical inventories used for overlap checking:
   `research/biomni-ecosystem/upstream/forks/batch-001.md` and
   `research/biomni-ecosystem/upstream/forks/batch-002.md`.
5. Pagination evidence is the page-3 HTTP `Link` header summarized above.

## Uncertainty and limitations

- The public-fork inventory remains incomplete; pages 4–7 are unprocessed.
- GitHub counts and sorted page boundaries can change during collection.
  `forks_count = 690` and the seven-page Link header are observations at the
  stated timestamps.
- Zero overlap does not eliminate page-drift risk when forks are created, deleted,
  or change visibility between requests.
- No branch or commit comparison was performed. Ahead/behind state, substantive
  uniqueness, related PRs, duplication, ancestry, and merge status remain
  `UNKNOWN`.
- `pushed_at` does not establish a unique fork change.
- Default-branch head SHAs were absent from this response and remain `UNKNOWN`.
- Public APIs cannot expose private forks, deleted forks, or non-public material.
- Repository license metadata does not resolve component-level licensing.

## Next action

Resume bounded discovery at:

`GET https://api.github.com/repos/snap-stanford/Biomni/forks?per_page=100&page=4&sort=newest`

Preserve the API version, sort, fields, evidence policy, and `UNKNOWN`
uniqueness status. Add no owner to `P` unless later screening establishes
substantive unique commits.
