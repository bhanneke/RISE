<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/lit-review.md -->

# `/lit-review`



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
name: lit-review
description: Structured literature search + synthesis with citation extraction, thematic clustering, and gap identification. Use when user says "find papers on X", "do a lit review", "what's the literature on...", "summarize what we know about...", "where's the gap in this field", "review recent work on Y". Produces a written review with BibTeX-ready citations. Uses WebSearch/WebFetch for recent work.
argument-hint: "[topic, paper title, or research question] [--no-verify]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "WebSearch", "WebFetch", "Task"]
---

# Literature Review

Conduct a structured literature search and synthesis on the given topic.

**Input:** `$ARGUMENTS` — a topic, paper title, research question, or phenomenon to investigate.

---

## Steps

1. **Parse the topic** from `$ARGUMENTS`. If a specific paper is named, use it as the anchor.

2. **Search for related work** using available tools:
   - Check `master_supporting_docs/supporting_papers/` for uploaded papers
   - Use `WebSearch` to find recent publications (if available)
   - Use `WebFetch` to access working paper repositories (if available)
   - Read any existing `.bib` file for papers already in the project

3. **Organize findings** into these categories:
   - **Theoretical contributions** — models, frameworks, mechanisms
   - **Empirical findings** — key results, effect sizes, data sources
   - **Methodological innovations** — new estimators, identification strategies, inference methods
   - **Open debates** — unresolved disagreements in the literature

4. **Identify gaps and opportunities:**
   - What questions remain unanswered?
   - What data or methods could address them?
   - Where do findings conflict?

5. **Extract citations** in BibTeX format for all papers discussed.

6. **Save the report** to `quality_reports/lit_review_[sanitized_topic].md`

---

## Output Format

```markdown
# Literature Review: [Topic]

**Date:** [YYYY-MM-DD]
**Query:** [Original query from user]

## Summary

[2-3 paragraph overview of the state of the literature]

## Key Papers

### [Author (Year)] — [Short Title]
- **Main contribution:** [1-2 sentences]
- **Method:** [Identification strategy / data]
- **Key finding:** [Result with effect size if available]
- **Relevance:** [Why it matters for our research]

[Repeat for 5-15 papers, ordered by relevance]

## Thematic Organization

### Theoretical Contributions
[Grouped discussion]

### Empirical Findings
[Grouped discussion with comparison across studies]

### Methodological Innovations
[Methods relevant to the topic]

## Gaps and Opportunities

1. [Gap 1 — what's missing and why it matters]
2. [Gap 2]
3. [Gap 3]

## Suggested Next Steps

- [Concrete actions: papers to read, data to obtain, methods to consider]

## BibTeX Entries

```bibtex
@article{...}
```
```

---

## Post-Flight Verification (mandatory, CoVe)

Before returning the draft literature review to the user, run the Post-Flight Verification protocol from [`.claude/rules/post-flight-verification.md`](../../rules/post-flight-verification.md). Literature reviews are **very high** hallucination risk because WebSearch can return plausible-sounding fabricated citations. CoVe catches this architecturally.

### Steps

1. **Extract claims** from the draft. Each cited paper, each paraphrased finding ("Smith 2019 shows X"), each negative-literature assertion ("no prior work studies Y") is a claim.
2. **Generate verification questions** per claim. Specific ones: "Does Smith (2019, *JEL*) Section 3 actually report the finding that X implies Y? Is the venue correct?"
3. **Spawn `claim-verifier`** via `Task` with `subagent_type=claim-verifier` and `context=fork`. Pass: the claims table, the verification questions, the source-material pointers (paper URLs, DOIs, `master_supporting_docs/` paths). **Do NOT pass the draft text itself** — the fresh-context independence is what makes CoVe work.
4. **Reconcile:** if the verifier reports PASS, attach a green Post-Flight block to the output. If PARTIAL, mark the unverifiable claims with uncertainty flags in the BibTeX block. If FAIL, **remove or rewrite the contradicted citations** using the verifier's evidence before returning.

### Skip conditions

- `--no-verify` flag — user opts out for speed.
- User hands you ≤3 papers they already have read and confirmed; CoVe is overhead for content they've personally verified.

### Output contract

Append a Post-Flight block to the report (collapsed by default). See rule doc for the format.

---

## Important

- **Be honest about uncertainty.** If you cannot verify a citation, say so.
- **Prioritize recent work** (last 5-10 years) unless seminal papers are older.
- **Note working papers vs published papers** — working papers may change.
- **Do NOT fabricate citations.** If you're unsure about a paper's details, flag it for the user to verify. Post-Flight Verification catches most fabrications automatically; this rule is the backup.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/lit-review/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>literature</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>literature-discovery</code> <code>literature-synthesis</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/lit-review/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/lit-review/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
