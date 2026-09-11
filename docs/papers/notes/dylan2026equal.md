---
citekey: dylan2026equal
title: 'At Equal Inference Cost, Multi-Agent Structure Does Not Beat a Single Frozen Agent'
authors:
- 'Dylan, D.'
- 'Brennan, A.'
- 'Murphy, C.'
- 'O''Sullivan, N.'
- 'Kelly, C.'
- 'Walsh, S.'
year: 2026
venue: 'arXiv preprint (cs.MA)'
doi: ''
url: https://arxiv.org/abs/2609.04217
kind: preprint
themes:
- agentic-reasoning
- sociotechnical
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2609.04217'
---

## Summary

Fixes the total number of LLM calls and evolves a Planner-Executor-Critic team against a single evolved agent on ALFWorld and WebShop; the team's mean is higher (0.769 vs 0.754) but statistically indistinguishable while consuming 1.8x the evaluation calls, and leave-one-in analysis shows all realized value comes from the executor while planner and critic evolve to empty or low-impact prompts. This is the sharpest in-window null result on whether organizational structure pays once compute is held constant, and it is precisely the confound the ISR paper must neutralize when comparing hierarchy, polyarchy and committee. It also supplies the methodological norm - equal inference budget rather than equal environment rollouts - that makes structure-versus-structure comparisons credible.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule; organization theory applied to AI agents; MAS failure and cost analyses). Verified against: Verified via arXiv API metadata record (export.arxiv.org id_list) on 2026-09-07: full abstract, 6 authors, v1, primary cs.MA. Note: the API 'published' field reads 2026-06-25 while the identifier and the arXiv cs.MA 2026-09 monthly listing both place it in September 2026; treat the listing as authoritative and re-check the date before citing.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent LLM pipelines, such as Planner-Executor-Critic teams, often report gains over single agents, but these gains usually come with higher inference cost because the team makes multiple model calls per environment step. (abstract)

> Existing automated methods search over roles, topologies, and prompts, but typically compare teams against single agents at equal environment rollouts, giving the team extra compute. (abstract)
