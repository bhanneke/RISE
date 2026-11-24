<!-- DO NOT EDIT — auto-generated from skills/aris.yml by scripts/build_skills_index.py -->

# ARIS skills

license: `MIT` · 87 skills · last update: 2026-11-24

**Source:** <https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep>

**Maintainers:** Yang, Ruofeng, Li, Yongcan, Li, Shuai

**Related project entry:** [`aris`](../projects/aris.md)

**Compatibility:** `claude-code` `codex` `cursor` `trae` `antigravity` `openclaw` `copilot-cli` `windsurf` `agnostic`

> 74+ Markdown SKILL.md files designed around cross-model adversarial collaboration. Framework-agnostic by design. Refresh 2026-11-24 (upstream pushed 2026-11-24): re-copied the 76 SKILL.md files that differ from the upstream HEAD; dropped 4 manifest entries that have no SKILL.md at those paths at HEAD (shared-references, skills-codex, skills-codex-claude-review, skills-codex-gemini-review - mirror directories, not skills); added 11 first-party skills (citation-crosscheck, firecrawl-search, integrity-forensics, keenable-search, lean-formalize, meta-apply, paper-poster-html, proof-orchestrator, research-implement-feature, web-debug-search, wiki-enrich). The skills/skills-codex* directories hold Codex-runtime variants of the same skills and are not catalogued separately. paper-poster is now a deprecated redirect to paper-poster-html.

**Source YAML:** [`skills/aris.yml`](https://github.com/bhanneke/RISE/blob/main/skills/aris.yml)

## Skills

### `analysis` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`analyze-results`](aris/analyze-results.md) | — | `data-analysis` | — | [view](aris/analyze-results.md) | — | — |

### `audit` (9)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`citation-audit`](aris/citation-audit.md) | — | `referee-simulation` | — | [view](aris/citation-audit.md) | — | — |
| [`citation-crosscheck`](aris/citation-crosscheck.md) | — | `revision-editing` | Double-blind bibliographic cross-check: one agent extracts each cited entry verbatim from the local .bib, a second independently re-fetches the same paper's record from the web while blind to the .bib, and a third extractor emits… | [view](aris/citation-crosscheck.md) | — | — |
| [`claims-drafting`](aris/claims-drafting.md) | — | `referee-simulation` | — | [view](aris/claims-drafting.md) | — | — |
| [`experiment-audit`](aris/experiment-audit.md) | — | `referee-simulation` | — | [view](aris/experiment-audit.md) | — | — |
| [`integrity-forensics`](aris/integrity-forensics.md) | — | `referee-simulation` | Runs an integrity-forensics sweep over a paper (span-anchored evidence ledger, model auditors, rules-only reporter) and turns the verdict into a typed pass/warn/block gate with an obligations ledger. | [view](aris/integrity-forensics.md) | — | — |
| [`novelty-check`](aris/novelty-check.md) | — | `referee-simulation` | — | [view](aris/novelty-check.md) | — | — |
| [`paper-claim-audit`](aris/paper-claim-audit.md) | — | `referee-simulation` | — | [view](aris/paper-claim-audit.md) | — | — |
| [`patent-novelty-check`](aris/patent-novelty-check.md) | — | `referee-simulation` | — | [view](aris/patent-novelty-check.md) | — | — |
| [`result-to-claim`](aris/result-to-claim.md) | — | `referee-simulation` | — | [view](aris/result-to-claim.md) | — | — |

### `code-gen` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`experiment-bridge`](aris/experiment-bridge.md) | — | `code-generation` | — | [view](aris/experiment-bridge.md) | — | — |
| [`experiment-queue`](aris/experiment-queue.md) | — | `code-generation` | — | [view](aris/experiment-queue.md) | — | — |
| [`research-implement-feature`](aris/research-implement-feature.md) | — | `code-generation` | Builds a working artifact from a plain implementation request: an end-to-end spine first, then one feature per step, with every under-determined decision logged in an assumption ledger before the code that depends on it. | [view](aris/research-implement-feature.md) | — | — |

### `design` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`ablation-planner`](aris/ablation-planner.md) | — | `research-design` | — | [view](aris/ablation-planner.md) | — | — |
| [`experiment-plan`](aris/experiment-plan.md) | — | `research-design` | — | [view](aris/experiment-plan.md) | — | — |
| [`paper-plan`](aris/paper-plan.md) | — | `research-design` | — | [view](aris/paper-plan.md) | — | — |

### `drafting` (25)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`dse-loop`](aris/dse-loop.md) | — | `paper-drafting` | — | [view](aris/dse-loop.md) | — | — |
| [`embodiment-description`](aris/embodiment-description.md) | — | `paper-drafting` | — | [view](aris/embodiment-description.md) | — | — |
| [`grant-proposal`](aris/grant-proposal.md) | — | `paper-drafting` | — | [view](aris/grant-proposal.md) | — | — |
| [`interview-cheatsheet`](aris/interview-cheatsheet.md) | — | `paper-drafting` | — | [view](aris/interview-cheatsheet.md) | — | — |
| [`invention-structuring`](aris/invention-structuring.md) | — | `paper-drafting` | — | [view](aris/invention-structuring.md) | — | — |
| [`jurisdiction-format`](aris/jurisdiction-format.md) | — | `paper-drafting` | — | [view](aris/jurisdiction-format.md) | — | — |
| [`kill-argument`](aris/kill-argument.md) | — | `paper-drafting` | — | [view](aris/kill-argument.md) | — | — |
| [`monitor-experiment`](aris/monitor-experiment.md) | — | `paper-drafting` | — | [view](aris/monitor-experiment.md) | — | — |
| [`paper-compile`](aris/paper-compile.md) | — | `paper-drafting` | — | [view](aris/paper-compile.md) | — | — |
| [`paper-illustration`](aris/paper-illustration.md) | — | `paper-drafting` | — | [view](aris/paper-illustration.md) | — | — |
| [`paper-illustration-image2`](aris/paper-illustration-image2.md) | — | `paper-drafting` | — | [view](aris/paper-illustration-image2.md) | — | — |
| [`paper-poster`](aris/paper-poster.md) | — | `paper-drafting` | Deprecated upstream: now only a redirect to paper-poster-html. | [view](aris/paper-poster.md) | — | — |
| [`paper-write`](aris/paper-write.md) | — | `paper-drafting` | — | [view](aris/paper-write.md) | — | — |
| [`paper-writing`](aris/paper-writing.md) | — | `paper-drafting` | — | [view](aris/paper-writing.md) | — | — |
| [`patent-pipeline`](aris/patent-pipeline.md) | — | `paper-drafting` | — | [view](aris/patent-pipeline.md) | — | — |
| [`pixel-art`](aris/pixel-art.md) | — | `paper-drafting` | — | [view](aris/pixel-art.md) | — | — |
| [`qzcli`](aris/qzcli.md) | — | `paper-drafting` | — | [view](aris/qzcli.md) | — | — |
| [`render-html`](aris/render-html.md) | — | `paper-drafting` | — | [view](aris/render-html.md) | — | — |
| [`run-experiment`](aris/run-experiment.md) | — | `paper-drafting` | — | [view](aris/run-experiment.md) | — | — |
| [`serverless-modal`](aris/serverless-modal.md) | — | `paper-drafting` | — | [view](aris/serverless-modal.md) | — | — |
| [`specification-writing`](aris/specification-writing.md) | — | `paper-drafting` | — | [view](aris/specification-writing.md) | — | — |
| [`system-profile`](aris/system-profile.md) | — | `paper-drafting` | — | [view](aris/system-profile.md) | — | — |
| [`training-check`](aris/training-check.md) | — | `paper-drafting` | — | [view](aris/training-check.md) | — | — |
| [`vast-gpu`](aris/vast-gpu.md) | — | `paper-drafting` | — | [view](aris/vast-gpu.md) | — | — |
| [`writing-systems-papers`](aris/writing-systems-papers.md) | — | `paper-drafting` | — | [view](aris/writing-systems-papers.md) | — | — |

### `figures` (4)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`figure-description`](aris/figure-description.md) | — | `paper-drafting` | — | [view](aris/figure-description.md) | — | — |
| [`figure-spec`](aris/figure-spec.md) | — | `paper-drafting` | — | [view](aris/figure-spec.md) | — | — |
| [`mermaid-diagram`](aris/mermaid-diagram.md) | — | `paper-drafting` | — | [view](aris/mermaid-diagram.md) | — | — |
| [`paper-figure`](aris/paper-figure.md) | — | `paper-drafting` | — | [view](aris/paper-figure.md) | — | — |

### `ideation` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`idea-creator`](aris/idea-creator.md) | — | `rq-formulation` `hypothesis-generation` | — | [view](aris/idea-creator.md) | — | — |
| [`idea-discovery`](aris/idea-discovery.md) | — | `rq-formulation` `hypothesis-generation` | — | [view](aris/idea-discovery.md) | — | — |
| [`idea-discovery-robot`](aris/idea-discovery-robot.md) | — | `rq-formulation` `hypothesis-generation` | — | [view](aris/idea-discovery-robot.md) | — | — |

### `infra` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`feishu-notify`](aris/feishu-notify.md) | — |  | — | [view](aris/feishu-notify.md) | — | — |
| [`web-debug-search`](aris/web-debug-search.md) | — |  | Searches GitHub, Stack Exchange, developer communities and official documentation for software errors, compatibility problems and workarounds. | [view](aris/web-debug-search.md) | — | — |

### `literature` (16)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`alphaxiv`](aris/alphaxiv.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/alphaxiv.md) | — | — |
| [`arxiv`](aris/arxiv.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/arxiv.md) | — | — |
| [`deepxiv`](aris/deepxiv.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/deepxiv.md) | — | — |
| [`exa-search`](aris/exa-search.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/exa-search.md) | — | — |
| [`firecrawl-search`](aris/firecrawl-search.md) | — | `literature-discovery` | Web search and page scraping via Firecrawl, returning full-page markdown. | [view](aris/firecrawl-search.md) | — | — |
| [`gemini-search`](aris/gemini-search.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/gemini-search.md) | — | — |
| [`keenable-search`](aris/keenable-search.md) | — | `literature-discovery` | Keyless web search and page fetch via Keenable. | [view](aris/keenable-search.md) | — | — |
| [`openalex`](aris/openalex.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/openalex.md) | — | — |
| [`prior-art-search`](aris/prior-art-search.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/prior-art-search.md) | — | — |
| [`research-lit`](aris/research-lit.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/research-lit.md) | — | — |
| [`research-pipeline`](aris/research-pipeline.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/research-pipeline.md) | — | — |
| [`research-refine`](aris/research-refine.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/research-refine.md) | — | — |
| [`research-refine-pipeline`](aris/research-refine-pipeline.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/research-refine-pipeline.md) | — | — |
| [`research-wiki`](aris/research-wiki.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/research-wiki.md) | — | — |
| [`semantic-scholar`](aris/semantic-scholar.md) | — | `literature-discovery` `literature-synthesis` | — | [view](aris/semantic-scholar.md) | — | — |
| [`wiki-enrich`](aris/wiki-enrich.md) | — | `literature-synthesis` | Fills in the per-paper TODO sections of research-wiki pages that literature-ingest skills leave as bare scaffolds. | [view](aris/wiki-enrich.md) | — | — |

### `meta` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`auto-paper-improvement-loop`](aris/auto-paper-improvement-loop.md) | — |  | — | [view](aris/auto-paper-improvement-loop.md) | — | — |
| [`meta-apply`](aris/meta-apply.md) | — |  | Privileged applier that lands approved meta-optimize patches into the skill corpus, with a cross-model jury and human approval at landing. | [view](aris/meta-apply.md) | — | — |
| [`meta-optimize`](aris/meta-optimize.md) | — |  | — | [view](aris/meta-optimize.md) | — | — |

### `modeling` (5)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`formula-derivation`](aris/formula-derivation.md) | — | `formal-modeling` | — | [view](aris/formula-derivation.md) | — | — |
| [`lean-formalize`](aris/lean-formalize.md) | — | `formal-modeling` | Develop and verify a mathematical proof in Lean, continue an incomplete Lean project, or audit whether it proves the original statement. | [view](aris/lean-formalize.md) | — | — |
| [`proof-checker`](aris/proof-checker.md) | — | `formal-modeling` | — | [view](aris/proof-checker.md) | — | — |
| [`proof-orchestrator`](aris/proof-orchestrator.md) | — | `formal-modeling` | Manages a stateful, run-directory-based proof project across runs, including manual handoff packages when a local attempt stalls. | [view](aris/proof-orchestrator.md) | — | — |
| [`proof-writer`](aris/proof-writer.md) | — | `formal-modeling` | — | [view](aris/proof-writer.md) | — | — |

### `review` (6)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`auto-review-loop`](aris/auto-review-loop.md) | — | `referee-simulation` | — | [view](aris/auto-review-loop.md) | — | — |
| [`auto-review-loop-llm`](aris/auto-review-loop-llm.md) | — | `referee-simulation` | — | [view](aris/auto-review-loop-llm.md) | — | — |
| [`auto-review-loop-minimax`](aris/auto-review-loop-minimax.md) | — | `referee-simulation` | — | [view](aris/auto-review-loop-minimax.md) | — | — |
| [`comm-lit-review`](aris/comm-lit-review.md) | — | `referee-simulation` | — | [view](aris/comm-lit-review.md) | — | — |
| [`patent-review`](aris/patent-review.md) | — | `referee-simulation` | — | [view](aris/patent-review.md) | — | — |
| [`research-review`](aris/research-review.md) | — | `referee-simulation` | — | [view](aris/research-review.md) | — | — |

### `revision` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`rebuttal`](aris/rebuttal.md) | — | `revision-editing` | — | [view](aris/rebuttal.md) | — | — |

### `slides` (4)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`paper-poster-html`](aris/paper-poster-html.md) | — | `dissemination` | Builds a conference poster as a single HTML/CSS file with measurement-driven layout checks and a print-ready PDF; upstream now treats it as the default poster pipeline. | [view](aris/paper-poster-html.md) | — | — |
| [`paper-slides`](aris/paper-slides.md) | — | `dissemination` | — | [view](aris/paper-slides.md) | — | — |
| [`paper-talk`](aris/paper-talk.md) | — | `dissemination` | — | [view](aris/paper-talk.md) | — | — |
| [`slides-polish`](aris/slides-polish.md) | — | `dissemination` | — | [view](aris/slides-polish.md) | — | — |

### `submission` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`overleaf-sync`](aris/overleaf-sync.md) | — | `dissemination` | — | [view](aris/overleaf-sync.md) | — | — |
| [`resubmit-pipeline`](aris/resubmit-pipeline.md) | — | `dissemination` | — | [view](aris/resubmit-pipeline.md) | — | — |
