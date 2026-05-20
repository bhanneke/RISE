---
citekey: ifargan2024datatopaper
title: Autonomous LLM-Driven Research --- from Data to Human-Verifiable Research Papers
authors:
- Ifargan, T.
- Hafner, L.
- Kern, M.
- Alcalay, O.
- Kishony, R.
year: 2024
venue: NEJM AI (arXiv 2404.17605)
doi: 10.1056/AIoa2400555
url: https://doi.org/10.1056/AIoa2400555
kind: paper
themes:
- agentic-pipelines
- traceability-verifiability
- end-to-end-research
methods:
- system-design
- case-studies
relates_to_projects: []
status: read
arxiv_id: '2404.17605'
---

## Summary

`data-to-paper` is an automation platform that guides interacting
LLM and rule-based agents through a complete 17-step research process
— data exploration, literature search, hypothesis formulation, plan
design, code writing/debugging, results interpretation, manuscript
drafting — while *programmatically back-tracing* the information flow
between data, methods, and results. The system supports
fixed/open-goal and copilot/autopilot modes. Two open-goal and two
fixed-goal case studies on public datasets evaluate the system's
ability to generate accurate, traceable manuscripts.

## Contribution

A concrete, transparent, traceable workflow that explicitly addresses
the emerging AI-in-science guidelines (accountability, oversight,
transparency). The system's *algorithmic chaining* of data → method
→ result is the key contribution — every claim in the output paper
can be programmatically traced back to the code that produced it.
For simple research goals the fully-autonomous mode produces
manuscripts "without major errors in about 80-90%" of runs; for
complex goals, human co-piloting becomes critical.

## Method

System paper with four case studies on public datasets, comparing
autopilot vs. copilot modes and open-goal vs. fixed-goal modalities.
Novelty and accuracy of the generated papers are evaluated through
manual inspection and (where applicable) recapitulation of known
peer-reviewed findings.

## Relevance to RISE

One of the cleanest existing examples of a *traceable* agentic
research pipeline — the property that "downstream results can be
traced back to the code that generated them" is exactly the
verifiability story that RISE positions as a sociotechnical
requirement. The 17-step decomposition is also useful as a reference
pipeline anatomy. Note: the published NEJM AI version is paywalled;
this entry's PDF is the arXiv preprint (2404.17605), which is
substantively identical.

## Critique / open questions

The 80-90% headline number applies to *simple* goals on tidy public
datasets; the paper concedes complex goals require co-piloting and
does not quantify how often. Novelty was "relatively limited" — the
generated insights recapitulated existing literature rather than
producing de novo contributions of independent scientific interest.
The four-case-study evaluation is small; generalisation to other
fields (beyond hypothesis-testing on tabular data) is open.

## Key quotes

> "Mimicking human scientific practices, we built data-to-paper, an
> automation platform that guides interacting LLM agents through a
> complete stepwise research process, while programmatically
> back-tracing information flow and allowing human oversight and
> interactions."

> "For simple research goals, a fully-autonomous cycle can create
> manuscripts which recapitulate peer-reviewed publications without
> major errors in about 80-90%, yet as goal complexity increases,
> human co-piloting becomes critical for assuring accuracy."

> "Beyond the process itself, created manuscripts too are inherently
> verifiable, as information-tracing allows to programmatically chain
> results, methods and data."
