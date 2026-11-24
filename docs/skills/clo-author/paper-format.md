<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/paper-format.md -->

# `paper-format`

Applies and enforces the mandatory paper house style: float placement, Table 1 of pre-treatment characteristics, table and subfigure wrappers, section order and captions.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../clo-author/">Clo-Author skills</a></div><div><b>Category:</b> <code>submission</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT (LICENSE file, "Copyright (c) 2026 Hugo Sant'Anna"; portions derived from claude-code-my-workflow, also MIT)</code></div><div><b>Updated:</b> 2026-10-15</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/paper-format/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/clo-author/paper-format/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hugosantanna/clo-author" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Paper Format (House Style)

Applies and enforces the **mandatory** organization rule in `.claude/rules/paper-organization.md`
(blocking invariants **INV-23, INV-24, INV-25**). This is non-negotiable house style — every agent and
Claude must follow it. When in doubt, open the reference exemplars named in the rule.

**Input:** `$ARGUMENTS` — a mode and optional target. Default mode: `audit`.

### Modes

#### `audit [main.tex]` (default)
Check a paper against the house style and report violations with invariant numbers:
1. **INV-23 — floats at end.** Grep `sections/*.tex` for `\begin{table}` / `\begin{figure}` → any hit is a violation (floats must be in `main.tex`'s end blocks, not in section files). Confirm `main.tex` has TABLES and FIGURES blocks after `\printbibliography`.
2. **INV-24 — Table 1.** Confirm the first table is pre-treatment characteristics: two group columns, thematic panels, unit counts at the bottom, and **no difference / SD / p-value column**.
3. **INV-25 — wrappers.** Every table uses `threeparttable` + `tablenotes` (or `\inputtblr` + `parbox`) with exhaustive notes; every figure uses `subcaption` with the overall `\caption{}` on top.
4. Booktabs only (no `\hline`/vertical rules), bare exhibits from scripts (INV-13), no in-figure titles (INV-12).
Report a pass/fail list; do not edit unless asked.

#### `scaffold [main.tex]`
Insert the empty TABLES and FIGURES blocks at the end of `main.tex` (after the bibliography) using the
canonical comment banners, and move any inline floats from section files into those blocks.

#### `table1`
Build the pre-treatment characteristics table (Table 1) from the project's panel: two group columns
(treated vs. control), thematic panels, counts at the bottom, no difference column. Export a bare
`tabular` to `tables/.../` and wrap it in `main.tex` with the canonical `threeparttable` block.

#### `show`
Print the house-style templates (table wrapper, figure wrapper, Table 1 model) from the rule for quick
copy-paste.

### Authority

The full specification lives in `.claude/rules/paper-organization.md`. This skill operationalizes it; the
rule is the source of truth. Where this house style and `working-paper-format.md` disagree on float
placement, the house style wins.
