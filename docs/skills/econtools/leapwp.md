<!-- DO NOT EDIT — auto-copied from skills/econtools/details/leapwp.md -->

# `/leapwp`

Turn a finished paper into a LEAP working paper and file it on the shelf.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../econtools/">EconTools</a></div><div><b>Category:</b> <code>submission</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT (stated in README; no licence file)</code></div><div><b>Updated:</b> 2026-09</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/johanfourieza/econtools/contents/.agents/skills/leapwp/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/econtools/leapwp/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/johanfourieza/econtools/blob/main/.agents/skills/leapwp/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/johanfourieza/econtools?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## LEAP Working Paper

Take a finished paper and make it circulable: front matter, disclosure, citation,
versioned filename, clean build, shelf copy. This is the last step in a project,
not the first.

The companion skill is `leapstyle`, which shapes the paper while it is being
written. Load `leapstyle` when the question is *how should this paper read*. Load
this skill when the question is *how does this paper get posted*. This skill does
not rewrite prose or restructure a paper; if that is needed, it happens first,
under `leapstyle`.

### Read this first

Read references/package.md completely before writing
anything. It carries the whole procedure: the ten steps, the templates, the
naming scheme and the checklist.

### Core workflow

1. Locate the source manuscript and read it end to end. In a journal submission
   folder, expect the front matter to have been stripped into a separate title
   page file; harvest it rather than asking the user to retype it.
2. Run the front matter intake: co-authors, acknowledgements, AI tools used. Ask
   only about what the paper and its title page do not already carry, and never
   invent any of the three. A declaration the manuscript already makes beats the
   current config.
3. Copy the source to a new versioned filename and edit the copy. Never write over
   the file that was read.
4. Fit the preamble, title footnote, author block and title page.
5. Install `assets/aea.bst` beside the `.tex`, set `\bibliographystyle{aea}`, and
   audit the `.bib` for full given names. Resolve against sources, never from
   memory; unresolved entries are reported, not guessed, and do not hold the
   build.
6. Build with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`. The build must be
   clean: no undefined citations, no undefined references, no stale-label warning.
7. Read pages 1 and 2 of the compiled PDF, and one page of the reference list.
   Verify the front page from the PDF, not from the source.
8. Copy the PDF to `C:\Users\johanf\Dropbox\0Claude0\1Research\WorkingPapers\`,
   moving any superseded version of the same stem into `archive\`. Never
   overwrite, never delete.
9. Report the source path, the shelf path, anything archived, what was decided on
   the author's behalf, and every open question.

### Invocation examples

```text
$leapwp paper.tex
$leapwp path/to/project/folder
```

Natural language also works when the skill is installed and discoverable: `Use
leapwp to turn this into a working paper`, `put this on the working paper shelf`.
