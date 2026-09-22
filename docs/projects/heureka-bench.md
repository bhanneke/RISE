<!-- DO NOT EDIT — auto-generated from projects/landscape/heureka-bench.yml by scripts/build_indexes.py -->

# HeurekaBench

`external` · status: `dormant` · focus: `analysis` · discipline: `biomedical` · started: 2025

**Project page:** <https://github.com/mlbio-epfl/HeurekaBench>

**Source:** [`projects/landscape/heureka-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/heureka-bench.yml)

## Positioning

A framework for *constructing* AI-co-scientist benchmarks rather than a fixed benchmark: a semi-automated pipeline uses multiple LLMs to mine validated insights out of published papers, reformulate them as open-ended research questions over the papers' own experimental datasets, and validate the resulting question-answer pairs against the published findings. The instantiation shipped in the repo, sc-HeurekaBench, does this for single-cell biology — 44 GB of datasets, six question-set variants (multiple-choice and open-ended, each in lite, full and tool-usage form), an LLM judge, and baseline runners for plain LLMs, CellVoyager and Biomni 0.0.6. Sits in the RISE evaluation-infrastructure layer alongside AstaBench, AIRS-Bench and LifeSciBench, but one level up: it is the recipe, not the target set.

## Distinctive contribution

The only entry in the catalog that publishes the *benchmark- construction* pipeline itself (`benchmark_creation/`, `benchmark_validation/`, `geval_prompts/`), so the recipe — published finding plus the study's raw data becomes a graded open-ended agent task — is portable to any field with data-backed papers, including economics replication packages, rather than being locked to the one domain it was instantiated in. Its headline empirical claim is architectural rather than a ranking: adding a critic module improves ill-formed responses from open-weight LLM agents by up to 22%, isolating response well-formedness from research ability.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure: the declared stages describe the tasks it constructs and grades, not scholarship it produces itself — no paper, code artifact, or finding leaves the framework. |
| Autonomy level | 0 | The construction pipeline is explicitly semi-automated (LLM generation with validation against published results) and the eval harness is a set of scripts; all research agency lives in the agents being measured. |
| Architectural transparency | 3 | Repo ships the construction pipeline, the validation stage, the G-Eval judge prompts (`geval_prompts/`), the answer-extraction and scoring scripts, and both baseline runners (`run_baselines/`, `run_biomni/`) — code and prompts, not just an artifact drop. |
| Inputs supported | 2 | Six question-set variants (mcq/oeq × lite/full/tool-usage) over 44 GB of real experimental data, runnable against three model paths (vLLM open-weights, closed APIs) and two agent adapters (CellVoyager, Biomni). |
| Outputs / reproducibility | 2 | Question sets are fixed JSON files and the dataset archive ships a SHA256 checksum, but distribution is six hand-reassembled Google Drive parts with no DOI or versioned release, and judge-scored open-ended answers are not bit-reproducible. |
| Internal evaluation | 3 | Accepted to ICLR 2026 (verified on the arXiv listing and the repo's own `@inproceedings` citation block) — peer-reviewed external validation, with baseline agents scored in the paper. |
| Openness | 1 | No LICENSE, LICENSE.md or COPYING file exists anywhere in the repo (verified 2026-09-08 via the GitHub contents API and the rendered page) and the API reports license null, so reuse terms default to all-rights-reserved despite the code being public. |
| Maturity / traction | 1 | 20 stars, 2 forks, 10 commits, no code push since 2026-02-16, no leaderboard, and the only instantiation is the authors' own single-cell set — a single-lab research artifact. |
| Cross-family policy | 0 | Model-agnostic evaluation target with no executor/reviewer pairing of its own; the construction pipeline is described as using multiple LLMs but the README does not document which families, so cross-family cannot be credited. |
| Runtime assurance | 1 | Generated questions are validated against the published findings at construction time and an optional critic module screens ill-formed agent answers — single-pass checks, with no gating on failure during an agent run. |
| Cross-platform portability | 2 | Runs against open-weight models via vLLM plus OpenAI/Anthropic APIs and two agent adapters, but the harness assumes a conda environment and the sc-HeurekaBench data layout. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-synthesis` `hypothesis-generation` `research-design` `data-analysis` `code-generation`


**Architectural features:** `multi-agent` `tool-use`


**Inputs:** `source-papers` `experimental-datasets` `agent-implementation`


**Outputs:** `question-answer-sets` `evaluation-scores`


**Data sources:** `single-cell-datasets`


**Knowledge sources:** `source-papers`


## Limitations

- No license file anywhere in the repo (verified 2026-09-08) — the sweep's 'license unconfirmed' flag resolves to 'none declared', so reuse is legally unresolved even though the code and data are downloadable.
- The framework claim is domain-general but the only instantiation is single-cell biology; portability to economics or other fields is argued, not demonstrated.
- The 44 GB dataset is distributed as six Google Drive archive parts that must be concatenated by hand — no DOI, no HuggingFace mirror, fragile hosting for a benchmark meant to be re-run.
- README does not state how many questions each of the six variants contains, so benchmark size cannot be verified from the repo.
- No leaderboard and no push to code since 2026-02-16; scores exist only inside the ICLR paper.
- Open-ended grading depends on an LLM judge whose own accuracy is not separately validated against human raters in the repo.

## Related projects in this catalog

- [`lifescibench`](lifescibench.md)
- [`bixbench3`](bixbench3.md)
- [`asta-bench`](asta-bench.md)
- [`airs-bench`](airs-bench.md)

## Papers describing this project

- **HeurekaBench: A Benchmarking Framework for AI Co-scientist** — Panigrahi, S. S., Videnović, J., Brbić, M. (2026). *ICLR 2026*. [arXiv:2601.01678](https://arxiv.org/abs/2601.01678)

## Related references (literature catalog)

- `panigrahi2026heurekabench` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
