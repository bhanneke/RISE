<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-reference-check.md -->

# `reference-check`



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

# Reference Check

## Purpose

Validate that every citation in a research paper draft can be traced to a
concrete source — either in the project bibliography, the knowledge base, or
an external database (CrossRef). Flag missing references so they can be
retrieved before submission.

---

## What Makes Well-Cited Work

1. **Every empirical claim about prior work has a citation** — no "it is well
   known that..." without a reference.
2. **Citations match the reference list** — no orphan citations (cited but not
   in references) and no orphan references (in list but never cited).
3. **Author names and years are consistent** — "Smith (2020)" in the text
   matches "Smith, J. (2020)" in the reference list, not "Smith, J. (2019)".
4. **Key methodological choices cite their origin** — DiD cites the canonical
   reference, not just the applied paper that used it.
5. **Self-citations are proportionate** — a few are normal, more than 20% of
   references is a flag.

---

## Common Citation Issues

| Issue | Example | Severity |
|-------|---------|----------|
| Orphan citation | "Jones (2021)" in text, absent from references | Critical |
| Orphan reference | Entry in bibliography never cited in text | Major |
| Year mismatch | Text says "(2020)", bib entry says 2019 | Major |
| Author spelling | "Mackinlay" vs "MacKinlay" | Minor |
| Missing DOI | Reference has no DOI when one exists | **Major** |
| Incomplete entry | Missing journal name or volume | Minor |

---

## Resolution Strategy

When checking references, resolution proceeds in tiers:

1. **BibTeX match** — Does the citation match an entry in the project's
   bibliography.bib by citation key or author+year?
2. **Knowledge base search** — Does a semantic search of the KB return a
   matching paper?
3. **CrossRef lookup** — Can we discover a DOI via the CrossRef API using
   author + title + year?
4. **Google Scholar fallback** — Generate a search URL for manual retrieval.

A citation is "resolved" if any tier succeeds. Unresolved citations are flagged
for human retrieval.

---

## DOI Completeness Check

**Every resolved reference must have a DOI.** After resolving citations:

1. Check each BibTeX entry for a `doi` field.
2. For entries missing DOI, query CrossRef (`https://api.crossref.org/works?query.bibliographic=...`).
3. Flag every reference without a DOI as a **Major** issue.
4. Only exceptions: pre-DOI books (before ~2000), unpublished manuscripts, and
   datasets without assigned DOIs. These must have a `note` field explaining the absence.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/review/reference-check.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>review</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/review-reference-check/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
