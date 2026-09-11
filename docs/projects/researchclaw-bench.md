<!-- DO NOT EDIT — auto-generated from projects/landscape/researchclaw-bench.yml by scripts/build_indexes.py -->

# ResearchClawBench

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/InternScience/ResearchClawBench>

**Source:** [`projects/landscape/researchclaw-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/researchclaw-bench.yml)

## Positioning

A benchmark for end-to-end autonomous research: 40 tasks (4 each across astronomy, chemistry, earth science, energy, information science, life science, materials science, mathematics, neuroscience and physics), each anchored to a real published paper and shipped with that paper's raw data and related literature. Two stages: the agent explores the data, writes code and produces a research report with figures and methodology; then a multimodal LLM judge scores the report against the original paper using an expert-written weighted rubric, in a quantitative mode (numbers and metrics) and a diagnostic mode (theoretical reasoning and evidence quality). Sits in the RISE evaluation-infrastructure layer alongside AstaBench, AIRS-Bench and AARRI-Bench.

## Distinctive contribution

The scale is calibrated to human work rather than to a pass rate: 0-100 where 50 means parity with the published paper and 70+ means surpassing it, which turns the leaderboard into a direct readout of the autonomy gap — the companion paper's best autonomous agent (Claude Code) averages 21.5, i.e. under half of parity. It also ships the harness rather than only the tasks: built-in adapters for nine agent runtimes (Claude Code, Codex CLI, ARIS Codex, OpenClaw, Nanobot, EvoScientist, ResearchClaw, LingTai) plus a ResearchHarness baseline for arbitrary standalone LLMs, a Hugging Face dataset carrying 16 community-contributed tasks on top of the 40 base tasks, and a hosted board with a task-submission route.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure: it measures whether other systems can carry a task from raw data to a report, and produces no scholarship of its own. |
| Autonomy level | 0 | Static task bundles plus a scoring harness; all agency sits in the agents being evaluated. |
| Architectural transparency | 3 | MIT-licensed with tasks/, evaluation/, eval_configs/, workspaces/ and the weighted rubrics public, nine runtime adapters in-repo, and a 51-author paper documenting the two-stage judging design. |
| Inputs supported | 2 | Each of the 40 tasks bundles raw data with the related literature, 16 further tasks arrive via the Hugging Face dataset, and nine documented adapters accept different agent runtimes; no private-corpus support, so short of the top band. |
| Outputs / reproducibility | 2 | Runs persist the agent's report, figures and code in workspaces/ alongside per-criterion rubric scores; LLM-judge scoring plus agent stochasticity means a rerun reproduces the procedure, not the number. |
| Internal evaluation | 2 | The companion arXiv preprint scores nine agent integrations and a frontier-LLM sweep on all 40 tasks (best agent 21.5, best LLM 20.7, frontier average 26.5) and names three failure modes; five arXiv versions but no peer-reviewed venue or third-party replication found. |
| Openness | 2 | MIT license with tasks, rubrics, harness and adapters public and the dataset on Hugging Face, but a leaderboard-grade run needs a paid frontier agent working a full study per task, so the demonstrated examples are not reproducible on commodity hardware. |
| Maturity / traction | 2 | 258 stars, 22 forks, 184 commits, pushed 2026-09-05, with a hosted leaderboard, a Hugging Face dataset and a community task-contribution route already used for 16 tasks — beta-stage with external participation, single-consortium origin. |
| Cross-family policy | 0 | Model-agnostic target with no executor/reviewer pairing of its own; the judge model is set in eval_configs but nothing requires or recommends that it differ from the agent under test. |
| Runtime assurance | 1 | Rubric judging is post-hoc (dimension 6); in flight there is only workspace isolation and task/eval config validation, with no gate that stops a run producing an ungrounded report. |
| Cross-platform portability | 3 | Nine agent-runtime adapters ship in-repo plus a generic ResearchHarness path for standalone LLMs — well past the five-environment threshold, and the task format is a data bundle rather than framework-specific code. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `research-design` `data-analysis` `code-generation` `paper-drafting` `replication`



**Inputs:** `task-bundle` `raw-data` `source-literature` `agent-adapter`


**Outputs:** `rubric-scores` `agent-research-reports` `leaderboard-entries`


**Data sources:** `task-bundled-raw-data` `huggingface-dataset`


**Knowledge sources:** `source-papers` `task-bundled-literature`


## Limitations

- Could not confirm a populated leaderboard: the hosted board at internscience.github.io/ResearchClawBench-Home renders client-side and returned no scored runs when fetched on 2026-09-08, so the cross-agent scores are verifiable only from the preprint, not from the live board.
- Scoring depends on a multimodal LLM judge with no stated model-family separation from the agent under test, so self-favouring bias is not ruled out; the rubrics are expert-written but the grader is not.
- No economics or social-science tasks. The ten domains are natural sciences plus mathematics and information science, and 'matching the paper' there means matching a measured result — not defending an identification strategy, which is where economics agents fail.
- Anchoring to published findings makes the target a moving one and rewards re-discovery: a task is scored against what the original authors concluded, which penalises a correct agent that disagrees with a flawed paper.
- Per-task cost and runtime are not documented in the repository, so the price of a full 40-task submission cannot be estimated from public material.

## Related projects in this catalog

- [`asta-bench`](asta-bench.md)
- [`airs-bench`](airs-bench.md)
- [`aarri-bench`](aarri-bench.md)
- [`evoscientist`](evoscientist.md)

## Papers describing this project

- **ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research** — Xu, W., Li, S., Ye, T., Cao, Q., et al. (2026). *arXiv*. [arXiv:2606.07591](https://arxiv.org/abs/2606.07591)

## Related references (literature catalog)

- Xu, W. et al. (2026). [*ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research*](../papers/notes/xu2026researchclawbench.md) `xu2026researchclawbench`
