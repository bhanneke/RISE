<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/qa-quarto.md -->

# `/qa-quarto`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/qa-quarto/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/qa-quarto/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/qa-quarto/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Adversarial Quarto vs Beamer QA Workflow

Compare Quarto HTML slides against their Beamer PDF benchmark using an iterative critic/fixer loop.

**Philosophy:** The Beamer PDF is the gold standard. The Quarto translation must be at least as good in every dimension.

---

### Workflow

```
Phase 0: Pre-flight → Phase 1: Critic audit → Phase 2: Fixer → Phase 3: Re-audit → Loop until APPROVED (max 5 rounds)
```

### Hard Gates (Non-Negotiable)

| Gate | Condition |
|------|-----------|
| **Overflow** | NO content cut off |
| **Plot Quality** | Interactive charts >= static plots |
| **Content Parity** | No missing slides/equations/text |
| **Visual Regression** | Quarto >= Beamer in all dimensions |
| **Slide Centering** | Content centered, no jumping |
| **Notation Fidelity** | All math verbatim from Beamer |

### Phase 0: Pre-flight

1. Locate Beamer (.tex/.pdf) and Quarto (.qmd/.html) files
2. Check freshness (re-render if QMD newer than HTML)
3. Verify TikZ SVGs if applicable

### Phase 1: Initial Audit

Launch the `quarto-critic` agent to compare Beamer vs Quarto comprehensively. Report saved to `quality_reports/[Lecture]_qa_critic_round1.md`.

### Phase 2: Fix Cycle

If not APPROVED, launch `quarto-fixer` agent to apply fixes (Critical → Major → Minor), re-render, and verify.

### Phase 3: Re-Audit

Re-launch critic to verify fixes. Loop back to Phase 2 if needed.

### Iteration Limits

Max 5 fix rounds. After that, escalate to user with remaining issues.

### Final Report

Save to `quality_reports/[Lecture]_qa_final.md` with hard gate status, iteration summary, and remaining issues.
