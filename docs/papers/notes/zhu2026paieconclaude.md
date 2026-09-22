---
citekey: zhu2026paieconclaude
title: 'pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development'
authors:
- 'Zhu, C.'
- 'Wang, X.'
- 'Zhang, W.'
year: 2026
venue: 'arXiv preprint'
doi: ''
url: https://arxiv.org/abs/2607.21268
kind: preprint
themes:
- human-ai-research-collaboration
- autonomous-research-agents
methods:
- system-design
- blinded-evaluation
relates_to_projects:
- pai-econ-claude
status: skimmed
arxiv_id: '2607.21268'
---

## Summary

Companion paper to the pAI-Econ-claude Claude Code Skill. Its framing:
in social-science tasks like economic theory, LLM agents must produce
outputs for which no cheap, task-complete, machine-readable
correctness signal exists — so how should generation, critique,
coordination, and human judgment be organized when no component can
certify the final result? The architecture answers with a shared
workspace of inspectable intermediate records, specialized gates that
diagnose targeted failure modes and recommend loopbacks *without*
certifying correctness, and human checkpoints holding authority over
decisions that are costly to reverse. Evaluated on five matched
economic-theory tasks against an ungated baseline: two
configuration-blinded evaluators agreed on all five pairwise rankings,
preferring the gated architecture in four; mean failure severity fell
from 1.58 to 1.16 and usefulness rose from 2.60 to 3.10.

## Contribution

Claimed: gated oversight improves auditability of AI-assisted economic
theory without substituting for formal verification, and — the
explicitly "bounded claim" — the allocation of irreversible human
judgment is a more informative design variable than pure agent
autonomy. Supported: a small (n=5) but blinded and honestly reported
comparison, including the negative case where scaffolding compressed
an economically important mechanism too aggressively.

## Method

Design-science-style system paper with a five-task matched comparison,
two blinded evaluators, severity and usefulness scales. The abstract
does not state who the evaluators were, how tasks were selected, or
the variance around the mean scores.

## Relevance to RISE

Catalog slug `pai-econ-claude` (formal-modeling; sits beside
theorist-toolbox in the economic-theory-agent niche). For the
*Architecture as Epistemology* paper this is the closest neighbor in
the catalog: it treats the organization of critique and the placement
of human judgment as the design variable of a MAS operating exactly
where no verifier exists — the no-machine-checkable-signal regime that
the ISR paper's forecasting task deliberately avoids by using resolved
outcomes. The two designs bracket the verification spectrum.

## Critique / open questions

Five tasks and two evaluators is a pilot-scale evidence base, and the
evaluation is by the system's own team. "Failure severity" and
"usefulness" scales are not externally anchored. The single-model,
single-platform design (Claude Code) means gate quality and generator
quality share one model family's blind spots — the same correlated-
error concern the catalog raises for other single-family systems.

## Key quotes

> "This creates a distinctive reliability problem for multi-agent
> systems: how should generation, critique, coordination, and human
> judgment be organized when no component can certify the final
> result?" (abstract)

> "Mean failure severity fell from 1.58 to 1.16, while overall
> usefulness rose from 2.60 to 3.10." (abstract)

> "The results support a bounded claim: gated oversight improves the
> auditability of AI-assisted economic theory without substituting for
> formal verification, and the allocation of irreversible human
> judgment is a more informative design variable than pure agent
> autonomy." (abstract)
