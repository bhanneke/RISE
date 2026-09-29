<!-- DO NOT EDIT — auto-copied from skills/thinkingwithagents-skills/details/academic-beamer-deck.md -->

# `/academic-beamer-deck`

Builds or redesigns academic Beamer decks from .tex sources, figures and talk context, with a narrative structure, a design system, strict layout and TikZ rules, and a compile check, and returns a compile-ready deck with an organised figures folder.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../thinkingwithagents-skills/">Thinking with Agents econ skills (Emily Beam and Erkmen Aslim)</a></div><div><b>Category:</b> <code>slides</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>CC-BY-4.0 (repo LICENSE, "Creative Commons Attribution 4.0 International, Copyright (c) 2026 Emily Beam")</code></div><div><b>Updated:</b> 2026-04-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/thinkingwithagents/skills/contents/academic-beamer-deck/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/thinkingwithagents-skills/academic-beamer-deck/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/thinkingwithagents/skills/blob/main/academic-beamer-deck/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/thinkingwithagents/skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

### Workflow

1. Audit and internalize all provided materials.
2. Create a slide plan before editing (structure, pacing, consolidation).
3. Rebuild the narrative for live presentation.
4. Apply visual system (theme, colors, hierarchy).
5. Optimize content density and clarity.
6. Implement layout using container-based alignment (not spacing hacks).
7. Verify compile + visual polish across all slide types.

---

### Narrative Structure

Default structure:

1. Title
2. Hook (engaging opening)
3. Research Question
4. Roadmap
5. Background
6. Data
7. Identification
8. Results
9. Mechanisms
10. Synthesis (diagram / summary)
11. Policy Implications
12. Takeaways
13. Appendix

Adapt as needed, but prioritize flow for a live audience.

---

### Design System

#### Theme

- Use a custom minimal Beamer theme
- Avoid default themes (e.g., CambridgeUS)
- Use:
  - aspectratio=169
  - no navigation symbols
  - custom frame titles and footline

---

### Default Color Scheme

Use this unless user specifies otherwise:

- Primary: SlateTeal (#1B4D5C)
  -> titles, headers

- Accent: WarmAmber (#D4A84B)
  -> highlights, key numbers

- Body Text: DeepCharcoal (#2C3E50)

- Secondary Accent: SoftCoral (#C0534D)
  -> negative results / significance

- Muted: CoolGray (#8899A6)
  -> notes, annotations

- Light Fill: PaleSage (#EDF2F0)
  -> tcolorbox fills, block bodies

- Background:
  - default: white (#FFFFFF)
  - optional: WarmWhite (#FAFAF8) (only if ALL figures have non-white backgrounds)

#### Color Rules

- Use accent sparingly
- Max 2-3 dominant colors per slide
- Ensure high contrast
- Maintain consistency across slides

---

### Typography & Structure

- Clear hierarchy:
  - titles emphasized
  - body minimal
  - highlights selective

- Prefer:
  - boxes for key ideas
  - structured layouts (columns, grids)

- Avoid:
  - dense paragraphs
  - clutter

---

### Content Rules

- One main idea per slide
- Prefer visuals over text
- Merge redundant slides
- Move secondary content to appendix
- Use overlays (\pause) sparingly

---

### Diagram Rules (TikZ / Visuals)

Optimize in this order:

1. Clarity
2. Balance
3. Fit
4. Compactness

Rules:
- Center composition on the slide
- When a horizontal chain overflows, wrap the final node(s) to a centered row below
  - Do NOT shrink text or node widths to force a single-row fit
  - Use coordinate midpoints to center the wrapped row:
    `\coordinate (mid) at ($(first.south)!0.5!(last.south)$);`
    requires `\usetikzlibrary{calc}`
- Avoid unnecessary arrows (especially to visually separated outcome nodes)
- Group annotation labels directly below their parent nodes
- Use muted colors (CoolGray) for annotation text
- Use a distinct style for outcome/result nodes (e.g., accent fill + accent border)
- Define reusable node styles (box, resultbox, evidence) instead of inline styling
- Always use `positioning` library (`right=of`, `below=of`) instead of manual coordinates

---

### Layout Rules (CRITICAL)

#### Core Principle

Never place elements flush against slide edges.
Define a consistent safe zone and enforce it structurally.

---

#### Safe Zone

Define a single inset value (e.g., 1.5cm) and apply it consistently to:
- page numbers (via footline rightskip)
- buttons (via trailing \hspace)
- any right-aligned content

This value should be defined once and reused. If the value changes, it must change everywhere.

---

#### Frame Titles

Use explicit vertical spacing in the frametitle template:

```latex
\setbeamertemplate{frametitle}{%
  \vskip18pt%
  \nointerlineskip%
  {\usebeamerfont{frametitle}\usebeamercolor[fg]{frametitle}\insertframetitle\par}%
  \vskip2pt%
  {\color{AccentColor}\rule{\textwidth}{1.2pt}}%
  \vskip4pt%
}
```

Key points:
- The top \vskip controls breathing room from the slide edge
- Start at 16-18pt; adjust based on user feedback
- Do NOT rely on Beamer's default frametitle spacing

---

#### Footline / Page Numbers

MUST use a beamercolorbox with explicit rightskip.

```latex
\setbeamertemplate{footline}{%
  \begin{beamercolorbox}[wd=\paperwidth, ht=18pt, right, rightskip=1.5cm]{footline}%
    \insertframenumber\,/\,\inserttotalframenumber\vskip4pt%
  \end{beamercolorbox}%
}
```

Why this is critical:
- Trailing \hspace after content gets CLIPPED by the beamercolorbox boundary
- This means `\hfill{content}\hspace{Xcm}` does NOT reliably inset from the right
- The ONLY reliable method is setting `rightskip` on the containing beamercolorbox
- This was the #1 layout bug encountered in practice

Do NOT use:
```latex
% BROKEN: hspace gets clipped at box edge
\setbeamertemplate{footline}{%
  \hfill \insertframenumber \hspace{1.5cm}\vskip8pt%
}
```

---

#### Buttons & Navigation

Buttons using \hfill push to the right edge and WILL overlap with page numbers.

Fix: add \hspace matching the footline rightskip after every button group:

```latex
\hfill \hyperlink{label}{\beamerbutton{Back}}\hspace{1.5cm}
```

Apply this to EVERY slide with buttons, including:
- main slides with appendix links (SDID, ATT, etc.)
- appendix slides with Back buttons
- slides with multiple buttons on one line (add \hspace only after the last button)

When a slide has multiple buttons on separate \hfill lines, only the LAST line needs the trailing \hspace:
```latex
\hfill \hyperlink{a}{\beamerbutton{Back (A)}}
\hfill \hyperlink{b}{\beamerbutton{Back (B)}}\hspace{1.5cm}
```

---

#### Structural Rule

If spacing changes do not behave as expected:
-> the issue is structural, not numerical
-> fix the container (footline/template), not the text
-> inspect the beamercolorbox or template definition first

---

### Figure Integration

- If ANY figures have white backgrounds -> use white slide background
- Only use WarmWhite (#FAFAF8) if all figures have transparent or matching backgrounds
- Use `keepaspectratio` on all \includegraphics calls
- Figures created for 4:3 will not stretch correctly in 16:9; constrain with width only
- Avoid visible "boxed" figures against the background

Rule:
Visual integration > strict theme purity

---

### Appendix

- Separate with a plain divider slide (styled to match the title slide)
- Use `appendixnumberbeamer` package to restart slide numbering
- Preserve all hyperlink labels from the main deck
- All Back buttons must link to the correct main-deck label
- Keep appendix slides functional but not presentation-heavy:
  - no progressive reveals
  - tables can be denser
  - reduce decorative elements

---

### Implementation Rules

- Prefer structural fixes over spacing hacks
- Inspect container (beamercolorbox, templates) first
- Avoid repeated trial-and-error spacing
- Use \graphicspath{{figures/}} and store all images in a figures/ subdirectory
- Do not commit compiled outputs (.pdf, .aux, .log, .nav, .out, .snm, .synctex.gz, .toc)

---

### Verification

#### Compile

- Must compile with pdfLaTeX (not XeLaTeX unless explicitly required)
- Zero errors (warnings for overfull hbox on tables are acceptable)
- Run at least two passes to resolve cross-references and hyperlinks

---

#### Visual QA

Check:

- frame titles have top breathing room (not flush with slide edge)
- page numbers are inset from right edge (visible gap)
- no overlap between buttons and page numbers on ANY slide
- diagrams are centered and fit within the frame
- figures blend with background (no visible white boxes)
- dense tables are readable (check appendix slides especially)
- title slide elements are not crowded

---

#### Stress Test

Verify on:

- appendix slides with Back buttons (button vs page number overlap)
- dense tables (overfull vbox warnings, readability)
- multi-figure slides (subfigure alignment)
- TikZ diagrams (overflow, centering)
- navigation-heavy slides (robustness checklist with many buttons)
- the title slide and appendix divider (plain frames have different spacing)

---

### Failure Modes to Avoid

- overcrowded slides
- excessive bullets
- overuse of overlays
- edge-clipped elements (especially page numbers)
- diagram overflow (horizontal chain too wide for 16:9)
- figure/background color mismatch
- fragile spacing hacks (\hspace at box boundaries)
- button/page-number overlap
- broken hyperlinks between main deck and appendix

---

### Success Criteria

A successful deck:

- compiles cleanly with pdfLaTeX
- fits presentation time
- is easier to present than original
- looks clean and professional
- preserves academic rigor
- handles spacing robustly across ALL slides (including appendix with buttons)
- has no element flush against any slide edge

---

### Heuristic

When in doubt:

- simplify
- align
- add breathing room
- fix containers, not text
- optimize for live audience, not archive
