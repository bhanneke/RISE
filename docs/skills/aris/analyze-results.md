<!-- DO NOT EDIT — auto-copied from skills/aris/details/analyze-results.md -->

# `analyze-results`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-11-24</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/analyze-results/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/analyze-results/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Analyze Experiment Results

Analyze: $ARGUMENTS

### Workflow

#### Step 1: Locate Results
Find all relevant JSON/CSV result files:
- Check `figures/`, `results/`, or project-specific output directories
- Parse JSON results into structured data

#### Step 2: Read the measurements in context
Identify the metric, units and run conditions. For comparisons, align the dataset and settings and show both values. Report a difference in the metric’s units (percentage points for rates). Use relative change when the baseline and metric make the ratio meaningful.

#### Step 3: Statistical Analysis
- If multiple seeds: report mean +/- std, check reproducibility
- If sweeping a parameter: identify trends (monotonic, U-shaped, plateau)
- Flag outliers or suspicious results

#### Step 4: Answer the research question
Lead with the measured result and identify the file or run it came from. Use a table when comparing configurations or seeds. Distinguish a measured trend from a proposed explanation. Suggest a follow-up experiment when it would resolve a question the data leaves open.

If the finding changes a conclusion in the project notes or experiment report, propose the corresponding update.
