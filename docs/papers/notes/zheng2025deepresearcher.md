---
citekey: zheng2025deepresearcher
title: 'DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments'
authors:
- Zheng, Y.
- Fu, D.
- Hu, X.
- Cai, X.
- Ye, L.
- Lu, P.
- Liu, P.
year: 2025
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2504.03160
kind: preprint
themes:
- agentic-tool-use
- agentic-reasoning
- hallucination
methods:
- rl-training
- benchmark-evaluation
- qualitative-analysis
relates_to_projects:
- deepresearcher
status: skimmed
arxiv_id: '2504.03160'
---

## Summary

DeepResearcher is a framework for end-to-end training of LLM-based
deep-research agents by reinforcement learning in real-world web
environments with live search, as opposed to prompt engineering or RL
inside controlled RAG environments that assume a fixed corpus. It
uses a specialized multi-agent architecture in which browsing agents
extract relevant information from varied webpage structures. On
open-domain research tasks it reports gains of up to 28.9 points over
prompt-engineering baselines and up to 7.2 points over RAG-based RL
agents. A qualitative analysis reports emergent behaviors: planning,
cross-validating information across sources, self-reflection to
redirect research, and honesty when no definitive answer is found.
The authors argue that real-web training is a fundamental requirement
for robust research capability. Code is released (arXiv v4, April
2025).

## Contribution

Claimed: the first comprehensive end-to-end RL framework for deep
research in real web environments; quantitative gains over both
baseline families; emergent cognitive behaviors; the thesis that
real-web training is necessary rather than incidental.

What the abstract supports: the point gains are stated but the tasks
and metric are unnamed; "first" is a priority claim; the emergent
behaviors come from qualitative analysis and are not quantified; the
"fundamental requirement" thesis is an interpretation of the
real-web-versus-RAG-RL gap, which the abstract presents as a highlight
rather than as a controlled ablation.

## Method

Design: RL training (algorithm not named in the abstract) of an LLM
agent with authentic web search; a multi-agent architecture with
browsing agents that extract information from web pages.

Evaluation: open-domain research tasks (unnamed) against
prompt-engineering and RAG-based-RL baselines; qualitative analysis
of agent behavior.

Not specified in the abstract: the base model and its size (the
catalog records a 7B checkpoint), the benchmarks and metric, the
number of tasks, in-domain versus out-of-domain evaluation, reward
design, and training cost.

## Relevance to RISE

Informs `rq-formulation`, `literature-discovery`, and
`literature-synthesis` (the catalog's tags). Catalog slug:
`deepresearcher`. "Deep research" here means open-domain web
question answering, not scientific-literature synthesis, so the
paper is relevant to RISE mainly as a training-paradigm reference —
learned rather than scaffolded research behavior — which is how the
catalog frames it (runtime assurance 2 for emergent cross-validation,
self-reflection, and honest non-answers as internal checks). No
grounded comparison with other catalog systems can be drawn from the
abstract.

Multi-agent structure / aggregation: the "multi-agent architecture"
in the abstract is a functional decomposition (browsing agents that
extract information for the reasoning agent), not multi-perspective
debate or consensus; the epistemically interesting mechanism is
instead the reported emergent ability to "cross-validate information
from multiple sources" — an aggregation rule acquired through RL
rather than imposed by a scaffold — which the abstract documents only
qualitatively.

## Critique / open questions

- Emergent behaviors, including honesty when evidence is missing,
  are asserted from qualitative analysis; no rates are given in the
  abstract.
- The metric behind "points" is unstated, so the size of the gains
  cannot be interpreted from the abstract.
- Whether the learned behaviors transfer to scientific-literature
  tasks with citation requirements is untested here.
- Live-web RL makes exact reproduction difficult; the catalog notes
  non-deterministic inference by design.
- The abstract concedes no limitations.

## Key quotes

> "In this paper, we introduce DeepResearcher, the first
> comprehensive framework for end-to-end training of LLM-based deep
> research agents through scaling reinforcement learning (RL) in
> real-world environments with authentic web search interactions."
> (abstract)

> "Our qualitative analysis reveals emergent cognitive behaviors from
> end-to-end RL training, including the ability to formulate plans,
> cross-validate information from multiple sources, engage in
> self-reflection to redirect research, and maintain honesty when
> unable to find definitive answers." (abstract)

> "Our results highlight that end-to-end training in real-world web
> environments is not merely an implementation detail but a
> fundamental requirement for developing robust research capabilities
> aligned with real-world applications." (abstract)
