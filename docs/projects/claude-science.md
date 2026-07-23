<!-- DO NOT EDIT — auto-generated from projects/landscape/claude-science.yml by scripts/build_indexes.py -->

# Claude Science

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://claude.com/product/claude-science>

**Source:** [`projects/landscape/claude-science.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/claude-science.yml)

## Positioning

Anthropic's AI workbench for researchers ("Claude Code for science"), announced 2026-06-30: a desktop app (macOS/Linux) in which a generalist coordinating agent with 60+ curated skills and connectors spawns specialist agents to run literature analysis, database queries, multistep data analyses, figure iteration, and manuscript drafting, with compute spanning the local machine, HPC clusters via SSH, and Modal GPUs. Covers a broad slice of the RISE pipeline from literature work through manuscript refinement, in the same big-lab workbench layer as Prism and Google Co-Scientist.

## Distinctive contribution

Auditable-artifact design: every figure ships with a reproducibility package (exact code, computational environment, plain-language methodology, full message history), and a background reviewer agent flags incorrect citations, untraceable numbers, and figures that don't match their underlying code as work progresses. Deepest pre-configured life-science stack of any big-lab offering — 60+ databases (UniProt, PDB, Ensembl, ChEMBL), NVIDIA BioNeMo Agent Toolkit, Evo 2, Boltz-2, OpenFold3 — backed by a grants program of $30,000 in credits for up to 50 AI-for- science projects (applications closed 2026-07-15).

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Eight stages from literature through manuscript refinement, but no declared referee-simulation or dissemination stage; the background reviewer is a runtime check, not a review stage. |
| Autonomy level | 2 | Supervised agent: user sets the task; coordinating agent spawns specialists, manages compute, and self-corrects, with the user reviewing resulting artifacts. |
| Architectural transparency | 1 | Coordinator/specialist/reviewer agent topology, skills-and-connectors model, and compute management documented at a high level; no code, prompts, or orchestration internals. |
| Inputs supported | 3 | Research prompts, own datasets, and custom skills/connectors to lab tools; both literature access and 60+ scientific databases, plus private data via SSH to users' own clusters. |
| Outputs / reproducibility | 3 | Headline design: every artifact ships with exact code, computational environment, plain-language methodology, and full message history — vendor-described, not yet independently verified. |
| Internal evaluation | 1 | Vendor-selected case studies (Manifold Bio, Allen Institute, UCSF Brain Tumor Center); no benchmark results or third-party evaluation. |
| Openness | 0 | Closed-source; beta gated behind paid Claude subscriptions (Pro/Max/Team/Enterprise); no free tier. |
| Maturity / traction | 2 | Public beta (June 2026) with external users across paid tiers, named institutional early adopters, discounted academic Team plan, and a grants program; weeks old at scoring date. |
| Cross-family policy | 0 | Anthropic models only; no cross-family executor/reviewer configuration. |
| Runtime assurance | 2 | Background reviewer agent flags incorrect citations, untraceable numbers, and figure-code mismatches in-flight and self-corrects; gating behavior not documented. |
| Cross-platform portability | 1 | Single provider and dedicated macOS/Linux app, but compute targets span local machines, HPC via SSH, and Modal GPUs. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `research-design` `data-acquisition` `data-analysis` `code-generation` `paper-drafting` `revision-editing`


**Architectural features:** `multi-agent` `tool-use` `persistent-memory` `iterative-loop` `artifact-versioning`


**Inputs:** `research-task-prompt` `user-datasets` `custom-skills-connectors`


**Outputs:** `analysis-artifacts` `reproducibility-packages` `figures` `manuscript-drafts`


**Data sources:** `scientific-databases` `user-provided`


**Knowledge sources:** `curated-skills-connectors` `scientific-literature`


## Limitations

- Closed-source and subscription-gated; cannot be audited, self-hosted, or pointed at non-Anthropic models.
- Pre-configured depth is life-science-specific (genomics, proteomics, structural biology, cheminformatics) and the grants program prioritizes biology — other disciplines start from a generic baseline.
- Effectiveness evidence is vendor-selected case studies rather than independent benchmarks; macOS/Linux only, no Windows.

## Related projects in this catalog

- [`google-co-scientist`](google-co-scientist.md)
- [`kosmos`](kosmos.md)
- [`robin`](robin.md)
- [`tooluniverse`](tooluniverse.md)
