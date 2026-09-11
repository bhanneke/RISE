---
citekey: agarwal2025autodiscovery
title: 'AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise'
authors:
- Agarwal, D.
- Majumder, B. P.
- Adamson, R.
- Chakravorty, M.
- Gavireddy, S. R.
- Parashar, A.
- Surana, H.
- Mishra, B. D.
- McCallum, A.
- Sabharwal, A.
- Clark, P.
year: 2025
venue: NeurIPS 2025 (arXiv 2507.00310)
doi: ''
url: https://arxiv.org/abs/2507.00310
kind: paper
themes:
- autonomous-research-agents
- agentic-reasoning
- evaluation-of-ai-research
methods:
- system-design
- benchmark-evaluation
- human-evaluation
relates_to_projects:
- asta-autodiscovery
status: skimmed
arxiv_id: '2507.00310'
---

## Summary

AutoDiscovery addresses open-ended autonomous scientific discovery
(ASD): instead of answering a human-specified research question, the
system chooses which hypotheses to pursue by its own criterion. The
criterion is Bayesian surprise, defined as the epistemic shift from the
LLM's prior belief in a hypothesis to its posterior belief after
gathering experimental results. To explore a space of nested
hypotheses, the method runs Monte Carlo tree search with progressive
widening, using surprisal as the reward. Evaluated on data-driven
discovery across 21 real-world datasets from biology, economics,
finance and behavioral science, AutoDiscovery produces 5–29% more
discoveries deemed surprising by the LLM than competing approaches
under a fixed budget. A human evaluation finds that two-thirds of its
discoveries are also surprising to domain experts. The paper was
accepted at NeurIPS 2025.

## Contribution

Claimed: a principled objective (Bayesian surprise) for open-ended ASD
that improves on diversity heuristics and ill-defined "interestingness"
proxies, plus a tree-search method that optimizes it. What the abstract
supports: the 5–29% gain is measured by the LLM's own surprise judgment
— the same quantity the method optimizes — so the comparison against
competitors is partly on the method's home turf. The independent check
is the expert evaluation (two-thirds surprising), but the abstract does
not report the corresponding rate for competitors, and "surprising" is
not the same as true, novel relative to the literature, or important.

## Method

As far as the abstract states: LLM prior and posterior beliefs about a
hypothesis; MCTS with progressive widening and surprisal reward; 21
datasets across four domains; fixed-budget comparison against
unnamed competitors; a human evaluation with domain experts. The
abstract does not specify how beliefs are elicited from the LLM, which
LLM was used, what the budget is, which competitors were run, how many
discoveries or experts were involved in the human study, or whether any
discovery was checked for statistical validity. The arXiv listing (v3,
February 2026) confirms acceptance at NeurIPS 2025.

## Relevance to RISE

Informs `hypothesis-generation`, `data-analysis` and `code-generation`
(the catalog's tags) and, through its "knowing which questions to ask"
framing, `rq-formulation`. Catalog slug:
[`asta-autodiscovery`](../../projects/asta-autodiscovery.md), which
describes the production version inside Ai2's AstaLabs; the catalog
notes there is no literature layer. Among catalog systems, it contrasts
with [`google-co-scientist`](../../projects/google-co-scientist.md),
whose abstract describes a tournament-evolution process for hypothesis
selection, and with [`kosmos`](../../projects/kosmos.md), which couples
data analysis with literature search. For the ISR question of how
aggregation rules shape epistemic quality, this paper is a direct case:
tree search (MCTS with progressive widening) is the selection structure
and Bayesian surprise is the selection rule, so the paper's own
comparison — surprise-driven search versus diversity or interestingness
heuristics — is a structure-and-rule comparison whose outcome is
measured by LLM-judged and expert-judged surprise.

## Critique / open questions

The circularity between the optimized criterion and the primary
outcome metric is the main open issue; only the expert evaluation
breaks it, and the abstract gives no size or protocol for that study.
Surprise is measured relative to the LLM's beliefs rather than the
literature, so a "discovery" may be a rediscovery or a spurious
correlation (the catalog entry raises both and flags the
multiple-comparisons risk of running many automated experiments). The
abstract's own concession is modest: the results are "an important step
towards" open-ended ASD, not a demonstration of it. Whether expert
surprise predicts validity or eventual publication cannot be assessed.

## Key quotes

> "This paper presents AutoDiscovery -- a method for open-ended ASD that
> instead drives scientific exploration using Bayesian surprise. Here,
> we quantify the epistemic shift from the LLM's prior beliefs about a
> hypothesis to its posterior beliefs after gathering experimental
> results." (abstract)

> "To efficiently explore the space of nested hypotheses, our method
> employs a Monte Carlo tree search (MCTS) strategy with progressive
> widening using surprisal as the reward function." (abstract)

> "Our results demonstrate that under a fixed budget, AutoDiscovery
> substantially outperforms competitors by producing 5-29% more
> discoveries deemed surprising by the LLM. Our human evaluation further
> reveals that two-thirds of discoveries made by our system are
> surprising to domain experts as well, suggesting this is an important
> step towards building open-ended ASD systems." (abstract)
