---
citekey: yamada2025aiscientistv2
title: 'The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search'
authors:
- Yamada, Y.
- Lange, R. T.
- Lu, C.
- Hu, S.
- Lu, C.
- Foerster, J.
- Clune, J.
- Ha, D.
year: 2025
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2504.08066
kind: preprint
themes:
- autonomous-research-agents
- ai-peer-review
- evaluation-of-ai-research
methods:
- system-design
- tree-search
- real-venue-submission
relates_to_projects:
- sakana-ai-scientist
status: skimmed
arxiv_id: '2504.08066'
---

## Summary

The AI Scientist-v2 is an end-to-end agentic system that formulates
hypotheses, designs and executes experiments, analyzes and visualizes
data, and writes manuscripts. Relative to v1
([lu2024aiscientist](lu2024aiscientist.md)) it drops the reliance on
human-authored code templates, is said to generalize across ML
domains, and replaces the fixed pipeline with a progressive agentic
tree search managed by a dedicated experiment-manager agent. The AI
reviewer is extended with a vision-language-model feedback loop that
iteratively refines figure content and aesthetics. The evaluation
consisted of submitting three fully autonomous manuscripts to a
peer-reviewed ICLR workshop; one scored above the average human
acceptance threshold, which the authors present as the first fully
AI-generated paper to pass peer review. Code is open-sourced, and the
paper also discusses the role of AI in science and AI safety.

## Contribution

Claimed: the first entirely AI-generated peer-review-accepted workshop
paper, template-free generalization across ML domains, and a novel
progressive agentic tree-search methodology. What the abstract
supports: one of three workshop submissions received scores above the
average acceptance threshold. That is a real external signal, but a
small one (n = 3, one workshop) and at workshop rather than
main-conference level — a limit the title itself concedes.
"Generalizes effectively across diverse machine learning domains" is
asserted without quantification in the abstract.

## Method

System paper with a field test. Three manuscripts were produced
autonomously and submitted to a peer-reviewed ICLR workshop; scores
were compared with the workshop's average human acceptance threshold.
The abstract does not specify which workshop, whether reviewers knew
the manuscripts were AI-generated, what the scores were, how many runs
or ideas were needed to obtain the three manuscripts, what happened to
the two that fell short, or which base models were used. The tree
search (branching, node selection, stopping rule) and the VLM
feedback loop are described only by name.

## Relevance to RISE

Informs hypothesis-generation, research-design, code-generation,
data-analysis, paper-drafting, revision-editing (the VLM figure loop),
and referee-simulation. It is the paper behind the catalog entry
`sakana-ai-scientist`, which scores it 3 on autonomy and 0 on
cross-family policy (same-model self-refinement). Two catalog
neighbors compare against it explicitly: the abstract of
[liu2026autoresearchclaw](liu2026autoresearchclaw.md) uses AI
Scientist v2 as its benchmark baseline, and the abstract of
[jin2026arbor](jin2026arbor.md) likewise organizes experimentation as
a manager-controlled tree. For the multi-agent
structure/aggregation question: the abstract's main structural change
is a progressive agentic tree search over experiments managed by an
experiment-manager agent, combined with a reviewer-plus-VLM feedback
loop for figures — but the abstract reports no ablation isolating the
contribution of the tree search from the base model or from the
template removal.

## Critique / open questions

Three submissions to one workshop cannot establish reliability; the
abstract gives a success count, not a rate over all attempts. The
comparison is against an average acceptance threshold, not against
human-written submissions to the same workshop, so reviewer leniency
and workshop-level standards are confounded with system capability.
Whether the accepted-scoring manuscript's claims were correct is not
addressed in the abstract. The abstract concedes the workshop-level
scope and that only one of three manuscripts crossed the threshold;
the promised discussion of AI safety is announced but its content is
not summarized. The catalog page notes that self-review is not a
substitute for external peer review and that quality depends on seed
templates — the latter sits awkwardly with the abstract's claim that
templates were eliminated and deserves a check against the full text.

## Key quotes

> "We evaluated The AI Scientist-v2 by submitting three fully
> autonomous manuscripts to a peer-reviewed ICLR workshop." (abstract)

> "Notably, one manuscript achieved high enough scores to exceed the
> average human acceptance threshold, marking the first instance of a
> fully AI-generated paper successfully navigating a peer review."
> (abstract)

> "Additionally, we enhance the AI reviewer component by integrating a
> Vision-Language Model (VLM) feedback loop for iterative refinement of
> content and aesthetics of the figures." (abstract)
