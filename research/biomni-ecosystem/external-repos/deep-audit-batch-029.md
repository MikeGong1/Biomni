# External repository deep audit — Batch 029

Observed at: `2026-08-24T06:26:56Z`

Status: **COMPLETE — STATIC-ONLY, DIRECT ADOPTION REJECTED**

## Scope and identity gate

- Stable queue orders: **1213–1262**.
- Canonical families: **50**.
- Canonical repository records: **51**.
- Exactly one representative was verified for every family; queue order, family key, role and member count round-trip to `database/repositories.jsonl`.
- Third-party code, notebooks, installers, workflows, models, containers and tests were not executed.

## Static acquisition and review method

Fork members were compared against the current source default branch through immutable GitHub comparison objects. Forks with no ahead commits close as source lineage. Unique fork blobs and independent repositories were inspected from immutable tarballs or Git trees, with bounded selected-blob fallback for very large artifacts. The review covered README and license text, dependency manifests and locks, workflows, notebooks as JSON, selected source text, data/configuration files, source/fork deltas, security-sensitive primitives, privacy/data-governance signals, reproducibility flags and repository-local licensing.

Pattern matches are triage signals, not proof of exploitability or scientific invalidity. Every implementation candidate remains rejected for direct adoption until manual semantic comparison, source-to-sink security validation, scientific-domain review, provenance verification and isolated runtime testing are complete.

## Result summary

| Result class | Families |
|---|---:|
| `DEEP_AUDIT_CANDIDATE` | 7 |
| `NO_UNIQUE_OR_SOURCE_LINEAGE` | 42 |
| `DOC_METADATA_MAINTENANCE_ONLY` | 0 |
| `NON_BIOMEDICAL_FALSE_POSITIVE` | 0 |
| `EMPTY` | 1 |

Static-review flags were present in 5 families for security-sensitive primitives, 2 for privacy/data-governance terms, and 4 for reproducibility or scientific-validation patterns. These counts are not severity scores.

## Family ledger

| Order | Bounded repositories | Result | Ahead commits | Code/doc/data files read | Principal disposition |
|---:|---|---|---:|---:|---|
| 1213 | `dabulseco/databook_matlab` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1214 | `yarikoptic/metadata-schema-zenodo` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1215 | `sbonner0/esm`, `Vik-u/esm` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1216 | `yarikoptic/bids-pydantic` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1217 | `yarikoptic/schemasheets` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1218 | `sphia-g/Biosensors` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1219 | `yarikoptic/zarr-specs` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1220 | `Mr-Milk/IMC-Analysis-Pipeline` | `DEEP_AUDIT_CANDIDATE` | 0 | 7/1/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1221 | `tangxuan82/Cardiac-Digital-Twin-Purkinje` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1222 | `yarikoptic/dandidav` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1223 | `yarikoptic/ome-ngff-validator` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1224 | `gutendzx/MIMO_DOA` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1225 | `yarikoptic/BENCHMARK-Metadata` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1226 | `yarikoptic/BrAinPI` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1227 | `Liripo/scPort` | `DEEP_AUDIT_CANDIDATE` | 0 | 8/1/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1228 | `changwn/CAR-Toner` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1229 | `yarikoptic/icn3d` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1230 | `yarikoptic/alphafold` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1231 | `yarikoptic/datalad-metalad` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1232 | `chaudhariatul/Grounded-SAM` | `DEEP_AUDIT_CANDIDATE` | 95 | 0/4/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1233 | `th86/pytorch_ehr` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1234 | `yarikoptic/moseq2-app` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1235 | `dabulseco/databook_python` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1236 | `yarikoptic/ontology-access-kit` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1237 | `andrewsu/Benchmarks` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1238 | `changwn/combinatorial_signaling_motif_libraries` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1239 | `DevinDeSilva/DruggableProtienPrediction` | `DEEP_AUDIT_CANDIDATE` | 0 | 17/110/117 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1240 | `yarikoptic/sleap` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1241 | `yarikoptic/spm` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1242 | `Charvijain16/resp` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1243 | `yarikoptic/pynwb` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1244 | `jaybee84/benchscofi` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1245 | `yarikoptic/AmadeusGPT` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1246 | `Mr-Milk/SpatialEntropy` | `DEEP_AUDIT_CANDIDATE` | 0 | 6/1/1 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1247 | `Mr-Milk/Aquila` | `DEEP_AUDIT_CANDIDATE` | 0 | 46/7/2 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1248 | `yarikoptic/nitime` | `DEEP_AUDIT_CANDIDATE` | 88 | 0/0/0 | REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead |
| 1249 | `yarikoptic/rapidtide-cloud` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1250 | `vladsavelyev/rnaseq` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1251 | `yarikoptic/pylibjpeg-libjpeg` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1252 | `yarikoptic/Public-nEUro.github.io` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1253 | `gutendzx/xsleepnet` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1254 | `yarikoptic/NeuroVault` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1255 | `yarikoptic/fsub_extractor` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1256 | `yarikoptic/nilearn` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1257 | `shantanusharma/hyena-dna` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1258 | `yarikoptic/ndx-beadl` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1259 | `little2b/the-RF-GSEA-Method` | `EMPTY` | 0 | 0/0/0 | CLOSE_EMPTY_OR_UNAVAILABLE_ARTIFACT; no integration capability retained |
| 1260 | `yarikoptic/zenodo` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1261 | `yarikoptic/hnn-core` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |
| 1262 | `yarikoptic/zarr_checksum` | `NO_UNIQUE_OR_SOURCE_LINEAGE` | 0 | 0/0/0 | CLOSE_NO_MEMBER_UNIQUE_CODE; retain source identity only; allocate no Feature or Implementation ID |

## Candidate and blocker details

### Order 1220 — `Mr-Milk/IMC-Analysis-Pipeline`

Bounded repositories: `Mr-Milk/IMC-Analysis-Pipeline`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 12, code 7, documentation 1, data 0, manifests 3.

Static security flags: `{"filesystem_mutation": 3, "network_fetch": 1}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 2}`.

Direct-adoption blockers:

- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1227 — `Liripo/scPort`

Bounded repositories: `Liripo/scPort`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 12, code 8, documentation 1, data 2, manifests 1.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1232 — `IDEA-Research/Grounded-Segment-Anything`

Bounded repositories: `chaudhariatul/Grounded-SAM`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 4, code 0, documentation 4, data 0, manifests 0.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- large-artifact review used bounded selected-blob sampling and is not evidence of runtime correctness.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1239 — `DevinDeSilva/DruggableProtienPrediction`

Bounded repositories: `DevinDeSilva/DruggableProtienPrediction`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 244, code 17, documentation 110, data 117, manifests 0.

Static security flags: `{"unsafe_deserialization": 16, "path_input": 4}`.

Privacy/data-governance flags: `{"upload_or_remote_transfer": 3, "human_genomics": 1}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 13}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1246 — `Mr-Milk/SpatialEntropy`

Bounded repositories: `Mr-Milk/SpatialEntropy`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 12, code 6, documentation 1, data 1, manifests 2.

Static security flags: `{"mutable_remote_install": 2}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{"unseeded_randomness": 8, "assertion_as_validation": 3}`.

Direct-adoption blockers:

- dependency resolution is not fully locked by an observed lockfile.
- static security-sensitive primitives require manual source-to-sink validation.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1247 — `Mr-Milk/Aquila`

Bounded repositories: `Mr-Milk/Aquila`.

Immutable acquisition: IMMUTABLE_TARBALL; files read 62, code 46, documentation 7, data 2, manifests 6.

Static security flags: `{"dynamic_code_execution": 1, "network_fetch": 1, "filesystem_mutation": 1, "mutable_remote_install": 1}`.

Privacy/data-governance flags: `{"clinical_or_patient_data": 81, "human_genomics": 25}`.

Scientific/reproducibility flags: `{"assertion_as_validation": 8, "hardcoded_absolute_path": 1}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- static security-sensitive primitives require manual source-to-sink validation.
- biomedical or user-data handling requires explicit privacy, consent and data-governance review.
- scientific reproducibility or validation flags require domain review.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

### Order 1248 — `nipy/nitime`

Bounded repositories: `yarikoptic/nitime`.

Immutable acquisition: IMMUTABLE_CHANGED_BLOBS; files read 1, code 0, documentation 0, data 0, manifests 0.

Static security flags: `{}`.

Privacy/data-governance flags: `{}`.

Scientific/reproducibility flags: `{}`.

Direct-adoption blockers:

- no license file was included in the bounded reviewed immutable blobs.
- no test surface was observed in the bounded static sample.
- dependency resolution is not fully locked by an observed lockfile.

Disposition: **REJECT_DIRECT_ADOPTION; preserve only as a bounded semantic-comparison or clean-room reconstruction lead**.

## Completion boundary

The batch is complete as a bounded static queue audit, not as an approval to install, execute or integrate any repository. No Feature or Implementation ID was allocated. Substantive candidates were normalized only as Change records, with Lineage records for fork-derived candidates, and remain rejected for direct adoption.
