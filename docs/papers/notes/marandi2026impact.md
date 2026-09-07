---
citekey: marandi2026impact
title: 'The impact of multi-agent debate protocols on debate quality: a controlled case study'
authors:
- 'Marandi, R. Z.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2603.28813
kind: preprint
themes:
- agentic-reasoning
- reasoning-faithfulness
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2603.28813'
---

## Summary

Methodologically the nearest neighbour to the paper's identification strategy: it holds prompts, decoding and seeds fixed and varies only the debate protocol (Within-Round, Cross-Round, Rank-Adaptive Cross-Round, and a No-Interaction baseline) across 20 macroeconomic events, precisely to disentangle protocol effects from model effects. It finds a trade-off between peer-referencing and convergence, and reports that the No-Interaction baseline maximizes Argument Diversity - an operational precedent both for the exploration/novelty measure and for the worry that interaction itself costs diversity. Single-author, small-N, so cite for design logic and the diversity metric rather than as a strong empirical result.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule; aggregating LLM judgments; epistemic quality of LLM outputs). Verified against: Opened https://arxiv.org/abs/2603.28813 (arXiv abstract page; confirmed title, single author, cs.MA, v1 28 Mar 2026, full abstract read)

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> In multi-agent debate (MAD) systems, performance gains are often reported; however, because the debate protocol (e.g., number of agents, rounds, and aggregation rule) is typically held fixed while model-related factors vary, it is difficult to disentangle protocol effects from model effects. (abstract)

> To isolate these effects, we compare three main protocols, Within-Round (WR; agents see only current-round contributions), Cross-Round (CR; full prior-round context), and novel Rank-Adaptive Cross-Round (RA-CR; dynamically reorders agents and silences one per round via an external judge model), against a No-Interaction baseline (NI; independent responses without peer visibility). (abstract)
