<!-- DO NOT EDIT — auto-generated from projects/landscape/auto-empirical-research-skills.yml by scripts/build_indexes.py -->

# Auto-Empirical Research Skills (AERS)

`external` · status: `active` · focus: `end-to-end` · discipline: `social-sciences` · started: 2026

**Project page:** <https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills>

**Source:** [`projects/landscape/auto-empirical-research-skills.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/auto-empirical-research-skills.yml)

## Positioning

A Claude-plugin-structured mega-catalog of agent skills for empirical social-science research: 74 collections / 1,094 vendored skills — 7 first-party Stanford REAP × CoPaper.AI collections (including the StatsPAI causal engine and the Paper-WorkFlow meta-orchestrator) plus 67 curated, security-audited community collections — spanning topic refinement, literature review, data acquisition, identification strategy, estimation (Python/Stata/R), robustness audit, publication tables, writing, review simulation, AI-trace removal, and journal submission. The headline "23,000+ skills" refers to an accompanying awesome-list map of 119 ecosystem repos; the vendored, cataloged content is 1,094 skills.

## Distinctive contribution

The largest empirical-social-science skills distribution in the catalog, and unusually serious about verification for a skills list: a numeric benchmark of 17 tasks whose gold values are recomputed from real data each run (encoding classic traps such as the LaLonde naive-ATT sign flip and Card IV recovery), a behavioral eval harness (37 scenarios / 183 rubric items), per-skill provenance and license audits in catalog JSON, and a root SKILL.md router so 1,094 skills are dispatched without flooding context. Vendors several standalone entries of this catalog (clo-author, academic-research-skills) as collections.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | 12 declared stages from RQ refinement through submission, including paper-drafting and referee-simulation; the 9-stage flagship pipeline maps skills to every stage. |
| Autonomy level | 2 | Paper-WorkFlow meta-orchestrator claims one-command idea-to-draft runs with optional human takeover at each persisted stage; most collections are copilot-style skills a human invokes. |
| Architectural transparency | 3 | All 1,094 skills vendored as public markdown/code, catalog JSON with provenance and per-skill audit, benchmark and eval harness fully public with CI. |
| Inputs supported | 2 | Topic / draft / dataset inputs; literature (OpenAlex) and data connectors (EDGAR) exist but live in heterogeneous vendored collections rather than one unified interface. |
| Outputs / reproducibility | 2 | Artifact-idempotent pipeline persists code, tables, and drafts at each stage; end-to-end reproducibility demonstrated only for reference implementations, not arbitrary papers. |
| Internal evaluation | 2 | 17 numeric benchmark tasks with data-recomputed golds plus 37-scenario/183-item eval harness in CI — but these score the reference pipelines, not typical agent output, and there is no external validation. |
| Openness | 2 | CC BY-SA 4.0 (copyleft, commercial use allowed); vendored collections keep their own licenses, tracked in a published license audit. |
| Maturity / traction | 2 | 3,029 stars / 399 forks within ~4 months, five-language docs, commercial deployment via CoPaper.AI — but too young for 'sustained' adoption. |
| Cross-family policy | 0 | Runtime manifests target multiple providers, but no cross-model-family review or verification mechanism exists. |
| Runtime assurance | 1 | Audit-style stages (10-item replication-package check, proofreading, AI-trace audits) run inside the flagship pipeline, but no documented gate-blocking on failure. |
| Cross-platform portability | 3 | Skills-as-markdown with a router SKILL.md and deployment manifests for Claude Code, Cursor, Aider, CodeBuddy, and OpenAI/Codex-style runtimes. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `literature-discovery` `literature-synthesis` `data-acquisition` `research-design` `data-analysis` `code-generation` `replication` `paper-drafting` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `tool-use` `artifact-versioning`


**Inputs:** `research-topic` `user-dataset` `paper-draft`


**Outputs:** `paper-draft` `analysis-code` `publication-tables` `figures` `replication-audit-report`


**Data sources:** `user-provided` `sec-edgar`


**Knowledge sources:** `openalex`


## Limitations

- The repo description's '23,000+ skills' counts an awesome-list ecosystem map (119 repos); the repo vendors 1,094 skills across 74 collections — the README is explicit about this distinction, the GitHub description is not.
- Roughly 90% of collections are vendored third-party work of heterogeneous quality; only the 7 first-party collections are behaviorally pinned by the numeric benchmark.
- Chinese-first documentation (default README) and CC BY-SA copyleft stacked on per-collection upstream licenses complicate reuse for some audiences.

## Related projects in this catalog

- [`statspai`](statspai.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`clo-author`](clo-author.md)
- [`research-paper-writing-skills`](research-paper-writing-skills.md)
