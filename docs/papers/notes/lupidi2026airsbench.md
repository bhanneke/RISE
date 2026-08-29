---
citekey: lupidi2026airsbench
title: 'AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents'
authors:
- Lupidi, A.
- Gauri, B.
- Foster, T. S.
- Al Omari, B.
- Magka, D.
- Pepe, A.
- Audran-Reiss, A.
- Aghamelu, M.
- Baldwin, N.
- Cipolina-Kun, L.
- et al.
year: 2026
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2602.06855
kind: preprint
themes:
- evaluation-of-ai-research
- autonomous-research-agents
methods:
- benchmark-design
- benchmark-evaluation
relates_to_projects:
- airs-bench
status: skimmed
arxiv_id: '2602.06855'
---

## Summary

AIRS-Bench (AI Research Science Benchmark) is a Meta FAIR suite of 20
tasks sourced from state-of-the-art machine learning papers, spanning
language modeling, mathematics, bioinformatics and time-series
forecasting. Each task is meant to exercise agentic capabilities over
the research lifecycle — idea generation, experiment analysis and
iterative refinement — and no baseline code is provided. The task
format is designed so that new tasks can be added and different agentic
frameworks compared. The authors establish baselines with frontier
models under both sequential and parallel scaffolds. Agents exceed
human SOTA on four tasks and fail to match it on the other sixteen;
even where they surpass the human benchmark they stay below the
theoretical performance ceiling of the task. Task definitions and
evaluation code are open-sourced.

## Contribution

Claimed: a lifecycle-spanning, unsaturated benchmark anchored to
published human SOTA, with a versatile task format and baseline results
across scaffolds. What the abstract supports: the 4-of-20 result and
the ceiling observation. "Full research lifecycle" is, per the abstract
itself, limited to idea generation, experiment analysis and refinement
on ML tasks; literature work, writing and review are not mentioned. The
claim that the format enables "rigorous comparison across different
agentic frameworks" is a design statement, not something the abstract
demonstrates.

## Method

As far as the abstract states: 20 tasks from SOTA ML papers, four
named domains, no baseline code, frontier models paired with sequential
and parallel scaffolds, comparison against human SOTA and against a
theoretical ceiling. The abstract does not specify which models were
used, how many runs or seeds, the scoring or normalization formula, how
the theoretical ceiling is defined, which four tasks were exceeded, the
compute budget per task, or whether sequential or parallel scaffolds
performed better. The arXiv listing (v3, February 2026) reports 49
pages, 14 figures and 10 tables; no journal reference.

## Relevance to RISE

Informs the `hypothesis-generation`, `research-design`, `data-analysis`
and `code-generation` stages, matching the catalog's tagging. Catalog
slug: [`airs-bench`](../../projects/airs-bench.md). Together with
[`naturebench`](../../projects/naturebench.md) it forms a
SOTA-anchored benchmark family: both score agents against the published
result of a source paper, but AIRS-Bench draws 20 tasks from ML papers
while NatureBench draws 90 from Nature-family papers across
disciplines. The catalog entry notes that AIRS-Bench tasks can run
under the [`mlgym`](../../projects/mlgym.md) scaffolding, and groups it
with [`asta-bench`](../../projects/asta-bench.md) as evaluation
infrastructure. For the ISR question of structure and epistemic
quality, the one structural variable the abstract reports is the
contrast between sequential and parallel scaffolds — a coarse
manipulation of agent organization whose effect is measured against a
human SOTA anchor — though the abstract does not say which scaffold won.

## Critique / open questions

From the abstract one cannot assess how tasks were selected, whether
the source papers' public availability creates contamination, what
"match" means numerically, how agent stochasticity was handled, or the
sensitivity of the 4/16 split to the compute budget. The abstract does
not discuss limitations of the benchmark; it frames non-saturation as a
feature. The catalog entry records a CC BY-NC 4.0 license and notes
that SOTA anchors are snapshots that drift as human results improve;
neither point appears in the abstract.

## Key quotes

> "AIRS-Bench tasks assess agentic capabilities over the full research
> lifecycle -- including idea generation, experiment analysis and
> iterative refinement -- without providing baseline code." (abstract)

> "We establish baselines using frontier models paired with both
> sequential and parallel scaffolds. Our results show that agents exceed
> human SOTA in four tasks but fail to match it in sixteen others."
> (abstract)

> "Even when agents surpass human benchmarks, they do not reach the
> theoretical performance ceiling for the underlying tasks." (abstract)
