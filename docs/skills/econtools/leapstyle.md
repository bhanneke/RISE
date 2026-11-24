<!-- DO NOT EDIT — auto-copied from skills/econtools/details/leapstyle.md -->

# `/leapstyle`

Apply the LEAP Economics house style to LaTeX papers, Beamer presentations, R/ggplot2 figures, and academic prose.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../econtools/">EconTools</a></div><div><b>Category:</b> <code>editing</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT (stated in README; no licence file)</code></div><div><b>Updated:</b> 2026-09</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/johanfourieza/econtools/contents/.agents/skills/leapstyle/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/econtools/leapstyle/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/johanfourieza/econtools/blob/main/.agents/skills/leapstyle/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/johanfourieza/econtools?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## LEAP Style

Apply the LEAP house style for Johan Fourie's research group at Stellenbosch University. Preserve the user's intellectual content and existing unrelated changes.

This is the skill for shaping a paper while it is being written: how it is structured, how it looks, how it reads. The companion skill is `leapwp`, which turns a finished paper into a circulated working paper -- title footnote, acknowledgements, AI disclosure, cite-as line, `aea` bibliography, versioned filename, clean build, and the copy into `1Research\WorkingPapers\`. Nothing here writes a front page, versions a file or shelves anything.

### Select the mode

Interpret the first argument or the task context:

- `paper [file.tex]`: apply the article layout and structure in references/paper.md.
- `slides [file.tex]`: apply the Beamer template and presentation rules in references/slides.md.
- `graph [file.R]`: apply the ggplot2 identity in references/graph.md.
- `writing [file]`: apply the prose-editing rules in references/writing.md.
- A manuscript request with no explicit mode: apply both `paper` and `writing` where relevant.
- No target or mode: describe the four modes and give invocation examples; do not create files.

Read each selected reference completely before editing. Read only the references needed for the task.

### Core workflow

1. Inspect repository guidance, the target file, dependencies, build instructions and worktree state.
2. In `paper` mode, leave the front page alone. Keep `\title`, `\author` and `\date{}` bare, and do not draft a title footnote, an acknowledgement, an AI disclosure or a cite-as line. Those are written once, from the finished paper, by `leapwp`.
3. Identify the venue. Follow known venue rules before LEAP defaults. If the venue is unknown, apply LEAP defaults and flag the venue-dependent decisions.
4. Preserve custom LaTeX commands, bibliography paths, packages required by the body, data logic and figure semantics.
5. Do not version or rename in any mode. Edit the live target, or create a separate styled version when the user asks for a conversion or comparison. Versioned filenames belong to `leapwp`, which assigns one when the paper is packaged.
6. Apply the selected reference rules. Do not strengthen claims, invent facts or citations, or silently repair uncertain content.
7. When editing prose, record suspected argument, evidence, data or citation errors separately. Preserve the intended claim unless the repair is unambiguous; disclose any such repair.
8. Validate the output with the project's native tools. Compile LaTeX, run relevant R/model checks and inspect generated output where practical.
9. For meaning-preserving passes, compare the citation-key multiset, numerals, equations, theorem/proposition blocks, labels/references and important hedges with the source. Inspect every difference that can carry substance.
10. Report output paths, checks run, unresolved questions and any substantive concerns discovered.

### Shared palette

Use these colors across LEAP outputs:

| Role | Name | Hex |
|---|---|---|
| Primary data | plum | `#5C2346` |
| Secondary data | blue | `#3D8EB9` |
| Tertiary data | sage | `#6B8E5E` |
| Fourth/highlight | gold | `#D4A03E` |
| Extended | rose | `#A34466` |
| Extended | teal | `#45808B` |
| Extended | earth | `#8B6B3D` |
| Extended/light fill | mint | `#97C5B0` |
| Slide chrome and links only | maroon | `#7A0019` |
| Non-significant/reference | grey | `#AAAAAA` |

For color-blind accessibility, prefer plum, blue, gold and teal, supplemented by line types or shapes. Avoid relying on plum versus rose or sage versus earth alone.

### Invocation examples

Use explicit Codex skill syntax:

```text
$leapstyle paper paper.tex
$leapstyle slides seminar.tex
$leapstyle graph figures.R
$leapstyle writing manuscript.tex
```

Natural language also works when the skill is installed and discoverable: `Use leapstyle to edit manuscript.tex`.
