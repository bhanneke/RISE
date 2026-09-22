---
citekey: wang2026aarribench
title: 'Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and
  Agentic Harnesses in Research Lifecycle'
authors:
- Wang, J.
- Lv, W.
- Fu, B.
- Fu, J.
- Song, J.
- Zhang, L.
- Xue, L.
- Chen, L.
- Xin, Z.
- Li, K.
- Cao, X.
year: 2026
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2606.07462
kind: preprint
themes:
- evaluation-of-ai-research
- autonomous-research-agents
- agentic-reasoning
methods:
- benchmark-design
- benchmark-evaluation
relates_to_projects:
- aarri-bench
status: skimmed
arxiv_id: '2606.07462'
---

## Summary

The paper conceptualizes AARR (Act As a Real Researcher), a benchmark
series that asks not whether agents can execute research tasks at the
macro level but whether they show the professionalism, thoroughness and
nuanced reasoning of human researchers in granular research scenarios.
The motivation is that agents, despite strong long-horizon coding and
autonomous experiment execution, still show limits in field
sensitivity, research ethics and scientific judgment. The first
instance, AARRI-Bench (Act As a Real Research Intern), is evaluated
across frontier models and agentic systems. The best configuration,
Mini-SWE-Agent with Claude Opus 4.7, reaches a 68.3% success rate and
frequently overlooks subtle details that are obvious to human
researchers. The authors conclude that researcher-like AI requires
study of research behavior rather than more complex scaffolding. Data
are released on GitHub.

## Contribution

Claimed: a new benchmark family targeting micro-level research
judgment, its first instantiation, and a diagnostic finding about
where frontier agents fail. What the abstract supports: the 68.3%
figure for one configuration and the qualitative failure description.
The conclusion that "complex scaffolding" is not the path to
researcher-like AI is asserted; the abstract reports no ablation that
isolates scaffolding from model capability, so this reads as
interpretation rather than demonstrated result.

## Method

As far as the abstract states: experiments across frontier models and
agentic systems on granular research scenarios, scored by success rate.
The abstract does not give the number of scenarios, the domains they
cover, how scenarios were authored, how success is verified, which
configurations other than the best were tested, how many runs underlie
the 68.3%, or any human success rate against which "obvious to real
human researchers" could be quantified. The catalog entry (scored from
the repository and paper) records 82 containerized scenarios in Harbor
task format with assertion-based verifiers; none of this is in the
abstract. arXiv v1 only, no comments or journal reference.

## Relevance to RISE

Because the scenarios probe judgment across research situations rather
than one stage, the catalog tags it with `hypothesis-generation`,
`literature-synthesis`, `research-design`, `data-analysis`,
`code-generation` and `revision-editing`. Catalog slug:
[`aarri-bench`](../../projects/aarri-bench.md). Its own framing —
"unlike existing benchmarks that primarily assess macro-level execution
capabilities" — positions it as a complement to execution-anchored
suites such as [`airs-bench`](../../projects/airs-bench.md) and
[`mlgym`](../../projects/mlgym.md), which the catalog also lists as
related. For the ISR question of how multi-agent structure shapes
epistemic quality, the abstract's claim that better scaffolding is not
sufficient is a direct, if unproven, challenge to the premise that
structure improves quality; the benchmark's granular judgment scenarios
could serve as a fine-grained outcome measure for testing whether
review loops or adversarial roles reduce the "overlooked subtle detail"
failure mode the abstract identifies.

## Critique / open questions

From the abstract one cannot assess scenario validity, verifier
reliability, whether a 68.3% success rate is one run or averaged, or
whether the scenarios could be contaminated. "Research ethics" and
"field sensitivity" are named as deficits but not operationalized in
the abstract. Only the first of a planned series exists; the later
stages the catalog entry mentions (AARRA, AARRS) are announcements, not
deliverables. The abstract concedes that agents "remain unable to fully
replace human researchers" but frames this as the benchmark's
motivation rather than as a limitation of the work. The catalog entry
notes no license file at scoring date.

## Key quotes

> "Unlike existing benchmarks that primarily assess macro-level
> execution capabilities, AARR focuses on whether agents can emulate the
> professionalism, thoroughness, and nuanced reasoning that characterize
> human researchers in granular research scenarios." (abstract)

> "We conduct extensive experiments across frontier models and agentic
> systems, revealing that even the best-performing configuration
> (Mini-SWE-Agent with Claude Opus 4.7) achieves only 68.3% success
> rate, frequently overlooking subtle yet critical details that are
> obvious to real human researchers." (abstract)

> "Our results indicate that developing researcher-like AI requires
> further exploration of research behavior, rather than merely complex
> scaffolding." (abstract)
