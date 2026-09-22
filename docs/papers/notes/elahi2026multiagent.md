---
citekey: elahi2026multiagent
title: 'Multiagent Protocols with Aggregated Confidence Signals'
authors:
- 'Elahi, A.'
- 'Di Eugenio, B.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2606.13591
kind: preprint
themes:
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2606.13591'
---

## Summary

Notes that no existing method produces or evaluates a confidence for the output of a multi-agent system as a whole - prior work uses confidence only within debate, to weight messages, trigger debate, or calibrate individual agents. It introduces three protocols that first transform raw confidence signals to make them comparable across models and then combine them by soft voting or a probability fusion the authors call Bayesian fusion, yielding aggregated confidence substantially more discriminative than the best single agent or standard debate baselines while correctness stays stable. A concrete, implementable specification for the confidence-weighted arm of the paper's aggregation factor.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-08-29 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments). Verified against: Opened https://arxiv.org/abs/2606.13591 (arXiv abstract page, v1 11 Jun 2026)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Confidence is used for reliability, oversight, and a range of downstream decision tasks in Natural Language Processing (NLP), yet no existing method produces or evaluates a confidence for the output of a multiagent system. (abstract)

> Prior work uses confidence within multiagent debate (MAD) to weight messages, trigger debate, or calibrate individual agents, but it never aggregates these into a single confidence for the system itself. (abstract)
