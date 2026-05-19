---
citekey: matton2025walkthetalk
title: 'Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations'
authors:
  - 'Matton, K.'
  - 'Ness, R. O.'
  - 'Guttag, J.'
  - 'Kıcıman, E.'
year: 2025
venue: 'ICLR 2025'
doi: ""
url: ""
kind: paper
themes:
  - reasoning-faithfulness
  - hallucination
  - evaluation-of-ai-research
methods:
  - empirical
  - causal-inference
  - benchmark
relates_to_projects:
  - reviewer
  - sakana-ai-scientist
status: read
---

## Summary

An ICLR 2025 paper proposing a new method for measuring whether LLM
explanations are *faithful* — i.e. whether the concepts the
explanation cites as influential actually are influential in the
model's behaviour. The authors give a rigorous definition of
faithfulness in terms of the difference between the set of concepts
the explanation implies are influential and the set that truly are,
and present a method that uses (1) an auxiliary LLM to construct
realistic counterfactuals by modifying concept values in the input,
and (2) a Bayesian hierarchical model to quantify per-concept causal
effects at example and dataset level.

## Contribution

Two contributions: a formal definition of LLM explanation faithfulness
in terms of concept-level causal effects, and a counterfactual +
Bayesian-hierarchical estimation method that operationalises it.
Applied to a social-bias hiring task, it uncovers cases where LLM
explanations cite age, traits and skills but hide the influence of
gender; applied to medical QA, it uncovers misleading attributions
about which evidence drove the answer.

## Method

Causal/counterfactual evaluation pipeline: LLM-generated
counterfactual inputs + Bayesian hierarchical model of causal effects
at example and dataset level; applied to social-bias and medical-QA
benchmarks.

## Relevance to RISE

Provides a deployable instrument for the *reasoning-faithfulness*
pillar of RISE. Any pipeline that surfaces an LLM's stated reasons
(e.g. an autonomous reviewer system like
[`reviewer`](../../projects/reviewer.md) or an autonomous scientist
like [`sakana-ai-scientist`](../../projects/sakana-ai-scientist.md))
can use this method to audit when those stated reasons are misleading,
complementing the related findings of [@chen2025reasoning].

## Critique / open questions

Counterfactuals are themselves LLM-generated, which can introduce
artefacts; the method is demonstrated on two tasks (social bias,
medical QA) and its applicability to long-form research-style
explanations needs separate evaluation. Bayesian hierarchical
estimation may be expensive to scale across many dataset items.

## Key quotes

> "We define faithfulness in terms of the difference between the set
> of concepts that LLM explanations imply are influential and the set
> that truly are."

> "On a social bias task, we uncover cases where LLM explanations
> hide the influence of social bias."
