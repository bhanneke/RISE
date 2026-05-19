<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/scientific-visualization.md -->

# `scientific-visualization`



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
name: scientific-visualization
description: Publication-ready scientific figure design with matplotlib and seaborn. Use when creating journal submission figures with proper formatting, accessibility, and statistical annotations.
metadata:
  category: writing
  trigger-keywords: "figure,plot,chart,visualization,matplotlib,seaborn,colorblind,publication"
  applicable-stages: "14,17,22"
  priority: "3"
  version: "1.0"
  author: researchclaw
  references: "adapted from K-Dense-AI/claude-scientific-skills"
---

## Scientific Visualization Best Practice

### Figure Design Principles
1. Every figure must have a clear, self-contained message
2. Minimize chartjunk: remove gridlines, background shading, and 3D effects
3. Use direct labeling instead of legends when possible
4. Remove top and right spines for cleaner appearance
5. Ensure all text is readable at final print size (minimum 6pt font)

### Journal Figure Sizing
1. **Single column**: 3.3-3.5 inches (85-89 mm) wide
2. **1.5 column**: 4.5-5.5 inches (114-140 mm) wide
3. **Double column / full width**: 6.5-7.1 inches (165-180 mm) wide
4. Resolution: 300 DPI minimum for raster; prefer vector formats (PDF, EPS, SVG)
5. Check target journal author guidelines for exact specifications

### Colorblind-Safe Design
1. Use colorblind-friendly palettes: seaborn "colorblind", Okabe-Ito, viridis, cividis
2. NEVER rely on color alone — combine with shape, pattern, or line style
3. Avoid red-green combinations; prefer blue-orange or blue-yellow contrasts
4. Test figures with a colorblind simulator before submission
5. Ensure figures work in grayscale for print journals

### Multi-Panel Layouts
1. Label panels with uppercase letters: (A), (B), (C) in bold, top-left corner
2. Use consistent axis scales across panels when comparing related data
3. Share axes where appropriate to reduce redundancy
4. Maintain consistent font sizes and line widths across all panels
5. Use `plt.subplots()` with `constrained_layout=True` for automatic spacing

### Statistical Annotations on Figures
1. Show individual data points alongside summary statistics (box + strip plots)
2. Always include error bars; specify type in caption (SEM, SD, 95% CI)
3. Use significance brackets with stars: * p<.05, ** p<.01, *** p<.001
4. Annotate effect sizes or key statistics directly on the figure when helpful
5. Never use bar charts for small-n data — use dot plots or box plots instead

### Export and Quality Checklist
1. Save in vector format (PDF/SVG) for line art; TIFF/PNG for photographs
2. Embed fonts or convert text to outlines for cross-platform consistency
3. Verify axis labels include units in parentheses: "Time (s)", "Force (N)"
4. Ensure figure caption fully explains all symbols, abbreviations, and panels
5. Check that color-coded elements match between figure and caption


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/scientific-visualization/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>aiming-lab/AutoResearchClaw</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../autoresearchclaw.md">AutoResearchClaw skills</a></dd>
<dt><b>Category</b></dt><dd><code>figures</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04-23</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw">⭐ aiming-lab/AutoResearchClaw</a><br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/autoresearchclaw/scientific-visualization/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/autoresearchclaw.yml">edit on GitHub</a>.</p>
</div>

</div>
