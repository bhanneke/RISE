---
citekey: lu2024aiscientist
title: 'The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery'
authors:
- Lu, C.
- Lu, C.
- Lange, R. T.
- Foerster, J.
- Clune, J.
- Ha, D.
year: 2024
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2408.06292
kind: preprint
themes:
- autonomous-research-agents
- ai-peer-review
- evaluation-of-ai-research
methods:
- system-design
- case-study
- automated-reviewer-validation
relates_to_projects:
- sakana-ai-scientist-v1
status: skimmed
arxiv_id: '2408.06292'
---

## Summary

The paper presents The AI Scientist, a framework in which a frontier
language model carries out the machine-learning research process
without human intervention: it generates research ideas, writes code,
executes experiments, visualizes results, writes a full scientific
paper, and then runs a simulated review process to evaluate the
result. The authors apply it to three ML subfields — diffusion
modeling, transformer-based language modeling, and learning dynamics —
and report that each idea is developed into a full paper at a cost of
less than $15. To score the output they design an automated reviewer,
which they report reaches near-human performance on paper scores; by
that reviewer's judgment, some generated papers exceed the acceptance
threshold of a top ML conference. Code is open-sourced. The abstract
frames the approach as the beginning of open-ended, community-like
iteration on research ideas, but states this only "in principle".

## Contribution

Claimed: "the first comprehensive framework for fully automatic
scientific discovery", plus an automated reviewer validated against
human scoring. What the abstract supports: an end-to-end pipeline
demonstrated in three ML subfields at very low per-paper cost, and an
automated reviewer that the authors report as near-human. The
headline acceptability claim is explicitly conditional on that same
reviewer ("as judged by our automated reviewer"), so it is an internal
rather than external validation. Open-ended iterative development is
asserted as possible, not demonstrated.

## Method

System description plus demonstration. Three ML subfields are used as
application areas; each idea is turned into a paper for under $15. An
automated reviewer is "designed and validated" and reported to
achieve near-human performance in evaluating paper scores — which
implies a comparison against human reviewer scores, but the abstract
does not specify the reference dataset, the number of papers, the
agreement metric, or which language models power the pipeline. The
abstract also does not state how many ideas were generated, how many
failed, or whether any generated paper was assessed by a human.

## Relevance to RISE

Informs the hypothesis-generation, research-design, code-generation,
data-analysis, paper-drafting, and referee-simulation stages; it is
the paper behind the catalog entry `sakana-ai-scientist-v1`, which
scores the system 2 on lifecycle coverage and 0 on cross-family policy
(self-refinement within one model family). It is the direct
predecessor of [yamada2025aiscientistv2](yamada2025aiscientistv2.md),
whose abstract positions v2 against v1 by removing human-authored code
templates and adding tree search. For the multi-agent
structure/aggregation question: the only aggregation mechanism the
abstract describes is a simulated review loop (an automated reviewer
scoring the generated paper), with the possibility of open-ended,
community-like iteration mentioned only "in principle"; no debate,
tournament, or tree-search mechanism appears in the abstract.

## Critique / open questions

The central acceptability claim is circular at the abstract level:
the papers are judged acceptable by a reviewer the same authors built,
and the abstract gives no figures for the reviewer's agreement with
humans. Whether generated ideas are novel in fact, rather than by the
reviewer's judgment, cannot be assessed from the abstract. The
abstract concedes little explicitly, though its hedge that open-ended
iteration works "in principle" signals that cumulative iteration was
not shown. The catalog page for `sakana-ai-scientist-v1` notes that
the self-review correlates weakly with external peer-review judgments
and that the system is locked to three CS templates; the abstract
itself does not mention templates.

## Key quotes

> "We introduce The AI Scientist, which generates novel research
> ideas, writes code, executes experiments, visualizes results,
> describes its findings by writing a full scientific paper, and then
> runs a simulated review process for evaluation." (abstract)

> "To evaluate the generated papers, we design and validate an
> automated reviewer, which we show achieves near-human performance in
> evaluating paper scores." (abstract)

> "The AI Scientist can produce papers that exceed the acceptance
> threshold at a top machine learning conference as judged by our
> automated reviewer." (abstract)
