<!-- DO NOT EDIT — auto-generated from projects/landscape/core-bench.yml by scripts/build_indexes.py -->

# CORE-Bench

`external` · status: `dormant` · focus: `replication` · discipline: `general` · started: 2024

**Project page:** <https://github.com/siegelz/core-bench>

**Source:** [`projects/landscape/core-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/core-bench.yml)

## Positioning

A computational-reproducibility benchmark: 270 tasks built from 90 published papers (Code Ocean capsules) in computer science, social science and medicine, written in Python or R, each asking an agent to reproduce the reported results and then answer written and vision-based questions about the output into a supplied `report.json`. Three difficulty tiers strip away scaffolding on the same 90 papers: CORE-Bench-Easy hands the agent the complete output of a successful run, Medium supplies the Dockerfile plus a README, Hard gives only the README so the agent must install dependencies and work out the run command itself. Sits in the RISE evaluation-infrastructure layer next to socsci-repro-bench, reprorepo and NatureBench, and is the reference benchmark for the reproducibility end of that layer.

## Distinctive contribution

The tiered design isolates *where* reproducibility agents fail rather than reporting one pass rate: with the same papers at every level, CORE-Agent on GPT-4o scores 60.00% (Easy), 57.78% (Medium) and 21.48% (Hard), which localises the bottleneck in environment setup rather than in reading results, while the split between 87.88% correct on written questions and 59.26% on vision questions isolates figure reading as a separate failure mode. It also ships a task-specialised agent (CORE-Agent, derived from a general AutoGPT baseline) alongside the harness and publishes its own cost curve — $0.6407 / $1.2005 / $2.9643 average per task under a $4 cap — one of the few benchmarks in the catalog that reports what running it costs.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage (replication): an evaluation target for reproducibility agents, not a system that produces scholarship. |
| Autonomy level | 2 | Once configured (Azure credentials or local privileged Docker, model API keys), the harness runs agents and grades report.json against ground truth with no per-task human intervention; the score describes the bundled harness and baseline agents, not a research pipeline. |
| Architectural transparency | 3 | MIT-licensed harness, both baseline agent implementations (AutoGPT and CORE-Agent with GPT-4o), the task dataset, config templates and the paper-figures notebook are all in the repo. |
| Inputs supported | 1 | One task format (capsule plus question set, differing only by difficulty tier) with bundled code and data; no literature corpus, no external data connectors, no paper PDF given to the agent. |
| Outputs / reproducibility | 2 | Per-task report.json is graded deterministically against ground truth and results are reported with 95% prediction intervals over stochastic runs, but the pinned Azure/Docker environment is no longer maintained and agent runs are not bit-reproducible. |
| Internal evaluation | 3 | Published in Transactions on Machine Learning Research (OpenReview BsMMc4MEGS) with a systematic two-agent x two-model evaluation across three tiers; 111 citations on Semantic Scholar and adopted as a task suite by the Holistic Agent Leaderboard (arXiv:2510.11977). |
| Openness | 2 | MIT license and a publicly downloadable test set (GPG-encrypted with the published password 'reproducibility'), but reproducing the reported numbers needs paid OpenAI credits plus Azure VMs or privileged Docker-in-Docker — not commodity-hardware reproducible. |
| Maturity / traction | 3 | Peer-reviewed in TMLR, 111 citations, 79 stars / 9 forks, and folded into the Holistic Agent Leaderboard harness — sustained external adoption, though this repo itself is now explicitly deprecated. |
| Cross-family policy | 0 | Agent-agnostic harness with no cross-family requirement or recommendation; the published baselines are GPT-4o and GPT-4o-mini only. |
| Runtime assurance | 1 | Light in-flight mechanisms only: Docker/VM isolation per task, a $4-per-task cost cap, and schema-shaped report.json validation; correctness checking is post-hoc grading. |
| Cross-platform portability | 2 | Two documented execution environments (local privileged Docker and parallelised Azure VMs) behind an agent-agnostic interface (any agent that writes report.json), with a third path via the Holistic Agent Leaderboard harness; baseline agents are OpenAI-only. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `replication`


**Architectural features:** `tool-use`


**Inputs:** `code-capsule` `task-questions` `dockerfile-or-readme`


**Outputs:** `task-reports` `accuracy-scores`


**Data sources:** `code-ocean-capsules`


## Limitations

- Deprecated: the README states 'this current harness is no longer actively maintained' and directs users to the Holistic Agent Leaderboard harness; last push 2025-11-23, 8 open issues.
- Running it requires paid infrastructure — Azure VMs (Standard_E2as_v5 / NC4as_T4_v3) or local Docker-in-Docker with --privileged, plus model API credits averaging $2.96 per Hard task.
- Tasks are drawn from Code Ocean capsules, i.e. papers that already shipped a runnable container, so accuracy on CORE-Bench overstates reproducibility on the general published literature.
- Measures reproducing the code's own output, not whether that output matches the paper's claims — the assessment question REPRO-Bench targets instead.
- Published baselines are 2024 models (GPT-4o, GPT-4o-mini); the reported 21.48% Hard-tier ceiling is stale as a capability estimate.
- The test set is GPG-encrypted with a password published in the README, which deters casual training-data contamination but does not prevent it.

## Related projects in this catalog

- [`repro-bench`](repro-bench.md)
- [`socsci-repro-bench`](socsci-repro-bench.md)
- [`reprorepo`](reprorepo.md)
- [`naturebench`](naturebench.md)
- [`paper2code`](paper2code.md)

## Papers describing this project

- **CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark** — Siegel, Z. S., Kapoor, S., Nadgir, N., Stroebl, B., Narayanan, A. (2024). *Transactions on Machine Learning Research (TMLR)*. [arXiv:2409.11363](https://arxiv.org/abs/2409.11363)

## Related references (literature catalog)

- Siegel, Z. S. et al. (2024). [*CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark*](../papers/notes/siegel2024corebench.md) `siegel2024corebench`
