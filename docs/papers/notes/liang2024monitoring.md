---
citekey: liang2024monitoring
title: 'Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews'
authors:
  - 'Liang, W.'
  - 'Izzo, Z.'
  - 'Zhang, Y.'
  - 'Lepp, H.'
  - 'Cao, H.'
  - 'Zhao, X.'
  - 'Chen, L.'
  - 'Ye, H.'
  - 'Liu, S.'
  - 'Huang, Z.'
  - 'McFarland, D. A.'
  - 'Zou, J. Y.'
year: 2024
venue: 'arXiv:2403.07183'
doi: ""
url: ""
kind: paper
themes:
  - ai-peer-review
  - evaluation-of-ai-research
  - sociotechnical
methods:
  - empirical
relates_to_projects:
  - reviewer
  - marg
  - ape
status: read
---

## Summary

The authors develop a maximum-likelihood, corpus-level estimator that combines expert-written and AI-generated reference texts to quantify the fraction of text in a large corpus that has been substantially modified or produced by an LLM. They apply this estimator to peer reviews submitted to ICLR 2024, NeurIPS 2023, CoRL 2023, and EMNLP 2023, all of which took place after ChatGPT's release. They find that between 6.5% and 16.9% of submitted review text could plausibly have been substantially modified by LLMs, beyond spell-checking or minor edits, with no comparable shift detected in Nature Portfolio journals.

## Contribution

A scalable, corpus-level method for monitoring LLM-modified content that side-steps the unreliability of individual-document AI detection, plus the first systematic empirical case study of LLM penetration into AI-conference peer review.

## Method

Maximum-likelihood distributional estimator trained on expert and AI reference texts; applied to peer-review corpora from four major AI venues. Behavioural correlates (reviewer confidence, submission timing, rebuttal engagement) are examined alongside corpus-level token-frequency shifts (e.g., "commendable", "meticulous", "intricate" rising 9.8x, 34.7x, 11.2x respectively in ICLR 2024).

## Relevance to RISE

This is the canonical empirical baseline for the prevalence of LLM use in peer review and directly informs the ai-peer-review thread of the catalog, complementing the JAIS Vol 25 Iss 1 cluster (sarker2024democratizing, weber2024roboreviewer, drori2024humanloop). It motivates the design of [`reviewer`](../../projects/reviewer.md), [`marg`](../../projects/marg.md), and [`ape`](../../projects/ape.md) by quantifying the scale and behavioural patterns (low confidence, deadline pressure, low rebuttal engagement) that AI-augmented review systems must contend with.

## Critique / open questions

The method estimates only corpus-level fractions and cannot identify individual reviews; behavioural correlates are associative, not causal. The reference distribution depends on choices of "expert" and "AI" templates that may bias the alpha estimate.

## Key quotes

> "Our results suggest that between 6.5% and 16.9% of text submitted as peer reviews to these conferences could have been substantially modified by LLMs, i.e. beyond spell-checking or minor writing updates."

> "The estimated fraction of LLM-generated text is higher in reviews which report lower confidence, were submitted close to the deadline, and from reviewers who are less likely to respond to author rebuttals."

> "We find a significant shift in the frequency of certain tokens in ICLR 2024, with adjectives such as 'commendable', 'meticulous', and 'intricate' showing 9.8, 34.7, and 11.2-fold increases in probability of occurring in a sentence."
