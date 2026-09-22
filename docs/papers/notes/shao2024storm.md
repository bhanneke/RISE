---
citekey: shao2024storm
title: Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models
authors:
- Shao, Y.
- Jiang, Y.
- Kanell, T. A.
- Xu, P.
- Khattab, O.
- Lam, M. S.
year: 2024
venue: NAACL 2024
doi: ''
url: https://arxiv.org/abs/2402.14207
kind: paper
themes:
- agentic-reasoning
- hallucination
- evaluation-of-ai-research
methods:
- system-design
- benchmark-evaluation
- expert-feedback
relates_to_projects:
- storm
status: skimmed
arxiv_id: '2402.14207'
---

## Summary

STORM (Synthesis of Topic Outlines through Retrieval and
Multi-perspective Question Asking) is a writing system for producing
grounded, organized long-form articles from scratch, aiming at
Wikipedia-comparable breadth and depth. The paper frames the
pre-writing stage — researching the topic and preparing an outline —
as the underexplored problem. STORM (1) discovers diverse
perspectives on the topic, (2) simulates conversations in which
writers holding different perspectives question a topic expert
grounded in trusted Internet sources, and (3) curates the collected
information into an outline. Evaluation uses FreshWiki, a dataset of
recent high-quality Wikipedia articles, outline assessments for the
pre-writing stage, and feedback from experienced Wikipedia editors.
Against an outline-driven retrieval-augmented baseline, more STORM
articles are judged organized (+25 points absolute) and broad in
coverage (+10). Editors flagged source bias transfer and
over-association of unrelated facts. NAACL 2024 main conference.

## Contribution

Claimed: identifying pre-writing as the bottleneck for grounded
long-form generation; a perspective-guided question-asking method;
the FreshWiki dataset and outline assessments; expert feedback that
surfaces new failure modes.

What the abstract supports: the organization and coverage gains are
relative to a single baseline, and the abstract does not say who
judged "organized" and "broad" (editors or an automatic judge).
"Comparable breadth and depth to Wikipedia pages" is the stated goal,
not a demonstrated result in the abstract. Accuracy of article
content is not reported in the abstract; the two failure modes the
editors identified are reported as findings.

## Method

Design: perspective discovery; simulated writer–expert conversations
grounded in Internet sources; outline curation; article generation
from the outline.

Evaluation: FreshWiki (recent Wikipedia articles; the abstract does
not state why recency was chosen); outline assessments for the
pre-writing stage; comparison with an outline-driven RAG baseline on
organization and coverage; qualitative feedback from experienced
Wikipedia editors.

Not specified in the abstract: the LLM and search engine, the number
of articles and editors, the definitions of "organized" and "broad",
absolute quality levels, and what counts as a "trusted" source.

## Relevance to RISE

Informs `literature-discovery`, `literature-synthesis`, and
`paper-drafting` (the catalog's tags); the question-asking step also
borders `rq-formulation`, since it decides what to ask before
searching. Catalog slug: `storm` (the catalog treats STORM and
Co-STORM as one project). Direct successor:
[jiang2024costorm](jiang2024costorm.md). The catalog's limitation
that output "is not publication-ready and requires significant
editing" is consistent with the abstract's editor-identified failure
modes.

Multi-agent structure / aggregation: STORM is the canonical
multi-perspective structure — parallel, perspective-conditioned
simulated conversations between writer agents and an expert agent
whose outputs are then curated into a single outline (parallel
generation + merge) — and the abstract attributes the organization
and coverage gains to this design relative to a single-outline
baseline, while the editor feedback names two epistemic failure
modes of grounded multi-source synthesis, source bias transfer and
over-association of unrelated facts, that any aggregation rule
would have to control.

## Critique / open questions

- Gains are measured against one baseline; robustness to other
  baselines cannot be assessed from the abstract.
- Factual accuracy of generated articles is not among the reported
  metrics in the abstract; only organization and coverage are.
- The abstract concedes source bias transfer and over-association of
  unrelated facts as open challenges.
- Wikipedia-style exposition differs from research synthesis (no
  argument, no gap identification), so transfer to literature
  reviews in the RISE sense is untested here.
- Who rated organization and coverage, and how perspectives are
  selected, is not stated in the abstract.

## Key quotes

> "STORM models the pre-writing stage by (1) discovering diverse
> perspectives in researching the given topic, (2) simulating
> conversations where writers carrying different perspectives pose
> questions to a topic expert grounded on trusted Internet sources,
> (3) curating the collected information to create an outline."
> (abstract)

> "Compared to articles generated by an outline-driven
> retrieval-augmented baseline, more of STORM's articles are deemed
> to be organized (by a 25% absolute increase) and broad in coverage
> (by 10%)." (abstract)

> "The expert feedback also helps identify new challenges for
> generating grounded long articles, such as source bias transfer and
> over-association of unrelated facts." (abstract)
