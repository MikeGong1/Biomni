# Code-visible GitHub People Universe Reconciliation — 001

Parent verification: `VERIFIED` at `2026-08-23T04:08:40Z`. This reconciliation
closes the bounded account set P before public-repository inventory begins. It
uses exact GitHub logins and commit SHAs only; no real-world identity mapping is
inferred.

## Bounded source closure

| Entry surface | Processed evidence | Canonical result |
|---|---|---|
| Public `snap-stanford` members | 6/6, endpoint exhausted | Six existing records; all independently re-resolved as GitHub `User` objects |
| Frozen-main contributors/history | 40 login accounts plus 56 exact unresolved raw tuples | Existing seed inventory preserved |
| Biomni PR authors | 76 unique logins from 182/182 PRs | Existing PR-author union preserved |
| Current public Biomni branches | 33/33; four nonzero-ahead refs; 12 unique commits | `serena2z`, `kexinhuang12345`, and `pre-commit-ci[bot]`, all already in P |
| Substantive fork owners | 63 eligible User owners and 12 Organization owners | 63/63 User owners already in P; Organizations excluded from people |
| Normalized fork changes | 75 changes, 72 unique repositories, 1,791 unique change SHAs | 1,791/1,791 official commit author objects resolved |
| Canonical union | all source surfaces above | 161 accounts: 159 GitHub `User` objects and two `Bot` objects |

The 1,791 normalized change SHAs contain 1,696 commits with a GitHub author
login and 95 commits without one. The 1,696 resolved commits reduce to 96 unique
logins; every login now has a canonical person ID. The 95 unresolved commits
reduce to 26 exact raw `(name, email)` tuples and remain explicitly unmapped.

## New canonical accounts

| Person ID | Login | GitHub type | Human-counted | Normalized commits | Change IDs | Repository IDs | Representative SHA |
|---|---|---|---:|---:|---|---|---|
| person-github-000147 | b-snel | User | yes | 4 | change-000024 | repo-000377 | `1f69a9aa08600078a1a14a1fa7a942952c38f44e` |
| person-github-000148 | claude | User | no | 32 | change-000004, 000032, 000034, 000039 | repo-000333, 000348, 000529, 000679, 000777–000779 | `00cf15200cc82b77b5dd1c8c37514a1777a4fcef` |
| person-github-000149 | Copilot | Bot | no | 6 | change-000028 | repo-000283 | `2fc6817e23734e575670aa46340e1ecec72d76f2` |
| person-github-000150 | cursoragent | User | no | 4 | change-000055 | repo-000665 | `0ec0ed34e73e4b686c70a635b8a56d51681c00d8` |
| person-github-000151 | div0-space | User | yes | 7 | change-000017 | repo-000412 | `1ac92f50d4e0ce95e3570a1fff7b1d74989cf0f8` |
| person-github-000152 | europaroso | User | yes | 183 | change-000009 | repo-000453 | `0062deedbc30d153c83b1f697ab717bb42c4b316` |
| person-github-000153 | hannes-brt | User | yes | 6 | change-000040 | repo-000351 | `200436837a4b02d177941ee43bd3f22b2df26e9e` |
| person-github-000154 | HNO333333 | User | yes | 9 | change-000046 | repo-000301 | `3918b4c18b25bcc2f5822603c3fe6a0c792dde6b` |
| person-github-000155 | kiro-agent | User | no | 1 | change-000038 | repo-000400 | `99075c8fef25fdce161c69f86a13f49e56763090` |
| person-github-000156 | robynm | User | yes | 3 | change-000024 | repo-000377 | `09d6fdb0931f642d6419f82febf69ae6c3133ab8` |
| person-github-000157 | shuhanx61 | User | yes | 1 | change-000046 | repo-000301 | `be6e1d13a5e5d1c9937466cd9ad617dc8fb4b27f` |
| person-github-000158 | sphia-g | User | yes | 4 | change-000007 | repo-000290 | `0125560b3afdf3f8ea51dfb328b5120dd8821642` |
| person-github-000159 | xinwuye | User | yes | 2 | change-000033 | repo-000332 | `6a43744ac6805851e3cce1c7e1d110942e86897e` |
| person-github-000160 | YasamanJafari | User | yes | 6 | change-000022 | repo-000367 | `1db4b9cf5c7eca58429f9b253595f7390c20795d` |
| person-github-000161 | Zyad-Khan | User | yes | 36 | change-000009 | repo-000453 | `03bd806a41a004422bb90595ce28b16206490a87` |

`claude`, `cursoragent`, and `kiro-agent` are GitHub `User`-type objects, but
their exact commit metadata identifies AI-agent provenance. They are retained as
code-visible accounts with `human_counted=false`; this does not assert vendor
ownership or a human identity. `Copilot` is a GitHub `Bot` linked by the commit
API to the `copilot-swe-agent` app.

## Existing records enriched

- `person-github-000001`–`000006`: public-member account type, database ID, and
  human-count flag are now explicit.
- `person-github-000018`, `000029`, and `000034`: exact upstream branch-author
  relations were added for `popper_biomni`, the two pre-commit branches, and
  `hotfix/v0.0.6-param-naming` respectively.
- `person-github-000085`–`000087`: batch-001 owner/authors were closed against
  the 20 previously uncached commit author objects.
- `person-github-000019`, `000049`, `000050`, `000090`, and `000113`: exact
  normalized fork-change author relations were added for Biomni-AD, Amplicon,
  the NYU visualization fork, and the JHK/Science-Will-Win lineages.

This pass added or reconciled directly verified relevant-person edges on 21
change records;
13 change records preserve all 26 exact raw identities that lack a GitHub author
login. This is an authorship surface, not a claim of copyright ownership,
employment, authorization, or real-name identity.

## Conservative exclusions and unresolved mappings

- GitHub service committer `web-flow` does not enter P: it appears only as a
  committer on two merge/automation commits, never as their actual author.
- The 26 fork-change raw tuples are not mapped to similarly named owners or known
  accounts. Examples include five distinct Fiona Cai local-host tuples, two John
  Yang local-host tuples, `Minta <mintalu6@gmail.com>`, EC2/Ubuntu/root identities,
  and institution/local-machine email strings.
- The separate frozen-main ledger retains 56 exact raw tuples. The two raw-tuple
  sets may overlap and are not summed into a claimed person count.
- GitHub `User` object type is not proof that a login represents a natural person.
  The canonical `human_counted` field is therefore explicit; the current union is
  156 human-counted accounts and five automation/non-human accounts.

## Evidence and limits

- Previously cached official compare commit objects cover 1,771 of 1,791 unique
  normalized change SHAs. One serialized GraphQL request resolved the remaining
  20/20 immutable commit objects; all belonged to the already present MikeGong1,
  Irishaze, or PayFv accounts.
- A serialized GraphQL profile query resolved all 14 newly identified User-type
  fork authors; the cached commit object independently reports `Copilot` as Bot.
  A separate serialized profile query resolved all six public organization members
  as User objects. No query returned an error or null target.
- Current branch and fork conclusions are limited to public refs and histories.
  Deleted, private, or unpushed work and hidden organization membership remain
  unobservable.
- Person depth remains exactly one. No collaborator or repository contributor was
  followed to create another person.

## Next action

Inventory all 161 canonical accounts' public repositories in bounded batches,
then screen repository relevance before any external-repository deep audit.
