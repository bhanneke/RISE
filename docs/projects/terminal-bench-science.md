<!-- DO NOT EDIT — auto-generated from projects/landscape/terminal-bench-science.yml by scripts/build_indexes.py -->

# Terminal-Bench-Science

`external` · status: `active` · focus: `analysis` · discipline: `general` · started: 2026

**Project page:** <https://github.com/harbor-framework/terminal-bench-science>

**Licence:** `Apache-2.0`

**Source:** [`projects/landscape/terminal-bench-science.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/terminal-bench-science.yml)

## Positioning

A benchmark of 70 (growing toward 100+) expert-curated computational research workflows spanning life, physical, earth, mathematical, and engineering sciences, run through the Harbor agent-evaluation framework. It extends the Terminal-Bench line — already used internally by Anthropic, OpenAI, and Google DeepMind to evaluate coding agents — into science-specific terminal and data-analysis tasks, each drawn from a workflow a practicing researcher actually performed. Sits in RISE's evaluation-infrastructure layer alongside AstaBench, MLGym, and EconCS Bench, but targets hands-on scientific computing (run a pipeline, fit a model, reproduce a result) rather than literature synthesis, theory, or paper-writing.

## Distinctive contribution

Built from genuine researcher workflows rather than synthetic tasks, with a large open domain-expert review process (376 contributors across 22 countries via proposals/reviews/PRs) and direct lineage from a harness that frontier labs already use for their own coding agents — making results comparable across labs' internal evaluations and the public leaderboard alike.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Tasks cover data-analysis/code-generation/replication of real computational workflows (2-3 adjacent stages); no ideation, literature, or drafting stages evaluated. |
| Autonomy level | 0 | Static, expert-authored task set with oracle solutions curated via PR review; any agency under test belongs to the agents being benchmarked, not the benchmark itself. |
| Architectural transparency | 3 | Full task specs, oracle solutions, Harbor scoring harness, and sandbox configs are public under Apache-2.0. |
| Inputs supported | 1 | Single input form (a sandboxed terminal task) with a per-task dataset; no literature or cross-task knowledge access. |
| Outputs / reproducibility | 1 | Persists agent trajectories/logs and pass-fail scores per run; no end-to-end reproducibility guarantee for the underlying research task itself. |
| Internal evaluation | 2 | Automated oracle-based scoring via the Harbor harness with a public leaderboard; systematic but not yet externally validated as a predictor of real research capability. |
| Openness | 3 | Apache-2.0 license; tasks run end-to-end via the open-source Harbor CLI against sandboxed Modal/Daytona environments, demonstrated reproducible. |
| Maturity / traction | 2 | v0.1 released September 2026 but with substantial early traction — 656 stars, 388 forks, 376 contributors across 22 countries, and direct lineage from the already lab-adopted Terminal-Bench. |
| Cross-family policy | 0 | Not applicable — model-agnostic evaluation harness with no policy on how systems under test are built. |
| Runtime assurance | 0 | No in-flight research-pipeline integrity mechanism; oracle comparison is post-hoc grading of the agent run, not a runtime check within a research process. |
| Cross-platform portability | 2 | Harbor supports multiple agent harnesses/models (e.g., claude-code and others) and multiple sandbox backends (Modal, Daytona). |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `code-generation` `replication`



**Inputs:** `task-specification` `per-task-dataset`


**Outputs:** `agent-trajectories` `pass-fail-scores` `leaderboard-rankings`


**Data sources:** `per-task-research-datasets`


**Knowledge sources:** `contributor-research-workflows`


## Limitations

- v0.1 is small (70 tasks) and its domain mix reflects which experts volunteered tasks so far, not a principled sampling of scientific computing.
- Oracle-based pass/fail scoring may undercredit valid alternative solution paths in open-ended research tasks.
- No external validation yet of how well benchmark scores predict real-world research productivity.

## Related projects in this catalog

- [`econcs-bench`](econcs-bench.md)
- [`asta-bench`](asta-bench.md)
- [`mlgym`](mlgym.md)
- [`mle-bench`](mle-bench.md)
- [`core-bench`](core-bench.md)
