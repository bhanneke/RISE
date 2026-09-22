---
citekey: tongyi2025deepresearch
title: Tongyi DeepResearch Technical Report
authors:
- Tongyi DeepResearch Team
- Li, B.
- Zhang, B.
- Zhang, D.
- Huang, F.
- Li, G.
- Chen, G.
- Yin, H.
- Wu, J.
- Zhou, J.
- et al.
year: 2025
venue: arXiv preprint (Alibaba)
doi: ''
url: https://arxiv.org/abs/2510.24701
kind: preprint
themes:
- agentic-reasoning
- agentic-tool-use
methods:
- system-design
- model-training
- benchmark-evaluation
relates_to_projects:
- tongyi-deepresearch
status: skimmed
arxiv_id: '2510.24701'
---

## Summary

Technical report for Tongyi DeepResearch, an agentic large language
model from Alibaba built for long-horizon, deep information-seeking
research tasks. Instead of prompting a general model into an agent
loop, the team trains agency into the model end-to-end through
"agentic mid-training" followed by "agentic post-training". All
training stages are fed by a fully automatic data-synthesis pipeline
that needs no human annotation, and each stage runs in its own
customized environment. The released model has 30.5 billion total
parameters of which 3.3 billion are activated per token. The abstract
claims state-of-the-art results on Humanity's Last Exam, BrowseComp,
BrowseComp-ZH, WebWalkerQA, xbench-DeepSearch, FRAMES and
xbench-DeepSearch-2510, and the model, framework and "complete
solutions" are open-sourced. The arXiv record has three versions (v1
Oct 2025, v3 May 2026).

## Contribution

Claimed: a complete training recipe (mid-training plus post-training),
a scalable synthetic-data pipeline, per-stage environments, and
state-of-the-art performance on seven agentic deep-research
benchmarks, delivered as open weights. What the abstract actually
supports: that the recipe exists and that benchmark results are
reported. The abstract gives no scores, baselines or ablations, so
the contribution of any single component (mid-training vs.
post-training vs. data synthesis) cannot be isolated from it, and
"state-of-the-art" is relative to an unspecified comparison set at
the time of each version.

## Method

Model training plus benchmark evaluation. The abstract states the two
training phases, the automatic data-synthesis pipeline, the
per-stage environments, the parameter counts and the benchmark
names. It does not specify the RL or optimisation algorithm, the size
or provenance of the synthetic data, the tools in the environment
(search, browse, code), inference modes, compute, or any numbers. The
catalog entry records ReAct and "Heavy" (IterResearch) inference modes
and GRPO-based RL; those details come from the project page and
technical blog, not from the abstract.

## Relevance to RISE

Informs the rq-formulation, literature-discovery and
literature-synthesis stages, matching the catalog entry
`tongyi-deepresearch`, which files it in the literature/synthesis
block with lifecycle coverage 1: it is a research-capable model, not
a paper-producing pipeline. The closest catalog neighbour with an
abstract in this KB is `deepresearcher`
([zheng2025deepresearcher](../../projects/deepresearcher.md)): both
train deep-research agents end-to-end with reinforcement learning
against real web environments; Tongyi DeepResearch adds an explicit
agentic mid-training phase and a fully automatic data-synthesis
pipeline and ships the weights. For the ISR question of how
multi-agent structure shapes epistemic quality, the abstract
describes a single trained agent and no multi-agent review, debate or
aggregation mechanism, so any quality control is located in training
rather than in structural aggregation; it is therefore a natural
single-agent reference point against which structured designs can be
contrasted.

## Critique / open questions

Nothing in the abstract allows assessment of benchmark scores,
contamination controls for the synthetic training data, or whether a
"fully automatic" data pipeline reinforces its own errors. Faithfulness
and citation accuracy of the produced research reports are not
mentioned. Applicability to scholarly literature search (as opposed to
open-web question answering) is not addressed. The abstract concedes
no limitations. Corporate authorship (a team name plus 56 named
authors) complicates attribution. The catalog entry notes that outputs
depend on live web state and are not bitwise reproducible.

## Key quotes

> "We present Tongyi DeepResearch, an agentic large language model,
> which is specifically designed for long-horizon, deep
> information-seeking research tasks." (abstract)

> "We design a highly scalable data synthesis pipeline that is fully
> automatic, without relying on costly human annotation, and empowers
> all training stages." (abstract)

> "Tongyi DeepResearch, featuring 30.5 billion total parameters, with
> only 3.3 billion activated per token, achieves state-of-the-art
> performance across a range of agentic deep research benchmarks,
> including Humanity's Last Exam, BrowseComp, BrowseComp-ZH,
> WebWalkerQA, xbench-DeepSearch, FRAMES and xbench-DeepSearch-2510."
> (abstract)
