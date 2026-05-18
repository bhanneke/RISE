<!-- DO NOT EDIT — auto-generated from projects/landscape/academic-research-skills.yml by scripts/build_indexes.py -->

# Academic Research Skills (ARS)

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/Imbad0202/academic-research-skills>

**Source:** [`projects/landscape/academic-research-skills.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/academic-research-skills.yml)

## Positioning

A comprehensive Claude Code plugin suite (v3.9.0 at scoring date) for the academic research pipeline: literature → write → review → revise → finalize. Three sub-suites — Deep Research (13 agents), Academic Paper (12 agents), Academic Paper Reviewer (7 agents) — with Style Calibration, anti-leakage protocols, Semantic Scholar API verification, VLM figure verification, and explicit human-in- the-loop gates throughout.

## Distinctive contribution

Most-adopted Claude Code-native research plugin (9k+ stars) with an explicit "AI as copilot, not pilot" design stance. v3.8 introduces a *claim-faithfulness audit pass* (`ARS_CLAIM_AUDIT=1`) that fetches each cited source against three-layer citation anchors and gate-blocks output on five hallucination classes (claim-not-supported, negative-constraint-violation, fabricated-reference, anchorless, constraint-violation-uncited). This is the most operationally serious anti-hallucination apparatus in the catalog.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five stages spanning literature through review; less coverage on empirical analysis / modeling than full-pipeline economics tools. |
| Autonomy level | 1 | Explicit copilot stance: 'AI is your copilot, not the pilot.' Human approval at every stage gate. |
| Architectural transparency | 3 | Detailed architecture docs (docs/ARCHITECTURE.md), public failure-mode reference, calibration thresholds (FNR<0.15, FPR<0.10) published in spec. |
| Inputs supported | 3 | Topic / draft / reviewer-comment inputs; Pandoc + tectonic for DOCX/PDF; multiple installation paths (plugin, project skills, global skills, claude.ai Project). |
| Outputs / reproducibility | 3 | Three-layer citation anchors enable claim-level audits; replication packages; versioned releases. |
| Internal evaluation | 3 | Calibration mode with gold-set FNR/FPR measurement; cross-model verification (`ARS_CROSS_MODEL`); engages published failure-mode literature directly. |
| Openness | 2 | CC BY-NC 4.0 (non-commercial); sponsor-supported; Codex CLI sibling distribution available. |
| Maturity / traction | 3 | 9.3k+ stars; v3.9.0 with multi-version release cadence; English + Traditional Chinese docs; multi-IDE support. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `debate-consensus` `human-in-loop` `tool-use` `rag-knowledge-base` `artifact-versioning`


**Inputs:** `research-topic` `paper-draft` `reviewer-comments`


**Outputs:** `paper-pdf` `paper-docx` `literature-review` `reviewer-report` `revision-plan`


**Data sources:** `user-provided`


**Knowledge sources:** `semantic-scholar` `arxiv`


## Limitations

- Non-commercial license restricts deployment options.
- Heavy on the writing/review block; lighter on empirical data analysis or formal modeling.
- Quality of claim-audit gating depends on user-supplied calibration set.
- Author's substantive scholarly background is not disclosed in repo metadata; project is engineering-led rather than discipline-led.

## Related projects in this catalog

- [`clo-author`](clo-author.md)
- [`e2er`](e2er.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`reviewer`](reviewer.md)

## Related references (literature catalog)

- Ji, Z. et al. (2023). [*Survey of Hallucination in Natural Language Generation*](../papers/notes/ji2023hallucination.md) `ji2023hallucination`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
