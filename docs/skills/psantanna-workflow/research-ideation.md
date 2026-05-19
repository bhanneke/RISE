<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/research-ideation.md -->

# `/research-ideation`



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
name: research-ideation
description: Generate structured research questions, testable hypotheses, and candidate empirical strategies from a topic, phenomenon, or dataset description. Use when user says "give me research ideas on X", "brainstorm questions about Y", "what could I study with this data?", "I'm looking for a paper idea on...", "generate hypotheses for...". One-shot generation, not multi-turn. For idea-refinement use `/interview-me`.
argument-hint: "[topic, phenomenon, or dataset description] [--no-verify]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "WebSearch", "WebFetch", "Task"]
---

# Research Ideation

Generate structured research questions, testable hypotheses, and empirical strategies from a topic, phenomenon, or dataset.

**Input:** `$ARGUMENTS` — a topic (e.g., "minimum wage effects on employment"), a phenomenon (e.g., "why do firms cluster geographically?"), or a dataset description (e.g., "panel of US counties with pollution and health outcomes, 2000-2020").

---

## Steps

1. **Understand the input.** Read `$ARGUMENTS` and any referenced files. Check `master_supporting_docs/` for related papers. Check `.claude/rules/` for domain conventions.

2. **Generate 3-5 research questions** ordered from descriptive to causal:
   - **Descriptive:** What are the patterns? (e.g., "How has X evolved over time?")
   - **Correlational:** What factors are associated? (e.g., "Is X correlated with Y after controlling for Z?")
   - **Causal:** What is the effect? (e.g., "What is the causal effect of X on Y?")
   - **Mechanism:** Why does the effect exist? (e.g., "Through what channel does X affect Y?")
   - **Policy:** What are the implications? (e.g., "Would policy X improve outcome Y?")

3. **Tag each RQ with a likely paper type** (drawn from `methods-referee.md`):
   - `reduced-form` (DiD, IV, RD, event study, synthetic control)
   - `structural` (estimation of a fully-specified model)
   - `theory+empirics` (formal model + empirical test of its predictions)
   - `descriptive` (measurement, data construction, pattern documentation)
   - `formal-theory` (pure theory, no empirical test in this paper)
   - `survey-experiment` (vignette, conjoint, list-experiment)
   - `unsure` (when multiple types are plausible — the user can pick later via `/interview-me`)

   Use `.claude/references/discipline-cards.md` to bias the distribution by field (econ vs poli-sci default frequencies differ — e.g., poli-sci skews more toward `survey-experiment` and `formal-theory` than econ does).

4. **For each research question, develop:**
   - **Hypothesis:** A testable prediction with expected sign/magnitude
   - **Identification strategy:** How to establish causality (DiD, IV, RDD, synthetic control, etc.)
   - **Data requirements:** What data would be needed? Is it available?
   - **Key assumptions:** What must hold for the strategy to be valid?
   - **Potential pitfalls:** Common threats to identification
   - **Related literature:** 2-3 papers using similar approaches

5. **Rank the questions** by feasibility and contribution.

6. **Save the output** to `quality_reports/research_ideation_[sanitized_topic].md`

---

## Output Format

```markdown
# Research Ideation: [Topic]

**Date:** [YYYY-MM-DD]
**Input:** [Original input]

## Overview

[1-2 paragraphs situating the topic and why it matters]

## Research Questions

### RQ1: [Question] (Feasibility: High/Medium/Low)

**Type:** Descriptive / Correlational / Causal / Mechanism / Policy
**Paper type:** reduced-form / structural / theory+empirics / descriptive / formal-theory / survey-experiment / unsure

**Hypothesis:** [Testable prediction]

**Identification Strategy:**
- **Method:** [e.g., Difference-in-Differences]
- **Treatment:** [What varies and when]
- **Control group:** [Comparison units]
- **Key assumption:** [e.g., Parallel trends]

**Data Requirements:**
- [Dataset 1 — what it provides]
- [Dataset 2 — what it provides]

**Potential Pitfalls:**
1. [Threat 1 and possible mitigation]
2. [Threat 2 and possible mitigation]

**Related Work:** [Author (Year)], [Author (Year)]

---

[Repeat for RQ2-RQ5]

## Ranking

| RQ | Feasibility | Contribution | Priority |
|----|-------------|-------------|----------|
| 1  | High        | Medium      | ...      |
| 2  | Medium      | High        | ...      |

## Suggested Next Steps

1. [Most promising direction and immediate action]
2. [Data to obtain]
3. [Literature to review deeper]
```

---

## Post-Flight Verification (mandatory, CoVe)

Before returning the ideation report, run the Post-Flight Verification protocol from [`.claude/rules/post-flight-verification.md`](../../rules/post-flight-verification.md). Research ideation is hallucination-prone in three specific ways:

1. **Negative-literature claims** — "no prior work studies X" is frequently wrong.
2. **Dataset structure claims** — "The CPS contains field `educ_attain`" can be confidently wrong about variable names, coverage years, or restricted-access status.
3. **Estimator feasibility claims** — "this works with panel fixed effects" can misstate an identification assumption.

### Steps

1. **Extract claims** from the draft ideation report: each negative-literature claim, each named dataset with attributed fields, each claimed identification strategy + required data structure.
2. **Generate verification questions** per claim. Example: "Has Card & Krueger, Autor, or anyone in the last 10 years studied X? Search Google Scholar + NBER working papers." / "Does IPUMS-CPS include the `educ_attain` variable 1990–2024?"
3. **Spawn `claim-verifier`** via `Task` with `subagent_type=claim-verifier` and `context=fork`. Hand it claims + questions + source pointers (WebSearch allowed, NBER/SSRN URLs preferred, dataset codebooks preferred). Do NOT include the draft.
4. **Reconcile:** PASS → attach green block; PARTIAL → mark uncertain RQs with flags; FAIL → rewrite the affected RQ/hypothesis/strategy.

### Skip conditions

- `--no-verify` flag
- User explicitly says "I'll verify the literature myself"

---

## Principles

- **Be creative but grounded.** Push beyond obvious questions, but every suggestion must be empirically feasible.
- **Think like a referee.** For each causal question, immediately identify the identification challenge.
- **Consider data availability.** A brilliant question with no available data is not actionable.
- **Suggest specific datasets** where possible (FRED, Census, PSID, administrative data, etc.).


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/research-ideation/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>ideation</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>rq-formulation</code> <code>hypothesis-generation</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/research-ideation/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/research-ideation/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
