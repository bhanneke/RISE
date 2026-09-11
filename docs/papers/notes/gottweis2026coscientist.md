---
citekey: gottweis2026coscientist
title: Accelerating scientific discovery with Co-Scientist
authors:
- Gottweis, J.
- Weng, W.-H.
- Daryin, A.
- Tu, T.
- Sirkovic, P.
- Myaskovsky, A.
- Glowaty, G.
- Weissenberger, F.
- Orlandi, A.
- Popovici, D.
- et al.
year: 2026
venue: Nature (arXiv 2502.18864)
doi: 10.1038/s41586-026-10644-y
url: https://arxiv.org/abs/2502.18864
kind: paper
themes:
- autonomous-research-agents
- agentic-reasoning
- human-ai-research-collaboration
methods:
- system-design
- wet-lab-validation
- test-time-compute-scaling
relates_to_projects:
- google-co-scientist
- open-coscientist
status: skimmed
arxiv_id: '2502.18864'
---

## Summary

Co-Scientist is a multi-agent system built on Gemini for structured
scientific thinking and hypothesis generation. Conditioned on a
scientist's research objective and prior evidence, it produces
research hypotheses intended for experimental verification. Agents
continuously generate, critique, and refine hypotheses, and the
process is accelerated by scaling test-time compute through an
asynchronous task-execution framework and a tournament evolution
process. Automated evaluations show hypothesis quality improving with
additional compute. Although general-purpose, validation is focused on
three biomedical applications — drug repurposing, novel target
discovery, and mechanisms of antimicrobial resistance. In the acute
myeloid leukemia case, drug-repurposing candidates and synergistic
combination therapies proposed by the system were validated in vitro.
This is the Nature (2026) version of the February 2025 arXiv preprint
"Towards an AI co-scientist"; arXiv v2 (June 2026) carries the Nature
title.

## Contribution

Claimed: (1) a multi-agent architecture with asynchronous task
execution for flexible compute scaling, (2) a tournament evolution
process for self-improving hypothesis generation, "demonstrably novel"
hypotheses, and real-world validation. What the abstract supports:
in-vitro confirmation of AML candidates and an automated-evaluation
trend that quality rises with test-time compute. The abstract contains
no quantitative results, no comparison with human experts or other
systems, and no operational definition of "demonstrably novel", so
the size of the effect and the hit rate of proposed versus validated
hypotheses cannot be judged from it.

## Method

System paper with biomedical validation. Design: multi-agent
generate-critique-refine loop, tournament evolution, asynchronous
execution, test-time compute scaling. Evaluation: automated
evaluations of hypothesis quality as compute scales (metric and judge
unspecified in the abstract), plus three biomedical applications with
in-vitro experiments for AML. The abstract does not name the agent
roles (the catalog page, drawing on the paper body, lists Generation,
Reflection, Ranking, Proximity, Evolution, and Meta-review agents
under a Supervisor with Elo-based tournaments), the number of
hypotheses generated or tested, or how human collaborators selected
candidates for the wet lab.

## Relevance to RISE

Informs literature-synthesis, hypothesis-generation, and
research-design; it does not execute experiments, analyze data, or
draft papers. Two catalog entries depend on it: `google-co-scientist`
(the closed first-party system, scored 3 on internal evaluation for
this Nature paper and 0 on cross-family policy because every agent
runs on Gemini) and `open-coscientist` (an MIT-licensed
reimplementation of the arXiv v1 design). Compared with
[ghareeb2026robin](ghareeb2026robin.md), the other Nature 2026 paper
in the KB with wet-lab validation, Co-Scientist stops at ranked
hypotheses whereas Robin also proposes experiments and interprets
results. For the multi-agent structure/aggregation question this is
the clearest case in the batch: the abstract attributes
self-improvement directly to a tournament evolution process in which
agents generate, critique, and refine hypotheses, and reports that
hypothesis quality keeps improving as test-time compute is scaled
through that structure — an aggregation rule presented as the source
of epistemic gains, though the abstract does not separate the
tournament's contribution from that of more sampling or the base
model.

## Critique / open questions

The abstract is entirely qualitative on outcomes; whether hypothesis
"quality" was judged by humans or by models is not stated, so
circularity of the automated evaluations cannot be ruled out. The
in-vitro validations are the strongest evidence, but without the
number of proposed candidates the base rate is unknown. Single model
family throughout means the critics share the generator's blind spots
(the catalog page makes the same point). Generality beyond
biomedicine is claimed but not validated in the abstract. The catalog
project page lists the authors in a different order (Palepu fifth)
from the arXiv v2 record (Palepu eleventh); the note follows arXiv.

## Key quotes

> "The system's design involves agents continuously generating,
> critiquing and refining hypotheses accelerated by scaling test-time
> compute." (abstract)

> "Key contributions include: (1) a multi-agent architecture with an
> asynchronous task execution framework for flexible compute scaling;
> (2) a tournament evolution process for self-improving hypotheses
> generation." (abstract)

> "Specifically, Co-Scientist helped identify new drug repurposing
> candidates and synergistic combination therapies for acute myeloid
> leukemia, which were validated through in vitro experiments."
> (abstract)
