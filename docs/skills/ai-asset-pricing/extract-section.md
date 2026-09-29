<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/extract-section.md -->

# `/extract-section`

Pulls one section out of main.tex by its key so later skills can work on it in isolation.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/extract-section/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/extract-section/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/extract-section/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Extract Section Skill

Extract a specific section from `main.tex` for reading or editing.

### Examples
- `/extract-section introduction` -- extract the introduction
- `/extract-section data` -- extract the data section
- `/extract-section results` -- extract the results section
- `/extract-section internet-appendix` -- extract the full Internet Appendix

### Section Keys

Look up the project's section keys in its `CLAUDE.md` (under "LaTeX Section
Keys"). The boilerplate template ships with these default keys:

| Key | Section |
|-----|---------|
| `introduction` | Introduction |
| `data` | Data |
| `methodology` | Methodology |
| `results` | Results |
| `conclusion` | Conclusion |
| `appendix-a` | Appendix A |
| `internet-appendix` | Internet Appendix |

Projects may register additional keys in their `CLAUDE.md`.

### Workflow

1. Read `main.tex`
2. Find `%% BEGIN:<key>` and `%% END:<key>` markers
3. Extract all content between the markers (inclusive)
4. Return clean LaTeX with line numbers relative to main.tex

**Marker format**: Each section is delimited by `%% BEGIN:<key>` and `%% END:<key>` comment lines in `main.tex`. Use Grep to locate the markers, then Read to extract the content between them.

### Output

The raw LaTeX content of the requested section, with line numbers relative to main.tex.
