---
citekey: evoscientist2026techreport
title: 'EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific
  Discovery'
authors:
- Lyu, Y.
- Zhang, X.
- Yi, X.
- Zhao, Y.
- Guo, S.
- Hu, W.
- Piotrowski, J.
- Kaliski, J.
- Urbani, J.
- Meng, Z.
- Zhou, L.
- Yan, X.
year: 2026
venue: arXiv 2603.08127 (Huawei Technologies / Vrije Universiteit Amsterdam, Tech Report)
doi: ''
url: https://arxiv.org/abs/2603.08127
kind: tech-report
themes:
- agentic-pipelines
- multi-agent-systems
- self-improvement
- memory-systems
methods:
- system-design
- benchmark-evaluation
relates_to_projects: []
status: read
arxiv_id: '2603.08127'
---

## Summary

EvoScientist is a multi-agent AI-scientist framework that
*continuously evolves* its research strategies through persistent
memory and self-evolution, rather than relying on a static
hand-designed pipeline. It comprises three specialised agents — a
Researcher Agent (RA) for idea generation, an Engineer Agent (EA) for
experiment implementation and execution, and an Evolution Manager
Agent (EMA) that distils insights from prior interactions into
reusable knowledge. Two persistent memory modules — an *ideation
memory* (top-ranked feasible directions plus previously-rejected ones)
and an *experimentation memory* (effective data-processing and
training strategies) — feed back into RA and EA decisions on
subsequent runs.

## Contribution

A concrete answer to a recurring weakness of prior AI-scientist
systems (AI Scientist v2, AI-Researcher, InternAgent, Agent Lab):
they treat end-to-end discovery as a static execution pipeline and
"rarely distill accumulated outcomes and failures into reusable
experience." EvoScientist reformulates the problem as a learning task
where interaction histories are first-class artifacts and uses them to
improve both ideation quality and experiment-code success rates
across runs.

## Method

System paper with benchmark evaluation. Compares EvoScientist to seven
open-source and commercial AI-scientist baselines on (i) idea quality
(novelty, feasibility, relevance, clarity) via automatic + human
evaluation and (ii) end-to-end code execution success rates.

## Relevance to RISE

EvoScientist makes the *memory layer* an explicit architectural
component of an agentic research pipeline, separate from the agents
that produce ideas or code. This maps onto the RISE pipeline anatomy
where "Knowledge" flows in as a side input — here, the knowledge
accumulates from the system's own prior runs. The framing that
"interaction histories are a first-class resource rather than
discarded execution traces" is a useful design pattern to cite when
discussing what RISE harnesses should retain.

## Critique / open questions

Self-evolution claims rest on relative comparisons against seven
baselines — the absolute magnitude of improvement in idea quality
metrics depends heavily on the evaluators used. Whether the
ideation/experimentation memories generalise across domains (vs.
overfitting to the benchmark task suite) is not tested. As with most
AI-scientist papers, "novelty" is operationalised through automatic
proxies and human ratings; downstream impact (would the generated
ideas actually be published?) is out of scope.

## Key quotes

> "Most state-of-the-art AI scientist systems rely on static,
> hand-designed pipelines and fail to adapt their idea- or
> code-generation strategies based on accumulated interaction
> histories. As a result, these systems systematically overlook
> promising research directions, repeat previously failed
> experiments, and pursue infeasible ideas."

> "EvoScientist contains two persistent memory modules: (i) an
> ideation memory, which summarizes feasible research directions from
> top-ranked ideas while recording previously unsuccessful directions
> identified during idea validation; and (ii) an experimentation
> memory, which captures effective data processing and model training
> strategies derived from code search trajectories and best-performing
> implementations."

> "How can we formulate end-to-end scientific discovery as a learning
> problem in which multi-agent systems evolve their idea-generation
> and code-generation by learning from prior successes and failures?"
