---
citekey: wu2025agenticreasoning
title: 'Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with
  Agentic Tools'
authors:
- Wu, J.
- et al.
year: 2025
venue: 'ACL (Proceedings, Volume 1: Long Papers)'
doi: ''
url: ''
kind: paper
themes:
- agentic-reasoning
- agentic-tool-use
methods:
- framework
- benchmark
relates_to_projects:
- e2er
- sakana-ai-scientist
status: read
rating: 4
---

## Summary

Wu et al. introduce a streamlined framework for "agentic reasoning"
in which an LLM is augmented with a small set of orchestrated tools
(search, code execution, structured memory) and an explicit
plan-then-act loop. They argue that careful tool composition — rather
than ever-larger models or longer chains of thought — accounts for
most observed gains in reasoning benchmarks.

## Contribution

A minimal, well-specified template for agentic reasoning that separates
*planning*, *tool invocation*, and *reflection* as distinct steps with
clean interfaces, plus empirical evidence that this template captures
much of the benefit of more elaborate multi-agent systems on standard
reasoning benchmarks.

## Method

Framework paper accompanied by benchmark evaluations on standard
reasoning datasets. The authors compare their streamlined design to
both vanilla chain-of-thought and more complex multi-agent baselines,
controlling for model and tool budget.

## Relevance to RISE

This paper supplies a canonical reference for the **agentic-reasoning**
primitive that sits inside the Knowledge-Production block of the RISE
diagram. Most RISE projects in the catalog (notably `e2er` and
`sakana-ai-scientist`) implement some variant of plan-act-reflect on
top of tool-augmented LLMs; Wu et al.'s framework is a natural
reference design against which those implementations can be compared.

## Critique / open questions

- The reported benchmark gains are sensitive to tool choice; it is
  unclear how much of the framework generalizes outside coding and
  short-form QA.
- The paper does not discuss artifact persistence or replication, which
  are central concerns for RISE pipelines but tangential to reasoning
  benchmarks.
- The framework treats tools as black boxes; failure modes specific to
  scientific tools (data-source rate limits, citation drift) are not
  addressed.
