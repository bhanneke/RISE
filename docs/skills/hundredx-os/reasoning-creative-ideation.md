<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/reasoning-creative-ideation.md -->

# `creative-ideation`



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

# Creative Research Ideation

## The Goal

Generate novel, feasible research ideas that a top economist would find worth pursuing. The best ideas start with a real-world phenomenon that demands explanation, not with a gap in the literature.

## The Three-Filter Framework

Every research idea must pass three filters before it is worth pursuing:

### Filter 1: Is it a real phenomenon?
- Does something surprising, consequential, or puzzling happen in the world?
- Can you state it in one sentence without referencing any academic paper?
- Would a smart non-economist find it interesting or counterintuitive?
- Is the phenomenon specific enough to study in one paper?

**Bad**: "No one has studied how DeFi affects price discovery" (literature gap, not phenomenon)
**Good**: "DEX prices lead CEX prices for small-cap tokens, but lag for large-cap — why?" (observable pattern that demands explanation)

### Filter 2: Is there a credible identification strategy?
- Can you identify a causal channel, or is this purely descriptive?
- Is there a natural experiment, instrument, or sharp design?
- What is the key identifying assumption, and is it defensible?
- Does the data exist (or can it be constructed) to implement this design?

**Sources of identification in crypto/DeFi:**
- Protocol governance votes that change parameters (DiD)
- Regulatory shocks with clear timing (event study)
- Threshold-based rules in smart contracts (RDD)
- Geographic variation in regulation (cross-country DiD)
- Token airdrops as exogenous wealth shocks
- Gas price spikes as exogenous transaction cost variation
- Bridge exploits/hacks as exogenous liquidity shocks

### Filter 3: Does the answer matter?
- Who would change their behavior based on the answer?
- Does it inform policy (regulation, protocol design, risk management)?
- Does it test or extend economic theory in a meaningful way?
- Would a finance or economics journal care, or is this only interesting to crypto insiders?

## Idea Generation Process

### Step 1: Start with phenomena, not methods
List 5-10 things that happen in the domain that are surprising, consequential, or unexplained. Do not think about methods yet.

### Step 2: For each phenomenon, ask "why?"
- What economic mechanism could explain this?
- What existing theory predicts the opposite? (tension = paper)
- What would have to be true for this to happen? (testable implications)

### Step 3: For each "why," identify the data
- What variation in the data would let you test the mechanism?
- Is there a natural experiment or quasi-random variation?
- Can you construct the key variables from available data?

### Step 4: For each viable idea, position it
- What are the 3 closest existing papers?
- How does this idea differ from each?
- Which journal would this target?

### Step 5: Rank by feasibility × impact
Score each idea on:
- **Data availability** (1-5): Can you get the data without heroic effort?
- **Identification credibility** (1-5): How clean is the causal design?
- **Novelty** (1-5): How far is this from existing work?
- **Importance** (1-5): How much would the answer matter?
- **Feasibility** (1-5): Can one person do this in 3-6 months?

Total = Data × min(Identification, Novelty) × Importance × Feasibility

## Patterns That Generate Good Ideas

### Theory meets new data
"Classic theory X predicts Y, but we've never been able to test it because Z data didn't exist. Now blockchain/DeFi/new-data-source provides exactly the variation we need."

### Mechanism design meets reality
"Protocol designers chose mechanism X. Theory predicts consequence Y. Does it happen? What are the unintended consequences?"

### Traditional finance in a new setting
"Phenomenon X is well-documented in equity markets. Does it also occur in DeFi, where frictions/institutions/information structure differ? What does the comparison reveal about the mechanism?"

### Regulatory arbitrage as identification
"Regulation X applies in jurisdiction A but not B. Comparing outcomes across jurisdictions identifies the causal effect of the regulation."

### Design discontinuities
"Smart contracts create sharp thresholds (liquidation ratios, fee tiers, governance quorums). These are natural RDD setups."

## Anti-Patterns to Avoid

- **"First to study X"**: Being first is not a contribution. What do we learn?
- **"We use fancy method Y"**: Methods serve questions, not the other way around.
- **"Crypto is important because market cap"**: Importance of the setting ≠ importance of the question.
- **"We build a dashboard/index/tool"**: Engineering is not research unless it generates new economic insight.
- **"Everything is correlated with Bitcoin"**: Correlation is not identification. What is the mechanism? What is the counterfactual?
- **Literature gap as motivation**: "No one has studied X" is an observation, not a reason. "X happens and we don't understand why" is a reason.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/reasoning/creative-ideation.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>audit</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/reasoning-creative-ideation/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
