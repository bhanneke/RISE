---
citekey: zhang2026agora
title: 'Agora: Git as Shared Memory for Collective AutoResearch'
authors:
- 'Zhang, Y.'
- 'Zou, Y.'
- 'Zhang, S.'
- 'Hu, J.'
- 'Zhang, H.'
- 'Xu, B.'
- 'Kautz, J.'
- 'Dong, Y.'
year: 2026
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2609.18094
kind: preprint
themes:
- autonomous-research-agents
- agentic-reasoning
- evaluation-of-ai-research
methods:
- system-design
- large-scale-deployment
relates_to_projects: []
status: skimmed
arxiv_id: '2609.18094'
---

## Summary

Agora (NVIDIA) gives research agents working in separate sessions a
shared memory: an append-only directed acyclic graph stored in Git,
where each commit records a result, insight, hypothesis, verification
or report and links to prior work. Searchable views surface leading
results, neglected branches and verification status, and
diversity-aware recommendations push experiments away from the current
leaders. The reported run is unusually concrete: nearly 12 days, 13
language-model workers, **no assigned tasks and no central planner**,
attacking a weight-transfer problem — initialise a frozen 119.6M
attention-SSM hybrid from 141 pretrained donor models, with no
training data and no gradient updates. The workers published 1,703
contributions and cut the development evaluator score from 3.39 to
1.899 bits per byte, closing 62% of the gap to a trained GPT-2 124M.
The winning method's ancestry spans 145 commits across 15 accounts,
and participants posted 165 independent reproductions.

## Contribution

Claimed and evidenced: a coordination substrate for many agents
working asynchronously without a planner, plus a run showing
cumulative progress attributable to it. The provenance numbers
(145-commit ancestry across 15 accounts, 165 reproductions) are the
strongest part — they demonstrate that contributions actually built on
each other rather than running in parallel.

## Method

System paper with a single deep deployment. Evaluation is by the
scientific outcome (bits per byte on a held-out evaluator) and by
process statistics from the Git DAG. There is no comparison against a
centrally planned baseline or a single-agent control, so the causal
contribution of Agora itself versus 13 workers and 12 days of compute
is not isolated.

## Relevance to RISE

Directly relevant to the catalog's end-to-end and multi-agent
entries, and closest in spirit to `deepscientist` (a Git repo per
research quest) — but Agora makes the repository the *coordination
mechanism* rather than a record. For the RISE pipeline anatomy it is
the clearest worked example of persistent shared memory as
infrastructure rather than as an agent's private scratchpad. For the
*Architecture as Epistemology* question it is a natural experiment at
the extreme of the structure axis: no hierarchy, no planner, pure
stigmergic coordination through an append-only artefact, with
diversity-aware recommendation as an explicit anti-herding mechanism —
which is exactly the intervention the diversity-collapse literature
(`chen2026diversity`, `kong2026multillm`) says is needed.

## Critique / open questions

n=1 deployment on a task with a cheap machine-checkable score
(bits per byte); whether the design survives tasks where no such
oracle exists is untested, and that regime is where most research
lives. No ablation of the diversity-aware recommender, so its
contribution to avoiding premature convergence is asserted rather than
shown. Cost is not reported in the abstract.

## Key quotes

> "Agora stores their contributions as an append-only directed acyclic
> graph (DAG) in Git. Each commit records a result, insight,
> hypothesis, verification, or report and links it to prior work."
> (abstract)

> "We report a run of nearly 12 days in which 13 language-model
> workers, with no assigned tasks or central planner, used Agora to
> solve a weight-transfer problem." (abstract)

> "They published 1,703 contributions and reduced the development
> evaluator score from 3.39 to 1.899 bits per byte, closing 62% of the
> gap to a trained GPT-2 124M." (abstract)
