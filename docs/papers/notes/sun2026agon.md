---
citekey: sun2026agon
title: 'Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy'
authors:
- 'Sun, Y.'
- 'Ren, X.'
- 'Yi, C.'
- 'Guo, J.'
- 'Zhang, K.'
- 'Du, J.'
- 'Yang, H.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2606.24177
kind: preprint
themes:
- autonomous-research-agents
- evaluation-of-ai-research
methods:
- system-design
- failure-taxonomy
- large-scale-deployment
relates_to_projects:
- agon
status: skimmed
arxiv_id: '2606.24177'
---

## Summary

Agon is a research orchestrator built on the premise that LLMs make
research *production* scalable, shifting the bottleneck from producing
artifacts to judging claims. Its answer: validate what can be checked
inside the workflow and leave the remaining judgments to human
scientists. The system rests on six design principles — Prompt
Economy, Future-Facing, Minimal Prompts, OmniDisciplinary, Massive
Parallelism, and Zero-Code — and was run across domains for 444
iterations of Prompt Economy loops, starting from small topics with no
human-written experimental code. The deployments demonstrate
scalability while exposing new classes of failure, which the authors
organize into a taxonomy along severity, fixability, visibility, and
capability locus.

## Contribution

Claimed: a scalable omnidisciplinary research orchestrator plus a
failure taxonomy that separates failures the loops can see and fix
from those that require human judgment, pushing toward a "machine
scales, human steers" paradigm. What the abstract supports: a
large-scale deployment (444 loop iterations) and the taxonomy; no
quality benchmark against other systems or human baselines is
mentioned.

## Method

System paper with at-scale deployment as the evidence base. The
abstract does not specify the domains covered, the underlying models,
how outputs were judged, or any quantitative quality metrics — only
the iteration count and the failure-taxonomy dimensions.

## Relevance to RISE

Informs rq-formulation through paper-drafting at the orchestration
level; catalog slug `agon`. The design question it poses — which
validations live inside the automated loop and which judgments are
reserved for humans — is a direct instance of the structure/aggregation
allocation question in the *Architecture as Epistemology* paper, and
its failure taxonomy (visibility and capability locus) is an attempt
to operationalize what the loop can and cannot certify about its own
output.

## Critique / open questions

Whether "Prompt Economy" delivers quality rather than only volume
cannot be assessed from the abstract: no external evaluation, no
acceptance outcomes, no comparison condition. The failure taxonomy's
inter-rater reliability and the base rates of each failure class are
not stated. The claim that remaining judgments are "left to human
scientists" leaves open how much human labor the 444 iterations
actually consumed.

## Key quotes

> "Large language models are making research production scalable,
> shifting the bottleneck from producing artifacts to judging claims."
> (abstract)

> "We organize these failures into a taxonomy along severity,
> fixability, visibility, and capability locus. The taxonomy separates
> failures the loops can see and fix from those that require human
> judgment." (abstract)

> "Together, these results show that Agon is pushing research toward a
> new paradigm: machine scales, human steers." (abstract)
