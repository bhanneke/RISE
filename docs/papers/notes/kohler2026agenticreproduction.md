---
citekey: kohler2026agenticreproduction
title: 'Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results'
authors:
- Kohler, B.
- Zollikofer, D.
- Einsiedler, J.
- Hoyle, A.
- Ash, E.
year: 2026
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2604.21965
kind: preprint
themes:
- replication-infrastructure
- evaluation-of-ai-research
methods:
- system-design
- benchmark-evaluation
- error-attribution
relates_to_projects:
- social-science-replicability
status: skimmed
arxiv_id: '2604.21965'
---

## Summary

The paper asks whether LLM agents can reproduce empirical
social-science results when given only a paper's methods description
and the original data, rather than the data plus the original code
as in prior work. The authors build an agentic reproduction system
that extracts structured methods descriptions from papers, runs
reimplementations under strict information isolation (agents never
see the original code, results, or paper), and compares reproduced
outputs to the originals deterministically at the level of individual
table cells. An error-attribution step traces discrepancies through
the system chain to root causes. Evaluating four agent scaffolds and
four LLMs on 48 papers with human-verified reproducibility, they find
agents can largely recover published results, with substantial
variation across models, scaffolds and papers; failures stem both
from agent errors and from underspecification in the papers. Single
arXiv version (Apr 2026).

## Contribution

Claimed: broadening agentic reproduction from "data plus code" to
"methods plus data", with isolation, cell-level comparison and root
cause attribution. What the abstract supports: the design and the
headline finding. It gives no recovery rates, no breakdown of
agent-error versus paper-underspecification failures, and no
statement of which scaffold or model performed best, so the
magnitude of "largely recover" and "varies substantially" cannot be
read off the abstract.

## Method

48 social-science papers whose reproducibility was previously
verified by humans; a 4 scaffold by 4 LLM design; deterministic
cell-level comparison; error attribution through the system chain.
The abstract does not specify which scaffolds or LLMs, the
disciplines within social science, the tolerance for a cell match,
whether the methods-description extractor is an LLM or a human, how
isolation is staged given that extraction must read the paper, or
where the data come from.

## Relevance to RISE

Informs replication, data-acquisition, data-analysis and
code-generation, matching the catalog entry
`social-science-replicability`. Note that the catalog page's
internal-evaluation note ("demonstrated on example papers; no broad
benchmark of replication success rates") is narrower than what the
abstract reports, namely a 48-paper, sixteen-configuration
evaluation; the catalog score may predate the paper. Relative to
`reprorepo` ([li2026reprorepo](li2026reprorepo.md)) the axes are
complementary: ReproRepo audits paper–repository pairs statically
against human-reported issues, whereas this system executes
reimplementations and checks numbers. Relative to `paper2code`
([seo2025paper2code](seo2025paper2code.md)), paper-to-code is a
shared sub-task, but here success is judged by matching the published
results rather than by implementation faithfulness. For the ISR
question on multi-agent structure, the abstract describes a staged
single-pipeline "system chain" (extraction, isolated reimplementation,
comparison, attribution) rather than multi-agent review or consensus;
its scaffold-by-model design is nonetheless direct evidence that
agent structure affects epistemic outcomes independently of the
underlying model.

## Critique / open questions

The abstract does not allow assessment of absolute recovery rates,
of whether failures on underspecified papers can be detected without
a ground truth (the in-the-wild use case), of how the 48 papers were
selected (human-verified reproducibility may favour easier cases), or
of the data-preparation effort required. The abstract concedes that
performance varies substantially between models, scaffolds and
papers, and that underspecification in the papers themselves is a
root cause of failure. Author-name spelling differs between the arXiv
record ("Benjamin Kohler", "Johanna Einsiedler") and the catalog page
("Köhler", "Einsiedler, A.").

## Key quotes

> "We broaden this scope by asking: Can they reproduce results given
> only a paper's methods description and original data?" (abstract)

> "We develop an agentic reproduction system that extracts structured
> methods descriptions from papers, runs reimplementations under
> strict information isolation -- agents never see the original code,
> results, or paper -- and enables deterministic, cell-level
> comparison of reproduced outputs to the original results."
> (abstract)

> "Root cause analysis reveals that failures stem both from agent
> errors and from underspecification in the papers themselves."
> (abstract)
