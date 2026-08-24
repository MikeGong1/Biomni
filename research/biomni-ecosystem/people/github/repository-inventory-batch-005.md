# Public Repository Inventory for Code-visible People — Batch 005

Parent verification: `VERIFIED`. Scope:
`person-github-000042`–`000051`, all GitHub User accounts.

Fourteen successful serialized GraphQL responses returned all 386 public owner
repositories. Seven accounts fit one 100-node page. zhanxw and changwn were
recovered in two 50-node pages, while Chahat08 required three; every final
`hasNextPage` is false and combined nodes equal `totalCount`. Three failed
100-node gateway responses were discarded. No repository code was executed.

## Coverage

| Person ID | Login | Repositories | Existing | New | High | Possible | Low | Irrelevant | Cursor |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| person-github-000042 | yhqu | 1 | 0 | 1 | 1 | 0 | 0 | 0 | exhausted |
| person-github-000043 | zancmeresek | 8 | 1 | 7 | 1 | 0 | 0 | 7 | exhausted |
| person-github-000044 | Zethson | 7 | 0 | 7 | 3 | 0 | 2 | 2 | exhausted |
| person-github-000045 | zhanxw | 88 | 1 | 87 | 37 | 12 | 18 | 21 | exhausted |
| person-github-000046 | zskylarli | 13 | 1 | 12 | 7 | 2 | 0 | 4 | exhausted |
| person-github-000047 | aevo98765 | 40 | 1 | 39 | 7 | 8 | 6 | 19 | exhausted |
| person-github-000048 | ahueb | 11 | 0 | 11 | 4 | 1 | 3 | 3 | exhausted |
| person-github-000049 | Ayushmaniar | 21 | 0 | 21 | 3 | 4 | 6 | 8 | exhausted |
| person-github-000050 | Chahat08 | 117 | 0 | 117 | 4 | 9 | 27 | 77 | exhausted |
| person-github-000051 | changwn | 80 | 1 | 79 | 32 | 23 | 17 | 8 | exhausted |
| **Total** | **10 accounts** | **386** | **5** | **381** | **99** | **59** | **79** | **149** | **exhausted** |

Five existing Biomni fork IDs are reused. The 381 new repositories use contiguous
IDs `repo-002270`–`repo-002650`.

## Metadata screening

HIGH requires explicit biomedical, biological, genomics, clinical, drug, protein,
scientific-agent, MCP, Skills, benchmark, or matching scientific infrastructure.
POSSIBLE preserves ambiguity for README checks. Generic ML/software without a
domain signal is LOW; unrelated coursework, games, consumer apps, and finance
utilities are IRRELEVANT.

The HIGH queue includes agentic-science, Biomni forks, bioinformatics and
single-cell/genomics tools, medical and clinical analysis, biomedical
foundation-model or benchmark work, scientific visualization, explicit MCP
servers, and telomere analysis. Labels remain metadata-grounded inference, not
integration recommendations.

Metadata aggregate: 185 forks and 201 source repositories; four archived and none
disabled; 13 expose a latest release; 241 have no affirmative SPDX object. Topic
nodes are complete. The 59 POSSIBLE entries await bounded README disambiguation.

## Repository ledger

| Repository ID | Repository | Form | Language | Code license | Last push | Relevance |
|---|---|---|---|---|---|---|
| repo-002270 | yhqu/agentic-science | fork | Python | MIT | 2026-05-25 | HIGH_RELEVANCE |
| repo-002271 | zancmeresek/Analysis-of-body-language-and-speech-in-video | fork | Python | LICENSE_UNCLEAR | 2024-11-19 | IRRELEVANT |
| repo-000535 | zancmeresek/Biomni | fork | Python | Apache-2.0 | 2025-08-05 | HIGH_RELEVANCE |
| repo-002272 | zancmeresek/frontend | source | Dockerfile | LICENSE_UNCLEAR | 2023-05-09 | IRRELEVANT |
| repo-002273 | zancmeresek/meta-vision-api | fork | TypeScript | LICENSE_UNCLEAR | 2023-11-28 | IRRELEVANT |
| repo-002274 | zancmeresek/padel-ai-system | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2026-01-11 | IRRELEVANT |
| repo-002275 | zancmeresek/PadelVic | fork | — | LICENSE_UNCLEAR | 2024-01-27 | IRRELEVANT |
| repo-002276 | zancmeresek/padlo-analytics-media | source | — | LICENSE_UNCLEAR | 2026-08-22 | IRRELEVANT |
| repo-002277 | zancmeresek/TestAppMain | source | — | LICENSE_UNCLEAR | 2024-04-11 | IRRELEVANT |
| repo-002278 | Zethson/fknni | source | Python | Apache-2.0 | 2026-01-02 | LOW_RELEVANCE |
| repo-002279 | Zethson/guide-seq-container | source | Dockerfile | LICENSE_UNCLEAR | 2021-02-22 | HIGH_RELEVANCE |
| repo-002280 | Zethson/igem_tuebingen_website | source | HTML | MIT | 2020-12-09 | HIGH_RELEVANCE |
| repo-002281 | Zethson/lukas_heumos_website | source | HTML | NOASSERTION | 2025-12-19 | IRRELEVANT |
| repo-002282 | Zethson/MHCBoost | source | Python | MIT | 2019-12-27 | HIGH_RELEVANCE |
| repo-002283 | Zethson/test-gpu-ci | source | — | LICENSE_UNCLEAR | 2023-01-31 | LOW_RELEVANCE |
| repo-002284 | Zethson/zethson | source | — | LICENSE_UNCLEAR | 2026-07-15 | IRRELEVANT |
| repo-002285 | zhanxw/adv-r | fork | R | LICENSE_UNCLEAR | 2013-08-29 | LOW_RELEVANCE |
| repo-002286 | zhanxw/ancestry | source | C++ | LICENSE_UNCLEAR | 2017-03-31 | HIGH_RELEVANCE |
| repo-002287 | zhanxw/anno | source | C++ | GPL-3.0 | 2016-05-18 | HIGH_RELEVANCE |
| repo-002288 | zhanxw/Arbor | fork | R | LICENSE_UNCLEAR | 2022-10-21 | POSSIBLE_RELEVANCE |
| repo-002289 | zhanxw/Argument | source | — | LICENSE_UNCLEAR | 2011-06-13 | LOW_RELEVANCE |
| repo-002290 | zhanxw/AstroNvimConfig | source | Lua | LICENSE_UNCLEAR | 2023-03-14 | IRRELEVANT |
| repo-002291 | zhanxw/autocat | source | Rust | LICENSE_UNCLEAR | 2026-02-05 | LOW_RELEVANCE |
| repo-002292 | zhanxw/awesome-tools | source | — | LICENSE_UNCLEAR | 2026-02-09 | LOW_RELEVANCE |
| repo-002293 | zhanxw/base | source | C++ | LICENSE_UNCLEAR | 2009-11-25 | LOW_RELEVANCE |
| repo-002294 | zhanxw/BayesSLAM | source | — | LICENSE_UNCLEAR | 2018-09-04 | HIGH_RELEVANCE |
| repo-002295 | zhanxw/BayesSMILES | fork | C++ | LICENSE_UNCLEAR | 2021-01-08 | HIGH_RELEVANCE |
| repo-002296 | zhanxw/BayesSMILES_web | source | JavaScript | LICENSE_UNCLEAR | 2021-01-08 | HIGH_RELEVANCE |
| repo-002297 | zhanxw/bench | source | Python | GPL-2.0 | 2015-11-02 | LOW_RELEVANCE |
| repo-002298 | zhanxw/bioconda-recipes | fork | Shell | LICENSE_UNCLEAR | 2020-03-12 | HIGH_RELEVANCE |
| repo-000445 | zhanxw/Biomni | fork | Python | Apache-2.0 | 2025-10-02 | HIGH_RELEVANCE |
| repo-002299 | zhanxw/birdseed2vcf | fork | Python | LICENSE_UNCLEAR | 2019-04-24 | HIGH_RELEVANCE |
| repo-002300 | zhanxw/cat | source | Python | LICENSE_UNCLEAR | 2017-04-27 | IRRELEVANT |
| repo-002301 | zhanxw/cbioportal | fork | JavaScript | AGPL-3.0 | 2019-08-23 | HIGH_RELEVANCE |
| repo-002302 | zhanxw/chatgpt-text-to-midjourney-image | fork | JavaScript | MIT | 2023-04-04 | IRRELEVANT |
| repo-002303 | zhanxw/checkVCF | source | Python | LICENSE_UNCLEAR | 2016-03-18 | HIGH_RELEVANCE |
| repo-002304 | zhanxw/compile-ci | source | Shell | LICENSE_UNCLEAR | 2018-10-09 | LOW_RELEVANCE |
| repo-002305 | zhanxw/CookLikeHOC | fork | JavaScript | LICENSE_UNCLEAR | 2025-09-22 | IRRELEVANT |
| repo-002306 | zhanxw/cromwell | fork | Scala | BSD-3-Clause | 2018-07-11 | HIGH_RELEVANCE |
| repo-002307 | zhanxw/cromwellDashboard | source | R | LICENSE_UNCLEAR | 2018-07-16 | HIGH_RELEVANCE |
| repo-002308 | zhanxw/dense-matrix-mult | fork | C | LICENSE_UNCLEAR | 2013-06-25 | LOW_RELEVANCE |
| repo-002309 | zhanxw/dotFiles | source | Emacs Lisp | LICENSE_UNCLEAR | 2022-03-02 | IRRELEVANT |
| repo-002310 | zhanxw/dzi-proxy | source | Python | GPL-3.0 | 2023-10-09 | POSSIBLE_RELEVANCE |
| repo-002311 | zhanxw/ehrdiff | fork | Python | MIT | 2023-04-26 | HIGH_RELEVANCE |
| repo-002312 | zhanxw/fast.lasso | source | C++ | GPL-3.0 | 2020-04-25 | POSSIBLE_RELEVANCE |
| repo-002313 | zhanxw/featurescript | fork | — | LICENSE_UNCLEAR | 2021-04-03 | IRRELEVANT |
| repo-002314 | zhanxw/FMAP | fork | Perl | NOASSERTION | 2017-06-07 | HIGH_RELEVANCE |
| repo-002315 | zhanxw/ggShinyApp | fork | R | MIT | 2015-01-30 | LOW_RELEVANCE |
| repo-002316 | zhanxw/glype | fork | PHP | NOASSERTION | 2022-03-24 | IRRELEVANT |
| repo-002317 | zhanxw/haoel.blog | source | HTML | LICENSE_UNCLEAR | 2023-05-19 | IRRELEVANT |
| repo-002318 | zhanxw/histoterm | source | Rust | GPL-3.0 | 2025-11-13 | LOW_RELEVANCE |
| repo-002319 | zhanxw/IntegrativeBayes | fork | C++ | GPL-3.0 | 2019-06-09 | POSSIBLE_RELEVANCE |
| repo-002320 | zhanxw/Isoplexis_Data_Analysis | source | Python | LICENSE_UNCLEAR | 2023-05-02 | POSSIBLE_RELEVANCE |
| repo-002321 | zhanxw/js.survival | source | JavaScript | LICENSE_UNCLEAR | 2023-05-26 | POSSIBLE_RELEVANCE |
| repo-002322 | zhanxw/klib | fork | C | LICENSE_UNCLEAR | 2013-11-30 | LOW_RELEVANCE |
| repo-002323 | zhanxw/laser | source | C++ | LICENSE_UNCLEAR | 2013-04-04 | HIGH_RELEVANCE |
| repo-002324 | zhanxw/leafcutter | fork | C++ | LICENSE_UNCLEAR | 2016-05-17 | HIGH_RELEVANCE |
| repo-002325 | zhanxw/libMvtnorm | source | Fortran | LICENSE_UNCLEAR | 2014-03-03 | LOW_RELEVANCE |
| repo-002326 | zhanxw/libStatGen | fork | C++ | LICENSE_UNCLEAR | 2013-07-03 | HIGH_RELEVANCE |
| repo-002327 | zhanxw/LinkageAnalyzer | source | R | LICENSE_UNCLEAR | 2015-02-19 | HIGH_RELEVANCE |
| repo-002328 | zhanxw/linux-insides | fork | — | LICENSE_UNCLEAR | 2015-09-06 | LOW_RELEVANCE |
| repo-002329 | zhanxw/Literature | source | Python | LICENSE_UNCLEAR | 2026-08-01 | POSSIBLE_RELEVANCE |
| repo-002330 | zhanxw/manubot | fork | Python | NOASSERTION | 2024-02-18 | HIGH_RELEVANCE |
| repo-002331 | zhanxw/Marlin | fork | C++ | GPL-3.0 | 2022-09-08 | IRRELEVANT |
| repo-002332 | zhanxw/Mask_RCNN | fork | Jupyter Notebook | NOASSERTION | 2018-02-21 | LOW_RELEVANCE |
| repo-002333 | zhanxw/MB-GAN | source | Jupyter Notebook | GPL-3.0 | 2020-12-14 | HIGH_RELEVANCE |
| repo-002334 | zhanxw/MB-SupCon | fork | Jupyter Notebook | GPL-3.0 | 2021-12-08 | POSSIBLE_RELEVANCE |
| repo-002335 | zhanxw/MCP-Biomedical-Agent | fork | Python | LICENSE_UNCLEAR | 2025-08-22 | HIGH_RELEVANCE |
| repo-002336 | zhanxw/mctoolsr | fork | HTML | LICENSE_UNCLEAR | 2017-11-29 | HIGH_RELEVANCE |
| repo-002337 | zhanxw/md2html | source | CSS | GPL-2.0 | 2015-03-06 | IRRELEVANT |
| repo-002338 | zhanxw/melpa | fork | Emacs Lisp | NOASSERTION | 2018-07-09 | IRRELEVANT |
| repo-002339 | zhanxw/MetaPrism | fork | Perl | LICENSE_UNCLEAR | 2021-01-19 | HIGH_RELEVANCE |
| repo-002340 | zhanxw/MicrobiomeBayesDiff | fork | R | LICENSE_UNCLEAR | 2019-03-22 | HIGH_RELEVANCE |
| repo-002341 | zhanxw/MicrobiomeProfiler | fork | R | LICENSE_UNCLEAR | 2021-10-15 | HIGH_RELEVANCE |
| repo-002342 | zhanxw/microbiomeViz | fork | R | LICENSE_UNCLEAR | 2019-03-06 | HIGH_RELEVANCE |
| repo-002343 | zhanxw/MicrobiotaProcess | fork | R | LICENSE_UNCLEAR | 2020-03-23 | HIGH_RELEVANCE |
| repo-002344 | zhanxw/molformer | fork | Jupyter Notebook | Apache-2.0 | 2023-10-16 | HIGH_RELEVANCE |
| repo-002345 | zhanxw/morpheus.R | fork | R | BSD-3-Clause | 2020-08-22 | POSSIBLE_RELEVANCE |
| repo-002346 | zhanxw/mt-dnn | fork | Python | MIT | 2019-05-31 | LOW_RELEVANCE |
| repo-002347 | zhanxw/mycode | source | C++ | LICENSE_UNCLEAR | 2015-05-18 | IRRELEVANT |
| repo-002348 | zhanxw/parallel | source | Python | LICENSE_UNCLEAR | 2013-09-15 | IRRELEVANT |
| repo-002349 | zhanxw/q | fork | Python | LICENSE_UNCLEAR | 2014-02-17 | IRRELEVANT |
| repo-002350 | zhanxw/re2 | source | — | BSD-3-Clause | 2015-06-24 | IRRELEVANT |
| repo-002351 | zhanxw/rvtests | source | C++ | LICENSE_UNCLEAR | 2022-01-26 | HIGH_RELEVANCE |
| repo-002352 | zhanxw/rvtests-docker | source | Dockerfile | LICENSE_UNCLEAR | 2018-10-11 | HIGH_RELEVANCE |
| repo-002353 | zhanxw/sc-type | fork | HTML | GPL-3.0 | 2023-05-23 | POSSIBLE_RELEVANCE |
| repo-002354 | zhanxw/ScopeViewer | fork | CSS | LICENSE_UNCLEAR | 2026-03-17 | HIGH_RELEVANCE |
| repo-002355 | zhanxw/screenshot-to-code | fork | TypeScript | MIT | 2024-03-03 | IRRELEVANT |
| repo-002356 | zhanxw/seqminer | source | C | NOASSERTION | 2026-02-23 | HIGH_RELEVANCE |
| repo-002357 | zhanxw/SeqMinerCmd | source | R | GPL-3.0 | 2013-12-08 | HIGH_RELEVANCE |
| repo-002358 | zhanxw/SGVFinder | fork | Python | NOASSERTION | 2025-11-17 | POSSIBLE_RELEVANCE |
| repo-002359 | zhanxw/shinydashboardPlus | fork | R | NOASSERTION | 2021-11-12 | LOW_RELEVANCE |
| repo-002360 | zhanxw/slmtop | fork | Rust | MIT | 2026-08-05 | IRRELEVANT |
| repo-002361 | zhanxw/SPD | source | C | GPL-3.0 | 2014-04-01 | HIGH_RELEVANCE |
| repo-002362 | zhanxw/TCR_explorer | fork | R | GPL-3.0 | 2019-06-13 | HIGH_RELEVANCE |
| repo-002363 | zhanxw/TCR_explorer_package | fork | R | GPL-3.0 | 2019-05-24 | HIGH_RELEVANCE |
| repo-002364 | zhanxw/tdca-paper-code | source | R | GPL-3.0 | 2026-04-14 | POSSIBLE_RELEVANCE |
| repo-002365 | zhanxw/upptime | source | Markdown | MIT | 2026-08-23 | IRRELEVANT |
| repo-002366 | zhanxw/upptime-1 | fork | — | MIT | 2022-09-01 | IRRELEVANT |
| repo-002367 | zhanxw/vcf2geno | source | C++ | LICENSE_UNCLEAR | 2013-12-08 | HIGH_RELEVANCE |
| repo-002368 | zhanxw/vercel-ai-chatbot-supbase | source | TypeScript | NOASSERTION | 2025-02-16 | LOW_RELEVANCE |
| repo-002369 | zhanxw/wdl-mode | source | Emacs Lisp | GPL-3.0 | 2019-07-15 | LOW_RELEVANCE |
| repo-002370 | zhanxw/XiaoweiLib | source | Python | MIT | 2018-12-18 | IRRELEVANT |
| repo-002371 | zhanxw/zhanxw.github.io | source | — | LICENSE_UNCLEAR | 2013-04-30 | IRRELEVANT |
| repo-002372 | zskylarli/bacteriaGAN | source | Jupyter Notebook | LICENSE_UNCLEAR | 2022-04-04 | HIGH_RELEVANCE |
| repo-002373 | zskylarli/basi-homepage | fork | HTML | LICENSE_UNCLEAR | 2021-07-28 | IRRELEVANT |
| repo-000651 | zskylarli/Biomni | fork | Python | Apache-2.0 | 2025-07-17 | HIGH_RELEVANCE |
| repo-002374 | zskylarli/cellocate | source | Jupyter Notebook | LICENSE_UNCLEAR | 2026-02-27 | HIGH_RELEVANCE |
| repo-002375 | zskylarli/MET | source | JavaScript | LICENSE_UNCLEAR | 2022-02-17 | IRRELEVANT |
| repo-002376 | zskylarli/onkio | source | TypeScript | LICENSE_UNCLEAR | 2026-08-19 | IRRELEVANT |
| repo-002377 | zskylarli/rings | source | JavaScript | LICENSE_UNCLEAR | 2023-04-28 | POSSIBLE_RELEVANCE |
| repo-002378 | zskylarli/scrna-bacteria-integration | source | Jupyter Notebook | MIT | 2022-04-26 | HIGH_RELEVANCE |
| repo-002379 | zskylarli/seurat-object | fork | R | NOASSERTION | 2023-10-19 | HIGH_RELEVANCE |
| repo-002380 | zskylarli/seurat-wrappers | fork | R | GPL-3.0 | 2024-04-30 | HIGH_RELEVANCE |
| repo-002381 | zskylarli/seurat_dev | fork | R | NOASSERTION | 2023-11-07 | HIGH_RELEVANCE |
| repo-002382 | zskylarli/transcrobialGAN | source | Jupyter Notebook | MIT | 2022-04-04 | POSSIBLE_RELEVANCE |
| repo-002383 | zskylarli/zskylarli.github.io | source | HTML | MIT | 2026-08-12 | IRRELEVANT |
| repo-002384 | aevo98765/agile-planning | source | — | LICENSE_UNCLEAR | 2024-04-11 | IRRELEVANT |
| repo-002385 | aevo98765/bee-agent-framework | fork | TypeScript | Apache-2.0 | 2025-03-05 | POSSIBLE_RELEVANCE |
| repo-002386 | aevo98765/bee-api | fork | TypeScript | Apache-2.0 | 2025-02-07 | POSSIBLE_RELEVANCE |
| repo-002387 | aevo98765/bee-community-tools | fork | TypeScript | Apache-2.0 | 2024-10-29 | POSSIBLE_RELEVANCE |
| repo-002388 | aevo98765/bee-stack | fork | Shell | Apache-2.0 | 2024-11-04 | POSSIBLE_RELEVANCE |
| repo-002389 | aevo98765/bee-ui | fork | TypeScript | Apache-2.0 | 2025-02-07 | POSSIBLE_RELEVANCE |
| repo-000732 | aevo98765/Biomni | fork | Python | Apache-2.0 | 2026-03-02 | HIGH_RELEVANCE |
| repo-002390 | aevo98765/bloom | fork | Python | MIT | 2026-03-26 | LOW_RELEVANCE |
| repo-002391 | aevo98765/calculator-fastapi-app | source | Python | LICENSE_UNCLEAR | 2024-07-15 | IRRELEVANT |
| repo-002392 | aevo98765/CellProfiler | fork | Python | NOASSERTION | 2022-06-29 | HIGH_RELEVANCE |
| repo-002393 | aevo98765/Centralized-repository-shipping_calculations | fork | Python | Apache-2.0 | 2024-04-24 | IRRELEVANT |
| repo-002394 | aevo98765/ci-cd-final-project | source | Python | Apache-2.0 | 2024-05-31 | IRRELEVANT |
| repo-002395 | aevo98765/Claude-Code-Test-Public | source | — | LICENSE_UNCLEAR | 2026-02-07 | LOW_RELEVANCE |
| repo-002396 | aevo98765/devops-capstone-project | source | Python | Apache-2.0 | 2024-06-21 | IRRELEVANT |
| repo-002397 | aevo98765/docling-mcp | fork | Python | MIT | 2025-06-23 | HIGH_RELEVANCE |
| repo-002398 | aevo98765/ds-content-interactive-jupyterlab-tutorial | fork | Jupyter Notebook | MIT | 2019-07-01 | LOW_RELEVANCE |
| repo-002399 | aevo98765/fgxgm-SecurityCheckSample | fork | HTML | Apache-2.0 | 2026-02-16 | IRRELEVANT |
| repo-002400 | aevo98765/ginapi | source | Go | LICENSE_UNCLEAR | 2022-03-31 | IRRELEVANT |
| repo-002401 | aevo98765/goapi | source | Go | LICENSE_UNCLEAR | 2021-11-29 | IRRELEVANT |
| repo-002402 | aevo98765/gohexproject | source | Go | LICENSE_UNCLEAR | 2022-04-04 | IRRELEVANT |
| repo-002403 | aevo98765/golf-coach-ai-fork | fork | TypeScript | MIT | 2021-02-21 | IRRELEVANT |
| repo-002404 | aevo98765/golf-coach-ai-material-kit-react | fork | JavaScript | LICENSE_UNCLEAR | 2023-01-12 | IRRELEVANT |
| repo-002405 | aevo98765/honors-agile-planning-task | source | — | LICENSE_UNCLEAR | 2024-04-15 | IRRELEVANT |
| repo-002406 | aevo98765/in-silico-proteome | source | Python | LICENSE_UNCLEAR | 2021-10-21 | HIGH_RELEVANCE |
| repo-002407 | aevo98765/instructlab-data | source | — | LICENSE_UNCLEAR | 2025-02-07 | POSSIBLE_RELEVANCE |
| repo-002408 | aevo98765/jbbmo-Introduction-to-Git-and-GitHub | fork | Python | Apache-2.0 | 2024-04-24 | IRRELEVANT |
| repo-002409 | aevo98765/materials | fork | Python | Apache-2.0 | 2025-05-01 | HIGH_RELEVANCE |
| repo-002410 | aevo98765/mcp | fork | — | Apache-2.0 | 2025-11-19 | HIGH_RELEVANCE |
| repo-002411 | aevo98765/movie_chat | source | HTML | LICENSE_UNCLEAR | 2021-05-09 | IRRELEVANT |
| repo-002412 | aevo98765/openclaw | fork | TypeScript | MIT | 2026-02-13 | LOW_RELEVANCE |
| repo-002413 | aevo98765/pandas | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2019-04-19 | LOW_RELEVANCE |
| repo-002414 | aevo98765/pandas-ai | fork | Python | NOASSERTION | 2024-10-22 | POSSIBLE_RELEVANCE |
| repo-002415 | aevo98765/pub_quiz | source | PowerShell | LICENSE_UNCLEAR | 2021-05-13 | IRRELEVANT |
| repo-002416 | aevo98765/skills | fork | Shell | MIT | 2026-08-06 | HIGH_RELEVANCE |
| repo-002417 | aevo98765/TaskTrackerAngular | source | TypeScript | LICENSE_UNCLEAR | 2021-08-04 | IRRELEVANT |
| repo-002418 | aevo98765/taxonomy | fork | Python | Apache-2.0 | 2024-09-20 | POSSIBLE_RELEVANCE |
| repo-002419 | aevo98765/tdd-bdd-final-project | source | Python | Apache-2.0 | 2024-05-24 | IRRELEVANT |
| repo-002420 | aevo98765/training-repo | source | Shell | Apache-2.0 | 2024-04-24 | IRRELEVANT |
| repo-002421 | aevo98765/ui | fork | TypeScript | Apache-2.0 | 2025-03-12 | LOW_RELEVANCE |
| repo-002422 | aevo98765/wtecc-CICD_PracticeCode | fork | Python | Apache-2.0 | 2024-05-29 | IRRELEVANT |
| repo-002423 | ahueb/Access-Checker | fork | Ruby | NOASSERTION | 2018-06-06 | HIGH_RELEVANCE |
| repo-002424 | ahueb/ai-nuggets | fork | Python | LICENSE_UNCLEAR | 2026-05-12 | HIGH_RELEVANCE |
| repo-002425 | ahueb/aseadexport | source | — | NOASSERTION | 2018-06-06 | IRRELEVANT |
| repo-002426 | ahueb/biothings_explorer | fork | Vue | Apache-2.0 | 2024-09-10 | HIGH_RELEVANCE |
| repo-002427 | ahueb/DrugMechDB | fork | Jupyter Notebook | CC0-1.0 | 2024-10-16 | HIGH_RELEVANCE |
| repo-002428 | ahueb/ensmallen | fork | Python | MIT | 2025-07-11 | LOW_RELEVANCE |
| repo-002429 | ahueb/evolving_ralph | source | Shell | MIT | 2026-03-25 | IRRELEVANT |
| repo-002430 | ahueb/matrix | fork | Python | Apache-2.0 | 2025-09-21 | POSSIBLE_RELEVANCE |
| repo-002431 | ahueb/SE_weather_app | source | Python | AGPL-3.0 | 2022-11-27 | IRRELEVANT |
| repo-002432 | ahueb/sulab.org | fork | HTML | BSD-3-Clause | 2024-08-05 | LOW_RELEVANCE |
| repo-002433 | ahueb/vec_rand | fork | Rust | MIT | 2025-07-08 | LOW_RELEVANCE |
| repo-002434 | Ayushmaniar/Allegro-Music-Transformer | fork | Jupyter Notebook | Apache-2.0 | 2025-05-31 | LOW_RELEVANCE |
| repo-002435 | Ayushmaniar/Ayushmaniar.github.io | source | TypeScript | LICENSE_UNCLEAR | 2026-03-08 | IRRELEVANT |
| repo-002436 | Ayushmaniar/Big-Data-Science-Drug-Protein-Interactions | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-06-10 | HIGH_RELEVANCE |
| repo-002437 | Ayushmaniar/CNN_SLAM | fork | Python | LICENSE_UNCLEAR | 2018-08-11 | LOW_RELEVANCE |
| repo-002438 | Ayushmaniar/Content | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2018-07-19 | IRRELEVANT |
| repo-002439 | Ayushmaniar/cs229-ps-2018 | fork | TeX | LICENSE_UNCLEAR | 2019-07-13 | IRRELEVANT |
| repo-002440 | Ayushmaniar/cse258-project | source | Jupyter Notebook | LICENSE_UNCLEAR | 2024-12-04 | LOW_RELEVANCE |
| repo-002441 | Ayushmaniar/Gemini_Hackathon | source | TypeScript | LICENSE_UNCLEAR | 2026-02-15 | LOW_RELEVANCE |
| repo-002442 | Ayushmaniar/it-cert-automation-practice | fork | Python | Apache-2.0 | 2024-04-24 | IRRELEVANT |
| repo-002443 | Ayushmaniar/learnopencv | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2018-10-24 | LOW_RELEVANCE |
| repo-002444 | Ayushmaniar/magic-wormhole | fork | Python | MIT | 2018-10-16 | IRRELEVANT |
| repo-002445 | Ayushmaniar/mindcraft | fork | JavaScript | MIT | 2024-12-13 | POSSIBLE_RELEVANCE |
| repo-002446 | Ayushmaniar/mindcraft_multiagent_task_generation | source | JavaScript | LICENSE_UNCLEAR | 2025-03-01 | POSSIBLE_RELEVANCE |
| repo-002447 | Ayushmaniar/minecraft-recipe-visualizer | source | Python | LICENSE_UNCLEAR | 2026-02-12 | IRRELEVANT |
| repo-002448 | Ayushmaniar/music-transformer | fork | Python | GPL-3.0 | 2025-03-03 | LOW_RELEVANCE |
| repo-002449 | Ayushmaniar/powerpoint-mcp | source | Python | LICENSE_UNCLEAR | 2026-05-01 | HIGH_RELEVANCE |
| repo-002450 | Ayushmaniar/PPT-Assistant | source | Python | LICENSE_UNCLEAR | 2025-08-02 | POSSIBLE_RELEVANCE |
| repo-002451 | Ayushmaniar/probability_plots | source | Python | LICENSE_UNCLEAR | 2018-09-14 | POSSIBLE_RELEVANCE |
| repo-002452 | Ayushmaniar/qwiklabs_practice | source | Python | LICENSE_UNCLEAR | 2024-04-21 | IRRELEVANT |
| repo-002453 | Ayushmaniar/stock-market-data-fetch | source | Python | LICENSE_UNCLEAR | 2025-12-28 | IRRELEVANT |
| repo-002454 | Ayushmaniar/telomere_analysis_cse280a | source | Jupyter Notebook | LICENSE_UNCLEAR | 2025-03-15 | HIGH_RELEVANCE |
| repo-002455 | Chahat08/12ResultAnalysis | source | Jupyter Notebook | LICENSE_UNCLEAR | 2021-01-13 | POSSIBLE_RELEVANCE |
| repo-002456 | Chahat08/ADHD-NTU-PU | source | Jupyter Notebook | LICENSE_UNCLEAR | 2021-09-17 | POSSIBLE_RELEVANCE |
| repo-002457 | Chahat08/algorithms | fork | C++ | MIT | 2018-10-13 | IRRELEVANT |
| repo-002458 | Chahat08/Algorithms_in_C_SEDGEWICK | source | C | LICENSE_UNCLEAR | 2020-11-20 | IRRELEVANT |
| repo-002459 | Chahat08/ARP-WATCH | source | Python | LICENSE_UNCLEAR | 2024-03-16 | LOW_RELEVANCE |
| repo-002460 | Chahat08/avi | source | — | LICENSE_UNCLEAR | 2023-03-23 | IRRELEVANT |
| repo-002461 | Chahat08/battlecode | source | — | LICENSE_UNCLEAR | 2023-01-05 | IRRELEVANT |
| repo-002462 | Chahat08/battlecode23 | source | Java | AGPL-3.0 | 2023-01-23 | IRRELEVANT |
| repo-002463 | Chahat08/blog-website | source | Python | LICENSE_UNCLEAR | 2021-01-03 | IRRELEVANT |
| repo-002464 | Chahat08/BMP | source | C++ | MIT | 2024-01-17 | LOW_RELEVANCE |
| repo-002465 | Chahat08/BMPLib | source | C++ | MIT | 2024-01-17 | LOW_RELEVANCE |
| repo-002466 | Chahat08/Brain-Tumor-Classification | source | Jupyter Notebook | LICENSE_UNCLEAR | 2022-10-23 | HIGH_RELEVANCE |
| repo-002467 | Chahat08/C-programs | fork | C | LICENSE_UNCLEAR | 2020-10-16 | IRRELEVANT |
| repo-002468 | Chahat08/Chahat08 | source | — | LICENSE_UNCLEAR | 2025-10-02 | IRRELEVANT |
| repo-002469 | Chahat08/Chahat08-Csharp-programs | source | C# | LICENSE_UNCLEAR | 2021-03-11 | IRRELEVANT |
| repo-002470 | Chahat08/Chahat08.github.io | source | HTML | LICENSE_UNCLEAR | 2026-07-14 | IRRELEVANT |
| repo-002471 | Chahat08/chahatkalsi.herokuapp.com | source | Java | LICENSE_UNCLEAR | 2023-01-13 | IRRELEVANT |
| repo-002472 | Chahat08/coding-interview-university | fork | — | CC-BY-SA-4.0 | 2020-10-26 | IRRELEVANT |
| repo-002473 | Chahat08/Conscious | source | — | LICENSE_UNCLEAR | 2021-01-17 | IRRELEVANT |
| repo-002474 | Chahat08/controller_input | source | C++ | LICENSE_UNCLEAR | 2024-03-02 | LOW_RELEVANCE |
| repo-002475 | Chahat08/CoolCoobs | source | C++ | MIT | 2024-01-29 | IRRELEVANT |
| repo-002476 | Chahat08/CPP-Overview | source | — | LICENSE_UNCLEAR | 2023-07-20 | IRRELEVANT |
| repo-002477 | Chahat08/CppCodes | fork | C++ | LICENSE_UNCLEAR | 2021-10-05 | IRRELEVANT |
| repo-002478 | Chahat08/CSE564_Final_Project | source | Jupyter Notebook | LICENSE_UNCLEAR | 2024-11-21 | HIGH_RELEVANCE |
| repo-002479 | Chahat08/Data-Structures-and-Algorithms | fork | C | LICENSE_UNCLEAR | 2018-10-13 | IRRELEVANT |
| repo-002480 | Chahat08/Data-Structures-And-Algorithms-Hacktoberfest18 | fork | C++ | LICENSE_UNCLEAR | 2018-10-12 | IRRELEVANT |
| repo-002481 | Chahat08/DeepLearning.ai-Summary | fork | Python | MIT | 2020-09-18 | IRRELEVANT |
| repo-002482 | Chahat08/Dimensionality-Reduction-Dashboard | source | JavaScript | LICENSE_UNCLEAR | 2024-03-15 | LOW_RELEVANCE |
| repo-002483 | Chahat08/DP | source | C++ | LICENSE_UNCLEAR | 2021-07-20 | IRRELEVANT |
| repo-002484 | Chahat08/Elements | source | CSS | LICENSE_UNCLEAR | 2022-11-09 | IRRELEVANT |
| repo-002485 | Chahat08/Exceptions | source | C++ | LICENSE_UNCLEAR | 2023-06-24 | IRRELEVANT |
| repo-002486 | Chahat08/File-Handling | source | C++ | LICENSE_UNCLEAR | 2023-06-28 | IRRELEVANT |
| repo-002487 | Chahat08/Fingernails-Segmentation | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2018-07-07 | POSSIBLE_RELEVANCE |
| repo-002488 | Chahat08/FitCode | source | JavaScript | MIT | 2021-11-14 | IRRELEVANT |
| repo-002489 | Chahat08/flask_sock_server | source | Python | LICENSE_UNCLEAR | 2024-11-03 | LOW_RELEVANCE |
| repo-002490 | Chahat08/game_server | source | Python | LICENSE_UNCLEAR | 2024-03-24 | IRRELEVANT |
| repo-002491 | Chahat08/graphs | source | C++ | LICENSE_UNCLEAR | 2022-05-11 | IRRELEVANT |
| repo-002492 | Chahat08/hacktoberfest | fork | HTML | GPL-3.0 | 2018-10-13 | IRRELEVANT |
| repo-002493 | Chahat08/Hacktoberfest-1 | fork | Python | MIT | 2018-10-12 | IRRELEVANT |
| repo-002494 | Chahat08/Hacktoberfest-2018 | fork | C | LICENSE_UNCLEAR | 2018-10-13 | IRRELEVANT |
| repo-002495 | Chahat08/Hacktoberfest-Census | fork | HTML | LICENSE_UNCLEAR | 2018-10-12 | IRRELEVANT |
| repo-002496 | Chahat08/Hacktoberfest-Mathematics | fork | Java | GPL-3.0 | 2018-10-13 | IRRELEVANT |
| repo-002497 | Chahat08/Hacktoberfest-Sign-In | fork | HTML | MIT | 2018-10-12 | IRRELEVANT |
| repo-002498 | Chahat08/Hacktoberfest2020 | fork | — | Apache-2.0 | 2020-09-26 | IRRELEVANT |
| repo-002499 | Chahat08/handson-ml2 | fork | Jupyter Notebook | Apache-2.0 | 2021-03-29 | IRRELEVANT |
| repo-002500 | Chahat08/hello-world | source | C++ | LICENSE_UNCLEAR | 2020-10-16 | IRRELEVANT |
| repo-002501 | Chahat08/HTML-Joystick | source | HTML | LICENSE_UNCLEAR | 2024-11-19 | LOW_RELEVANCE |
| repo-002502 | Chahat08/HTTP-TLS-Sniffer | source | Python | LICENSE_UNCLEAR | 2024-03-16 | LOW_RELEVANCE |
| repo-002503 | Chahat08/java-bitwise-manipulation | source | Java | LICENSE_UNCLEAR | 2023-01-18 | IRRELEVANT |
| repo-002504 | Chahat08/Java-Project-Structure | source | Java | LICENSE_UNCLEAR | 2023-01-05 | LOW_RELEVANCE |
| repo-002505 | Chahat08/Java-Project-Structure-With-Testing | source | Java | LICENSE_UNCLEAR | 2023-01-12 | LOW_RELEVANCE |
| repo-002506 | Chahat08/Java-Software-Testing | source | JavaScript | LICENSE_UNCLEAR | 2023-01-09 | IRRELEVANT |
| repo-002507 | Chahat08/jpmc-task-1 | fork | Python | LICENSE_UNCLEAR | 2022-11-08 | IRRELEVANT |
| repo-002508 | Chahat08/jpmc-task-2 | fork | Python | LICENSE_UNCLEAR | 2022-11-08 | IRRELEVANT |
| repo-002509 | Chahat08/jpmc-task-3 | fork | Python | LICENSE_UNCLEAR | 2022-11-08 | IRRELEVANT |
| repo-002510 | Chahat08/Lexical-Analyzer | source | — | LICENSE_UNCLEAR | 2023-01-08 | IRRELEVANT |
| repo-002511 | Chahat08/lhdbuild-csharp | source | C# | LICENSE_UNCLEAR | 2021-01-11 | IRRELEVANT |
| repo-002512 | Chahat08/Lilac | source | C++ | LICENSE_UNCLEAR | 2022-06-19 | IRRELEVANT |
| repo-002513 | Chahat08/LinkedLists | source | C++ | LICENSE_UNCLEAR | 2021-04-18 | IRRELEVANT |
| repo-002514 | Chahat08/List-Insertion-Sort | source | C | LICENSE_UNCLEAR | 2021-01-13 | LOW_RELEVANCE |
| repo-002515 | Chahat08/MergeSort | source | C++ | LICENSE_UNCLEAR | 2021-04-24 | LOW_RELEVANCE |
| repo-002516 | Chahat08/numpy-100 | fork | Python | MIT | 2020-09-28 | LOW_RELEVANCE |
| repo-002517 | Chahat08/Off-Axis-Stereo | source | C++ | LICENSE_UNCLEAR | 2024-01-31 | LOW_RELEVANCE |
| repo-002518 | Chahat08/OpenGL-Cube | source | C++ | LICENSE_UNCLEAR | 2024-01-22 | IRRELEVANT |
| repo-002519 | Chahat08/OpenGL-Scene-1 | source | C | MIT | 2024-02-18 | IRRELEVANT |
| repo-002520 | Chahat08/OpenGL-Startup-Template | source | C++ | LICENSE_UNCLEAR | 2024-01-24 | IRRELEVANT |
| repo-002521 | Chahat08/OpenGL2 | source | C++ | LICENSE_UNCLEAR | 2024-01-28 | IRRELEVANT |
| repo-002522 | Chahat08/opengl_1 | source | C++ | LICENSE_UNCLEAR | 2023-04-28 | IRRELEVANT |
| repo-002523 | Chahat08/opengl_2 | source | C++ | LICENSE_UNCLEAR | 2023-04-28 | IRRELEVANT |
| repo-002524 | Chahat08/opengl_3 | source | C++ | LICENSE_UNCLEAR | 2023-05-02 | IRRELEVANT |
| repo-002525 | Chahat08/opengl_4 | source | C++ | LICENSE_UNCLEAR | 2023-05-10 | IRRELEVANT |
| repo-002526 | Chahat08/opengl_5 | source | C++ | LICENSE_UNCLEAR | 2023-05-17 | IRRELEVANT |
| repo-002527 | Chahat08/OpenGL_6 | source | C++ | LICENSE_UNCLEAR | 2023-06-16 | IRRELEVANT |
| repo-002528 | Chahat08/OpenGL_7 | source | C++ | LICENSE_UNCLEAR | 2023-06-17 | IRRELEVANT |
| repo-002529 | Chahat08/Operator-Overloading | source | C++ | LICENSE_UNCLEAR | 2023-07-20 | LOW_RELEVANCE |
| repo-002530 | Chahat08/PearlHacks2021 | source | Jupyter Notebook | LICENSE_UNCLEAR | 2021-02-21 | IRRELEVANT |
| repo-002531 | Chahat08/Pineball | source | ShaderLab | LICENSE_UNCLEAR | 2021-05-30 | IRRELEVANT |
| repo-002532 | Chahat08/Pokemon-Statistics-Visualisation | source | JavaScript | LICENSE_UNCLEAR | 2024-03-15 | IRRELEVANT |
| repo-002533 | Chahat08/ppm | source | C++ | LICENSE_UNCLEAR | 2023-03-25 | IRRELEVANT |
| repo-002534 | Chahat08/PyCalc | fork | Python | LICENSE_UNCLEAR | 2020-09-27 | IRRELEVANT |
| repo-002535 | Chahat08/Python-DMA | source | Jupyter Notebook | LICENSE_UNCLEAR | 2022-03-09 | LOW_RELEVANCE |
| repo-002536 | Chahat08/python-tkinter-minesweeper | fork | Python | MIT | 2020-10-18 | IRRELEVANT |
| repo-002537 | Chahat08/QuickSort | source | — | LICENSE_UNCLEAR | 2021-04-24 | LOW_RELEVANCE |
| repo-002538 | Chahat08/Radiance | source | HTML | MIT | 2021-02-19 | IRRELEVANT |
| repo-002539 | Chahat08/Seive-Of-Erastosthenes | source | C | LICENSE_UNCLEAR | 2021-01-26 | LOW_RELEVANCE |
| repo-002540 | Chahat08/Simple-Tic-Tac-Toe | source | C++ | LICENSE_UNCLEAR | 2020-10-16 | IRRELEVANT |
| repo-002541 | Chahat08/SolarSprint | source | CSS | LICENSE_UNCLEAR | 2021-01-11 | IRRELEVANT |
| repo-002542 | Chahat08/sorting-algorithms | fork | Java | MIT | 2020-09-30 | LOW_RELEVANCE |
| repo-002543 | Chahat08/Sorting-Algorithms-in-C | source | C | LICENSE_UNCLEAR | 2021-02-03 | LOW_RELEVANCE |
| repo-002544 | Chahat08/Sorting-Algorithms-Review | source | C++ | LICENSE_UNCLEAR | 2021-10-21 | LOW_RELEVANCE |
| repo-002545 | Chahat08/spring-app | source | Java | LICENSE_UNCLEAR | 2023-03-23 | LOW_RELEVANCE |
| repo-002546 | Chahat08/Spring-MVC-App | source | Java | LICENSE_UNCLEAR | 2023-01-04 | LOW_RELEVANCE |
| repo-002547 | Chahat08/Stereo-Scene-1 | source | C++ | MIT | 2024-02-15 | LOW_RELEVANCE |
| repo-002548 | Chahat08/Stereo_1 | source | C++ | LICENSE_UNCLEAR | 2024-01-29 | LOW_RELEVANCE |
| repo-002549 | Chahat08/StereoCell | source | C# | LICENSE_UNCLEAR | 2025-12-07 | HIGH_RELEVANCE |
| repo-002550 | Chahat08/template | source | HTML | LICENSE_UNCLEAR | 2021-04-08 | IRRELEVANT |
| repo-002551 | Chahat08/Tetris | fork | Python | LICENSE_UNCLEAR | 2020-09-30 | IRRELEVANT |
| repo-002552 | Chahat08/The-Diamond-Lake-Shed | source | C# | LICENSE_UNCLEAR | 2021-11-07 | IRRELEVANT |
| repo-002553 | Chahat08/Theatre | source | C# | LICENSE_UNCLEAR | 2021-04-11 | IRRELEVANT |
| repo-002554 | Chahat08/tic-tac-toe | source | C++ | LICENSE_UNCLEAR | 2021-01-12 | IRRELEVANT |
| repo-002555 | Chahat08/tkinter-calc | fork | Python | NOASSERTION | 2020-09-27 | IRRELEVANT |
| repo-002556 | Chahat08/tkinter_temp_converter | source | Python | LICENSE_UNCLEAR | 2020-09-30 | IRRELEVANT |
| repo-002557 | Chahat08/tkinter_text_editor | source | Python | LICENSE_UNCLEAR | 2020-10-16 | IRRELEVANT |
| repo-002558 | Chahat08/tkinter_tile_flipping_game | source | Python | LICENSE_UNCLEAR | 2020-10-16 | IRRELEVANT |
| repo-002559 | Chahat08/Trees | source | C++ | LICENSE_UNCLEAR | 2021-10-21 | LOW_RELEVANCE |
| repo-002560 | Chahat08/UnityVolumeRendering | fork | C# | MIT | 2025-02-23 | POSSIBLE_RELEVANCE |
| repo-002561 | Chahat08/vida-website | fork | MDX | LICENSE_UNCLEAR | 2026-06-25 | POSSIBLE_RELEVANCE |
| repo-002562 | Chahat08/Volume_Renderer | source | C | LICENSE_UNCLEAR | 2024-08-04 | POSSIBLE_RELEVANCE |
| repo-002563 | Chahat08/Vox-Insight | source | JavaScript | MIT | 2025-07-12 | IRRELEVANT |
| repo-002564 | Chahat08/VTK_Engine | source | C++ | LICENSE_UNCLEAR | 2025-03-28 | POSSIBLE_RELEVANCE |
| repo-002565 | Chahat08/VTK_Tiled_Rendering | source | C++ | MIT | 2024-11-02 | POSSIBLE_RELEVANCE |
| repo-002566 | Chahat08/VTK_Tiled_Volume_Rendering | source | C++ | LICENSE_UNCLEAR | 2024-11-02 | POSSIBLE_RELEVANCE |
| repo-002567 | Chahat08/Web-Tech | source | HTML | LICENSE_UNCLEAR | 2021-07-25 | IRRELEVANT |
| repo-002568 | Chahat08/WebGL_Engine | source | JavaScript | MIT | 2025-01-28 | LOW_RELEVANCE |
| repo-002569 | Chahat08/websocket_client | source | C++ | LICENSE_UNCLEAR | 2024-11-03 | IRRELEVANT |
| repo-002570 | Chahat08/Win32_OpenGL | source | C | LICENSE_UNCLEAR | 2024-08-21 | IRRELEVANT |
| repo-002571 | Chahat08/Zarr_Rechunker | source | — | LICENSE_UNCLEAR | 2026-02-14 | HIGH_RELEVANCE |
| repo-002572 | changwn/ATAC_integrity | source | R | LICENSE_UNCLEAR | 2019-09-08 | HIGH_RELEVANCE |
| repo-002573 | changwn/autokeras | fork | Python | MIT | 2020-02-14 | LOW_RELEVANCE |
| repo-002574 | changwn/awesome-single-cell | fork | — | MIT | 2020-05-16 | HIGH_RELEVANCE |
| repo-002575 | changwn/BC-CRC | source | — | LICENSE_UNCLEAR | 2023-03-06 | HIGH_RELEVANCE |
| repo-000484 | changwn/Biomni | fork | Python | Apache-2.0 | 2025-09-03 | HIGH_RELEVANCE |
| repo-002576 | changwn/bjguahao | fork | Python | GPL-3.0 | 2019-08-27 | IRRELEVANT |
| repo-002577 | changwn/CAR-Toner | fork | R | GPL-3.0 | 2024-01-25 | HIGH_RELEVANCE |
| repo-002578 | changwn/car_t_stimulation | fork | Jupyter Notebook | MIT | 2022-12-15 | HIGH_RELEVANCE |
| repo-002579 | changwn/CARMSeD | fork | PureBasic | LICENSE_UNCLEAR | 2025-12-04 | POSSIBLE_RELEVANCE |
| repo-002580 | changwn/CARPOOL | fork | Python | LICENSE_UNCLEAR | 2022-03-14 | POSSIBLE_RELEVANCE |
| repo-002581 | changwn/cart_llms | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2026-03-16 | POSSIBLE_RELEVANCE |
| repo-002582 | changwn/CARTmath | fork | R | LICENSE_UNCLEAR | 2025-04-24 | HIGH_RELEVANCE |
| repo-002583 | changwn/cellrank | fork | Python | BSD-3-Clause | 2020-12-08 | HIGH_RELEVANCE |
| repo-002584 | changwn/Chinese-Medical-QA-Data | fork | — | LICENSE_UNCLEAR | 2020-02-06 | HIGH_RELEVANCE |
| repo-002585 | changwn/ChIP-seq_JiZhang | source | — | LICENSE_UNCLEAR | 2021-12-21 | HIGH_RELEVANCE |
| repo-002586 | changwn/Codes-for-SCUFS-FRFS0-SSVT | fork | — | LICENSE_UNCLEAR | 2018-05-31 | LOW_RELEVANCE |
| repo-002587 | changwn/combinatorial_signaling_motif_libraries | fork | Jupyter Notebook | MIT | 2024-01-15 | HIGH_RELEVANCE |
| repo-002588 | changwn/dagmm | fork | Python | MIT | 2020-05-12 | LOW_RELEVANCE |
| repo-002589 | changwn/DC_ictd_backup | source | R | LICENSE_UNCLEAR | 2020-05-22 | POSSIBLE_RELEVANCE |
| repo-002590 | changwn/DCONVscore | source | R | LICENSE_UNCLEAR | 2018-10-10 | POSSIBLE_RELEVANCE |
| repo-002591 | changwn/DeconvoLib | source | R | Apache-2.0 | 2019-12-23 | POSSIBLE_RELEVANCE |
| repo-002592 | changwn/Deconvolution_paper | source | — | LICENSE_UNCLEAR | 2023-12-14 | POSSIBLE_RELEVANCE |
| repo-002593 | changwn/DETERRENT | fork | Python | LICENSE_UNCLEAR | 2020-06-25 | LOW_RELEVANCE |
| repo-002594 | changwn/dockstore_tool_arriba | fork | Shell | LICENSE_UNCLEAR | 2018-03-08 | HIGH_RELEVANCE |
| repo-002595 | changwn/DTF-Drug-Synergy | fork | Python | LICENSE_UNCLEAR | 2020-11-24 | HIGH_RELEVANCE |
| repo-002596 | changwn/E-MTAB-6141 | fork | — | LICENSE_UNCLEAR | 2020-05-21 | HIGH_RELEVANCE |
| repo-002597 | changwn/ECE629 | source | Python | LICENSE_UNCLEAR | 2020-10-24 | IRRELEVANT |
| repo-002598 | changwn/ECE662-mini | source | Python | LICENSE_UNCLEAR | 2020-04-25 | IRRELEVANT |
| repo-002599 | changwn/enrichR | fork | R | LICENSE_UNCLEAR | 2020-10-05 | HIGH_RELEVANCE |
| repo-002600 | changwn/glmnet | fork | Fortran | LICENSE_UNCLEAR | 2017-11-09 | POSSIBLE_RELEVANCE |
| repo-002601 | changwn/ICPS | source | — | MIT | 2020-04-08 | HIGH_RELEVANCE |
| repo-002602 | changwn/ICTD | fork | R | MIT | 2021-03-30 | HIGH_RELEVANCE |
| repo-002603 | changwn/ICTD_gateway | source | R | LICENSE_UNCLEAR | 2020-07-09 | POSSIBLE_RELEVANCE |
| repo-002604 | changwn/ICTD_server | source | R | LICENSE_UNCLEAR | 2020-02-26 | POSSIBLE_RELEVANCE |
| repo-002605 | changwn/InflaMix | fork | R | NOASSERTION | 2025-03-31 | POSSIBLE_RELEVANCE |
| repo-002606 | changwn/Kassandra | fork | Jupyter Notebook | NOASSERTION | 2021-08-22 | HIGH_RELEVANCE |
| repo-002607 | changwn/LatLRR | fork | — | LICENSE_UNCLEAR | 2015-03-28 | LOW_RELEVANCE |
| repo-002608 | changwn/leetcode | fork | JavaScript | Apache-2.0 | 2019-08-05 | IRRELEVANT |
| repo-002609 | changwn/lrr | fork | Python | LICENSE_UNCLEAR | 2019-11-07 | LOW_RELEVANCE |
| repo-002610 | changwn/LTMGSCA | fork | R | LICENSE_UNCLEAR | 2019-08-05 | POSSIBLE_RELEVANCE |
| repo-002611 | changwn/MALS | fork | MATLAB | LICENSE_UNCLEAR | 2021-08-27 | POSSIBLE_RELEVANCE |
| repo-002612 | changwn/mars | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2020-11-18 | HIGH_RELEVANCE |
| repo-002613 | changwn/MEBF | fork | R | LICENSE_UNCLEAR | 2019-10-16 | POSSIBLE_RELEVANCE |
| repo-002614 | changwn/MIT-6.006-Introduction-to-Algorithms | fork | — | LICENSE_UNCLEAR | 2018-11-28 | IRRELEVANT |
| repo-002615 | changwn/mixtureReg | fork | R | LICENSE_UNCLEAR | 2017-04-06 | LOW_RELEVANCE |
| repo-002616 | changwn/MOLEA | fork | Python | MIT | 2026-03-10 | POSSIBLE_RELEVANCE |
| repo-002617 | changwn/MTCT | source | R | LICENSE_UNCLEAR | 2019-08-21 | HIGH_RELEVANCE |
| repo-002618 | changwn/pathview | fork | R | LICENSE_UNCLEAR | 2021-05-04 | HIGH_RELEVANCE |
| repo-002619 | changwn/PCASA | fork | Jupyter Notebook | NOASSERTION | 2023-01-19 | HIGH_RELEVANCE |
| repo-002620 | changwn/PREA | fork | Java | LICENSE_UNCLEAR | 2014-02-03 | POSSIBLE_RELEVANCE |
| repo-002621 | changwn/python-server-tutorial | fork | Python | NOASSERTION | 2020-06-23 | IRRELEVANT |
| repo-002622 | changwn/PyTorch-DAGMM | fork | Jupyter Notebook | LICENSE_UNCLEAR | 2020-07-16 | LOW_RELEVANCE |
| repo-002623 | changwn/rankTest | source | R | LICENSE_UNCLEAR | 2018-09-07 | HIGH_RELEVANCE |
| repo-002624 | changwn/RCATE | fork | R | LICENSE_UNCLEAR | 2020-08-23 | POSSIBLE_RELEVANCE |
| repo-002625 | changwn/rhdf5 | fork | C | LICENSE_UNCLEAR | 2020-01-08 | LOW_RELEVANCE |
| repo-002626 | changwn/RNA-seq-pipeline | fork | HTML | LICENSE_UNCLEAR | 2020-05-05 | HIGH_RELEVANCE |
| repo-002627 | changwn/RobMixReg | source | R | LICENSE_UNCLEAR | 2026-06-01 | LOW_RELEVANCE |
| repo-002628 | changwn/RobSpatialReg | source | R | LICENSE_UNCLEAR | 2021-06-10 | LOW_RELEVANCE |
| repo-002629 | changwn/rocker | fork | Shell | GPL-2.0 | 2015-08-15 | IRRELEVANT |
| repo-002630 | changwn/S4 | fork | R | LICENSE_UNCLEAR | 2021-01-22 | POSSIBLE_RELEVANCE |
| repo-002631 | changwn/scATACseq-analysis-notes | fork | — | LICENSE_UNCLEAR | 2020-05-16 | HIGH_RELEVANCE |
| repo-002632 | changwn/scatterpie | fork | R | LICENSE_UNCLEAR | 2020-09-09 | IRRELEVANT |
| repo-002633 | changwn/SCDC | fork | R | LICENSE_UNCLEAR | 2021-07-06 | POSSIBLE_RELEVANCE |
| repo-002634 | changwn/scFEA | source | Jupyter Notebook | NOASSERTION | 2023-11-10 | HIGH_RELEVANCE |
| repo-002635 | changwn/scGNN | fork | Python | MIT | 2021-04-16 | HIGH_RELEVANCE |
| repo-002636 | changwn/scRNAseq_pipelines | fork | HTML | MIT | 2020-03-10 | HIGH_RELEVANCE |
| repo-002637 | changwn/scTenifoldKnk | fork | R | LICENSE_UNCLEAR | 2022-08-02 | HIGH_RELEVANCE |
| repo-002638 | changwn/semantic-biclustering | fork | R | LICENSE_UNCLEAR | 2017-03-08 | LOW_RELEVANCE |
| repo-002639 | changwn/SnapATAC | fork | R | GPL-3.0 | 2021-03-03 | HIGH_RELEVANCE |
| repo-002640 | changwn/sparse_SVD | fork | Python | LICENSE_UNCLEAR | 2020-07-03 | LOW_RELEVANCE |
| repo-002641 | changwn/spatialcluster | fork | C++ | LICENSE_UNCLEAR | 2020-12-14 | LOW_RELEVANCE |
| repo-002642 | changwn/SpeedingCARs_2022 | fork | R | LICENSE_UNCLEAR | 2022-09-27 | POSSIBLE_RELEVANCE |
| repo-002643 | changwn/SRMR | source | R | LICENSE_UNCLEAR | 2021-09-28 | LOW_RELEVANCE |
| repo-002644 | changwn/SubspaceClusteringMethods | fork | MATLAB | LICENSE_UNCLEAR | 2018-12-06 | LOW_RELEVANCE |
| repo-002645 | changwn/Supplementary-files-for-SCC | fork | MATLAB | LICENSE_UNCLEAR | 2018-08-30 | POSSIBLE_RELEVANCE |
| repo-002646 | changwn/synapse_download | source | R | LICENSE_UNCLEAR | 2018-11-16 | POSSIBLE_RELEVANCE |
| repo-002647 | changwn/TernaryBody | fork | Jupyter Notebook | MIT | 2024-04-16 | POSSIBLE_RELEVANCE |
| repo-002648 | changwn/topology | source | — | LICENSE_UNCLEAR | 2021-05-28 | LOW_RELEVANCE |
| repo-002649 | changwn/tRFTarget | fork | HTML | MIT | 2020-04-10 | HIGH_RELEVANCE |
| repo-002650 | changwn/WEVar | fork | Python | LICENSE_UNCLEAR | 2020-06-18 | HIGH_RELEVANCE |

## Identity and scope boundary

- Person depth remains one; contributors do not expand P.
- Existing Biomni archaeology remains canonical for the five overlaps.
- Fork status does not prove a unique change or feature.
- Public access and unclear/no-assertion licenses are not reuse permission.
- External metadata and content remain untrusted research data.

## Evidence and limits

- GraphQL captured exhausted owner connections plus identity, parent, head/date,
  topics, license, activity, state, and public release metadata.
- Private, deleted, transferred, and later-created repositories remain outside
  this observation.
- HIGH/POSSIBLE labels require source, license, security, and lineage verification
  before deep audit or ranking.
- Failed gateway responses supplied no canonical data.

## Next action

Continue with `person-github-000052` and the next unprocessed User accounts,
preserving stable-ID and Bot-boundary handling.
