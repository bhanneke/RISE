---
citekey: ji2026candidate
title: 'Candidate supply and answer selection shape the value of LLM judging in multi-agent systems'
authors:
- 'Ji, J.-H.'
- 'Li, S.'
- 'Cheng, J.'
- 'She, Z.'
- 'Yu, J.-T.'
- 'Yuan, Z.'
year: 2026
venue: 'arXiv preprint (cs.AI)'
doi: ''
url: https://arxiv.org/abs/2608.25937
kind: preprint
themes:
- agentic-reasoning
- sociotechnical
- reasoning-faithfulness
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2608.25937'
---

## Summary

Decomposes multi-agent reasoning into candidate generation, peer communication and terminal selection, and shows that a correct answer is frequently already present in the candidate pool while the system still converges on and reports a wrong one - consensus without quality control producing what the authors call memetic drift. Replaying 81,390 fixed candidate pools drawn from 16,278 questions, changing only the final selection rule (answer frequency combined with a judge signal) lifts accuracy from 63.82% to 70.82-70.95% by rescuing correct answers outnumbered by popular errors. This is the cleanest existing demonstration that the aggregation rule, holding generation fixed, binds output quality - the ISR paper's core claim - and the fixed-pool replay design is a directly reusable identification strategy for separating structure effects from aggregation effects.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule; aggregating LLM judgments; organization theory applied to AI agents; epistemic quality of LLM outputs). Verified against: Verified via arXiv API metadata record on 2026-09-07: full abstract, 6 authors, v2 (v1 2026-08-26, updated 2026-08-30), primary cs.AI, also cs.MA.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. (abstract)

> Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. (abstract)
