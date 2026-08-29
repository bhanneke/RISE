---
citekey: nathani2025mlgym
title: 'MLGym: A New Framework and Benchmark for Advancing AI Research Agents'
authors:
- Nathani, D.
- Madaan, L.
- Roberts, N.
- Bashlykov, N.
- Menon, A.
- Moens, V.
- Budhiraja, A.
- Magka, D.
- Vorotilov, V.
- Chaurasia, G.
- et al.
year: 2025
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2502.14499
kind: preprint
themes:
- evaluation-of-ai-research
- autonomous-research-agents
- agentic-tool-use
methods:
- framework-design
- benchmark-evaluation
relates_to_projects:
- mlgym
status: skimmed
arxiv_id: '2502.14499'
---

## Summary

Meta MLGym and MLGym-Bench are a framework and benchmark for evaluating
and developing LLM agents on AI research tasks. The authors present it
as the first Gym environment for machine-learning tasks, intended to
enable reinforcement-learning research on training such agents.
MLGym-Bench contains 13 open-ended AI research tasks drawn from
computer vision, NLP, reinforcement learning and game theory; solving
them is meant to require generating ideas and hypotheses, creating and
processing data, implementing methods, training models, running
experiments, analyzing results and iterating. Five frontier models
(Claude-3.5-Sonnet, Llama-3.1 405B, GPT-4o, o1-preview, Gemini-1.5 Pro)
are evaluated. The headline finding is that these models improve on the
provided baselines, usually by finding better hyperparameters, but do
not generate novel hypotheses, algorithms, architectures or substantial
improvements. Framework and benchmark are open-sourced.

## Contribution

Claimed: the first Gym environment for ML research tasks, a 13-task
benchmark, an extensible framework (adding tasks, integrating agents,
synthetic data generation, developing learning algorithms), and an
empirical finding about frontier models. What the abstract supports:
the task set, the list of evaluated models and the qualitative finding.
The "first Gym" claim is not verifiable from the abstract. The
RL-training affordance is described as enabled, not demonstrated — the
abstract reports no RL-trained agent and no numbers.

## Method

As far as the abstract states: 13 tasks in four ML sub-areas, five
named frontier models, evaluation against given baselines. The abstract
does not specify the scoring metric per task, the agent scaffold or
tool set the models were given, the number of runs, the compute or step
budget, or how the absence of "novel hypotheses, algorithms,
architectures" was judged (this is presumably a qualitative assessment,
but the abstract does not say). arXiv v1 only (February 2025); the
listing reports 35 pages, 12 figures, 10 tables and no journal
reference.

## Relevance to RISE

Informs the `hypothesis-generation`, `research-design`, `data-analysis`
and `code-generation` stages, consistent with the catalog's tagging.
Catalog slug: [`mlgym`](../../projects/mlgym.md). The catalog pairs it
with [`aviary`](../../projects/aviary.md) as gym-style evaluation
infrastructure: both formalize agent-environment interaction, but
MLGym's tasks are ML research problems while Aviary's scientific
environments are biology-oriented, and the catalog distinguishes MLGym
by its stated aim of training research agents via RL. The catalog entry
for [`airs-bench`](../../projects/airs-bench.md) notes that its tasks
run under MLGym scaffolding. For the ISR question of structure and
epistemic quality, the abstract describes no multi-agent aggregation
mechanism, but its headline outcome — improvement through
hyperparameter search rather than new hypotheses or architectures — is
precisely the novelty-versus-tuning distinction that a comparison of
debate, tree-search or review-loop structures would need to measure,
and a Gym interface allows such structures to be swapped while tasks
are held fixed.

## Critique / open questions

The task set is ML-only, so nothing in the abstract speaks to social
science or biomedical research (the catalog entry makes the same
point). The central finding about the absence of novel hypotheses rests
on an unspecified judgment procedure and on a single-agent evaluation
of five models; whether any agent structure changes this is untested
here. The abstract concedes no limitations beyond the finding itself.
The catalog entry records a CC BY-NC 4.0 license, an author warning to
expect major design changes, and dormant status (last push August
2025), none of which appear in the abstract.

## Key quotes

> "This is the first Gym environment for machine learning (ML) tasks,
> enabling research on reinforcement learning (RL) algorithms for
> training such agents." (abstract)

> "Solving these tasks requires real-world AI research skills such as
> generating new ideas and hypotheses, creating and processing data,
> implementing ML methods, training models, running experiments,
> analyzing the results, and iterating through this process to improve
> on a given task." (abstract)

> "We find that current frontier models can improve on the given
> baselines, usually by finding better hyperparameters, but do not
> generate novel hypotheses, algorithms, architectures, or substantial
> improvements." (abstract)
