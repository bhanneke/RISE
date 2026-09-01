<!-- DO NOT EDIT — auto-generated from projects/landscape/agent-laboratory.yml by scripts/build_indexes.py -->

# Agent Laboratory

`external` · status: `dormant` · focus: `end-to-end` · discipline: `computer-science` · started: 2025

**Project page:** <https://github.com/SamuelSchmidgall/AgentLaboratory>

**Source:** [`projects/landscape/agent-laboratory.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/agent-laboratory.yml)

## Positioning

An end-to-end autonomous research workflow (arXiv:2501.04227) that guides a research idea through three phases — literature review, experimentation, and report writing — with specialized LLM-driven agents and external tools (arXiv, Hugging Face, Python, LaTeX). The companion **AgentRxiv** framework lets agents share and build on each other's outputs cumulatively.

## Distinctive contribution

Treats *cumulative agentic research* as a first-class concern via AgentRxiv: agents upload, retrieve, and build on prior agentic work. Distinguishes itself from one-shot pipelines by explicitly modeling iterative community-of-agents progress.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Seven stages across the three phases (literature, experiment, report). |
| Autonomy level | 2 | Designed as a research *assistant*: human researcher provides idea and reviews phase outputs. |
| Architectural transparency | 3 | Open under MIT; arXiv paper documents agent roles and phases; AgentRxiv mechanism described publicly. |
| Inputs supported | 2 | Research-idea inputs with optional dataset; multiple LLM back-ends (OpenAI, DeepSeek). |
| Outputs / reproducibility | 2 | Versioned artifacts via AgentRxiv; full bitwise reproducibility depends on LLM determinism. |
| Internal evaluation | 2 | ArXiv paper reports systematic evaluation across phases; external validation pending. |
| Openness | 3 | MIT-licensed; broad community translations of README; LaTeX optional via flag. |
| Maturity / traction | 0 | 5.8k+ stars but no activity in >12 months (last commit 2025-08-20, per rubric's abandoned band); 38 open issues and 21 open PRs unaddressed. |
| Cross-family policy | 0 | No required cross-family policy; multi-back-end (OpenAI o-series + DeepSeek) without architectural separation. |
| Runtime assurance | 1 | Phase-level review gates; AgentRxiv enables cross-project artifact reuse but no in-pipeline claim audit. |
| Cross-platform portability | 1 | Multi-back-end (OpenAI, DeepSeek) but framework-level (not multi-IDE). |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `hypothesis-generation` `research-design` `data-analysis` `code-generation` `paper-drafting`


**Architectural features:** `multi-agent` `human-in-loop` `tool-use` `iterative-loop` `artifact-versioning`


**Inputs:** `research-idea` `dataset`


**Outputs:** `paper-draft` `code` `experiment-logs`


**Data sources:** `huggingface` `user-provided`


**Knowledge sources:** `arxiv`


## Limitations

- Computer-science orientation; portability to empirical social sciences untested.
- Quality strongly dependent on choice of LLM back-end and human supervision points.
- Pdflatex required for publication-quality output.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`sakana-ai-scientist-v1`](sakana-ai-scientist-v1.md)
- [`robin`](robin.md)
- [`e2er`](e2er.md)

## Papers describing this project

- **Agent Laboratory: Using LLM Agents as Research Assistants** — Schmidgall, S., Su, Y., Wang, Z., Sun, X., Wu, J., Yu, X., et al. (2025). *arXiv*. [arXiv:2501.04227](https://arxiv.org/abs/2501.04227)

## Also compared in

- **ARIS Table 4** ([`yang2026aris`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Scored: no cross-family, NO adversarial review, no composable skills, ✓ E2E, NO assurance, no portability. ARIS specifically flags the absence of system-level integrity checks.
- **A Survey of AI Scientists** ([`tie2025aiscientistsurvey`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Covered as a three-phase research-assistant pipeline.

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
