<!-- DO NOT EDIT — auto-copied from skills/prose-revision/details/prose-revision.md -->

# `prose-revision-skill-ht-anthony-lee-zhang`

Revise draft prose by finding the best structure for the ideas already there — idea flow first, linguistic flow second; preserve voice and claim strength; distinct from proofreading.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../prose-revision/">Prose Revision (h/t Anthony Lee Zhang)</a></div><div><b>Category:</b> <code>editing</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Gabberflast/prose-revision-skill-ht-anthony-lee-zhang/contents/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/prose-revision/prose-revision/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Gabberflast/prose-revision-skill-ht-anthony-lee-zhang/blob/main/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Gabberflast/prose-revision-skill-ht-anthony-lee-zhang?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Prose Revision

### Default stance

Assume the user usually has the right set of ideas and wants help discovering the best structure for them. Revise aggressively at the level of order, emphasis, sentence boundaries, transitions, and paragraph shape, while preserving the substantive claims. The rule of thumb: aggressive on structure, conservative on content.

Flow operates at every level — sentence, paragraph, section, and whole — and the same discipline applies at each: get the ideas into the right order, and let each unit do one clear job, before smoothing the language inside it. The largest levels come first, because a paragraph that presupposes something established only later is an idea-flow problem that no sentence-level work can fix.

Before diagnosing structure, note the intended audience, the piece's purpose, and the desired tone, and preserve the author's voice and register. The goal is the author's ideas expressed more clearly, not a generic "clean" style imposed on top of them. When these are not stated, infer them from the text; ask only when the ambiguity is consequential and cannot be resolved from context.

Do not add or subtract ideas by default, and do not change their strength. Add a missing idea, remove an idea, or move an idea out of its unit only when it is clearly necessary for the unit to work — and when you do, make that intervention explicit. Preserve hedges and claim strength with the same care: do not turn "suggests" into "shows" or drop a load-bearing "may" for the sake of cleaner prose. Sharper wording must not quietly sharpen the claim.

If the draft is already clear and well-ordered, say so and make only minimal changes. Do not manufacture edits to look productive. "This already works; here are two small tightenings" is a valid response.

Treat an awkward sentence as evidence of a possible idea-flow problem, not merely a bad-English problem. A sentence is often awkward because it is trying to do two jobs at once, because the previous sentence did not prepare it, or because the unit's logical order is not yet right.

### Workflow

1. Read the target prose and enough surrounding context to understand the local argument.
2. For anything longer than a paragraph, check the larger structure first: the order of paragraphs and sections, and whether each unit sets up the next. Fix that before working inside individual paragraphs.
3. Identify each unit's intended job: the claim, contrast, mechanism, qualification, implication, or transition it needs to deliver.
4. Diagnose idea flow before wording. Look for ideas in the wrong order, overloaded sentences, missing connective tissue, premature qualifications, buried main claims, or a final sentence that belongs earlier.
5. If the idea structure is what prevents good flow, explain that structural problem first. Do not try to solve structural confusion with surface polish.
6. Rearrange and repack the existing ideas into a clearer logical sequence. Only then make the language smoother, cleaner, and more elegant.
7. Offer revised versions when alternatives genuinely help, distinguished by how much they restructure (see Output style). Keep explanations concise and focused on why the structure works.
8. If the user asks you to apply edits, edit the source file rather than a generated copy, and preserve notation, citations, labels, author notes, and technical claims unless the user explicitly asks to change them. For academic or technical prose, make an explicit pass to protect precise terminology, claim strength, and technical claims.

### What to improve

Prioritize changes that improve the reader's path through the ideas:

- Order the units so each one sets up the next, and put the main point where it can organize what follows.
- Split sentences that are doing multiple logical jobs; combine sentences when separation makes the logic choppy.
- Move qualifications after the claim they qualify, unless the qualification must come first for accuracy.
- Add transitions only after the underlying relation between ideas is clear.
- Replace vague connective language ("also," "moreover") with the actual logical relation: contrast, mechanism, implication, caveat, example, or consequence.
- Prefer precise, economical wording once the idea structure is sound.

### Output style

For short interactive requests, usually provide:

1. A brief diagnosis of what is limiting the flow.
2. One to three revised versions. When a single revision is clearly best, give just that one; when alternatives make a real tradeoff, offer two or three, distinguished by how much they restructure:
   - **Light** — same order, cleaner sentences.
   - **Moderate** — resequenced ideas, adjusted emphasis.
   - **Full** — unit rebuilt around the main claim.
3. A one-line note on the tradeoff, or on why a single version suffices.

For documents longer than about three pages, provide a structured revision report (diagnosis plus prioritized changes) unless the user asks for direct edits. Address the larger structure first, then work section by section, flagging the highest-leverage fixes first.

Keep line-level proofreading (typos, minor grammar) out of prose-revision responses unless it materially affects flow or clarity.

### Worked example

**Draft:**
"While it is important to note that the results are preliminary, and although the sample size was admittedly small, we found that the treatment group showed improvement, which was something we had hoped for, and this improvement was statistically significant."

**Diagnosis:** The main claim — a statistically significant improvement — is buried behind two qualifications and an aside about what the authors hoped for. The reader reaches the point only at the very end. The qualifications belong *after* the claim, and the aside is an idea that isn't doing a job.

**Revised** (one version suffices here — the fix is unambiguous):
"The treatment group showed a statistically significant improvement. This result is preliminary and rests on a small sample."

**Why it works:** The claim now leads and organizes the passage; the caveats follow as qualifications of a claim the reader already holds; and the aside is cut — an explicit removal, justified because it added no information the reader needed. The claim's strength is preserved exactly: "statistically significant improvement" is neither softened nor inflated.

The same diagnosis scales up: a claim buried at the end of a paragraph, or a paragraph placed before the one it depends on, is the same problem one level larger.
