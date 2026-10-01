<!-- DO NOT EDIT — auto-generated from projects/landscape/litreview-arena.yml by scripts/build_indexes.py -->

# LitReview Arena

`external` · status: `active` · focus: `literature` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/VanellopeAsher/LitReview-Arena>

**Licence:** `MIT`

**Source:** [`projects/landscape/litreview-arena.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/litreview-arena.yml)

## Positioning

A benchmark and evaluation platform for literature-review-writing agents: it collects blind pairwise ("battle-style") expert preferences between AI-generated and human/baseline literature-review drafts across five dimensions (coverage, claim support, structure, research suggestions, overall utility), then converts them into a reproducible offline benchmark. Sits in the RISE evaluation-infrastructure layer next to `asta-bench` and `surveyx`, but targets literature-synthesis quality specifically rather than end-to-end research-agent capability.

## Distinctive contribution

Replaces citation-overlap metrics and generic LLM-as-judge scoring with ~2,754 recruited-expert pairwise judgments (experts constrained to researchers with AI paper-writing experience), and ships `LitJudge`, a calibrated evaluator whose alignment with human judgment (Spearman's rho 0.78) approaches inter-expert consistency — far above a naive LLM-judge baseline (rho 0.467).

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation target/platform; it judges literature-synthesis output rather than producing scholarship itself. |
| Autonomy level | 0 | Static benchmark + judging pipeline; agency lives in the literature-review agents being evaluated (e.g., Sonar Deep Research, STORM). |
| Architectural transparency | 3 | Full data (2,754 judgments), LitJudge evaluator code, and calibration protocol published under MIT. |
| Inputs supported | 1 | Single input form (review drafts to compare); no agent-facing data/knowledge access of its own. |
| Outputs / reproducibility | 2 | Persists structured judgment data and leaderboard scripts; reproducible from released data but not an end-to-end paper+code+data pipeline. |
| Internal evaluation | 3 | Accepted at ICML 2026; large-scale recruited-expert study is itself the paper's external validation. |
| Openness | 2 | MIT license, data and evaluator code public; running the full expert-judgment pipeline needs recruited annotators, not just commodity compute. |
| Maturity / traction | 1 | 3 stars / 0 forks as of scoring date; posted August 2026, single-team artifact validated via one peer-reviewed study. |
| Cross-family policy | 0 | Not applicable — an evaluation benchmark, not a review/executor-reviewer system. |
| Runtime assurance | 0 | Offline benchmark; no in-flight integrity mechanisms. |
| Cross-platform portability | 2 | Format-agnostic text comparisons already used to score 3+ distinct systems/backbones (e.g., Sonar Deep Research, STORM, base LLMs). |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis`



**Inputs:** `literature-review draft` `research topic/query`


**Outputs:** `pairwise win/loss judgments` `dimension-wise scores` `leaderboard`


**Knowledge sources:** `arxiv (source papers for review topics)`


## Limitations

- Pairwise expert 'battles' require recruiting researchers with AI paper-writing experience — costly to scale beyond the fixed dataset snapshot.
- Built and validated on AI-domain literature reviews only; not tested on economics/social-science review writing.
- Very young repository (3 stars); no sustained external leaderboard submissions yet.

## Related projects in this catalog

- [`asta-bench`](asta-bench.md)
- [`surveyx`](surveyx.md)
- [`storm`](storm.md)
- [`open-scholar`](open-scholar.md)

## Papers describing this project

- **LitReview Arena: Evaluating Literature Review Agents with Battle-Style Peer Review Platform** — Zhao, R., Chen, Z., Liu, X., and others (2026). *ICML 2026 / arxiv*. [arXiv:2608.21374](https://arxiv.org/abs/2608.21374)
