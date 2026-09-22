---
citekey: huang2026counterfactual
title: 'Counterfactual Graph for Multi-Agent LLM Calibration'
authors:
- 'Huang, J.'
- 'Li, M.'
- 'Li, Z.'
- 'Kwon, S.'
- 'Yu, H.'
- 'Zhang, C.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2605.30653
kind: preprint
themes:
- agentic-reasoning
- llm-cognition
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2605.30653'
---

## Summary

Shows that treating agreement as evidence fails after agents communicate, because communication induces correlated failures and false consensus, so the same vote share may reflect reliable agreement under one topology but over-confidence under another. CAGE-CAL compares an observed post-communication agent graph against a matched counterfactual no-communication graph to estimate the shift in dependence and recalibrate confidence, and its calibrated confidence improves topology selection over the best fixed-topology strategy. The cleanest statement in this literature that the meaning of an aggregation statistic is conditional on the organizational structure that produced it - precisely the structure-by-rule interaction the paper's design is built to detect.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-08-29 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; correlated errors / homogeneity across LLM agents; MAS topology / structure vs. aggregation rule). Verified against: Opened https://arxiv.org/abs/2605.30653 (arXiv abstract page, v1 28 May 2026)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent LLM systems often treat agreement as evidence: when many agents in a panel give the same answer, that answer is assumed to be more reliable. (abstract)

> We show that this assumption can fail after agents communicate. (abstract)
