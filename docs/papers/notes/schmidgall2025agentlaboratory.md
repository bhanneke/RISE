---
citekey: schmidgall2025agentlaboratory
title: 'Agent Laboratory: Using LLM Agents as Research Assistants'
authors:
- Schmidgall, S.
- Su, Y.
- Wang, Z.
- Sun, X.
- Wu, J.
- Yu, X.
- Liu, J.
- Moor, M.
- Liu, Z.
- Barsoum, E.
year: 2025
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2501.04227
kind: preprint
themes:
- autonomous-research-agents
- human-ai-research-collaboration
- evaluation-of-ai-research
methods:
- system-design
- human-evaluation
- cost-analysis
relates_to_projects:
- agent-laboratory
status: skimmed
arxiv_id: '2501.04227'
---

## Summary

Agent Laboratory is an LLM-agent framework that takes a human-provided
research idea through three stages — literature review,
experimentation, and report writing — and outputs a code repository
and a research report. Users can give feedback and guidance at each
stage. The authors run the framework with several state-of-the-art
LLMs and recruit researchers to assess it: participants answer a
survey, provide feedback that steers the process, and evaluate the
final paper. Four findings are reported: o1-preview yields the best
research outcomes; the generated ML code reaches state-of-the-art
performance relative to existing methods; human feedback at each
stage significantly improves overall research quality; and the
framework cuts research expenses by 84% compared with previous
autonomous research methods. The stated aim is to shift researcher
effort toward creative ideation rather than low-level coding and
writing.

## Contribution

Claimed: an end-to-end research-assistant framework, evidence that
per-stage human feedback improves output quality, and a large cost
reduction. What the abstract supports: the four findings are stated
as results of a deployment with human participants, but without
sample sizes, effect sizes, or the identity of the "previous
autonomous research methods" used as the cost baseline. The
distinctive framing is that of an assistant rather than a replacement
— the human supplies the idea and gates each stage — which is the
paper's clearest departure from
[lu2024aiscientist](lu2024aiscientist.md).

## Method

Deployment study. The framework is run with multiple LLM back-ends;
"multiple researchers" participate through a survey, in-process
feedback, and final-paper evaluation. The abstract does not specify
how many researchers took part, how many research ideas were run,
what rubric the final evaluation used, whether evaluators were blind
to condition, what statistical test underlies "significantly", which
existing methods the generated code was compared against, or how the
84% cost figure was computed.

## Relevance to RISE

Informs literature-discovery, literature-synthesis, research-design,
code-generation, data-analysis, and paper-drafting; it is the paper
behind the catalog entry `agent-laboratory`, which scores autonomy at
2 (research assistant with human gates) and, following ARIS Table 4,
flags the absence of adversarial review and in-pipeline assurance.
Consistent with that, the abstract describes no referee-simulation or
automated-review stage, unlike the Sakana line
([lu2024aiscientist](lu2024aiscientist.md),
[yamada2025aiscientistv2](yamada2025aiscientistv2.md)). For the
multi-agent structure/aggregation question: the abstract describes a
sequential three-stage pipeline whose quality-control mechanism is a
human feedback gate at each stage rather than debate, tournaments, or
an automated review loop — and its finding that per-stage human
feedback "significantly improves the overall quality of research" is
itself a result about how an aggregation rule (human gate vs. none)
shapes output quality.

## Critique / open questions

The human-involvement finding is the most useful for RISE but is
reported without magnitude, and the abstract leaves open whether the
researchers who gave feedback were also the ones who evaluated the
final papers. "State-of-the-art performance" of generated code is a
strong claim with no task named in the abstract. The 84% cost
reduction is relative to an unnamed baseline, so it cannot be
interpreted. The abstract concedes no limitations; the catalog page
adds a computer-science orientation and dependence on the chosen
back-end and supervision points. Whether the AgentRxiv extension
described on the catalog page is part of this paper cannot be
determined from the abstract.

## Key quotes

> "This framework accepts a human-provided research idea and
> progresses through three stages--literature review, experimentation,
> and report writing to produce comprehensive research outputs,
> including a code repository and a research report, while enabling
> users to provide feedback and guidance at each stage." (abstract)

> "(3) Human involvement, providing feedback at each stage,
> significantly improves the overall quality of research; (4) Agent
> Laboratory significantly reduces research expenses, achieving an 84%
> decrease compared to previous autonomous research methods."
> (abstract)

> "We hope Agent Laboratory enables researchers to allocate more effort
> toward creative ideation rather than low-level coding and writing,
> ultimately accelerating scientific discovery." (abstract)
