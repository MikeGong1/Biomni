# SciAgent-Skills static deep audit

Observed at: `2026-08-23T15:33:49Z`

## Canonical decision

- Repository: `jaechang-hits/SciAgent-Skills` (`repo-002881`)
- Immutable default head: `a0aac0f4576a550d5316baf6da3d72e53408b3a2`
- Audit status: **DEEP_AUDITED — STATIC_ONLY**
- Functional/scientific validation: **FAILED / NOT EXECUTED**
- Benchmark fidelity: **FAILED**
- Integration disposition: **REJECT ALL 203 AS-IS; preserve 125 clean-room leads,
  78 no-near-term-candidate entries**

The repository is an instruction corpus, not a callable scientific implementation.
`DEEP_AUDITED` records closure of the bounded public Git/PR/fork/file surface and
line-by-line static processing. It does not mean any Skill, code example, API,
model, database, analysis, clinical action, robot protocol, or benchmark was run
or scientifically verified.

## Acquisition and full coverage

Serialized GitHub acquisition exhausted:

- forks: page 1 = 34, page 2 = 0;
- pulls (`state=all`): page 1 = 39, page 2 = 0;
- releases: page 1 = 0, page 2 = 0;
- public source branches: 10; tags: 0.

The source mirror passed `git fsck`. Default main has 140 commits; the 10 public
heads have a 143-commit union. The current recursive tree has 327 tracked files.
Every file was covered by non-overlapping static tasks:

- 203 current `skills/**/SKILL.md` files, 94,819 lines;
- 85 current ancillary reference/script/resource files under `skills/`;
- 39 remaining repository files, including registry, plugin, tests, scripts,
  templates, lockfile, workflows, integration templates, legacy Skills and the
  repository-local Skill creator.

There are 208 tracked `SKILL.md` files in total: 203 active, four legacy, and one
repository-local creator. No third-party instruction was followed and no repository
code, test, installer, workflow, model, API, or hardware path was executed.

The machine-readable per-Skill result is
`sciagent-skill-audit-manifest.jsonl` (203 rows; SHA-256
`eb5c2f282f9243a8bfe4628d50d9405fa7d282d975fe0047a8e519851dd8392e`).
The fork result is `sciagent-fork-audit-manifest.jsonl` (34 rows; SHA-256
`5b5ed42396e0defda73d81208b94b7ea79baccf73d9a5ab545a4919faafa2911`).

## Current inventory and discovery contradictions

Registry and filesystem agree on 203 active Skills:

| Subtype | Count |
|---|---:|
| toolkit | 72 |
| database | 53 |
| pipeline | 40 |
| guide | 38 |

Category counts are 64 genomics-bioinformatics, 30 structural/drug, 30 scientific
computing, 24 scientific writing, 11 systems/multiomics, 10 proteomics, 8 data
visualization, 7 cell biology, 7 medical imaging, 5 lab automation, 4
biostatistics, and 3 molecular biology.

Public installation surfaces disagree:

- README badge/text says 199; its category rows sum to 198;
- plugin and integration metadata say 197;
- plugin paths omit the entire seven-Skill `medical-imaging` category and expose
  only 196 active Skills;
- registry and filesystem are the only internally consistent 203/203 surfaces.

Consequently the plugin cannot be described as a complete installation of the
current registry.

## Skill-level static decisions

All 203 are `REJECT AS-IS`. “Candidate” below means only a requirements/reference
lead for clean-room reimplementation after current upstream documentation,
licensing, scientific review, sandboxing and tests are established.

| Audit partition | Skills | Clean-room leads | No near-term candidate |
|---|---:|---:|---:|
| genomics-bioinformatics | 64 | 54 | 10 |
| scientific-computing + biostatistics + visualization | 42 | 21 | 21 |
| writing + lab automation + imaging + cell biology | 43 | 18 | 25 |
| structural biology + drug discovery | 30 | 17 | 13 |
| proteomics + systems/multiomics + molecular biology | 24 | 15 | 9 |
| **Total** | **203** | **125** | **78** |

A repository-wide lexical risk screen found 173 Skill files with install/shell/
clone/execution language, 68 with credential or secret-handling language, and 15
with physical hardware/lab-automation language. These are discovery counts, not
proof that every matching line is exploitable; the per-Skill manifest contains the
audited disposition.

## Representative scientific and clinical failures

### Genomics and bioinformatics

- gnomAD calls an approximately `5.5e-38` pLI “very high” even though pLI is on
  [0,1]; the displayed value instead indicates almost no pLI evidence.
- JASPAR treats a PFM as position-keyed data, uses an incorrect maximum-score
  calculation, and scans only one strand.
- VCF guidance treats caller-specific QUAL as a universal single-variant error
  probability and promotes a global `QUAL>=30` rule.
- Scanpy uses a fixed `<5000 genes` doublet heuristic; featureCounts infers
  strandedness from whichever of three count modes gives the highest assignment
  rate. Neither is a sound general decision rule.
- COSMIC examples encode plaintext email/password into Basic authentication and
  rely on an unfrozen REST contract.

### Statistics, computing, and visualization

- `statistical-analysis` silently chooses tests with invalid universal cutoffs;
  scikit-survival examples misstate cumulative-incidence return contracts.
- Seaborn `standard_scale` is called a z-score; matplotlib guidance invents fixed
  significance notation; several visualization Skills convert editorial choices
  into scientific conclusions.
- The 3Dmol generator interpolates title/subtitle and `</script>`-capable molecular
  text into HTML, then loads unversioned remote JavaScript without SRI/CSP.
- NEB/IRC can pass without a valid trajectory and relies on a single-barrier
  heuristic; setup downloads an unchecked xTB archive and performs mutable package
  installation.
- HypoGeniC adapts to validation results; PyHealth lacks PHI/DUA/external-
  validation boundaries; model/transformer recipes omit weight/license/data
  provenance and can turn generated text into claimed scientific fact.

### Writing, imaging, cell biology, and lab automation

- `clinical-decision-support-documents` labels a home-grown 1A–2C hierarchy as
  official GRADE and uses it in treatment-recommendation output.
- Western-blot normalization uses `PSMAD2/(SMAD2/GAPDH)`, multiplying GAPDH back
  into the result rather than implementing the stated normalization.
- Pydicom's claimed Annex E anonymization removes only a small tag list and omits
  private tags, nested sequences, dates, burned-in pixels, free text and UID
  consistency.
- Opentrons and PyLabRobot contain executable PCR, magnetic-bead, dilution and
  cherry-pick protocols without required calibration, liquid-class, collision,
  biosafety, waste or operator-approval gates.
- Scientific manuscript guidance claims eight missing reference/asset files;
  image/tracking recipes include contradictory Cellpose thresholds, questionable
  Trackpy APIs and destructive 16-bit→8-bit normalization.

### Structural biology and drug discovery

- Docking scores from Vina/smina are repeatedly treated as binding energy,
  affinity, and ranked “hits,” although they are empirical scoring functions.
- DrugBank prose invents severity/risk scores; FDA label examples treat label
  records as NDA/ANDA approval/year evidence; Open Targets Phase 4 is treated as
  proof of approval; UniChem DrugBank presence is mislabeled “approved.”
- DailyMed coverage is generalized to all FDA-approved drugs and suggested for
  clinical/EHR integration; DDInter research entries become “avoid/safe” actions.
- Commercial/cloud routes such as Rowan omit spend confirmation, compound-IP
  privacy, service terms and internally consistent SDK/API evidence.

### Proteomics, systems biology, and molecular biology

- The sgRNA guide cannot parse its bundled CSV and calls 119 dataset links plus
  119 summary links “238 datasets.”
- PyOpenMS treats an arbitrary score as a 1% q-value; MaxQuant's default
  imputation+t-test workflow can systematically inflate false positives.
- KEGG licensing is misrepresented, and its ORA/GSEA behavior is incorrectly
  described; BRENDA combines medians from unrelated experiments into a fictitious
  kinetic pair and models plaintext password handling.
- CellChat/MOFA/Muon/omics guides contain pseudoreplication, confounding or
  unreliable statistical heuristics; libSBML disables unit checking and still
  claims validation.
- Paid/cloud sequence submission and ESM inference lack explicit approval, cost,
  sequence privacy/IP, weight-license and biosafety boundaries.

## Registry, scaffolder, security, and provenance

- Structural tests count sections, list items, code fences and URLs; they do not
  parse/run examples, verify APIs, test scientific claims, check source versions,
  or validate license applicability. Calling Skills “validated” is therefore
  misleading.
- The scaffolder interpolates description/license into YAML without safe
  serialization, can inject frontmatter/registry fields, writes before validation,
  is not lock/interrupt safe, and treats missing `pixi` as validation success.
- The registry validator does not require its full documented schema, reject
  unknown keys, resolve/confine paths, or reject symlinks. Consumers then read the
  registry-provided path.
- `.env` is not ignored. Blind evaluation searches repository, home, `~/work` and
  current-directory `.env` before using ambient AWS credentials; exceptions can be
  persisted without redaction.
- Installation guidance uses mutable clones/plugin state and `curl | bash`; CI
  actions use tags, not immutable SHAs; helper scripts download unsigned/unhashed
  binaries or remote JavaScript.

No live secret was found in the frozen tree. The risk is the credential-discovery
and execution pattern, not a detected production token.

Root content is described as CC-BY-4.0, but every Skill frontmatter instead names
an upstream software/database/service license. Across the corpus those values span
CC, MIT, BSD, Apache, GPL/LGPL/AGPL, proprietary, unknown, and service-specific
restrictions. They do not prove the prose/example license, model/data/API terms, or
right to relicense migrated content. Of 69 Skill reference files, 54 say they were
condensed from original material and 46 of those contain no source URL. File-level
origin revision, hash, modification notice and attribution remain unresolved.

## Benchmark and evaluation fidelity

The public “92.0% BixBench-Verified-50” and +26.7-point claims are not reproducible
from this repository. The only benchmark artifact is a PNG relabeled in README;
the image itself identifies `OmicsHorizon` and says six systems are compared from
public reports. There is no task set, per-item output, scorer, model/runtime config,
log, source snapshot or same-protocol ablation.

`blind_test_results.csv` is a separate, non-BixBench experiment:

- 140/203 current Skills (68.9655%) are represented;
- 139 are `MUST_KEEP`, one `KEEP`, none `REMOVE`;
- 102 have score zero and 89 explicitly say “no answer found”;
- the judge receives no gold answer or Skill content;
- the narrow answer parser loses common formats, and judge-JSON parse failure is
  converted to score zero and then `MUST_KEEP`;
- raw answers, per-question scores, request metadata, temperature, timestamps,
  seeds, model IDs and judge responses were not preserved.

This evidence cannot measure Skill value, justify removals, or support BixBench
claims.

## Source branch and PR normalization

All 39 PRs and 140 main commits were normalized. PR status is 36 merged, two
closed-unmerged, one open. Sixteen use true merge commits and 20 use squash/
rebase-style integration; 92/140 main commits map to cached PR evidence, and 48 do
not. Forty-nine stable patch-equivalence pairs prevent main/PR double-counting.

Canonical change sets:

- `change-000081`: current 203-Skill main library plus registry/authoring/
  evaluation infrastructure, preserving its 140-commit history and 36 merged PR
  surfaces as one composite pending Phase 10 feature decomposition;
- `change-000082`: closed-unmerged PR #22 adding OmniPath and pypath knowledge-
  graph Skills; useful lead but API/data-license/runtime claims are unverified;
- closed PR #36 is a docs-only DESeq2 rule on the old path and is explicitly
  superseded by merged PR #37; indexed in lineage but no substantive change ID;
- `change-000083`: open PR #39's ZINC22/CartBlanche migration, still unmerged and
  requiring live API/terms validation;
- `change-000084`: unassociated organism-aware variant-calling branch, one commit
  and two files, requiring reference/annotation/caller correctness review.

`lineage-000031` records merge, squash/patch identity, historical supersession,
open and unassociated branch relations without treating Git surfaces as separate
features.

## Public fork normalization

All 34 public forks (`repo-007589`–`repo-007622`) and all 86 public heads were
processed; no tag exists. Twenty-eight forks are stale/historical with no unique
commit, one is an exact current sync, and two contain only already-merged PR
lineages. Five forks expose 21 unique heads with 56 commit occurrences; duplicate
ancestry reduces these to 55 distinct SHAs. Seventeen heads are exact cached
merged-PR heads and are not new changes.

Four remaining groups are:

1. `change-000085`: `emoeller80281` NEB/IRC branch, five-commit alternate/later
   visualization variant with eight changed paths. It is not identical or ancestral
   to merged PR #44 and retains the current NEB scientific/supply-chain blockers.
2. `change-000086`: `emoeller80281` main, seven commits that remove many Skills,
   compress descriptions and prune registry/plugin surfaces across 249 changed
   files (315 path endpoints). It is a deployment-size curation alternative, not a
   scientific capability, and is rejected as-is.
3. `8c23ac3d23d1789a0cd245c24452478075237ffc`: `pors` README-only Paperzilla
   mention. It is indexed `DOC_ONLY/OUT_OF_SCOPE_DEPENDENCY_LEAD`, with no change
   or person ID.
4. `change-000087`: `wonho-hits` KFold Skill plus registry entry. The Skill calls
   absent `biomni.tool.k_fold`/Modal deployment files, sends sequences/ligands to a
   cloud A100 service, and lacks code/model-weight/license/privacy/cost evidence;
   reject as-is and retain only an out-of-scope dependency lead.

`lineage-000032` records these groups and the 17 exact PR lineages. An independent
fork verifier reproduced 34/86/55 counts and the same four groups after an initial
fork worker normalization bug was identified and corrected.

## Candidate direction

No formal Feature or Implementation ID is allocated in Phase 8. The useful output
is a bounded set of clean-room leads:

- a strict, hashed, versioned Skill registry with file-level provenance/license;
- a transactional, safely serialized, fail-closed scaffolder and scientific lint
  tiers beyond structural checks;
- carefully selected read-only database adapters with current schemas/terms,
  privacy controls and rate limits;
- typed genomics/statistics workflows with explicit design assumptions,
  deterministic tests, references and error states;
- sanitized local visualization components with no remote mutable code;
- selected modeling wrappers only after model/data/license/compute validation and
  a no-clinical-decision boundary.

Do not copy the 203-Skill corpus wholesale, install it as an agent instruction
bundle, repeat the 92% benchmark claim, or treat frontmatter licenses as provenance.

## Evidence boundary

Primary records are `evidence-000151` through `evidence-000157`. Static coverage
is complete; runtime/API/scientific/license validation is not. The two manifests
are canonical compact reductions of larger temporary worker reports whose hashes
are recorded. Owners discovered only through external forks were not added to the
people universe.
