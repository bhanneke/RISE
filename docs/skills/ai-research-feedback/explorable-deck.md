<!-- DO NOT EDIT — auto-copied from skills/ai-research-feedback/details/explorable-deck.md -->

# `/explorable-deck`

Builds a Quarto reveal.js talk in the explorable-explanation style: one idea per slide under an assertion title, a concrete running example, run-time SVG figures the presenter steps through live, the source's own figures recoloured into the deck palette, speaker notes on every slide and an appendix for side questions. All chart numbers sit in one data file. The deck template ships next to the SKILL.md in the source repository.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-research-feedback/">AI Research Feedback (Claes Bäckman)</a></div><div><b>Category:</b> <code>slides</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-11-15</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/claesbackman/AI-research-feedback/contents/Skills/explorable-deck/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-research-feedback/explorable-deck/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/explorable-deck/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/claesbackman/AI-research-feedback?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Explorable deck

Build a Quarto reveal.js deck that teaches the way a good explorable does, but inside the frame a talk imposes: linear, timed, driven by a presenter, 1280×720 with no scrolling. The explorable's non-linear tree becomes a spine of counted slides plus an appendix of side rooms. Its playables become stages the presenter operates while talking. Its "static read must work" becomes: the printed PDF must carry the argument on its own.

The sibling skill `explorable-explanations` builds the website version, and `explorable-beamer` builds the same deck in LaTeX beamer for a user who names Beamer, LaTeX, TeX or PDF. This one produces a Quarto deck, and it reuses the website's models and numbers when one already exists for the topic.

### What you produce

One folder per deck, rendered with `quarto render index.qmd`:

```
<deck>/
  index.qmd            the deck: YAML header, one `##` per slide, `::: {.notes}` on every slide
  theme/deck.scss      tokens, faces, layouts, the stage, controls, figure frames
  theme/fonts.html     the three web fonts (system fallbacks in the theme)
  js/lib.js            drawing helpers and L.DATA, the single home of every number a chart uses
  js/deck-charts.js    the stages: CH['name'] = (el, {animate}) => cleanup
  js/include.html      the script tags Quarto appends to the body
  figs/*.svg           the source's figures, converted from PDF and recoloured (build output)
  figs/convert_figs.sh, figs/restyle_figs.py
  shoot_chrome.py      screenshots every slide, prints console messages
  README.md            how to render, check, present; where the numbers come from
  plan.md              the talk script (see below)
```

`scripts/new_deck.sh <path>` copies the template in `assets/template/` and the scripts into place. Start every new deck from it: the template already solves the reveal.js traps listed in the notes reference.

### Read first

1. The Explorable Explanations Playbook: Nicky Case, Bret Victor, Steven Strogatz. Read §1–4 and §10 closely and skim the rest once per project. It explains why the craft rules exist so you can apply them with judgment. Its three-act arc, ladder of abstraction, empathy for the perplexed reader, and message → mechanics apply to a talk unchanged. Its §6 (interaction craft) and §9 (the frontier) describe the website; for a talk, the interaction section of `deck-craft.md` overrides them.
2. Deck craft: how the explorable craft translates to slides, and what goes wrong. Read before planning, and again when reviewing.
3. Quarto and reveal.js notes: the template's layout vocabulary, the stage API, the figure pipeline, rendering, screenshots, PDF export, and the traps. Read before building.
4. Look at the four screenshots in references/example-deck/ of a finished deck built this way (a hook with two characters, an animated reveal stage, a paper figure beside prose, a coefficient plot), and at Case's Evolution of Trust for the broader vibe. The example deck is a housing-returns paper (Bäckman, D'Lima and Khorunzhina, "Anna and Bo"); if the source is that paper or a neighbour of it, borrow nothing from the examples but the register. For any topic, take the register, not the content: the topic decides the colours, the characters and the shapes.

### Review level

The render and its checks always run. The subagent review is the slow part of a run: five or six agents each read the whole deck and every screenshot, and a second version is built after them. It is worth most once the user has seen the deck and settled the content, so it runs only when asked:

| level | how the user asks | what runs after the checks |
|---|---|---|
| none (default) | a plain request for a deck | the self-check only; the handover says review was skipped and how to ask for it |
| `review` | "with review", "review the deck", `/explorable-deck review` | the four judges and Maria, then a second version |
| `full` | "full review", "with the creative director", `/explorable-deck full` | the above, then the creative director |

A request to review a deck that already exists skips steps 1–6: run the final check in step 7 so the screenshots are current, then steps 8–11 at the level asked. "Review" on its own means `review`.

### Working rhythm

1. **Read the source.** The paper, notes, or codebase, and any existing explorable for the topic. If one exists, its `lib.js` data object and chart code are the deck's starting material: copy them rather than redrawing, so the two never disagree on a number.
2. **Fix the frame** before writing a slide: the audience (Strogatz's traumatized, perplexed or naturals, and which one the slide text is written for), the length in minutes, the venue. When the user has not said, assume a 20-minute conference talk for a mixed academic room, and say so. Length changes the shape, not just the count:

   | slot | counted slides | stages | build-ins | bets | literature slide |
   |---|---|---|---|---|---|
   | 12 min | 8–10 | 1 | 1 | 1 | no, one sentence on the hook |
   | 20 min | 13–16 | 2–3 | 1–2 | 1–2 | one slide |
   | 45+ min | 25–35 | 3–5 | 2 | one before each BUT | one slide, plus recap slides as cognitive gates |

   Everything a questioner might want goes in the appendix; in a long lecture the rooms move into the spine.
3. **Write `plan.md`** as a scriptwriter: the one big thing in a sentence, the cause → effect chain with its THEREFORE and BUT turns, then slide by slide what the room sees, what the presenter does with each stage, what they should notice, and which appendix room each question opens. Name the characters and the four semantic colours here.
4. **Scaffold** with `scripts/new_deck.sh`. Keep the citation comment at the top of `index.qmd` when you replace the template content. Give each of the four colour tokens a topic alias in `theme/deck.scss` (`--gain: var(--primary);`) and paint the charts with the aliases; never rename the generic tokens, because the classes and the notes reference depend on them. Fill `L.DATA` and convert the source figures you will use. If a `dataviz` skill is available, its rules on marks and colour apply inside the palette; the palette itself comes from this theme.
5. **Build the hook and the first section**, render, screenshot, and look at every screenshot yourself before going on. In an interactive session, show this batch to the user before building the rest.
6. **Build the rest.** Every stage has a caption that says whether it is measured or stylised, a finished state for `?static` and print, and a speaker note that says what to do with it. Every evidence slide has a source line. Titles are assertions.
7. **Check.** While building, iterate with `quarto render index.qmd` and `python shoot_chrome.py N …`, numbering the slides you changed and every slide touched by a change to the theme, `L.DATA` or a shared chart. A numbered run replaces only those screenshots and reports console messages only for those slides. Inserting or deleting a slide shifts the numbers after it, so run it without numbers after such a change. Fix every console message and every slide whose content reaches the bottom edge of the frame, where the progress bar and menu button sit, as they appear. When the deck is complete, run the final check once: `quarto render index.qmd`, then `python shoot_chrome.py` with no numbers. Fix every finding and read all the screenshots.
8. **Self-check**, at every level: go through "What goes wrong" in `references/deck-craft.md` against the source and the screenshots you have already read, and fix what you find. This is your own pass, with no subagents.
9. **Review**, at `review` and `full` only: the four judges and Maria, prompts below. Then build the second version from what they found and run the final check again.
10. **Creative director**, at `full` only, prompt below. Apply the ideas that survive the craft rules and run the final check again.
11. **Write the deck's README** and tell the user where the deck is, how to present it (S speaker view, F fullscreen, O overview, E print view then print to PDF), and which stages are live. If no review ran, close with one line saying so and how to ask for it: "review the deck" runs the judges and Maria, and "full review" adds the creative director.

### Review prompts

Run these at the `review` and `full` levels only, after the final check passes. Launch the four judges and Maria together in one message so they run in parallel; the creative director comes after the second version. Each reads `index.qmd`, `js/deck-charts.js`, `plan.md`, the craft reference, and the screenshots in `_shots/`.

**Four-dimension judges.** One subagent per dimension, each told to find violations of `references/deck-craft.md` and to list them by slide number with the sentence or element at fault, no fixes:

- *Writing*: do the titles read as the argument in sequence, is each slide one idea, does the slide text say only what the room should read while the presenter talks, are numbers reported with their magnitude and their source?
- *Slides*: does anything crowd or overflow, is whitespace doing its job, do layouts vary with the idea, is anything decorative competing with the content?
- *Visuals*: does colour encode the argument and nothing else, does every stage and figure teach the idea its slide asserts, is every stylised element labelled as such, would it read from the back of the room?
- *Teaching*: where does the reader start, is the concrete instance established before the abstraction, are the BUT turns earned, does the ending give the room its own question?

**The audience member.** One subagent:

```
Put yourself in the shoes of Maria, a sharp researcher in the talk's own field, in the fourth row at 4 p.m. on the second day of a conference. She has seen three hundred decks and likes about ten of them. She is not hostile, but her attention is a resource the speaker has to earn on every slide.

Go through the deck in order, from the code and the screenshots, and say exactly where she stops following: a slide that jumps to a new idea without setting it up, a title that is a label rather than a claim, a number without a magnitude she can feel, a chart she has to decode, a promise from an earlier slide left unfulfilled, a stage whose point she cannot see from her seat, a slide that says what the previous one said. Be blunt and specific, slide by slide. Point at problems only; do not propose fixes.
```

Treat what she finds as the opportunity it is, and build the second version properly rather than patching sentences.

**Creative director.** One subagent, at the `full` level, after the second version is built and structure and writing are settled:

```
Act as creative director for this deck. Review the theme, the chart code and the screenshots. Assume structure, teaching and writing are already right. Your job is personality: what would make someone recognise this deck from one slide across the room?

Think at two scales. The whole deck: colour, type, a recurring visual motif or material that belongs to this topic, motion that carries meaning. Individual slides: a distinctive treatment for the hook, the reveal, the dividers, the closing slide; a small drawn illustration or visual joke that makes one idea stick.

Be a radical thinker with tasteful restraint. Keep the clarity and the fixed frame; projectors and print flatten shaders and 3D, so personality comes from drawing, type and colour. Propose your strongest ideas with a concrete description of how two or three existing slides would change, so the result can be pictured before it is built. If an image-generation skill is available in this session you may use it; otherwise everything is drawn in SVG or CSS.
```

### Rules that break decks

The full list with reasons is in the notes reference. The ones that fail silently:

- A `###` or any heading inside a slide body makes pandoc open a nested section, and reveal.js turns the slide into a vertical stack. Use `[Text]{.colhead}` for a column heading or `[Text]{.ph}` for a small heading anywhere else.
- Never name a class `.controls`; reveal.js hides it.
- Appendix slides carry `{visibility="uncounted"}` so the count ends on the closing slide.
- Slides do not scroll. What does not fit is a second slide, not a smaller font.
- Numbers come from `L.DATA` or the source's tables, never from another slide's prose. A number that also appears in a chart is written as `[]{.data key="specs.0.beta" d="3"}` so the prose reads the same object the chart does. Significance comes from the table's stars (`sig: true/false` in `L.DATA`), not from rounded standard errors, because the two disagree in exactly the marginal rows a talk cares about.
- Slide numbers, in the plan, the notes and the reviews, are the screenshot numbers: the title slide is 01.
- Room links are `[text](#slide-id)`. Quarto adds the `/` itself; `#/slide-id` in the source renders as `#//slide-id` and opens the title slide.
- Screenshots are taken with `?static` so build-in animations do not leave half-drawn charts.
