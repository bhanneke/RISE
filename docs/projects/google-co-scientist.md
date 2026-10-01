<!-- DO NOT EDIT — auto-generated from projects/landscape/google-co-scientist.yml by scripts/build_indexes.py -->

# AI Co-Scientist (Google DeepMind)

`external` · status: `active` · focus: `ideation` · discipline: `general` · started: 2025

**Project page:** <https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/>

**Source:** [`projects/landscape/google-co-scientist.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/google-co-scientist.yml)

## Positioning

Google's closed multi-agent research partner (announced Feb 2025, published in Nature 2026-05-19) that generates, debates, and evolves novel research hypotheses. Built on Gemini, it orchestrates six specialized agents — Generation, Reflection, Ranking, Proximity, Evolution, Meta-review — under a Supervisor, using Elo-based tournaments and simulated scientific debate to surface and refine ideas. Originally an upstream *ideation*-only system, a follow-up preprint (arXiv:2608.26701, 2026-08-28) documents an execution-grounded configuration that closes the loop in specific case studies: interfacing with a real chemical-vapor-deposition reactor and Gemini 3 Deep Think to design and run materials-science syntheses, building a data-analysis pipeline for biology imaging data, and autonomously producing a working inference-time-scaling architecture in computer science — i.e. beyond pure ideation into research-design, data-analysis and code-generation in these demonstrated cases, though the publicly described default product remains hypothesis/proposal generation.

## Distinctive contribution

The most externally validated hypothesis-generation system on the landscape: peer-reviewed in Nature, with wet-lab confirmation of AI-proposed leads in AML drug repurposing, liver-fibrosis reversal, and antimicrobial-resistance gene transfer, and active use by infectious-disease, aging, and ALS research teams across 100+ institutions. A 2026-08-28 follow-up preprint extends this with closed-loop, execution-grounded validation across three disciplines: single-attempt synthesis of monolayer MoS2/MoSe2/WS2 semiconductors and a novel MXene precursor route in materials science, a biology prediction pipeline matching unpublished wet-lab measurements, and a CS architecture that outperformed six frontier models on HealthBench — plus enterprise previews reported at Daiichi Sankyo, Bayer Crop Science and US National Laboratories. RISE separately catalogs the open-source reimplementation open-coscientist; this entry is the closed, first-party system whose design that project reverse-engineers.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Six stages: the original four upstream stages plus data-analysis and code-generation, now demonstrated in a 2026-08-28 follow-up preprint's closed-loop materials-science, biology and CS case studies; still no paper-drafting or referee-simulation stage, and the demonstrated execution capability is case-study-specific rather than the documented default product. |
| Autonomy level | 3 | Supervisor agent autonomously orchestrates the generate-debate-evolve tournament loop; scientist supplies the goal and reviews the ranked hypotheses. |
| Architectural transparency | 1 | Nature paper and the 2025 arXiv preprint document the agent roles and Elo-tournament design, but no code, prompts, or configs are released. |
| Inputs supported | 2 | Natural-language research goal plus access to literature and specialized databases (ChEMBL, UniProt) and tools such as AlphaFold. |
| Outputs / reproducibility | 1 | Persists prose hypotheses and cited research overviews; closed and hosted, with no reproducible artifact package. |
| Internal evaluation | 3 | Peer-reviewed in Nature (10.1038/s41586-026-10644-y) with experimental wet-lab validation of AI-proposed leads and sustained multi-institution adoption; reinforced by a 2026-08-28 arXiv follow-up (2608.26701) reporting closed-loop execution results across materials science, biology and CS, including single-attempt monolayer-semiconductor synthesis and outperforming six frontier models on HealthBench. |
| Openness | 1 | No source or prompts released; a heavily gated trusted-tester tool (Hypothesis Generation in Gemini for Science) is the only access path. |
| Maturity / traction | 3 | Peer-reviewed, Google-backed, and in active real-world use across 100+ institutions with reported drug-discovery outcomes; as of 2026-08-28 enterprise previews are also named at Daiichi Sankyo, Bayer Crop Science and US National Laboratories, with closed-loop materials/biology/CS case studies published. |
| Cross-family policy | 0 | Single model family — all agents run on Gemini. |
| Runtime assurance | 3 | Reflection (peer-review) agent, Elo ranking tournament, and Meta-review provide multiple in-pipeline debate gates; the 2026-08-28 follow-up preprint adds real execution feedback as a runtime check (synthesis outcomes, lab measurements, benchmark scores feeding back into the loop), reporting a drop in severe methodological errors from 100% in baseline models to 24% — a heavier audit stack than debate-only gating. |
| Cross-platform portability | 0 | Closed, hosted on Google infrastructure and locked to Gemini; not deployable on other stacks. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `hypothesis-generation` `research-design` `data-analysis` `code-generation`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base` `iterative-loop` `debate-consensus`


**Inputs:** `research-goal`


**Outputs:** `ranked-hypotheses` `research-proposals` `research-overview`


**Data sources:** `web-search` `chembl` `uniprot` `alphafold`


**Knowledge sources:** `scientific-literature` `web-search`


## Limitations

- Closed source with trusted-tester-only access; the architecture is known from the papers but neither code nor prompts are published, so results are not independently reproducible.
- Execution-grounded closed-loop capability (materials/biology/CS) is demonstrated in named case studies in the 2026-08-28 preprint, not confirmed as the generally available default product; most deployments remain hypothesis-and-proposal generation with human teams executing downstream work.
- Runs entirely within the Gemini family, so it lacks cross-model-family review and is subject to that family's blind spots and single-vendor lock-in.

## Related projects in this catalog

- [`open-coscientist`](open-coscientist.md)
- [`robin`](robin.md)
- [`researchagent`](researchagent.md)
- [`ai-co-mathematician`](ai-co-mathematician.md)

## Papers describing this project

- **Accelerating scientific discovery with Co-Scientist** — Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Palepu, A., Sirkovic, P., et al. (2026). *Nature*. [doi](https://doi.org/10.1038/s41586-026-10644-y)
- **Towards an AI co-scientist** — Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Palepu, A., Sirkovic, P., et al. (2025). *arXiv (Google DeepMind)*. [arXiv:2502.18864](https://arxiv.org/abs/2502.18864)
- **Accelerating Scientific Research with Gemini in the Real-World** — Schmidgall, S., Zhu, X., Shaw, M., Yang, L., Liévin, V., Yang, J., et al. (2026). *arXiv (Google DeepMind)*. [arXiv:2608.26701](https://arxiv.org/abs/2608.26701)

## Related references (literature catalog)

- Gottweis, J. et al. (2026). [*Accelerating scientific discovery with Co-Scientist*](../papers/notes/gottweis2026coscientist.md) `gottweis2026coscientist`
