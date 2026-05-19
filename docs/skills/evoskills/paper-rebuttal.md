<!-- DO NOT EDIT — auto-copied from skills/evoskills/details/paper-rebuttal.md -->

# `paper-rebuttal`

Rebuttal pipeline for reviewer comments

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
name: paper-rebuttal
description: "Guides writing effective rebuttals after receiving peer review feedback. Covers review diagnosis (score-driven color-coding), response strategy (champion identification, common-theme consolidation), tactical writing (18 rules), and counterintuitive rebuttal principles. Use when: user received reviewer scores/comments, needs to write a rebuttal or author response, wants to respond to specific criticism (e.g. 'limited novelty', 'missing baselines'), mentions 'rebuttal', 'reviewer comments', 'author response', or 'respond to reviewers'. Do NOT use for pre-submission self-review (use paper-review instead)."
allowed-tools: "write_file edit_file read_file think_tool"
metadata:
  author: EvoScientist
  version: '1.0.0'
  tags: [core, writing, academic-writing, peer-review]
---

# Paper Rebuttal

A systematic approach to writing rebuttals after receiving peer review feedback. The goal is not to defend every point — it's to move scores by addressing the concerns that actually drive them.

## When to Use This Skill

- User received reviewer comments and needs to write a rebuttal
- User asks how to respond to specific reviewer criticism
- User wants to analyze reviews strategically before responding
- User mentions "rebuttal", "reviewer comments", "review feedback", "respond to reviewers"

> For pre-submission self-review and catching weaknesses before they become reviewer complaints, use the `paper-review` skill.

## Step 1: Diagnose Reviews

Before writing a single word, answer: **"Why did this reviewer give this exact score?"** Not what they wrote — what drove the score. Most researchers skip this and address every comment equally. That is a mistake.

### Score Diagnosis

For each reviewer, ask: "What would move this reviewer from their current score to acceptance?"

| Score Range | Typical Situation | Your Strategy |
|-------------|------------------|---------------|
| 7+ | Already your champion | Arm them with ammunition for the discussion phase |
| 5-6 | On the fence, 1-2 concerns holding them back | Identify and resolve those specific concerns |
| 3-4 | Fundamental objection | Determine if the objection is addressable; if not, focus elsewhere |

### Color-Code Every Comment

Read through each review and mark every comment:

| Color | Meaning | Action | Budget |
|-------|---------|--------|--------|
| **Red** | Score-driving concern — this is why the score is low | Address first, maximum effort and evidence | 60% |
| **Orange** | Addressable concern — can be resolved | Respond with concrete data or revision | 30% |
| **Gray** | Minor or cosmetic | Acknowledge briefly, confirm fix | 10% |
| **Green** | Positive comment or praise | Note as ammunition for your champion | — |

### Identify the Invisible Question

Behind every reviewer comment is an unspoken question. A comment like "The baselines are outdated" really asks: "Is this method actually competitive with current approaches?" Address the invisible question, not just the surface request.

## Step 2: Plan Response Strategy

### Categorize Every Concern

| Category | Response Strategy |
|----------|-----------------|
| **Misunderstanding** | Clarify with specific references to the paper; restate the key point |
| **Missing experiment** | Provide the experiment inline if feasible; otherwise explain constraints honestly |
| **Missing baseline** | Add comparison or explain precisely why the baseline is not applicable |
| **Writing clarity** | Acknowledge and provide revised text in the rebuttal |
| **Fundamental concern** | Address directly with technical arguments AND additional evidence |
| **Minor issue** | Thank the reviewer and confirm the fix |

### Identify Common Themes

If multiple reviewers raise the same concern, it's almost certainly a real weakness. Consolidate these into a "Common Response" section — this saves word count and demonstrates that you understand the pattern.

### Distinguish Actionable vs. Subjective

- **Actionable**: "Missing comparison with Method X" — you can do this
- **Subjective**: "The novelty is limited" — harder to address, but can be reframed with evidence

### The Champion Strategy

**Your rebuttal's real audience is not the negative reviewer — it's the positive one.**

Your champion argues on your behalf in the AC discussion, often using your exact words. Write your rebuttal to arm them:

1. Make key arguments **copy-pasteable** — your champion will quote you directly
2. Highlight where reviewers **agree with each other** — consensus strengthens the champion's position
3. Flag **contradictions between reviewers** — if R1 says "limited novelty" but R2 says "interesting approach," your champion can use this
4. Lead with **strengths before weaknesses** — remind the AC what your paper does well

See [references/rebuttal-tactics.md](references/rebuttal-tactics.md) for the full 18 tactical rules.

## Step 3: Write the Rebuttal

### Structure

1. **Opening**: One line thanking reviewers (keep it short)
2. **Common concerns**: Address issues raised by multiple reviewers first — these are highest priority
3. **Per-reviewer responses**: Address remaining concerns in priority order (red → orange → gray), NOT in the order the reviewer wrote them

### Per-Concern Format

For each concern, follow this three-part structure:

1. **Acknowledge**: Show you understand the concern (one sentence)
2. **Respond**: Provide your answer — evidence, clarification, new experiment results
3. **Action**: State what you changed in the revision (specific section/table/figure)

Use a fillable template at [assets/rebuttal-template.md](assets/rebuttal-template.md).

### The Neutral Third-Party Test

Before submitting, have someone who hasn't read your paper read only the reviews and your rebuttal. Ask: "Can you tell whether the concerns were addressed?" If not, rewrite.

## Counterintuitive Rebuttal Principles

1. **Submit a rebuttal even with extreme scores.** A paper with scores of 3/8/8 has better odds than you think. The negative reviewer may realize they are an outlier during discussion. But only if you submit a rebuttal — without one, the AC has nothing to work with.

2. **Concede something small, win something big.** Acknowledging a minor weakness ("We agree that Table 2 could include dataset X for completeness") makes your defense of major points more credible. Pure defense with zero concession reads as unobjective.

3. **One new experiment beats three paragraphs of explanation.** Reviewers are trained to be skeptical of arguments. They are not trained to be skeptical of data. A small new experiment that directly addresses a concern is worth more than any amount of reasoning.

4. **The best rebuttal is written before submission.** Draft responses to likely attacks while writing the paper ("prebuttal"). Two benefits: you often realize the attack is valid and fix the paper, and if the attack comes, you have a polished response ready.

5. **Don't defend every point equally.** Equal effort signals you don't know which points matter. Allocate your word budget according to the color-coding: 60% red, 30% orange, 10% gray. Reviewers notice when you nail the big issues.

## Common Reviewer Concerns

Prepare responses for these frequent concerns. Having a prepared response doesn't mean copying it verbatim — adapt to your specific paper and the reviewer's specific framing.

| Common Concern | Response Strategy |
|---------------|-------------------|
| "Limited novelty" | Articulate the specific insight; show what prior work cannot do; narrow and sharpen the claim |
| "Marginal improvement" | Emphasize other advantages (speed, generalizability, simplicity); add challenging test cases |
| "Missing ablations" | Provide the ablation table inline in the rebuttal |
| "Missing baselines" | Add the comparison or explain precisely why it's not applicable |
| "Not reproducible" | Add implementation details; commit to code release with a specific timeline |
| "Limited evaluation" | Add diverse datasets or metrics; if infeasible, explain resource constraints honestly |
| "No limitation discussed" | Add a limitation section in the revision; acknowledge this was an oversight |
| "Overclaimed results" | Weaken specific claims to match evidence; show the revised wording |
| "Unfair comparison" | Use standard evaluation protocols; add commonly reported baselines |
| "Method is engineering, not research" | Identify the scientific insight behind the design; explain why the choice is non-obvious |
| "Metrics don't match claims" | Align each claim with a specific metric; add the missing metric if feasible |
| "Related work incomplete" | Add the missing references; explain the relationship to your work |

> **Need to run new experiments for the rebuttal?** Use the `experiment-craft` skill for targeted debugging, or `experiment-pipeline` for a full new experiment stage.

## Handoff from Paper Review

This skill picks up where `paper-review` leaves off. If you used `paper-review` before submission, these artifacts are especially useful for rebuttal:

| Artifact from paper-review | How It Helps Rebuttal |
|---------------------------|----------------------|
| Reject-first simulation | You've already anticipated likely attacks |
| Claim-evidence audit table | Quickly verify whether a reviewer's concern about unsupported claims is valid |
| Prebuttal drafts (Phase 6) | Ready-made response templates for common criticisms |
| Trust scorecard | Identifies weaknesses you can proactively concede |

## Reference Navigation

| Topic | Reference File | When to Use |
|-------|---------------|-------------|
| 18 tactical rules | [rebuttal-tactics.md](references/rebuttal-tactics.md) | Detailed writing guidance for structure, content, tone |
| Rebuttal template | [rebuttal-template.md](assets/rebuttal-template.md) | Starting a new rebuttal document |


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/EvoScientist/EvoSkills/contents/skills/paper-rebuttal/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>EvoScientist/EvoSkills</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../evoskills.md">EvoSkills</a></dd>
<dt><b>Category</b></dt><dd><code>revision</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>revision-editing</code></dd>
<dt><b>License</b></dt><dd>Apache-2.0</dd>
<dt><b>Last update</b></dt><dd>2026-05-17</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/EvoScientist/EvoSkills">⭐ EvoScientist/EvoSkills</a><br><img src="https://img.shields.io/github/stars/EvoScientist/EvoSkills?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/EvoScientist/EvoSkills" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/evoskills/paper-rebuttal/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/evoskills.yml">edit on GitHub</a>.</p>
</div>

</div>
