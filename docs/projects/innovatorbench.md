<!-- DO NOT EDIT — auto-generated from projects/landscape/innovatorbench.yml by scripts/build_indexes.py -->

# InnovatorBench

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/GAIR-NLP/InnovatorBench>

**Licence:** `Apache-2.0`

**Source:** [`projects/landscape/innovatorbench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/innovatorbench.yml)

## Positioning

An ICLR 2026 benchmark-platform pair (arXiv:2510.27598) for end-to-end innovative LLM research: 20 tasks built from the open-source code of 14 published papers, spanning six research areas — data construction, data filtering, data augmentation, loss design, reward design, and scaffold construction. Agents work through an observe-reason-act loop on a companion execution environment (also called ResearchGym in the paper, distinct from the separately-maintained Anikethh/ResearchGym repo of the same name) and submit results for automated grading. Sits in the RISE evaluation-infrastructure layer alongside AIRS-Bench, MLGym, and the (separate) ResearchGym benchmark.

## Distinctive contribution

Targets genuinely open-ended *innovation* tasks (new loss functions, reward designs, data pipelines) rather than reproduction of a known result, with long time horizons (2h-36h) and multi-GPU/multi-node execution support plus a checkpoint/resume system for interrupted runs. The companion paper reports the ICLR abstract's finding that agents need over 11 hours to reach their best performance, and that Claude Sonnet 4, GPT-5, GLM-4.5, and Kimi-K2 all score non-zero but well below saturation (weighted final scores 5.35-24.01 on the public leaderboard, itself marked "under construction").

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure; scores the innovation ability of agents under test, does not itself produce scholarship. |
| Autonomy level | 0 | Static task environments plus a ReAct-agent reference implementation and grading harness; agency lives in the agent configuration being evaluated. |
| Architectural transparency | 3 | Public code (agents/, research_gym/, evaluations/, llm/), ICLR 2026 paper and slides documenting the six research domains, task construction from 14 papers, and leaderboard methodology. |
| Inputs supported | 1 | One input form — a YAML task/agent config pair run via main.py — against a bundled dataset path; no external literature or live data-source connector. |
| Outputs / reproducibility | 2 | Checkpoint/resume support and fixed task environments per run, with a leaderboard protocol for comparing agents; stochastic agent behavior and GPU/multi-node variance limit exact reruns. |
| Internal evaluation | 2 | Systematic evaluation of four frontier models (Claude Sonnet 4, GPT-5, GLM-4.5, Kimi-K2) reported in the ICLR 2026 paper with a public (in-progress) leaderboard; peer-reviewed via ICLR 2026 main-conference acceptance. |
| Openness | 1 | Apache-2.0 license, but demonstrated tasks require multi-GPU/multi-node setups and 2-36h runs — not reproducible on commodity hardware. |
| Maturity / traction | 1 | 17 stars / 1 fork / 8 commits as of 2026-11-01; ICLR 2026 main-conference acceptance (poster) gives it more standing than a workshop paper, but adoption outside the authors' group is not yet evident. |
| Cross-family policy | 0 | Not applicable — model-agnostic evaluation target; the paper benchmarks four different model families but the framework has no executor/reviewer pairing of its own. |
| Runtime assurance | 1 | Light — automated grading plus a checkpoint/resume system; no dedicated cheating/rule-violation inspector (unlike the separate Anikethh/ResearchGym) or claim-faithfulness gating. |
| Cross-platform portability | 1 | Supports OpenAI and Anthropic backends with a documented ReAct agent interface; DIY agent/eval substitution is supported, but this is a single Python framework, not a protocol-based multi-runtime design. |

*Scored on 2026-11-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation`



**Inputs:** `task-specification` `agent-implementation`


**Outputs:** `evaluation-metrics` `agent-trajectories`


**Data sources:** `benchmark-datasets`


**Knowledge sources:** `source-papers`


## Limitations

- Leaderboard explicitly marked 'under construction' at scoring date — scores may not be stable or comparable across submissions yet.
- Demonstrated runs require multi-GPU/multi-node infrastructure and long (2-36h) time budgets.
- Shares its companion-environment name ("ResearchGym") with an unrelated, separately-maintained benchmark (Anikethh/ResearchGym), which risks confusion when searching for either.
- Domain is ML/AI research only — no economics or social-science tasks.

## Related projects in this catalog

- [`researchgym`](researchgym.md)
- [`airs-bench`](airs-bench.md)
- [`mlgym`](mlgym.md)
- [`asta-bench`](asta-bench.md)

## Papers describing this project

- **InnovatorBench: Evaluating Agents' Ability to Conduct Innovative LLM Research** — Fu, D., Wu, et al. (2026). *ICLR 2026*. [arXiv:2510.27598](https://arxiv.org/abs/2510.27598)
