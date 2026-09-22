---
citekey: li2026ideation
title: 'The Ideation Bottleneck: Decomposing the Quality Gap Between AI-Generated and Human Economics Research'
authors:
- 'Li, N.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2604.03338
kind: preprint
themes:
- evaluation-of-ai-research
- autonomous-research-agents
methods:
- benchmark-evaluation
- quantitative-comparison
relates_to_projects:
- ape
status: skimmed
arxiv_id: '2604.03338'
---

## Summary

Decomposes the quality gap between AI-generated and human economics
research into two components: research idea quality and execution
quality. The corpus is 953 papers — 912 AI-generated papers from the
APE project and 41 human papers from the American Economic Review and
AEJ: Economic Policy. Idea quality is scored by a two-model ensemble
of LMs fine-tuned on publication decisions; execution quality by a
six-dimension rubric assessed with Gemini 3.1 Flash Lite (the same
model family as the APE tournament judge). The idea-quality gap is
large (Cohen's d = 2.23; 47.1% vs. 16.5% mean "exceptional"
probability), the execution gap smaller (d = 0.90; 4.38 vs. 3.84 on a
5-point rubric). Ideation accounts for ~71% of the overall difference;
74% of AI papers use difference-in-differences; only 7 AI papers
(0.8%) beat the median human paper on both dimensions.

## Contribution

Claimed and supported within its design: the first decomposition of
the AI-vs-human quality gap for economics papers, locating the
bottleneck in ideation rather than execution. The strength of the
claim depends entirely on the model-based evaluators (see critique).

## Method

Observational comparison with model-based scoring; no human expert
ratings are mentioned in the abstract. Sample is heavily unbalanced
(912 vs. 41), and the human side is drawn from two top outlets only.

## Relevance to RISE

Catalog slug `ape` (whose papers this analyzes); themes
evaluation-of-ai-research. Two findings matter for the *Architecture
as Epistemology* framing: the ideation bottleneck locates the deficit
in the exploration/novelty dimension rather than execution, and the
74% difference-in-differences share is direct evidence of method
monoculture in AI-generated research — the homogenization concern the
correlated-errors literature predicts.

## Critique / open questions

Both evaluators are models — and execution is judged by the same model
family that judged the APE tournament, which the paper presents as
consistency but is equally a shared-bias risk; the human-paper
benchmark going through the same judges does not remove bias that
correlates with AI style. "Exceptional probability" from models
fine-tuned on publication decisions inherits whatever the publication
process rewards. Whether the 71/29 split generalizes beyond the APE
generation pipeline is untested.

## Key quotes

> "The idea quality gap is large (Cohen's d = 2.23, p < 0.001), with
> human papers achieving 47.1% mean ensemble exceptional probability
> versus 16.5% for AI." (abstract)

> "Idea quality accounts for approximately 71% of the overall quality
> difference, with execution contributing 29%." (abstract)

> "We document that 74% of AI papers employ difference-in-differences,
> and only 7 AI papers (0.8%) surpass the median human paper on both
> idea and execution quality simultaneously." (abstract)
