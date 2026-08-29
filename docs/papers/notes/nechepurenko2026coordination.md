---
citekey: nechepurenko2026coordination
title: 'Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems'
authors:
- 'Nechepurenko, M.'
- 'Shuvalov, P.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2605.03310
kind: preprint
themes:
- agentic-reasoning
- evaluation-of-ai-research
- sociotechnical
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2605.03310'
---

## Summary

Argues coordination should be treated as a configurable architectural layer, separable from agent logic and from information access, so that architectures can be reasoned about rather than merely engineered - and instantiates this on a forecasting task with an information-controlled design: one LLM, fixed tools, fixed per-call output cap and fixed prompt template across five reference coordination configurations, with compute per question treated as an endogenous output. It separates calibration from discrimination in the Brier score so configurations leave distinguishable signatures even when aggregate scores coincide, and reports a cost-quality Pareto frontier on 100 Polymarket markets resolved after the model's training cutoff. This is the same experimental logic as the paper's, on the same kind of task, with a candid statement of its own statistical limits (pairwise tests do not survive Bonferroni at n=100) - both a precedent and a power-analysis lesson.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-08-29 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule; LLM agents in forecasting; organization theory applied to AI agents; MAS failure and cost analyses). Verified against: Opened https://arxiv.org/abs/2605.03310 (arXiv abstract page, v1 5 May 2026)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent LLM systems fail in production at rates between 41% and 87%, mostly due to coordination defects rather than base-model capability. (abstract)

> Existing responses split between cataloguing failure modes empirically and shipping declarative orchestration frameworks as engineering tools; neither delivers a principled mapping from coordination configuration to predictable failure-mode signature. (abstract)
