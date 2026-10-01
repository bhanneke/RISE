<!-- DO NOT EDIT — auto-generated from projects/landscape/automated-w2s-research.yml by scripts/build_indexes.py -->

# Automated Alignment Researchers (Anthropic)

`external` · status: `active` · focus: `analysis` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/safety-research/automated-w2s-research>

**Licence:** `MIT`

**Source:** [`projects/landscape/automated-w2s-research.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/automated-w2s-research.yml)

## Positioning

Anthropic's open-sourced sandbox and agent harness for automating a specific slice of alignment research — weak-to-strong generalization. Nine Claude-powered agent instances autonomously propose training methods, implement them, train and evaluate models against a server-side held-out metric (Performance Gap Recovery), and post findings to a shared forum that other agents can read. Sits in the single-domain, experiment-driven corner of the landscape alongside AlphaEvolve and RD-Agent, but the object of study is AI safety research itself rather than general empirical science; covers hypothesis-generation through code-generation and evaluation with no literature search or paper-drafting stage.

## Distinctive contribution

The first publicly released code + sandbox + baselines for autonomous alignment research with a verifiable, cheat-resistant metric (ground truth never leaves the server) and a documented inter-agent "findings forum." The companion paper reports automated researchers closing almost the full performance gap (PGR 0.97) across 10 distinct alignment failure modes within six hours, outperforming the best one-shot method from 28 experienced human researchers given up to eight hours, with generalization to held-out benchmarks and models up to 4.7x larger than the target model.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Four adjacent stages (hypothesis-generation through code-generation/evaluation); no literature search or paper-drafting stage. |
| Autonomy level | 3 | Agents run multi-day, multi-hundred-hour research loops (propose, implement, train, evaluate, share) without per-step human approval within the sandboxed task. |
| Architectural transparency | 3 | Full agent code, prompts, sandbox/Docker/RunPod configs, dashboard, and five baseline implementations are public on GitHub under MIT. |
| Inputs supported | 1 | Single input form (a predefined weak-to-strong benchmark task) plus access to labeled/unlabeled chat, math, and code datasets; no literature access. |
| Outputs / reproducibility | 2 | Persists code, trained models, and evaluation metrics with cached baseline results and three execution modes, but live agent runs are LLM-stochastic and GPU-dependent, not deterministically reproducible end-to-end. |
| Internal evaluation | 2 | Systematic evaluation across 10 alignment failures with held-out generalization checks and a time-boxed 28-researcher human baseline; arXiv preprint only, not yet peer-reviewed. |
| Openness | 2 | MIT license with full setup docs and cached data/results; reproducing agent runs needs GPU compute (local or RunPod), not casual commodity hardware. |
| Maturity / traction | 1 | Young research artifact (paper and repo, August 2026); 314 stars / 49 forks and only 2 commits on main at scoring date — early-stage, not a maintained product. |
| Cross-family policy | 0 | All nine automated-researcher agents run on Claude; no cross-model-family executor/reviewer setup. |
| Runtime assurance | 2 | Server-side held-out evaluation API withholds ground truth so agents cannot directly optimize against it, a moderate in-pipeline anti-gaming gate; no separate claim- or citation-faithfulness checks (not applicable to this task domain). |
| Cross-platform portability | 2 | Three execution backends (local subprocess, Docker, RunPod cloud) support parallel distributed runs, though locked to the Claude model family. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `persistent-memory`


**Inputs:** `alignment-benchmark-task` `labeled-unlabeled-datasets`


**Outputs:** `training-methods` `code` `evaluation-metrics` `findings-reports`


**Data sources:** `chat-math-code-labeled-datasets`


**Knowledge sources:** `inter-agent-findings-forum`


## Limitations

- Narrow to one task family (weak-to-strong generalization on chat/math/code data), not a general-purpose research agent.
- Single model family (Claude) only; no cross-family review built in.
- Requires GPU compute (local or RunPod) to run; not reproducible on a laptop without cloud spend.
- Early-stage research artifact (August 2026) with minimal commit history; not positioned as a maintained product.

## Related projects in this catalog

- [`arbor`](arbor.md)
- [`rd-agent`](rd-agent.md)
- [`alphaevolve`](alphaevolve.md)
- [`mle-bench`](mle-bench.md)

## Papers describing this project

- **Automated Researchers Can Mitigate Well-characterized Alignment Failures** — Chen, Y.-H., Wen, J., Kirchner, J. H. (2026). *arXiv (Anthropic)*. [arXiv:2608.28945](https://arxiv.org/abs/2608.28945)
