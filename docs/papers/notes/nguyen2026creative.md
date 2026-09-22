---
citekey: nguyen2026creative
title: 'Creative Generation via Multi-Agent Debate: Does Debate Suppress Diversity?'
authors:
- 'Nguyen, T. A.'
- 'Nguyen, K.-B.'
- 'Do, V. D.'
- 'Venkatesh, S.'
- 'Le, H.'
year: 2026
venue: 'EMNLP 2026 (Main Conference)'
doi: ''
url: https://arxiv.org/abs/2609.00683
kind: preprint
themes:
- agentic-reasoning
- llm-cognition
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2609.00683'
---

## Summary

This is the most directly on-point paper found: it shows that multi-agent debate's convergence-driven design actively suppresses output diversity across independent runs on creative and scientific-ideation tasks, creating an inherent trade-off with exploration even while quality is preserved. The authors prove that preserving within-session agent diversity is a necessary condition for cross-run diversity, then intervene structurally, via Cognitive Lens Assignment (persistent distinct cognitive modes to counter identity drift) and Embedding-based Peer Selection (each agent sees only its most semantically distant peers, i.e. an explicit change to the communication topology to counter majority pull). Both the exploration/novelty metric and the who-talks-to-whom lever are exactly the paper's constructs, so this is a mandatory citation and the main empirical precedent to build on and distinguish from.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule; aggregating LLM judgments; correlated errors / homogeneity across LLM agents). Verified against: Opened https://arxiv.org/abs/2609.00683 and read the full abstract, five-author list, submission date 1 Sep 2026, primary category cs.CL, and the comment confirming acceptance to EMNLP 2026 Main Conference (28 pages).

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Creative generation tasks, such as narrative writing and scientific ideation, demand both high-quality outputs and distinct responses across independent runs to maximize exploration. (abstract)

> Multi-Agent Debate (MAD) has shown strong quality gains on factual and reasoning tasks, making it a natural candidate for creative generation. (abstract)
