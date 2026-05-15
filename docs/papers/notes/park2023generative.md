---
citekey: park2023generative
title: "Generative Agents: Interactive Simulacra of Human Behavior"
authors: ["Park, J. S.", "et al."]
year: 2023
venue: "UIST 2023"
doi: ""
url: ""
kind: paper
themes:
  - autonomous-research-agents
  - sociotechnical
  - llm-cognition
methods:
  - simulation
  - user-study
relates_to_projects:
  - sakana-ai-scientist
  - agent-laboratory
status: read
rating: 5
---

## Summary

Park et al. simulate a small town of 25 LLM-driven agents who plan
their days, hold conversations, form social ties, and remember past
events. The architecture combines a long-term memory stream,
periodic reflection that synthesizes high-level inferences from
memories, and a planning loop that decomposes goals into actions.
Human raters find the resulting behavior more believable than
ablations and a human-written baseline.

## Contribution

The first widely-discussed implementation of *persistent,
self-organizing* LLM agents — establishing memory + reflection +
planning as the canonical scaffolding for long-running agentic
systems and showing it works for socially complex tasks, not just
toy benchmarks.

## Method

Twenty-five agents with seed personas inhabit a sandbox town. Their
memory stream is a time-stamped log of observations scored along
recency, importance, and relevance dimensions. Reflection
periodically distills the stream into higher-level beliefs.
Evaluation: human-rated believability across five dimensions, plus
ablation of memory components.

## Relevance to RISE

The memory + reflection + planning triple is recognizable in every
multi-agent RISE pipeline in this catalog. Where Park et al. simulate
*human behavior*, RISE pipelines repurpose the same primitives to
simulate *research behavior* — but the architectural debt is direct.
The paper also raises sociotechnical questions
([@peter2025anthropomorphic], [@sarker2019sociotechnical]) about what
it means when these simulacra produce scholarship attributable to no
human author.

## Critique / open questions

- Believability ≠ correctness. The reflection step routinely
  generates plausible but unverified inferences — a failure mode
  that, transplanted into research pipelines, manifests as
  hallucinated citations or fabricated results.
- The sandbox is small and self-contained; scaling the architecture
  to long-horizon scientific work introduces failure modes (memory
  drift, reflection contamination) not visible in the original
  evaluation.

## Key quotes

*To be added on re-read with page references.*
