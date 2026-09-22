---
citekey: li2026diverse
title: 'Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry'
authors:
- 'Li, Y.'
- 'Tao, Y.'
- 'Zhang, K.'
- 'Wang, T.'
- 'Gu, G.'
- 'Zhou, Y.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2607.01661
kind: preprint
themes:
- agentic-reasoning
- llm-cognition
- evaluation-of-ai-research
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2607.01661'
---

## Summary

The closest prior work on the paper's own empirical terrain: multi-agent LLM deliberation on binary forecasting questions drawn from real prediction markets (PolyGym, 375 questions), scored by Brier score and accuracy. It shows that when all agents receive identical evidence deliberation collapses into herding and multi-agent barely beats a single agent, then proves that partitioning evidence into shared-public and disjoint-private subsets reduces inter-agent error correlation, instantiating this with relevance-aware routing and confidence-weighted aggregation for 12-18% Brier improvement. It establishes information asymmetry as a competing explanation for multi-agent gains that the design must hold constant or measure, otherwise structure effects are confounded with evidence allocation.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; correlated errors / homogeneity across LLM agents; LLM agents in forecasting). Verified against: Opened https://arxiv.org/abs/2607.01661 (arXiv abstract page; confirmed title, 6 authors, cs.AI, v1 2 Jul 2026, full abstract read)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent systems are increasingly used for forecasting future events, as deliberation among multiple LLMs is believed to improve reasoning and calibration. (abstract)

> Yet existing approaches overlook a critical design choice: what information each agent receives. (abstract)
