---
citekey: jin2026remember
title: 'Remember and Reweight: Enhancing Multi-Agent Debate with Experience Memory and Confidence Estimation'
authors:
- 'Jin, X.'
- 'Ma, Z.'
- 'Zeng, Y.'
- 'Cui, X.'
- 'Zhang, H.'
- 'Wang, J.'
year: 2026
venue: 'Findings of EMNLP 2026'
doi: ''
url: https://arxiv.org/abs/2609.03619
kind: preprint
themes:
- agentic-reasoning
- llm-cognition
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2609.03619'
---

## Summary

Names and attacks the 'shared misconception' failure mode: when a majority of agents initially converge on an incorrect answer, debate amplifies rather than corrects the error, and the authors argue prior work fixes peer skew while leaving agents' correlated concept priors untouched. Their remedy is a confidence-weighted aggregation rule in which retrieved debate history calibrates the prior and yields per-agent reliability weights that modulate peer influence. Directly relevant as a recent instance of the confidence-weighting cell in the paper's aggregation-rule design space, and as evidence that correlated priors, not just topology, drive consensus failure.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; correlated errors / homogeneity across LLM agents). Verified against: Opened https://arxiv.org/abs/2609.03619 and read the full abstract, six-author list, submission date 3 Sep 2026, primary category cs.CL, comment confirming EMNLP 2026 Findings (24 pages).

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent debate (MAD) improves the reasoning capabilities of large language models by having multiple agents iteratively refine their responses through discussion. (abstract)

> However, MAD suffers from a critical vulnerability known as shared misconception: when a majority of agents initially converge on an incorrect answer, the debate process tends to amplify rather than correct the error. (abstract)
