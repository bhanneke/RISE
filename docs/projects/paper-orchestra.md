<!-- DO NOT EDIT — auto-generated from projects/landscape/paper-orchestra.yml by scripts/build_indexes.py -->

# PaperOrchestra

`external` · status: `dormant` · focus: `drafting` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/google-research/paper-orchestra>

**Source:** [`projects/landscape/paper-orchestra.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/paper-orchestra.yml)

## Positioning

A write-up-only multi-agent pipeline from Google Research: point it at a directory of raw research materials (the idea plus experimental logs) and a LaTeX template directory, and five specialised agents — outline generation, literature review, section writing, content refinement and plotting — return a submission-ready manuscript with a synthesised related-work section and generated plots and conceptual diagrams. Everything upstream of the write-up must already be done, so it sits squarely in the RISE drafting layer next to autosurvey, clo-author and zeropaper rather than in the end-to-end lane.

## Distinctive contribution

It publishes its judges: the repo ships the full autorater stack — citation F1 scoring, literature-review quality rubrics, side-by-side literature-review and whole-paper quality comparators, an agent-review module, and the prompt templates all of them use — which is a reusable evaluation harness for AI-written manuscripts independent of the generator, and rarer in this catalog than the generator itself. The companion arXiv paper (2604.05018) reports human-evaluation win-rate margins of 50–68% on literature-review quality and 14–38% on overall manuscript quality against autonomous baselines, and introduces PaperWritingBench, derived from 200 top-tier AI conference papers.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five write-up-side stages (outline, literature review, section writing, refinement, plotting into a conference-compliant template) with everything upstream missing — no ideation, research design, data acquisition, analysis or code generation; the experiments must already exist. |
| Autonomy level | 2 | Supervised agent: the human assembles the materials directory and template and reviews the returned manuscript; the interactive Streamlit frontend allows step-level involvement but the CLI path runs the five agents through without approval gates. |
| Architectural transparency | 3 | Apache-2.0 with the five-agent pipeline in methods/, the CLI, the templates, and — unusually — the complete autorater evaluation harness plus its prompts/ directory published, alongside an arXiv paper documenting the architecture and human-evaluation protocol; only the evaluation dataset is withheld. |
| Inputs supported | 2 | Multiple input forms (a raw-materials directory of ideas and experimental logs, plus a LaTeX template directory) combined with live literature access through the Semantic Scholar API; no private-corpus or dataset connector. |
| Outputs / reproducibility | 2 | Produces a complete, version-controllable LaTeX manuscript with generated figures and a synthesised bibliography from a declared materials directory, but no seeds, run manifest or provenance linking claimed numbers back to the supplied logs. |
| Internal evaluation | 2 | Systematic internal evaluation reported in the arXiv paper — human-evaluation win-rate margins of 50–68% (literature-review quality) and 14–38% (overall manuscript quality) against autonomous baselines, on the 200-paper PaperWritingBench — but the preprint is not peer-reviewed and the benchmark dataset is not released, so no third party can reproduce or contest the numbers. |
| Openness | 2 | Apache-2.0 and the pipeline plus autoraters are runnable against your own materials, so examples are partially reproducible; but the evaluation dataset is explicitly withheld ('released separately at a later date'), no example materials directory is shipped, and OpenAI or Vertex/Gemini plus Semantic Scholar keys are required. |
| Maturity / traction | 1 | 124 stars and 19 forks on a two-commit code drop with no releases, nothing pushed since 2026-05-17, and an explicit note that it is not an officially supported Google product — attention without maintenance. |
| Cross-family policy | 0 | The backend is configured globally as OpenAI or Vertex AI/Gemini with no documented per-agent model assignment, so the section writer and the refinement agent run in the same family; unverified whether per-agent overrides exist, scored low accordingly. |
| Runtime assurance | 1 | One light in-pipeline check — a dedicated content-refinement agent making a single-pass review over the draft, with related work grounded in Semantic Scholar retrieval; the citation-F1 and quality autoraters are post-hoc evaluation tooling, not gates in the generation path. |
| Cross-platform portability | 1 | Two documented backends (OpenAI, or Vertex AI/Gemini) behind one Python CLI plus a Streamlit frontend — a small adapter set, one runtime. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `paper-drafting` `revision-editing` `dissemination`


**Architectural features:** `multi-agent` `tool-use` `dag-orchestration`


**Inputs:** `raw-materials-directory` `experimental-logs` `latex-template`


**Outputs:** `latex-manuscript` `literature-review-section` `figures` `conceptual-diagrams`


**Data sources:** `user-provided`


**Knowledge sources:** `semantic-scholar`


## Limitations

- Only 2 commits on main and nothing pushed since 2026-05-17 — a one-shot code drop rather than a maintained project, despite living in the google-research organisation (which the README notes is not an official Google product).
- The PaperWritingBench evaluation dataset is explicitly not included and 'will be released separately at a later date', so the reported 50–68% and 14–38% win-rate margins cannot be checked or reproduced.
- Targets AI/ML conference papers: the writing machinery (outline, related work, refinement, plotting) may transfer, but the disciplinary conventions of economics — identification narratives, robustness batteries, table norms, referee expectations — are not modelled.
- It is a write-up tool, not a research pipeline: it presumes finished experiments and does no analysis, code generation or verification of the numbers it is handed.
- Requires paid OpenAI or Vertex/Gemini keys plus a Semantic Scholar API key; no free-tier path.
- No per-agent model configuration is documented, so cross-family review could not be verified either way.

## Related projects in this catalog

- [`autosurvey`](autosurvey.md)
- [`clo-author`](clo-author.md)
- [`zeropaper`](zeropaper.md)
- [`research-paper-writing-skills`](research-paper-writing-skills.md)

## Papers describing this project

- **PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing** — Song, Y., Song, Y., Pfister, T., Yoon, J. (2026). *arXiv*. [arXiv:2604.05018](https://arxiv.org/abs/2604.05018)

## Related references (literature catalog)

- `song2026paperorchestra` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
