---
citekey: laban2026llmscorrupt
title: 'LLMs Corrupt Your Documents When You Delegate'
authors:
  - 'Laban, P.'
  - 'Schnabel, T.'
  - 'Neville, J.'
year: 2026
venue: 'arXiv 2604.15597 (Microsoft Research preprint)'
doi: ""
url: ""
kind: preprint
themes:
  - agentic-tool-use
  - hallucination
  - evaluation-of-ai-research
  - reasoning-faithfulness
methods:
  - empirical
  - benchmark
relates_to_projects:
  - sakana-ai-scientist
  - data-to-paper
  - mlgym
status: read
---

## Summary

A Microsoft Research benchmark study of *delegated* LLM workflows —
the emerging paradigm where users supervise an LLM completing tasks
on their behalf rather than co-edit interactively. The authors
introduce DELEGATE-52, a benchmark with 310 work environments across
52 professional domains (coding, crystallography, music notation,
3D objects, textile patterns, …), each containing real documents of
~15k tokens and 5–10 complex editing tasks. Their round-trip relay
simulation evaluates long-horizon delegation without needing
reference solutions, by exploiting the reversibility of forward and
inverse editing tasks.

## Contribution

A large-scale empirical claim: across 19 LLMs, even frontier models
(Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4) "corrupt an average of
25% of document content by the end of long workflows," with other
models failing more severely. Additional experiments show that
agentic tool use does not improve performance, and that degradation
worsens with document size, interaction length, and presence of
distractor files. The headline finding: current LLMs introduce
sparse but severe errors that silently compound over delegation.

## Method

Benchmark construction (DELEGATE-52 across 52 domains) plus a novel
round-trip relay simulation that uses task reversibility to measure
silent document degradation; evaluation of 19 contemporary LLMs.

## Relevance to RISE

A direct stress test for the "delegate the whole research workflow"
posture of agentic RISE pipelines. Projects like
[`sakana-ai-scientist`](../../projects/sakana-ai-scientist.md),
[`data-to-paper`](../../projects/data-to-paper.md), and
[`mlgym`](../../projects/mlgym.md) chain many edits over long
horizons exactly the way DELEGATE-52 shows is brittle. Any RISE
evaluation should adopt the round-trip relay idea, and any system
should be tested for silent compounding corruption across interaction
length.

## Critique / open questions

DELEGATE-52 is text-only; visual renderings are illustrative.
Task reversibility (forward + inverse) is a strong assumption that
may not hold for genuine research tasks (e.g. hypothesis revision).
The "agentic tool use does not help" finding is provocative and
needs replication across more agent harnesses.

## Key quotes

> "Even frontier models (Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4)
> corrupt an average of 25% of document content by the end of long
> workflows, with other models failing more severely."

> "Current LLMs are unreliable delegates: they introduce sparse but
> severe errors that silently corrupt documents, compounding over
> long interaction."
