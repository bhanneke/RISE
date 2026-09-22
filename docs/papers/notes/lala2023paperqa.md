---
citekey: lala2023paperqa
title: 'PaperQA: Retrieval-Augmented Generative Agent for Scientific Research'
authors:
- Lála, J.
- O'Donoghue, O.
- Shtedritski, A.
- Cox, S.
- Rodriques, S. G.
- White, A. D.
year: 2023
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2312.07559
kind: preprint
themes:
- hallucination
- agentic-tool-use
- evaluation-of-ai-research
methods:
- system-design
- benchmark-evaluation
- expert-comparison
relates_to_projects:
- paper-qa
status: skimmed
arxiv_id: '2312.07559'
---

## Summary

PaperQA is a retrieval-augmented generation (RAG) agent for answering
questions over the scientific literature. Motivated by LLM
hallucination and uninterpretability, the agent retrieves across
full-text scientific articles, assesses the relevance of sources and
passages, and generates answers with provenance via RAG. Evaluated as
a question-answering model, it is reported to exceed existing LLMs and
LLM agents on current science QA benchmarks. The authors also
introduce LitQA, a benchmark that requires retrieval and synthesis of
information from full-text papers across the literature, and report
that PaperQA matches expert human researchers on it. This is the
first-generation PaperQA paper (arXiv v2, December 2023); the catalog
entry `paper-qa` primarily describes its successor, PaperQA2.

## Contribution

Claimed: (i) a RAG agent that reduces hallucination and provides
provenance for answers; (ii) better performance than existing LLMs
and LLM agents on science QA benchmarks; (iii) the LitQA benchmark;
(iv) parity with expert human researchers on LitQA.

What the abstract supports: the system is described only at the level
of three capabilities (retrieval over full text, relevance assessment
of sources and passages, RAG answering). No benchmark names, sizes,
or margins are given, and "matches expert human researchers" is
asserted without numbers, the number of experts, or the task
conditions. The provenance/interpretability benefit is stated as a
motivation for RAG in general, not demonstrated as a measured
property of PaperQA in the abstract.

## Method

Design: an agent that (a) performs information retrieval across
full-text scientific articles, (b) assesses the relevance of
retrieved sources and passages, and (c) answers via RAG.

Evaluation: (1) existing science QA benchmarks (not named in the
abstract), where PaperQA is compared to "existing LLMs and LLM
agents"; (2) LitQA, a new benchmark described only as requiring
retrieval and synthesis from full-text papers across the literature;
(3) a comparison with expert human researchers on LitQA.

Not specified in the abstract: the underlying LLM(s), the corpus and
search back-end, the size and construction of LitQA, the number of
human experts and how they were recruited, the scoring protocol,
cost, and latency.

## Relevance to RISE

Informs the `literature-discovery` and `literature-synthesis` stages.
Catalog slug: `paper-qa`. This note is the origin paper for the
PaperQA line; the catalog's scoring (internal evaluation 3, runtime
assurance 3) rests mainly on the successor paper
[skarlinski2024paperqa2](skarlinski2024paperqa2.md). OpenScholar
([asai2024openscholar](asai2024openscholar.md)) later benchmarks
against PaperQA2, not against this version.

Multi-agent structure / aggregation: the abstract describes a single
agent whose only aggregation mechanism is relevance assessment of
retrieved sources and passages before answer generation — a filtering
step, not a multi-perspective, debate, or consensus structure.

## Critique / open questions

- The human-parity claim cannot be assessed from the abstract: no
  numbers, no sample size, no description of expert conditions.
- The "existing LLM agents" baselines are unnamed, so the size of the
  reported advantage is unknown.
- LitQA construction (who wrote the questions, which domains, whether
  contamination was controlled) is not described in the abstract.
- The abstract concedes only the general problem that motivates the
  work (LLM hallucination and uninterpretability); it names no
  PaperQA-specific limitations.
- Superseded by PaperQA2; readers should treat this note as
  provenance for the line rather than as the current evidence base.

## Key quotes

> "We present PaperQA, a RAG agent for answering questions over the
> scientific literature." (abstract)

> "PaperQA is an agent that performs information retrieval across
> full-text scientific articles, assesses the relevance of sources and
> passages, and uses RAG to provide answers." (abstract)

> "To push the field closer to how humans perform research on
> scientific literature, we also introduce LitQA, a more complex
> benchmark that requires retrieval and synthesis of information from
> full-text scientific papers across the literature." (abstract)
