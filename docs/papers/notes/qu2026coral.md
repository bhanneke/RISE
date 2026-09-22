---
citekey: qu2026coral
title: 'CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery'
authors:
- Qu, A.
- Zheng, H.
- Zhou, Z.
- Yan, Y.
- Tang, Y.
- Ong, S. Y.
- Hong, F.
- Zhou, K.
- Jiang, C.
- Kong, M.
- et al.
year: 2026
venue: COLM 2026 (arXiv 2604.01658)
doi: ''
url: https://arxiv.org/abs/2604.01658
kind: paper
themes:
- autonomous-research-agents
- agentic-reasoning
methods:
- system-design
- benchmark-evaluation
- mechanistic-analysis
relates_to_projects:
- coral
status: skimmed
arxiv_id: '2604.01658'
---

## Summary

CORAL is a framework for autonomous multi-agent evolution on
open-ended problems. Where existing LLM-based evolution relies on
fixed heuristics and hard-coded exploration rules, CORAL uses
long-running agents that explore, reflect, and collaborate through
shared persistent memory, asynchronous multi-agent execution, and
heartbeat-based interventions, with safeguards including isolated
workspaces, evaluator separation, resource management, and agent
session and health management. On mathematical, algorithmic, and
systems optimization tasks it sets new state-of-the-art results on 10
tasks, with 3-10 times higher improvement rates and far fewer
evaluations than fixed evolutionary search baselines. On Anthropic's
kernel engineering task, four co-evolving agents improve the best
known score from 1363 to 1103 cycles. Mechanistic analyses attribute
the gains to knowledge reuse and to multi-agent exploration and
communication, which the authors read as evidence that greater agent
autonomy and multi-agent evolution improve open-ended discovery.

## Contribution

Claimed: "the first framework for autonomous multi-agent evolution on
open-ended problems", and the thesis that agent autonomy beats fixed
heuristics. What the abstract supports: state-of-the-art results on
10 tasks against fixed evolutionary search baselines (unnamed in the
abstract), one concrete kernel-engineering improvement, and
analyses said to trace gains to knowledge reuse and inter-agent
communication. "Open-ended discovery" is operationalized as score
improvement on graded optimization tasks rather than as knowledge
claims. The priority claim ("first") cannot be verified from the
abstract.

## Method

Evaluation on diverse mathematical, algorithmic, and systems
optimization tasks against fixed evolutionary search baselines; a
four-agent case on Anthropic's kernel engineering task; mechanistic
analyses of where gains come from. The abstract does not specify the
baselines, the base models, the number of agents per task (four is
given only for the kernel case), evaluation budgets, variance across
runs, the precise definition of "improvement rate", what
heartbeat-based interventions do, or how evaluator separation is
enforced.

## Relevance to RISE

Informs research-design, code-generation, and data-analysis; the
catalog entry `coral` also tags referee-simulation for its rubric
judge packages and classes the system as optimization infrastructure
rather than scholarly authoring. Its closest catalog neighbor is
[jin2026arbor](jin2026arbor.md): both carry persistent memory across
experiments on optimization tasks, but CORAL's agents are peers
sharing memory asynchronously whereas Arbor's are executors under a
coordinator over a tree. For the multi-agent structure/aggregation
question this abstract treats the structure itself as the treatment:
gains are credited to multi-agent exploration and communication and
to knowledge reuse, "evaluator separation" keeps the scoring role
distinct from the generating agents, and the mechanistic analyses are
presented as showing how the multi-agent arrangement produces the
improvement — though the abstract does not state a single-agent
control at equal budget.

## Critique / open questions

The autonomy-versus-heuristics comparison is confounded unless the
baselines used equally capable models and comparable budgets; "far
fewer evaluations" addresses budget but not model quality. Whether
the gains come from having multiple agents or from the long-running,
reflective design of each agent cannot be separated from the
abstract. Reducing "discovery" to a grader score means the epistemic
quality of what the agents learn is not assessed. The safeguards are
listed but no failure modes of long-running autonomous agents are
reported. The abstract concedes no limitations explicitly. On
metadata: the COLM 2026 venue comes from the catalog project entry
(the bib note says "per project entry"); the arXiv v2 record fetched
for this note shows no comments or journal-reference field confirming
it.

## Key quotes

> "CORAL replaces rigid control with long-running agents that explore,
> reflect, and collaborate through shared persistent memory,
> asynchronous multi-agent execution, and heartbeat-based
> interventions." (abstract)

> "On Anthropic's kernel engineering task, four co-evolving agents
> improve the best known score from 1363 to 1103 cycles." (abstract)

> "Mechanistic analyses further show how these gains arise from
> knowledge reuse and multi-agent exploration and communication."
> (abstract)
