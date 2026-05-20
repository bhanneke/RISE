<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/translate-to-quarto.md -->

# `/translate-to-quarto`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/translate-to-quarto/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/translate-to-quarto/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/translate-to-quarto/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Beamer → Quarto Translation Workflow

Full translation of a Beamer LaTeX lecture to Quarto RevealJS HTML slides.

**CRITICAL: The Beamer .tex file is the SINGLE SOURCE OF TRUTH.**

---

### Phase 0: Pre-Flight Checks

#### 0A. Environment Parity Audit
Scan Beamer for all custom environments. Verify CSS equivalents exist in your theme SCSS. If any are missing, create them FIRST.

#### 0B. TikZ Freshness Verification
Run `/extract-tikz` to verify SVGs match current Beamer source.

#### 0C. RDS Data Inventory
List all RDS files needed for interactive charts.

#### 0D. Citation Key Mapping
Extract all citations from Beamer, map to bibliography keys.

### Phase 1: Pre-Translation Preparation
- Read complete Beamer source, count frames
- Inventory figures (TikZ → SVG, R plots → plotly, other → SVG)

### Phase 2: Create QMD File with YAML Header
- Standard RevealJS YAML with theme, logo, footer, bibliography
- Setup chunk for R data loading if needed

### Phase 3: Slide-by-Slide Translation
- Delegate to `beamer-translator` agent
- 1:1 frame-to-slide mapping
- Verbatim math, environment parity, no font reduction

### Phase 4: TikZ Diagram Integration
Reference extracted SVGs with 0-based indexing.

### Phase 5: R Figure Integration (Plotly-First)
Interactive plotly from RDS data, static SVG for TikZ/complex figures.

### Phase 6: First Render & Content Fidelity Check
Render, count slides, go through EVERY slide checking for issues.

### Phase 6.5: Pedagogical Review
Run pedagogy-reviewer before visual polish.

### Phase 7: Visual Polish
Semantic colors, transition slides, framing sentences.

### Phase 8: Proofreading
Run `/proofread` on the QMD file.

### Phase 9: Final Verification & Deployment
Render, open in browser, verify all elements.

### Phase 10: Beamer Source Sync
Apply any corrections back to Beamer source.

### Phase 11: Documentation
Update CLAUDE.md, session log, create PR.
