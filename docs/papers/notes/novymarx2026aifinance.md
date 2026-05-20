---
citekey: novymarx2026aifinance
title: AI-Powered (Finance) Scholarship
authors:
- Novy-Marx, R.
- Velikov, M. Z.
year: 2024
venue: NBER Working Paper 33363
doi: ''
url: https://www.nber.org/papers/w33363
kind: paper
themes:
- autonomous-research-agents
- research-productivity
- evaluation-of-ai-research
- hallucination
methods:
- empirical
- pipeline-demo
relates_to_projects:
- data-to-paper
- sakana-ai-scientist
- autoresearchclaw
status: read
---

## Summary

A demonstration that LLMs can be used to automatically generate
hundreds of complete academic finance papers on stock-return
predictability. The authors mine over 30,000 candidate predictor
signals from accounting data, run them through the Novy-Marx and
Velikov (2024) "Assaying Anomalies" protocol to identify 96 that
pass standardised criteria, generate template performance reports,
and then use state-of-the-art LLMs to produce three distinct
complete paper versions per signal — each with a different creative
name, custom introduction, theoretical justification, and citation
set.

## Contribution

Two contributions: a working LLM pipeline that turns a passing-signal
report into a fully written finance paper at scale, and a cautionary
demonstration of "industrialised HARKing" (Hypothesizing After Results
are Known) — including LLM-generated citations to "existing (and, on
occasion, imagined) literature." Companion artefacts (code, generated
papers, an AI-generated podcast) are released on GitHub.

## Method

Empirical pipeline demonstration: data mining + the Assaying Anomalies
protocol + LLM generation of multiple paper versions per surviving
signal.

## Relevance to RISE

A canonical "what could go wrong" reference for RISE: it shows that
end-to-end generation of plausible, well-formatted research papers is
already feasible in a structured domain, and that hallucinated
citations are a built-in failure mode. Directly relevant to RISE
catalog projects building end-to-end pipelines such as
[`data-to-paper`](../../projects/data-to-paper.md) and
[`sakana-ai-scientist`](../../projects/sakana-ai-scientist.md), and a
test case for the
[`autoresearchclaw`](../../projects/autoresearchclaw.md) evaluation
agenda.

## Critique / open questions

The pipeline is by construction post-hoc rationalisation of mined
signals; the paper itself frames this as a feature for the cautionary
argument rather than as a research-discovery system. No human-quality
or peer-review evaluation of the generated papers is reported in the
visible excerpt.

## Key quotes

> "This experiment illustrates AI's potential for enhancing financial
> research efficiency, but also serves as a cautionary tale,
> illustrating how it can be abused to industrialize HARKing
> (Hypothesizing After Results are Known)."

> "The different versions include creative names for the signals,
> contain custom introductions providing different theoretical
> justifications for the observed predictability patterns, and
> incorporate citations to existing (and, on occasion, imagined)
> literature supporting their respective claims."
