<!-- DO NOT EDIT — auto-generated from projects/landscape/prism.yml by scripts/build_indexes.py -->

# Prism

`external` · status: `active` · focus: `drafting` · discipline: `general` · started: 2026

**Project page:** <https://openai.com/prism/>

**Source:** [`projects/landscape/prism.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/prism.yml)

## Positioning

OpenAI's free AI-native LaTeX workspace for scientific writing and collaboration, launched late January 2026 on Crixet, a cloud LaTeX platform OpenAI acquired. GPT-5.2 (upgraded to GPT-5.3 with Codex CLI in March 2026) operates inside the document with access to the paper's structure, equations, citations, and figures, covering drafting, revision, real-time collaboration, arXiv-backed referencing, and publication prep. Sits in the writing layer of the RISE pipeline — the manuscript-workspace counterpart to workbench products like Claude Science.

## Distinctive contribution

First big-lab product to make the manuscript itself the AI-native surface: the model is embedded in the LaTeX project rather than bolted on as a chat sidecar, and the workspace is free with unlimited projects and collaborators on a personal ChatGPT account. Converts whiteboard/handwritten sketches to LaTeX, auto-finds and formats arXiv references, and — since the March 2026 Codex integration — runs Python/R in-workspace with compile-check-revise self-repair loops for LaTeX errors.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Six stages centered on the writing layer (reference search, in-workspace analysis/code since March 2026, drafting, revision, publication prep); nothing upstream of the manuscript. |
| Autonomy level | 1 | Copilot: the researcher authors the paper; the in-document model drafts, edits, and self-repairs LaTeX on request, with the human approving changes. |
| Architectural transparency | 1 | Model identity (GPT-5.2/5.3-Codex), Crixet foundation, and in-document context integration disclosed; no prompts, code, or architecture documentation beyond marketing. |
| Inputs supported | 2 | Multiple input forms (LaTeX projects, natural-language and voice instructions, sketch photos, data files) plus arXiv literature access; no private-corpus integration. |
| Outputs / reproducibility | 2 | Cloud projects persist LaTeX source, bibliographies, and (post-March) executed code and generated figures; no Git integration, limited version-history transparency, no reproducibility manifest. |
| Internal evaluation | 0 | No published evaluation, benchmark, or systematic quality evidence in launch or upgrade coverage at scoring date. |
| Openness | 1 | Closed-source, but the hosted service is free with a personal ChatGPT account (unlimited projects/collaborators); advanced AI features expected to move behind paid tiers. |
| Maturity / traction | 2 | Production launch (Jan 2026) on an acquired platform, open globally to ChatGPT Free/Go/Plus/Pro with a major March upgrade; no adoption numbers disclosed. |
| Cross-family policy | 0 | OpenAI models only (GPT-5.2, then GPT-5.3 with Codex CLI); no cross-family configuration. |
| Runtime assurance | 1 | Compile-check-revise self-repair loops and arXiv-grounded citation insertion; no claim-audit, fact-check, or figure-integrity gates. |
| Cross-platform portability | 0 | Single hosted web surface tied to one provider; no self-hosting, IDE integrations, or alternative runtimes. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `dissemination`


**Architectural features:** `single-llm` `tool-use` `iterative-loop`


**Inputs:** `latex-project` `natural-language-instructions` `whiteboard-sketches` `data-files`


**Outputs:** `latex-manuscripts` `formatted-bibliographies` `figures` `compiled-pdfs`


**Data sources:** `user-provided`


**Knowledge sources:** `arxiv`


## Limitations

- Closed-source hosted service: manuscripts live in OpenAI's cloud with only the standard ChatGPT training opt-out; no self-hosting or audit path.
- No native Git integration and limited version-history transparency; early reviews describe it as a functional silo disconnected from external codebases.
- Locked to OpenAI models, and the free tier is strategic — advanced AI features are slated to require paid ChatGPT subscriptions.

## Related projects in this catalog

- [`storm`](storm.md)
- [`autosurvey`](autosurvey.md)
- [`research-paper-writing-skills`](research-paper-writing-skills.md)
