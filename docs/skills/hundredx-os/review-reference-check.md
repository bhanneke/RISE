<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-reference-check.md -->

# `reference-check`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/review/reference-check.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Reference Check

### Purpose

Validate that every citation in a research paper draft can be traced to a
concrete source — either in the project bibliography, the knowledge base, or
an external database (CrossRef). Flag missing references so they can be
retrieved before submission.

---

### What Makes Well-Cited Work

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

### Common Citation Issues

| Issue | Example | Severity |
|-------|---------|----------|
| Orphan citation | "Jones (2021)" in text, absent from references | Critical |
| Orphan reference | Entry in bibliography never cited in text | Major |
| Year mismatch | Text says "(2020)", bib entry says 2019 | Major |
| Author spelling | "Mackinlay" vs "MacKinlay" | Minor |
| Missing DOI | Reference has no DOI when one exists | **Major** |
| Incomplete entry | Missing journal name or volume | Minor |

---

### Resolution Strategy

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

### DOI Completeness Check

**Every resolved reference must have a DOI.** After resolving citations:

1. Check each BibTeX entry for a `doi` field.
2. For entries missing DOI, query CrossRef (`https://api.crossref.org/works?query.bibliographic=...`).
3. Flag every reference without a DOI as a **Major** issue.
4. Only exceptions: pre-DOI books (before ~2000), unpublished manuscripts, and
   datasets without assigned DOIs. These must have a `note` field explaining the absence.
