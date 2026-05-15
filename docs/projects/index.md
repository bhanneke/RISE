# Projects catalog

This catalog evaluates agentic-research systems against the
[standard rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).
Vocabularies for stages, architectural features, focus, and
disciplinary scope are defined in
[`projects/VOCABULARY.md`](https://github.com/bhanneke/RISE/blob/main/projects/VOCABULARY.md).

The matrix and per-project pages below are **auto-generated** from
`projects/*.yml` and `projects/landscape/*.yml` by
`scripts/build_indexes.py`. Do not edit by hand — edit the YAML
sources.

<!-- AUTO-GENERATED:projects-start -->

### Comparison matrix

| Project | Type | Focus | LC | AUT | ARC | IN | OUT | EVAL | OPEN | MAT | Discipline |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [E2ER — End-to-End Research](e2er.md) | owned | `end-to-end` | 3 | 2 | 2 | 3 | 2 | 1 | 2 | 1 | economics |
| [Agent Laboratory](agent-laboratory.md) | external | `end-to-end` | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 3 | computer-science |
| [APE — Automated Peer Evaluator](ape.md) | external | `review` | 0 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | general |
| [AutoSurvey](autosurvey.md) | external | `literature` | 1 | 3 | 2 | 1 | 2 | 3 | 1 | 1 | general |
| [Aviary (FutureHouse)](aviary.md) | external | `end-to-end` | 0 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | general |
| [coarse.ink](coarse-ink.md) | external | `drafting` | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | general |
| [DeepResearcher (GAIR-NLP)](deepresearcher.md) | external | `literature` | 1 | 3 | 3 | 2 | 2 | 3 | 3 | 2 | general |
| [GPT Researcher](gpt-researcher.md) | external | `literature` | 1 | 3 | 3 | 2 | 2 | 1 | 3 | 3 | general |
| [Kosmos (jimmc414 implementation)](kosmos.md) | external | `end-to-end` | 2 | 3 | 3 | 2 | 2 | 2 | 1 | 2 | general |
| [MARG (Multi-Agent Review Generation)](marg.md) | external | `review` | 0 | 2 | 3 | 1 | 3 | 2 | 3 | 1 | general |
| [MLGym (Meta)](mlgym.md) | external | `end-to-end` | 0 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | computer-science |
| [Open CoScientist Agents](open-coscientist.md) | external | `ideation` | 1 | 3 | 3 | 2 | 1 | 1 | 3 | 1 | general |
| [OpenScholar (AI2)](open-scholar.md) | external | `literature` | 0 | 2 | 3 | 2 | 2 | 3 | 3 | 2 | general |
| [PaperQA2 (FutureHouse)](paper-qa.md) | external | `literature` | 0 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | general |
| [PaperCoder (Paper2Code)](paper2code.md) | external | `replication` | 1 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | computer-science |
| [refine.ink](refine-ink.md) | external | `revision` | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | general |
| [ResearchAgent (NAACL 2025)](researchagent.md) | external | `ideation` | 1 | 2 | 3 | 2 | 2 | 2 | 1 | 1 | general |
| [Reviewer (Ingar30)](reviewer.md) | external | `review` | 0 | 2 | 3 | 1 | 2 | 1 | 3 | 1 | economics |
| [Robin (FutureHouse)](robin.md) | external | `end-to-end` | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 2 | biomedical |
| [Sakana AI Scientist v2](sakana-ai-scientist.md) | external | `end-to-end` | 2 | 3 | 3 | 1 | 2 | 2 | 3 | 2 | computer-science |
| [Sakana AI Scientist (v1)](sakana-ai-scientist-v1.md) | external | `end-to-end` | 2 | 3 | 3 | 1 | 2 | 2 | 2 | 3 | computer-science |
| [Social Science Replicability Infrastructure](social-science-replicability.md) | external | `replication` | 1 | 2 | 2 | 2 | 2 | 1 | 3 | 1 | social-sciences |
| [STORM / Co-STORM](storm.md) | external | `literature` | 1 | 2 | 3 | 2 | 2 | 2 | 3 | 3 | general |
| [SurveyX](surveyx.md) | external | `literature` | 1 | 3 | 2 | 1 | 1 | 2 | 1 | 2 | general |
| [Tongyi DeepResearch](tongyi-deepresearch.md) | external | `literature` | 1 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | general |
| [ToolUniverse](tooluniverse.md) | external | `end-to-end` | 0 | 2 | 3 | 3 | 2 | 2 | 3 | 2 | biomedical |
| [zeropaper](zeropaper.md) | external | `drafting` | 1 | 2 | 2 | 1 | 1 | 0 | 3 | 1 | general |

*Score columns: LC = lifecycle coverage, AUT = autonomy, ARC = architectural transparency, IN = inputs supported, OUT = outputs/reproducibility, EVAL = internal evaluation, OPEN = openness, MAT = maturity/traction. Scale 0–3. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

### One-line summaries

- **[E2ER — End-to-End Research](e2er.md)** — E2ER is a strategist-driven agentic research pipeline that takes a research idea (human- or agent-supplied) and carries it through literature synthesis, identification, data acquisition, analysis, and paper drafting.
- **[Agent Laboratory](agent-laboratory.md)** — An end-to-end autonomous research workflow (arXiv:2501.04227) that guides a research idea through three phases — literature review, experimentation, and report writing — with specialized LLM-driven agents and external tools (arXiv, Hugging Face, Python, LaTeX).
- **[APE — Automated Peer Evaluator](ape.md)** — A focused tool for automated peer evaluation of submitted papers, sitting at the *referee-simulation* stage of the RISE pipeline.
- **[AutoSurvey](autosurvey.md)** — A NeurIPS 2024 framework (arXiv:2406.10252) for automatically generating comprehensive literature surveys from a topic and a paper database.
- **[Aviary (FutureHouse)](aviary.md)** — A gymnasium for defining custom language-agent environments (arXiv:2412.21154), with pre-built environments for math, general knowledge, biological sequences, scientific literature search, and protein stability.
- **[coarse.ink](coarse-ink.md)** — Research-workflow tooling that supports upstream stages of writing and project management.
- **[DeepResearcher (GAIR-NLP)](deepresearcher.md)** — An end-to-end RL-trained deep-research agent (arXiv:2504.03160) that learns to plan, retrieve, cross-validate, and self-reflect via reinforcement learning in real-world web environments rather than in simulated retrieval.
- **[GPT Researcher](gpt-researcher.md)** — An autonomous "deep research" agent that produces long-form, cited reports on any topic from web and local sources.
- **[Kosmos (jimmc414 implementation)](kosmos.md)** — An open-source implementation of the Kosmos AI scientist architecture (Lu et al., arXiv:2511.02824), adapted to run via Claude Code or the Anthropic / OpenAI APIs.
- **[MARG (Multi-Agent Review Generation)](marg.md)** — A research artifact (arXiv:2401.04259) and reusable demo for generating peer reviews of scientific papers using multiple specialized agents.
- **[MLGym (Meta)](mlgym.md)** — A gym-style framework and benchmark (MLGym-Bench, arXiv:2502.14499) for advancing AI research agents on 13 diverse ML research tasks (CV, NLP, RL, game theory).
- **[Open CoScientist Agents](open-coscientist.md)** — An open-source implementation of Google DeepMind's *AI co-scientist* (arXiv:2502.18864), built on LangGraph and GPT Researcher.
- **[OpenScholar (AI2)](open-scholar.md)** — A retrieval-augmented LM designed to answer scientific queries by searching the literature and generating responses grounded in sources.
- **[PaperQA2 (FutureHouse)](paper-qa.md)** — A high-accuracy retrieval-augmented generation package focused on scientific PDFs (and Office docs, source code).
- **[PaperCoder (Paper2Code)](paper2code.md)** — An ICLR 2026 multi-agent system (arXiv:2504.17192) that transforms a machine-learning paper into a working code repository via a three-stage pipeline (planning, analysis, code generation) with specialized agents per stage.
- **[refine.ink](refine-ink.md)** — Academic prose tooling focused on the revision/editing stage of the RISE pipeline.
- **[ResearchAgent (NAACL 2025)](researchagent.md)** — The NAACL 2025 reference implementation (arXiv:2404.07738) of *iterative research idea generation over scientific literature*.
- **[Reviewer (Ingar30)](reviewer.md)** — A reproducible multi-agent reviewer for academic economics papers.
- **[Robin (FutureHouse)](robin.md)** — A multi-agent system for automating scientific discovery (arXiv:2505.13400), with explicit support for hypothesis generation, experiment design, and data analysis.
- **[Sakana AI Scientist v2](sakana-ai-scientist.md)** — An autonomous "AI scientist" pipeline that ideates, runs experiments (primarily ML), drafts a paper, and self-reviews.
- **[Sakana AI Scientist (v1)](sakana-ai-scientist-v1.md)** — The original AI Scientist release (arXiv:2408.06292): an end-to-end agentic pipeline that ideates, runs experiments, and writes a paper with self-review on a fixed set of CS templates (NanoGPT, 2D Diffusion, Grokking).
- **[Social Science Replicability Infrastructure](social-science-replicability.md)** — Infrastructure aimed at the replication stage of the RISE pipeline: given a published paper, attempt to reproduce its empirical results in an automated or semi-automated fashion.
- **[STORM / Co-STORM](storm.md)** — An LLM-powered knowledge-curation system that writes Wikipedia-style long-form articles from web search.
- **[SurveyX](surveyx.md)** — An academic survey-automation system (arXiv:2502.14776) that generates domain-specific surveys from a paper title plus retrieval keywords.
- **[Tongyi DeepResearch](tongyi-deepresearch.md)** — An agentic large language model purpose-built for long-horizon deep-information-seeking tasks (arXiv:2510.24701), shipped both as open weights (30.5B total / 3.3B active) and as inference code with ReAct and 'Heavy' (IterResearch) modes.
- **[ToolUniverse](tooluniverse.md)** — A curated tool registry and MCP server (arXiv:2509.23426) that packages biomedical, chemical, and general scientific APIs into a uniform agent-callable surface.
- **[zeropaper](zeropaper.md)** — An autonomous paper-writing pipeline that takes a research topic and produces a written paper with minimal user input.

<!-- AUTO-GENERATED:projects-end -->

## How to add a project

1. Copy `projects/landscape/sakana-ai-scientist.yml` as a template.
2. Fill in fields per [`projects/schema.md`](https://github.com/bhanneke/RISE/blob/main/projects/schema.md).
3. Score it against [`projects/EVALUATION.md`](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).
4. Open a pull request.
