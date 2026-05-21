---
citekey: ghareeb2026robin
title: A Multi-Agent System for Automating Scientific Discovery
authors:
- Ghareeb, A. E.
- Chang, B.
- Mitchener, L.
- Yiu, A.
- Szostkiewicz, C. J.
- Shved, D.
- Gyimesi, G. J.
- Laurent, J. M.
- Wright, S. M.
- Razzak, M. T.
- White, A. D.
- Finnemann, S. C.
- Hinks, M. M.
- Rodriques, S. G.
year: 2026
venue: Nature (arXiv 2505.13400)
doi: 10.1038/s41586-026-10652-y
url: https://arxiv.org/abs/2505.13400
kind: paper
themes:
- agentic-pipelines
- multi-agent-systems
- autonomous-research-agents
- end-to-end-research
methods:
- system-design
- lab-in-the-loop
- wet-lab-validation
relates_to_projects: []
status: read
arxiv_id: '2505.13400'
---

## Summary

Robin is a multi-agent system from FutureHouse that integrates
literature-search agents with data-analysis agents to run the full
hypothesis → experiment-proposal → result-interpretation →
revised-hypothesis loop. The system was deployed on a real
biomedical problem — dry age-related macular degeneration (dAMD), the
leading cause of blindness in the developed world — and *autonomously*
proposed enhancing retinal pigment epithelium (RPE) phagocytosis as a
therapeutic strategy. Robin then identified and validated **ripasudil**
(a clinically-used ROCK inhibitor never previously proposed for dAMD)
as a promising candidate, and proposed a follow-up RNA-seq experiment
that revealed ABCA1 upregulation as a possible novel target.

## Contribution

The first reported AI system to autonomously discover *and* wet-lab
validate a novel therapeutic candidate within an iterative
lab-in-the-loop framework. All hypotheses, experimental plans, data
analyses, and figures in the main text were produced by Robin —
humans executed the bench experiments, but the intellectual loop is
end-to-end automated. This goes beyond prior AI-scientist systems
(AI Scientist, EvoScientist, ARIS, data-to-paper) which automate the
*writing* of a research paper but stop short of generating a validated
biomedical discovery.

## Method

System paper with a single, deep biomedical case study. Authors built
a multi-agent harness combining literature-search and data-analysis
roles; deployed it on the dAMD problem; performed the proposed
wet-lab experiments; iterated. Evaluation is by the scientific
outcome itself (a novel, mechanistically-validated drug candidate)
rather than by benchmark metrics.

## Relevance to RISE

Among the most important recent agentic-research-pipeline papers for
the RISE catalog. Distinguishing features vs. other end-to-end AI
scientists in the catalog:

- **Lab-in-the-loop validation.** Where [yang2026aris](yang2026aris.md),
  [evoscientist2026techreport](evoscientist2026techreport.md), and
  [ifargan2024datatopaper](ifargan2024datatopaper.md) validate against
  benchmarks or recapitulate known findings, Robin validates against
  reality (a wet-lab assay).
- **Discovery as the evaluation criterion.** The system is evaluated
  by whether it produced a novel, real, mechanistically-grounded
  therapeutic candidate — a much harder bar than "novelty score from
  an LLM judge".
- **Sociotechnical implications.** A concrete, peer-reviewed
  (Nature) demonstration that the agentic-discovery thread can produce
  outcomes that matter outside the AI literature itself. Useful for
  the introduction of the RISE position paper.

## Critique / open questions

A single case study — the result is striking but generalisability to
other biomedical (or non-biomedical) discovery problems is open.
Lab-in-the-loop is *semi-*autonomous: humans still run the wet
experiments, set up the assays, and presumably curate the candidate
list at decision points. The paper does not report how many
ripasudil-class false positives Robin generated before this one was
validated — a base-rate analysis would be needed to compare against
domain experts on the same task. The "all hypotheses and figures
produced by Robin" claim is strong; readers should look at the
methods carefully to understand exactly which decision points
involved human input.

## Key quotes

> "Here, we introduce Robin, the first multi-agent system capable of
> fully automating the key intellectual steps of the scientific
> process. By integrating literature search agents with data analysis
> agents, Robin can generate hypotheses, propose experiments,
> interpret experimental results, and generate updated hypotheses,
> achieving a semi-autonomous approach to scientific discovery."

> "By applying this system, we were able to identify a novel treatment
> for dry age-related macular degeneration (dAMD), the major cause of
> blindness in the developed world. Robin proposed enhancing retinal
> pigment epithelium phagocytosis as a therapeutic strategy, and
> identified and validated a promising therapeutic candidate,
> ripasudil."

> "As the first AI system to autonomously discover and validate a
> novel therapeutic candidate within an iterative lab-in-the-loop
> framework, Robin establishes a new paradigm for AI-driven scientific
> discovery."
