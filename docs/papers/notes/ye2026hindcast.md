---
citekey: ye2026hindcast
title: 'Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters'
authors:
- 'Ye, X.'
- 'Dineen, J.'
- 'Zhu, E.'
- 'Lu, S.'
- 'Song, K.'
- 'Zhou, B.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2607.14051
kind: preprint
themes:
- evaluation-of-ai-research
- reasoning-faithfulness
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2607.14051'
---

## Summary

Names the validity threat that any research-forecasting evaluation has to answer for: answer leakage through two channels, retrieval of post-event reports and training on temporally proximate data, which inflates backtested forecasting skill. Its remedy is a protocol that grades the model as if it stood at a chosen past date, using resolved Polymarket markets with model access restricted to pre-cutoff archived Reddit posts, benchmarked against both realised outcomes and historical market prices. This is the cleanest citation for the temporal-cutoff discipline the paper's task design needs, and its finding that retrieval helps only where substantive prior discussion existed (and hurts where archives were mostly speculation) is relevant to how evidence access is held constant across structures.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: LLM agents in forecasting; epistemic quality of LLM outputs). Verified against: Opened https://arxiv.org/abs/2607.14051 (arXiv abstract page; confirmed title, 6 authors, cs.CL, submitted 15 Jul 2026, abstract read)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Forecasters are evaluated by backtesting, which replays resolved questions and grades the probability the system would have assigned before the outcome was known. (abstract)

> For LLMs, two channels leak the answer into this test. (abstract)
