<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/submit.md -->

# `submit`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../clo-author/">Clo-Author skills</a></div><div><b>Category:</b> <code>submission</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>none declared</code></div><div><b>Updated:</b> 2026-05-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/submit/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/clo-author/submit/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hugosantanna/clo-author" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Submit

Submission pipeline with four modes covering journal selection through final verification.

**Input:** `$ARGUMENTS` — mode keyword, optionally followed by journal name.

---

### Modes

#### `/submit target` — Journal Targeting
Get ranked journal recommendations.

**Agent:** Orchestrator (journal selection function)

Considers: contribution fit, methodology fit, audience fit, recent publications, desk rejection risk. Consults .claude/references/domain-profile.md for journal tiers.

Output: Ranked list of 3 target journals with rationale.
Save to `quality_reports/journal_recommendations_[date].md`

#### `/submit package` — Build Replication Package
Assemble AEA-compliant replication package.

**Agents:** Coder + Verifier

Produces:
- Master script that runs all analyses end-to-end
- README with data sources, computational requirements, instructions
- Data documentation and codebook
- Organized file structure per AEA standards
Save to `paper/replication/`

#### `/submit audit` — Audit Replication Package
Verify replication package completeness.

**Agent:** Verifier (submission mode — 10 checks)

Checks:
1. Master script exists and runs
2. All tables reproduce
3. All figures reproduce
4. README complete
5. Data documentation present
6. Numbered script order
7. Dependencies listed
8. Runtime documented
9. Output paths match paper references
10. No hardcoded paths

#### `/submit final [journal]` — Final Submission Gate
Full verification + score enforcement + submission checklist.

Workflow:
1. Run comprehensive review if not done recently
2. Run replication audit
3. Check score gate: aggregate >= 95, all components >= 80
4. Save gate summary to `quality_reports/quality_gate_[date].md`
5. Generate HTML quality gate report and refresh dashboard:
```bash
python3 scripts/generate_html_report.py quality-gate quality_reports/quality_gate_[date].md
python3 scripts/generate_dashboard.py
```
6. If PASS: generate cover letter draft + submission checklist
7. If FAIL: list blocking issues and stop

---

### Bundled Resources (Level 3)

| Resource | Path | When |
|----------|------|------|
| Submission checklist | `templates/submission-checklist.md` | `/submit final` — pre-submission verification |
| Cover letter | `templates/cover-letter.tex` | `/submit final` — draft cover letter |
| Replication README | `templates/replication-readme.md` | `/submit package` — AEA-compliant README |
| Audit checklist | `templates/audit-10-checks.md` | `/submit audit` — verifier submission mode |
| Gotchas | `gotchas.md` | Always — known failure points |

---

### Principles
- **Score >= 95 + all components >= 80. No exceptions.**
- **Don't skip verification.** Even if reports exist, check they're recent.
- **If it fails, stop.** Don't generate materials for a failing paper.
- **Cover letter is a draft.** User must review before sending.
