<!-- DO NOT EDIT — auto-generated from projects/landscape/deepresearch-bench.yml by scripts/build_indexes.py -->

# DeepResearch Bench

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2025

**Project page:** <https://github.com/Ayanami0730/deep_research_bench>

**Licence:** `Apache-2.0 (LICENSE file; the README badge says MIT)`

**Source:** [`projects/landscape/deepresearch-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/deepresearch-bench.yml)

## Positioning

An ICLR 2026 benchmark of 100 PhD-level research tasks (50 Chinese, 50 English) across 22 fields, written by domain experts to match real user query distributions, for evaluating "Deep Research Agent" (DRA) systems — i.e., web-search-and-synthesis agents rather than wet-lab or formal-modeling systems. Evaluates agent *outputs* (submitted reports) rather than running agents itself, so it sits downstream of systems like GPT-Researcher, STORM, or OpenAI/Gemini Deep Research in the RISE evaluation-infrastructure layer.

## Distinctive contribution

Two purpose-built automated evaluators instead of a single LLM judge: RACE (Reference-based Adaptive Criteria-driven Evaluation), which generates task-specific criteria across comprehensiveness, insight/depth, instruction-following and readability and scores reports against reference reports with task-adapted weights; and FACT (Framework for Factual Abundance and Citation Trustworthiness), which extracts statement-URL pairs, scrapes cited sources, and reports citation accuracy and effective-citation counts per task. The authors report strong agreement between RACE/FACT and human judges, and the repo has run a maintained public leaderboard since 2025 (migrated its judge model from Gemini-2.5-Pro to GPT-5.5 in 2026 after a Google API deprecation).

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure; scores the literature-discovery/synthesis quality of agents under test, does not itself produce scholarship. |
| Autonomy level | 0 | Static query set plus an automated scoring pipeline (RACE + FACT); agency lives entirely in the deep-research agent being evaluated. |
| Architectural transparency | 3 | Public code and data (query set, evaluation criteria, RACE/FACT scripts), with the evaluator-model migration history documented in-repo and a companion paper describing both scoring methodologies. |
| Inputs supported | 1 | One input form — a JSON report per query matching the required schema — with no requirement on how the agent under test sources its literature or data. |
| Outputs / reproducibility | 2 | Fixed 100-task query set with versioned reference/criteria data and a public leaderboard submission protocol (reproducibility link, raw articles, model metadata required); judge-model drift (Gemini to GPT-5.5) means absolute scores are not stable across the benchmark's own history. |
| Internal evaluation | 2 | Systematic cross-model evaluation reported for the official leaderboard with claimed strong RACE/FACT-vs-human agreement; peer-reviewed via ICLR 2026 acceptance, though human-judgment validation numbers are the authors' own and not independently replicated in this catalog. |
| Openness | 2 | Code and benchmark data are public under Apache-2.0 (the LICENSE file; the README badge says MIT, checked 2026-11-02); official leaderboard submission requires a temporary GPT-5.5 access key from the maintainers. |
| Maturity / traction | 2 | 848 stars / 87 forks / 47 commits as of 2026-11-01, 21 open issues, ICLR 2026 acceptance, and an actively maintained leaderboard with a documented 2026 evaluator migration — real external usage, though governed by a single academic group. |
| Cross-family policy | 0 | Not applicable — model-agnostic evaluation target; the benchmark itself uses a fixed judge model (GPT-5.5) rather than a cross-family executor/reviewer pairing. |
| Runtime assurance | 0 | No runtime mechanism — FACT's citation checking and RACE's criteria scoring are both post-hoc evaluation of a finished report, not an in-flight gate during agent execution. |
| Cross-platform portability | 1 | Supports OpenRouter or direct OpenAI backends for the evaluator, and accepts any agent's output via a documented JSON schema, but ships as a single Python evaluation pipeline, not a multi-runtime protocol. |

*Scored on 2026-11-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis`



**Inputs:** `agent-implementation` `task-specification`


**Outputs:** `evaluation-metrics` `citation-accuracy-scores`


**Data sources:** `benchmark-datasets`


**Knowledge sources:** `reference-reports`


## Limitations

- The README badge says MIT while the LICENSE file is Apache-2.0; the LICENSE file governs.
- Evaluates web-search-and-synthesis 'deep research' agents specifically — out of scope for systems that don't produce a written report (e.g., pure code/experiment agents).
- Judge-model dependency: the 2026 forced migration from Gemini-2.5-Pro to GPT-5.5 after a Google deprecation shows leaderboard scores are not judge-model-stable over time; legacy results live on a separate Gemini-2.5 branch.
- Official leaderboard submission requires a maintainer-issued temporary API key, adding friction beyond self-hosted evaluation.

## Related projects in this catalog

- [`gpt-researcher`](gpt-researcher.md)
- [`storm`](storm.md)
- [`open-scholar`](open-scholar.md)
- [`airs-bench`](airs-bench.md)

## Papers describing this project

- **DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents** — Du, M., Xu, B., et al. (2026). *ICLR 2026*. [arXiv:2506.11763](https://arxiv.org/abs/2506.11763)
