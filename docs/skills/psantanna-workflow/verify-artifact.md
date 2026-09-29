<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/verify-artifact.md -->

# `/verify-artifact`

Proves a file about to be sent or published is the intended one: rebuild from source, integrity check, diff against source, and recipient echo-back.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-08-21</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/verify-artifact/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/verify-artifact/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/verify-artifact/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Verify the artifact before it leaves

A review is only as good as the thing reviewed. If the artifact is corrupt, truncated, stale, or silently renumbered, a competent reviewer will return confident findings about defects **that do not exist in your work** — and you will spend a cycle chasing them. This is cheap to prevent and expensive to miss.

**Rule: never send a derived artifact you have not diffed against its source.**

### 1. Rebuild from source, in one shell invocation

Never send yesterday's build. Rebuild, then copy to the send location in the *same* command, so nothing can change underneath you.

Cloud-synced folders (Dropbox/iCloud/OneDrive) **dehydrate files**: a PDF can become 0 bytes or a partial copy between building and reading it. Symptoms: `Syntax Error: Couldn't find trailer dictionary`, a 70 KB file that should be 700 KB. Build-tool "up to date" messages are *not* evidence the file is intact — the tool checks timestamps, not content. Always stage to a local (non-synced) directory and verify there.

### 2. Integrity checks (mechanical, fast, non-negotiable)

- **Size and structure**: byte size in the expected range; page/record/row count as expected.
- **It parses**: open it with a real reader (`pdfinfo`, `pdftotext`, a JSON/CSV parser, `unzip -t`). A file that exists is not a file that works.
- **Sample the content**: first and last page/record actually contain what you expect — truncation shows up at the end.
- **Unresolved markers**: for documents, count `??`, `[cite]`, `TODO`, `XXX`, `\ref{` leftovers, "Chapter ??"; for code/data, NaNs, empty cells, placeholder values.

### 3. Diff the derived artifact against its source

This is the step people skip and the one that pays. If you produced the artifact by transforming, excerpting, compressing, or subsetting, then **enumerate what could have been lost** and check it:

- **Labels/anchors/IDs**: set of identifiers in source vs artifact. Anything defined in source and *referenced but missing* in the artifact is a break.
- **Numbering**: removing a numbered object silently renumbers everything after it, so a citation that was "Lemma 10" becomes "Lemma 6" — every downstream reference now points somewhere plausible and wrong. Check numbering stability, not just presence.
- **Counts**: sections, tables, figures, rows, functions, endpoints — before vs after.
- **Nested content**: excerpting a block can remove *statements* nested inside it, not just the prose you meant to cut.

If you cut anything, leave a visible in-artifact note saying so, so a reviewer does not read an omission as a gap.

### 4. Make the recipient prove what they got

Ask the reviewer (human or model) to **state, at the top of their response, the exact filenames, page/record counts, and version they are reviewing**. This catches stale caches, wrong attachments, and silent fallbacks to an older upload — failures that are otherwise invisible until the findings make no sense.

Use unique filenames per round (`report_r6.pdf`, not `report.pdf`). Repeated identical names invite the recipient's system to serve a cached earlier copy.

### 5. If findings look strange, suspect the artifact first

Before acting on a review, ask: could this finding be an artifact of what I sent? Signals: complaints about missing/undefined references, "sections appear truncated", "the proof ends mid-argument", numbering that does not match your copy, or objections to text you know is present. **Re-verify the artifact before you re-verify the work.** Applying "fixes" for artifact-induced findings actively damages correct material.

### Minimum checklist

1. Rebuild from source; stage to a local dir in the same shell command.
2. Verify it parses; check size, counts, first/last content.
3. Count unresolved markers — expect zero.
4. Diff identifiers/numbering/counts against source; note any deliberate omissions in the artifact itself.
5. Unique filename for this round.
6. Require the recipient to echo filename + counts.

### Cross-references

- `verification-ladder.md` — rung 2 (existence → substantiveness → wiring → coherence)
- `external-oracle-process.md` §7 — cloud-synced files upload corrupt
