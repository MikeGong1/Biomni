# Public Fork Unique-Change Screening — Batch 026

Parent verification: `VERIFIED`. Scope: next 25 active unscreened fork
identities. One serialized authenticated GraphQL query resolved all 25
repositories and returned all 28 branch refs without pagination: 27 upstream-
known heads and one new SHA. One serialized compare and one immutable blob request
retrieved the complete one-commit, nine-file Docker/uv change and its omitted
294,528-byte lock file. No image, script, dependency, package, notebook, or test
was executed.

## Coverage and classifications

| Repository ID | Fork | Owner type | Branches | Upstream-known | Exact PR heads | Reused heads | New heads | Screening status |
|---|---|---|---:|---:|---:|---:|---:|---|
| repo-000624 | loseruser0/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000691 | lilleswing/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000693 | ZY-JLU/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000692 | bennyyu786/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000701 | jucor/Biomni | User | 2 | 2 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000726 | parsaghaffari/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000720 | leoisl/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000707 | DenverN3/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000706 | lihqi/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000703 | tahabi09/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000702 | d1on/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000699 | wowtqt/Biomni-bio-aiagent | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000698 | arianpasquali/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000696 | realzhukaihua/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000695 | mpckkk/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000728 | standardmodelbio/Biomni | Organization | 2 | 1 | 0 | 0 | 1 | DIVERGED_SUBSTANTIVE_DOCKER_UV_MIGRATION_BLOCKED |
| repo-000729 | tahoebio/Biomni-tahoe-fork | Organization | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000727 | throwoutofcoffeeexception/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000724 | jamesthesnakegatech/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000723 | varunkothamachu/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000722 | evelynmitchell/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000721 | vaalessi/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000718 | abuchin/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000717 | gmfc/biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |
| repo-000716 | manussun/Biomni | User | 1 | 1 | 0 | 0 | 0 | NO_UNIQUE_CHANGE |

Classification counts: NO_UNIQUE_CHANGE=24 and
DIVERGED_SUBSTANTIVE_DOCKER_UV_MIGRATION_BLOCKED=1.

## Retained historical change

### repo-000728 — standardmodelbio/Biomni

- `feat/docker-uv-migration@ed3dd5f...` is one ahead / 476 behind with merge
  base `675a128...`. It adds full/minimal Dockerfiles and compose profiles,
  Docker documentation, ignore rules, a new pyproject, and an exact uv lock. This
  is one connected environment change, not nine separate features.
- The lock is a real positive artifact: Python is constrained to 3.11, 194
  packages are resolved, 193 use the HTTPS PyPI registry, distributions carry
  hashes, and the local Biomni package is editable. Its 24 direct runtime
  dependencies match the lock root; all 826 recorded Python artifact URLs have
  SHA-256 values. No Git or plaintext-HTTP package source appears in the lock.
- The build wiring defeats that benefit. `.dockerignore` excludes `uv.lock`, while
  both Dockerfiles copy `uv.lock*` and then execute `uv sync --frozen`. A lock
  excluded from the build context cannot satisfy that contract; the builds are
  expected to fail at COPY or frozen sync rather than reproduce the locked graph.
- The full image creates its project and `.venv` under `/app`, but both full compose
  services bind-mount the host checkout over `/app`. This hides the image-built
  environment. `/app/.venv/bin` is not put on PATH, and the interactive service
  starts plain `/bin/bash`; `uv run` can instead rebuild against mutable host files
  at runtime. The image is not the immutable execution unit the documentation claims.
- The minimal Jupyter service publishes port 8888 on all host interfaces, listens
  on `0.0.0.0`, runs as root, explicitly sets an empty notebook token, receives
  Anthropic/OpenAI keys, has writable tutorial/data mounts, unrestricted outbound
  networking, and no CPU/memory/PID/disk limits or privilege reductions. Any
  reachable client can obtain root code execution in the container, read or alter
  mounted data, and use or exfiltrate keys. No Docker socket/device is mounted, so
  this is not automatically host-root, but the host mounts and secrets are critical.
- Full Jupyter also binds all interfaces, runs as root, receives keys, and mounts
  the entire repository/data read-write. It does not explicitly disable its token,
  so it must not be mislabeled unauthenticated; its risks remain broad exposure,
  secret availability, writable host state, and unconstrained code execution.
- `.dockerignore` does not exclude `.env` or `.env*`; a local credential file can
  enter `COPY . .` and persist in an image layer. Compose environment variables
  are readable by the code-capable process. No secrets mechanism, non-root user,
  read-only root, mount boundary, capability drop, health check, or network policy
  is supplied.
- Supply chain is not reproducible beyond Python artifacts: mutable base tags,
  unpinned apt packages, unpinned `curl | sh` uv installer, unpinned `pip install
  uv`, and floating CRAN installs remain. The unversioned Hatchling build backend
  is absent from the lock and can be resolved dynamically. The lock records package
  hashes but no transitive license/SBOM decision.
- The new pyproject/lock covers a narrow Python stack, not E1. It omits Torch,
  Biopython, Scanpy, AnnData, RDKit, rpy2, and many tool/CLI dependencies imported
  across Biomni. Full R installs only base R plus ggplot2/dplyr/tidyr; DESeq2,
  WGCNA, the full R script, and broader conda/CLI capabilities are absent. Claims
  that all conda dependencies were converted, all necessary R packages exist, or
  minimal builds complete in about 30 seconds are contradicted or unverified.
- No build, import, tutorial, Jupyter-auth, secret, resource, or multi-architecture
  test accompanies the change. The new pyproject says Apache-2.0 while surviving
  `setup.py` says MIT, creating package-metadata conflict. Repository licensing
  also does not settle base-image, uv, apt, CRAN, or PyPI obligations; those require
  an SBOM and license review.
- Preserve only the design concepts—container profiles and hashed Python locking.
  Reimplement on current main with lock-in-context checks, non-root isolated
  services, loopback/authenticated Jupyter, secret mounts, bounded resources,
  digest-pinned toolchains, explicit Python-only versus E1 matrices, and actual
  build/import/tutorial smoke tests. Do not cherry-pick this branch.

## Identity boundary

- The repository owner is an Organization and does not enter P. The sole substantive
  commit maps author and committer login `shaunporwal`; add that User account as a
  relevant fork-branch contributor without inferring additional real-world identity.
- Owners of the 24 upstream-only repositories do not enter through this batch.

## Evidence and limits

- Authenticated GraphQL inventory covered all 25 repositories and 28 refs with no
  pagination. One serialized compare recovered the exact nine-file delta; one
  serialized immutable-blob request closed the omitted `uv.lock` gap.
- Static inspection proves configuration contradictions and exposure settings.
  No Docker engine, package manager, registry, CRAN, Jupyter server, or third-party
  program was invoked.
- Conceptual overlap with other Docker/deployment candidates is not SHA, tree,
  blob, patch, or ancestry identity; no cross-repository derivation is claimed.

## Next action

Continue the next bounded active-fork batch. Retain one environment change and one
single-repository lineage for historical decomposition; direct integration remains
blocked by build correctness, exposure, dependency, supply-chain, and license risks.
