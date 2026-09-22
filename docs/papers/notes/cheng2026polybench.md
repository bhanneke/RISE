---
citekey: cheng2026polybench
title: 'PolyBench: Benchmarking LLM Forecasting and Trading Capabilities on Live Prediction Market Data'
authors:
- 'Cheng, P.'
- 'Liu, J.'
- 'Long, Y.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2604.14199
kind: preprint
themes:
- agentic-reasoning
- evaluation-of-ai-research
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2604.14199'
---

## Summary

A large timestamp-locked forecasting benchmark (38,666 Polymarket binary markets over 4,997 events, 36,165 predictions from seven frontier models) whose headline result is a calibration failure rather than an accuracy failure: only two of seven models earn positive returns while the other five lose money despite uniformly high stated confidence. That systematic overconfidence is the empirical premise behind confidence-weighted aggregation, so it belongs in the argument for why the aggregation rule cannot simply trust self-reported confidence. Secondary priority because its outcome measures are financial (confidence-weighted return, APY, Sharpe) rather than epistemic.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; LLM agents in forecasting). Verified against: Opened https://arxiv.org/abs/2604.14199 (arXiv abstract page; confirmed title, 3 authors, q-fin.CP, submitted 3 Apr 2026, full abstract read)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Predicting real-world events from live market signals demands systems that fuse qualitative news with quantitative order-book dynamics under strict temporal discipline -- a challenge existing benchmarks fail to capture. (abstract)

> We present \textbf{PolyBench}, a multimodal benchmark derived from Polymarket that records point-in-time cross-sections of 38,666 binary prediction markets spanning 4,997 events, synchronously coupling each snapshot with a Central Limit Order Book (CLOB) state and a real-time news stream. (abstract)
