<!-- DO NOT EDIT — auto-generated from projects/landscape/agent-economist.yml by scripts/build_indexes.py -->

# AgentEconomist

`external` · status: `active` · focus: `analysis` · discipline: `economics` · started: 2026

**Project page:** <https://arxiv.org/abs/2604.27725>

**Source:** [`projects/landscape/agent-economist.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/agent-economist.yml)

## Positioning

An interactive research copilot (arXiv:2604.27725) that turns a human researcher's abstract economic intuition into a runnable agent-based computational experiment. Three stages — literature- grounded hypothesis drafting, experimental-design/simulator parameterization, and experiment execution — sit on top of AgentEconomy, an LLM-driven agent-based macroeconomic simulator (households, firms, government, banking, calibrated from empirical microdata). A human reviews and steers each stage.

## Distinctive contribution

Targets the ideation-to-simulation slice of the economics research pipeline specifically, pairing a 13,000+ paper domain knowledge base with a full agent-based macro simulator rather than a generic code sandbox; explicitly positions itself against "The AI Scientist"-style systems, arguing those optimize for an autonomous end product over supporting the human's own research process.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Four stages — hypothesis drafting, experimental design, simulator parameterization, and execution/results — but stops before paper-drafting or referee-simulation. |
| Autonomy level | 1 | Explicitly interactive/human-in-the-loop: the researcher reviews and steers each of the three pipeline stages rather than approving only a final artifact. |
| Architectural transparency | 1 | Paper describes the three-stage architecture and the AgentEconomy simulator design; no code, prompts, or configs found public at scoring date. |
| Inputs supported | 1 | Single input form (a free-text economic intuition), but draws on both a literature corpus (13,000+ papers) and empirical microdata for simulator calibration. |
| Outputs / reproducibility | 2 | Persists structured experiment artifacts (simulator configs, run code, results) per the paper, but the system itself is not public, so end-to-end reproduction by third parties is unverified. |
| Internal evaluation | 2 | Systematic evaluation comparing AgentEconomist-produced ideas/experiments against baseline-LLM outputs using human expert judges on the same prompts; arXiv preprint only, not yet peer-reviewed at scoring date. |
| Openness | 0 | No public code or AgentEconomy simulator release found at scoring date; paper only. |
| Maturity / traction | 1 | Academic research prototype (arXiv, posted 2026-04-30); single-team, no reported external users or releases. |
| Cross-family policy | 0 | No cross-model-family review described; single underlying LLM backend. |
| Runtime assurance | 1 | Literature-grounding of hypotheses against the domain KB acts as a light in-pipeline check; no described math/claim-audit or adversarial gate. |
| Cross-platform portability | 0 | Research prototype tied to the authors' AgentEconomy simulator; no described deployment on other runtimes. |

*Scored on 2026-11-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `formal-modeling` `data-analysis`


**Architectural features:** `multi-agent` `human-in-loop` `rag-knowledge-base` `tool-use` `iterative-loop`


**Inputs:** `research-direction`


**Outputs:** `computational-results` `simulation-code`


**Data sources:** `empirical-microdata`


**Knowledge sources:** `economics-literature-corpus`


## Limitations

- No public code or data release found at scoring date — architecture and results are known only from the paper.
- Scope is agent-based macroeconomic simulation specifically, not general empirical economics (no identification strategy, no real-dataset estimation, no paper-drafting stage).
- Evaluation relies on a human expert user study of unreported scale; quantitative headline results were not found in public summaries at scoring date.

## Related projects in this catalog

- [`econcs-bench`](econcs-bench.md)
- [`econ-skills`](econ-skills.md)

## Papers describing this project

- **AgentEconomist: An End-to-end Agentic System Translating Economic Intuitions into Executable Computational Experiments** — Chen, Jiaju, He, Xiangnan, Li, Yong, et al. (2026). *arXiv*. [arXiv:2604.27725](https://arxiv.org/abs/2604.27725)

## Related references (literature catalog)

- `chen2026agenteconomist` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
