<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/dashboard.md -->

# `dashboard`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

---
name: dashboard
description: Generate or refresh the unified project dashboard HTML. Scans data files, scripts, quality reports, plans, git history, and literature to build a single-page project overview. Invoke with /dashboard to create from scratch or update an existing dashboard.
argument-hint: "[refresh | create | add-changelog TITLE]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash
---

# Dashboard

Generate or refresh `project_dashboard.html` — a single scrollable HTML page with everything about the project.

**Input:** `$ARGUMENTS` — optional subcommand.

---

## Subcommands

### `/dashboard` or `/dashboard refresh` — Rebuild from current state

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

### `/dashboard create` — Generate from scratch

Full generation including research design sections. Use after `/discover` and `/strategize` have produced outputs. Prompts user for:
- Research question (one sentence)
- Causal chain (nodes)
- Contributions (2-4 bullets)
- Risk matrix entries

Then generates all 10 sections with the operational ones populated from disk scan.

### `/dashboard add-changelog TITLE` — Append a changelog entry

Append a new entry to the changelog section with today's date. Prompts for:
- Tag type (data/design/code/paper/infra/review)
- Bullet points describing what happened

---

## Section Structure (10 sections, this order)

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

## Data Section Order

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

## Data Status Labels

Only two statuses. No ambiguity.

| Label | Pill class | Meaning |
|-------|-----------|---------|
| `downloaded` | `pill-pass` | File is on disk in `data/raw/` |
| `manual download` | `pill-warn` | Requires registration or browser interaction — flag for collaborators |

---

## Design System

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

## Rules

1. **One file** — always `project_dashboard.html`, never split
2. **Refresh is safe** — operational sections (data, code, quality, history) are rebuilt from disk. Research sections (overview, identification, literature) are preserved unless `create` mode.
3. **Changelog is append-only** — never delete or rewrite existing entries
4. **Run after milestones** — data downloads, completed analyses, paper submissions. Or anytime with `/dashboard refresh`.
5. **Collaborator-friendly** — use clear language, link to download instructions for `manual download` items


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/dashboard/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>hugosantanna/clo-author</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../clo-author.md">Clo-Author skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>none declared</dd>
<dt><b>Last update</b></dt><dd>2026-05-11</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/hugosantanna/clo-author">⭐ hugosantanna/clo-author</a><br><img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/hugosantanna/clo-author" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/clo-author/dashboard/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/clo-author.yml">edit on GitHub</a>.</p>
</div>

</div>
