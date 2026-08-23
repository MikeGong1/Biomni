# External deep audit batch 003 — K-Dense, Latch and medical-AI fork families

Observed at: `2026-08-23T16:44:36Z`

Batch status: **COMPLETE — STATIC_ONLY**

## Canonical decision

Queue orders 6, 7 and 9 contain seven bounded person-repository records, all
forks of sources whose owners are outside the depth-1 people universe. All native
fork refs, tags, pull/release pages and child-fork counts were closed before
scientific review.

| Queue | Source family | Bounded forks | Decision |
|---:|---|---:|---|
| 6 | `K-Dense-AI/scientific-agent-skills` | 5 | four substantive historical/current change sets retained; no direct adoption |
| 7 | `latchbio/latch` | 1 | exact current source main; no unique change |
| 9 | `JuneYaooo/awesome-medical-ai` | 1 | one README row, exact open source PR #2; DOC_ONLY |

The K-Dense family yields four Change IDs and three Lineage IDs:

- `change-000088`: merged PR #75, a twelve-Skill scientific bundle;
- `change-000089`: two Kuan fork-only database/API fix commits;
- `change-000090`: merged BIDS PR #125 and its current-source successor;
- `change-000091`: open DataLad PR #227, including the bounded fork prefix;
- `lineage-000033`–`lineage-000035`: Kuan, BIDS and DataLad DAGs.

No Feature or Implementation ID is allocated in Phase 8. The other bounded refs
are exact source objects/ancestors, generated release identities, DOC_ONLY,
FORMAT_ONLY or ENVIRONMENT-only changes and do not justify additional IDs.

## Acquisition and bounded coverage

All external acquisition was serialized and did not use a user token. Ten current
repository metadata documents and ten partial Git mirrors were frozen. Seven
bounded fork pull/release endpoints returned complete short first pages: all pull
pages were empty; releases were Kuan 1, Alex 2 and zero for the other five. Every
fork reports zero child forks.

| Surface | K-Dense source / 5 forks | Latch source / fork | Awesome source / fork |
|---|---:|---:|---:|
| Source heads | 4 | 312 | 1 |
| Source tags | 101 | 68 | 0 |
| Source pull refs | 157 | 513 | 4 |
| Source reported forks, outside `R` | 3,319 | 25 | 5 |
| Bounded native heads | 12 | 1 | 2 |
| Bounded native tags | 170 | 0 | 0 |
| Bounded releases | 3 | 0 | 0 |
| Heads/tags-only unique commits | 12 | 0 | 1 |
| Unique commits after source PR refs | 5 | 0 | 0 |

All mirrors passed `git fsck --full --strict`. Several mirrors report the same
non-fatal dangling Kuan commit after object sharing/fetch, so the evidence supports
object integrity, not a false “zero diagnostics” claim. Source refs were fetched
with `--no-tags` into `refs/upstream/*`; native packed refs remained unchanged.

Source public refs total 317 heads, 169 tags and 674 pull refs. Their 3,349 fork
networks were not expanded: these sources are lineage anchors, not bounded
repository entities. No source repository or source owner ID is added.

## Queue order 6 — K-Dense scientific-agent-skills family

The current source is `390f5146bf3c1877cf15636a3dd7b775e4f0f185`
(696 default-history commits, 2,446 files). Five bounded forks expose 12 heads and
170 native tags. Two forks are pure source history, one carries only source PR
lineages, and two have a true content delta.

### Native-ref normalization

| Repository | Native heads/tags | Default relation | Ref result |
|---|---:|---|---|
| `kuanlinhuang/claude-scientific-skills` | 1 / 1 | main behind 355, ahead 4 | two content commits + two clean sync merges; tag aliases same tip |
| `KalinNonchev/scientific-agent-skills` | 3 / 99 | main behind 28, ahead 0 | all heads/tags exact source refs or ancestors |
| `alexs42/claude-scientific-skills` | 2 / 2 | main behind 322, ahead 0 | one DOC_ONLY security-report commit |
| `yarikoptic/claude-scientific-skills` | 5 / 68 | main behind 310, ahead 0 | BIDS merged; seven commits closed by PR #123/#227 refs |
| `leizhou69/scientific-agent-skills` | 1 / 0 | main behind 271, ahead 0 | source ancestor only |

Independent verification found no stable patch-id duplicate for the three
single-parent fork-only patch groups. Kuan merge commits `713d5bb...` and
`9e54b4a...` have empty remerge diffs and are topology, not content changes.

### `change-000088` — merged Kuan PR #75

PR #75 head `7f94783fab51a468f9a4b08472e8c49111b21fcd` added 12 Skills,
27 files and 6,961 lines. It merged as
`a4eabbb519efebe35bf0baefc5e8ea38e3486f84` on 2026-03-03 and is an ancestor of
current source main.

The old `scientific-skills/` paths no longer exist. Current source retains five
standalone Skills (`depmap`, `glycoengineering`, `molecular-dynamics`,
`phylogenetics`, `scvelo`) and consolidates seven database Skills into
`skills/database-lookup`. Only five reference blobs remain byte-identical. This
is a real historical Feature bundle, but current source is its successor.

| PR Skill | Current relation | Static disposition |
|---|---|---|
| BindingDB | consolidated database reference | current schema-verified rewrite lead only |
| cBioPortal | consolidated database reference | reject PR workflow; denominator and HTTP method errors |
| DepMap | standalone successor | clean-room lead after statistics/access review |
| Glycoengineering | standalone successor | major scientific review; no direct adoption |
| gnomAD | consolidated database reference | reject PR interpretation and query logic |
| GTEx | consolidated database reference | current-version reference lead only |
| InterPro | consolidated database reference | current-schema reference lead only |
| JASPAR | consolidated API reference | redesign scanning/statistics; reject PR code |
| Molecular dynamics | standalone successor | reject until timestep/protocol correction |
| Monarch | consolidated database reference | current entity-centric rewrite lead only |
| Phylogenetics | standalone successor | CLI/scientific/license review required |
| scVelo | corrected standalone successor | use only current successor as a review lead |

Direct fork adoption is **0/12**. Representative material failures include:

- molecular dynamics configures a 4 fs integrator without hydrogen mass
  repartitioning, but later time calculations assume 2 fs;
- gnomAD LoF filtering has boolean-precedence/LC-HC errors and misstates ACMG
  evidence strength;
- glycoengineering treats S/T followed by Pro as a universal inhibitory rule and
  mutates sequons without structure/function constraints;
- cBioPortal mixes patient numerator with sample denominator and calls a fetch
  endpoint with GET;
- JASPAR references undefined `pfm_data`, uses arbitrary score thresholds and
  labels any score drop as disruption;
- Monarch reverses subject/object association roles;
- phylogenetics synthesizes questionable MAFFT flags and ignores `seq_type`;
- original scVelo uses a removed preprocessing parameter; current source fixes it.

External database/API queries can disclose rare phenotype combinations,
unpublished variants, targets, compounds or sequences. Requests generally lack
timeouts and version/schema pins. Per-Skill license headers range across CC,
LGPL, MIT, BSD, `Unknown` and database-specific terms; root MIT does not close
text, data, service or attribution provenance.

The 12-row reduction is
`deep-audit-batch-003-kuan-skill-manifest.jsonl`.

### `change-000089` — Kuan fork-only API fixes

Two non-merge commits survive all source public refs:

- `eb99ad20f41aec72ad8844abad60bc39b93a155e` (+78/-81, six files);
- `d82644b0172f20b3c8f892ce26bd9c8746319a28` (+69/-58, six files).

They touch 11 unique paths across ClinicalTrials, Ensembl, JASPAR, Monarch,
OpenTargets, GTEx and GWAS. Some changes are valid (JASPAR variable repair,
Monarch direction, GTEx v8); others conflict with current APIs or their own code
(Ensembl species path, blanket ClinicalTrials totals, GWAS v2/Mondo assumptions,
OpenTargets `data_types` versus `datasource_ids`). Current source removed the
separate database Skills and independently rewrote their concepts. Preserve the
patches as history, not an integration candidate.

The fork release/tag `v2.26.0` resolves to
`9e54b4aeed137128113ce7b38f99535d3705860a`; source `v2.26.0` resolves to
`3ed035e64cd856852b6b25edd39d0d5e492e9947`. The source tag is an ancestor, but
the fork tag is seven commits later and differs across 148 files. A version key
must include owner/repository, resolved SHA and tree; tag name alone is unsafe.

### `change-000090` — merged BIDS PR #125

PR #125 contains three commits ending at
`75f688228a6c1d7387db81347117a3fd27b53de4`, 8 files and 23,503 additions. It
merged as `8f0ec176971bda8c269e59741339fe9c2e5d890d` and is an ancestor of current
source. Current source moved it to `skills/bids`, split the entry into a shorter
Skill plus `core_workflows.md`, added tests and metadata, but left six schema,
BEP, guide and updater blobs unchanged.

Historical capabilities include BIDS naming/layout, PyBIDS, validation,
DICOM conversion, metadata/events/participants, derivatives/BIDS Apps and a
remote schema/BEP updater. Direct adoption is rejected because:

- human summaries contradict the bundled schema for DWI/fmap requirements and
  misspell `RepetitionTimePreparation`;
- events duration, dummy-scan semantics and PyBIDS-as-validator guidance are
  wrong or overstated;
- modality coverage claims omit independent EMG/MRS/iEEG/behavioral sections;
- concrete BIDS-App Docker commands omit required mounts and pins;
- recommended validator ignore flags can conceal real consistency/header errors;
- preserving raw DICOM under `sourcedata/` plus `.bidsignore` is not
  de-identification, access control or publication protection;
- the updater accepts arbitrary redirecting URLs without allowlist, timeout,
  size/hash/signature, schema-shape/version validation, atomic replacement or a
  provenance manifest;
- bundled BIDS 1.11.1/schema 1.2.1 conflicts with examples/changelog still fixed
  at 1.10.0, proving content/version drift.

The `[DATALAD RUNCMD]` commit records a command but no inputs, outputs, remote
revision or content hashes. Retain only the capability taxonomy for a clean-room,
official-schema-derived design with an explicit PHI gate.

### `change-000091` — open DataLad PR #227

Open, unmerged PR #227 ends at
`997202b7d481c40ca5e22d3ff79f24446642ab44`. The bounded yarikoptic branch
`369e51382109cf6ed078df33b6cefe7a9776e9fb` supplies the first three commits and
has the exact same final tree as the five-commit PR head. The PR exists only in
public pull refs; synthetic `refs/pull/227/merge` is not an upstream merge.

The six-file change describes DataLad/git-annex two-layer storage, retrieval,
provenance/rerun, containers, siblings and publication. Useful clean-room concepts
include pointer-versus-content, `whereis` as recorded belief, special remotes,
`publish-depends`, explicit inputs/outputs, RIA and STAMPED/YODA. Direct adoption
is rejected because it:

- calls `datalad rerun` and historical containers “safe” without inspecting
  untrusted commands, sandboxing, minimal mounts or credential isolation;
- presents GitHub plus `encryption=none` S3 publishing without visibility,
  bucket-policy, PHI/PII/consent or explicit publication approval gates;
- exposes destructive `drop --reckless kill` and `git annex dropunused all`
  without verified live copies, recovery or target-by-target approval;
- permits secrets at any DataLad config level and does not stop tokens entering
  versioned `datalad run` commands/logs;
- uses an off-by-one rerun range and an FSL BET `-m` example that fails to declare
  the generated mask output;
- overstates rerunnable as reproducible and gives an incomplete AGPL obligation
  summary;
- has no tests, pinned command schemas, destructive-command lint or offline
  fixtures.

Keep this as an experimental clean-room candidate only. The canonical experimental
head is the PR head; the bounded fork is a prefix/effective-tree lineage, not a
separate implementation.

### Non-capability surfaces

`alexs42` commit `cca489f1b5942c014de2e7cdd73000b188cd8729` adds only a
432-line AI-authored security report. Its “LOW RISK / SECURE” conclusion is not
supported by reproducible artifacts and is contradicted by its own tree: file
counts are wrong; dynamic import, CLI credential paths, LabArchives plaintext
input/YAML storage, argv key exposure, no-timeout requests and the executable
agent-instruction threat surface are omitted. Treat it as DOC_ONLY evidence, not
a security fix or assurance.

Closed-unmerged PR #123 adds a codespell workflow/config and one typo fix
(4 commits, 3 files, +32/-1). It is ENVIRONMENT/FORMAT_ONLY: `contents: read` and
a pinned codespell action are positive, while `actions/checkout@v4` remains
mutable. No capability ID is warranted.

Alex fork `v2.27.0` and source `v2.27.0` also resolve to different commits; the
fork target remains source-public history, so this is a version-identity warning,
not a unique change.

## Queue order 7 — Latch

`shantanusharma/latch` has one head, no tags, no PR/release/child fork and main
`3f31cad1851b7ac7bfa08a4cb2bab8f9850547b8`, exactly equal to source current
main. Source has 312 heads, 68 tags and 513 pull refs; its 25 forks remain outside
the bounded universe. No unique code, attribution to the fork owner or capability
ID is warranted.

## Queue order 9 — Awesome Medical AI

`reacher-z/awesome-medical-ai` main is a source ancestor six commits behind.
Branch `add-dilran-20260815` SHA
`33731382811e2c81556d12d27e2a434b694b1f9c` exactly equals open source PR #2.
The only delta is one README catalog row linking to an external DILRAN repository
and badge. It is not DILRAN code, model, paper, data or validation. Source current
main still lacks the row.

The awesome list is CC0, but that does not relicense the linked DILRAN project.
The existing repository owner, PR user, raw Git identity, claimed represented
maintainer and external link owner remain separate identities; no person expansion
or mapping is inferred. The delta is DOC_ONLY and receives no Change/Feature ID.

## Evidence and persistence boundary

The seven-row ref reduction is
`deep-audit-batch-003-lineage-manifest.jsonl` (SHA-256
`3fa1fd75739c687da2ff65f6bb81dbf87738244a7223cf750854c31e38acbbdb`); the Kuan
twelve-Skill reduction is `deep-audit-batch-003-kuan-skill-manifest.jsonl`
(SHA-256 `a5d3f0f1662c23a4abb00a21b195b59100cbd4992b0335ad6c488b7f37958a2c`).
Primary evidence is `evidence-000163`–`evidence-000168`.

All findings are static. No third-party Skill, Python, shell, test, installer,
validator, DataLad command, BIDS updater, scientific model or external API was
executed. Current source projects and their out-of-scope fork networks were not
declared deep-audited; they were used only to resolve the seven bounded forks.
