---
citekey: baek2024researchagent
title: 'ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models'
authors:
- Baek, J.
- Jauhar, S. K.
- Cucerzan, S.
- Hwang, S. J.
year: 2024
venue: NAACL 2025 (arXiv 2404.07738)
doi: ''
url: https://arxiv.org/abs/2404.07738
kind: paper
themes:
- autonomous-research-agents
- ai-peer-review
- human-ai-research-collaboration
methods:
- system-design
- human-evaluation
- model-based-evaluation
relates_to_projects:
- researchagent
status: skimmed
arxiv_id: '2404.07738'
---

## Summary

ResearchAgent is an LLM system for research ideation grounded in the
literature. Starting from a core scientific paper, it gathers related
publications by walking an academic graph and pulls in entities from
a knowledge store mined from concepts shared across many papers. On
that basis it automatically defines a research problem, proposes a
method and designs experiments. These outputs are then refined
iteratively: multiple LLM-based ReviewingAgents provide reviews and
feedback, and the system revises. The reviewing agents are
instantiated with human-preference-aligned LLMs whose evaluation
criteria are elicited from actual human judgments. The authors
validate the system on publications from multiple disciplines using
both human and model-based evaluation of novelty, clarity and
validity, and frame the work as an initial step toward AI-mediated
research support. Published at NAACL 2025 (arXiv v2, Feb 2025).

## Contribution

Claimed: (i) literature- and entity-grounded idea generation, (ii) a
reviewer-agent revision loop with human-aligned criteria, and (iii)
demonstrated effectiveness across disciplines. What the abstract
supports: the architecture exists and human and model-based
evaluations favour it. The abstract reports no numbers, baselines or
effect sizes; "novel, clear, and valid" are rater-judged proxies, and
whether the generated ideas can actually be executed is not
evaluated. The abstract itself calls the work an "initial foray".

## Method

System paper. Pipeline: core paper, then academic-graph neighbours
plus knowledge-store entities, then problem / method / experiment
design, then iterative revision driven by multiple ReviewingAgents
whose criteria are elicited from human judgments via LLM prompting.
Evaluation: human and model-based ratings on publications across
multiple disciplines. The abstract does not specify how many papers
or disciplines, which LLMs, how many reviewing agents or revision
rounds, what the baselines were, inter-rater agreement, or how
"validity" is operationalised.

## Relevance to RISE

Informs literature-discovery, rq-formulation, hypothesis-generation
and research-design, matching the catalog entry `researchagent`,
which scores lifecycle coverage 1 because the system stops before
analysis, drafting or review of papers. It is the upstream complement
of `agent-laboratory`
([schmidgall2025agentlaboratory](../../projects/agent-laboratory.md)),
which takes a human-provided idea through literature review,
experimentation and report writing: ResearchAgent produces the idea.
Two of the authors (Baek, Hwang) also built `paper2code`
([seo2025paper2code](seo2025paper2code.md)), a downstream
code-generation system from the same group. For the ISR question on
multi-agent structure, the abstract describes an explicit
reviewer–author loop, with multiple ReviewingAgents giving feedback
and the generator revising iteratively, "mimicking a scientific
approach to improving ideas with peer discussions", and the
reviewers' criteria aligned to human judgments; the abstract does not
say how several reviews are aggregated (consensus, concatenation, or
otherwise) or whether the reviewers interact with one another.

## Critique / open questions

The abstract does not allow assessment of whether the reviewer loop
improves ideas relative to a single pass, since no ablation is
reported there. Model-based evaluation may share biases with the
generator (the catalog notes a single LLM family). Human-preference
alignment of reviewers could reward conformity and clarity over
substantive novelty. No test connects generated ideas to executed
studies or publications. The abstract concedes that this is an initial
foray. The catalog additionally notes no declared open-source license
and OpenAI-API lock-in.

## Key quotes

> "This system automatically defines novel problems, proposes methods
> and designs experiments, while iteratively refining them based on
> the feedback from collaborative LLM-powered reviewing agents."
> (abstract)

> "Then, mimicking a scientific approach to improving ideas with peer
> discussions, we leverage multiple LLM-based ReviewingAgents that
> provide reviews and feedback via iterative revision processes."
> (abstract)

> "These reviewing agents are instantiated with human
> preference-aligned LLMs whose criteria for evaluation are elicited
> from actual human judgments via LLM prompting." (abstract)
