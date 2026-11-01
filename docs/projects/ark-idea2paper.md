<!-- DO NOT EDIT — auto-generated from projects/landscape/ark-idea2paper.yml by scripts/build_indexes.py -->

# ARK (idea2paper)

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/kaust-ark/ARK>

**Licence:** `Apache-2.0`

**Source:** [`projects/landscape/ark-idea2paper.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ark-idea2paper.yml)

## Positioning

A CS-research pipeline ("Automatic Research Kit") that orchestrates six specialized agents — Researcher, Reviewer, Planner, Writer, Experimenter, Coder — through a three-phase Research / Dev / Review loop to turn a research idea into a submission-formatted LaTeX paper with DBLP-verified references, controllable via CLI, a web dashboard, or Telegram.

## Distinctive contribution

Pairs the idea-to-paper pipeline with a review loop that repeats until a score threshold is met before advancing, and ships venue-specific LaTeX templates (NeurIPS, ICML, ICLR, MLSys, the ACL family, CVPR/ICCV, SOSP/OSDI/USENIX-style systems venues) plus a Slurm-backed Experimenter for compute-heavy runs, aiming the pipeline specifically at ML-systems and ML research rather than a domain-agnostic brief.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Covers idea through paper plus an internal review/revision loop (~9 stages by declared pipeline_stages), but literature-discovery is DBLP-reference verification rather than a synthesis stage, and there is no external dissemination/submission-packaging step. |
| Autonomy level | 2 | Runs the three-phase Research/Dev/Review loop to a score threshold without per-step approval, but a human still supplies the initial idea and reviews the final output; no claim of fully unattended multi-paper operation. |
| Architectural transparency | 2 | Six-agent architecture, CLI, and pipeline phases are documented in the README with architecture decision records in-repo; full agent prompts are not confirmed read in this review. |
| Inputs supported | 1 | Single input form (a research idea/proposal); literature access is reference verification against DBLP rather than a literature corpus or external data-source integration. |
| Outputs / reproducibility | 2 | Persists paper + code + experiment logs with a CI badge and example PDFs in-repo, but there is no declared data manifest or end-to-end reproduction recipe independent of the Researcher/Experimenter agents' live runs. |
| Internal evaluation | 1 | Three linked example PDFs are presented as papers the project wrote, and a self-reported '$10-25 per paper' cost figure, but no third-party evaluation, acceptance record, or benchmark comparison is shown at this scoring date — anecdotal. |
| Openness | 2 | Apache-2.0 license; install script, Docker files, and example tasks are present, but GPU/Slurm-dependent examples fall short of guaranteed commodity-hardware reproduction. |
| Maturity / traction | 1 | 38 stars, 6 forks, 734 commits on main, 2 open issues as of 2026-11-01; active development (ADRs, tests, CI) but no outside-user evidence beyond repo activity — research-prototype stage. |
| Cross-family policy | 0 | No stated requirement or default for cross-model-family review between agents; single-stack by design as documented. |
| Runtime assurance | 1 | Reviewer-agent scoring gate and a repeat-until-threshold review loop provide a light runtime check; no claim-level citation/fact audit or math-proof verification described. |
| Cross-platform portability | 1 | CLI, web dashboard, and Telegram control surfaces plus Docker packaging; no multi-LLM-provider or multi-runtime portability claim beyond its own six-agent stack. |

*Scored on 2026-11-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `literature-discovery` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `multi-agent` `dag-orchestration` `iterative-loop` `tool-use` `artifact-versioning`


**Inputs:** `research-idea`


**Outputs:** `paper-draft` `code` `experiment-logs` `self-review`


**Knowledge sources:** `dblp`


## Limitations

- All performance and cost claims ($10-25/paper, anti-fabrication safeguards) are self-reported in the README; no independent evaluation of output paper quality was found at this scoring date.
- Slurm/HPC and multi-GPU orientation for the Experimenter agent narrows practical use to users with compute-cluster access for all but the smallest tasks.
- Young project (38 stars) with no outside-adoption evidence beyond its own repository activity.
- Scope is explicitly CS/ML-systems (venue templates listed are all CS venues); not positioned for economics/social-science use.

## Related projects in this catalog

- [`agent-laboratory`](agent-laboratory.md)
- [`ai-researcher`](ai-researcher.md)
- [`zeropaper`](zeropaper.md)
