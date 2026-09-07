---
citekey: yoon2026arcticswarm
title: 'ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Agent Research'
authors:
- 'Yoon, S.'
- 'Liu, B.'
- 'Wang, Y.'
- 'Wu, R.'
- 'Xu, C.'
- 'Kuang, N. L.'
- 'Hwang, S.-w.'
- 'He, Y.'
- 'Yao, Z.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2609.01870
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
arxiv_id: '2609.01870'
---

## Summary

The closest empirical analogue to the paper's own setting: an open-ended, verifier-free research task where the authors show that giving parallel agents access to peers' partial findings makes search converge on an early candidate before alternatives are tested, i.e. structure directly damages exploration. Their remedy is architectural rather than about model quality: separate evidence gathering from evidence integration via a shared bulletin board, gate isolation so selected searches keep their own prior, and enforce structured review at three commitment boundaries (82.6 percent vs 78.8 without gated isolation and 74.5 with review also disabled). This is the paper to cite for 'communication topology determines exploration breadth' and to distinguish from because it still scores itself on benchmark accuracy rather than epistemic quality.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule; aggregating LLM judgments; correlated errors / homogeneity across LLM agents; organization theory applied to AI agents; epistemic quality of LLM outputs). Verified against: Opened https://arxiv.org/abs/2609.01870 and read the full abstract with the ablation numbers; arXiv API confirms the nine-author list, published 2026-09-01, cs.MA.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-agent systems have shown strong performance in domains with reliable verifiers such as coding, where multi-parallel candidate generation selected by a verifier is effective. (abstract)

> However, such pipelines would not generalize to open-ended, long-horizon research tasks without a verifier. (abstract)
