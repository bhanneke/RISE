<!-- DO NOT EDIT — auto-generated from projects/landscape/asta-autodiscovery.yml by scripts/build_indexes.py -->

# Asta AutoDiscovery

`external` · status: `active` · focus: `ideation` · discipline: `general` · started: 2025

**Project page:** <https://allenai.org/blog/autodiscovery>

**Source:** [`projects/landscape/asta-autodiscovery.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/asta-autodiscovery.yml)

## Positioning

Ai2's autonomous data-driven discovery agent (formerly AutoDS; relaunched inside AstaLabs on 2026-02-12): pointed at a structured dataset, it generates natural-language hypotheses, proposes experiment plans, writes and executes Python analyses — up to 500 experiments in a session — and ranks the resulting findings by Bayesian surprise, the shift from the LLM's prior to posterior belief in each hypothesis. Sits at the hypothesis-generation → data-analysis → code-generation slice of the pipeline; no literature layer and no paper drafting.

## Distinctive contribution

The first production discovery agent to use Bayesian surprise as the objective: an MCTS search with progressive widening treats surprisal as reward, so the system hunts belief-shifting findings rather than confirmations. Early-access users have generated 46K+ hypotheses across oncology, neuroscience, climate science, and the social sciences, and several independently verified social-science findings were published in a peer-reviewed paper (arXiv:2511.12529).

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three adjacent stages (hypothesis generation, analysis, code); no literature discovery, drafting, or review. |
| Autonomy level | 3 | User points it at a dataset; it then runs hundreds of hypothesis-experiment cycles over several hours without per-step approval. |
| Architectural transparency | 3 | NeurIPS 2025 paper plus open code: research implementation (allenai/autodiscovery, with DiscoveryBench/BLADE evaluation) and Apache-2.0 production code (allenai/asta-autodiscovery). |
| Inputs supported | 1 | Single input form — a structured dataset with metadata; data access but no literature-corpus integration. |
| Outputs / reproducibility | 2 | Persists hypotheses, executable Python code, and statistical results per run, but hosted service deletes source datasets after 7 days and MCTS/LLM stochasticity limits exact reruns. |
| Internal evaluation | 3 | Peer-reviewed at NeurIPS 2025 (21-dataset evaluation, expert judgment on two-thirds of discoveries); downstream social-science findings independently verified and published. |
| Openness | 2 | Apache-2.0 code and pip/conda install for the research implementation, but end-to-end reproduction of the hosted product's runs not demonstrated; hosted access is credit-gated early access through 2026-07-31. |
| Maturity / traction | 2 | Early-access beta inside AstaLabs with external users across many domains (46K+ hypotheses); production repo under active development. |
| Cross-family policy | 0 | Exploration and belief models are configurable, but documented setups are single-family (OpenAI gpt-4o for both); no cross-family review design. |
| Runtime assurance | 1 | Hypotheses are checked by actually executing statistical experiments before ranking, but there is no independent claim audit, citation grounding, or multiple-testing gate. |
| Cross-platform portability | 1 | Two execution paths — hosted AstaLabs app and self-hosted CLI — with OpenAI-model examples only. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `data-analysis` `code-generation`


**Architectural features:** `tool-use` `iterative-loop`


**Inputs:** `structured-dataset`


**Outputs:** `ranked-hypotheses` `experiment-code` `statistical-results`


**Data sources:** `user-provided`


**Knowledge sources:** `llm-prior-beliefs`


## Limitations

- Structured-dataset discovery only: 'surprise' is measured against the LLM's beliefs, not the published literature, so rediscoveries and spurious-correlation artifacts must be screened by domain experts.
- Hosted service is gated early access (hypothesis credits, costs subsidized only through 2026-07-31) and deletes source datasets 7 days after analysis.
- Surprisal-driven search over hundreds of automated experiments raises multiple-comparisons risk; flagged findings are candidates for validation, not conclusions.

## Related projects in this catalog

- [`asta-bench`](asta-bench.md)
- [`kosmos`](kosmos.md)
- [`data-to-paper`](data-to-paper.md)
- [`google-co-scientist`](google-co-scientist.md)

## Papers describing this project

- **AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise** — Agarwal, D., Majumder, B. P., Adamson, R., Chakravorty, M., Gavireddy, S. R., Parashar, A., et al. (2025). *NeurIPS 2025*. [arXiv:2507.00310](https://arxiv.org/abs/2507.00310)

## Related references (literature catalog)

- Agarwal, D. et al. (2025). [*AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise*](../papers/notes/agarwal2025autodiscovery.md) `agarwal2025autodiscovery`
