<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/deploy.md -->

# `/deploy`



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
name: deploy
description: Render Quarto `.qmd` slides to HTML and sync to `docs/` for GitHub Pages. Use when user says "deploy", "publish the slides", "ship to pages", "push the lecture live", "render and publish", or after Quarto edits that need to go public. NOT for local Quarto render only — use `quarto render` directly for that.
argument-hint: "[LectureN or 'all']"
allowed-tools: ["Read", "Bash"]
---

# Deploy Slides to GitHub Pages

Render Quarto slides and sync all files to `docs/` for GitHub Pages deployment.

## Steps

1. **Run the sync script:**
   - If `$ARGUMENTS` is provided (e.g., "Lecture4"): `./scripts/sync_to_docs.sh $ARGUMENTS`
   - If no argument: `./scripts/sync_to_docs.sh` (syncs all lectures)

2. **Verify deployment:**
   - Check that HTML files exist in `docs/slides/`
   - Check that `_files/` directories were copied (RevealJS assets)
   - Check that `docs/Figures/` was synced from `Figures/`

3. **Verify interactive charts** (if applicable):
   - Grep rendered HTML for interactive widget count
   - Confirm count matches expected

4. **Verify TikZ SVGs** (if applicable):
   - Check that all referenced SVG files exist in `docs/Figures/LectureN/`

5. **Open in browser** for visual verification:
   - `open docs/slides/LectureX_Name.html`          # macOS
   - `# xdg-open docs/slides/LectureX_Name.html`    # Linux
   - Confirm slides render, images display, navigation works

6. **Report results** to the user

## What the sync script does:
- Renders all `.qmd` files in `Quarto/` (skips `*_backup*` files)
- Copies HTML and `_files/` directories to `docs/slides/`
- Copies Beamer PDFs from `Slides/` to `docs/slides/`
- Syncs `Figures/` to `docs/Figures/` using rsync


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/deploy/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>submission</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>dissemination</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/deploy/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/deploy/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
