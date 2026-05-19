<!-- DO NOT EDIT — auto-copied from skills/evoskills/details/nano-banana.md -->

# `nano-banana`

AI-generated inline figures (Google Gemini Nano Banana)

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
name: nano-banana
description: "Generate professional presentation slides and high-quality illustrations using Gemini image generation API (Nano Banana 2), with interactive browser-based review and iterative editing. Full workflow: content planning conversation → slides_plan.json → batch image generation → review with feedback → targeted slide editing → PPTX packaging. Use when: user wants to create a presentation, make slides, generate a PPT/PPTX, prepare a talk deck, design visual slide content, or generate high-quality figures/illustrations for papers and documents. Do NOT use for: writing academic papers (use paper-writing) or planning academic conference talk narrative structure (use academic-slides)."
allowed-tools: "write_file edit_file read_file think_tool execute"
metadata:
  author: EvoScientist
  version: '1.0.0'
  tags: [core, presentation, image-generation]
---

# Nano Banana

Generate high-quality presentation slides as images using Gemini's image generation API, review them interactively in a browser, and iteratively edit based on feedback.

## When to Use This Skill

- User asks to create a presentation, slide deck, or PPT
- User wants to generate visual slides for a talk or lecture
- User has a document or outline and wants slides based on it
- User says "make me a PPT", "generate slides", "create a presentation"
- User wants to edit or refine existing generated slides
- User needs high-quality figures, diagrams, or illustrations for papers or documents
- User asks to generate research figures, architecture diagrams, or concept illustrations

**Do NOT use for:**
- Writing academic papers → use `paper-writing`
- Planning academic conference talk narrative structure → use `academic-slides`

---

## Before You Start: Prerequisites

Before proceeding with any slide generation, verify these prerequisites:

1. **API Key**: Check that a Google API key is available. Run:
   ```bash
   echo $GOOGLE_API_KEY
   ```
   If empty, ask the user to provide one. They can either:
   - Set it via config: `EvoSci config set google_api_key <key>`
   - Provide it directly (pass via `--api-key` argument)
   - If the user provides the key in conversation, pass it to scripts with `--api-key`

2. **Language**: Ask the user what language the slide content should be in. This affects the content you write in `slides_plan.json`, not the style template.

---

## Core Workflow

```
Phase 1: Content Planning Conversation     ← most important phase
Phase 2: Generate slides_plan.json
Phase 3: Select Style & Generate Slides
Phase 4: Launch Review Server
Phase 5: Apply Feedback Edits              ← repeat Phase 4-5 until satisfied
Phase 6: Package as PPTX
Phase 7: Cleanup
```

Follow these phases in order. Do NOT skip Phase 1 — the quality of generated slides depends directly on planning depth.

---

## Phase 1: Content Planning Conversation

This is the most critical phase. Rushing to generation without proper planning produces mediocre slides. Engage the user in a structured conversation:

**Step 1 — Understand the context:**
- What is the topic of the presentation?
- Who is the audience? (technical peers, executives, students, general public)
- How long is the talk? (this determines page count)
- What is the occasion? (conference, internal talk, lecture, pitch)

**Step 2 — Define the storyline:**
- What is the opening hook? (a surprising fact, a question, a trend)
- What are the 3-5 main sections or arguments?
- What is the key takeaway the audience should remember?
- What is the closing message?

**Step 3 — Outline per-page content:**
- For each slide, agree on: title + 2-4 key points + visual description
- Identify which slides are cover, content, or data type
- Ensure logical flow between pages

**Duration-to-page-count guidance:**

| Duration | Pages | Structure |
|----------|-------|-----------|
| 5 min | 5 | Cover + 3 content + closing |
| 10-15 min | 8-12 | Cover + intro + 3-4 sections + summary + closing |
| 20-30 min | 15-20 | Cover + intro + 5-6 sections + summary + closing |
| 45-60 min | 25-30 | Cover + intro + 7-9 sections (2-3 pages each) + summary + closing |

**If the user provides a document or outline**, read it thoroughly, then propose a slide breakdown for approval before proceeding.

---

## Phase 2: Generate slides_plan.json

Create a `slides_plan.json` file in the workspace root with this schema:

```json
{
  "title": "Presentation Title",
  "total_slides": 10,
  "slides": [
    {
      "slide_number": 1,
      "page_type": "cover",
      "content": "Title: My Presentation\nSubtitle: A subtitle here\nLabel: 2026 Edition"
    },
    {
      "slide_number": 2,
      "page_type": "content",
      "content": "Title: First Topic\nKey points:\n- Point one\n- Point two\n- Point three"
    },
    {
      "slide_number": 3,
      "page_type": "data",
      "content": "Title: Key Metrics\nMetric 1: 95% accuracy\nMetric 2: 3x faster\nMetric 3: 10k users"
    }
  ]
}
```

**page_type values:** `cover`, `content`, `data`

### Critical Content Field Rules

The `content` field is what gets passed to the image generation model. Follow these rules strictly:

1. **DO** write descriptive titles and bullet points
2. **DO** describe the visual layout you want (e.g., "left-right comparison", "4 icon cards")
3. **DO NOT** prefix lines with "Slogan:", "Visual:", "Points:", or any meta-labels — the model will render these as visible text on the slide
4. **DO NOT** put the same sentence in both the title area and the bottom of the content — it causes duplication
5. **DO NOT** include footer text, page numbers, or watermark instructions

**Bad example** (meta-labels leak as visible text):
```
Title: Why AI Matters
Visual: left-right comparison chart
Points:
- Point one
- Point two
Slogan: AI changes everything
```

**Good example** (clean, no meta-labels):
```
Title: Why AI Matters
Visual layout: left-right comparison chart showing traditional vs AI approach
Key points:
- Point one with brief explanation
- Point two with brief explanation
Bottom tagline: AI changes everything
```

---

## Phase 3: Select Style & Generate Slides

### Available Styles

| Style | File | Visual Characteristics | Best For |
|-------|------|----------------------|----------|
| Lineal Color | `styles/lineal-color.md` | White background, teal accents, flat 2D icons, info cards | Technical talks, lectures, educational |
| Gradient Glass | `styles/gradient-glass.md` | Light pastel background, frosted glass cards, Apple Keynote feel | Product launches, pitches, SaaS |
| Vector Illustration | `styles/vector-illustration.md` | Cream background, black outlines, retro colors, toy-model charm | Educational, children's content, brand stories |

Present the styles to the user and let them choose. If unsure, recommend Lineal Color as the default.

### Available Models

| Model | Speed | Quality | When to Use |
|-------|-------|---------|-------------|
| `gemini-3-pro-image-preview` | Moderate | Best | Final version, important presentations |
| `gemini-3.1-flash-image-preview` | Fast | Good | Drafts, rapid iteration, large decks |
| `gemini-2.5-flash-image` | Fastest | Basic | Quick prototypes, bulk generation |

For first-time generation, recommend `gemini-3.1-flash-image-preview` (fast iteration). Switch to `gemini-3-pro-image-preview` for the final version.

### Generate Command

```bash
python /skills/nano-banana/scripts/generate_ppt.py \
  --plan slides_plan.json \
  --style /skills/nano-banana/styles/lineal-color.md \
  --model gemini-3.1-flash-image-preview \
  --output ppt_output
```

**Arguments:**
- `--plan` (required): Path to slides_plan.json
- `--style` (required): Path to style template
- `--model`: Image generation model (default: `gemini-3-pro-image-preview`)
- `--resolution`: `2K` (default) or `4K`
- `--output`: Output directory (default: `ppt_output/TIMESTAMP`)
- `--api-key`: Google API key (if not in environment)
- `--workers`: Number of parallel workers (default: 1, recommended: 3-5 for large decks)

Output structure:
```
ppt_output/
├── images/
│   ├── slide-01.png
│   ├── slide-02.png
│   └── ...
├── prompts.json    # All prompts used (for debugging)
└── index.html      # Browser viewer
```

---

## Phase 4: Launch Review Server

Start the interactive review server so the user can review slides and write feedback:

```bash
python /skills/nano-banana/scripts/serve_viewer.py \
  --dir ppt_output \
  --plan slides_plan.json \
  --port 8080 \
  --pid-file .viewer.pid
```

Tell the user:
> Review server is running at http://localhost:8080. Open it in your browser to review each slide. Write feedback in the text box below any slide that needs changes, then click "Save Feedback". Tell me when you're done.

The server saves feedback directly into `slides_plan.json` as a `feedback` field on each slide.

Wait for the user to confirm they have saved their feedback before proceeding.

---

## Phase 5: Apply Feedback Edits

Read `slides_plan.json` and find all slides with a non-empty `feedback` field. For each one, run the edit script:

```bash
python /skills/nano-banana/scripts/edit_slide.py \
  --input ppt_output/images/slide-{NUMBER}.png \
  --instruction "{FEEDBACK_TEXT}" \
  --output ppt_output/images/slide-{NUMBER}.png \
  --model gemini-3.1-flash-image-preview
```

**Arguments:**
- `--input` (required): Path to the original slide image
- `--instruction` (required): The edit instruction (from feedback field)
- `--output`: Output path (default: overwrite input)
- `--model`: Image generation model
- `--api-key`: Google API key (if not in environment)

After editing all slides with feedback, clear the `feedback` fields from `slides_plan.json` and tell the user to refresh the browser to see updated slides.

If the user has more feedback, repeat Phase 4-5. This review-edit cycle continues until the user is satisfied.

---

## Phase 6: Package as PPTX

Once the user approves all slides, ask for the desired filename and package them:

```bash
python /skills/nano-banana/scripts/package_pptx.py \
  --dir ppt_output/images \
  --output presentation.pptx \
  --kill-server .viewer.pid
```

**Arguments:**
- `--dir` (required): Directory containing slide-XX.png images
- `--output` (required): Output .pptx file path
- `--kill-server`: PID file from serve_viewer.py — automatically stops the review server after packaging

---

## Phase 7: Cleanup

- The review server is automatically stopped by `package_pptx.py --kill-server`
- Ask the user if they want to keep `ppt_output/` directory or clean it up
- The `slides_plan.json` can be kept for future re-generation

---

## Counterintuitive Rules

1. **Never include meta-labels in content** — Words like "Slogan:", "Visual:", "Points:" will be rendered as visible text on the slide. Describe what you want without prefixes.

2. **Content describes WHAT, not HOW** — The style template handles visual layout. The content field should focus on text and logical structure, not colors or positioning.

3. **More planning = better slides** — Spending 10 minutes on Phase 1 conversation saves hours of re-generation. Do not rush to Phase 3.

4. **Edit, don't regenerate** — When a slide needs minor changes (text fix, color change, remove footer), use `edit_slide.py` instead of regenerating from scratch. Editing preserves visual consistency.

5. **Use flash model for drafts** — `gemini-3.1-flash-image-preview` is fast enough for iteration. Only switch to `gemini-3-pro-image-preview` for the final version after all feedback is addressed.

6. **Never read generated images yourself** — Not all models support multimodal input. Do NOT use `read_file` on generated PNG images to check quality. Always launch the review server and let the user inspect slides visually in the browser. The user's feedback is your only quality signal.

7. **One idea per slide** — Do not pack multiple concepts into a single slide. If a slide has more than 4 bullet points, split it into two slides.

8. **Bottom taglines should not repeat the title** — If the title says "Why AI Matters", the bottom tagline should add new insight, not restate the title.

---

## Scripts Reference

| Script | Purpose | Key Arguments |
|--------|---------|---------------|
| `scripts/generate_ppt.py` | Batch generate all slides from plan | `--plan`, `--style`, `--model`, `--output`, `--resolution`, `--api-key`, `--workers` |
| `scripts/edit_slide.py` | Edit a single slide based on instruction | `--input`, `--instruction`, `--output`, `--model`, `--api-key` |
| `scripts/serve_viewer.py` | Local review server with feedback | `--dir`, `--plan`, `--port`, `--no-open`, `--pid-file` |
| `scripts/package_pptx.py` | Package slide images into .pptx | `--dir`, `--output`, `--kill-server` |

---

## Style Template Format

Style templates are markdown files in `styles/` with a fixed structure that `generate_ppt.py` parses:

| Section | Purpose | Parsed by Code |
|---------|---------|----------------|
| `## Base Prompt` | Visual specifications shared by all slides | Yes — injected into every prompt |
| `## Page Templates` | Layout descriptions per page type | Fallback only |
| `## Examples` | Actual prompt templates with `{Base Prompt}` and `[Content]` placeholders | Yes — primary templates |
| Other sections | Documentation only | No |

To create a new style: copy an existing `.md` file, modify the `## Base Prompt` and `## Examples` sections. The code extracts `### Cover`, `### Content`, and `### Data` code blocks from `## Examples`.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/EvoScientist/EvoSkills/contents/skills/nano-banana/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>EvoScientist/EvoSkills</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../evoskills.md">EvoSkills</a></dd>
<dt><b>Category</b></dt><dd><code>figures</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>Apache-2.0</dd>
<dt><b>Last update</b></dt><dd>2026-05-17</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/EvoScientist/EvoSkills">⭐ EvoScientist/EvoSkills</a><br><img src="https://img.shields.io/github/stars/EvoScientist/EvoSkills?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/EvoScientist/EvoSkills" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/evoskills/nano-banana/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/evoskills.yml">edit on GitHub</a>.</p>
</div>

</div>
