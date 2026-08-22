# Code-visible People Seed Inventory 001

Parent verification: `VERIFIED` at `2026-08-22T20:53:22Z`. Fresh contributor
requests returned 45 rows: 39 User logins, one Bot login, and five anonymous
rows; page 2 was empty and contribution counts sum to 487. The frozen Git DAG has
487 reachable commits and 56 exact raw author/committer tuples. No explicit login
overlaps the six existing public-member records. Raw tuples remain unresolved.

```yaml
task_id: people-seed-inventory-001
status: COMPLETE_FOR_BOUNDED_SCOPE
claim_class: FACT
source_tier: 1
observed_at_utc: 2026-08-22T20:38:14Z
repository: snap-stanford/Biomni
frozen_main_head: 400c1f366b96a35ca253e13c9b06c5076af41d65
contributors_pagination: EXHAUSTED
history_walk: COMPLETE_THROUGH_FROZEN_HEAD
canonical_ids_allocated: 0
```

## Scope and method

This is a bounded initial seed inventory from exactly two code-visible surfaces:

1. the official GitHub contributors endpoint for `snap-stanford/Biomni`, requested
   with `anon=1`, `per_page=100`, and explicit page numbers until an empty page;
2. every commit reachable from frozen main HEAD
   `400c1f366b96a35ca253e13c9b06c5076af41d65`, using raw Git author and committer
   name/email fields (`%an`, `%ae`, `%cn`, `%ce`).

The actual objective is a safe repository-discovery seed set, not biographical
identity resolution. Explicit GitHub logins are deduplicated by login. Raw commit
name/email pairs are preserved separately as unresolved identity mappings. No
name, email, numeric user ID, or apparent noreply-email correspondence was used to
guess that a commit identity belongs to a GitHub login.

No person's repositories were inventoried. No paper, lab, company, collaborator,
or social relationship was added. PR authors and owners of forks later shown to
have substantive unique commits will be merged from their dedicated inventories;
they are not complete in this seed. Public organization members and relevant
branch-only contributors are also outside this bounded worker.

All external content was treated as untrusted data. No repository code, script,
package, binary, workflow, or source-provided instruction was executed.

## Counts and coverage

| Measure | Count/status |
|---|---:|
| Contributor endpoint rows with `anon=1` | 45 |
| Explicit GitHub login rows | 40 |
| Explicit `User` login rows | 39 |
| Explicit `Bot` login rows | 1 |
| Anonymous contributor rows | 5 |
| Endpoint-reported contributions, including anonymous | 487 |
| Commits reachable from frozen HEAD | 487 |
| Unique raw author name/email pairs | 55 |
| Unique raw committer name/email pairs | 39 |
| Exact author/committer pairs appearing in both roles | 38 |
| Union of exact raw author/committer pairs | 56 |
| Distinct raw names in that union | 51 |
| Distinct raw emails in that union | 50 |
| Canonical person IDs allocated | 0 |

The equality between 487 endpoint-reported contributions (when anonymous rows are
included) and 487 reachable commits is an observation, not an identity mapping.

## Pagination evidence

- Page 1 request:
  `GET /repos/snap-stanford/Biomni/contributors?per_page=100&page=1&anon=1`
- Page 1 HTTP result: `200`; 45 rows; fewer than `per_page=100`; no next-page
  relation.
- Page 2 request:
  `GET /repos/snap-stanford/Biomni/contributors?per_page=100&page=2&anon=1`
- Page 2 HTTP result: `200`; zero rows. Its `Link` header identified page 1 as
  `rel="last"`.
- Pagination status: **EXHAUSTED**. There is no resume cursor.

## Explicit GitHub-login seeds

Each row is a direct contributor relationship reported by the official endpoint.
Contribution counts are GitHub's returned values, not independent feature counts.
The bot is retained as a code-visible actor but is not counted as a human person.

| GitHub login | API type | Relationship/evidence | Stable API evidence |
|---|---|---|---|
| [`amehrjou`](https://github.com/amehrjou) | `User` | contributor; 2 contributions | user ID `17348736` |
| [`andrewsu`](https://github.com/andrewsu) | `User` | contributor; 1 contribution | user ID `2635409` |
| [`anngvu`](https://github.com/anngvu) | `User` | contributor; 4 contributions | user ID `32753274` |
| [`divyesh-htree`](https://github.com/divyesh-htree) | `User` | contributor; 2 contributions | user ID `163984725` |
| [`Edison-A-N`](https://github.com/Edison-A-N) | `User` | contributor; 6 contributions | user ID `16491887` |
| [`evolu8`](https://github.com/evolu8) | `User` | contributor; 1 contribution | user ID `1828165` |
| [`ginylil-tech`](https://github.com/ginylil-tech) | `User` | contributor; 1 contribution | user ID `219282325` |
| [`HasanAldhahi`](https://github.com/HasanAldhahi) | `User` | contributor; 1 contribution | user ID `88090091` |
| [`HelloWorldLTY`](https://github.com/HelloWorldLTY) | `User` | contributor; 6 contributions | user ID `43333475` |
| [`igor-sadalski`](https://github.com/igor-sadalski) | `User` | contributor; 6 contributions | user ID `63819680` |
| [`jucor`](https://github.com/jucor) | `User` | contributor; 1 contribution | user ID `660037` |
| [`kexinhuang12345`](https://github.com/kexinhuang12345) | `User` | contributor; 80 contributions | user ID `27795075` |
| [`kuanlinhuang`](https://github.com/kuanlinhuang) | `User` | contributor; 10 contributions | user ID `10150469` |
| [`lxasqjc`](https://github.com/lxasqjc) | `User` | contributor; 2 contributions | user ID `24780428` |
| [`marcosbolanos`](https://github.com/marcosbolanos) | `User` | contributor; 7 contributions | user ID `34308113` |
| [`mickaelleclercq`](https://github.com/mickaelleclercq) | `User` | contributor; 6 contributions | user ID `16944989` |
| [`MintaYLu`](https://github.com/MintaYLu) | `User` | contributor; 5 contributions | user ID `75707105` |
| [`MinxZ`](https://github.com/MinxZ) | `User` | contributor; 4 contributions | user ID `20724988` |
| [`nevergreendd`](https://github.com/nevergreendd) | `User` | contributor; 2 contributions | user ID `26918264` |
| [`PabloPauling`](https://github.com/PabloPauling) | `User` | contributor; 15 contributions | user ID `173919672` |
| [`Pidem`](https://github.com/Pidem) | `User` | contributor; 2 contributions | user ID `18529916` |
| [`PLippmann`](https://github.com/PLippmann) | `User` | contributor; 4 contributions | user ID `55153114` |
| [`pre-commit-ci[bot]`](https://github.com/apps/pre-commit-ci) | `Bot` | contributor; 70 contributions | user ID `66853113` |
| [`ryanDing26`](https://github.com/ryanDing26) | `User` | contributor; 2 contributions | user ID `110417507` |
| [`RyanLi1028`](https://github.com/RyanLi1028) | `User` | contributor; 6 contributions | user ID `71858089` |
| [`SALhik`](https://github.com/SALhik) | `User` | contributor; 1 contribution | user ID `123875913` |
| [`sbonner0`](https://github.com/sbonner0) | `User` | contributor; 5 contributions | user ID `10208489` |
| [`serena2z`](https://github.com/serena2z) | `User` | contributor; 157 contributions | user ID `71460822` |
| [`shantanusharma`](https://github.com/shantanusharma) | `User` | contributor; 3 contributions | user ID `925897` |
| [`shengyongniu`](https://github.com/shengyongniu) | `User` | contributor; 12 contributions | user ID `10880134` |
| [`shibahara-1113`](https://github.com/shibahara-1113) | `User` | contributor; 1 contribution | user ID `122777116` |
| [`SnowLightPath`](https://github.com/SnowLightPath) | `User` | contributor; 14 contributions | user ID `203191455` |
| [`th86`](https://github.com/th86) | `User` | contributor; 1 contribution | user ID `603372` |
| [`tuln128`](https://github.com/tuln128) | `User` | contributor; 1 contribution | user ID `43870685` |
| [`vlln`](https://github.com/vlln) | `User` | contributor; 1 contribution | user ID `43031803` |
| [`yhqu`](https://github.com/yhqu) | `User` | contributor; 1 contribution | user ID `59551064` |
| [`zancmeresek`](https://github.com/zancmeresek) | `User` | contributor; 1 contribution | user ID `80284560` |
| [`Zethson`](https://github.com/Zethson) | `User` | contributor; 2 contributions | user ID `21954664` |
| [`zhanxw`](https://github.com/zhanxw) | `User` | contributor; 1 contribution | user ID `157832` |
| [`zskylarli`](https://github.com/zskylarli) | `User` | contributor; 5 contributions | user ID `64866606` |

No duplicate GitHub login or numeric user ID was present among these 40 rows.

## Anonymous rows from the contributor endpoint

These rows have no GitHub login and therefore remain unresolved name/email
identities. Four are exact raw author tuples in the local history. The `root`
row differs from the raw Git tuple only by email-domain letter case; it is not
silently merged.

| Returned name/email | Relationship/evidence |
|---|---|
| `Igor Sadalski <igor.sadalski@somite.ai>` | anonymous contributor; 21 contributions |
| `Igor Sadalski <igor@somite.ai>` | anonymous contributor; 6 contributions |
| `root <root@laptop-vei2itl9.localdomain>` | anonymous contributor; 3 contributions; potential case-only duplicate of raw Git tuple |
| `Helloworldlty <tianyu.18@intl.zju.edu.cn>` | anonymous contributor; 3 contributions |
| `Minta <mintalu6@gmail.com>` | anonymous contributor; 2 contributions |

## Raw commit identities — unresolved mappings

Rows are deduplicated only by the exact `(name, email)` tuple across the complete
reachable history. Counts are occurrences in the named Git role. `A:` and `C:`
give a representative full commit SHA for author and committer evidence. Every SHA
resolves under `https://github.com/snap-stanford/Biomni/commit/<SHA>`.

| Commit identity (exact name + email) | Relationship/count | Representative evidence SHA(s) |
|---|---|---|
| `amehrjou <mehrjou.arash@gmail.com>` | author (2); committer (2) | `A:97b4da64aad811baa0a7f6def878b4542d8fbae3; C:97b4da64aad811baa0a7f6def878b4542d8fbae3` |
| `Andrew Su <asu@scripps.edu>` | author (1); committer (1) | `A:c73eb050597f566c14f6313b1920c65d668db3aa; C:c73eb050597f566c14f6313b1920c65d668db3aa` |
| `Anh Nguyet Vu <anngvu@gmail.com>` | author (4); committer (4) | `A:5f540c25587474444ea7c14953001d98f088b19d; C:5f540c25587474444ea7c14953001d98f088b19d` |
| `divyesh-htree <divyesh.patil@fxis.ai>` | author (2); committer (2) | `A:074f5b90326b878e4881e041e6aba8e86f44c03f; C:074f5b90326b878e4881e041e6aba8e86f44c03f` |
| `Edison <Edison.A.N@hotmail.com>` | author (1) | `A:9f51eeb1010cb536623bebcfa44bcaf2cdccabfd` |
| `Edison-A-N <Edison.A.N@hotmail.com>` | author (5); committer (5) | `A:d4b410d64eedc7b8a9d3a1b22eace52bb1d0cf58; C:d4b410d64eedc7b8a9d3a1b22eace52bb1d0cf58` |
| `evolu8 <phil@evolu8.com>` | author (1) | `A:b677959799db7482ec78b36164d974641bc1af8f` |
| `Ginylil-Tech <tech@ginylil.com>` | author (1); committer (1) | `A:63443affda1a09e758785b55be4c16f06d077b56; C:63443affda1a09e758785b55be4c16f06d077b56` |
| `GitHub <noreply@github.com>` | committer (174) | `C:400c1f366b96a35ca253e13c9b06c5076af41d65` |
| `Hasan Aldhahi <88090091+HasanAldhahi@users.noreply.github.com>` | author (1); committer (1) | `A:e63d7a7b85cb0bc0d220f97fd6f183eb92ab37c1; C:e63d7a7b85cb0bc0d220f97fd6f183eb92ab37c1` |
| `HelloWorldLTY <43333475+HelloWorldLTY@users.noreply.github.com>` | author (6) | `A:f5f2711f804e6bd7b23521ef0aab47f7b8c80959` |
| `Helloworldlty <tianyu.18@intl.zju.edu.cn>` | author (3); committer (3) | `A:89395b6d44a68a28c5381554cd4e8696db3e5775; C:89395b6d44a68a28c5381554cd4e8696db3e5775` |
| `huangkuanlin <huangkuanlin@gmail.com>` | author (10); committer (10) | `A:2927ef128c195fc1920a693b2ef16b1cfe9e779c; C:2927ef128c195fc1920a693b2ef16b1cfe9e779c` |
| `Igor Sadalski <igor.sadalski@gmail.com>` | author (6); committer (6) | `A:0de0af2030d8019696ed5ec6321f0a787f000851; C:0de0af2030d8019696ed5ec6321f0a787f000851` |
| `Igor Sadalski <igor.sadalski@somite.ai>` | author (21); committer (21) | `A:9bcb417990d28ec822e6b6646263acab66a0a84a; C:9bcb417990d28ec822e6b6646263acab66a0a84a` |
| `Igor Sadalski <igor@somite.ai>` | author (6); committer (6) | `A:07c9dc194fd589030a1f8bf6041ba17004b0deca; C:07c9dc194fd589030a1f8bf6041ba17004b0deca` |
| `Julien Cornebise <julien@cornebise.com>` | author (1) | `A:96e2f74cc4b4389ecabd455b581298f92cf02fc9` |
| `Kexin Huang <kexinh@stanford.edu>` | author (58) | `A:400c1f366b96a35ca253e13c9b06c5076af41d65` |
| `Kexin Huang <kexinhuang.work@gmail.com>` | author (7); committer (7) | `A:8490900aa6b050f992a3384321d70d93e8cdd85e; C:8490900aa6b050f992a3384321d70d93e8cdd85e` |
| `kexinhuang12345 <kexinh@stanford.edu>` | author (15); committer (15) | `A:9c469f21d6739d2bba67883bd04f54cd109cd47d; C:9c469f21d6739d2bba67883bd04f54cd109cd47d` |
| `Lukas Heumos <lukas.heumos@posteo.net>` | author (2); committer (2) | `A:5cc0c545f43617e264327ca97e67554cadcab2cc; C:5cc0c545f43617e264327ca97e67554cadcab2cc` |
| `lxasqjc <chen.jin@astrazeneca.com>` | author (2); committer (2) | `A:647e9f1fca9ef4565fb8541135a03371de861307; C:647e9f1fca9ef4565fb8541135a03371de861307` |
| `marcos <marcosqbv@gmail.com>` | author (6); committer (6) | `A:b82d340786828b468af0b37fe6cc4eaf82f5a521; C:b82d340786828b468af0b37fe6cc4eaf82f5a521` |
| `marcosbolanos <marcosqbv@gmail.com>` | author (1); committer (1) | `A:62940c152b5be455f3336fdf6efe2c9dd0b21173; C:62940c152b5be455f3336fdf6efe2c9dd0b21173` |
| `Mickael Leclercq <mickaelleclercq@users.noreply.github.com>` | author (6); committer (6) | `A:b3d4deb81e79903ce84ae1477da80c4c0b415820; C:b3d4deb81e79903ce84ae1477da80c4c0b415820` |
| `Minta <mintalu6@gmail.com>` | author (2); committer (2) | `A:d811aba230369ba4e24b32ad799ce8c13785c618; C:d811aba230369ba4e24b32ad799ce8c13785c618` |
| `MintaYLu <75707105+MintaYLu@users.noreply.github.com>` | author (5) | `A:9891fe923e8ca4e6551e9074da05c119b058f78e` |
| `MinxZ <z670172581@icloud.com>` | author (4); committer (4) | `A:2b4adf222f42b6f60187aefd2022ff6d8871e1f3; C:2b4adf222f42b6f60187aefd2022ff6d8871e1f3` |
| `nevergreendd <nevergreendd@gmail.com>` | author (2); committer (2) | `A:7cefe0ea43aab28bc232a57d924145bf637b3f2e; C:7cefe0ea43aab28bc232a57d924145bf637b3f2e` |
| `NIU, SHENG-YONG <niu.shengyong@gmail.com>` | author (2) | `A:30e085557fa4c4c536ff8c1e473ca60676c932b8` |
| `Pablo Villanueva <pablo@pauling.ai>` | author (3) | `A:e4e1aedf9860cccbbd7722f2817d51d2c667e71a` |
| `PabloPauling <pablo@pauling.ai>` | author (12); committer (12) | `A:30cb04a4ac3b0df04106ea36231060cfd664eeaf; C:30cb04a4ac3b0df04106ea36231060cfd664eeaf` |
| `Pierre de Malliard <demalliardpierre@gmail.com>` | author (2) | `A:54ff0d84f7bc0c5974e5ef0d03fda881244710f1` |
| `PLippmann <p.lippmann@tudelft.nl>` | author (4); committer (4) | `A:788d02f624b45f0d1450a975d14d701e55ee1274; C:788d02f624b45f0d1450a975d14d701e55ee1274` |
| `pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>` | author (70); committer (58) | `A:72600f0ddd9204bda3df9a1e64042ad473c81f03; C:0260c876e88868002a0a59f0eef03ce340aa2841` |
| `root <root@LAPTOP-VEI2ITL9.localdomain>` | author (3) | `A:0d90735149e1c7ad749ffb2ba43fdaef66932bd0` |
| `Ryan Ding <110417507+ryanDing26@users.noreply.github.com>` | author (1) | `A:c1a6552da6047fcae6c47868ec27286f973d900f` |
| `Ryan Li <71858089+RyanLi0802@users.noreply.github.com>` | author (3) | `A:1465cb2653a53ddab9c05280bf2677a14841dfd9` |
| `Ryan Li <lansong@stanford.edu>` | author (3); committer (7) | `A:8089bed75c32f6f7bdcace72c837ad3784984c04; C:8089bed75c32f6f7bdcace72c837ad3784984c04` |
| `ryanDing26 <110417507+ryanDing26@users.noreply.github.com>` | author (1); committer (1) | `A:0c66fc9daaf65b1244f4389bc2a94c45b6844038; C:0c66fc9daaf65b1244f4389bc2a94c45b6844038` |
| `SALhik <123875913+SALhik@users.noreply.github.com>` | author (1) | `A:12e2833974727b3b3330dd81110d19f77163f5be` |
| `sbonner0 <stephen.bonner0@icloud.com>` | author (5); committer (5) | `A:ae0c6afed1758db9c9bead584126de39e00c6535; C:ae0c6afed1758db9c9bead584126de39e00c6535` |
| `Serena Z <serena2z@stanford.edu>` | author (54); committer (54) | `A:6603b4aa43694d2a2eb8565c484c16264dc68daf; C:6603b4aa43694d2a2eb8565c484c16264dc68daf` |
| `Serena Zhang <71460822+serena2z@users.noreply.github.com>` | author (75) | `A:429e5be970f149877515198aa138d204b308e32a` |
| `serena2z <serena2zhang@gmail.com>` | author (28); committer (28) | `A:3e704830ed2f8f36a6b156244a2a087cc928c175; C:3e704830ed2f8f36a6b156244a2a087cc928c175` |
| `Shantanu Sharma <shantanusharma@users.noreply.github.com>` | author (3); committer (3) | `A:709dfcab6d023f4e4100d90945c4ba3d4d7af6d7; C:709dfcab6d023f4e4100d90945c4ba3d4d7af6d7` |
| `shengyongniu <niu.shengyong@gmail.com>` | author (10); committer (10) | `A:948a5c1576afc0d736cbccee03f7091a4d44312a; C:948a5c1576afc0d736cbccee03f7091a4d44312a` |
| `SnowLightPath <takuma.shibahara@daiichisankyo.com>` | author (14); committer (13) | `A:d05f5fda5dd2ba5bf338cf216448e8d7122184dd; C:0506666ad3b32b73556aad58a89201430503b5e9` |
| `SnowLightPath <takuma_shibahara@icloud.com>` | author (1) | `A:875e590dbb5326b4da839d588fc4ccdd2c4df84a` |
| `Tai-Hsien OuYang <th8623@gmail.com>` | author (1) | `A:a252ebc62caaa908de6e2a7dd4c49773d56df30c` |
| `tuln128 <tuln128@gmail.com>` | author (1); committer (1) | `A:2c30bd1069e51ba39032f9448719efe2d3e1d364; C:2c30bd1069e51ba39032f9448719efe2d3e1d364` |
| `vlln <vlln@qq.com>` | author (1); committer (1) | `A:c66f22a4b81f2f2cf79b9938cd1c034eb7f459eb; C:c66f22a4b81f2f2cf79b9938cd1c034eb7f459eb` |
| `Yuanhao Qu <yuanhaoqu@gmail.com>` | author (1); committer (1) | `A:e875ed42f89892f67d0ba8bd03a1f37729851725; C:e875ed42f89892f67d0ba8bd03a1f37729851725` |
| `zhanxw <zhanxw@users.noreply.github.com>` | author (1) | `A:6b378531bfcd15b389dd428efa52d441648931e2` |
| `Zhuoyan Li <64866606+zskylarli@users.noreply.github.com>` | author (5); committer (5) | `A:e1b0c0d33ebce0eec8a34031c4b26590e771bb16; C:e1b0c0d33ebce0eec8a34031c4b26590e771bb16` |
| `Žan Cmerešek <cmeresek.zan@gmail.com>` | author (1); committer (1) | `A:5be01d8569841ad8db6f47a5f1fc62ad44a2dc4b; C:5be01d8569841ad8db6f47a5f1fc62ad44a2dc4b` |

## Duplicates and unresolved identity mappings

The following are syntactic duplicate leads only. They are **not** merged into a
person and are not asserted to map to any login.

Same email, multiple raw names:

- `110417507+ryanDing26@users.noreply.github.com`: `Ryan Ding`, `ryanDing26`
- `Edison.A.N@hotmail.com`: `Edison`, `Edison-A-N`
- `kexinh@stanford.edu`: `Kexin Huang`, `kexinhuang12345`
- `marcosqbv@gmail.com`: `marcos`, `marcosbolanos`
- `niu.shengyong@gmail.com`: `NIU, SHENG-YONG`, `shengyongniu`
- `pablo@pauling.ai`: `Pablo Villanueva`, `PabloPauling`

Same raw name, multiple emails:

- `Igor Sadalski`: `igor.sadalski@gmail.com`, `igor.sadalski@somite.ai`,
  `igor@somite.ai`
- `Kexin Huang`: `kexinh@stanford.edu`, `kexinhuang.work@gmail.com`
- `Ryan Li`: `71858089+RyanLi0802@users.noreply.github.com`,
  `lansong@stanford.edu`
- `SnowLightPath`: `takuma.shibahara@daiichisankyo.com`,
  `takuma_shibahara@icloud.com`

Additional identity cautions:

- Numeric IDs or login-like strings embedded in GitHub noreply emails are retained
  as raw evidence, not treated as verified cross-layer mappings.
- In particular, the contributor login `RyanLi1028` and raw noreply string
  `RyanLi0802` are different strings; no relationship is inferred.
- `GitHub <noreply@github.com>` is a service committer identity, and
  `pre-commit-ci[bot]` is automation. Neither should inflate a human-person count.
- `root <root@LAPTOP-VEI2ITL9.localdomain>` is a local-machine-style identity with
  no verified public GitHub account mapping.

## OUT_OF_SCOPE_LEAD

None generated. No paper/lab/company/social surface was consulted, and no external
repository contributor was followed.

## Evidence URLs and SHAs

- Complete contributor request, page 1:
  https://api.github.com/repos/snap-stanford/Biomni/contributors?per_page=100&page=1&anon=1
- Exhaustion check, page 2:
  https://api.github.com/repos/snap-stanford/Biomni/contributors?per_page=100&page=2&anon=1
- Frozen main commit:
  https://github.com/snap-stanford/Biomni/commit/400c1f366b96a35ca253e13c9b06c5076af41d65
- Frozen main HEAD: `400c1f366b96a35ca253e13c9b06c5076af41d65`
- Root commit reachable from frozen HEAD:
  `54cfd4712e7596cb02aa93c87e22897a2948d5aa`
- Per-identity representative evidence SHAs are recorded in the raw-identity table.

## Uncertainty and limitations

- GitHub contributor aggregation is cached and time-dependent. This report records
  the response observed at the stated UTC time and does not claim visibility into
  private, deleted, or unattributed activity.
- The API's `contributions` count is treated as returned metadata. It does not
  prove feature authorship, patch uniqueness, or current code ownership.
- Git author and committer fields are self-supplied metadata. They prove that a
  string occurs in public history, not a real-world identity.
- Exact tuple separation is intentionally conservative and may overcount people.
  Conversely, shared machines, emails, or display names can make apparently
  similar tuples belong to different actors.
- This worker does not yet include the complete PR-author, public-org-member,
  relevant-branch-contributor, or substantive-fork-owner surfaces required for the
  final bounded set `P`.

## Next action

The parent coordinator should merge the explicit login seeds with the completed
PR-author inventory and later substantive-fork-owner inventory, deduplicating only
by explicit GitHub login. Keep the 56 raw Git tuples in the unresolved-identity
ledger until direct public evidence supports a mapping; never infer mappings from
name similarity alone. Only after the bounded people set is normalized should a
separate phase inventory each eligible person's public repositories.
