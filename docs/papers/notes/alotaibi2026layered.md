---
citekey: alotaibi2026layered
title: 'Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers'
authors:
- 'Alotaibi, A.'
- 'Jabbar, M. S.'
- 'Al-Azani, S.'
- 'Ahmed, M.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2608.28327
kind: preprint
themes:
- agentic-reasoning
- llm-cognition
methods: []
relates_to_projects: []
status: queued
sweep_priority: medium
arxiv_id: '2608.28327'
---

## Summary

Although framed as an LLM-security paper, this is a clean measurement of the condition under which stacking LLM components compounds: residual failure falls multiplicatively only under independence, and across all fifteen measurable pairs in a seven-layer stack failure correlation is positive (phi 0.30 to 0.75), with the joint residual exceeding the multiplicative prediction by up to 0.172. The authors show the dependence is architectural rather than sampling-based because members correlate through the shared model they all wrap, so no wider member pool weakens it, and the full stack is statistically indistinguishable from its strongest single layer while refusing four in five benign prompts. Citable for the general claim that agent diversity selects members but does not predict what an assembled architecture delivers.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **medium-priority** candidate for the *Architecture as Epistemology* (ISR) paper (angle: aggregating LLM judgments; correlated errors / homogeneity across LLM agents). Verified against: Opened https://arxiv.org/abs/2608.28327 and read the full abstract, four-author list, submission date 28 Aug 2026, primary category cs.CR.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. (abstract)

> A stack is an ensemble, and ensembles compound only under a condition the LLM security literature recommends but never measures: the members must fail on different inputs. (abstract)
