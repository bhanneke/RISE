---
citekey: brincoveanu2026augmenting
title: "Augmenting Systematic Literature Reviews: A Human-AI Collaborative Framework"
authors:
  - "Brîncoveanu, Constantin"
  - "Carl, K Valerie"
  - "Witzki, Aaron"
  - "Hinz, Oliver"
year: 2026
venue: "conference"
doi: "10.1007/978-3-032-02813-6_1"
kind: "paper"
themes:
  - is-methodology
  - human-ai-research-collaboration
methods:
  - framework
relates_to_projects: []
status: "read"
---

## Summary
This paper proposes a novel framework for integrating Large Language Models (LLMs) and context engines into the traditional Systematic Literature Review (SLR) process. It addresses the scalability constraints of human-only reviews and the reliability/hallucination limits of AI-only approaches by structurally separating search, synthesis, and theoretical linking.

## Contribution
1. Introduces a methodology mirroring the Wolfswinkel grounded-theory SLR approach but augmented with a strict AI pipeline.
2. Formalizes a "Human-in-the-loop" vs "Agential Drift" boundary, ensuring theoretical validity is retained by human researchers while data processing is executed by agents.
3. Provides empirical/qualitative evaluations of AI impact on subjectivity/bias in Information Systems research.

## Method
The framework uses a phased approach anchored on Qualitative Content Analysis (Mayring/Schreier) replacing strict Gioia methodology. It involves scraping context, utilizing retrieval-augmented generation (RAG) to detect contradictions, and assigning AI personas for thematic synthesis before human review.

## Relevance to RISE
Highly relevant for agentic-research systems. It provides a formal methodological template for how automated research agents can review literature systematically (aligns with `literature-synthesis` and `literature-discovery`) without violating scientific rigor.

## Critique / open questions
The framework conceptually relies on the capability of the underlying LLM/context engine to accurately retrieve complex inter-document contradictions; performance may degrade rapidly if the underlying vector database architecture is poorly tuned.

## Key quotes
