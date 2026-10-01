<!-- DO NOT EDIT — auto-generated from projects/landscape/foresci.yml by scripts/build_indexes.py -->

# ForeSci

`external` · status: `research-prototype` · focus: `ideation` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/roytian1992/ResearchForesight>

**Licence:** `none`

!!! warning "No licence declared"
    The repository declares no licence, so its code cannot be reused,
    modified or redistributed without the maintainer's permission. RISE
    describes and links to the project; nothing from it is reproduced here.

**Source:** [`projects/landscape/foresci.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/foresci.yml)

## Positioning

A temporally-controlled benchmark of 500 tasks testing whether LLM agents can make forward-looking research judgments — direction forecasting, bottleneck/opportunity discovery, strategic research planning, and venue-aware positioning — from a frozen, cutoff-dated knowledge base (~7,500 documents across four fast-moving AI subfields: LLM agents, fine-tuning, RAG systems, visual generative modeling), with post-cutoff papers held out purely for validation. Sits in the RISE evaluation-infrastructure layer testing the rq-formulation / research-design front end of the pipeline, alongside `econcs-bench` and `naturebench`, rather than any component that itself produces a paper.

## Distinctive contribution

The only benchmark in the catalog scoring forward-looking research judgment itself — what should be studied next, and where it would be publishable — rather than execution skill, via a leakage-controlled design (knowledge base frozen at a cutoff, evaluation targets drawn only from post-cutoff papers) and family-specific LLM-as-judge rubrics for persuasiveness and evidence traceability.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation harness: grades agents' forward-looking research judgment; produces no scholarship of its own. |
| Autonomy level | 0 | Static task files, frozen knowledge base, and grading scripts; any agency lives in the systems attempting the tasks. |
| Architectural transparency | 3 | Pip-installable repo publishes the 500 task files (JSONL), the ~7,500-document per-domain knowledge base, evaluation scripts, prompt templates, and the LLM-as-judge rubrics for all four decision families. |
| Inputs supported | 1 | One input form (a task prompt plus its frozen per-domain knowledge base); no live literature or data-source access — staleness is deliberate, to prevent leakage from post-cutoff papers. |
| Outputs / reproducibility | 1 | Deterministic claim-F1/evidence-traceability scoring exists, but the repo publishes no versioned leaderboard, run manifest, or release tags at review date, and the persuasiveness score depends on an LLM judge. |
| Internal evaluation | 2 | The companion paper (arXiv:2606.00644) reports systematic evaluation of native LLMs, Hybrid RAG, and three research-agent adaptations across four backbones; no public leaderboard or third-party replication yet. |
| Openness | 1 | No license file found in the repository at scoring date — reuse terms are unclear despite the code and data being publicly visible. |
| Maturity / traction | 1 | 1 star, 0 forks, single-author repo released alongside a May/June 2026 preprint — a fresh research-prototype drop with no external adoption evident yet. |
| Cross-family policy | 0 | Not applicable — a model-agnostic evaluation harness with no executor/reviewer configuration of its own. |
| Runtime assurance | 0 | No in-flight runtime mechanisms; this is post-hoc evaluation of submitted judgments, not a pipeline with runtime gates. |
| Cross-platform portability | 2 | The harness evaluates native LLMs, a Hybrid-RAG baseline, and three research-agent scaffolds across four model backbones — multiple providers/runtimes, short of the 5+ band. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `hypothesis-generation` `research-design` `dissemination`



**Inputs:** `frozen-knowledge-base` `task-prompt`


**Outputs:** `prediction-scores` `evidence-traceability-report`


**Knowledge sources:** `frozen-arxiv-snapshot-kb`


## Limitations

- No license file at scoring date — reuse terms are unclear.
- No populated leaderboard in the repository itself; comparative model results live only in the companion paper.
- Single-author repo (1 star, 0 forks) released alongside the paper — no independent validation yet that the frozen knowledge base or judge rubrics generalize beyond the four covered AI subfields.
- Scope is limited to four fast-moving AI/ML subfields, not a general cross-discipline research-judgment benchmark.
- Persuasiveness/research-judgment scoring depends on an LLM-as-judge rubric rather than human expert validation.

## Related projects in this catalog

- [`econcs-bench`](econcs-bench.md)
- [`naturebench`](naturebench.md)
- [`scholar-eval`](scholar-eval.md)

## Papers describing this project

- **ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment** — Tian, Q., Yin, H., Xia, Y., Kong, Y., Liu, Z. (2026). *arxiv*. [arXiv:2606.00644](https://arxiv.org/abs/2606.00644)
