---
citekey: patel2026representational
title: 'Representational Collapse in Multi-Agent LLM Committees: Measurement and Diversity-Aware Consensus'
authors:
- 'Patel, D.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2604.03809
kind: preprint
themes:
- llm-cognition
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2604.03809'
---

## Summary

Takes the committee structure directly - replicated models under different role prompts aggregating by majority vote - and shows the assumed complementarity of agent contributions does not hold. Embedding chain-of-thought rationales gives mean pairwise cosine similarity of 0.888 and effective rank 2.17 out of 3.0 across 100 GSM8K questions with three agents, which the author terms representational collapse; collapse intensifies on harder tasks. Their DALC consensus method reweights by diversity from embedding geometry, beating self-consistency (87% vs 84%) at 26% lower token cost. Supplies a concrete, cheap measurement of within-committee homogeneity that the paper could adopt as a manipulation check on its structure factor.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-08-29 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: correlated errors / homogeneity across LLM agents; MAS topology / structure vs. aggregation rule; aggregating LLM judgments). Verified against: Opened https://arxiv.org/abs/2604.03809 (arXiv abstract page, v1 4 Apr 2026)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent LLM committees replicate the same model under different role prompts and aggregate outputs by majority vote, implicitly assuming that agents contribute complementary evidence. (abstract)

> We embed each agent's chain-of-thought rationale and measure pairwise similarity: across 100 GSM8K questions with three Qwen2.5-14B agents, mean cosine similarity is 0.888 and effective rank is 2.17 out of 3.0, a failure mode we term representational collapse. (abstract)
