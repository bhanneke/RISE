<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-conference-submission.md -->

# `conference-submission`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/review/conference-submission.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Conference Submission Checklist

### HumanxAI Finance Conference Requirements

#### Submission Materials
1. **Extended abstract or full paper** (PDF format)
2. **AI workflow description**: Document how AI tools were used in the research process
3. **LaTeX source files** (if full paper)

#### Extended Abstract Requirements (if submitting abstract)
- 2-4 pages, single-spaced
- Must include: research question, contribution, method, preliminary results
- References do not count toward page limit
- Use standard academic formatting (12pt, reasonable margins)

#### Full Paper Requirements (if submitting paper)
- Standard academic paper format
- No strict page limit, but conciseness is valued
- Must include all standard sections: introduction, literature, data, method, results, conclusion
- Tables and figures should be publication-quality

#### AI Workflow Documentation
The conference specifically values transparency about AI use. Document:
- Which AI tools were used (Claude Code, etc.)
- What tasks were delegated to AI (literature search, code generation, writing assistance, etc.)
- How human judgment directed and validated AI outputs
- Quality control measures (human review cycles, verification steps)
- What the human researcher contributed vs. what AI contributed

This is a feature, not a bug — the conference celebrates human-AI collaboration. Be specific and honest.

### Pre-Submission Checklist

#### Content Quality
- [ ] Research question is clearly stated in the first paragraph
- [ ] Contribution is articulated in 1-2 sentences
- [ ] Identification strategy is explicit and defended
- [ ] Results are presented with appropriate uncertainty (confidence intervals, standard errors)
- [ ] Economic magnitude is discussed, not just statistical significance
- [ ] Limitations are acknowledged honestly
- [ ] Literature positioning covers the 3-5 closest prior papers

#### Data & Methods
- [ ] Data sources are documented (reproducibility)
- [ ] Sample construction is transparent (inclusions, exclusions, time period)
- [ ] Summary statistics table is complete (N, mean, SD, min, max)
- [ ] Estimation method matches the research question
- [ ] Standard errors are clustered/robust as appropriate
- [ ] At least one robustness check per major identification threat

#### Writing Quality
- [ ] Introduction accomplishes all 5 tasks (question, gap, method, results, roadmap)
- [ ] No filler phrases or hedging ("it is important to note that...")
- [ ] Active voice throughout
- [ ] Every table and figure is discussed in the text
- [ ] Consistent notation and terminology
- [ ] Abstract is self-contained and informative (question, method, finding)

#### Formatting
- [ ] PDF compiles without errors
- [ ] All figures are vector graphics or high-resolution (300+ DPI)
- [ ] Tables are properly formatted (no vertical lines, minimal horizontal rules)
- [ ] References are complete (no "et al." in reference list, only in citations)
- [ ] Page numbers are present
- [ ] Author information matches submission system

#### AI Workflow Document
- [ ] Lists all AI tools used with version/model information
- [ ] Describes the pipeline: idea → design → literature → data → estimation → writing
- [ ] Explains human checkpoints and quality gates
- [ ] Honest about AI limitations encountered
- [ ] Describes the iterative refinement process

### Common Rejection Reasons at Finance Conferences

1. **Unclear contribution**: Referee cannot state in one sentence what the paper adds
2. **Weak identification**: Causal claims without credible identification strategy
3. **Overfitting to crypto**: Results are about crypto-specific phenomena with no broader economic insight
4. **Missing benchmarks**: No comparison to existing methods or baselines
5. **Scope too broad**: Paper tries to answer too many questions
6. **Poor writing**: Verbose, poorly organized, unclear exposition
7. **Insufficient robustness**: Only one specification, no sensitivity analysis
8. **Stale data**: Results based on data that is several years old without justification
