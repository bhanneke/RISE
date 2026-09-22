---
citekey: miao2026paper2agent
title: Reimagining research papers as interactive and reliable AI agents
authors:
- 'Miao, J.'
- 'Davis, J. R.'
- 'Zhang, Y.'
- 'Pritchard, J. K.'
- 'Zou, J.'
year: 2026
venue: Nature
doi: '10.1038/s41586-026-11044-y'
url: https://doi.org/10.1038/s41586-026-11044-y
kind: paper
themes:
- agentic-tool-use
- autonomous-research-agents
- replication-infrastructure
methods:
- system-design
- case-study
relates_to_projects: []
status: skimmed
---

## Summary

Paper2Agent is an automated framework that converts a research paper
into an AI agent. Rather than leaving a reader to understand and adapt
the paper's code, data and methods, the system analyses the paper and
its repository, builds a Model Context Protocol (MCP) server exposing
the manuscript, supplementary materials, datasets, code and workflows
as callable tools, and then iteratively tests the server to make it
robust. The resulting agent behaves as a "virtual corresponding
author": a coding agent such as Claude Code can invoke it in natural
language to run the paper's workflows. The authors demonstrate it on
AlphaGenome (genomic variant interpretation), TISSUE (spatial
transcriptomics) and Scanpy (single-cell analysis), reporting that the
agents reproduce the original papers' results and also answer new
questions — including an application to psoriasis.

## Contribution

Claimed: a paradigm shift for knowledge dissemination, turning the
paper from a passive artefact into an active system, and a route to
AI co-scientists. What the abstract supports: a working pipeline plus
three case studies where the generated agents reproduced original
results. The generalisation claim rests on those cases; no
cross-domain benchmark is reported in the abstract.

## Method

System paper with case studies. Pipeline: analyse paper and codebase →
extract tools and workflows → emit an MCP server → iterative testing
to harden it. Evaluation is by reproduction of the source papers'
results and by novel downstream questions. The abstract does not give
success rates across a corpus of papers, nor how often the extraction
step fails.

## Relevance to RISE

This is the first entry in the knowledge base that inverts the usual
direction of the pipeline. Everything else in the catalog consumes
literature (literature-discovery, literature-synthesis) or produces it
(paper-drafting); Paper2Agent makes an already-published paper
*executable*, which sits closest to `replication` and to the
reproducibility line represented by `reprorepo` and
`social-science-replicability`. It is arguably a landscape entry as
much as a paper — worth considering for `projects/landscape/` if the
code is public and maintained. For the RISE framing it also supplies a
concrete mechanism for the "Knowledge" side input: a paper-as-tool
rather than a paper-as-text.

## Critique / open questions

Three bioinformatics case studies is a narrow base for a claim about
knowledge dissemination generally; the method depends on the paper
having a working, well-structured repository, which is exactly what
most papers lack — the reproducibility literature in this KB
(`brodeur2025reproducibility`, `li2026reprorepo`) exists because code
artefacts are usually missing or broken. Whether an agent that
"reproduces the results" is checking the science or merely re-running
the authors' own code is the question the abstract does not address.

## Key quotes

> "Conventional research papers require readers to understand and
> adapt the paper's code, data and methods to their work, creating
> barriers to...". (abstract)

> "Paper2Agent addresses this challenge by converting a paper into an
> AI agent that functions as a virtual corresponding author, exposing
> its manuscript, supplementary materials, datasets, code and
> workflows as active, agent-native knowledge rather than static
> text." (abstract)
