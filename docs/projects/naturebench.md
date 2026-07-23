<!-- DO NOT EDIT — auto-generated from projects/landscape/naturebench.yml by scripts/build_indexes.py -->

# NatureBench

`external` · status: `active` · focus: `analysis` · discipline: `general` · started: 2026

**Project page:** <https://github.com/FrontisAI/NatureBench>

**Source:** [`projects/landscape/naturebench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/naturebench.yml)

## Positioning

A cross-discipline benchmark (arXiv:2606.24530) of 90 tasks distilled from peer-reviewed Nature-family papers across six scientific domains, asking whether AI coding agents can match — or surpass — the published state of the art. Each task is a containerized package (task brief, the paper's dataset, a held-out test set with hidden ground truth, an automated evaluator) built by NatureGym, an automated Claude-Code-skills pipeline that converts a published paper into an executable Docker task. Sits in the RISE evaluation-infrastructure layer alongside AstaBench, MLGym, and EconCS Bench, but targets empirical scientific ML with executable, SOTA-anchored scoring.

## Distinctive contribution

Scores agents against each source paper's *reported SOTA* (Surpass-SOTA rate) rather than mere reproduction, with an information firewall that strips the source method from the task brief so agents must discover solutions. Ships a full harness with built-in adapters for Claude Code, Codex CLI, and Gemini CLI, a post-hoc validity judge, and a public leaderboard: across twelve harness-model configurations the best reaches a 17.8% Surpass-SOTA rate, with failures dominated by method-selection errors.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Benchmark / evaluation infrastructure; produces task packages and scores, not scholarship. |
| Autonomy level | 0 | Evaluation harness — agency lives in the agents under test; NatureGym automates task construction but is a build pipeline, not a research agent. |
| Architectural transparency | 3 | Full code: harness, agent adapters, evaluators, post-hoc judge, NatureGym construction skills, docs, HuggingFace dataset, and public leaderboard. |
| Inputs supported | 1 | Single input form (containerized task package) with each task bundling the source paper's dataset; no broader literature or private-corpus access. |
| Outputs / reproducibility | 2 | Dockerized tasks, hidden test sets, versioned dataset, and persisted results directories; agent nondeterminism precludes exact reruns. |
| Internal evaluation | 2 | Systematic evaluation of twelve harness-model configurations with public leaderboard and failure analysis in the arXiv paper; not yet peer-reviewed. |
| Openness | 2 | MIT for original work (NOTICE-scoped); third-party task data under heterogeneous per-task licenses; full runs need agent API keys and 24-80 GB GPUs. |
| Maturity / traction | 1 | Young (June 2026) but active: 77 stars in the first month, a v2 paper revision, and a leaderboard refresh adding new models. |
| Cross-family policy | 1 | Post-hoc validity judge is configured independently of the executing agent, so cross-family judging is possible via config but neither default nor required. |
| Runtime assurance | 1 | Hidden-ground-truth evaluator plus a post-hoc validity judge screen scored outputs; no in-flight gating while the agent runs. |
| Cross-platform portability | 2 | Built-in adapters for Claude Code, Codex CLI, and Gemini CLI plus a documented custom-agent interface. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `code-generation`


**Architectural features:** `tool-use`


**Inputs:** `nature-family-papers` `coding-agent-configurations`


**Outputs:** `containerized-task-packages` `surpass-sota-scores` `leaderboard`


**Data sources:** `paper-datasets` `huggingface-dataset`


**Knowledge sources:** `source-papers`


## Limitations

- Heavy compute footprint: gpu_high tasks assume A100-class (80 GB) GPUs, so full benchmark runs are beyond commodity hardware.
- The information firewall removes the source method from task briefs, but the underlying Nature-family papers are public, so pretraining contamination cannot be ruled out.
- Third-party data bundled per task is governed by heterogeneous per-task license notices, complicating redistribution.

## Related projects in this catalog

- [`asta-bench`](asta-bench.md)
- [`mlgym`](mlgym.md)
- [`airs-bench`](airs-bench.md)
- [`lifescibench`](lifescibench.md)

## Papers describing this project

- **NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?** — Wang, Y., Cheng, L., Zuo, Y., Zeng, S., He, B., Jiang, C., et al. (2026). *arXiv*. [arXiv:2606.24530](https://arxiv.org/abs/2606.24530)
