---
citekey: stevenson2026humans
title: 'Humans in the Loop: The Next Frontier in the Credibility Revolution'
authors:
- 'Stevenson, M. T.'
- 'Fischman, J. B.'
year: 2026
venue: SSRN working paper 6308160
doi: ''
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6308160
kind: preprint
themes:
- is-methodology
- replication-infrastructure
- human-ai-research-collaboration
methods:
- conceptual
- econometric-theory
relates_to_projects: []
status: skimmed
---

## Summary

Published empirical estimates are inflated and overconfident, and the
authors locate the cause in the econometric framework itself: it
treats the researcher as a calculator that mechanically implements a
method, when in practice a human is making subjective choices
throughout. Once researcher behaviour is modelled, estimator
properties change sharply. Low-power designs such as instrumental
variables show high bias **even at a first-stage F-statistic of 200**;
threshold testing on the first-stage F can *reduce* bias, contrary to
Angrist and Kolesár (2024); and reported standard errors understate
uncertainty because they ignore variation from the researcher's own
choices. The paper argues that modifying econometric practice to
account for the human in the research loop is the next frontier of the
credibility revolution.

## Contribution

Reframes a familiar worry (p-hacking, garden of forking paths) as a
formal property of estimators conditional on researcher behaviour,
rather than as misconduct. The F=200 result is the striking one: it
undercuts a rule of thumb the applied literature leans on heavily. The
claim against Angrist and Kolesár is a direct, checkable disagreement
with a standard reference.

## Method

Theoretical with worked examples; assumptions about researcher
behaviour do the work. The abstract does not state how those
assumptions are justified or how sensitive the conclusions are to
them — which is the obvious place a referee would press.

## Relevance to RISE

The sharpest available statement of *why* automating the research
pipeline is not merely a productivity question. If estimator
properties depend on the behaviour of whoever is in the loop, then
replacing a human with an agent does not remove the problem; it
replaces one behavioural profile with another, largely uncharacterised
one. Agents have their own systematic choice patterns — the
AI-generated economics corpus is 74% difference-in-differences
(`li2026ideation`) — so the distribution of researcher degrees of
freedom changes shape rather than collapsing. This is the methodological
counterpart to the reproducibility entries (`brodeur2025reproducibility`,
`social-science-replicability`, `reprorepo`) and belongs in any honest
account of what an automated pipeline does to inference.

## Critique / open questions

Everything rests on the plausibility of the assumed researcher
behaviour model; the abstract gives no sense of the range examined. It
is also silent on the question this KB cares about most — whether an
LLM in the loop is better or worse than a human on these dimensions,
which is an empirical question nobody has answered. Working paper,
not yet peer reviewed (the acknowledgements name an editor and
referees, so a journal process appears to be underway).

## Key quotes

> "Despite the advances of the credibility revolution, published
> estimates tend to be inflated and overconfident. We argue that this
> stems from a weakness in the dominant econometric framework:
> treating the researcher like a calculator that mechanically
> implements the econometric method." (abstract)

> "Under plausible assumptions on researcher behavior, low-power
> estimators such as instrumental variables exhibit high degrees of
> bias, even with a first-stage F-statistic of 200." (abstract)

> "And standard errors understate uncertainty, since they ignore
> variation due to researchers' subjective choices." (abstract)
