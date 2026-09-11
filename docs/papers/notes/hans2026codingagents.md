---
citekey: hans2026codingagents
title: 'Coding-agents can replicate scientific machine learning papers'
authors:
- 'Hans, A.'
- 'Bilionis, I.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2607.02134
kind: preprint
themes:
- replication-infrastructure
- agentic-tool-use
- reasoning-faithfulness
- autonomous-research-agents
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2607.02134'
---

## Summary

Introduces 'Paper-replication', a workflow implemented as a coding-agent skill that turns each paper claim into a target with recorded evidence, provenance links and validation gates, so completion depends on workspace artefacts rather than the agent's own closing message. Twelve independent runs over four scientific ML papers all pass the gate with 158 matched targets, yet runs differ in how claims are decomposed, in numerical fidelity, in runtime and in the evidence-acceptance rules used — a concrete demonstration of non-determinism in agentic replication. Useful as a design pattern for a claim-level replication pipeline.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-08-29 literature sweep as a **medium-priority** candidate for the RISE knowledge base (angle: replication and reproducibility). Verified against: arXiv abstract page opened 2026-08-29 (title, 2 authors, submitted 2 Jul 2026, full abstract read)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Scientific machine learning papers typically make computational claims, e.g., that the relative mean square error is less than 5% or that the 95% predictive credible interval covers the test data. (abstract)

> A coding agent can be prompted to replicate those claims from paper materials alone, but the prompt does not by itself reliably preserve progress or check whether generated evidence supports the paper's claims. (abstract)
