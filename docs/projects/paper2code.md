<!-- DO NOT EDIT — auto-generated from projects/landscape/paper2code.yml by scripts/build_indexes.py -->

# PaperCoder (Paper2Code)

`external` · status: `active` · focus: `replication` · discipline: `computer-science` · started: 2025

**Project page:** <https://github.com/going-doer/Paper2Code>

**Source:** [`projects/landscape/paper2code.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/paper2code.yml)

## Positioning

An ICLR 2026 multi-agent system (arXiv:2504.17192) that transforms a machine-learning paper into a working code repository via a three-stage pipeline (planning, analysis, code generation) with specialized agents per stage. Sits at the replication / code- generation block of the RISE pipeline, distinct from referee- simulation or drafting tools.

## Distinctive contribution

Explicitly targets the *paper-to-implementation* gap rather than paper-from-scratch authoring, and reports outperforming strong baselines on both Paper2Code and PaperBench evaluation suites. Ships its own benchmark datasets alongside the system.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three stages all in the replication arc; does not cover lit synthesis or drafting. |
| Autonomy level | 3 | Runs end-to-end from a paper to a code repository. |
| Architectural transparency | 3 | Open under Apache-2.0; ICLR 2026 paper documents agent roles; benchmark datasets released. |
| Inputs supported | 2 | Accepts PDF and LaTeX inputs; supports OpenAI API and vLLM-served open-source models. |
| Outputs / reproducibility | 3 | Bundled benchmark datasets + run scripts make published-paper experiments reproducible. |
| Internal evaluation | 3 | Reports gains on Paper2Code and PaperBench against strong baselines; model-based eval published. |
| Openness | 3 | Apache-2.0; reproducible setup; ICLR paper. |
| Maturity / traction | 3 | 4.6k+ stars; ICLR 2026 acceptance; clear external citation trajectory. |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `replication` `research-design` `code-generation`


**Architectural features:** `multi-agent` `dag-orchestration` `tool-use` `artifact-versioning`


**Inputs:** `target-paper`


**Outputs:** `code-repository` `implementation-plan` `analysis-report`


**Data sources:** `paper-pdf` `paper-latex`


**Knowledge sources:** `target-paper`


## Limitations

- ML-paper focus; portability to empirical economics or biomedical papers untested in the published evaluations.
- Cost per run (~$0.50–0.70 with o3-mini) is non-trivial at scale.
- Faithfulness depends on the LaTeX/PDF parsing quality.

## Related projects in this catalog

- [`social-science-replicability`](social-science-replicability.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`sakana-ai-scientist`](sakana-ai-scientist.md)

## Papers describing this project

- **Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning** — Seo, M., Baek, J., Lee, S., Hwang, S. J. (2025). *ICLR 2026 (arXiv)*. [arXiv:2504.17192](https://arxiv.org/abs/2504.17192)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
