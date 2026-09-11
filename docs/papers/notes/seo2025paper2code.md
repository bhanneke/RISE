---
citekey: seo2025paper2code
title: 'Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning'
authors:
- Seo, M.
- Baek, J.
- Lee, S.
- Hwang, S. J.
year: 2025
venue: ICLR 2026 (arXiv 2504.17192)
doi: ''
url: https://arxiv.org/abs/2504.17192
kind: paper
themes:
- replication-infrastructure
- autonomous-research-agents
methods:
- system-design
- benchmark-evaluation
- human-evaluation
relates_to_projects:
- paper2code
status: skimmed
arxiv_id: '2504.17192'
---

## Summary

PaperCoder is a multi-agent LLM framework that turns a machine-learning
paper into an operational code repository. It works in three stages:
planning (a high-level roadmap, a system architecture with diagrams,
file dependencies and configuration files), analysis (interpreting
implementation-specific details), and generation (modular,
dependency-aware code). Each stage is carried out by a set of
specialised agents. The authors evaluate generated implementations
with model-based and human judgments, notably from the original
authors of the source papers, using author-released repositories as
ground truth where they exist, and report that PaperCoder produces
high-quality, faithful implementations and outperforms strong
baselines by substantial margins on the PaperBench benchmark. Code is
public. Accepted at ICLR 2026 (arXiv v5, Feb 2026).

## Contribution

Claimed: a paper-to-repository pipeline that yields faithful
implementations and beats strong baselines on the authors' own
evaluation and on PaperBench. What the abstract supports: the
three-stage multi-agent design and the evaluation protocol. No
numbers are given in the abstract; "faithful" is as judged by
model-based and author evaluation, not by reproducing the papers'
reported results. The catalog entry records that the project also
ships its own benchmark datasets, which the abstract does not
mention.

## Method

Multi-agent pipeline with stage-specific agents. Evaluation:
model-based scoring, human scoring by the papers' authors, comparison
to author-released repositories where available, and PaperBench. The
abstract does not specify the number of papers, which LLMs back the
agents, how faithfulness is scored, whether or how often generated
code executes, whether generated code reproduces the papers' numbers,
cost per paper, or which baselines were compared. The catalog
entry records roughly $0.50–0.70 per run with o3-mini; that figure is
not in the abstract.

## Relevance to RISE

Informs replication, code-generation and research-design, matching
the catalog entry `paper2code`. It complements
`social-science-replicability`
([kohler2026agenticreproduction](kohler2026agenticreproduction.md)),
where agents reproduce published numbers from a methods description
and the original data under information isolation: PaperCoder's
target is the code artifact judged for implementation faithfulness,
Kohler et al.'s target is the reproduced result judged cell by cell,
and the domains differ (ML vs. social science). It also complements
`reprorepo` ([li2026reprorepo](li2026reprorepo.md)), which audits
existing paper–repository pairs, whereas PaperCoder creates the
repository when none exists. For the ISR question on multi-agent
structure, the abstract describes a division of labour by stage,
with specialised agents "designed to collaborate effectively across
the pipeline", but no review, critique or consensus mechanism among
agents; epistemic checks are external (author evaluation, PaperBench)
rather than structural.

## Critique / open questions

The abstract does not allow assessment of how often generated
repositories run, whether they reproduce reported results, or whether
the source papers (those with public repositories in particular) were
in the LLMs' training data. Author evaluation has an unknown sample
size and unknown leniency. The abstract concedes that ground truth is
available only "if available", so part of the evaluation lacks a
reference repository. The catalog adds that portability to empirical
economics or biomedical papers is untested and that faithfulness
depends on PDF/LaTeX parsing quality.

## Key quotes

> "Inspired by this, we introduce PaperCoder, a multi-agent LLM
> framework that transforms machine learning papers into operational
> code repositories." (abstract)

> "Moreover, each phase is instantiated through a set of specialized
> agents designed to collaborate effectively across the pipeline."
> (abstract)

> "We then evaluate PaperCoder on generating code implementations
> from machine learning papers based on both model-based and human
> evaluations, particularly from the authors of those papers, with
> author-released repositories as ground truth if available."
> (abstract)
