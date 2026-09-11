---
citekey: asai2024openscholar
title: 'OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs'
authors:
- Asai, A.
- He, J.
- Shao, R.
- Shi, W.
- Singh, A.
- Chang, J. C.
- Lo, K.
- Soldaini, L.
- Feldman, S.
- D'Arcy, M.
- et al.
year: 2024
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2411.14199
kind: preprint
themes:
- hallucination
- evaluation-of-ai-research
- agentic-reasoning
methods:
- system-design
- benchmark-evaluation
- human-evaluation
relates_to_projects:
- open-scholar
status: skimmed
arxiv_id: '2411.14199'
---

## Summary

OpenScholar is a specialized retrieval-augmented LM that answers
scientific queries by retrieving passages from 45 million
open-access papers and synthesizing citation-backed responses. To
evaluate it, the authors build ScholarQABench, a multi-domain
literature-search benchmark of 2,967 expert-written queries and 208
long-form answers across computer science, physics, neuroscience,
and biomedicine. On it, OpenScholar-8B outperforms GPT-4o by 5% and
PaperQA2 by 7% in correctness. GPT-4o is reported to hallucinate
citations 78–90% of the time, whereas OpenScholar reaches citation
accuracy on par with human experts. The datastore, retriever, and
self-feedback inference loop also improve off-the-shelf models
(OpenScholar-GPT4o: +12% correctness). Experts preferred
OpenScholar-8B and OpenScholar-GPT4o over expert-written responses
51% and 70% of the time (GPT-4o: 32%). Code, models, datastore, data,
and a demo are open-sourced.

## Contribution

Claimed: the first large-scale multi-domain literature-search
benchmark; a small open model that beats GPT-4o and PaperQA2 on
correctness; near-expert citation accuracy; the inference pipeline
as a plug-in improvement for closed models; expert preference over
human-written answers; full openness.

What the abstract supports: all headline numbers are stated, but they
are measured on the authors' own benchmark, and "first large-scale
multi-domain" is a priority claim that cannot be checked from the
abstract. The 51% preference for OpenScholar-8B over expert-written
answers is, on its face, parity rather than superiority; the 70%
figure for OpenScholar-GPT4o is the stronger result. The abstract
does not isolate the contribution of the self-feedback loop from
that of the datastore and retriever.

## Method

Design: retrieval over 45M open-access papers; a specialized 8B LM;
a self-feedback inference loop; the same pipeline wrapped around
GPT-4o.

Evaluation: ScholarQABench (2,967 queries, 208 long-form answers, four
domains); automatic metrics for correctness and citation accuracy;
human evaluation as expert pairwise preference against
expert-written answers.

Not specified in the abstract: how "correctness" is scored (rubric,
LLM judge, or expert), how citation hallucination is operationalized,
whether the GPT-4o citation-hallucination figure is for GPT-4o with
or without retrieval, the number of expert evaluators, the training
recipe for the 8B model, and what the self-feedback loop concretely
does.

## Relevance to RISE

Informs `literature-discovery` and `literature-synthesis`. Catalog
slug: `open-scholar`. The catalog's stated distinctive contribution —
pairing the system with ScholarQABench and an expert-evaluation
interface — is exactly what the abstract foregrounds. Grounded
comparison: the abstract benchmarks directly against PaperQA2
([skarlinski2024paperqa2](skarlinski2024paperqa2.md); slug
`paper-qa`) and reports +7% correctness; both catalog pages list the
other as related. The 45M-paper datastore is open-access only, which
bounds coverage for fields where much literature is paywalled.

Multi-agent structure / aggregation: the only structural mechanism the
abstract names is a "self-feedback inference loop" — an iterative
self-review loop within a single model rather than multi-agent
debate or parallel generation — and the abstract attributes
measurable gains to it jointly with the datastore and retriever,
which makes OpenScholar a data point on whether a review loop
improves epistemic quality without multiple agents, subject to the
caveat that the loop's isolated effect is not reported in the
abstract.

## Critique / open questions

- Benchmark and system come from the same team; absolute correctness
  levels and confidence intervals are not in the abstract.
- "On par with human experts" for citation accuracy is not
  quantified in the abstract.
- Preference near 50% for the 8B model against expert answers is
  reported as a positive; the abstract does not discuss what drove
  preferences (style, coverage, or accuracy).
- Domains are natural sciences and CS; no social-science or IS
  queries, so transfer to the curator's field is untested.
- Open-access-only datastore is a coverage limitation that the
  abstract states but does not discuss.
- The abstract concedes no limitations explicitly.

## Key quotes

> "We introduce OpenScholar, a specialized retrieval-augmented LM
> that answers scientific queries by identifying relevant passages
> from 45 million open-access papers and synthesizing citation-backed
> responses." (abstract)

> "While GPT4o hallucinates citations 78 to 90% of the time,
> OpenScholar achieves citation accuracy on par with human experts."
> (abstract)

> "In human evaluations, experts preferred OpenScholar-8B and
> OpenScholar-GPT4o responses over expert-written ones 51% and 70% of
> the time, respectively, compared to GPT4o's 32%." (abstract)
