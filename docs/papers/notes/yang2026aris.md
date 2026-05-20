---
citekey: yang2026aris
title: 'ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration'
authors:
- Yang, R.
- Li, Y.
- Li, S.
year: 2026
venue: arXiv 2605.03042 (Shanghai Jiao Tong University / Shanghai Innovation Institute, Tech Report)
doi: ''
url: https://arxiv.org/abs/2605.03042
kind: tech-report
themes:
- agentic-pipelines
- multi-agent-systems
- evaluation-rigor
- harness-engineering
methods:
- system-design
- deployment-experience
relates_to_projects:
- aris
status: read
arxiv_id: '2605.03042'
---

## Summary

ARIS is an open-source research harness for autonomous ML research,
built around the assumption that "any long-term task performed by a
single agent is unreliable." It coordinates research workflows through
*cross-family* adversarial collaboration: an executor model drives
forward progress while a reviewer drawn from a different model family
critiques intermediate artifacts and requests revisions. The system is
organised into three architectural layers — execution (65+ reusable
Markdown-defined skills, MCP integrations, persistent research wiki,
deterministic figure generation), orchestration (five end-to-end
workflows with adjustable effort settings and reviewer routing), and
assurance (claim auditing, mathematical-proof checks, scientific
editing pipeline, visual PDF inspection).

## Contribution

A concrete instantiation of *harness engineering* for autonomous ML
research that treats assurance as a first-class workflow layer rather
than a single review pass. The three named bottlenecks — persistent
research state, modular execution, independent assurance — are
presented as system-level consequences of the "single-agent
long-horizon research is unreliable" assumption, not as separate
desiderata bolted on after the fact. A prototype self-improvement loop
records research traces and proposes harness changes, gated by
reviewer approval.

## Method

System-design technical report with early deployment experience across
three executor platforms. No controlled benchmark study; the paper
documents architecture, assurance mechanisms, and qualitative
deployment observations rather than measured win-rates against
baselines.

## Relevance to RISE

ARIS is one of the most architecturally explicit recent agentic
research harnesses and shares the RISE perspective that workflow
*harness* (skills, state, review) matters as much as model weights.
The cross-family executor/reviewer pairing is a clean operational
answer to single-agent failure modes; the three-stage claim audit is a
useful template for evaluation rigor in RISE-style pipelines. ARIS is
also the canonical reference behind the `aris` skills pack bundled in
this KB.

## Critique / open questions

The "any long-term task by a single agent is unreliable" framing is
stated as an assumption rather than an empirical finding; the paper
acknowledges it may understate current single-agent capabilities and
prefers the strict version for high-rigor settings. The "more than 65
skills" and three-layer architecture are not yet evaluated against
ablations (e.g., what if assurance is removed? what if same-family
review is used?). Cross-family review introduces real coordination
cost; the trade-off vs. single-family pipelines is asserted but not
quantified.

## Key quotes

> "Any long-term task performed by a single agent is unreliable.
> We need to divide the total workflow into sub-workflows and
> cross-family models to review the output at each step independently."

> "The central failure mode is not visible breakdown but plausible
> unsupported success: a long-running agent can produce claims whose
> evidential support is incomplete, misreported, or silently inherited
> from the executor's framing."

> "We default to cross-family pairings because prior work suggests
> that mixed-model agent configurations can produce less correlated
> and more varied critiques … we adopt this as a recommended
> configuration rather than a hard system constraint."
