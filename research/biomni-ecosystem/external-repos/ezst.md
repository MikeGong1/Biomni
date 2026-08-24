# QING1105/ezST static deep audit and PR #330 lineage

Observed at: `2026-08-23T14:12:07Z`

## Canonical decision

- Repository: `QING1105/ezST` (`repo-003211`)
- Immutable head: `427792f0bbf2564dbf124b4444ffdb07cc400a25`
- Audit status: **DEEP_AUDITED — STATIC_ONLY**
- Runtime/scientific status: **NOT VERIFIED; multiple source-level contradictions**
- Integration disposition: **REJECT AS-IS; selective clean-room design only**
- Lineage decision: **derived functional descendant of open Biomni PR #330, not
  an independent eleven-feature implementation, not an exact duplicate, and not a
  clean supersession**

`DEEP_AUDITED` records closure of the bounded static research surface. Repository
code, installers, dependencies, and analyses were never executed, as required by
the research security policy. The status does not assert scientific validity,
license clearance, safe execution, or integration readiness.

## Public-surface exhaustion

The source mirror has one public branch, `master`, at the audited head; no tag was
present. Its four commits form one linear chain. The current recursive tree has 36
entries: 16 trees and 20 blobs. All 19 text blobs were inspected; the remaining
blob is a 1254×1254 RGB PNG. Across all four commits, the reachable Git object set
contains four commits, 29 trees, and 29 blobs; all commit diffs and deleted or
superseded source surfaces were inspected. `git fsck --full` reported no broken or
unreachable object in the frozen source mirror.

Serialized REST acquisition used explicit `per_page=100` pages:

| Surface | Source pages | Terminal evidence |
|---|---|---|
| forks | page 1 = 1, page 2 = 0 | exhausted |
| pulls (`state=all`) | page 1 = 0, page 2 = 0 | exhausted |
| releases | page 1 = 0, page 2 = 0 | exhausted |

The only child fork is `Han-Z02/ezST` (`repo-007588`). It has only `master` at
`c45fc11fe846e46eaf3bc4929e94a6b1d33c8bb2`, no tags, PRs, releases, child forks,
or unique commit. Against source `master`, its merge base is its own head; it is
ahead 0 and behind 1. The owner is not added to the people universe because
external-repository forks do not expand `person_depth`.

## Git change decomposition

| Commit | Static change set | Canonical treatment |
|---|---|---|
| `d4de73d1dbc0640f480158a4bc5ffb04676c6a98` | Six Codex Skills, marketplace/plugin metadata, staged run→interpret→review protocol, documentation and logo; no runtime | unique staged-workflow wrapper (`change-000077`) |
| `ee9f332e025c79706785e1e8f307cc70f6373412` | Conda/Python/R installer and environment self-check | deployment support within `change-000077` |
| `c45fc11fe846e46eaf3bc4929e94a6b1d33c8bb2` | Deletes Conda environment and switches to pip metadata; at this point `packages=[]` and no Python runtime exists | historical packaging refactor within `change-000077`; also exact child-fork head |
| `427792f0bbf2564dbf124b4444ffdb07cc400a25` | Adds the 2,620-line standalone runtime, exports eleven functions, changes coordinate loading, and extends empty scaffold directories | PR-derived standalone runtime plus unique loader/package delta (`change-000078`) |

The five stage-specific Skills are unchanged from the root commit through HEAD;
only the orchestrator Skill later changes for installation/environment guidance.
Packaging commits are not counted as new scientific features.

## Biomni PR #330 derivation and deduplication

Live primary evidence still showed PR #330 open and unmerged at the observation
time:

- base: `snap-stanford/Biomni main@400c1f366b96a35ca253e13c9b06c5076af41d65`;
- feature commit: `27e75f2359254b7308117a316522f26c61bd190a`;
- head after pre-commit formatting: `ef75a199f4786704520bd16a4bce4da0ad2ef4ee`;
- author/source: `QING1105`, branch `feat/spatial-transcriptomics-tools`;
- five changed files, 2,655 additions, no deletion.

PR #330 introduces the Biomni-native `spatial_transcriptomics.py`, eleven tool
descriptions, registry wiring, and Python/R installation surfaces. Its functional
commit predates the ezST root by about one hour and 45 minutes; the ezST root README
explicitly says Biomni supplies the same eleven functions.

The PR runtime has 2,076 lines and the ezST runtime 2,620 physical lines. Both
contain the same ordered set of 14 top-level definitions: eleven public functions
and three helpers. A no-index diff ignoring all whitespace and blank lines reported
162 additions and 82 deletions. The independently computed delta patch ID under
the recorded ignore-at-EOL/blank-line predicate is
`3cedea02d5ee5bd86c8d4a99b30b9b4e2a5a55a1`. Most differences are coordinate
loading, gene-symbol choice, Python-compatibility/formatting, and empty project
scaffolds; the gzip, DestVI, R interpolation, CellChat, and stage-contract defects
are inherited.

There is no cross-repository Git ancestry, so `derived_from` is a high-confidence
`INFERENCE`, not an ancestry `FACT`. It is supported jointly by authorship and
chronology, the root dependency statement, exact definition-set identity, and the
function-body diff. The scientific core is normalized as `change-000076`; the
unique Skills/package layer and derived standalone delta are `change-000077` and
`change-000078` within `lineage-000029`.

## Current capabilities

The package exports eleven user-facing functions:

1. project scaffolding;
2. h5ad, 10x-directory, and wide-CSV loading plus coordinates;
3. spot QC;
4. total-count normalization/log transform/HVG selection;
5. PCA/neighbors/UMAP/Leiden clustering;
6. coordinate-graph Leiden domains;
7. Moran's I spatial-gene ranking;
8. SPOTlight deconvolution through a generated R bridge;
9. DestVI deconvolution;
10. CellChat through a generated R bridge; and
11. Squidpy neighborhood enrichment.

The distinct ezST contribution is the five-stage conversational workflow: each
stage asks an agent to run tools, interpret plots/results, stop, and wait for an
explicit `通过`, `调整`, or `跳过` decision. This is a useful clean-room UX pattern,
but prose gates do not correct the underlying data, scientific, or execution
defects.

## Blocking correctness and scientific findings

### Data ingestion and QC

- In `load_visium_data`, gzip discovery changes only loop-local `f`; `mtx`, `feat`,
  and `bar` remain uncompressed paths. A standard compressed 10x directory can
  therefore be rejected or read from nonexistent paths.
- The ezST-only headerless coordinate rewrite selects the first two numeric
  columns. For standard six-column Space Ranger positions these are `in_tissue`
  and `array_row`, not pixel x/y. A fully numeric first row can also be discarded
  as a header. When barcodes are missing after filtering, the code warns and then
  still indexes all AnnData barcodes, which can raise `KeyError`.
- Wide CSV creates dense `X`, while gene plotting calls `.X.toarray()` without a
  dense fallback.
- QC recognizes only uppercase human-style `MT-`, not common mouse `mt-` genes.
  Skill defaults (`500/250/20`) differ from function defaults (`200/20/20`), and
  the promised pre/post and spatial QC plots are not produced.

### Spatial statistics

- `identify_spatial_domains` runs Leiden only on a coordinate graph and never uses
  expression. Its result is a geometric graph partition, insufficient by itself
  for the claimed molecular tissue-domain interpretation.
- Moran's I is computed only for `var_names[:2000]`, despite logging all genes;
  the first 2,000 arbitrary columns are not an HVG/statistical universe, and the
  output is ranked by I without a multiple-testing decision rule.

### Deconvolution and downstream contract

- `normalize_visium` saves counts in `.raw`, but DestVI does not recover spatial
  `.raw`; it casts the normalized/log-transformed `X` directly to `int32` and uses
  it as counts. The recommended S2→S4 path can therefore train on truncated values.
- SPOTlight writes `barcode` as the final CSV column, but Python reads column zero
  as the index, losing the first cell-type column as data and leaving barcode as a
  nonnumeric column.
- Both deconvolution paths output proportions CSV/plots only. Neither writes the
  “deconvolved h5ad” required by S5, and continuous proportions are not the
  categorical `obs[cell_type_key]` consumed by neighborhood enrichment/CellChat.
- `_plot_proportions` draws global means and the first 20 spot bars; it does not
  use coordinates and does not create the advertised spatial proportion maps.
- Neighborhood enrichment assumes `obs[cell_type_key]` is already categorical;
  ordinary string/object labels can fail at `.cat.categories`.

### CellChat

Coordinates are attached only as a Seurat dimensional reduction. `createCellChat`
is not created with a spatial datatype/coordinate contract, and
`computeCommunProb` receives no distance/spatial restriction. The implementation
does not support its “spatially proximal” claim. It writes two CSVs and one circle
plot, not the advertised saved CellChat object, heatmap, bubble plot, or summary
artifact.

## Security, privacy, and supply chain

- Both R bridges generate source code by interpolating caller-controlled paths,
  `cell_type_key`, output paths, and other values. `species` is inserted unquoted
  into `CellChatDB.{species}`. The generated file is then executed with
  `subprocess.run`; `shell=True` is absent, but R-source injection remains possible.
- The caller also chooses the `Rscript` executable path and unrestricted input and
  output paths. Bridge directories retain raw expression matrices, barcodes, cell
  labels, and coordinates after the temporary R script is deleted. No patient/
  confidential-data minimization, retention, access, provider, or consent policy
  exists.
- No literal credential, HTTP upload client, dynamic Python evaluation, or
  `shell=True` was found in the current runtime.
- Python/R dependencies have no lock, artifact hash, upper bound, or SBOM.
  CellChat is installed from a mutable GitHub default branch. Several declared
  Python dependencies are unused by the runtime.
- The README's “published” command `pip install ezST` is definitively unsafe for
  this project: the case-normalized PyPI name `ezst` belongs to unrelated package
  version 0.3.44, authored by `aiacademy`, summarized as “ai library for
  education,” and linked to `ezstkr/pypi_ezst`. That command installs the other
  project, not QING1105/ezST. This is a wrong-package/name-collision supply-chain
  risk; it is not evidence that the name owner acted maliciously.

## Packaging, tests, license, and provenance

- `pyproject.toml` and plugin manifest say 0.1.0, while `ezst.__version__` says
  0.2.0. Plugin URLs point to nonexistent branch `main`; only/default `master` was
  observed. `ezst.visium_new_platforms` is advertised but absent.
- Setuptools packages only `src/ezst`. Plugin, Skills, installers, and marketplace
  data sit outside that package tree, so the package-data glob does not establish
  that a wheel contains the advertised Codex plugin. There is no console entry
  point, MCP/tool server, or runtime registration binding Skills to the functions.
- Historical `install/requirements.txt` still refers to a deleted
  `environment.yml`; two Skills refer to nonexistent
  `install_r_packages_spatial.R`. Project scaffold paths conflict with Skill output
  paths.
- No test, fixture, CI workflow, lockfile, tag, or GitHub release exists. PR #330's
  claim of validation on GSE246011 has no committed result/test artifact in the
  audited change set.
- README, metadata, and Skills say MIT, but no root LICENSE text exists and GitHub
  reports no detected license. The highly derived PR code was publicly offered in
  an Apache-2.0 Biomni fork, while ezST provides no attribution/relicensing note.
  Same-author ownership may permit dual licensing, but the public evidence does
  not prove rights or scope. Canonical status remains `LICENSE_UNCLEAR` and
  `PROVENANCE_RELICENSE_UNRESOLVED`.

## Normalized candidates and disposition

No formal Feature or Implementation ID is allocated before Phase 10 normalization.
Candidate families are preserved without double-counting:

| Candidate | Source lineage | Biomni baseline | Disposition |
|---|---|---|---|
| staged Visium run→interpret→human-review workflow | ezST Skills | no dedicated state machine found | clean-room UX candidate |
| Visium loading/QC and standard Scanpy clustering | PR #330 core; ezST derived delta | no dedicated tool found; Scanpy exists | typed native wrapper after redesign |
| coordinate-graph domains and Moran SVG | PR #330 core | Squidpy dependency exists | redesign scientific contract and statistics |
| DestVI/SPOTlight deconvolution | PR #330 core | scvi-tools exists | reject current implementation; typed clean-room adapters |
| neighborhood enrichment | PR #330 core | Squidpy exists | discrete-label adapter after validation |
| spatial CellChat | PR #330 core | no dedicated tool found | reject; implement real spatial model and safe bridge |
| packaging/install/scaffolding | ezST | Biomni already has environments | not an independent Feature |
| Visium HD/Xenium/Atera/velocity | comments/empty directories only | N/A | no implementation; do not create a candidate |

The current repository and PR are evidence sources, not integration sources. Do
not cherry-pick or copy. Preserve the staged-review concept and method choices as
clean-room leads; redesign data contracts, safe parameter transfer, statistics,
privacy, dependency pinning, and tests before any future integration proposal.

## Evidence boundary

Primary evidence is `evidence-000141` through `evidence-000143`. No code was run,
so dependency API compatibility, build/install success, runtime outputs, and
scientific performance remain unverified. This uncertainty is an implementation
status, not an unprocessed public-source surface. The child fork adds no unique
change, and no out-of-scope person was added.

An independent verifier passed refs/object integrity, REST pagination closure,
fork closure, current-text coverage, and the PR #330 derivation, but recommended
keeping `PARTIAL` because runtime/scientific/license validation was not complete.
The parent resolved that status disagreement by the authoritative research scope:
third-party execution is prohibited in this phase, and `DEEP_AUDITED` measures
bounded static coverage rather than implementation verification. The verifier's
integration-readiness failure is retained in every separate blocker status above.
