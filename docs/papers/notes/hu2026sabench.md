---
citekey: hu2026sabench
title: 'SA-Bench: Evaluating Semantic Alignment in LLM-Based Paper Reproduction'
authors:
- 'Hu, X.'
- 'Pan, Z.'
- 'Su, Z.'
- 'Liu, Z.'
- 'Zhang, W.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2608.24252
kind: preprint
themes:
- replication-infrastructure
- evaluation-of-ai-research
- autonomous-research-agents
- reasoning-faithfulness
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2608.24252'
---

## Summary

Names and measures 'semantic drift': paper-reproduction code that runs but silently diverges from the paper's specification. Decomposes 30 ICLR/ICML/NeurIPS 2025 papers into 1,491 atomic Semantic Alignment Units across numerical, methodological, protocol and ordering drift, then scores 12 generator configurations; the best (Claude + PaperCoder) reaches only 0.301 of 1.0, and the failure taxonomy shows agents attempt most requirements but implement them wrongly, with mismatches and stubs dominating zero scores. The key finding for replication agents is that scaffolds optimised for executability buy almost nothing for scientific faithfulness.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the RISE knowledge base (angle: replication and reproducibility). Verified against: Opened https://arxiv.org/abs/2608.24252, read full abstract, 5 authors, 2026-08-25, cs.AI/cs.SE. Dedupe: no 'sa-bench' or 'semantic alignment' match.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> LLM agents can generate paper reproduction code, yet often produce scientifically unfaithful implementations. (abstract)

> We define this failure mode as semantic drift, where generated code silently diverges from the paper's specifications. (abstract)
