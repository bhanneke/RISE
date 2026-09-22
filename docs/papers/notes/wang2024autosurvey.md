---
citekey: wang2024autosurvey
title: 'AutoSurvey: Large Language Models Can Automatically Write Surveys'
authors:
- Wang, Y.
- Guo, Q.
- Yao, W.
- Zhang, H.
- Zhang, X.
- Wu, Z.
- Zhang, M.
- Dai, X.
- Zhang, M.
- Wen, Q.
- et al.
year: 2024
venue: NeurIPS 2024
doi: ''
url: https://arxiv.org/abs/2406.10252
kind: paper
themes:
- autonomous-research-agents
- evaluation-of-ai-research
- agentic-reasoning
methods:
- system-design
- benchmark-evaluation
relates_to_projects:
- autosurvey
status: skimmed
arxiv_id: '2406.10252'
---

## Summary

AutoSurvey is a methodology for automatically generating
comprehensive literature surveys in fast-moving fields such as AI.
The abstract names three obstacles to LLM survey writing — context
window limits, parametric-knowledge constraints, and the absence of
evaluation benchmarks — and answers them with a four-step pipeline:
initial retrieval and outline generation; subsection drafting by
specialized LLMs; integration and refinement; and evaluation and
iteration. The stated contributions are a comprehensive solution to
the survey problem, a reliable evaluation method, and experimental
validation of effectiveness. Code and resources are released on
GitHub. Published at NeurIPS 2024 (arXiv v2, June 2024).

## Contribution

Claimed: a complete survey-generation system, a reliable evaluation
method, and experimental validation.

What the abstract supports: the pipeline stages are named, but the
abstract gives no numbers, baselines, survey lengths, or
metric definitions. "Reliable evaluation method" is asserted
without stating what it measures or how reliability was established.
The catalog page attributes citation-quality and content-quality
scores and survey lengths of 8k–64k tokens to the paper; those
details come from the catalog entry, not the abstract.

## Method

Design: retrieval → outline generation → parallel subsection drafting
by "specialized LLMs" → integration and refinement → evaluation and
iteration.

Evaluation: described only as "rigorous evaluation and iteration"
and "a reliable evaluation method".

Not specified in the abstract: which LLMs are used and whether
"specialized" means distinct models or distinct prompts; the
retrieval corpus; the number and length of generated surveys;
whether evaluation is automatic or human; the comparison baselines;
and the metrics.

## Relevance to RISE

Informs `literature-discovery`, `literature-synthesis`, and
`paper-drafting` (the catalog tags all three). Catalog slug:
`autosurvey`. The catalog lists `surveyx`
([liang2025surveyx](liang2025surveyx.md)) as the closest sibling;
the SurveyX abstract does not name AutoSurvey among its baselines,
so any head-to-head comparison rests on the catalog, not on either
abstract.

Multi-agent structure / aggregation: the abstract describes a
parallel-generation-and-merge structure — subsections drafted by
specialized LLMs and then passed through "integration and
refinement" — followed by an "evaluation and iteration" loop, which
is the parallel generation + merge + review-loop pattern the
curator's ISR paper is concerned with; the abstract gives no evidence
that isolates the effect of the merge or the iteration step on
survey quality.

## Critique / open questions

- No quantitative results in the abstract; effectiveness cannot be
  assessed from it.
- If the evaluation method is LLM-based (not stated), the "reliable
  evaluation" claim would be circular without human validation.
- How integration handles overlap or contradiction between
  independently drafted subsections is not described.
- The abstract says resources are open; the catalog records no
  declared license in the repository — a tension worth checking
  before reuse.
- The abstract concedes the three general challenges of LLM survey
  writing but no AutoSurvey-specific limitations.

## Key quotes

> "AutoSurvey addresses these challenges through a systematic
> approach that involves initial retrieval and outline generation,
> subsection drafting by specialized LLMs, integration and
> refinement, and rigorous evaluation and iteration." (abstract)

> "While large language models (LLMs) offer promise in automating
> this process, challenges such as context window limitations,
> parametric knowledge constraints, and the lack of evaluation
> benchmarks remain." (abstract)

> "Our contributions include a comprehensive solution to the survey
> problem, a reliable evaluation method, and experimental validation
> demonstrating AutoSurvey's effectiveness." (abstract)
