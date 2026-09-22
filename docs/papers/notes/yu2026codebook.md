---
citekey: yu2026codebook
title: 'Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems'
authors:
- 'Yu, J.'
- 'Li, Y.'
- 'Jiang, E. H.'
- 'Zhang, Z.'
- 'Liu, D.'
- 'Zhao, W.'
- 'Li, L.'
- 'Chang, K.-W.'
- 'Wu, Y. N.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2609.02264
kind: preprint
themes:
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2609.02264'
---

## Summary

The current state of the art in automated topology search, and useful to the paper for two negative findings rather than its method: topologies that survive a reward filter collapse to roughly six distinct graphs even as codebook capacity grows from 8 to 64, and edge count is negatively correlated with measured token consumption so sparsifying a graph makes inference more expensive. It also notes that message-passing scorers over agent-profile nodes are adjacency-invariant when agents share a profile, the default in published benchmarks, meaning existing topology-search literature largely cannot separate structure from role heterogeneity. That is a direct argument for the paper's deliberate crossing of structure with aggregation rule instead of black-box search.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule). Verified against: Opened https://arxiv.org/abs/2609.02264 and read the full abstract including the six-graph collapse and Pearson r about -0.4 findings; arXiv API confirms nine authors, published 2026-09-02, cs.AI.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Adapting the communication topology of an LLM multi-agent system to each query improves both accuracy and efficiency, yet current designers treat this as conditional graph generation: a variational, autoregressive, or diffusion decoder searches the $N \times N$ adjacency space, and a graph-network proxy trained on utility and a structural cost such as edge count ranks the sampled candidates. (abstract)

> We argue that this formulation is misaligned with the problem. (abstract)
