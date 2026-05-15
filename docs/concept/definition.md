# What is Research Information Systems Engineering?

## Working definition

**Research Information Systems Engineering (RISE)** is the discipline
concerned with the design, construction, and study of information
systems whose primary purpose is to *produce scholarly knowledge*.

A RISE system is distinguished from neighboring artifacts by three
commitments:

1. **Knowledge production as output.** The system's terminal artifacts
   are scholarly: papers, datasets, code releases, replication
   reports — not predictions, decisions, or recommendations as ends
   in themselves.
2. **Agentic mediation.** The pipeline is at least partially executed
   by AI agents — LLMs with tools, multi-agent orchestrations, or
   human–AI hybrids — not solely by human researchers using
   non-agentic software.
3. **Methodological accountability.** The system is designed against
   research-methodological norms (identification, replicability,
   peer-review readiness, citation grounding), not only against
   software-engineering norms.

The three commitments are jointly necessary. A system that produces
scholarly outputs without agentic mediation is a research
*workflow*, not RISE. An agentic system whose terminal artifact is a
chat response is a chatbot, not RISE. An agentic system that drafts
papers but does not engage methodological standards (no
identification, no citation grounding, no review) is a *style
engine* — see [@riemer2024styleengines] — useful, but not RISE.

## Why a separate name?

The umbrella terms in use — *AI for science*, *AI scientist*,
*agentic research*, *autonomous research agents* — each foreground
one face of the object. **AI for science** is too broad: it includes
AlphaFold-style prediction systems whose outputs are scientific
*claims about the world* rather than scholarly artifacts. **AI
scientist** anthropomorphizes a system as a researcher, which
prejudges the sociotechnical question (cf.
[@peter2025anthropomorphic]). **Agentic research** describes the
*method* but underspecifies the *output* and *accountability*
dimensions.

RISE names the engineering and methodological discipline that sits
across these — borrowing from information-systems design science,
e-Science research infrastructure, and AI4Science — and treats the
agentic research pipeline itself as its primary object of design and
study.

## What RISE is not

- **Generic AI-for-science tooling** (e.g., protein-structure
  prediction) that produces *scientific predictions* rather than
  scholarly artifacts.
- **Pure information-systems theory** without a built artifact.
- **AI writing assistants** whose unit of output is prose rather than
  research products.
- **Evaluation infrastructure** for AI systems
  (e.g., [`aviary`](../projects/aviary.md)) — directly relevant, but
  not a RISE pipeline.

## Scope of this knowledge base

RISE here is treated as a **named subfield**, not a synonym for "AI
for science." The literature surveyed (see [Papers](../papers/index.md))
foregrounds the *agentic pipeline* as the object of design and
study. The [projects catalog](../projects/index.md) evaluates concrete
systems — both owned (E2ER) and external (Sakana AI Scientist, STORM,
GPT Researcher, PaperQA2, OpenScholar, MARG, Agent Laboratory, Robin,
APE, Reviewer, …) — against a shared rubric.

## Sociotechnical commitment

This knowledge base sits, deliberately, in the **sociotechnical**
tradition of information systems research [@sarker2019sociotechnical].
A RISE contribution is not only a technical artifact: it is an
intervention in the social system of scholarship. That commitment
shapes the evaluation rubric (autonomy level and human-in-loop are
first-class), shapes the scope (peer-review tools are first-class
projects, not peripheral), and shapes the kinds of papers featured
in the literature (the discipline's reception of GenAI is as central
as its mechanics).

## Related fields

- **e-Science and research infrastructure.** Cyberinfrastructure for
  large-scale, data-intensive science.
- **AI4Science.** Broader — includes scientific prediction (AlphaFold)
  alongside scholarly-artifact production.
- **Information Systems (design-science tradition).** The
  methodological home of artifact-producing research.
- **Open and reproducible science.** Pre-registration, replication,
  computational reproducibility.
- **Science of science / metascience.** Empirical study of how
  research is produced and disseminated.

See [History](history.md) for the lineages these draw on.
