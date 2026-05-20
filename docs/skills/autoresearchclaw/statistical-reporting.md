<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/statistical-reporting.md -->

# `statistical-reporting`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../autoresearchclaw/">AutoResearchClaw skills</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/statistical-reporting/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/autoresearchclaw/statistical-reporting/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/aiming-lab/AutoResearchClaw" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

### Statistical Reporting Best Practice

#### Test Selection Quick Reference
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

#### Assumption Checking
1. **Normality**: Shapiro-Wilk test (n < 50) or visual Q-Q plots
2. **Homogeneity of variance**: Levene's test before t-tests and ANOVA
3. **Independence**: Verify study design ensures independent observations
4. **Linearity**: Scatter plots and residual plots for regression
5. **Multicollinearity**: VIF < 5 for multiple regression predictors
6. When assumptions are violated, use non-parametric alternatives or robust methods

#### APA Reporting Format
1. **t-test**: t(df) = X.XX, p = .XXX, d = X.XX
2. **ANOVA**: F(df_between, df_within) = X.XX, p = .XXX, eta-squared = .XX
3. **Correlation**: r(df) = .XX, p = .XXX [95% CI: .XX, .XX]
4. **Chi-square**: chi-square(df, N = XXX) = X.XX, p = .XXX
5. **Regression**: beta = X.XX, SE = X.XX, t = X.XX, p = .XXX
6. Always report exact p-values (not "p < .05") unless p < .001
7. Use leading zero for values that can exceed 1 (e.g., t = 0.50) but not for those bounded by 1 (e.g., p = .032, r = .45)

#### Effect Sizes
1. ALWAYS report effect sizes alongside p-values
2. Cohen's d for group comparisons: small = 0.2, medium = 0.5, large = 0.8
3. Eta-squared for ANOVA: small = .01, medium = .06, large = .14
4. R-squared for regression: report adjusted R-squared for multiple predictors
5. Odds ratios for logistic regression with 95% confidence intervals
6. Distinguish statistical significance from practical significance

#### Common Mistakes to Avoid
1. Never say "the results were not significant, therefore there is no effect"
2. Do not confuse correlation with causation in observational data
3. Apply multiple comparison corrections (Bonferroni, FDR) when running many tests
4. Report confidence intervals, not just point estimates
5. State whether tests are one-tailed or two-tailed and justify the choice
