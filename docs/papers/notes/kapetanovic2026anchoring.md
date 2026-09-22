---
citekey: kapetanovic2026anchoring
title: 'Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence'
authors:
- 'Kapetanovic, A.'
- 'Altwlkany, K.'
- 'Mercep, A.'
- 'Duricic, T.'
- 'Lacic, E.'
year: 2026
venue: 'Proceedings of the 35th ACM International Conference on Information and Knowledge Management (CIKM ''26)'
doi: ''
url: https://arxiv.org/abs/2608.25869
kind: preprint
themes:
- agentic-reasoning
- llm-cognition
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2608.25869'
---

## Summary

Directly falsifies the independence assumption that any voting or averaging aggregation rule rests on, in the specific case where agents see each other's prior scores. Across 192,000 attempted evaluations (185,271 successful), seven of eight models show anchored-metadata effects with bootstrap intervals below zero, Cohen's d up to 0.71, and on categorical industry data with human ground truth the anchoring blocks 48 percent of error corrections and flips 10.18 percent of correct judgments to a wrong assigned label. Neither chain-of-thought nor an explicit disregard-the-metadata warning removes the effect. For the paper this is the mechanism-level evidence that the information an agent is allowed to see, i.e. the communication structure, contaminates the aggregation stage and cannot be fixed by prompting.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; correlated errors / homogeneity across LLM agents). Verified against: Opened https://arxiv.org/abs/2608.25869 and read the full abstract, five-author list, submission date 26 Aug 2026, primary category cs.CL, and the comment confirming publication in CIKM '26 proceedings.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Large language models (LLMs) increasingly assess generated content, giving rise to the LLM-as-a-Judge paradigm. (abstract)

> These systems now score outputs, filter content, and gate iterative refinement in production pipelines, where each judgment is often assumed to be independent of earlier evaluations. (abstract)
