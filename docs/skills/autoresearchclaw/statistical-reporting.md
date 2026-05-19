<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/statistical-reporting.md -->

# `statistical-reporting`



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
name: statistical-reporting
description: Statistical test selection, assumption checking, and APA-formatted reporting. Use when analyzing experimental results or writing results sections.
metadata:
  category: writing
  trigger-keywords: "statistic,hypothesis test,p-value,regression,ANOVA,t-test,effect size,confidence interval"
  applicable-stages: "14,17"
  priority: "3"
  version: "1.0"
  author: researchclaw
  references: "adapted from K-Dense-AI/claude-scientific-skills"
---

## Statistical Reporting Best Practice

### Test Selection Quick Reference
1. **Comparing two groups (independent, normal)**: Independent t-test
2. **Comparing two groups (independent, non-normal)**: Mann-Whitney U test
3. **Comparing two groups (paired, normal)**: Paired t-test
4. **Comparing two groups (paired, non-normal)**: Wilcoxon signed-rank test
5. **Comparing 3+ groups (independent, normal)**: One-way ANOVA + post-hoc
6. **Comparing 3+ groups (non-normal)**: Kruskal-Wallis test
7. **Relationship between continuous variables**: Pearson or Spearman correlation
8. **Categorical outcomes**: Chi-square or Fisher's exact test
9. **Predicting continuous outcome**: Linear regression
10. **Predicting binary outcome**: Logistic regression

### Assumption Checking
1. **Normality**: Shapiro-Wilk test (n < 50) or visual Q-Q plots
2. **Homogeneity of variance**: Levene's test before t-tests and ANOVA
3. **Independence**: Verify study design ensures independent observations
4. **Linearity**: Scatter plots and residual plots for regression
5. **Multicollinearity**: VIF < 5 for multiple regression predictors
6. When assumptions are violated, use non-parametric alternatives or robust methods

### APA Reporting Format
1. **t-test**: t(df) = X.XX, p = .XXX, d = X.XX
2. **ANOVA**: F(df_between, df_within) = X.XX, p = .XXX, eta-squared = .XX
3. **Correlation**: r(df) = .XX, p = .XXX [95% CI: .XX, .XX]
4. **Chi-square**: chi-square(df, N = XXX) = X.XX, p = .XXX
5. **Regression**: beta = X.XX, SE = X.XX, t = X.XX, p = .XXX
6. Always report exact p-values (not "p < .05") unless p < .001
7. Use leading zero for values that can exceed 1 (e.g., t = 0.50) but not for those bounded by 1 (e.g., p = .032, r = .45)

### Effect Sizes
1. ALWAYS report effect sizes alongside p-values
2. Cohen's d for group comparisons: small = 0.2, medium = 0.5, large = 0.8
3. Eta-squared for ANOVA: small = .01, medium = .06, large = .14
4. R-squared for regression: report adjusted R-squared for multiple predictors
5. Odds ratios for logistic regression with 95% confidence intervals
6. Distinguish statistical significance from practical significance

### Common Mistakes to Avoid
1. Never say "the results were not significant, therefore there is no effect"
2. Do not confuse correlation with causation in observational data
3. Apply multiple comparison corrections (Bonferroni, FDR) when running many tests
4. Report confidence intervals, not just point estimates
5. State whether tests are one-tailed or two-tailed and justify the choice


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/statistical-reporting/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>aiming-lab/AutoResearchClaw</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../autoresearchclaw.md">AutoResearchClaw skills</a></dd>
<dt><b>Category</b></dt><dd><code>analysis</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>data-analysis</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04-23</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw">⭐ aiming-lab/AutoResearchClaw</a><br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/autoresearchclaw/statistical-reporting/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/autoresearchclaw.yml">edit on GitHub</a>.</p>
</div>

</div>
