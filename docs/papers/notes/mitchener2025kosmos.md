---
citekey: mitchener2025kosmos
title: 'Kosmos: An AI Scientist for Autonomous Discovery'
authors:
- Mitchener, L.
- Yiu, A.
- Chang, B.
- Bourdenx, M.
- Nadolski, T.
- Sulovari, A.
- Landsness, E. C.
- Barabasi, D. L.
- Narayanan, S.
- Evans, N.
- et al.
year: 2025
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2511.02824
kind: preprint
themes:
- autonomous-research-agents
- hallucination
- research-productivity
- evaluation-of-ai-research
methods:
- system-design
- human-evaluation
- case-study
relates_to_projects:
- kosmos
status: skimmed
arxiv_id: '2511.02824'
---

## Summary

Kosmos is an AI scientist for data-driven discovery. Given an
open-ended objective and a dataset, it runs for up to 12 hours through
cycles of parallel data analysis, literature search, and hypothesis
generation, then synthesizes its findings into scientific reports. Its
distinguishing design is a structured world model shared between a
data-analysis agent and a literature-search agent, which the authors
credit with keeping the system coherent over 200 agent rollouts —
about 42,000 lines of code executed and 1,500 papers read per run.
Every statement in a report is cited to code or primary literature.
Independent scientists judged 79.4% of report statements accurate;
collaborators estimated that a 20-cycle run equals about six months of
their own research time and that valuable findings scale linearly with
cycles (tested up to 20). Seven discoveries across metabolomics,
materials science, neuroscience, and statistical genetics are
highlighted, three of which reproduce unpublished or preprinted
results not accessed at runtime.

## Contribution

Claimed: a system that overcomes the loss of coherence that limits
prior agents' action horizons, with traceable reasoning and genuine
discoveries. What the abstract supports: quantitative scale figures
and a statement-level accuracy rate from independent scientists; a
collaborator-reported productivity estimate and scaling claim; seven
case studies, three of which have the strongest evidence form in the
batch (blind reproduction of results the system could not have seen).
The "novel contributions" claim for the other four rests on the
authors' assessment; the abstract does not say how novelty was
verified.

## Method

Two-agent architecture plus shared world model. Evaluation combines
(i) statement-level accuracy scoring of reports by independent
scientists, (ii) collaborator self-reports of time saved and of
findings per cycle, and (iii) seven highlighted discoveries. The
abstract does not specify the number of independent scientists, the
number of reports or statements scored, how "accurate" was
operationalized, the number of runs behind the averages, the base
model(s), the content of the world model, how the seven discoveries
were selected from the total output, or the per-run cost.

## Relevance to RISE

Informs literature-discovery, literature-synthesis,
hypothesis-generation, data-analysis, code-generation, and
paper-drafting (report synthesis). The catalog slug `kosmos` refers to
the open-source jimmc414 reimplementation of this architecture, not to
the authors' own system; that page lists this paper as the source
design. The author list overlaps substantially with
[ghareeb2026robin](ghareeb2026robin.md) (Ghareeb, Laurent, Skarlinski,
Rodriques, Hinks, White appear on both), placing Kosmos in the
FutureHouse lineage; where Robin's evaluation is a wet-lab result,
Kosmos's is statement accuracy and collaborator assessment. For the
multi-agent structure/aggregation question: the abstract's
coordination mechanism is not debate, tournament, or review but a
shared structured world model between two specialized agents running
parallel cycles, with correctness checked post hoc by independent
scientists rather than by any in-pipeline adversarial or reviewer
role.

## Critique / open questions

A 79.4% accuracy rate means roughly one statement in five was judged
inaccurate in reports whose every statement is cited — citation
guarantees traceability, not correctness, and the abstract does not
say whether errors stem from faulty code, misread papers, or
unsupported inference. Time-saved and linear-scaling claims are
collaborator self-reports, and the abstract itself limits the scaling
claim to 20 cycles. The seven discoveries may be a selected subset of
many runs; no baseline (human analyst or prior system on the same
datasets) is mentioned. The kosmos catalog page attributes the paper
to "Lu et al."; the arXiv record lists Mitchener as first author.

## Key quotes

> "Unlike prior systems, Kosmos uses a structured world model to share
> information between a data analysis agent and a literature search
> agent." (abstract)

> "Independent scientists found 79.4% of statements in Kosmos reports
> to be accurate, and collaborators reported that a single 20-cycle
> Kosmos run performed the equivalent of 6 months of their own research
> time on average." (abstract)

> "Three discoveries independently reproduce findings from preprinted
> or unpublished manuscripts that were not accessed by Kosmos at
> runtime, while four make novel contributions to the scientific
> literature." (abstract)
