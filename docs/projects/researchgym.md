<!-- DO NOT EDIT — auto-generated from projects/landscape/researchgym.yml by scripts/build_indexes.py -->

# ResearchGym

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/Anikethh/ResearchGym>

**Licence:** `none`

!!! warning "No licence declared"
    The repository declares no licence, so its code cannot be reused,
    modified or redistributed without the maintainer's permission. RISE
    describes and links to the project; nothing from it is reproduced here.

**Source:** [`projects/landscape/researchgym.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/researchgym.yml)

## Positioning

A benchmark and execution environment (arXiv:2602.15112, ICLR 2026 Agents in the Wild Workshop) that turns five oral/spotlight papers from ICML, ICLR, and ACL into 39 containerized sub-tasks: each paper's dataset, evaluation harness, and baseline code are kept, but its proposed method is hidden, so an agent must propose a hypothesis, implement it, and beat the paper's own metric. Sits in the RISE evaluation-infrastructure layer alongside AIRS-Bench, MLGym, and AstaBench.

## Distinctive contribution

A Gym-like `AgenticEnv` interface (UV-local or Docker runtime) with an explicit $10 default API-cost budget per 12-24h run, cost tracking baked into the harness, and a dedicated InspectionAgent that post-hoc audits each completed run for cheating or rule violations — a runtime-integrity layer most sibling benchmarks lack. The companion paper reports a GPT-5-based agent beating the provided human baseline in only 1 of 15 runs (6.7%) while completing ~26.5% of sub-tasks on average, with one run surpassing an ICML 2025 Spotlight result.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure; scores the research ability of agents under test, does not itself produce scholarship. |
| Autonomy level | 0 | Static task environments plus a cost-budgeted scoring harness; all agency lives in the agent being evaluated (reference RGAgent, ClaudeCode, or Codex wrappers provided). |
| Architectural transparency | 3 | Public code and trajectories on GitHub, documented CLI (run_agent.py), Agent Adapter / Runtime / AgenticEnv architecture, and an arXiv paper (v1/v2) describing the full grading pipeline. |
| Inputs supported | 2 | Five standardized task environments (continual-learning, cross-modal-retrieval, replay buffers, materials tokenization, time-series explanation) runnable under two runtimes (UV, Docker); no external literature or data-source connector beyond the bundled pruned repos. |
| Outputs / reproducibility | 2 | Fixed baseline code and grading scripts per task with full run logs (transcript.json, cost_summary.json); agent-run stochasticity and the $10 cost cap limit exact reruns. |
| Internal evaluation | 2 | Systematic multi-model evaluation (GPT-5, Claude Code/Opus-4.5, Codex/GPT-5.2) reported in the companion arXiv paper using the papers' own original evaluation scripts rather than an LLM judge; not yet peer-reviewed beyond workshop acceptance. |
| Openness | 1 | Public repository with code and trajectories released, but no license file identified in the repo at scoring date — reuse terms are unclear. |
| Maturity / traction | 1 | 43 stars / 6 forks / 36 commits as of 2026-11-01; accepted to the ICLR 2026 Agents in the Wild Workshop, but young (Feb 2026) and still small. |
| Cross-family policy | 1 | Optional — ships wrappers for both ClaudeCode and Codex, so a cross-family executor/inspector split is configurable, but the default RGAgent is not cross-family by design. |
| Runtime assurance | 2 | Moderate — a dedicated InspectionAgent audits every completed run for cheating/rule violations, on top of fixed-budget cost tracking during the run; no claim-faithfulness or citation checks (not applicable to this task type). |
| Cross-platform portability | 1 | Two runtimes (local UV, Docker) and three model providers (OpenAI, Anthropic, Gemini) documented; not a framework-agnostic protocol. |

*Scored on 2026-11-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation`



**Inputs:** `task-specification` `agent-implementation`


**Outputs:** `evaluation-metrics` `agent-trajectories`


**Data sources:** `benchmark-datasets`


**Knowledge sources:** `source-papers`


## Limitations

- No license file identified at scoring date — reuse terms are unclear.
- Only five task environments (39 sub-tasks) at launch — narrow coverage relative to AIRS-Bench or MLGym.
- Workshop-level peer review only (ICLR 2026 Agents in the Wild Workshop), not a main-conference acceptance.
- Domain is ML/AI research (vision, NLP, RL, time series) — no economics or social-science tasks.

## Related projects in this catalog

- [`airs-bench`](airs-bench.md)
- [`mlgym`](mlgym.md)
- [`asta-bench`](asta-bench.md)
- [`innovatorbench`](innovatorbench.md)

## Papers describing this project

- **ResearchGym: Evaluating Language Model Agents on Real-World AI Research** — TCS Research, Yale University (2026). *arXiv / ICLR 2026 Agents in the Wild Workshop*. [arXiv:2602.15112](https://arxiv.org/abs/2602.15112)
