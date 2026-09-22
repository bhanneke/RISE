---
citekey: zhu2026demystifying
title: 'Demystifying Multi-Agent Debate: The Role of Confidence and Diversity'
authors:
- 'Zhu, X.'
- 'Zhang, C.'
- 'Chi, Y.'
- 'Stafford, T.'
- 'Collier, N.'
- 'Vlachos, A.'
year: 2026
venue: 'arXiv preprint (v3 3 Jun 2026)'
doi: ''
url: https://arxiv.org/abs/2601.19921
kind: preprint
themes:
- agentic-reasoning
- llm-cognition
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2601.19921'
---

## Summary

Gives the formal reason debate as an aggregation rule is not automatically better than voting: under homogeneous agents and uniform belief updates, debate preserves expected correctness and so cannot reliably improve on majority vote. It then isolates the two mechanisms that make debate work - diversity of initial viewpoints and calibrated confidence communication - with theory plus experiments on six reasoning QA benchmarks, and explicitly connects the human deliberation literature to LLM debate. This is the cleanest citation for treating aggregation rule as a design dimension separate from structure, and it supplies the confidence-weighting condition directly.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; correlated errors / homogeneity across LLM agents). Verified against: Opened https://arxiv.org/abs/2601.19921 (arXiv abstract page; confirmed title, 6 authors, cs.CL, v1 9 Jan 2026 / v2 1 Jun 2026 / v3 3 Jun 2026, full abstract read)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent debate (MAD) is widely used to improve large language model (LLM) performance through test-time scaling, yet recent work shows that vanilla MAD often underperforms simple majority vote despite higher computational cost. (abstract)

> Studies show that, under homogeneous agents and uniform belief updates, debate preserves expected correctness and therefore cannot reliably improve outcomes. (abstract)
