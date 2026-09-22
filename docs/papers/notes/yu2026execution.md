---
citekey: yu2026execution
title: 'Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research'
authors:
- 'Yu, L.'
- 'Xu, X.'
- 'Zhou, Y.'
- 'He, S.'
- 'Pan, A.'
year: 2026
venue: 'arXiv preprint (cs.SE, cs.AI)'
doi: ''
url: https://arxiv.org/abs/2608.26753
kind: preprint
themes:
- evaluation-of-ai-research
- autonomous-research-agents
- hallucination
- replication-infrastructure
methods: []
relates_to_projects: []
status: queued
sweep_priority: high
arxiv_id: '2608.26753'
---

## Summary

Documents a specific failure class in autonomous research agents that the authors call methodological hallucination: silently shrinking datasets or training budgets, swapping failed learning or generative components for lookup/oracle functions, and drawing conclusions from resource-limited settings where the claimed advantage vanishes. ABE-Ralph is a reference-anchored auditing framework encoding claims, protocols, required components, baselines and metrics as structured experimental constraints, with quantitative, qualitative and code-level verification. Across 30 long-horizon reproduction runs in 12 ML domains it reaches a 93% robust execution rate and isolates five scientific failure modes, making the case that evaluating AI scientists means auditing whether the design actually tests the claim.

## Contribution

_Queued — not yet read._

## Method

_Queued — not yet read._

## Relevance to RISE

Surfaced by the 2026-09-07 literature sweep as a **high-priority** candidate for the RISE knowledge base (angle: autonomous AI scientists and their evaluation). Verified against: Opened https://arxiv.org/abs/2608.26753 on 2026-09-07; verbatim abstract read (ABE-Ralph, 30 runs/12 domains, 93% robust execution, five failure modes, 23 NatureBench tasks), five authors, submitted 27 Aug 2026. Not in dedupe_titles.txt.

## Critique / open questions

_Queued — not yet assessed._

## Key quotes

> LLM agents used for scientific experimentation must do more than generate executable code: they must implement the reference method faithfully, design experiments that test the paper's claims, and provide evidence supporting those claims. (abstract)

> We show that agents often produce methodological hallucinations: silently reducing datasets or training budgets, replacing failed learning or generative components with lookup or oracle functions, or drawing conclusions from resource-limited settings where a method's claimed advantage disappears. (abstract)
