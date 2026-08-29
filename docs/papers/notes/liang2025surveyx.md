---
citekey: liang2025surveyx
title: 'SurveyX: Academic Survey Automation via Large Language Models'
authors:
- Liang, X.
- Yang, J.
- Wang, Y.
- Tang, C.
- Zheng, Z.
- Song, S.
- Lin, Z.
- Yang, Y.
- Niu, S.
- Wang, H.
- et al.
year: 2025
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2502.14776
kind: preprint
themes:
- autonomous-research-agents
- evaluation-of-ai-research
- hallucination
methods:
- system-design
- benchmark-evaluation
relates_to_projects:
- surveyx
status: skimmed
arxiv_id: '2502.14776'
---

## Summary

SurveyX is an automated academic-survey generation system that
splits survey writing into a Preparation phase and a Generation
phase, modeled on human writing processes. It introduces three
mechanisms: online reference retrieval, a preprocessing method called
AttributeTree, and a re-polishing process. The abstract positions the
system against limitations of prior automated survey generation —
finite context windows, lack of in-depth content discussion, and the
absence of systematic evaluation frameworks. Reported results:
SurveyX outperforms existing automated survey generation systems in
content quality (a 0.259 improvement) and citation quality (a 1.76
enhancement), "approaching human expert performance across multiple
evaluation dimensions". Example surveys are hosted at surveyx.cn.
arXiv v2 (February 2025; 15 pages, 16 figures per the arXiv
comments).

## Contribution

Claimed: a two-phase survey-generation system with three novel
mechanisms, and evaluation showing gains over existing systems that
approach human-expert quality.

What the abstract supports: two improvement figures are given without
metric scales, so 0.259 and 1.76 are not interpretable from the
abstract alone; the compared "existing automated survey generation
systems" are unnamed; "approaching human expert performance" is not
quantified. What AttributeTree does is not explained beyond
"pre-processing method", and "online reference retrieval" is named
as an innovation without detail.

## Method

Design: Preparation phase and Generation phase; online reference
retrieval; AttributeTree preprocessing; re-polishing.

Evaluation: comparison to existing automated survey systems on
content quality and citation quality, with human-expert performance
as a reference point across "multiple evaluation dimensions".

Not specified in the abstract: baselines, metric definitions and
scales, whether evaluators are LLMs or humans, the number of survey
topics, the LLM back-end, and the retrieval sources.

## Relevance to RISE

Informs `literature-discovery`, `literature-synthesis`, and
`paper-drafting` (the catalog tags all three). Catalog slug:
`surveyx`. The catalog page records that the open-source release
omits the online crawler and paper database, so the "online reference
retrieval" that the abstract presents as an innovation is available
only through the hosted service; the abstract's claims therefore
describe the closed configuration. The catalog lists `autosurvey`
([wang2024autosurvey](wang2024autosurvey.md)) as the closest
sibling, but the abstract does not name it, so no head-to-head
comparison can be drawn from the abstracts.

Multi-agent structure / aggregation: the abstract describes a
sequential two-phase pipeline with a "re-polishing" revision pass
and names no multi-perspective agents, debate, or parallel
generation with merge, which places SurveyX at the
single-pipeline-plus-revision-loop end of the structural spectrum in
the curator's framing; whether re-polishing involves a separate
reviewer model or self-revision is not stated.

## Critique / open questions

- The improvement figures lack scales and baselines; effect size
  cannot be judged from the abstract.
- Whether content and citation quality were judged by LLMs or humans
  is not stated; if LLM-judged, the "approaching human expert"
  claim needs a human anchor.
- Because the catalog reports that the retrieval and paper-DB
  components are closed, the abstract's results cannot be
  independently reproduced from the open release.
- The abstract concedes no limitations.
- Metadata nit: the last author is recorded as "Zhiyu li"
  (lowercase surname) in both the manifest and the bib entry.

## Key quotes

> "Inspired by human writing processes, we propose SurveyX, an
> efficient and organized system for automated survey generation that
> decomposes the survey composing process into two phases: the
> Preparation and Generation phases." (abstract)

> "By innovatively introducing online reference retrieval, a
> pre-processing method called AttributeTree, and a re-polishing
> process, SurveyX significantly enhances the efficacy of survey
> composition." (abstract)

> "Experimental evaluation results show that SurveyX outperforms
> existing automated survey generation systems in content quality
> (0.259 improvement) and citation quality (1.76 enhancement),
> approaching human expert performance across multiple evaluation
> dimensions." (abstract)
