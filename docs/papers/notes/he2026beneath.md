---
citekey: he2026beneath
title: 'Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops'
authors:
- 'He, B.'
- 'Zhang, W.'
- 'Jin, Y.'
- 'Liu, X.'
year: 2026
venue: 'EMNLP 2026; arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2609.00077
kind: paper
themes:
- autonomous-research-agents
- evaluation-of-ai-research
- reasoning-faithfulness
- agentic-tool-use
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2609.00077'
---

## Summary

Diagnoses a specific pathology of metric-driven autonomous research loops: surface edit diversity stays constant while semantic and mechanism-level diversity collapses, so the agent keeps rewriting different lines of code to propose the same kind of algorithmic change - and the gap between in-loop metric gains and held-out gains widens. The proposed DAPS mitigation (category-coverage reweighting, persistent edit memory, validation gate) is evaluated under a three-tier protocol that separates the in-loop metric, the audit metric and a blind metric no loop component sees, cutting semantic-cluster decay 69.1% and improving relative faithfulness 83.7% blind. A sharp, generalizable warning about overfitting to verifiable in-loop rewards.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the RISE knowledge base (angle: autonomous AI scientists and their evaluation). Verified against: Opened https://arxiv.org/abs/2609.00077 on 2026-09-07; verbatim abstract read (algorithmic mode collapse, DAPS, three-tier blind/audit protocol, 69.1%/83.7% figures), four authors, submitted 31 Aug 2026, comment confirms EMNLP 2026 acceptance. Not in dedupe_titles.txt.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Code-level autonomous research loops (ARLs) have recently emerged as a concrete object of study in automated machine learning research. (abstract)

> In such loops, an LLM agent proposes modifications to an experimental training pipeline, executes the modified pipeline, and retains edits that improve a verifiable in-loop metric. (abstract)
