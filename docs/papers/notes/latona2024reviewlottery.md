---
citekey: latona2024reviewlottery
title: 'The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores
  and Acceptance Rates'
authors:
- Russo Latona, G.
- Horta Ribeiro, M.
- Davidson, T. R.
- Veselovsky, V.
- West, R.
year: 2024
venue: arXiv 2405.02150
doi: ''
url: https://arxiv.org/abs/2405.02150
kind: preprint
themes:
- ai-peer-review
- evaluation-of-ai-research
- ai-publishing-ecosystems
methods:
- empirical
- quasi-experiment
relates_to_projects:
- reviewer
- marg
status: read
arxiv_id: '2405.02150'
---

## Summary

A quasi-experimental study of the prevalence and impact of
AI-assisted peer reviews at the 2024 International Conference on
Learning Representations (ICLR). Using the GPTZero detector to flag
AI-assisted reviews, the authors estimate a lower bound for
prevalence, compare paired scores from AI-assisted versus human
reviews of the same paper, and run a matched analysis of acceptance
outcomes for submissions near the decision threshold.

## Contribution

Three empirical findings: (1) at least 15.8% of ICLR 2024 reviews
were AI-assisted; (2) in pairs of reviews of the same paper,
AI-assisted reviews scored higher than human reviews 53.4% of the
time (p = 0.002; +14.4% relative odds); and (3) in a matched study,
threshold-borderline submissions that received an AI-assisted review
were 4.9 percentage points more likely to be accepted (p = 0.024).
Together, AI-assistance behaves like a lottery boost for borderline
papers.

## Method

Quasi-experimental observational study of ICLR 2024 OpenReview data;
LLM-text detection via GPTZero; within-paper review pair comparisons
plus matched/threshold analysis of acceptance.

## Relevance to RISE

A foundational empirical reference for the RISE pillar on AI peer
review and AI-mediated evaluation: it demonstrates that LLM-assisted
review changes outcomes at scale and at a venue that several catalog
projects (e.g. [`reviewer`](../../projects/reviewer.md),
[`marg`](../../projects/marg.md)) explicitly target. Any RISE
evaluation that treats peer-review acceptance as ground truth must
account for the lottery effect documented here.

## Critique / open questions

GPTZero gives a lower bound only; the paper cannot distinguish "LLM
as spell-checker" from "LLM as core argument generator," and the
detector itself has known false-positive issues. The 4.9pp effect is
estimated near the threshold and may not generalise away from
borderline papers.

## Key quotes

> "We obtain a lower bound for the prevalence of AI-assisted reviews
> at ICLR 2024 using the GPTZero LLM detector, estimating that at
> least 15.8% of reviews were written with AI assistance."

> "Submissions near the acceptance threshold that received an
> AI-assisted peer review were 4.9 percentage points (p = 0.024) more
> likely to be accepted than submissions that did not."
