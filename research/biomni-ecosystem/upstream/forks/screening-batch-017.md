# Public Fork Unique-Change Screening — Batch 017

Parent verification: `VERIFIED`. Scope: next 25 active unscreened REST forks.
One serialized GraphQL query returned all 30 branch refs without pagination.
Three new unique SHAs were compared serially with a two-second interval; all
comparisons succeeded. One omitted notebook patch was retrieved once through the
Contents API and inspected statically without executing cells.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000448 | polya20/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000447 | so2zhang/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000446 | lun-ai/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000442 | olachinkei/Biomni_Weave | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000441 | mshahbazq/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000690 | HelloWorldLTY/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000451 | RedTint/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000452 | tavangariz/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000623 | MintaYLu/Biomni | User | 3 | 1 | 1 | 0 | 1 | PR_LINEAGE_PLUS_SUPERSEDED_REGISTRATION_PROTOTYPE |
| repo-000455 | giacomoni/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000454 | europaroso/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000456 | liangli217/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000460 | catalyst-plus/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000458 | wx115/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000457 | Treywea/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000461 | satchellhong/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000465 | Javkhaa/Biomni | User | 2 | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_BROKEN_VENV_ENVIRONMENT |
| repo-000464 | explcre/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000463 | GenBrainAI/biomni | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000462 | fengtang07/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000466 | morisy575/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000478 | stw2/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000467 | talhamehmood9299/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000498 | anngvu/Biomni | User | 3 | 2 | 0 | 0 | 1 | UPSTREAM_EQUIVALENT_CODE_PLUS_NOTEBOOK_BENCHMARK |
| repo-000470 | edsonmartins/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: DIVERGED_SUBSTANTIVE_BROKEN_VENV_ENVIRONMENT=1,
PR_LINEAGE_PLUS_SUPERSEDED_REGISTRATION_PROTOTYPE=1,
UPSTREAM_EQUIVALENT_CODE_PLUS_NOTEBOOK_BENCHMARK=1,
NO_UNIQUE_CHANGE=22.

## Substantive and lineage candidates

### repo-000623 — MintaYLu/Biomni

- `bioimaging-registration`: one ahead / 157 behind, four files. Adds an 825-line
  SimpleITK registration module, 294-line schemas, registry import, and a renamed
  installer that adds unpinned SimpleITK. It exposes rigid, affine, deformable, and
  batch registration helpers with preprocessing, transforms, metrics, saved images,
  plots, and transform files.
- The implementation is defective: “rigid” starts from a generic identity transform;
  B-spline construction uses physical dimensions instead of mesh size; documented
  `number_of_control_points`, `amoeba`, and `normalized_correlation` paths disagree
  with code; schema defaults differ from implementation; correlation is duplicated;
  failures can be silently converted to zero metrics or empty visualization lists.
- There is no dimension/geometry/orientation validation, image mask, multiresolution
  strategy, deterministic sampling, convergence/deformation QA, label-safe
  interpolation, resource bound, test, or declared package dependency. Arbitrary
  input/output paths, fixed overwrite names, full-array copies, and the erroneous
  mesh expose filesystem and denial-of-service risk.
- This is not clinically validated registration. It lacks target-registration
  error, overlap/surface metrics, inverse consistency, Jacobian/fold checks,
  modality/scanner validation, PHI controls, access policy, metadata removal, or
  human-review boundaries.
- Local upstream evidence establishes a later same-author registration commit
  `d811aba...` in merged PR #207. It integrates the same four helper names into
  `bioimaging.py` and corrects major transform construction. The observed fork
  `bioimaging` head is already upstream-known. This earlier branch is retained as a
  historical substantive prototype but is superseded and not an integration target.
- The fork's `main` at `0be92e19...` is exact closed-unmerged PR #158 for nnU-Net
  segmentation; it is a separate exact PR surface and receives no duplicate change.
- Raw author `Minta <mintalu6@gmail.com>` matches the later canonical author tuple,
  but is not silently mapped to the `MintaYLu` account.

### repo-000465 — Javkhaa/Biomni

- `replace_conda`: one ahead / 153 behind, seven files and 1,287 added lines. It
  adds a pip/venv setup, privileged OS installer, split requirement lists, and
  generated activation/PATH files. Existing conda files remain, so this is an
  additive alternative, not an actual repository-wide conda replacement.
- The system installer mutates apt/dnf/yum/Homebrew state, may install EPEL, runs a
  fetched Homebrew installer without digest verification, and tolerates individual
  failures. The setup then upgrades pip, installs 84 mostly unpinned Python
  packages, runs existing R/CLI installers, and can still report success after
  partial failure.
- Biomni itself is never installed. Python 3.8 is accepted despite the Python 3.11/
  NumPy 2.1 stack; PyMC3 and other compiled packages are incompatible or highly
  platform-sensitive. `import biopython`, `community`, BLAST checks, macOS
  `ldconfig`, and custom venv-name handling are incorrect.
- Paths resolve from caller CWD, so same-named attacker-controlled requirement or
  installer files can be consumed. Generated shell files embed absolute author-
  machine paths and unsanitized user-controlled values, prepend downloaded tools to
  PATH, and can persist shell metacharacters for later execution.
- There is no lock, hash, SBOM, isolated R/CLI environment, idempotent update,
  complete platform matrix, or dependency/license inventory. The change shifts
  conda problems into host ABI and pip build problems, and is weaker than the
  already recorded sszhu micromamba/uv environment candidate.
- The owner and author are the same `Javkhaa` User account. Retain as a historical
  environment attempt, but reject wholesale integration and do not run/source it.

### repo-000498 — anngvu/Biomni

- Four ahead / 194 behind. Three code files modify Synapse defaults and entity-aware
  downloads; the tip adds `tutorials/synapse_demo.ipynb`.
- Parent verification proves the final blobs of all three code files are exactly
  identical to upstream commit `5f540c25587474444ea7c14953001d98f088b19d`
  (`Optimize tools`) by the same author. Those fork commits are a merged/squashed-
  equivalent code surface and are not allocated another change.
- The code changes themselves are risky: dataset becomes the silent default for
  search/download, project search guidance is removed, entity type is free-form,
  multi-ID behavior is restricted, dataset IDs enter query text, paths are
  unconstrained, and the Synapse token is passed in subprocess argv. Useful
  entity-aware validation intent should be redesigned against current PR #173/#209
  lineage rather than cherry-picked.
- The notebook blob is 372,124 bytes with nine cells, five executed code cells and
  15 stored output blocks. It reports only that `SYNAPSE_AUTH_TOKEN` is set—not its
  value—but also exposes `.env` loading, `/home/avu/...` paths, Synapse IDs, file
  storage metadata, individual/specimen/sample identifiers, complete prompts,
  generated code, errors, traces, response tables, and model configuration.
- Stored runs download and analyze cutaneous-neurofibroma clinical/tumor files and
  newly released proteomics/phosphoproteomics. Successful authenticated access does
  not prove redistribution or commercial rights; entity-specific Synapse access,
  citation, consent, human-data, and derivative-output terms are not persisted.
- Scientific claims are not benchmark-grade. Treatment conclusions use tumor-level
  observations nested within participants without a documented control/model;
  “significant efficacy” and heterogeneity are overstated. The proteomics run has
  duplicated columns, repeated exceptions, effectively one WT sample, unclear
  biological groups, fragile slicing, multiple hypothesis and pseudo-replication
  concerns, then promotes pathways, biomarkers, and therapeutic targets as novel
  without cohort metadata or external validation.
- Retain only the notebook tip as a quarantined `BENCHMARK`/tutorial change. A clean
  derivative must remove outputs and identifiers, use public version-pinned data,
  document terms and ground truth, freeze model/query settings, define scoring and
  failures, prevent leakage, and add statistical/domain review. `anngvu` already
  belongs to P and receives attribution without a duplicate person ID.

## Non-substantive findings

- Twenty-two repositories expose only upstream-known heads.
- No other new dependency, documentation, personal-config, or previously screened
  branch heads occur in this batch.

## Identity boundary

- Existing people MintaYLu and anngvu gain their relevant fork surfaces; no duplicate
  person IDs are created. Raw Minta author identity remains separate from the owner.
- New substantive User owner/author Javkhaa enters P.
- Upstream-only fork owners and the GenBrainAI Organization do not enter through
  this batch.

## Evidence

- Authenticated GraphQL branch/owner inventory for 25 repositories and 30 refs.
- Three serialized successful comparisons against frozen main, separated by two
  seconds; local resolution identified exact PR #158.
- Exact Git blob comparison proves anngvu's three code files equal upstream
  `5f540c2`; one serialized Contents API request retrieved the exact notebook blob.
- Function/timeline/authorship evidence places Minta's prototype before the later
  merged PR #207 registration implementation. This supersession relation is an
  inference; it is not claimed as patch identity.

## Next action

Continue the next bounded active-fork batch. Retain three changes and two lineages
for medical-imaging correctness, environment security, Synapse privacy/terms,
benchmark validity, provenance, license, and feature decomposition.
