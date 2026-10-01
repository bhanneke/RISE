<!-- DO NOT EDIT — auto-copied from skills/econ-skills/details/latex-slide.md -->

# `/latex-slide`

Builds, edits, fixes, and reviews Beamer slide decks, with an automated overflow audit.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../econ-skills/">econ-skills (zbsaygin)</a></div><div><b>Category:</b> <code>slides</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/zbsaygin/econ-skills/contents/latex-slide/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/econ-skills/latex-slide/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/zbsaygin/econ-skills/blob/main/latex-slide/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/zbsaygin/econ-skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## LaTeX Slide Deck Manager

Build, edit, fix, and review Beamer slide decks for academic presentations.

### Trigger conditions

Invoke this skill when the user asks to:
- Create / build / start / initialize a slide deck or presentation
- Add graphs, tables, model slides, literature, or content to an existing deck
- Fix / debug / resolve compilation errors in a slide deck
- Review / check / audit / proofread a slide deck
- Any task involving a Beamer `.tex` file

### Task routing

Determine which task the user wants from `$ARGUMENTS` or their message:

| Keywords | Task |
|----------|------|
| create, build, start, initialize, new deck | **Initialize** |
| add, insert, include, put, new slide, new section | **Add** |
| fix, debug, error, broken, won't compile, doesn't compile | **Fix** |
| review, check, audit, proofread, typo, inconsistency | **Check** |

If the intent is ambiguous, ask the user which task they need.

### Style guide

All tasks must follow these formatting rules. Reference this section when creating or editing slides.

#### Colors
- `Accent1` (rgb 0.94, 0.87, 0.8) — frame backgrounds, block body background
- `Accent2` (rgb 0.0, 0.47, 0.44) — accents, section fillers, takeaway arrows, block title background
- `Accent3` (rgb 0.75, 0.15, 0.45) — sparingly for emphasis
- `BodyText` (HTML #111111) — body text

#### Block environments (propositions, theorems, etc.)
- Block title: white text on `Accent2` background
- Block body: `BodyText` on `Accent1` background
- Use Beamer's built-in `block` environment: `\begin{block}{Proposition (Title)}...\end{block}`
- Stick to the four palette colors defined in the template; do not introduce additional accent colors

#### Hyperlink buttons
- Always bottom-right: `\hfill \hyperlink{label}{\beamerbutton{Text}}`
- Body slides: `[label=topic_main]` with `\beamerbutton{Details}` or descriptive text (e.g., "Robustness", "Time Series")
- Appendix slides: `[label=topic_appendix]` with `\beamerbutton{Back}`
- Every body slide that has appendix counterparts MUST have a forward button
- Every appendix slide MUST have a back button to its body counterpart

#### Label convention
- Body: `[label=topic_main]`
- Appendix: `[label=topic_appendix]`
- Multiple appendix slides for same topic: `[label=topic_appendix_v2]`, `[label=topic_appendix_detail]`, etc.
- Before assigning labels, grep the file for existing labels to avoid collisions

#### Itemize spacing
```latex
\begin{itemize}
    \setlength{\itemsep}{4pt}
    \vspace{4pt}
    \item First item
    \item Second item
\end{itemize}
```
The `\vspace{4pt}` before the first `\item` prevents the first item from being too tight against the preceding element. Wrap in `\begin{minipage}{0.9\textwidth}` for better margins.

#### vspace usage
- Always leave an empty line before and after `\vspace{x pt}` commands, otherwise LaTeX may swallow them.

#### Graphs and images

**Aspect-ratio sizing rule.** For a standard graph slide — one figure, frametitle, footer with optional buttons, and no body text — pick the binding dimension based on the figure's aspect ratio. LaTeX preserves aspect automatically when only one dimension is specified; no `keepaspectratio` needed.

Measure the aspect ratio by reading the figure's PDF:

```
python3 -c "import fitz; r=fitz.open('ABSOLUTE_PATH')[0].rect; print(round(r.width/r.height, 3))"
```

Then apply:
- **Aspect ≥ 1.5** (wide figure) → `\includegraphics[width=0.9\textwidth]{ABSOLUTE_PATH}`
- **Aspect < 1.5** (tall figure) → `\includegraphics[height=0.82\textheight]{ABSOLUTE_PATH}`

These numbers are calibrated for the Madrid 16:9 template so the figure fills as much of the usable area as possible. If the audit protocol flags the frame after compile, let the fix flow handle tuning — don't hand-tweak during placement.

For slides with body text, bullets, or multiple figures, the rule doesn't apply — use judgment and let the audit catch issues.

- Use `clip, trim=Xcm Ycm Zcm Wcm` to crop excess whitespace.
- Always use absolute paths for graph files.
- Add source line: `\vfill \tiny Source: Data source here`.

#### Two-column layouts
For slides with text + figure side by side:
```latex
\begin{columns}[T]
    \begin{column}{0.48\textwidth}
        \begin{itemize}
            \setlength{\itemsep}{4pt}
            \vspace{4pt}
            \item Key point one
            \item Key point two
        \end{itemize}
    \end{column}
    \begin{column}{0.48\textwidth}
        \includegraphics[width=\textwidth]{absolute_path.pdf}
    \end{column}
\end{columns}
```
Use `[T]` for top-alignment. Adjust column widths (should sum to ~0.96 to leave a gap). Common use: bullet summary on left, supporting figure on right.

#### Section fillers
```latex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{Subsection Title}
\begin{frame}
    \centering
    \LARGE
    \textcolor{Accent2}{N. Section Filler Title}
\end{frame}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

#### Appendix structure
```latex
\appendix

\begin{frame}
    \centering
    \Huge
    Appendix
\end{frame}

\begin{frame}
    \frametitle{Appendix Outline}
    \tableofcontents
\end{frame}

\section{Appendix Section Title}
\begin{frame}
    \centering
    \Huge
    Appendix \\
    \vspace{20 pt}
    \large
    Appendix Subsection Title
\end{frame}
```

#### References
```latex
\begin{frame}[allowframebreaks]
    \frametitle{References}
    \footnotesize
    \bibliographystyle{aer}
    \bibliography{<REFERENCES_PATH>}
\end{frame}
```
Always use the absolute path defined by `<REFERENCES_PATH>`. Style is always `aer`.

#### Content philosophy
- Slides help the audience follow — they should NOT tell everything
- The presenter comments on slides verbally; bullets are guides, not scripts
- Keep bullets concise and well-separated
- If a slide is too packed, split or use `\small` (see overflow handling below)
- Use `\pause` sparingly — one per slide max, to reveal the punchline or key result. Never before every bullet (annoying for the audience).

#### Visual QA — The core principle
**Never reason about slide layout from code alone.** After compiling, always read the output PDF with the Read tool and look at the actual result. Use subagents to read specific pages when reviewing a full deck.

This applies to every task: adding slides, fixing layout, reviewing a deck. One look at the PDF tells you what's wrong; guessing from LaTeX code leads to long debugging loops.

#### Overflow handling
- **Use `\small`** for math-heavy, proof, or appendix-style content that may be skipped.
- **Split into multiple slides** for main narrative, key arguments, model exposition. Prefer splitting over shrinking.
- Never reduce global spacing to fix overflow — fix individual slides instead.
- A slide with 4+ outer-level items and equations will almost always need `\small` or splitting.
- Nested lists compound the problem: 3 outer items each with 2-3 sub-items is likely to overflow.

#### Audit protocol

Run this protocol after every compile that changed one or more frames. It replaces ad-hoc overflow checking with a gated, iterative loop backed by a Python audit script and a sub-agent visual pass.

**Step 1 — Identify changed frames (the diff gate).**
From your Edit operations, collect the set of frames whose source changed. A frame is "changed" if the net character delta inside its `\begin{frame}...\end{frame}` body is **> 20 characters** (insertions + deletions combined) or if the frame is newly added. Skip frames with smaller changes. The 20-char threshold is intentionally wide — about five words — so any edit that could plausibly alter layout passes through, and frames you did not touch are not re-audited.

**Step 2 — Compile and flag.**
Compile the deck (see compilation protocol). Then run:

```
python <SKILLS_DIR>/latex-slide/audit/overflow_audit.py \
    --tex PATH.tex --pdf PATH.pdf --log PATH.log \
    --only-flagged --pretty
```

The script emits JSON per frame with any of the following flags:
- `log_overfull_hbox` / `log_overfull_vbox` — `Overfull` warnings from the pdflatex log, pinned to the frame's source-line range (catches horizontal overflow, which PyMuPDF misses).
- `pymupdf_vertical_tight` / `pymupdf_vertical_overflow` — non-footer content extends past `y = 243` / `y = 247`; footer text (top y > 247.5) is excluded. Calibrated for 16:9 Madrid theme (footer text block y0=247.79, y1=253.77).
- `line_count_excess` — weighted line count > 8 where each `\item` = 1 and each display-math row (lines in `align`, `equation`, `gather`, `multline`, `\[ ... \]`) = 2.

Thresholds are defined as constants at the top of `overflow_audit.py` and should be tuned there, not in prose here.

Intersect the script's flagged frames with the changed-frames set from Step 1. The intersection is the audit set.

**Step 3 — Visual sub-agent audit.**
For each frame in the audit set, dispatch a Sonnet sub-agent in parallel using Template A in `<SKILLS_DIR>/latex-slide/audit/subagent-prompts.md`. Pass: PDF path, page number, frame title, full frame source, the flags raised, and the current round number.

Each sub-agent returns exactly one verdict:
- `ok` — looks fine; automated flag was a false positive.
- `split` — frame must be broken across two frames; includes a split proposal.
- `adjust` — specific copy-pasteable mechanical changes (font, `\vspace`, image width).
- `unsure` — cannot decide, or the fix requires editorial judgment. Escalate to the user.

**Step 4 — Apply and iterate.**
Apply `split` and `adjust` verdicts directly to the `.tex`. Collect every `unsure` verdict for the final escalation list — do NOT act on them. Recompile, then re-run Steps 2–3 using the frames you just modified as the new changed-frames set.

**Step 5 — Max 3 rounds, then escalate.**
If any frame is still flagged after 3 rounds, stop touching it and add it to the escalation list. For each escalated frame, report to the user:
- Frame index, page number, and title
- Which flags persist after round 3
- Every verdict the sub-agent returned across the 3 rounds, with its recommended changes
- What decision the user needs to make

Also include every `unsure` verdict from any round in the escalation list, with its `QUESTIONS_FOR_HUMAN` payload.

**Step 6 — Summary.**
Report counts: frames changed, frames flagged, verdicts applied by type (`ok` / `split` / `adjust`), frames escalated and why. Do not mark the audit complete if the escalation list is non-empty — it means the user still has pending decisions.

#### Common layout problems and fixes

**Figures:**
- Too small or too large → adjust `width=X\textwidth` multiplier. Read the PDF to judge — don't guess.
- If a figure can't fit without making content illegible, **stop and flag to the user**.

**Notes and source lines:**
- Note/source too close to figure, too far from footer → add `\vspace` before and after so the note sits just one line above the footer.
- If note + source fits one line, keep them on one line. If they overlap with beamer buttons or are too long, split: note first line, source second line.
- Source can share a line with buttons (source left, buttons right). Note goes one line above.
- Beamer buttons and note on the same line will overlap → buttons should be one line above footer (right-pushed), note one line above buttons (left-pushed).

**Titles:**
- Title wrapping to two lines looks ugly → rephrase to fit one line. If it genuinely can't fit, split the idea across subtitle or restructure the slide.

**Bullet spacing:**
- Too few bullets with too much whitespace → increase `\itemsep` and `\vspace` to spread content.
- Too many bullets crammed together → decrease `\itemsep`, or split the slide.
- Adjust both `\itemsep` and the initial `\vspace` to center content vertically on the slide.
- **Nested items**: inner `\itemsep` should be less than outer (decrease by ~2pt). This creates visual hierarchy.

**Bullet length:**
- Bullets should be one line. Rarely two lines if unavoidable, but many 2-line bullets look ugly — use keywords and helper words, not full sentences.

**Math:**
- Equations that don't fit → use `align*` with `&` markers to split across multiple lines.

**Tables:**
- Must fit the slide. Use `\scriptsize` or `\footnotesize` for dense tables. If it still can't fit without being illegible, **flag to the user** — don't force it.

#### Splitting slides
- Use numbered suffixes like "(1/2)" and "(2/2)" for technical content that forms a continuous argument (e.g., proofs, multi-step derivations).
- Use distinct descriptive titles for narrative content that can stand alone.
- When splitting an `enumerate` across two slides, use `\setcounter{enumi}{N}` on the second slide to continue numbering.
- Repeat the key equation at the top of continuation slides if needed for context.
- Avoid creating slides that are too thin (just one bullet). If a natural split would produce a very thin slide, prefer `\small` instead.

#### Deck structure convention
The standard deck ordering is:
1. Title slide
2. Question / motivation slide
3. Literature review slide
4. Agenda / TOC slide
5. Section 1 (with subsection fillers between subsections)
6. Section 2, 3, ...
7. Appendix header (big "Appendix" filler)
8. Appendix outline
9. Appendix sections with subsection headers
10. References

---

### Task 1: Initialize

Create a new slide deck from scratch.

#### Step 1.1: Confirm output path
Ask the user where the `.tex` file should be created if not clear from the prompt.
- Default convention: `<PROJECTS_DIR>/<project_name>/slides.tex`
- Never overwrite an existing file without asking first.

#### Step 1.2: Read the template
Read the template fresh from `<SKILLS_DIR>/latex-slide/template.tex`. Never use a cached copy — the user may update the template over time. If converting from an existing deck, diff its preamble against the template to catch any custom macros the user added that need to be preserved.

#### Step 1.3: Gather context
Check all that apply:
1. **User prompt**: topic, purpose, structural hints
2. **Working directory**: Glob for `*.md`, `*.tex` files; read relevant ones
3. **Explicit context**: files provided via `--context` argument
4. **Graph folder**: files in `--graphs` folder
5. **Conversation context**: prior discussion about the project

#### Step 1.4: Choose initialization mode

- **From previous deck**: User provides a `.tex` file. Read it, preserve slide content, replace preamble with template preamble, clean up formatting to match style guide.

- **From prompt**: User describes what the deck should cover. Construct a section skeleton with title, question, literature, agenda, body sections, appendix header, references.

- **From project notes**: User points to markdown files. Read them, identify key findings/arguments, create a skeleton that maps the narrative to sections. Keep bullets concise — extract the essence, don't copy verbatim.

- **From graphs**: User provides a folder of graphs/figures. This is the most involved mode:
  1. Launch subagents to analyze each graph: read the image, search for the code that produced it (look in nearby Python/Stata/Julia scripts), determine what it shows and its message.
  2. Group graphs thematically into sections.
  3. Pick the most impactful graphs for the body; rest go to appendix.
  4. Create section structure with subsection fillers.
  5. Assign descriptive titles based on what each graph shows.
  6. Wire all body-appendix hyperlink buttons.

If the user doesn't specify a mode, infer from context. If still unclear, ask.

#### Step 1.5: Organize content
- Build the deck structure following the deck structure convention (see style guide)
- For graph-based init: assign labels (`topic_main`, `topic_appendix`), wire buttons both ways
- Include section fillers between subsections
- Add appendix header, appendix outline, and appendix subsection headers
- Add the commented-out ready-to-copy template slides at the end (they are already in the template)

#### Step 1.6: Build the deck
Replace placeholders in the template:
- `TITLE` and `Short Title` with the presentation title
- `DATE` with the presentation date (or `\today`)
- Replace `% SECTIONS_PLACEHOLDER` with the organized content
- Keep the template's default author; add co-authors only if specified

#### Step 1.7: Compile and verify
Follow the compilation protocol (see below). Iterate until the deck compiles with 0 errors. Common init-time issues: placeholder graph paths (replace `GRAPH_PATH` with actual paths or remove those example slides), missing citekeys.

#### Step 1.8: Summary
Tell the user: where the file was created, what sections exist, how many body vs. appendix slides, and suggest next steps.

---

### Task 2: Add

Add new content to an existing slide deck.

#### Step 2.1: Parse what to add
Identify the content type:
- **Graphs/figures**: image files (PDF, PNG) to include
- **Tables**: regression tables, summary statistics
- **Model slides**: economic model (agents' problems, equilibrium, etc.)
- **Literature bullets**: new papers to add to lit review
- **Content slides**: bullet points, text, equations
- **Section**: a new section with filler and subsection structure

Identify source material: file paths, URLs, conversation context.

#### Step 2.2: Read the current deck
Read the full `.tex` file. Understand:
- Existing sections and their order
- Current label namespace (grep for `[label=`)
- Appendix structure and sections
- Where new content logically fits

#### Step 2.3: Decide placement
- If the user specifies where → obey exactly.
- If the user says "hero" or "main" → body section.
- If the user says "appendix" or "robustness" → appendix.
- If the user gives a folder of analysis: put the most important in the body, all auxiliary/robustness in the appendix. If unclear which is most important, ask.
- If no guidance at all: pick the most impactful for the body, rest in appendix.

#### Step 2.4: Create the content

**Graphs**: `\includegraphics[width=0.7\textwidth]{absolute_path}`. Add source line. Use `clip, trim` if the graph has whitespace. For multiple related graphs, consider subfigures or two-column minipage layout.

**Tables**: If the table is a PDF/image, use `\includegraphics`. If raw data, build with `tabular` using `booktabs` (`\toprule`, `\midrule`, `\bottomrule`). Use `\scriptsize` or `\footnotesize` for dense tables.

**Model slides**: Follow the natural sequence of the model:
1. Model summary/overview slide (key mechanisms in 3-4 bullets)
2. Environment (geography, time, agents)
3. Each agent's problem in order of the model's logic (e.g., preferences → decisions → constraints)
4. The novel mechanism (the thing that makes this model special — highlight it)
5. Market clearing conditions
6. Equilibrium definition

Each slide: one concept, formatted math (`align*`), concise labels for assumptions. Not too many slides — keep it tight.

**Literature bullets**: Search `<REFERENCES_BIB>` for citekeys. If needed, search the web for the paper. Create concise bullets grouped by strand, with `\textcolor{Accent2}{$\to$ Key takeaway}` arrows. Do NOT make bullets verbose.

**Content/bullet slides**: Use the itemize pattern from the style guide. Wrap in minipage. If too packed, split across slides.

#### Step 2.5: Wire hyperlinks
For every new body slide with appendix counterparts:
1. Add `[label=newtopic_main]` to the body frame
2. Add `[label=newtopic_appendix]` to the appendix frame
3. Body slide gets: `\hfill \hyperlink{newtopic_appendix}{\beamerbutton{Descriptive Text}}`
4. Appendix slide gets: `\hfill \hyperlink{newtopic_main}{\beamerbutton{Back}}`

Create proper appendix subsection headers for the new content.

#### Step 2.6: Compile and audit
1. Compile the deck (see compilation protocol).
2. Run the **audit protocol** (see style guide → "Audit protocol") with the newly added/edited frames as the changed set. The protocol handles log parsing, PyMuPDF flags, density check, sub-agent visual review, and 3-round iteration with escalation.
3. Verify all new hyperlinks resolve (no "undefined reference" warnings for the new labels).
4. Report the audit summary (verdicts applied, frames escalated) as part of Step 2.7.

#### Step 2.7: Summary
Report: what was added, where (body vs. appendix), which buttons were wired, any issues found.

---

### Task 3: Fix

Diagnose and fix compilation errors or broken references.

#### Step 3.1: Read the error
If the user provides error output, parse it. If not:
1. Compile the deck with `pdflatex -interaction=nonstopmode`
2. Read the `.log` file, search for lines starting with `! ` (errors)
3. Identify the first error (LaTeX stops processing at the first fatal error in some modes)

#### Step 3.2: Diagnose
Do NOT do trial-and-error. Understand the root cause:

- **Wrong slide labels**: Grep for all `\hyperlink{X}` and `[label=X]` pairs. Find mismatches. Fix the reference to match the existing label, or add the missing label.

- **Changed citekeys**: Search `<REFERENCES_BIB>` for the author surname to find the current citekey. Common cause: the user updated a paper in Zotero from working paper to published version, changing the citekey.

- **Moved graph files**: Search the filesystem (cloud-storage directory, projects directories) for the filename. Update the path. Common locations:
  - `<CLOUD_STORAGE_DIR>`
  - `<PROJECTS_DIR>`

- **Stale auxiliary files**: If the error seems like corruption (e.g., aux file references that don't match the tex source), clean with `latexmk -c` and recompile from scratch.

- **Package conflicts or undefined control sequences**: Check if a package is missing from the preamble. Search the web for the specific error message if unfamiliar.

- **Bibliography errors**: Check `.blg` file for bibtex errors. Common: malformed bib entries, encoding issues in author names.

#### Step 3.3: Fix
Apply the minimal fix. Do not refactor or restructure unrelated content. If it's obvious (wrong citekey, wrong path, wrong label), fix it directly. If uncertain, flag to the user with your diagnosis.

#### Step 3.4: Compile and verify
Full compile cycle. Read the log. If errors remain, diagnose and fix the next one. Iterate: fix → compile → check → fix until 0 errors.

#### Step 3.5: Escalate if stuck
If stuck after genuine investigation (not trial-and-error), flag to the user:
- What was tried
- What the error means
- What information you need (e.g., "I can't find the graph file anywhere — did you move it?")

---

### Task 4: Check

Comprehensive review for an audience of top-5 journal editors.

#### Step 4.1: Read the full deck
Read the entire `.tex` file. Understand the narrative arc. If project notes exist (check working directory for `*.md` files, especially `notes.md`, `notes/README.md`), read those too.

#### Step 4.2: Pass 1 — English
- Fix typos and grammar errors
- Ensure text reads naturally
- Do NOT make bullets verbose — keep them concise
- Check consistency: capitalization in titles, bullet style, tense

#### Step 4.3: Pass 2 — Math
- Check all equations for correctness: matching subscripts, correct operators, consistent notation
- Cross-reference with project notes or model documentation if available
- Verify equation tags/labels match their content

#### Step 4.4: Pass 3 — Formatting and layout
- Compile the deck.
- Run the **audit protocol** with the **full frame set** as the changed set (a Check task audits every frame, not just edited ones; the 20-char diff gate does not apply here).
- The protocol handles overflow, density, log warnings, and sub-agent visual review with 3-round iteration and escalation. Record escalated frames for the final report.
- Additionally verify, independent of the audit protocol:
  - All empirical slides have source lines
  - `\setlength{\itemsep}` and `\vspace` are used consistently in all itemize environments
  - Section fillers use the correct pattern (centered, LARGE, Accent2)
  - Graph widths are consistent across similar slides

#### Step 4.5: Pass 4 — Hyperlinks and structure
- Verify every `\hyperlink{X}` has a matching `[label=X]`
- Verify every body slide with appendix content has a forward button
- Verify every appendix slide has a back button
- Check that sections are in logical order
- Check that appendix sections mirror body sections
- Verify TOC renders correctly

#### Step 4.6: Pass 5 — Editorial
This is the most important pass. Think like an AER editor reviewing a seminar presentation:
- Are the research questions clear from the first few slides?
- Does the evidence build logically toward the model/mechanism?
- Is any analysis missing that appears in project notes but not in the deck?
- Should any slides be reordered for better flow?
- Should any body slides move to the appendix (too detailed for main presentation)?
- Should any appendix slides move to the body (too important to hide)?
- Are section transitions smooth?
- Flag: "Your notes mention X analysis, but it's not in the deck. Consider adding it."
- Suggest: "Consider reordering sections Y and Z — the current flow assumes the audience knows..."

#### Step 4.7: Apply and report
- Passes 1-4 are mechanical: apply fixes directly
- Pass 5 is editorial: report suggestions to the user for approval, do not apply unilaterally
- Compile and verify after all fixes
- Present a summary: what was fixed, what is suggested

---

### Compilation protocol

Use this protocol after every structural change. Referenced by all tasks.

```
1. Primary: latexmk -pdf -interaction=nonstopmode <file>.tex
2. If latexmk unavailable or fails unexpectedly:
   a. pdflatex -interaction=nonstopmode <file>.tex
   b. bibtex <file>
   c. pdflatex -interaction=nonstopmode <file>.tex
   d. pdflatex -interaction=nonstopmode <file>.tex
3. If stale aux files suspected:
   a. latexmk -c  (clean auxiliary files)
   b. OR: rm <file>.aux <file>.nav <file>.snm <file>.toc <file>.out <file>.bbl <file>.blg
   c. Retry from step 1
4. After compile: read <file>.log
   - Search for "! " (errors) — must be 0
   - Search for "Overfull" (warnings) — fix if they cause visible problems
5. Iterate until 0 errors
```

---

### Important rules

- **Always read the template fresh** from `<SKILLS_DIR>/latex-slide/template.tex`. Never use a cached copy.
- **Never create symlinks** for bibliography. The template has the absolute path.
- **Never overwrite** an existing `.tex` file without confirmation.
- **Use `aer` bibliography style** (already in template).
- **Preserve preamble content** from the template. Only modify title, author, date, and document body.
- **Buttons always bottom-right**: `\hfill \hyperlink{...}{\beamerbutton{...}}`
- **No verbose slides.** Academic audience. Bullets guide, not narrate.
- **When in doubt about placement, prefer appendix.** Body slides are premium real estate.
- **Always use absolute paths** for graph files.
- **After every structural change, compile and verify.**
- **Do not do trial-and-error when fixing errors.** Understand the problem first, then fix.
- **Use subagents** to analyze graphs, explore project structure, or check references in parallel when the task involves multiple independent sub-tasks.
- **Zotero BibTeX**: The master bibliography is at `<REFERENCES_BIB>`. Citekeys follow the Better BibTeX pattern: `authorShorttitleYear` (e.g., `cardMinimumWagesEmployment1994`). When a citekey doesn't resolve, search this file by author surname.
