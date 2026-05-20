<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/lit-review-assistant.md -->

# `lit-review-assistant`

Search, summarize, and synthesize economics literature.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code> · <code>literature-synthesis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/literature/lit-review-assistant/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/lit-review-assistant/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/literature/lit-review-assistant/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Literature Review Assistant

### Purpose

This skill helps economists conduct literature reviews by structuring searches, summarizing papers, and synthesizing findings. It provides templates for organizing literature and identifying research gaps.

### When to Use

- Starting a literature review for a new project
- Finding related work for a paper's introduction
- Synthesizing existing evidence on a topic
- Identifying gaps in the literature

### Instructions

#### Step 1: Define the Research Domain

Ask the user:
1. What is your specific research question?
2. What's the scope? (Narrow field survey vs. cross-disciplinary review)
3. What databases do you have access to? (JSTOR, EconLit, Google Scholar, NBER)
4. What time period is relevant?
5. Are there seminal papers to start from?

#### Step 2: Structure the Search

Help define search terms:
1. **Primary terms**: Core concepts (e.g., "minimum wage", "employment")
2. **Methodological filters**: (RCT, IV, difference-in-differences)
3. **Outcome terms**: What effects are measured
4. **Geographic/temporal scope**: If relevant

#### Step 3: Organize and Synthesize

Create a structured summary for each paper:
- Citation
- Research question
- Data and methods
- Key findings
- Limitations
- How it relates to user's project

#### Step 4: Identify Patterns and Gaps

- What do papers agree on?
- Where are disagreements?
- What questions remain unanswered?
- What methods haven't been applied?

### Example Output: Literature Summary Template

```markdown
## Literature Review: [TOPIC]

### Search Strategy

**Databases:** EconLit, NBER, Google Scholar, SSRN
**Date range:** 2010-2024
**Search terms:** 
- ("minimum wage" OR "wage floor") AND (employment OR jobs)
- ("minimum wage") AND ("difference-in-differences" OR "DiD")

**Inclusion criteria:**
- Peer-reviewed or NBER working papers
- Focused on [specific outcome]
- Uses causal identification strategy

---

### Seminal Papers

#### Card and Krueger (1994)
**Citation:** Card, D., & Krueger, A. B. (1994). Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania. *American Economic Review*, 84(4), 772-793.

**Research Question:** What is the effect of minimum wage increases on employment?

**Data & Method:** 
- DiD comparing NJ (treatment) to PA (control)
- Survey of fast-food restaurants before/after NJ minimum wage increase

**Key Findings:**
- No negative employment effect found
- Employment slightly increased in NJ relative to PA

**Contribution:** Challenged conventional view; pioneered quasi-experimental methods in labor economics

**Limitations:**
- Single state, short time horizon
- Potential survey response bias

---

#### Cengiz et al. (2019)
**Citation:** Cengiz, D., Dube, A., Lindner, A., & Zipperer, B. (2019). The Effect of Minimum Wages on Low-Wage Jobs. *Quarterly Journal of Economics*, 134(3), 1405-1454.

**Research Question:** Do minimum wage increases destroy jobs or compress the wage distribution?

**Data & Method:**
- Bunching estimator using 138 minimum wage events
- Examine employment distribution around minimum wage

**Key Findings:**
- Jobs below the new minimum wage disappear
- But replaced by jobs just above the minimum
- No significant overall employment loss

**Contribution:** Novel bunching methodology; large-scale evidence

---

### Synthesis: What We Know

| Finding | Evidence Quality | Consensus Level |
|---------|-----------------|-----------------|
| Small minimum wage increases have minimal employment effects | Strong (multiple RCTs/quasi-experiments) | High |
| Effects may be heterogeneous by region | Medium | Growing |
| Large increases (e.g., $15) less studied | Limited | Low |

### Research Gaps

1. **Mechanism:** How do firms absorb higher labor costs? (Prices, profits, productivity?)
2. **Long-run effects:** Most studies focus on 1-2 years
3. **Geographic heterogeneity:** Do effects differ in low vs. high cost-of-living areas?
4. **Spillovers:** Effects on workers earning above minimum wage

### Connection to Your Project

Your study of [SPECIFIC QUESTION] can contribute by:
- [How your work fills a gap]
- [What new data/method you bring]
```

### Paper Summary Template

```markdown
### [Author(s)] ([Year])

**Title:** [Full title]

**Published in:** [Journal/Working Paper Series]

**Research Question:** [One sentence]

**Data:**
- Source: [Dataset name]
- Period: [Years]
- Sample: [N observations, unit of analysis]

**Identification Strategy:** [Method in one sentence]

**Main Findings:**
1. [Key result 1 with magnitude]
2. [Key result 2]
3. [Robustness/heterogeneity]

**Limitations:**
- [Main concern 1]
- [Main concern 2]

**Relevance to your project:** [One sentence on how it connects]

**Key quote:** "[Most important direct quote]" (p. XX)
```

### Search Strategy Tips

#### Google Scholar Operators
- `"exact phrase"` - Exact matching
- `author:surname` - Papers by specific author
- `source:journal` - Papers in specific journal
- `-exclude` - Exclude terms
- `[year]..[year]` - Date range

#### Finding Seminal Papers
1. Check citations in recent survey papers
2. Look for papers with 1000+ citations
3. Check JEL codes in EconLit
4. Review "related articles" in Google Scholar

#### Building Citation Networks
1. Start with 2-3 seminal papers
2. Check what recent papers cite them (forward citations)
3. Check their references (backward citations)
4. Identify clusters of related work

### Best Practices

1. **Use reference managers** (Zotero, Mendeley, BibDesk)
2. **Create annotated bibliographies** as you read
3. **Track search queries** for reproducibility
4. **Update regularly** before submission
5. **Balance breadth and depth** - cover field but focus on closest work

### Common Pitfalls

- ❌ Only citing papers that support your argument
- ❌ Not engaging with contradictory findings
- ❌ Confusing correlation with causation when summarizing
- ❌ Citing papers you haven't actually read
- ❌ Missing important recent papers

### References

- [EconLit](https://www.aeaweb.org/econlit/) - Authoritative economics database
- [NBER Working Papers](https://www.nber.org/papers) - Latest research
- [IDEAS/RePEc](https://ideas.repec.org/) - Free economics papers
- [Connected Papers](https://www.connectedpapers.com/) - Visual citation networks

### Changelog

#### v1.0.0
- Initial release with templates and search strategies
