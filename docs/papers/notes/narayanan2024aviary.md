---
citekey: narayanan2024aviary
title: 'Aviary: training language agents on challenging scientific tasks'
authors:
- Narayanan, S.
- Braza, J. D.
- Griffiths, R.
- Ponnapati, M.
- Bou, A.
- Laurent, J.
- Kabeli, O.
- Wellawatte, G.
- Cox, S.
- Rodriques, S. G.
- White, A. D.
year: 2024
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2412.21154
kind: preprint
themes:
- agentic-tool-use
- agentic-reasoning
- evaluation-of-ai-research
methods:
- framework-design
- agent-training
- benchmark-evaluation
relates_to_projects:
- aviary
status: skimmed
arxiv_id: '2412.21154'
---

## Summary

Aviary is FutureHouse's extensible "gymnasium" for language agents,
motivated by the observation that scientific tasks require many cycles
of analysis, tool use and experimentation, and that agents' flexible
components (internal reasoning, planning, tool use, sampling
stochasticity) make software implementations hard to standardize. The
paper formalizes agents as policies solving language-grounded partially
observable Markov decision processes, which it calls language decision
processes. It implements five environments, three of them scientific:
manipulating DNA constructs for molecular cloning, answering research
questions from the scientific literature, and engineering protein
stability, chosen for multi-step reasoning and relevance to current
biology. Using online training and inference-time compute scaling, the
authors report that agents built on open-source, non-frontier LLMs can
match and exceed frontier-LLM agents and human experts on multiple
tasks at up to 100x lower inference cost.

## Contribution

Claimed: a formalism (language decision processes), a software
gymnasium with scientific environments, and evidence that trained
open-model agents rival frontier agents and experts at much lower cost.
What the abstract supports: the existence of the formalism and the five
environments, and a qualitatively stated result. "Multiple tasks",
"match and exceed" and "up to 100x" are not quantified per task in the
abstract, and the training method is named only as "online training".

## Method

As far as the abstract states: five environments (three scientific);
agents formalized as policies over language decision processes; online
training plus scaling of inference-time compute; comparison against
frontier-LLM agents and human experts. The abstract does not specify
the training algorithm, which open-source models were trained, how
inference-time compute was scaled (sampling, voting, search), how human
expert baselines were collected, on which tasks the agents exceeded
experts, or how cost was measured. arXiv v1 only (December 2024); no
comments or journal reference on the listing.

## Relevance to RISE

The literature-question environment informs the `literature-discovery`
stage and the analysis-heavy biology environments the `data-analysis`
stage, matching the catalog's tags. Catalog slug:
[`aviary`](../../projects/aviary.md); the catalog lists
[`paper-qa`](../../projects/paper-qa.md) and
[`robin`](../../projects/robin.md) as related FutureHouse projects that
Aviary evaluates. Compared with [`mlgym`](../../projects/mlgym.md),
both are gym-style abstractions for research agents, but Aviary's
scientific environments are biology tasks and its abstract reports
training results, whereas MLGym's abstract targets ML research tasks
and reports only evaluation of untrained frontier models. For the ISR
question of structure and epistemic quality, the abstract names
"scaling inference-time compute" as a lever without saying whether it
means sampling, voting or search, so no specific aggregation rule can
be attributed; the language-decision-process formalism is nonetheless
useful because it gives a vocabulary in which debate, tournament or
tree-search structures can be expressed as policies over a shared
environment and scored on fixed tasks.

## Critique / open questions

From the abstract one cannot assess how the human-expert baseline was
designed, whether "100x lower inference cost" excludes training cost,
or how the stochasticity the abstract itself flags was handled in
evaluation. The three scientific environments are biology-specific, so
transfer to social-science or economics research is untested here (the
catalog entry notes limited social-science coverage). The abstract
concedes no limitations. Whether results hold for the open-source
models available at the time of writing versus later frontier models is
an open question the abstract cannot answer.

## Key quotes

> "Here, we introduce Aviary, an extensible gymnasium for language
> agents. We formalize agents as policies solving language-grounded
> partially observable Markov decision processes, which we term language
> decision processes." (abstract)

> "We then implement five environments, including three challenging
> scientific environments: (1) manipulating DNA constructs for molecular
> cloning, (2) answering research questions by accessing scientific
> literature, and (3) engineering protein stability." (abstract)

> "Finally, with online training and scaling inference-time compute, we
> show that language agents backed by open-source, non-frontier LLMs can
> match and exceed both frontier LLM agents and human experts on
> multiple tasks at up to 100x lower inference cost." (abstract)
