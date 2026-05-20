---
citekey: collu2025misleading
title: Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing
  via Hidden Prompt-Injection Attacks
authors:
- Collu, M. G.
- Salviati, U.
- Confalonieri, R.
- Conti, M.
- Apruzzese, G.
year: 2026
venue: arXiv:2508.20863
doi: ''
url: https://arxiv.org/abs/2508.20863
kind: paper
themes:
- ai-peer-review
- hallucination
- sociotechnical
methods:
- empirical
- experimental
relates_to_projects:
- reviewer
- marg
- ape
status: read
arxiv_id: '2508.20863'
---

## Summary

The authors investigate hidden prompt-injection attacks in which paper authors embed adversarial text inside a PDF that remains invisible to human readers but is parsed and acted upon by LLM-based reviewers. They formalise three threat models with distinct attacker motivations (not all malicious), design corresponding invisible prompts, and derive four representative reviewing prompts from a user study with domain scholars. They then evaluate the robustness of the adversarial prompts across reviewing prompts, several commercial LLM systems, and multiple peer-reviewed papers.

## Contribution

A formal threat-model taxonomy for adversarial manipulation of LLM peer reviewers, a paired user study to elicit realistic reviewing prompts, an empirical demonstration that hidden prompt injections can reliably steer LLM-generated reviews, and an evaluation of methods to make adversarial prompts harder to detect by automated content checks.

## Method

Three formalised threat models map to designed adversarial prompts; a user study with domain scholars yields four representative reviewing prompts; robustness is evaluated by crossing reviewing prompts x commercial LLM systems x peer-reviewed papers. Detectability under automated content checks is empirically measured for several stealth strategies.

## Relevance to RISE

Defines an explicit attack surface for any RISE catalog project that uses LLMs in the reviewing loop, including [`reviewer`](../../projects/reviewer.md), [`marg`](../../projects/marg.md), and [`ape`](../../projects/ape.md). Together with keuper2025promptinjection and the prevalence findings of liang2024monitoring, it forces evaluation-of-ai-research and ai-peer-review designs to include adversarial-robustness criteria and PDF-content sanitisation as first-class requirements.

## Critique / open questions

The "honest-but-lazy" reviewer assumption may understate or overstate real reviewer behaviour, and effectiveness against future LLMs with prompt-injection defences is not guaranteed. The evaluation focuses on commercial systems whose internal safety layers are opaque.

## Key quotes

> "We investigate the potential for hidden prompt injection attacks, where authors embed adversarial text within a paper's PDF to influence the LLM-generated review."

> "We begin by formalising three distinct threat models that envision attackers with different motivations—not all of which implying malicious intent."

> "Our results show that adversarial prompts can reliably mislead the LLM, sometimes in ways that adversely affect a 'honest-but-lazy' reviewer. Finally, we propose and empirically assess methods to reduce detectability of adversarial prompts under automated content checks."
