---
citekey: li2026agenticbiomedical
title: Agentic AI and the Rise of in silico Team Science in Biomedical Research
authors:
- Li, B.
- Saini, A. K.
- Hernandez, J. G.
- Moore, J. H.
year: 2026
venue: Nature Biotechnology 44(5):711–725
doi: 10.1038/s41587-026-03035-1
url: https://doi.org/10.1038/s41587-026-03035-1
kind: review
themes:
- agentic-pipelines
- multi-agent-systems
- autonomous-research-agents
- sociotechnical
methods:
- narrative-review
- typology
relates_to_projects: []
status: read
---

## Summary

A Nature Biotechnology review framing the emerging class of agentic
AI systems as *teams of intelligent computational experts* — an
"in silico team science" — capable of taking on labor-intensive
biomedical research tasks such as literature review, hypothesis
formulation, data analysis, and model interpretation. The paper
organises the design space around **three key algorithms** and
**seven foundational building-block characteristics** that
distinguish deployable agentic systems from prompt-chaining
prototypes, and surveys applications in drug discovery, data
analysis, and biomarker identification.

## Contribution

A structured *typology* for agentic-AI systems in a high-stakes
domain. Where most prior reviews are either too general
(LLM-as-tool-use survey) or too narrow (single application paper),
this one positions itself at the seam between agent architecture and
biomedical workflow — naming the algorithms and characteristics that
practitioners should think about before deploying. The "in silico
team science" framing is itself a contribution: it reframes
agentic-AI from "automated assistant" to "distributed collaborator
team", with implications for credit, oversight, and integration into
existing research-lab social structures.

## Method

Narrative review; surveys recent agentic-AI work in biomedical
research and synthesises into a structured framework of algorithms
and characteristics. No primary empirical evaluation.

## Relevance to RISE

A useful *theoretical anchor* for the RISE concept paper. Three
specific points of contact:

- **"In silico team science" framing** parallels the sociotechnical
  framing RISE proposes — agentic pipelines are not just tools but
  collaborator teams that need integration into existing research
  practices.
- **Domain-specific concretisation**: biomedical research is one of
  the fields where agentic pipelines have already demonstrated
  end-to-end value ([ghareeb2026robin](ghareeb2026robin.md) is the
  clearest example), so a review that surveys this surface is
  directly applicable when discussing field-level adoption.
- **Building-block taxonomy** complements the architectural
  decomposition in [yang2026aris](yang2026aris.md) — Yang et al.
  argue for three system layers (execution, orchestration,
  assurance); Li et al. add seven characteristics that any layer
  needs to satisfy. The two papers are complementary perspectives on
  the same design problem.

## Critique / open questions

A review-paper limitation applies: the seven characteristics and
three algorithms are extracted from existing systems rather than
validated empirically against a benchmark of deployment outcomes.
The framework risks being too high-level for engineers and too
prescriptive for theorists. The "team science" metaphor is
provocative but unargued — whether agentic systems actually behave
like research teams (with division of labor, conflict, coordination
overhead) vs. like distributed function calls is an empirical
question the paper does not test. As is typical for Nature Biotech
review articles, the focus is biomedical; whether the framework
ports to other research domains (economics, social science) is
unaddressed.

## Key quotes

> "Agentic artificial intelligence (AI) systems are emerging as teams
> of intelligent computational experts capable of rivaling human
> performance in labor-intensive tasks, including literature review,
> hypothesis formulation, data analysis and model interpretation."

> "These systems are poised to accelerate labor-intensive biomedical
> research by making autonomous decisions based on contextual
> information and expert feedback."

> "Here we discuss three key algorithms and seven foundational
> building-block characteristics that contribute to the development
> of agentic AI systems. We highlight their biomedical applications,
> design considerations and the challenges and opportunities
> associated with deploying agentic AI systems to advance
> collaborative scientific research."
