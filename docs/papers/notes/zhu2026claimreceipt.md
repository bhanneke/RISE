---
citekey: zhu2026claimreceipt
title: 'ClaimReceipt: Verifying Evidence Sufficiency and Coverage in Agent Evaluations'
authors:
- 'Zhu, P.'
- 'Chang, S.'
year: 2026
venue: 'arXiv preprint (cs.AI); submitted to NeurIPS 2026 workshop ''Who Verifies the Agents?'''
doi: ''
url: https://arxiv.org/abs/2609.01992
kind: preprint
themes:
- reasoning-faithfulness
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2609.01992'
---

## Summary

Separates two evidentiary questions that agent evaluations routinely conflate - whether a reported claim is recomputable from retained evidence (sufficiency) and whether the retained records cover the committed experiment set (coverage) - and argues that generic logs and hash-linked transcripts answer neither reliably. The verifier binds typed evidence to a signed, pre-registered experiment manifest and returns PASS, INVALID or INCONCLUSIVE per claim at 0.021% of model-inference time; withholding a terminal receipt correctly yields INCONCLUSIVE_COVERAGE. For the ISR paper's traceability construct this is the sharpest available formal definition: traceability is not the existence of a log but the recomputability of a specific claim plus the visibility of omissions.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: epistemic quality of LLM outputs). Verified against: Verified via arXiv API metadata record on 2026-09-07: full abstract, 2 authors, v1, published 2026-09-02, primary cs.AI (also cs.CR, cs.MA), 8 pages.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Agent evaluations face two distinct evidentiary questions: whether a reported claim is recomputable from retained evidence (sufficiency), and whether the retained records cover the committed experiment set (coverage). (abstract)

> Generic logs and hash-linked transcripts answer neither reliably. (abstract)
