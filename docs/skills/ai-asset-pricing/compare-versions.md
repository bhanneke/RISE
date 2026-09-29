<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/compare-versions.md -->

# `/compare-versions`

Shows the diff between current and proposed text together with the reason for each change.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>editing</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/compare-versions/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/compare-versions/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/compare-versions/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Compare Versions Skill

Show a side-by-side comparison of old vs. new text after an edit, with rationale for each change.

### Examples
- `/compare-versions` -- compare after the most recent edit
- `/compare-versions introduction` -- compare current vs. proposed introduction text

### Workflow

1. Identify the two text versions (before and after edit)
2. Align paragraphs between versions
3. For each changed paragraph, show:
   - **Before**: The original text
   - **After**: The revised text
   - **Why**: Category of change (banned word, terminology, voice, precision, concision, restructure)
4. Summarize total changes by category

### Output Format

```
COMPARISON: [section name]
==========================

CHANGE 1 [Banned word]:
  Before: "...we utilize a comprehensive set of..."
  After:  "...we use a thorough set of..."

CHANGE 2 [Terminology]:
  Before: "...microstructure noise affects..."
  After:  "...measurement error affects..."

[etc.]

SUMMARY:
- Banned words fixed: N
- Terminology corrections: N
- Voice improvements: N
- Precision additions: N
- Concision cuts: N
- Total changes: N
```
