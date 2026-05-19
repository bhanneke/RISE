# Constructive Feedback Review — Best Practices

## Purpose

Transform raw feedback (which may be harsh, dismissive, or unconstructively negative) into a professional, constructive review. The output should be honest about weaknesses but always actionable, respectful, and oriented toward improvement. The goal: the author reads the review and knows exactly what to fix and feels motivated to do so.

---

## Core Principles

### 1. Separate the Work from the Person

- Critique the text, argument, or method — never the author.
- **Bad:** "The author clearly doesn't understand identification."
- **Good:** "The identification strategy would benefit from a more explicit discussion of the exclusion restriction."
- Use "the paper," "the argument," "the analysis" as subjects — not "you" or "the author."

### 2. Be Specific and Actionable

Every critique must include:
1. **What** the problem is (specific, with a reference to where in the text)
2. **Why** it matters (what goes wrong if it's not fixed)
3. **How** to fix it (a concrete suggestion)

- **Bad:** "The writing is unclear."
- **Good:** "Section 3.2, paragraph 2 conflates the treatment effect with the selection effect. Separating these into distinct paragraphs — first establishing the selection concern, then presenting the identification strategy that addresses it — would clarify the argument."

### 3. Lead with Strengths

- Always identify genuine strengths before discussing weaknesses.
- This is not empty praise — it signals what the author should preserve and build on.
- Even deeply flawed work has elements worth acknowledging: an interesting question, a novel data source, an ambitious scope.

### 4. Calibrate Tone to Severity

| Severity | Tone | Example opener |
|----------|------|----------------|
| Minor | Suggestion | "Consider rephrasing..." or "A small point:..." |
| Moderate | Recommendation | "I'd recommend strengthening..." or "This section would benefit from..." |
| Major | Clear statement | "A key concern is..." or "The central argument requires..." |
| Fundamental | Honest but respectful | "The paper's main contribution would be clearer if..." |

### 5. Frame Negatives as Opportunities

- **Negative framing:** "The literature review is superficial and misses major contributions."
- **Constructive framing:** "The literature review covers the core references. Engaging with [Author 2020] and [Author 2022] would strengthen the positioning, as these papers address closely related identification concerns."

### 6. Use the Sandwich Sparingly — Prefer Structured Feedback

The praise-criticism-praise sandwich can feel patronizing when overused. Instead, use a clear structure:

1. **Overall assessment** (1-2 sentences: what the work aims to do and how well it succeeds)
2. **Key strengths** (what works well and should be preserved)
3. **Major points** (substantive issues that affect the core argument, ordered by importance)
4. **Minor points** (specific, line-level improvements)
5. **Summary recommendation** (clear next step)

---

## Transforming Negative Input

When the source feedback is harshly negative, apply these transformations:

| Negative Input Pattern | Constructive Output |
|----------------------|-------------------|
| "This is wrong" | "This claim would benefit from additional support. Specifically, [evidence needed]." |
| "Makes no sense" | "The logic in this passage could be made more explicit. The link between [A] and [B] isn't immediately clear to the reader." |
| "Poorly written" | "The prose could be tightened in several places. For example, [specific passage] could be streamlined by [specific suggestion]." |
| "Waste of time" | "The paper tackles an interesting question but the current version doesn't yet deliver on its promise. The gap between the ambition and execution can be closed by [specific steps]." |
| "Obvious/trivial" | "The contribution would be stronger with a clearer articulation of what this adds beyond the existing literature, particularly relative to [closest existing work]." |
| "Cherry-picked results" | "The robustness of the findings would be strengthened by [additional specifications/samples]. Presenting results across multiple specifications would increase confidence in the main finding." |
| "I don't believe the results" | "The credibility of the estimates could be bolstered by [specific robustness checks]. Addressing potential concerns about [specific threat] would strengthen the paper significantly." |

---

## Tone Calibration Rules

- **Never use sarcasm.** It is destructive and unprofessional.
- **Never use absolute dismissals.** "This paper should not be published" becomes "The paper requires substantial revision before it is ready for publication. The key areas for revision are..."
- **Acknowledge difficulty.** "This is a difficult identification problem, and the paper makes a reasonable first attempt. To be more convincing, consider..."
- **Be direct, not harsh.** Vagueness is not kindness — the author needs to know what to fix.
- **Use conditional language for suggestions, declarative language for errors.** "You might consider adding..." (suggestion) vs. "Equation 3 contains an error: the summation index should run from 1 to N, not 0 to N." (factual correction)

---

## Review Output Format

```
## Overall Assessment
[1-2 sentences: what the work does and overall quality assessment]

## Strengths
- [Genuine strength 1]
- [Genuine strength 2]
- [Genuine strength 3]

## Major Points
1. [Most important issue]
   - What: [specific description]
   - Why it matters: [consequence if not addressed]
   - Suggestion: [concrete fix]

2. [Second most important issue]
   ...

## Minor Points
- [Page/section ref]: [specific suggestion]
- [Page/section ref]: [specific suggestion]

## Summary
[1-2 sentences: overall recommendation and encouragement]
```

---

## Common Rejection Patterns at Q1 Journals

Most reject votes at top journals stem from the same recurring issues. When reviewing, check for these systematically -- they are the difference between a revise-and-resubmit and a desk reject.

### 1. Contribution Is Not a Clear, Testable Sentence

The paper describes what it does ("we study X") rather than what it finds ("we show that X because Y, validated by Z"). If the contribution cannot be stated in one sentence with a subject, a verb, and a falsifiable claim, the paper is not ready.

**Constructive framing:** "The contribution would be sharper if stated as a single testable proposition. Currently, the reader finishes the introduction understanding the topic but not the specific claim being advanced."

### 2. Methods Do Not Support the Headline Claim

The paper's headline finding implies a scope or causal interpretation that the methods cannot deliver. Common variants: claiming causal effects from descriptive regressions, generalizing from a narrow sample without discussing external validity, or drawing mechanism conclusions from reduced-form evidence.

**Constructive framing:** "The empirical strategy credibly identifies [narrow thing], but the framing claims [broad thing]. Either narrow the claim to match the design, or add [specific additional evidence] to support the broader interpretation."

### 3. Unfair Benchmarking

Baselines are weak, conditions are mismatched, or comparisons are cherry-picked. Signs: comparing against outdated methods, using different data or evaluation metrics for different approaches, or omitting the most relevant competing method.

**Constructive framing:** "The comparison with [Baseline] would be more informative if both approaches were evaluated under matched conditions: same data split, same metrics, same time period. Adding [strongest competing approach] as a baseline would also strengthen the contribution claim."

### 4. Cosmetic Novelty

The paper introduces a new label or minor tweak to an existing mechanism but the underlying approach is essentially the same. The "novelty" is in naming, not in substance.

**Constructive framing:** "The paper would benefit from a more explicit discussion of how [proposed approach] differs mechanistically from [existing approach]. Currently, the distinction appears to be primarily terminological."

### 5. Uncertainty Is Ignored

No sensitivity analysis, no robustness checks, no error analysis. The paper presents point estimates as if they were certain. Signs: no alternative specifications, no discussion of what happens when key assumptions are relaxed, no acknowledgment of estimation uncertainty beyond standard errors.

**Constructive framing:** "The credibility of the main finding would increase substantially with sensitivity analysis on the top 2-3 assumptions. Specifically, [assumption X] drives the result -- what happens when it is relaxed?"

### 6. Key Assumptions Are Hidden or Under-Justified

The paper makes identifying assumptions but buries them in notation or never states them in plain language. The reader cannot assess whether the assumptions are plausible without reverse-engineering the formal setup.

**Constructive framing:** "The key identifying assumptions would benefit from being stated in plain language alongside the formal notation. Specifically, [assumption in equation N] implies [plain-language consequence] -- is this plausible in this setting?"

### 7. Logic Is Hard to Audit

The writing obscures what was actually done. Signs: methods described in a different order than they were executed, key decisions buried in footnotes, results that seem to come from nowhere, inconsistencies between text and tables.

**Constructive framing:** "The exposition could be made more auditable by [specific suggestion: e.g., reordering sections to match the actual analysis flow, moving footnote N into the main text, adding a paragraph linking the model prediction to the specific regression being estimated]."

---

### Summary: What Reviewers Reject

Reviewers do not reject effort. They reject unsupported certainty. A paper that is honest about its limitations, transparent about its assumptions, and precise about its claims will always fare better than one that oversells.
