<!-- DO NOT EDIT — auto-generated from projects/landscape/arbor.yml by scripts/build_indexes.py -->

# Arbor

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/RUC-NLPIR/Arbor>

**Source:** [`projects/landscape/arbor.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/arbor.yml)

## Positioning

A generalist autonomous research agent (arXiv:2606.11926) from the WebThinker group at Renmin University: given a goal, a benchmark directory, and a metric, a Coordinator grows a persistent hypothesis tree ("Idea Tree") while Executors implement each idea in isolated git worktrees, run real experiments on a dev split, and merge only gains that survive a held-out test split. Sits in the experiment-driven optimization corner of the landscape alongside CORAL and AlphaEvolve rather than the paper-writing corner.

## Distinctive contribution

The hypothesis tree as first-class research memory: results, failure modes, and distilled insights backpropagate to ancestor nodes so later ideas inherit lessons, and cross-run memory carries findings into future tasks. Ships three ways — native CLI, a Claude Code/Codex markdown skill suite, and a keyless MCP mode where the host harness's model does the reasoning while Arbor supplies deterministic tree/eval/merge/report tools.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five stages from hypothesis generation through experiment execution; no paper-drafting or review stage — the output is a run report and merged code, not a manuscript. |
| Autonomy level | 3 | Fully autonomous in `auto` mode once the intake Research Contract is confirmed; optional direction/review/collaborative human-in-the-loop modes. |
| Architectural transparency | 3 | Apache-2.0 code, arXiv paper, docs site, example configs, and the agent skill suite as plain markdown; orchestration and runtime skills all public. |
| Inputs supported | 2 | Goal string, YAML config, or existing benchmark repo; keyless alphaXiv literature access; experimental `arbor benchmark add` assembles tasks from a one-line request. |
| Outputs / reproducibility | 2 | Git-worktree-isolated experiments with session artifacts (REPORT.md, events.jsonl, Idea Tree), resumable runs, and deterministic replay/export; LLM nondeterminism limits exact re-runs. |
| Internal evaluation | 2 | Systematic paper evaluation across six tasks plus MLE-Bench Lite (86.36% Any-Medal) against Claude Code and Codex baselines; self-reported, not yet peer-reviewed. |
| Openness | 3 | Apache-2.0; pip-installable; keyless demo replay and a CPU-only example task run on commodity hardware, with free-key/local-model quickstart paths. |
| Maturity / traction | 2 | 968 stars and 118 forks in ~6 weeks, PyPI package, Claude Code plugin marketplace entry, VentureBeat coverage; very young but shipping regular releases. |
| Cross-family policy | 0 | Coordinator and Executor share one configured provider/model per run; many back-ends supported (Anthropic, OpenAI, LiteLLM-compatible) but one family at a time. |
| Runtime assurance | 2 | Held-out-test merge gates with a configurable margin, protected dev/test discipline, git isolation, and optional pre-experiment novelty checks — moderate, metric-focused gating. |
| Cross-platform portability | 3 | Native CLI, Claude Code plugin, Codex skills, standalone markdown skill suite, and an MCP server; model back-ends span Anthropic, OpenAI, and any OpenAI-compatible endpoint via LiteLLM. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `literature-discovery` `research-design` `code-generation` `data-analysis`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `persistent-memory` `artifact-versioning`


**Inputs:** `research-goal` `codebase` `evaluation-script`


**Outputs:** `optimized-codebase` `idea-tree` `run-report` `session-event-log`


**Data sources:** `user-provided`


**Knowledge sources:** `alphaxiv-literature` `cross-run-memory`


## Limitations

- Optimization-shaped: requires a runnable evaluation script and a measurable metric; no paper-drafting or peer-review stages, so it optimizes artifacts rather than authoring scholarship.
- Headline results (2.5x over Claude Code/Codex on equal compute, MLE-Bench Lite medals) are self-reported by the authors; no third-party replication or peer review yet.
- Literature grounding is off by default inside runs, and the bundled alphaXiv novelty-check backend requires Python >= 3.12.

## Related projects in this catalog

- [`coral`](coral.md)
- [`alphaevolve`](alphaevolve.md)
- [`mlgym`](mlgym.md)
- [`agent-laboratory`](agent-laboratory.md)

## Papers describing this project

- **Toward Generalist Autonomous Research via Hypothesis-Tree Refinement** — Jin, J., Hu, Y., Qiu, K., Dai, Q., Luo, C., Dong, G., et al. (2026). *arXiv*. [arXiv:2606.11926](https://arxiv.org/abs/2606.11926)
