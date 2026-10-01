<!-- DO NOT EDIT — auto-generated from projects/landscape/zirui-claude-skills.yml by scripts/build_indexes.py -->

# Claude Code Skills for Empirical Research (zirui-song)

`external` · status: `active` · focus: `analysis` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/zirui-song/claude-skills>

**Licence:** `MIT`

**Source:** [`projects/landscape/zirui-claude-skills.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/zirui-claude-skills.yml)

## Positioning

A personal Claude Code skill pack of 21 skills for empirical economics/finance research, split into six legacy "/command"-style skills (robustness checklist, literature review, coding guidelines, data documentation, project structure, referee response) and fifteen newer agent-skill-format skills organised into four groups: an empirical pipeline group (table regeneration, pipeline refresh, Stata-preflight, robustness-battery, spec-curve-sweep, power-first), a verification group (verify-claims, verify-numbers-pipeline, referee-panel), a LaTeX/Overleaf sync group, and a cross-model-review group built on Claude-Codex plan debate.

## Distinctive contribution

Unlike most cataloged economics skill packs, this one's centre of gravity is runtime numerical assurance rather than drafting or literature work: verify-numbers-pipeline builds a YAML claim manifest of every reported statistic plus a verify_numbers.py checker wired to a git pre-commit hook that blocks a commit containing a stale number, and referee-panel runs five parallel adversarial reviewers (identification, power, literature, provenance, independent replication) into one ranked threat memo. spec-curve-sweep operationalises a 200-500-specification sweep with a resumable runner and drafted online appendix — a concrete, code-backed version of specification-curve analysis rarely automated elsewhere in this catalog.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Seven distinct stages (literature synthesis, research design via plan-debate, data analysis/robustness, code generation, revision, referee simulation, Overleaf dissemination), but no literature-discovery, hypothesis-generation, or from-scratch paper-drafting skill. |
| Autonomy level | 1 | Verification and referee skills surface findings (UNVERIFIED tags, threat memos) for the researcher to act on; the pre-commit hook blocks rather than auto-fixes. |
| Architectural transparency | 3 | All 21 skills are public Markdown/YAML-frontmatter files; verify-numbers-pipeline additionally ships a concrete verify_numbers.py script and Makefile target. |
| Inputs supported | 2 | Multiple input forms (paper draft, Stata/Python pipeline, Overleaf project, referee report) with execution/data access via the pipeline-refresh and table-regeneration skills; no literature-corpus or external-API access documented. |
| Outputs / reproducibility | 2 | verify-numbers-pipeline's claim manifest plus pre-commit gate is a genuine traceability mechanism, but there is no single declared end-to-end reproduce-from-inputs path across the whole pack. |
| Internal evaluation | 1 | referee-panel and verify-claims provide internal adversarial checks on a given paper, but the pack itself has no reported benchmark or external evaluation. |
| Openness | 2 | MIT license; skills are plain Markdown/Python but assume placeholder paths, a Stata installation, and (for three skills) a separate Codex CLI setup. |
| Maturity / traction | 1 | 17 stars, a GitHub Actions badge auto-counting skills (some upkeep automation), single maintainer, pre-1.0. |
| Cross-family policy | 1 | A dedicated 'cross-model review' skill group (codex-bridge, codex-review-plan, review-codex-plan, plan-debate) runs Claude against Codex, but it is a separately-invoked optional skill set, not the default path for the pack's other 17 skills. |
| Runtime assurance | 3 | verify-numbers-pipeline gates commits on a machine-checkable claim manifest; verify-claims marks every unverifiable number/citation UNVERIFIED; referee-panel and power-first add identification/power checks before any coefficient is interpreted — a genuinely heavy in-pipeline audit stack with gating on failure. |
| Cross-platform portability | 1 | Claude Code primary, with Codex CLI as a documented secondary backend for the cross-model-review group; no other IDEs/providers. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-synthesis` `research-design` `data-analysis` `code-generation` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `multi-agent` `debate-consensus` `tool-use` `iterative-loop`


**Inputs:** `paper-draft` `stata-python-pipeline` `overleaf-project` `referee-report`


**Outputs:** `robustness-table` `verified-claim-manifest` `referee-threat-memo` `revised-latex-document` `referee-response-letter`


## Limitations

- Single-maintainer personal project; two overlapping skill formats (legacy '/command' .md files vs. newer agent-skill folders) in the same repo could confuse adoption.
- Placeholders (paths, usernames, example coefficients) require manual substitution per project.
- No external benchmark validates the verification claims (verify-claims, referee-panel) themselves — their rigor is asserted, not measured.
- Codex-dependent skills require a separate Codex CLI install and API key.

## Related projects in this catalog

- [`econtools`](econtools.md)
- [`econ-skills`](econ-skills.md)
- [`ai-research-feedback`](ai-research-feedback.md)
- [`aris`](aris.md)
