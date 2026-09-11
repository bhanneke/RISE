---
citekey: song2026consensus
title: 'Beyond Consensus: Downward Bias and Role Asymmetry in Multi-Agent LLM Judges for Subjective Evaluation'
authors:
- 'Song, M.'
- 'Kim, C.'
- 'Eo, S.'
- 'Park, C.'
year: 2026
venue: 'Findings of EMNLP 2026'
doi: ''
url: https://arxiv.org/abs/2608.30373
kind: preprint
themes:
- agentic-reasoning
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2608.30373'
---

## Summary

Methodologically this is the paper that most closely executes the structure-versus-aggregation decomposition: three ablations isolate role prompting, multi-round interaction, and explicit score sharing, and the degradation in human alignment relative to a single judge is traced to asymmetric role prompting rather than to the interaction itself. The consensus score falls well beyond the arithmetic midpoint of standalone strict and lenient conditions (strict-stance dominance, not averaging), symmetric roles largely recover baseline performance, and masking peer scores widens disagreement while worsening alignment. For a paper claiming that structure crossed with aggregation rule determines epistemic quality, this is both a template for the ablation design and evidence that consensus mechanisms can manufacture agreement without improving judgment.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: MAS topology / structure vs. aggregation rule; aggregating LLM judgments). Verified against: Opened https://arxiv.org/abs/2608.30373 and read the full abstract, four-author list, submission date 31 Aug 2026, primary category cs.CL, and the comment confirming acceptance to Findings of EMNLP 2026.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Multi-Agent Debate (MAD) has been widely adopted to improve LLM-based evaluation by prompting multiple agents to negotiate and reach a consensus. (abstract)

> However, for subjective rubric-based scoring, inter-agent agreement does not guarantee alignment with human judgments. (abstract)
