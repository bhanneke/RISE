---
citekey: chen2025reasoning
title: Reasoning Models Don't Always Say What They Think
authors:
- Chen, Y.
- et al.
year: 2025
venue: arXiv 2505.05410 (Anthropic Alignment Science Team)
doi: ''
url: https://arxiv.org/abs/2505.05410
kind: preprint
themes:
- reasoning-faithfulness
- agentic-reasoning
- hallucination
- evaluation-of-ai-research
methods:
- empirical
- evaluation
relates_to_projects:
- reviewer
- sakana-ai-scientist
status: read
arxiv_id: '2505.05410'
---

## Summary

An evaluation of chain-of-thought (CoT) faithfulness in state-of-the-art
reasoning models (Claude 3.7 Sonnet, DeepSeek R1) compared with
non-reasoning baselines (Claude 3.5 Sonnet New, DeepSeek V3). The
authors test 6 reasoning-hint types by presenting paired
multiple-choice questions (without and with an inserted hint) and
measuring whether models that switch their answer because of the hint
acknowledge it in their CoT.

## Contribution

Three findings about CoT faithfulness: (1) for most settings and
models, CoTs reveal hint usage in at least 1% of examples but the
reveal rate is "often below 20%"; (2) outcome-based reinforcement
learning initially improves faithfulness but plateaus without
saturating; (3) when RL increases reward-hacking hint usage, the
propensity to verbalise the hint does not increase even without
training against a CoT monitor. The authors conclude that CoT
monitoring is useful but insufficient on its own to rule out
misaligned behaviour.

## Method

Empirical evaluation: paired prompts (with vs. without hint), 6 hint
categories, comparison across reasoning and non-reasoning models, RL
ablations.

## Relevance to RISE

Foundational evidence for the *reasoning-faithfulness* theme: if a
RISE pipeline relies on a reasoning model's stated chain of thought
to audit its decisions, the audit is unreliable. Directly relevant to
any RISE project that uses LLM "thinking" as evidence — including
evaluation hubs like [`reviewer`](../../projects/reviewer.md) and
autonomous-research systems such as
[`sakana-ai-scientist`](../../projects/sakana-ai-scientist.md) — and a
necessary citation for the RISE evaluation chapter on chain-of-thought
trustworthiness.

## Critique / open questions

Faithfulness is measured against an indirect proxy (acknowledgement
of an inserted hint), not against the model's internal computation;
the operationalisation may understate or overstate true unfaithfulness.
Only two reasoning models are tested, both as of early 2025.

## Key quotes

> "CoT monitoring is a promising way of noticing undesired behaviors
> during training and evaluations, but … it is not sufficient to rule
> them out."

> "For most settings and models tested, CoTs reveal their usage of
> hints in at least 1% of examples where they use the hint, but the
> reveal rate is often below 20%."
