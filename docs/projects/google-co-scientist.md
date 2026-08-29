<!-- DO NOT EDIT — auto-generated from projects/landscape/google-co-scientist.yml by scripts/build_indexes.py -->

# AI Co-Scientist (Google DeepMind)

`external` · status: `active` · focus: `ideation` · discipline: `general` · started: 2025

**Project page:** <https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/>

**Source:** [`projects/landscape/google-co-scientist.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/google-co-scientist.yml)

## Positioning

Google's closed multi-agent research partner (announced Feb 2025, published in Nature 2026-05-19) that generates, debates, and evolves novel research hypotheses. Built on Gemini, it orchestrates six specialized agents — Generation, Reflection, Ranking, Proximity, Evolution, Meta-review — under a Supervisor, using Elo-based tournaments and simulated scientific debate to surface and refine ideas. It sits in the upstream *ideation* layer: it proposes hypotheses and experiments but does not run experiments, analyze data, or draft papers.

## Distinctive contribution

The most externally validated hypothesis-generation system on the landscape: peer-reviewed in Nature, with wet-lab confirmation of AI-proposed leads in AML drug repurposing, liver-fibrosis reversal, and antimicrobial-resistance gene transfer, and active use by infectious-disease, aging, and ALS research teams across 100+ institutions. RISE separately catalogs the open-source reimplementation open-coscientist; this entry is the closed, first-party system whose design that project reverse-engineers.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Four tightly clustered upstream stages culminating in ranked hypotheses and proposed experiments; no execution, analysis, or drafting. |
| Autonomy level | 3 | Supervisor agent autonomously orchestrates the generate-debate-evolve tournament loop; scientist supplies the goal and reviews the ranked hypotheses. |
| Architectural transparency | 1 | Nature paper and the 2025 arXiv preprint document the agent roles and Elo-tournament design, but no code, prompts, or configs are released. |
| Inputs supported | 2 | Natural-language research goal plus access to literature and specialized databases (ChEMBL, UniProt) and tools such as AlphaFold. |
| Outputs / reproducibility | 1 | Persists prose hypotheses and cited research overviews; closed and hosted, with no reproducible artifact package. |
| Internal evaluation | 3 | Peer-reviewed in Nature (10.1038/s41586-026-10644-y) with experimental wet-lab validation of AI-proposed leads and sustained multi-institution adoption. |
| Openness | 1 | No source or prompts released; a heavily gated trusted-tester tool (Hypothesis Generation in Gemini for Science) is the only access path. |
| Maturity / traction | 3 | Peer-reviewed, Google-backed, and in active real-world use across 100+ institutions with reported drug-discovery outcomes. |
| Cross-family policy | 0 | Single model family — all agents run on Gemini. |
| Runtime assurance | 2 | Reflection (peer-review) agent, Elo ranking tournament, and Meta-review provide multiple in-pipeline debate gates, with citations grounding outputs. |
| Cross-platform portability | 0 | Closed, hosted on Google infrastructure and locked to Gemini; not deployable on other stacks. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `hypothesis-generation` `research-design`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base` `iterative-loop` `debate-consensus`


**Inputs:** `research-goal`


**Outputs:** `ranked-hypotheses` `research-proposals` `research-overview`


**Data sources:** `web-search` `chembl` `uniprot` `alphafold`


**Knowledge sources:** `scientific-literature` `web-search`


## Limitations

- Closed source with trusted-tester-only access; the architecture is known from the papers but neither code nor prompts are published, so results are not independently reproducible.
- Covers ideation only — proposes hypotheses and experiments but does not execute them; all wet-lab validation and downstream work is performed by human teams.
- Runs entirely within the Gemini family, so it lacks cross-model-family review and is subject to that family's blind spots and single-vendor lock-in.

## Related projects in this catalog

- [`open-coscientist`](open-coscientist.md)
- [`robin`](robin.md)
- [`researchagent`](researchagent.md)
- [`ai-co-mathematician`](ai-co-mathematician.md)

## Papers describing this project

- **Accelerating scientific discovery with Co-Scientist** — Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Palepu, A., Sirkovic, P., et al. (2026). *Nature*. [doi](https://doi.org/10.1038/s41586-026-10644-y)
- **Towards an AI co-scientist** — Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Palepu, A., Sirkovic, P., et al. (2025). *arXiv (Google DeepMind)*. [arXiv:2502.18864](https://arxiv.org/abs/2502.18864)

## Related references (literature catalog)

- Gottweis, J. et al. (2026). [*Accelerating scientific discovery with Co-Scientist*](../papers/notes/gottweis2026coscientist.md) `gottweis2026coscientist`
