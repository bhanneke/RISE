<!-- DO NOT EDIT — auto-generated from projects/landscape/research-town.yml by scripts/build_indexes.py -->

# ResearchTown

`external` · status: `active` · focus: `ideation` · discipline: `general` · started: 2024

**Project page:** <https://github.com/ulab-uiuc/research-town>

**Source:** [`projects/landscape/research-town.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/research-town.yml)

## Positioning

An ICML 2025 multi-agent platform for *community-level* automatic research simulation. ResearchTown models a research community as agents (Researchers), environments (collaboration rooms), and engines (state-machine controllers that route agents between tasks like idea discussion, rebuttal writing, paper writing, and reviewing). Sits in the ideation + lit-synthesis + drafting + review block.

## Distinctive contribution

Studies *community dynamics* rather than single-pipeline output: how groups of agents interact, divide labor, and shape each other's work. The simulator-vs-pipeline framing makes it a natural vehicle for studying field-level RISE questions (cf. [@gartenberg2026morebetter], [@tonerrodgers2025genai]).

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five stages spanning ideation through review (in simulation). |
| Autonomy level | 3 | Community runs autonomously; user configures the simulation. |
| Architectural transparency | 3 | Open under Apache-2.0; ICML 2025 publication; researcher/environment/engine abstractions documented. |
| Inputs supported | 2 | Community/paper-seed inputs; configurable agent skill sets. |
| Outputs / reproducibility | 2 | PyPI-installable; trajectories persisted; LLM nondeterminism limits exact reproduction. |
| Internal evaluation | 2 | ICML paper presents systematic evaluation of community-level metrics. |
| Openness | 3 | Apache-2.0; pip-installable; active community channels. |
| Maturity / traction | 2 | 204 stars; ICML 2025 acceptance; active development through 2026-05. |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-synthesis` `rq-formulation` `hypothesis-generation` `paper-drafting` `referee-simulation`


**Architectural features:** `multi-agent` `dag-orchestration` `persistent-memory` `artifact-versioning`


**Inputs:** `research-community-spec` `paper-seed`


**Outputs:** `agent-trajectories` `simulated-papers` `simulated-reviews`


**Knowledge sources:** `paper-corpus`


## Limitations

- Community simulation, not a deployable RISE pipeline — outputs are research about RISE, not research output.
- OpenAI API + database required to run end-to-end.

## Related projects in this catalog

- [`agent-laboratory`](agent-laboratory.md)
- [`open-coscientist`](open-coscientist.md)
- [`aviary`](aviary.md)
- [`mlgym`](mlgym.md)

## Papers describing this project

- **ResearchTown: Simulator of Human Research Community** — ULab UIUC team (2025). *ICML 2025*. [link](https://github.com/ulab-uiuc/research-town)

## Related references (literature catalog)

- Park, J. S. et al. (2023). [*Generative Agents: Interactive Simulacra of Human Behavior*](../papers/notes/park2023generative.md) `park2023generative`
- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
