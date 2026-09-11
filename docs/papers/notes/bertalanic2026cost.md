---
citekey: bertalanic2026cost
title: 'The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate'
authors:
- 'Bertalanič, B.'
- 'Fortuna, C.'
year: 2026
venue: 'ACM Conference on AI and Agentic Systems'
doi: '10.1145/3786335.3813137'
url: https://arxiv.org/abs/2605.00914
kind: paper
themes:
- llm-cognition
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2605.00914'
---

## Summary

A controlled study of N=10 homogeneous agents over R=3 rounds comparing peer debate against isolated self-correction plus a stochastic noise control - the independent-versus-deliberative contrast with a placebo arm. It decomposes debate failure into three named pathways: sycophantic conformity (modal adoption up to 85.5%), contextual fragility (peer rationales destabilise previously correct reasoning, up to 70.0%), and consensus collapse (plurality voting discards correct answers already present in the generation pool, oracle gap up to 32.3 percentage points). Ablations over communication density and temperature show conformity reaches high levels at minimal peer exposure and intensifies with greater initial diversity, and debate consumes 2.1-3.4x more tokens for equal or lower accuracy. Gives the paper both a mechanism vocabulary and a cost baseline.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-08-29 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: correlated errors / homogeneity across LLM agents; MAS failure and cost analyses; aggregating LLM judgments; MAS topology / structure vs. aggregation rule). Verified against: Opened https://arxiv.org/abs/2605.00914 (arXiv abstract page, v1 29 Apr 2026; related DOI 10.1145/3786335.3813137)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent debate, where teams of LLMs iteratively exchange rationales and vote on answers, is widely deployed under the assumption that peer review filters hallucinations. (abstract)

> Yet the failure dynamics of homogeneous debate remain poorly understood, therefore we report findings from a controlled empirical study of teams of $N{=}10$ homogeneous agents (Qwen2.5-7B, Llama-3.1-8B, Ministral-3-8B) across $R{=}3$ debate rounds on two high-difficulty benchmarks (GSM-Hard and MMLU-Hard). (abstract)
