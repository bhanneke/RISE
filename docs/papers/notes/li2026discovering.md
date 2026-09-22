---
citekey: li2026discovering
title: 'Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference'
authors:
- 'Li, J.'
- 'He, P.'
- 'Ji, Q.'
- 'Wang, W.'
- 'Liu, L.'
- 'Sun, C.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2608.12921
kind: preprint
themes:
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2608.12921'
---

## Summary

Attacks the black-box character of existing topology-generation work: because current methods optimize communication graphs purely against task-level reward, they cannot say why particular edges are selected. E2-Explainer recasts topology explanation as causal attribution, using a Granger-style objective that masks each communication channel and measures the change in task outcome and in the stability of the final response, then distills budgeted critical subgraphs into an amortized explainer that can also be executed to prune redundant edges. Relevant to the paper's traceability dimension and as prior art for edge-level causal attribution, which is the natural robustness check on any claim that a specific structural feature produced the epistemic gain.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule). Verified against: Opened https://arxiv.org/abs/2608.12921 and read the full abstract, six-author list, submission date 13 Aug 2026 (v2 14 Aug), primary category cs.MA. Before the Aug 25 window boundary; included as directly on-angle prior art.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> The performance of large language model (LLM)-based multi-agent systems (MAS) largely depends on effective communication topologies. (abstract)

> Existing topology generation methods, however, typically learn communication topologies through black-box optimization driven solely by task-level rewards. (abstract)
