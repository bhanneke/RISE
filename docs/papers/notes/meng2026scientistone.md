---
citekey: meng2026scientistone
title: 'ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence'
authors:
- 'Meng, R.'
- 'Dalvi Mishra, B.'
- 'Chen, J.'
- 'Li, C.-L.'
- 'Goyal, P.'
- 'Parmar, M.'
- 'Song, Y.'
- 'Song, Y.'
- 'Sinha, R.'
- 'Ranganathan, P.'
- et al.
year: 2026
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2605.26340
kind: preprint
themes:
- evaluation-of-ai-research
- hallucination
- autonomous-research-agents
- replication-infrastructure
methods:
- system-design
- audit
- benchmark-evaluation
relates_to_projects:
- sakana-ai-scientist
- autoresearchclaw
- deepscientist
status: skimmed
arxiv_id: '2605.26340'
---

## Summary

Google Cloud AI Research argues that autonomous research agents produce
competitive results and professional-looking manuscripts whose
failures are invisible to surface evaluation: fabricated citations,
scores that do not reproduce, and method descriptions that diverge
from the code. Three contributions follow. **Chain-of-Evidence** is a
verifiability framework in which every claim must trace to its
evidence source. **ScientistOne** is an end-to-end system that
maintains those chains by construction through literature review,
solution discovery and writing. **CoE Audit** is a post-hoc audit with
four integrity checks (score verification, specification violation,
reference verification, method-code alignment) applied uniformly to
any system. Across 75 papers from five systems on five research tasks,
every baseline shows at least one systematic failure: hallucinated
reference rates up to 21%, score verification passing in as few as
42% of papers, and method-code alignment between 20% and 80%.
ScientistOne reports 0/337 hallucinated references, 12/12 score
verification and 14/15 method-code alignment.

## Contribution

Two separable contributions of unequal weight. The system result is
the headline, but the audit is the more durable one: a uniform,
system-independent set of integrity checks applied to other people's
outputs. The self-comparison is less convincing than the audit,
because the authors both built the evaluation and designed their
system to pass it.

## Method

Head-to-head comparison across 75 generated papers, five systems, five
tasks, plus a generalisation check on six further tasks. The abstract
names Parameter Golf and MLE-Bench among the latter. Which five
baseline systems appear is stated in the body; the abstract does not
list them.

## Relevance to RISE

The strongest external evidence in this knowledge base on output
integrity for systems RISE catalogues — the audited baselines include
`sakana-ai-scientist`, `autoresearchclaw`, `deepscientist` and
HKUDS AI-Researcher ([tang2025airesearcher]). The four checks map
closely onto the rubric's `outputs_reproducibility` and
`assurance_runtime` dimensions and could be used to score them more
concretely than the present evidence notes do. It also puts numbers on
the claim this KB keeps making qualitatively: a professional-looking
manuscript says little about whether its references exist or its code
does what the text says. For the *Architecture as Epistemology* paper,
Chain-of-Evidence is a direct operationalisation of the traceability
dimension.

## Critique / open questions

The audit is designed by the team whose system tops it, so the
headline comparison needs independent replication with the audit
applied by others. Five tasks is a narrow base, and "matching or
exceeding human expert performance" depends on task choice. Whether
evidence chains carry over to fields without executable code — most of
the social sciences — is untested.

## Key quotes

> "Autonomous research agents produce competitive solutions and
> professional-looking manuscripts, yet their outputs contain
> verifiability failures undetectable by surface-level evaluation:
> fabricated citations, unreproducible scores, and method descriptions
> that diverge from the implementation." (abstract)

> "Across 75 papers spanning five systems and five frontier research
> tasks, every baseline exhibits at least one systematic failure mode:
> hallucinated reference rates reach 21%, score verification passes in
> as few as 42% of papers, and method-code alignment ranges from 20%
> to 80%." (abstract)
