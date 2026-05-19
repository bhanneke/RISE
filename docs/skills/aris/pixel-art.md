<!-- DO NOT EDIT — auto-copied from skills/aris/details/pixel-art.md -->

# `pixel-art`



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
name: pixel-art
description: Generate pixel art SVG illustrations for READMEs, docs, or slides. Use when user says "画像素图", "pixel art", "make an SVG illustration", "README hero image", or wants a cute visual.
argument-hint: [description of what to draw]
allowed-tools: Write, Edit, Read, Bash(open *)
---

# Pixel Art SVG Generator

Create a pixel art SVG illustration: $ARGUMENTS

## Design Principles

### Pixel Grid
- Each "pixel" is a `<rect>` with width/height of 7px
- Grid spacing: 7px (no gaps between pixels)
- Characters are typically 8-10 pixels wide, 8-12 pixels tall
- Use `<g transform="translate(x,y)">` to position and reuse character groups

### Color Palette
Keep it simple — 3-5 colors per character:
- **Skin**: `#FFDAB9` (light), `#E8967A` / `#D4956A` (blush/shadow)
- **Eyes**: `#333`
- **Hair**: `#8B5E3C` (brown), `#2C2C2C` (black), `#FFD700` (blonde), `#C0392B` (red)
- **Clothes**: use project's brand color (e.g. `#4A9EDA` for blue, `#74AA63` for green)
- **Shoes/pants**: `#444`
- **Accessories**: `#555` (glasses frames), `#FFD700` (crown)

### Character Template (7px grid)
```
Row 0 (hair top):     4 pixels centered
Row 1 (hair):         6 pixels wide
Row 2 (face top):     6 pixels — all skin
Row 3 (eyes):         6 pixels — skin, eye, skin, skin, eye, skin
Row 4 (mouth):        6 pixels — skin, skin, mouth, mouth, skin, skin
Row 5 (body top):     8 pixels — hand, 6 shirt, hand
Row 6 (body):         6 pixels — all shirt
Row 7 (legs):         2+2 pixels — with gap in middle
```

### Scene Composition

#### Chat Dialogue Layout (like our hero image)
- Two characters on left/right sides, vertically centered
- Chat bubbles between them, alternating left/right
- Bubble tails point toward the speaking character
- Arrows between bubbles show direction of communication
- Use `orient="auto"` markers for arrow heads
- Bottom: tagline or decoration

#### Single Character with Label
- Character centered
- Label text below
- Optional: speech bubble above

#### Group Scene
- Characters spaced evenly
- Optional: ground line, background elements
- Keep viewBox tight — no wasted space

### SVG Structure
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 W H" font-family="monospace">
  <defs>
    <!-- Arrow markers if needed -->
  </defs>

  <rect width="W" height="H" fill="#fafbfc" rx="12"/>  <!-- Background -->

  <!-- Characters via <g transform="translate(...)"> -->
  <!-- Dialogue bubbles: <rect> + <polygon> tail + <text> -->
  <!-- Arrows: <line> with marker-end -->
  <!-- Labels: <text> with text-anchor="middle" -->
</svg>
```

### Chat Bubble Recipe
```xml
<!-- Blue bubble (left character speaks) -->
<rect x="110" y="29" width="280" height="26" fill="#e8f4fd" stroke="#4a9eda" stroke-width="1.5" rx="8"/>
<!-- Tail pointing left toward character -->
<polygon points="108,41 99,47 108,46" fill="#e8f4fd" stroke="#4a9eda" stroke-width="1.5"/>
<rect x="107" y="40" width="3" height="7" fill="#e8f4fd"/>  <!-- covers stroke at junction -->
<text x="123" y="46" font-size="13px">📄 Message here</text>

<!-- Orange bubble (right character responds) -->
<rect x="490" y="71" width="280" height="26" fill="#fdf2e8" stroke="#da8a4a" stroke-width="1.5" rx="8"/>
<!-- Tail pointing right toward character -->
<polygon points="772,83 781,89 772,88" fill="#fdf2e8" stroke="#da8a4a" stroke-width="1.5"/>
<rect x="770" y="82" width="3" height="7" fill="#fdf2e8"/>
<text x="503" y="88" font-size="13px">🤔 Response here</text>
```

### Arrow Recipe
```xml
<defs>
  <marker id="ar" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#4a9eda"/>
  </marker>
</defs>
<!-- Right arrow (→): x1 < x2 -->
<line x1="392" y1="42" x2="465" y2="42" stroke="#4a9eda" stroke-width="2" marker-end="url(#ar)"/>
<!-- Left arrow (←): x1 > x2 -->
<line x1="488" y1="84" x2="420" y2="84" stroke="#da8a4a" stroke-width="2" marker-end="url(#ar-o)"/>
```

## Workflow

### Step 1: Understand the Request
- What characters/objects to draw?
- What's the scene? (dialogue, portrait, group, diagram)
- What colors/brand to match?
- What size? (compact for badge, wide for README hero)

### Step 2: Generate SVG
- Write to a temp file or project directory
- Open with `open <file.svg>` for preview
- Keep viewBox tight — measure actual content bounds

### Step 3: Iterate with User
- User provides feedback on screenshot
- Common fixes: overlap, arrow direction, spacing, sizing
- Use `Edit` for small tweaks, `Write` for major redesigns
- Typical: 2-4 iterations to get it right

### Step 4: Finalize
- Ensure no personal info in the SVG
- Clean up: remove unused defs, tighten viewBox
- Suggest adding to README: `![Alt text](filename.svg)`

## Common Pitfalls
- **Arrow direction**: `orient="auto"` follows line direction. Line going right→left = arrowhead points left
- **Bubble overlap**: keep 38-44px vertical spacing between rows
- **Text overflow**: monospace 13px ≈ 7.8px/char, emoji ≈ 14px. Measure before setting bubble width
- **Character overlap with bubbles**: keep character x-zone and bubble x-zone separated by ≥10px
- **viewBox too large**: match viewBox to actual content, add ~10px padding
- **Tail stroke artifact**: always add a small `<rect>` at the bubble-tail junction to cover the stroke line


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/pixel-art/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/pixel-art/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
