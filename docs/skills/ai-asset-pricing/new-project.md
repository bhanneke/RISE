<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/new-project.md -->

# `/new-project`

Scaffolds a new empirical project folder with LaTeX, code, scripts, results, literature and guidance subfolders plus a README and a project-level CLAUDE.md.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-04-19</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/new-project/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/new-project/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/new-project/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Create New Research Project

Four phases: **Validate → Gather Context → Create Scaffold → Setup Paper**.

### Examples

- `/new-project momentum_replication` -- create project with name only
- `/new-project vol_surface "Implied volatility surface dynamics"` -- name + description
- `/new-project bond_liquidity` -- another example

### Phase 1: Validate Input

Parse `$ARGUMENTS`:
- **First token** = project name
- **Remaining tokens** (if any) = optional description text

If `$ARGUMENTS` is empty, use `AskUserQuestion` to ask:
> "What should the project be called? Use lowercase with underscores (e.g., `momentum_replication`, `vol_surface`, `bond_liquidity`)."

**Validation rules:**
- Must match regex: `^[a-z][a-z0-9_]{1,49}$` (lowercase, underscores only, starts with letter, 2-50 chars)
- Reject Windows-reserved names: `con`, `prn`, `aux`, `nul`, `com1`-`com9`, `lpt1`-`lpt9`
- If invalid, explain the rules, show examples, and re-ask

**Collision check:**
- If `projects/<name>/` already exists, ask the user: "Project `<name>` already exists. Do you want to open it, or choose a different name?"
- Do NOT overwrite existing projects

### Phase 2: Gather Context

If no description was provided in `$ARGUMENTS`, use a **single** `AskUserQuestion` with these questions:
1. "Brief description of the project (1-2 sentences):"
2. "Which WRDS databases will this project use? (e.g., CRSP, OptionMetrics, Compustat, TAQ, Bonds, JKP)"
3. "Any initial methodology notes or reminders for this project?"

If a description WAS provided in `$ARGUMENTS`, still ask questions 2 and 3.

Store the answers for template filling.

### Phase 3: Create Scaffold

#### 3a. Create directories

Run a single Bash command:
```bash
mkdir -p projects/<name>/{latex,code,scripts/tests,results/{figures,tables},literature,guidance,_misc}
```

#### 3b. Write project README.md

Use the Write tool to create `projects/<name>/README.md`:

```markdown
## {Project Name in Title Case}

{User's description}

### Status

- [ ] Data sourced
- [ ] Exploratory analysis complete
- [ ] Main results produced
- [ ] Write-up drafted
- [ ] Write-up finalized

### Data Dependencies

This project uses datasets from the global `data/` folder:

| Dataset | Description | Status |
|---------|-------------|--------|
| *(to be filled as data is fetched)* | | |

### Structure

| Folder | Purpose |
|--------|---------|
| `latex/` | LaTeX writeup |
| `code/` | Production code (clean, reusable) |
| `scripts/tests/` | Exploratory investigations (each in own subfolder with `output/`) |
| `results/` | Publication-ready figures and tables |
| `literature/` | Reference papers |
| `guidance/` | Methodology notes |
| `_misc/` | Catch-all |

### Notes

- Created: {today's date, YYYY-MM-DD}
- WRDS databases: {databases}
```

#### 3c. Write project CLAUDE.md

Use the Write tool to create `projects/<name>/CLAUDE.md`:

```markdown
### Project: {project_name}

{User's description}

### Data Sources

WRDS databases: {databases}

Data is pulled from the global `data/` folder. Datasets used by this project:
- *(list grows as data is fetched)*

### Conventions

#### Scripts and Tests
- Exploratory work goes in `scripts/tests/{test_name}/`
- Each test gets its own subfolder with an `output/` dir for all artifacts
- Name test folders descriptively: `summary_stats`, `return_predictability`, `cross_section_reg`, etc.

#### Output Formats
- **Figures:** PNG (300 DPI) for drafts, PDF for final versions in `results/figures/`
- **Figure generation:** Use `docs/ai/figures.md` and `fintools.figures`; use
  `style="fins"` for house-style publication plots and `style="ft"` for
  FT-style output
- **Tables:** LaTeX `.tex` for the paper, CSV for debugging
- **Final outputs** for the paper go in `results/figures/` and `results/tables/`

#### Code
- `code/` = clean, reusable production code
- `scripts/` = one-off investigations and scratch work
- Import from `code/` into `scripts/`, never the reverse

#### LaTeX
- Main document: `latex/main.tex`
- Reference results: `../results/figures/`, `../results/tables/`
- BibTeX: `latex/references.bib`

### Paper-Specific Terminology

*(Define paper-specific preferred/banned terms here. Example:)*
| Use | Instead of | Reason |
|-----|------------|--------|
| *(e.g., "execution risk")* | *(e.g., "trading friction")* | *(our umbrella term)* |

### LaTeX Section Keys

*(Register `%% BEGIN/END` section marker keys here for `/latex-doctor` verification.)*
| Key | Section |
|-----|---------|
| `introduction` | Introduction |

### Target Journal

*(e.g., JF, RFS, JFE — used by `/submission-prep` for journal-specific checks.)*

### Key Claims to Verify at Submission

*(List the main quantitative claims that `/submission-prep` should verify against tables/text.)*
- *(e.g., "58 of 341 factors are significant at 5%")*

### Project-Specific Instructions

{User's notes, or "None yet -- add methodology reminders, conventions, or constraints here."}
```

#### 3d. Write project .gitignore

Use the Write tool to create `projects/<name>/.gitignore`:

```gitignore
## LaTeX build artifacts
latex/*.aux
latex/*.bbl
latex/*.blg
latex/*.log
latex/*.out
latex/*.fdb_latexmk
latex/*.fls
latex/*.synctex.gz
latex/*.toc

## Python
__pycache__/
*.pyc
.ipynb_checkpoints/

## R
.Rhistory
.RData

## OS
.DS_Store
Thumbs.db
```

#### 3e. Print scaffold summary

Print the directory tree to the user:

```
### Project Created: {project_name}

projects/{project_name}/
  README.md
  CLAUDE.md
  .gitignore
  latex/
  code/
  scripts/
    tests/
  results/
    figures/
    tables/
  literature/
  guidance/
  _misc/
```

### Phase 4: Setup Paper

After printing the scaffold summary, ask the user:

> "Set up the LaTeX paper now? This copies the boilerplate template into `latex/` with your title and [REMOVE]-tagged exemplar content."

Use `AskUserQuestion` with options:
- **Yes** — proceed to set up the paper
- **No** — skip; user can run `/setup-paper` later

If **Yes**:
1. Derive a default paper title from the project name (replace underscores with spaces, title case)
2. `cd` into `projects/<name>/` so that `/setup-paper` detects it as the active project
3. Invoke `/setup-paper` with the derived title — it will auto-target `latex/`
4. The user can provide `--authors` and `--topic` at this point if they want

If **No**, print:

```
Next steps:
  1. Run /setup-paper "Your Title" to scaffold the LaTeX paper when ready
  2. Add literature PDFs to literature/
  3. Start an investigation: create scripts/tests/{test_name}/ with an output/ subfolder
  4. Fetch data using WRDS agents — it saves to data/ and you reference it from here
  5. Add methodology notes to guidance/
```
