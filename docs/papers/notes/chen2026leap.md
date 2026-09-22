---
citekey: chen2026leap
title: 'LEAP: Likelihood Elicitation and Aggregation for LLM-based Probabilistic Forecasting'
authors:
- 'Chen, Y.'
- 'Zhao, Y.'
- 'Xu, X.'
- 'Xie, Q.'
- 'Wu, J.'
- 'Liu, Z.'
year: 2026
venue: 'EMNLP 2026 (accepted); arXiv preprint cs.AI'
doi: ''
url: https://arxiv.org/abs/2609.01337
kind: preprint
themes:
- agentic-reasoning
- evaluation-of-ai-research
- reasoning-faithfulness
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2609.01337'
---

## Summary

Names and attacks 'Monolithic Prediction' - the standard design in which one LLM reads all collected evidence together and emits the forecast - on the grounds that it obscures how individual evidence items affect the result and collapses uncertainty across competing outcomes. LEAP instead examines each evidence item separately, elicits likelihood parameters, and combines them with an explicit prior through a deterministic probabilistic model, improving most prediction and calibration metrics under controlled comparisons of prior access, inference budget and aggregation. This is the ISR thesis stated within a single agent: changing only where and how evidence is aggregated changes forecast quality, and the decomposition is justified explicitly as preserving reproducible evidence contributions - traceability - which makes it both the closest methodological sibling and a necessary baseline.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule; aggregating LLM judgments; LLM agents in forecasting; epistemic quality of LLM outputs). Verified against: Verified by opening https://arxiv.org/abs/2609.01337 on 2026-09-07: full abstract read verbatim, 6 authors, submitted 1 September 2026, cs.AI, accepted to EMNLP 2026, 20 pages, 3 figures, 15 tables.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> LLM-based forecasting systems have improved on real-world tasks such as financial markets and sports outcomes, largely through stronger search and tool use. (abstract)

> Many systems still ask an LLM to read all collected evidence together and produce the final forecast. (abstract)
