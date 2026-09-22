---
citekey: tran2026singleagent
title: 'Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets'
authors:
- 'Tran, D.'
- 'Kiela, D.'
year: 2026
venue: 'arXiv preprint (cs.CL)'
doi: ''
url: https://arxiv.org/abs/2604.02460
kind: preprint
themes:
- sociotechnical
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2604.02460'
---

## Summary

Supplies the theoretical backbone that the in-window null results lack: an information-theoretic argument grounded in the Data Processing Inequality showing that under a fixed reasoning-token budget with perfect context utilization, a single agent is more information-efficient, and predicting that multi-agent systems become competitive only when single-agent context utilization degrades or more compute is spent. Confirmed empirically across Qwen3, DeepSeek-R1-Distill-Llama and Gemini 2.5 under matched budgets, with identified artifacts in API-based budget control and standard benchmarks that inflate apparent multi-agent gains. Reported despite falling outside the window because it is the strongest general statement that reported architectural benefits are better explained by unaccounted computation and context effects - the null hypothesis this paper must defeat - and it is missing from the knowledge base.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: organization theory applied to AI agents; MAS failure and cost analyses). Verified against: Verified by opening https://arxiv.org/abs/2604.02460 on 2026-09-07: full abstract read verbatim, 2 authors, v1 2 April 2026, v2 11 April 2026, cs.CL primary (also cs.MA). Pre-window; flagged as centrally missing.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Recent work reports strong performance from multi-agent LLM systems (MAS), but these gains are often confounded by increased test-time computation. (abstract)

> When computation is normalized, single-agent systems (SAS) can match or outperform MAS, yet the theoretical basis and evaluation methodology behind this comparison remain unclear. (abstract)
