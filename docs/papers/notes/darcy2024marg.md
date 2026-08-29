---
citekey: darcy2024marg
title: 'MARG: Multi-Agent Review Generation for Scientific Papers'
authors:
- D'Arcy, M.
- Hope, T.
- Birnbaum, L.
- Downey, D.
year: 2024
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2401.04259
kind: preprint
themes:
- ai-peer-review
- evaluation-of-ai-research
methods:
- system-design
- user-study
relates_to_projects:
- marg
status: skimmed
arxiv_id: '2401.04259'
---

## Summary

MARG generates review-style feedback on scientific papers using
multiple GPT-4 instances that engage in internal discussion. The
paper's text is distributed across agents, which lets the system read
full papers that exceed the base model's context limit, and agents
are specialised with sub-tasks for different comment types
(experiments, clarity, impact). In a user study, GPT-4 baselines were
rated as producing generic or very generic comments more than half
the time, and the best baseline yielded only 1.7 comments per paper
rated good overall. MARG reduced the rate of generic comments from
60% to 29% and produced 3.7 good comments per paper, a 2.2x
improvement. Single arXiv version (Jan 2024); no journal reference is
listed.

## Contribution

Claimed: that multi-agent internal discussion plus specialisation
makes LLM feedback more specific and helpful. What the abstract
supports: the user-study figures as stated. The abstract does not
separate the effect of full-text access (context extension via
distribution) from the effect of specialisation and discussion, so
which structural feature drives the gain cannot be identified from
the abstract alone.

## Method

System description plus a user study comparing MARG to GPT-4
baselines on rated comment quality (generic vs. specific; good
overall). The abstract does not specify the number of papers or
raters, who the raters were, the rating scale, statistical tests, or
the paper domain. The catalog entry records the named baselines
(SARG-B, LiZCa), the ARIES dataset as data source, and bundled
reproduction configs and a GPT cache; none of that is in the
abstract.

## Relevance to RISE

Informs referee-simulation only, matching the catalog entry `marg`
(lifecycle coverage 0, single stage). It is a useful contrast to
`researchagent` ([baek2024researchagent](baek2024researchagent.md)):
ResearchAgent's ReviewingAgents critique machine-generated ideas
inside a generation loop, whereas MARG reviews human-written full
papers for their authors, so the two abstracts describe distinct
roles for "reviewer agents". For the ISR question on multi-agent
structure, MARG is a direct instance of the mechanism: several LLM
instances holding different parts of the paper and different
comment-type roles "engage in internal discussion" before feedback is
emitted, and the abstract attributes the drop in generic comments to
this structure; it does not describe the aggregation rule by which
the discussion becomes the final comment set.

## Critique / open questions

The abstract does not allow assessment of whether "good" comments are
correct (specificity is not accuracy), whether MARG's feedback would
change an editorial decision, cost or latency, or whether raters were
blind to condition. Generalisation beyond GPT-4 is unknown; the
catalog flags pre-2024 model assumptions. The abstract concedes the
baselines' generic-comment problem but states no limitation of MARG
itself; 29% of its comments remain generic by its own numbers.

## Key quotes

> "We study the ability of LLMs to generate feedback for scientific
> papers and develop MARG, a feedback generation approach using
> multiple LLM instances that engage in internal discussion."
> (abstract)

> "By distributing paper text across agents, MARG can consume the
> full text of papers beyond the input length limitations of the base
> LLM, and by specializing agents and incorporating sub-tasks tailored
> to different comment types (experiments, clarity, impact) it
> improves the helpfulness and specificity of feedback." (abstract)

> "Our system substantially improves the ability of GPT-4 to generate
> specific and helpful feedback, reducing the rate of generic comments
> from 60% to 29% and generating 3.7 good comments per paper (a 2.2x
> improvement)." (abstract)
