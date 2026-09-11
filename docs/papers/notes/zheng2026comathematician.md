---
citekey: zheng2026comathematician
title: 'AI co-mathematician: Accelerating mathematicians with agentic AI'
authors:
- Zheng, D.
- von Glehn, I.
- Zwols, Y.
- Beloshapka, I.
- Buesing, L.
- Roy, D. M.
- Wattenberg, M.
- Georgiev, B.
- Schmidt, T.
- Cowie, A.
- et al.
year: 2026
venue: arXiv preprint (Google DeepMind)
doi: ''
url: https://arxiv.org/abs/2605.06651
kind: preprint
themes:
- human-ai-research-collaboration
- autonomous-research-agents
- agentic-tool-use
methods:
- system-design
- case-study
- benchmark-evaluation
relates_to_projects:
- ai-co-mathematician
status: skimmed
arxiv_id: '2605.06651'
---

## Summary

The AI co-mathematician is a Google DeepMind workbench through which
mathematicians interactively use AI agents for open-ended research. It
is designed to support the exploratory, iterative reality of
mathematical work — ideation, literature search, computational
exploration, theorem proving and theory building — through an
asynchronous, stateful workspace that manages uncertainty, refines the
user's intent, tracks failed hypotheses and outputs native mathematical
artifacts, thereby mirroring human collaborative workflows. In early
tests the system helped researchers solve open problems, identify new
directions and recover overlooked literature references. It also
reports state-of-the-art results on hard problem-solving benchmarks,
including 48% on FrontierMath Tier 4, which the authors describe as a
new high among all AI systems evaluated.

## Contribution

Claimed: a highly interactive paradigm for AI-assisted mathematical
discovery, plus benchmark leadership. What the abstract supports: the
48% FrontierMath Tier 4 figure and a qualitative account of early use.
The "helped researchers solve open problems" claim is anecdotal in the
abstract — no count, no protocol, no statement of how much of each
result was the system's versus the mathematician's. The abstract says
nothing about the agent architecture; the catalog entry's description
of a coordinator with parallel workstreams on Gemini 3.1 comes from the
paper body, not the abstract.

## Method

As far as the abstract states: a system description, early tests with
researchers, and evaluation on problem-solving benchmarks including
FrontierMath Tier 4. The abstract does not specify the underlying
models, the agent topology, the number of users or problems in the
early tests, the evaluation protocol for FrontierMath (attempts,
compute, verification), or which other AI systems it was compared
against. The arXiv listing (v2, May 2026, "23 pages; several citations
added") carries no journal reference.

## Relevance to RISE

The abstract's own list of supported activities maps onto
`rq-formulation` ("refines user intent"), `hypothesis-generation`,
`literature-discovery`, `formal-modeling`, `code-generation`
("computational exploration") and `paper-drafting` ("native
mathematical artifacts"), consistent with the catalog's tags. Catalog
slug: [`ai-co-mathematician`](../../projects/ai-co-mathematician.md);
the catalog also notes that RISE's own theorist-toolbox skills emulate
its coordinator-plus-workstream design in open form. Compared with
[`google-co-scientist`](../../projects/google-co-scientist.md), whose
abstract foregrounds a tournament-evolution process for hypotheses,
this abstract foregrounds interactivity and persistent state rather
than any competitive aggregation. For the ISR question of structure and
epistemic quality, the only structural mechanism the abstract itself
names is a stateful workspace that "tracks failed hypotheses" — a
memory-based rather than adversarial mechanism — while the catalog
entry (scored from the full paper) records in-pipeline review cycles;
FrontierMath Tier 4 is attractive as an outcome measure for
structure comparisons because correctness is checkable, unlike
open-ended discovery claims.

## Critique / open questions

The system is closed (catalog entry: no code, prompts or public
access), so nothing in the abstract can be independently reproduced.
"Early tests" are unquantified, and the abstract cannot tell us how
much of the headline discoveries depended on the expert in the loop.
The 48% figure leaves most Tier 4 problems unsolved, and "among all AI
systems evaluated" leaves the comparison set unspecified. The abstract
concedes no limitations. Transfer beyond pure mathematics to empirical
disciplines is not addressed.

## Key quotes

> "We introduce the AI co-mathematician, a workbench for mathematicians
> to interactively leverage AI agents to pursue open-ended research."
> (abstract)

> "By providing an asynchronous, stateful workspace that manages
> uncertainty, refines user intent, tracks failed hypotheses, and
> outputs native mathematical artifacts, the system mirrors human
> collaborative workflows." (abstract)

> "Besides demonstrating a highly interactive paradigm for AI-assisted
> mathematical discovery, the AI co-mathematician also achieves state of
> the art results on hard problem-solving benchmarks, including scoring
> 48% on FrontierMath Tier 4, a new high score among all AI systems
> evaluated." (abstract)
