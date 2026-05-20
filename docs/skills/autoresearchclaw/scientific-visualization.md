<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/scientific-visualization.md -->

# `scientific-visualization`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../autoresearchclaw/">AutoResearchClaw skills</a></div><div><b>Category:</b> <code>figures</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/scientific-visualization/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/autoresearchclaw/scientific-visualization/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/aiming-lab/AutoResearchClaw" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

### Scientific Visualization Best Practice

#### Figure Design Principles
1. Every figure must have a clear, self-contained message
2. Minimize chartjunk: remove gridlines, background shading, and 3D effects
3. Use direct labeling instead of legends when possible
4. Remove top and right spines for cleaner appearance
5. Ensure all text is readable at final print size (minimum 6pt font)

#### Journal Figure Sizing
1. **Single column**: 3.3-3.5 inches (85-89 mm) wide
2. **1.5 column**: 4.5-5.5 inches (114-140 mm) wide
3. **Double column / full width**: 6.5-7.1 inches (165-180 mm) wide
4. Resolution: 300 DPI minimum for raster; prefer vector formats (PDF, EPS, SVG)
5. Check target journal author guidelines for exact specifications

#### Colorblind-Safe Design
1. Use colorblind-friendly palettes: seaborn "colorblind", Okabe-Ito, viridis, cividis
2. NEVER rely on color alone — combine with shape, pattern, or line style
3. Avoid red-green combinations; prefer blue-orange or blue-yellow contrasts
4. Test figures with a colorblind simulator before submission
5. Ensure figures work in grayscale for print journals

#### Multi-Panel Layouts
1. Label panels with uppercase letters: (A), (B), (C) in bold, top-left corner
2. Use consistent axis scales across panels when comparing related data
3. Share axes where appropriate to reduce redundancy
4. Maintain consistent font sizes and line widths across all panels
5. Use `plt.subplots()` with `constrained_layout=True` for automatic spacing

#### Statistical Annotations on Figures
1. Show individual data points alongside summary statistics (box + strip plots)
2. Always include error bars; specify type in caption (SEM, SD, 95% CI)
3. Use significance brackets with stars: * p<.05, ** p<.01, *** p<.001
4. Annotate effect sizes or key statistics directly on the figure when helpful
5. Never use bar charts for small-n data — use dot plots or box plots instead

#### Export and Quality Checklist
1. Save in vector format (PDF/SVG) for line art; TIFF/PNG for photographs
2. Embed fonts or convert text to outlines for cross-platform consistency
3. Verify axis labels include units in parentheses: "Time (s)", "Force (N)"
4. Ensure figure caption fully explains all symbols, abbreviations, and panels
5. Check that color-coded elements match between figure and caption
