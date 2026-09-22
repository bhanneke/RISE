---
citekey: he2026illusion
title: 'The Illusion of Independent Quorums: Epistemic Fault Domains and Correlated Cognitive Failures in Agentic Quorums'
authors:
- 'He, J.'
- 'Yu, D.'
year: 2026
venue: 'arXiv preprint (cs.DC)'
doi: ''
url: https://arxiv.org/abs/2609.02925
kind: preprint
themes:
- agentic-reasoning
- llm-cognition
- sociotechnical
- reasoning-faithfulness
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2609.02925'
---

## Summary

Formalizes why agent quorums that look independent are not: distinct reviewers share upstream telemetry, documents and tool backends, so many votes can collapse onto a single corrupted root cause - replication does not imply epistemic redundancy. The authors define Epistemic Fault Domains and a Structural Epistemic Cut that lower-bounds the number of root faults needed for semantic compromise, and prove that arbitrarily large quorums can retain a cut of 1 and that adding voters at a fixed threshold cannot increase credited resilience. This attacks the conditional-independence assumption on which Sah and Stiglitz's polyarchy and committee results rest, giving the ISR paper a formal criterion for when a voting aggregation rule delivers only fake redundancy.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; correlated errors / homogeneity across LLM agents; organization theory applied to AI agents; epistemic quality of LLM outputs; MAS failure and cost analyses). Verified against: Verified via arXiv API metadata record on 2026-09-07: full abstract, 2 authors, v1, published 2026-08-24, primary cs.DC (also cs.MA, cs.SE), 13 pages, code and frozen benchmark at github.com/openkedge/efd.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent quorums are widely used to authorize high-stakes infrastructure and policy mutations, yet distinct reviewers often share upstream telemetry, documents, or tool backends. (abstract)

> When upstream inputs fail, multiple votes collapse onto a single corrupted cause: replication does not imply epistemic redundancy. (abstract)
