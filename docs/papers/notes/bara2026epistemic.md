---
citekey: bara2026epistemic
title: 'Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence'
authors:
- 'Bara, M.'
year: 2026
venue: 'arXiv preprint (cs.AI)'
doi: ''
url: https://arxiv.org/abs/2609.01873
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
arxiv_id: '2609.01873'
---

## Summary

States the problem as 'another agent is not another observation' and formalizes an epistemic Sybil extension as a report carrying zero conditional mutual information about the target given existing reports, proving that no report-only aggregator can generally separate replication from independent corroboration. In more than 20,000 controlled LLM-agent report and extraction calls, holding one evidence root fixed while report multiplicity rises from 1 to 32 collapses naive posterior coverage from 0.940 to 0.263, whereas raising evidence-root multiplicity to 16 closes the gap; correlated extraction errors induced by a shared base model lower the information ceiling further. For a paper measuring justification soundness and traceability this gives both the theoretical reason confidence-weighted and voting rules over-credit agreement, and a calibration-based diagnostic that tracks evidential ancestry rather than agent count.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; correlated errors / homogeneity across LLM agents; organization theory applied to AI agents; epistemic quality of LLM outputs; MAS failure and cost analyses). Verified against: Verified via arXiv API metadata record on 2026-09-07: full abstract, single author, v1, published 2026-09-01, primary cs.AI (also cs.MA), 23 pages, code and data at github.com/marcbara/epistemic-sybil-resistance.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent AI systems improve inference by spawning agents and synthesizing reports. (abstract)

> But another agent is not another observation: apparently independent reports may descend from the same evidence, and genuinely independent evidence can produce nearly identical reports. (abstract)
