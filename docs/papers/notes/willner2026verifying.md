---
citekey: willner2026verifying
title: 'Verifying the Verifiers: Towards Autonomous Policy Evaluation'
authors:
- 'Willner, O.'
- 'Yanagizawa-Drott, D.'
year: 2026
venue: 'Social Catalyst Lab / University of Zurich working paper'
doi: ''
url: https://ape.socialcatalystlab.org/verify
kind: preprint
themes:
- evaluation-of-ai-research
- ai-peer-review
- replication-infrastructure
methods:
- benchmark-evaluation
- error-injection
relates_to_projects:
- ape
status: skimmed
---

## Summary

Working paper from the team behind Project APE evaluating whether
LLM-based verification systems can detect errors in AI-generated
policy-evaluation research. The authors introduce CRED (Classification
of Research Errors and Defects), an error/defect taxonomy, inject
known errors into 100 reproducible papers, and score 80+ model
configurations on their ability to detect them. Headline finding:
detection recall improved from roughly 30% in late 2024 to 99% by July
2026, while verification costs collapsed. The project page hosts a
live benchmark leaderboard; code and reproducibility materials are on
GitHub (SocialCatalystLab/ape-papers).

## Contribution

Claimed: a taxonomy plus a ground-truthed benchmark for automated
research verification, and time-series evidence that frontier models
have become near-complete error detectors on this benchmark. What can
be assessed from the landing page: the design (error injection into
reproducible papers gives real ground truth) and the trend claim; the
recall numbers are the authors' own on their own benchmark.

## Method

Error-injection benchmark: known defects seeded into 100 reproducible
papers, detection measured across 80+ model configurations over time.
The landing page does not state the error-type distribution, whether
recall is balanced across CRED categories, or false-positive rates
(precision) — a verifier that flags everything also achieves high
recall.

## Relevance to RISE

Catalog slug `ape` (same lab); themes evaluation-of-ai-research and
replication-infrastructure. If near-99% recall holds up, the
economics of the verification layer in research pipelines change
qualitatively — the "judging claims is the bottleneck" premise (cf.
[sun2026agon](sun2026agon.md)) becomes partly automatable for the
error classes CRED covers. For the ISR paper it is a candidate
external anchor for what "justification checking" can be delegated to
machines versus reserved for humans.

## Critique / open questions

Injected errors are a lower bound on difficulty: they are, by
construction, errors that were detectable enough to inject cleanly —
naturally occurring flaws (subtle identification failures, unstated
data problems) may not follow the same distribution. Precision is not
reported on the landing page. The note is based on the project page,
not the full PDF; status stays skimmed until the paper itself is read.

## Key quotes

_—_ (No verbatim abstract captured yet; see the working-paper PDF at
the project page.)
