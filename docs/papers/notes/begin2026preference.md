---
citekey: begin2026preference
title: 'Preference Optimization Drives Monoculture in LLM Prediction Markets'
authors:
- 'Begin, J.'
- 'Gho, B.'
- 'Muppavarapu, S.'
- 'Tsay, T.'
- 'Mohan, A.'
- 'Shaik, A.'
- 'Li, R.'
- 'Sharma, V.'
- 'Vaidheeswaran, A.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2606.26583
kind: preprint
themes:
- llm-cognition
- evaluation-of-ai-research
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2606.26583'
---

## Summary

Directly tests whether the error-independence that prediction markets rest on survives when the crowd is LLM agents, and finds it does not: DPO-tuned agents show pairwise error correlation rho = 0.70, reducing ten agents to roughly 1.4 effective independent forecasters, with N_eff flat from N=5 to N=40 and the 10-agent market (67.6%) failing to beat a single standalone agent (70.2%). Two ablations isolate preference optimization as the causal driver, replicated across labs and scales, and cross-model diversity is the strongest mitigation (rho 0.68 to 0.40). The sharpest available quantification of the correlated-error ceiling on market-based and confidence-weighted aggregation in an LLM population.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-08-29 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: correlated errors / homogeneity across LLM agents; LLM agents in forecasting; aggregating LLM judgments). Verified against: Opened https://arxiv.org/abs/2606.26583 (arXiv abstract page, v1 25 Jun 2026)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Prediction markets rest on the independence of participant errors. (abstract)

> As LLM agents become active traders on platforms like Kalshi and Polymarket, we ask: does this independence hold when the crowd is composed of LLMs? (abstract)
