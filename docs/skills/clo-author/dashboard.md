<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/dashboard.md -->

# `dashboard`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../clo-author/">Clo-Author skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>none declared</code></div><div><b>Updated:</b> 2026-05-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/dashboard/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/clo-author/dashboard/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hugosantanna/clo-author" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Dashboard

Generate or refresh `project_dashboard.html` — a single scrollable HTML page with everything about the project.

**Input:** `$ARGUMENTS` — optional subcommand.

---

### Subcommands

#### `/dashboard` or `/dashboard refresh` — Rebuild from current state

Scan the project and regenerate all sections of `project_dashboard.html`:

1. **Scan data:** `find data/ -type f` — count files, sizes, categories. Classify each as `downloaded` or `manual download`.
2. **Scan scripts:** `find scripts/ -type f -name "*.R" -o -name "*.py" -o -name "*.jl"` — list with status.
3. **Scan quality reports:** `find quality_reports/ -type f` — timeline entries.
4. **Scan plans:** `find quality_reports/plans/ -type f` — active plans with status from frontmatter.
5. **Read CLAUDE.md:** Extract project name, target journal, paper status.
6. **Read git log:** Recent commits for history section.
7. **Preserve changelog:** Never overwrite existing changelog entries — only append.
8. **Preserve research content:** Overview (question, causal chain, contributions, risks), identification strategy, literature — these are authored content. Refresh operational sections only unless `create` mode.

Output: Write/update `project_dashboard.html` in project root.

#### `/dashboard create` — Generate from scratch

Full generation including research design sections. Use after `/discover` and `/strategize` have produced outputs. Prompts user for:
- Research question (one sentence)
- Causal chain (nodes)
- Contributions (2-4 bullets)
- Risk matrix entries

Then generates all 10 sections with the operational ones populated from disk scan.

#### `/dashboard add-changelog TITLE` — Append a changelog entry

Append a new entry to the changelog section with today's date. Prompts for:
- Tag type (data/design/code/paper/infra/review)
- Bullet points describing what happened

---

### Section Structure (10 sections, this order)

| # | Section | Nav ID | Content |
|---|---------|--------|---------|
| 1 | Overview | `#overview` | Question, causal chain, contributions, risk matrix |
| 2 | Data | `#data` | Role inventory + file-level tables with sizes |
| 3 | Identification | `#identification` | IV/design, specifications, threats, fallback |
| 4 | Literature | `#literature` | Positioning, proximity, gaps |
| 5 | Code | `#code` | Scripts list with run status |
| 6 | Quality | `#quality` | Component scores and gate status |
| 7 | History | `#history` | Timeline of quality reports |
| 8 | Plans | `#plans` | Active plans (DRAFT/APPROVED/COMPLETED) |
| 9 | Paper | `#paper` | Figures/tables plan, word allocation |
| 10 | Changelog | `#changelog` | Reverse-chronological milestone log |

---

### Data Section Order

File-level detail sections **must follow the same order as the master inventory table**. The master inventory defines the canonical order by role:

1. **TREATMENT** — the shock/exposure variable
2. **IV components** — instruments (soil, wind, etc.)
3. **OUTCOME 1** — primary outcome
4. **OUTCOME 2** — secondary outcome
5. **MECHANISM** — intermediate channel variables
6. **CROSSWALK** — boundary harmonization files
7. **APPENDIX** — supplementary/heterogeneity data

When generating or refreshing the data section, always emit file-level subsections in this order. The sub-nav links must match.

---

### Data Status Labels

Only two statuses. No ambiguity.

| Label | Pill class | Meaning |
|-------|-----------|---------|
| `downloaded` | `pill-pass` | File is on disk in `data/raw/` |
| `manual download` | `pill-warn` | Requires registration or browser interaction — flag for collaborators |

---

### Design System

Use the clo-author HTML design system:
- CSS variables for colors (supports dark mode via `prefers-color-scheme` + manual toggle)
- Sticky main nav at top with smooth scroll
- Section sub-navs where data has many subsections
- Pills for status badges
- Cards for key items (bordered-left with accent color)
- `report-table` for structured data
- Monospace for file paths and dates
- Serif for section titles
- Footer: "Generated YYYY-MM-DD by clo-author"

---

### Rules

1. **One file** — always `project_dashboard.html`, never split
2. **Refresh is safe** — operational sections (data, code, quality, history) are rebuilt from disk. Research sections (overview, identification, literature) are preserved unless `create` mode.
3. **Changelog is append-only** — never delete or rewrite existing entries
4. **Run after milestones** — data downloads, completed analyses, paper submissions. Or anytime with `/dashboard refresh`.
5. **Collaborator-friendly** — use clear language, link to download instructions for `manual download` items
