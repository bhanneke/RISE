---
citekey: li2026reprorepo
title: 'ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues'
authors:
- Li, S.
- Wei, Q. A.
- Tang, J.
- Chen, V.
- Shah, N. B.
- Dettmers, T.
- Yang, Y.
- Talwalkar, A.
year: 2026
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2606.18237
kind: preprint
themes:
- replication-infrastructure
- evaluation-of-ai-research
methods:
- benchmark-construction
- benchmark-evaluation
relates_to_projects:
- reprorepo
status: skimmed
arxiv_id: '2606.18237'
---

## Summary

ReproRepo is a framework for evaluating LLM agents as reproducibility
auditors. Rather than curating reproduction tasks by hand, it uses
human-raised GitHub issues as naturally occurring supervision on
realistic reproduction blockers. The authors instantiate it on 1,149
recent machine-learning papers from major conferences and evaluate
four frontier model-agent configurations. They find that agents can
identify many real-world reproducibility problems from
paper–repository pairs without executing any code: the best
configuration, Codex with GPT-5.5, surfaces at least one semantically
related human-reported blocker for about 90% of papers. Agents are
particularly good at surfacing visible failures and locating the
right semantic region, but often fall short of exact localisation.
The framework is positioned as reusable and scalable; code is
released. Single arXiv version (June 2026).

## Contribution

Claimed: a scalable, reusable reproducibility-audit framework that
sidesteps manual curation and evaluation. What the abstract supports:
the scale (1,149 papers) and the headline figure. Note that the ~90%
criterion is "at least one semantically related" blocker per paper,
a lenient recall-style measure; the abstract says nothing about
precision or false alarms, so the practical value of the audits
cannot be judged from it.

## Method

Benchmark construction from paper–repository pairs plus GitHub
issues; static audits by four agent configurations with no code
execution; scoring of agent findings against hidden human-reported
blockers. The abstract does not specify how semantic relatedness is
judged (LLM judge or human), which the other three configurations
are, per-issue recall, false-positive rates, which conferences or
years, or how issues were filtered for reproducibility relevance. The
catalog entry records LLM-based issue review, pinned snapshots and a
blind protocol; those details are not in the abstract.

## Relevance to RISE

Informs replication, matching the catalog entry `reprorepo`, which
files it in the evaluation-infrastructure layer (lifecycle coverage
0: it audits scholarship rather than producing it). Relative to
`social-science-replicability`
([kohler2026agenticreproduction](kohler2026agenticreproduction.md))
the two are complementary: ReproRepo predicts blockers statically
against a crowd signal, Kohler et al. execute reimplementations and
compare numbers. Relative to `paper2code`
([seo2025paper2code](seo2025paper2code.md)), ReproRepo evaluates
agents that read an existing paper and repository, whereas PaperCoder
writes the repository. The abstract's finding that non-executing
audits already surface a large share of reported blockers is
relevant to any RISE harness that wants a cheap pre-execution
replication check. For the ISR question on multi-agent structure, the
abstract describes single-agent audits with no multi-agent review or
aggregation; its epistemic reference point is instead a crowd-sourced
signal (human-reported issues), which is itself an aggregation of
community judgment with known coverage limits.

## Critique / open questions

The abstract does not allow assessment of precision, of how generous
"semantically related" is, or of contamination: the issues are
public, and the abstract does not say whether snapshots predate the
evaluated models' training data. The abstract concedes that agents
"may still be insufficient in exact localization". The catalog adds
that only blockers someone chose to report are visible to the
benchmark, that runtime-only failures are out of scope, and that only
aggregate result tables are released.

## Key quotes

> "We introduce ReproRepo, a scalable framework for reproducibility
> evaluation that leverages human-raised GitHub issues as naturally
> occurring supervision on realistic reproduction blockers."
> (abstract)

> "Our results show that LLM agents, even without executing code, can
> identify many real-world reproducibility problems from
> paper-repository pairs: the best agent in our study, namely Codex
> with GPT-5.5, surfaces at least one semantically related
> human-reported blocker for ~90% of papers in the study." (abstract)

> "Further analysis shows that agents are particularly effective for
> surfacing visible failures and identifying the right semantic
> region, but may still be insufficient in exact localization."
> (abstract)
