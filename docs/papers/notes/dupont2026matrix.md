---
citekey: dupont2026matrix
title: 'Improving the matrix multiplication exponent with modern optimization and AlphaEvolve'
authors:
- 'Dupont, E.'
- 'Eisenberger, M.'
- 'Kozlovskii, B.'
- 'Mehrabian, A.'
- 'Ruiz, F. J. R.'
- 'See, A.'
- 'Zhou, R.'
- 'Alman, J.'
- 'Vassilevska Williams, V.'
- 'Balog, M.'
year: 2026
venue: 'arXiv preprint (Google DeepMind)'
doi: ''
url: https://arxiv.org/abs/2608.16884
kind: preprint
themes:
- autonomous-research-agents
methods:
- optimization
- formal-result
relates_to_projects:
- alphaevolve
status: skimmed
arxiv_id: '2608.16884'
---

## Summary

A research note improving the best known upper bound on the matrix
multiplication exponent ω. The authors attack the optimization problem
at the core of combination loss analysis (the refinement of the laser
method behind the current records): they reformulate the problem so it
can be solved in a larger setting than previously possible, design a
new optimization algorithm using recent machine-learning advances, and
refine that algorithm with AlphaEvolve. The combined approach yields
ω < 2.371177, improving the previous best bound of 2.371339. Notably,
the author list joins the DeepMind AlphaEvolve team with the
complexity theorists whose hand-derived analyses held the prior
records (Alman, Vassilevska Williams, Zhou).

## Contribution

Claimed and supported by the abstract: a new state-of-the-art bound on
a decades-old open problem, obtained with an agentic evolutionary
coding system in the loop. The improvement is small in absolute terms
(fifth decimal place), as is typical for this line of work.

## Method

Theoretical-computer-science note: reformulation of the combination
loss optimization problem, a bespoke ML-designed optimization
algorithm, and AlphaEvolve refinement. The abstract does not state how
much of the gain each of the three steps contributes.

## Relevance to RISE

Catalog slug `alphaevolve` (formal-modeling stage). Together with
[georgiev2025alphaevolvemath] this is the second peer-checkable
mathematical advance with AlphaEvolve in the loop, and the clearest
kind of evidence in the catalog that agentic systems can contribute to
results whose correctness is externally verifiable — the opposite pole
from research tasks with no machine-checkable correctness signal.

## Critique / open questions

The division of labor between the human theorists and the automated
components cannot be judged from the abstract, so what "AlphaEvolve
refined the algorithm" means in practice — search over parameters vs.
discovery of new structure — is open. As a note, it has not been
peer-reviewed yet.

## Key quotes

> "Second, we leverage recent advances in machine learning to design a
> new optimization algorithm for this problem. Finally, we refine the
> resulting optimization algorithm with AlphaEvolve." (abstract)

> "Our combined approach yields an upper bound of ω < 2.371177,
> improving the previous best bound of 2.371339." (abstract)
