---
citekey: turtel2026proper
title: 'How Proper Scoring Rules Shape LLM Forecasting'
authors:
- 'Turtel, B.'
- 'Wilczewski, P.'
- 'Skotheim, K.'
- 'Satopää, V. A.'
- 'Tetlock, P. E.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2608.28482
kind: preprint
themes:
- agentic-reasoning
- evaluation-of-ai-research
- reasoning-faithfulness
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2608.28482'
---

## Summary

Relevant to the measurement side of the paper rather than to structure: five proper scoring rules used as training objectives for binary forecasts of resolved real-world events produce models that differ substantially in calibration and in how their errors are composed (systematic bias versus genuine information versus random noise), while differing only slightly in aggregate accuracy and discrimination. The Brier-trained model wins on Brier and AUC-ROC, the log-trained model on log score and calibration error, and models with similar aggregate scores get there by different routes. Useful support for the paper's central methodological move, that aggregate accuracy hides the properties one actually cares about on a forecasting task, and worth citing because Tetlock is a co-author and reviewers will expect the forecasting-evaluation literature to be engaged. Caveat: single seed per condition.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; LLM agents in forecasting; epistemic quality of LLM outputs). Verified against: Opened https://arxiv.org/abs/2608.28482 and read the full abstract, five-author list including Ville A. Satopää and Philip E. Tetlock, submission date 28 Aug 2026 16:08 UTC, primary category cs.LG.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> This paper evaluates how reward function choice shapes the performance and behavior of LLM forecasters. (abstract)

> We compare five proper scoring rules as training objectives for binary forecasts of resolved real-world events. (abstract)
