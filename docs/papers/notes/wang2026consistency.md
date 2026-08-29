---
citekey: wang2026consistency
title: 'The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment'
authors:
- 'Wang, X.'
- 'Yang, C. C.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2606.08457
kind: preprint
themes:
- reasoning-faithfulness
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2606.08457'
---

## Summary

Introduces CARA (Cross-Agent Reasoning Alignment), automated metrics for whether agents who agree on an answer also agree on the reasoning, and identifies the consistency illusion: debate reduces detectable contradictions between agents while simultaneously decreasing the semantic similarity of their reasoning chains, so agents appear to agree more but reason less consistently. Their Grounded Debate Protocol, requiring agents to commit to named facts and take explicit stances on others' claims, improves alignment with Cohen's d of +1.43 to +1.99 without extra LLM calls. A directly borrowable operationalisation of epistemic quality orthogonal to accuracy, and its call to audit reasoning alignment alongside accuracy is this paper's thesis in miniature.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-08-29 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: epistemic quality of LLM outputs; aggregating LLM judgments). Verified against: Opened https://arxiv.org/abs/2606.08457 (arXiv abstract page, v1 7 Jun 2026)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent LLM systems for medical question answering often treat consensus as a reliability signal: if multiple agents agree on an answer, it is presumed trustworthy. (abstract)

> However, answer-level consensus does not entail reasoning-level alignment. (abstract)
