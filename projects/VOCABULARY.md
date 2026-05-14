# Controlled vocabularies

This file is the single source of truth for the tag values used across
both knowledge bases. Adding or renaming a tag is a deliberate act:
update this file, update affected entries, regenerate indexes.

---

## Themes — for **papers** KB

A paper note may carry multiple themes.

| Tag | Meaning |
|-----|---------|
| `autonomous-research-agents` | End-to-end "AI scientist" systems; pipelines that aim to produce a paper without human intervention. |
| `agentic-tool-use` | Tool-augmented LLMs; the toolformer line; MCP-style protocols. |
| `agentic-reasoning` | Multi-step planning, decomposition, ReAct-style loops. |
| `hallucination` | Factual fabrication, citation invention, ungrounded claims. |
| `reasoning-faithfulness` | Whether the reasoning a model verbalizes matches what drives its outputs. |
| `llm-cognition` | The debate over LLM understanding, generalization, world models. |
| `ai-peer-review` | LLMs as reviewers; AI's effects on peer review; checklist assistants. |
| `research-productivity` | Empirical studies of AI augmenting researchers' output. |
| `style-engines` | The framing of GenAI as a producer of *forms* / templates. |
| `is-methodology` | Methodological reflection on IS research with GenAI. |
| `sociotechnical` | The sociotechnical lens; anthropomorphism; discipline-level effects. |
| `replication-infrastructure` | Automated replication systems; replicability tooling. |
| `ai-publishing-ecosystems` | aixiv and similar; AI-native publication venues. |
| `evaluation-of-ai-research` | Benchmarks, rubrics, and metrics for AI-generated research output. |
| `human-ai-research-collaboration` | Division of labor between researchers and agents. |

---

## Pipeline stages — for **projects** KB

A project may cover multiple stages. Used to compute lifecycle coverage.

| Tag | Meaning |
|-----|---------|
| `rq-formulation` | Sharpening an underspecified prompt into a research question. |
| `hypothesis-generation` | Generating testable hypotheses. |
| `literature-discovery` | Finding relevant papers. |
| `literature-synthesis` | Summarizing, integrating, identifying gaps. |
| `research-design` | Choosing method, identification strategy, data plan. |
| `data-acquisition` | Fetching, scraping, requesting datasets. |
| `data-analysis` | Cleaning, exploratory + confirmatory analysis. |
| `formal-modeling` | Theoretical / mathematical models, simulations. |
| `code-generation` | Producing analysis or replication code. |
| `paper-drafting` | First-draft generation of paper sections. |
| `revision-editing` | Improving prose, structure, argumentation. |
| `referee-simulation` | Pre-submission peer-review simulation. |
| `replication` | Reproducing the results of a published paper end-to-end. |
| `dissemination` | Formatting for journals/preprints; submission packaging. |

---

## Architectural features — for **projects** KB

How the system is built. Multiple tags allowed.

| Tag | Meaning |
|-----|---------|
| `single-llm` | One LLM, one process, no orchestration. |
| `multi-agent` | Multiple specialized agents collaborating. |
| `human-in-loop` | Mandatory human approval gates within the pipeline. |
| `tool-use` | LLM invokes external tools (code, search, APIs). |
| `rag-knowledge-base` | Retrieval-augmented generation over a curated KB. |
| `persistent-memory` | State that survives across runs (not just session context). |
| `dag-orchestration` | Workflow expressed as a directed acyclic graph of stages. |
| `iterative-loop` | Refinement loops with stopping criteria. |
| `debate-consensus` | Multiple agents debate or vote toward consensus. |
| `artifact-versioning` | Outputs are versioned and persisted as first-class artifacts. |

---

## Disciplinary scope — for **projects** KB

Single tag preferred; `general` if domain-agnostic.

| Tag | Meaning |
|-----|---------|
| `general` | Domain-agnostic. |
| `economics` | Economics, finance, applied econometrics. |
| `finance` | Specifically empirical finance / asset pricing / market microstructure. |
| `biomedical` | Biology, medicine, clinical research. |
| `computer-science` | ML/CS research itself as the object. |
| `social-sciences` | Sociology, political science, psychology, behavioral. |
| `information-systems` | IS as an academic discipline (MIS Quarterly, ISR, etc.). |

---

## How to extend

1. Propose the new tag in an issue/PR.
2. Add it to this file with a one-line definition.
3. Apply it to existing entries where it now applies.
4. Regenerate indexes: `python scripts/build_indexes.py`.

Avoid synonyms. Avoid sub-types unless ≥3 entries justify the
distinction.
