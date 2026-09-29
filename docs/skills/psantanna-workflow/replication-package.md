<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/replication-package.md -->

# `/replication-package`

Assembles a submission-ready replication package to the AEA Data and Code Availability Standard: README, dataset manifest, computational requirements, table and figure map.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code> · <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/replication-package/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/replication-package/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/replication-package/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Replication Package

Produce the deposit an economist hands a journal at acceptance: a directory tree (`data/`, `code/`, `output/`, `README`) plus a DCAS compliance checklist, built to the [AEA Data and Code Availability Standard](https://datacodestandard.org/), openICPSR deposit expectations, and the [Social Science Reproduction Platform](https://www.socialsciencereproduction.org/) reproduction protocol. This skill **moves the repo from auditing reproducibility to producing the deposit** — `/audit-reproducibility` proves the numbers; this skill packages everything a third party needs to regenerate them from scratch.

**Core principle:** the package is reproducible by a stranger with the data and the README — no tacit knowledge, no "ask the author" steps. Every table and figure maps to the exact script and line that produces it.

### When to use

- **At acceptance.** The journal's data editor (AEA, REStud, JPE, EJ, ...) requests a DCAS-compliant deposit before the paper is typeset.
- **Before an openICPSR / Zenodo / Dataverse upload.** Build the tree and README once, locally, before the web upload.
- **Pre-submission dry run.** Catch the "I never wrote down where Table 3 comes from" gap while it is cheap to fix.
- **Confidential-data papers.** Produce the access-restricted-data note and a runnable-on-restricted-data package even when the data itself cannot be deposited.

### Inputs

- `$0` — path to the manuscript (`.tex`, `.qmd`, `.md`, `.pdf`). Required (the source of the Table/Figure inventory).
- `$1` — outputs directory. Defaults to `output/`, where every language's pipeline writes. Recognised alternative: `_targets/objects/`. If `output/` does not exist but a pre-v2.6 `scripts/<lang>/_outputs/` does, use that and say so.

### Workflow

#### Phase 0: Pre-flight — detect language(s) and outputs

1. Detect the analysis language(s) by scanning for `scripts/R/*.R` (+ `renv.lock` / `DESCRIPTION`), `scripts/stata/*.do`, `scripts/python/*.py` (+ `requirements.txt` / `environment.yml` / `pyproject.toml`). A project may be **polyglot** — record all detected languages.
2. Locate the outputs directory (`$1`) and the one-command entry point (`00_run_all.R`, `99_run_all.do`, `run.py`, `Makefile`). If none exists, flag it — DCAS requires a single master script.
3. If `quality_reports/passports/<paper-slug>.yaml` exists, load it; its `claims:` entries are the authoritative Table/Figure → `source_file:source_line` map for Phase 1.

#### Phase 1: Generate the standard replication README

Write `replication_package/README.md` (the AEA template, fields below). Leave a `[FILL]` marker on any field you cannot infer — never fabricate a data source or license.

- **Overview / paper citation** — title, authors, abstract one-liner.
- **Data Availability Statement** — for each dataset: public / restricted / proprietary, and whether it is redistributed in the package. This is the single most-rejected DCAS field; be explicit.
- **Dataset manifest** — a table, one row per file: `filename | description | source (URL/citation) | access (public / DUA / purchase) | license | provided in package? (Y/N)`.
- **Computational requirements** — OS, software + versions (R / Stata / Python), key packages, approximate runtime, RAM, any HPC/cluster need.
- **Step-by-step run instructions** — the single master-script invocation, then the expected outputs.
- **Table/Figure → script:line map** — one row per exhibit: `Exhibit | Program | Line | Output file`. Read from the passport if present; otherwise grep the manuscript for `\input{}` / `\includegraphics{}` and trace each to the producing script. This map is what a reproducer follows; it is the heart of the package.

#### Phase 2: Capture the computational environment

Generate the dependency lockfile(s) and an environment snapshot for each detected language. Prefer `/capture-environment` if available; otherwise produce them directly:

- **R** — `renv::snapshot()` → `renv.lock`; `sessionInfo()` → `output/sessionInfo.txt`.
- **Python** — `pip freeze` → `requirements.txt` (or export the conda `environment.yml`); record `python --version`.
- **Stata** — `creturn list` / `about` / the `which` list → `output/sessionInfo_stata.txt`, the environment record the Stata convention requires; confirm every `.do` pins `version NN` (per `stata-code-conventions.md`).
- **Container (recommended by DCAS for non-trivial setups)** — scaffold a `Dockerfile` pinning the base image + language version.

#### Phase 3: Confirm claims reproduce before packaging

Run `/audit-reproducibility` `$0 $1` (passport-aware if the YAML exists).

- **Any FAIL** (out of tolerance, no named alternative) → **block**: do not assemble a package around numbers that do not reproduce. Surface the failing claims and stop.
- **EXPLAINED** (out of tolerance with a recorded named alternative) → allowed; carry the note into the README's known-discrepancies section.
- **All PASS / PASS + EXPLAINED** → proceed to Phase 4.

#### Phase 4: Assemble the tree + DCAS checklist

Create the deposit skeleton (copy/symlink real files where they exist; leave `[FILL]` placeholders otherwise):

```
replication_package/
├── README.md                # Phase 1
├── data/
│   ├── raw/                 # as-obtained (or a pointer + DUA note if restricted)
│   └── analysis/            # constructed analysis files
├── code/                    # numbered scripts + master script (00_run_all.* / 99_run_all.do)
└── output/                  # tables/, figures/, logs/, sessionInfo.txt (R) / sessionInfo_stata.txt (Stata), renv.lock / requirements.txt
```

Then emit the **DCAS compliance checklist** (`replication_package/DCAS_checklist.md`): Data Availability Statement present · every dataset has source + access + license · master script present and one-command · computational requirements stated · every Table/Figure mapped to program:line · no absolute/machine-specific paths in code · seeds set for any stochastic step · license file (a code license such as BSD/MIT + a data-usage statement). Mark each PASS / FAIL / `[FILL]`.

#### Phase 5: Confidential-data handling

Per `.claude/rules/confidential-data.md`, scan the manifest for restricted, proprietary, or PII-bearing inputs (administrative records, IRS/Census RDC, proprietary panels, linked health data).

- **Never copy restricted data into `replication_package/data/`.** Replace it with a pointer: the provider, the application/DUA process, the access cost, and the expected wait time.
- Generate `replication_package/data/access-restricted-data.md` — the access-restricted-data note a reproducer follows to obtain the same inputs.
- Confirm the **code still ships** (DCAS requires runnable-on-restricted-data code even when the data cannot be deposited), and that any committed extracts pass disclosure-avoidance (cell suppression / rounding) before they enter `output/`.

### Output / Report format

Write `quality_reports/replication_package_[paper-slug].md`:

```markdown
## Replication Package: [Paper Title]
**Date:** [YYYY-MM-DD]  **Languages:** [R / Stata / Python]  **Deposit target:** [openICPSR / Zenodo / Dataverse]

### DCAS checklist
| Item | Status |
|---|---|
| Data Availability Statement | PASS / FAIL / [FILL] |
| Dataset manifest (source · access · license) | ... |
| One-command master script | ... |
| Computational requirements | ... |
| Table/Figure → program:line map | ... |
| No machine-specific paths · seeds set | ... |
| Reproducibility audit (Phase 3) | PASS / EXPLAINED-only / FAIL (blocker) |
| Confidential-data note (if applicable) | ... |

### Skeleton built at
replication_package/  (tree + README + checklist)

### Open [FILL] items
[one line per unresolved field]
```

### Exit behavior

- **All checklist items PASS (or PASS + `[FILL]`) and audit PASS/EXPLAINED-only:** exit 0; print the tree location and any `[FILL]` items for the author to complete.
- **Any audit FAIL (Phase 3):** exit 1; package assembly halts. Numbers that do not reproduce do not get deposited.
- **Restricted data detected but no access note generated:** exit 1 with the confidential-data blocker — packaging cannot proceed until Phase 5 runs.

### Cross-references

- `.claude/rules/replication-protocol.md` — tolerance contract + passport schema (the upstream verification this skill packages).
- `.claude/skills/audit-reproducibility/SKILL.md` — the Phase 3 gate; proves claims reproduce.
- `.claude/rules/confidential-data.md` — restricted-data deposit rules driving Phase 5.
- `templates/passport-template.yaml` — source of the Table/Figure → program:line map when present.
- `.claude/skills/data-analysis/SKILL.md` · `.claude/skills/stata-replication/SKILL.md` — the R / Stata pipelines whose outputs this skill packages.
- `.claude/skills/simulation-study/SKILL.md` — seeded Monte Carlo outputs are packaged the same way (seeds + per-rep raw results belong in `output/`).
- `.claude/skills/preregister/SKILL.md` — for RCTs, the PAP belongs in the deposit alongside the analysis.

### What this skill does NOT do

- **Verify the numbers.** That is `/audit-reproducibility` (called in Phase 3). This skill packages a *verified* result; it blocks rather than re-derives on FAIL.
- **Upload to the repository.** It builds the local tree and README; the author performs the openICPSR / Zenodo / Dataverse upload and gets the DOI. Web deposit is deliberately out of scope.
- **Judge the research.** Whether the identification strategy (DiD / event-study, IV, RCT, panel FE) is sound is a `/review-paper` question. A reproducible package can still house a flawed design.
- **De-identify your data.** It flags restricted inputs and refuses to deposit them; it does not run disclosure-avoidance algorithms on raw microdata — that is the author's (and the RDC's) responsibility.
