---
citekey: wang2026naturebench
title: 'NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?'
authors:
- Wang, Y.
- Cheng, L.
- Zuo, Y.
- Zeng, S.
- He, B.
- Jiang, C.
- Yang, J.
- Wang, Y.
- Zhao, K.
- Huang, W.
- et al.
year: 2026
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2606.24530
kind: preprint
themes:
- evaluation-of-ai-research
- replication-infrastructure
- autonomous-research-agents
methods:
- benchmark-design
- benchmark-evaluation
- failure-analysis
relates_to_projects:
- naturebench
status: skimmed
arxiv_id: '2606.24530'
---

## Summary

NatureBench is a cross-discipline benchmark of 90 tasks distilled from
peer-reviewed Nature-family papers, built to test whether AI coding
agents can go beyond reproducing a published result toward discovery on
real scientific problems. It rests on NatureGym, an automated pipeline
that constructs a standardized, containerized environment per task from
the source paper, which the authors present as a fix for the
environment-fragmentation problem of earlier agent-on-research
benchmarks. Ten frontier agent configurations are evaluated with web
search disabled; the strongest surpasses the published SOTA on only
17.8% of tasks under a "g>0.1" criterion. A method-pathway analysis
finds that successes come mainly from methodological translation —
recasting the scientific task as a familiar supervised prediction
problem — rather than scientific invention, and that failures stem from
wrong method choice and insufficient compute rather than
misunderstanding the task. Benchmark, pipeline and a leaderboard with
maintainer-side reproduction are released.

## Contribution

Claimed: a SOTA-anchored, cross-discipline benchmark; an automated
task-construction pipeline; a diagnostic distinction between
translation and invention. What the abstract supports: the 17.8%
headline for one criterion and the qualitative pathway and failure
findings. "Discovery" is operationalized as beating the source paper's
reported metric, which is a narrower notion than the abstract's framing
suggests. The claim that NatureGym restores "credibility" to
agent-on-research benchmarks is an argument, not a measured result.

## Method

As far as the abstract states: 90 tasks from Nature-family papers,
per-task containerized environments built automatically from the source
paper, ten frontier agent configurations, a web-search-disabled
protocol, a surpass-SOTA criterion of g>0.1, and a qualitative analysis
of method pathways and failure causes. The abstract does not define g,
name the models or harnesses, state the compute budget, describe how
SOTA is extracted from each paper, explain how method pathways were
classified, or list the disciplines. The arXiv v2 comment (July 2026)
says results for GLM-5.2 and MinMax-M3 were added; the catalog entry
speaks of twelve harness-model configurations, whereas the abstract
still says ten.

## Relevance to RISE

Informs the `data-analysis` and `code-generation` stages (the catalog's
tags) and, because every task starts from a published paper's data and
metric, the `replication` stage as a baseline that agents must exceed.
Catalog slug: [`naturebench`](../../projects/naturebench.md). It shares
the SOTA-anchoring design with
[`airs-bench`](../../projects/airs-bench.md) but extends the source
pool from ML papers to peer-reviewed natural-science publications; the
catalog also groups it with [`asta-bench`](../../projects/asta-bench.md),
[`mlgym`](../../projects/mlgym.md) and
[`lifescibench`](../../projects/lifescibench.md). For the ISR question
of structure and epistemic quality, the abstract describes no debate,
tournament or review mechanism, but its "translation versus invention"
pathway analysis and its finding that wrong method choice dominates
failures offer an outcome measure that is more informative than a pass
rate: a comparison of aggregation structures could ask whether tree
search or adversarial critique shifts agents from translation toward
invention, or merely raises the surpass rate.

## Critique / open questions

From the abstract one cannot assess how sensitive the 17.8% figure is
to the g threshold, which ten configurations were run, or how
reproducible the pathway classification is. Disabling web search does
not address pretraining contamination, since the source papers are
public; the catalog entry raises this, the abstract does not. Listing
"insufficient compute budget" as a dominant failure cause implies
results are budget-dependent, but the budget is not stated. The
abstract acknowledges no limitations of the benchmark itself. The
catalog entry notes heterogeneous per-task data licenses and A100-class
GPU requirements for some tasks.

## Key quotes

> "We introduce NatureBench, a cross-discipline benchmark of 90 tasks
> distilled from peer-reviewed Nature-family publications, designed to
> evaluate whether AI coding agents can move beyond reproduction toward
> discovery on real scientific problems." (abstract)

> "Evaluating ten frontier agent configurations under a strict
> web-search-disabled protocol, we find that the strongest model
> surpasses SOTA on only 17.8% of tasks under the g>0.1 criterion."
> (abstract)

> "Analysis of method pathways reveals that agents succeed primarily
> through methodological translation, converting scientific tasks into
> familiar supervised prediction problems, rather than through genuine
> scientific invention." (abstract)
