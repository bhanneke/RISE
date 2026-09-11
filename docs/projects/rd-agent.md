<!-- DO NOT EDIT — auto-generated from projects/landscape/rd-agent.yml by scripts/build_indexes.py -->

# RD-Agent (R&D-Agent)

`external` · status: `active` · focus: `analysis` · discipline: `general` · started: 2024

**Project page:** <https://github.com/microsoft/RD-Agent>

**Source:** [`projects/landscape/rd-agent.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/rd-agent.yml)

## Positioning

Microsoft's framework for automating data-driven R&D as a two-role loop: a Research agent proposes a hypothesis, a Development agent implements it as executable code, the result is run against real data, and the measured feedback drives the next iteration. Declared scenarios in the README are quantitative finance (automated factor and model joint optimisation), medical prediction, general ML engineering (Kaggle competitions and paper-to-code reimplementation), LLM fine-tuning (FT-Agent) and RL post-training pipelines (Agent² RL-Bench). Sits in the RISE analysis layer, not the writing layer: it automates the discovery loop and stops at code and metrics — no manuscript. Nearest neighbours in the catalog are MLGym and Arbor for experiment-loop automation and paper2code for paper-to-implementation.

## Distinctive contribution

The only entry in the catalog whose flagship application is quantitative-finance factor discovery — R&D-Agent-Quant (NeurIPS 2025) jointly optimises factors and models against market data — and it pairs that with the strongest published benchmark position of any autoresearch system here: 30.22% overall success on MLE-Bench's 75 Kaggle competitions with o3 as Research and GPT-4.1 as Development, against 16.9% for the previous best (AIDE with o1-preview). Its paper-to-factor path also makes replication a first-class capability: it reads a paper or report, extracts the model or factor, and reimplements it as running code.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five stages — hypothesis generation, experiment planning, analysis, code generation, and paper-to-implementation replication — with the whole scholarly-communication half missing: no literature discovery or synthesis, no paper drafting, no referee simulation. |
| Autonomy level | 3 | Autonomous by design: once a scenario is configured the propose → implement → execute → evaluate loop iterates without per-task human approval, which is what makes unattended MLE-Bench runs across 75 competitions possible. |
| Architectural transparency | 3 | MIT license with the full framework, scenario configs and prompt templates in the repo (1,018 commits), the two-role loop documented in the README, seven papers listing the design, and published MLE-Bench numbers with the exact model pairing used. |
| Inputs supported | 2 | Multiple input forms (a research goal, a user dataset, a Kaggle competition directory, a paper or report to extract a model from) with real data-source access including market data via the quant scenario; falls short of band 3 because there is no literature-corpus connector — papers must be handed to it. |
| Outputs / reproducibility | 2 | Persists executable code, factor/model proposals with performance metrics, and full execution traces viewable in a web/Streamlit UI, and scenarios are re-runnable from config — but runs are LLM-stochastic, there is no data manifest, and no manuscript artifact is produced. |
| Internal evaluation | 3 | External validation on several axes: reported MLE-Bench SOTA (30.22% vs 16.9% prior best) plus peer-reviewed papers at NeurIPS 2025 (R&D-Agent-Quant), ICML 2026 (FT-Dojo) and ACL 2026 Findings, and a publicly hosted demo at rdagent.azurewebsites.net. |
| Openness | 2 | MIT license with the whole framework public and documented scenarios, but the headline results require paid frontier models (o3 + GPT-4.1) and substantial compute per loop — not reproducible end-to-end on commodity hardware. |
| Maturity / traction | 3 | 14,542 stars / 1,890 forks / 1,018 commits, created 2024-04-03 and pushed 2026-09-04, maintained under the Microsoft org with a hosted demo and a sustained multi-paper publication record. |
| Cross-family policy | 1 | Cross-family is possible but neither required nor default: LiteLLM is the default backend so any provider mix is configurable, yet the Research/Development split is a role split, and the published best configuration (o3 + GPT-4.1) draws both roles from the same family. |
| Runtime assurance | 2 | Moderate, and grounded in execution rather than prose: every proposal must compile, run on real data and beat the incumbent on a declared metric before it is retained, with failed runs and error traces fed back into the loop. No claim, citation, math or figure audit — it produces no prose to audit. |
| Cross-platform portability | 2 | LiteLLM is the default backend with OpenAI/Azure OpenAI, DeepSeek and custom API bases documented, so 3+ providers are supported without a rewrite; but it is a single agent runtime (its own Python framework plus Docker and a Streamlit UI), not a framework-agnostic design. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation` `replication`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `persistent-memory`


**Inputs:** `research-goal` `user-dataset` `kaggle-competition` `published-paper-or-report`


**Outputs:** `analysis-code` `factor-and-model-library` `performance-metrics` `execution-traces`


**Data sources:** `user-provided` `market-data` `kaggle`


**Knowledge sources:** `user-supplied-papers-and-reports`


## Limitations

- Not a scholarship pipeline: it produces code, factors and metrics, and stops there — no drafting, no citation handling, no review stage.
- The headline MLE-Bench figure depends on an expensive frontier-model pairing (o3 + GPT-4.1); cheaper configurations are not reported at that level.
- Kaggle-derived benchmarks carry a real training-contamination risk for competitions predating the models' cutoffs.
- LLM-stochastic loops mean a given scenario's result is a distribution, not a number; the repo reports no variance across seeds for its scenario runs.
- 218 open issues at scoring date, consistent with a fast-moving research framework rather than a stable product.
- The quant scenario expects Qlib conventions and user-supplied market data; a discovered factor's out-of-sample validity is the user's problem, and nothing in the loop guards against overfitting to the evaluation split.
- Because it emits no prose, none of the catalog's claim-faithfulness or hallucinated-citation assurances apply or are needed — which also means it cannot be used to check a paper.

## Related projects in this catalog

- [`mlgym`](mlgym.md)
- [`mle-bench`](mle-bench.md)
- [`paper2code`](paper2code.md)
- [`arbor`](arbor.md)
- [`statspai`](statspai.md)

## Papers describing this project

- **R&D-Agent: An LLM-Agent Framework Towards Autonomous Data Science** — Yang, X., Yang, X., Fang, S., Zhang, Y., Wang, J., Xian, B., Li, Q., Li, J., Xu, M., Li, Y., Pan, H., Zhang, Y., Liu, W., Shen, Y., Chen, W., Bian, J. (2025). *arXiv*. [arXiv:2505.14738](https://arxiv.org/abs/2505.14738)
- **R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization** — Li, Y., Yang, X., Yang, X., Xu, M., Wang, X., Liu, W., Bian, J. (2025). *NeurIPS 2025*. [arXiv:2505.15155](https://arxiv.org/abs/2505.15155)

## Related references (literature catalog)

- `li2025rdagentquant` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `yang2025rdagent` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
