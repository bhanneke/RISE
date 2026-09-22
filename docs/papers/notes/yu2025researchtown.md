---
citekey: yu2025researchtown
title: 'ResearchTown: Simulator of Human Research Community'
authors:
- Yu, H.
- Hong, Z.
- Cheng, Z.
- Zhu, K.
- Xuan, K.
- Yao, J.
- Feng, T.
- You, J.
year: 2025
venue: ICML 2025
doi: ''
url: https://arxiv.org/abs/2412.17767
kind: paper
themes:
- autonomous-research-agents
- ai-peer-review
- sociotechnical
- evaluation-of-ai-research
methods:
- system-design
- simulation
- benchmark-evaluation
relates_to_projects:
- research-town
status: skimmed
arxiv_id: '2412.17767'
---

## Summary

ResearchTown asks whether LLMs can simulate a human research
community. It represents the community as an agent-data graph:
researchers are agent-type nodes, papers are data-type nodes, and
edges follow collaboration relationships. TextGNN, a text-based
inference framework, models research activities such as paper
reading, paper writing and review writing as special cases of one
unified message-passing process over that graph. To evaluate the
simulation the authors introduce ResearchBench, which masks a node
and scores the simulated reconstruction by similarity. They report
three findings: the simulation of collaborative activities including
paper and review writing is realistic; it stays robust with multiple
researchers and diverse papers; and it can generate interdisciplinary
ideas that may inspire new directions. Published at ICML 2025 (arXiv
v2, June 2025).

## Contribution

Claimed: a graph formalism for research communities, an inference
framework that unifies research activities as message passing, a
scalable benchmark, and the three findings above. What the abstract
supports: the framework and benchmark exist, and "realistic" is
operationalised as similarity of a reconstructed node to the real
masked node, i.e. the ability to regenerate existing papers or
reviews, not the quality of new science. Finding (3) is hedged in the
abstract itself ("potentially inspire").

## Method

Simulation framework plus a self-built benchmark. Evaluation is a
node-masking prediction task on the agent-data graph scored by
similarity. The abstract does not specify the similarity metric, the
size of the graph or paper corpus, the number of simulated
researchers, the backbone LLM, baselines, any human evaluation, how
robustness is measured, or how the quality of simulated reviews is
judged beyond similarity to real ones.

## Relevance to RISE

Informs literature-synthesis, rq-formulation, hypothesis-generation,
paper-drafting and referee-simulation, matching the catalog entry
`research-town`, which positions it as a simulator whose outputs are
research about research pipelines rather than a deployable pipeline.
For the ISR question on multi-agent structure this is the most
explicit structural object in the catalog: knowledge production is
modelled as message passing over a collaboration graph, so paper
writing and review writing are literally aggregations over
neighbouring agent and paper nodes, and community topology directly
determines what gets produced; the abstract, however, evaluates
fidelity to the real community (similarity to masked nodes) rather
than the epistemic quality of the generated output, so it establishes
the mechanism without measuring its effect on quality.

## Critique / open questions

Similarity-based scoring rewards reproducing what already exists and
cannot by itself detect whether simulated reviews are calibrated
against real review outcomes. The abstract mentions no human
evaluation and no comparison to non-graph multi-agent baselines. The
claim about interdisciplinary ideas is untested in the abstract. The
abstract concedes that the community is "simplified" as an agent-data
graph. The catalog notes that published runs use a single LLM family
and that end-to-end operation requires the OpenAI API and a database.

## Key quotes

> "Within this framework, the human research community is simplified
> as an agent-data graph, where researchers and papers are
> represented as agent-type and data-type nodes, respectively, and
> connected based on their collaboration relationships." (abstract)

> "We also introduce TextGNN, a text-based inference framework that
> models various research activities (e.g., paper reading, paper
> writing, and review writing) as special forms of a unified
> message-passing process on the agent-data graph." (abstract)

> "To evaluate the quality of the research community simulation, we
> present ResearchBench, a benchmark that uses a node-masking
> prediction task for scalable and objective assessment based on
> similarity." (abstract)
