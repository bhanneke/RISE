<!-- DO NOT EDIT — auto-copied from skills/auto-empirical-research-skills/details/aers-router.md -->

# `auto-empirical-research-skills`

Root router for whole-repo installs — classifies an empirical-research request by stage/method and dispatches to one of the 1,094 vendored skills via catalog JSON lookups instead of reading the repo wholesale.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../auto-empirical-research-skills/">Auto-Empirical Research Skills (AERS) — first-party skills</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>CC BY-SA 4.0 (repo default); MIT for the mirrored first-party collections (StatsPAI, AER-skills, Paper-WorkFlow)</code></div><div><b>Updated:</b> 2026-07-22</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Auto-Empirical-Research-Skills/contents/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/auto-empirical-research-skills/aers-router/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Auto-Empirical-Research-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Auto-Empirical Research Skills Router

Use this root skill when the full AERS repository has been installed as a single skill folder. Treat it as a router and catalog, not as a request to load every vendored `SKILL.md`.

The catalog holds **1,094 skills across 74 vendored collections**. Never read them all — route to one, then load only that skill's `SKILL.md`.

### Workflow

1. Classify the user's empirical-research task by **stage**, then load the single best-matching skill:
   - Full pipeline or orchestration: start with `skills/69-Paper-WorkFlow/` or the `skills/00.*` flagship analysis skills (StatsPAI / Python / Stata / R).
   - Causal inference and econometrics: pick by method from the table below, or search `catalog/skills.json` / `docs/TAXONOMY.md`.
   - AER or top economics journal work: start with `skills/50-brycewang-aer-skills/`.
   - Replication, citation, or peer review: use `docs/SKILL_CATALOG.md` and `docs/GOLDEN_WORKFLOWS.md` to choose a focused skill.
   - Chinese academic de-AIGC or academic rewriting: start with `skills/48-copaper-ai-chinese-de-aigc/` or nearby writing skills in the catalog.
2. Read only the selected child skill's `SKILL.md`, then follow its progressive-disclosure instructions for `references/`, `scripts/`, `assets/`, or templates.
3. If no child skill clearly matches, inspect `catalog/skills.json` first (has `path`, `name`, `description`, `line_count`, and a globally-unique `qualified_name`), then `docs/SKILL_CATALOG.md`. For richer filtering (topic `tags`, `quality_score`, `license`, `commercial_use`), use `catalog/skills-enriched.json`. Avoid broad recursive reads of `skills/`.
   - Both catalog JSON files are large (roughly 1 MB / 20k lines each) — query them instead of reading them whole. Example:

     ```bash
     python3 -c "import json; [print(s['qualified_name'], '->', s['path']) for s in json.load(open('catalog/skills.json'))['skills'] if 'synthetic control' in (s['name'] + ' ' + s['description']).lower()]"
     ```

     A plain `grep -in "synthetic control" catalog/skills.json` works too when a rough match is enough.
4. For installation help, use `docs/INSTALL.md` for Codex-style copy installs and `INSTALL.md` for Claude Code marketplace/plugin installs.
5. If editing this repository, keep parent and nested repos separate. In particular, inspect `git status` inside `skills/69-Paper-WorkFlow/` (a git submodule) before touching it.

### Method → where to start

Match the user's identification strategy or task to a starting collection, then confirm against `catalog/skills.json`:

| Task / method | Start here |
|---|---|
| Full paper pipeline (orchestrator) | `skills/69-Paper-WorkFlow/` |
| DiD / staggered DiD / event study | `skills/50-brycewang-aer-skills/`, `skills/10-Jill0099-causal-inference-mixtape/`, `skills/13-scunning1975-MixtapeTools/` |
| Instrumental variables (IV) | `skills/50-brycewang-aer-skills/`, `skills/40-py-econometrics-pyfixest/` |
| Regression discontinuity (RDD) | `skills/50-brycewang-aer-skills/`, `skills/10-Jill0099-causal-inference-mixtape/` |
| Synthetic control (SCM) | `skills/50-brycewang-aer-skills/`, `skills/13-scunning1975-MixtapeTools/` |
| Panel fixed effects | `skills/40-py-econometrics-pyfixest/`, `skills/39-vincentarelbundock-marginaleffects/` |
| Matching / propensity scores | `skills/10-Jill0099-causal-inference-mixtape/`, `skills/11-James-Traina-compound-science/` |
| Structural estimation | `skills/11-James-Traina-compound-science/`, `skills/14-luischanci-claude-code-research-starter/` |
| Time series / forecasting | `skills/17-DAAF-Contribution-Community-daaf/`, `skills/43-wentorai-research-plugins/` |
| Text as data / NLP | `skills/43-wentorai-research-plugins/` |
| Spatial / GIS analysis | `skills/17-DAAF-Contribution-Community-daaf/`, `skills/43-wentorai-research-plugins/` |
| Experiments / RCT design | `skills/11-James-Traina-compound-science/`, `skills/25-HosungYou-Diverga/` |
| Survey / questionnaire design | `skills/43-wentorai-research-plugins/`, `skills/25-HosungYou-Diverga/` |
| DML / CATE / causal forests | `skills/00.1-Full-empirical-analysis-skill_Python/`, `skills/63-tondevrel-scientific-agent-skills/` |
| Bayesian modeling | `skills/23-Learning-Bayesian-Statistics-baygent-skills/`, `skills/51-pymc-labs-CausalPy/` |
| Stata analysis | `skills/00.2-Full-empirical-analysis-skill_Stata/`, `skills/32-dylantmoore-stata-skill/`, `skills/64-tmonk-mcp-stata/` |
| R analysis | `skills/00.3-Full-empirical-analysis-skill_R/`, `skills/55-ab604-claude-code-r-skills/` |
| Game theory / theory papers | `skills/65-game-theory-paper-writer/` |
| Qualitative / thematic analysis | `skills/53-keemanxp-thematic-analysis-skill/` |
| Data acquisition (SEC filings, open data) | `skills/57-dgunning-edgartools/`, `skills/59-shiquda-openalex-skill/` |
| Literature review | `skills/36-taoyunudt-literature-review-skill/`, `skills/52-keemanxp-slr-prisma/`, `skills/59-shiquda-openalex-skill/` |
| Citation checking | `skills/62-PHY041-claude-skill-citation-checker/` |
| Manuscript writing / proofreading | `skills/04-K-Dense-AI-claude-scientific-writer/`, `skills/38-peternka-academic-proofreader/` |
| Peer review / referee reports / referee responses | `skills/21-claesbackman-AI-research-feedback/`, `skills/12-pedrohcgs-claude-code-my-workflow/`, `skills/67-econfin-workflow-toolkit/` |
| LaTeX / Quarto compilation, slides | `skills/08-ndpvt-web-latex-document-skill/`, `skills/60-regisely-superpapers/`, `skills/12-pedrohcgs-claude-code-my-workflow/` |
| De-AIGC / humanize | `skills/48-copaper-ai-chinese-de-aigc/`, `skills/45-stephenturner-skill-deslop/`, `skills/47-conorbronsdon-avoid-ai-writing/` |
| Chinese SSCI/CSSCI journal polishing | `skills/70-ssci-polish/`, `skills/49-voidborne-d-humanize-chinese/` |
| Replication | `skills/28-maxwell2732-paper-replicate-agent-demo/`, `skills/29-quarcs-lab-project20XXy/` |
| Open science / reproducibility | `skills/54-scdenney-open-science-skills/`, `skills/29-quarcs-lab-project20XXy/` |
| Grant proposals / funding | `skills/42-wanshuiyin-ARIS/`, `skills/43-wentorai-research-plugins/` |
| Conference posters / post-acceptance | `skills/42-wanshuiyin-ARIS/`, `skills/33-Galaxy-Dawn-claude-scholar/` |

### Full-pipeline trigger

If the user is asking for a complete empirical paper from idea to submission, route to `skills/69-Paper-WorkFlow/`. The orchestrator loads the right skill at the right stage and stops for human decisions at the two hard gates (Method Gate after Stage 3, Draft Quality Gate after Stage 7).

Trigger phrases (any one is enough to dispatch to the orchestrator):

- `/paper-workflow`
- "帮我写一篇实证论文"
- "从选题到投稿"
- "end-to-end empirical paper"
- "完整复现"
- "from proposal to submission"

The orchestrator is **not** the right entry point for a single-task ask (e.g. "fit a DiD", "recode this variable", "write a referee report") — those are listed in the Method → where to start table above.

### Coverage Notes

- `skills/69-Paper-WorkFlow/` is a **git submodule**. If its folder is empty, the copy or clone skipped submodules (`git submodule update --init` fixes a clone); fall back to the `skills/00.*` flagship pipeline skills, which are vendored directly.
- The vendored ARIS collection (`skills/42-wanshuiyin-ARIS/`) also ships its skill set as OpenAI Codex CLI runtime ports (`skills-codex*` subtrees). Those stay on disk but are excluded from `catalog/skills.json` (see `scripts/skill_discovery.py`) — route Claude agents to the primary `skills/` tree only.

### Install Notes

- Whole-repo imports are supported by this root `SKILL.md` as a lightweight compatibility entry point.
- Individual skill installs are still preferred when a runtime expects one folder per skill. Copy the folder that directly contains the target `SKILL.md`.
- Do not copy the repository root into a runtime and expect every child skill to become individually registered unless that runtime explicitly supports recursive skill discovery.
- **Name collisions:** the catalog contains 47 bare `name`s shared across collections (e.g. `data-analysis`, `lit-review`, `proofread`). When a runtime registers skills by flat name, install one collection at a time, or disambiguate with the globally-unique `qualified_name` field in `catalog/skills.json` (`<collection>::<name>`, e.g. `12-pedrohcgs-claude-code-my-workflow::data-analysis`), or the full `skills/<collection>/.../SKILL.md` path.

### Key Files

- `catalog/skills.json`: machine-readable list of vendored skills.
- `catalog/skills-enriched.json`: same list plus `tags`, `quality_score`, `license`, and `commercial_use` for filtering.
- `docs/SKILL_CATALOG.md`: human-readable skill index.
- `docs/TAXONOMY.md`: task and method taxonomy.
- `docs/GOLDEN_WORKFLOWS.md`: ready-to-use empirical-research prompts.
- `docs/INSTALL.md`: runtime installation guidance for single-skill and whole-repo use.
