<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/reasoning-anti-slop.md -->

# `anti-slop`

*Pack: [100xOS shared skills](../hundredx-os.md) · category `audit` · field `economics`*

---

# Anti-Slop Rules for Academic Writing

## Purpose

AI-generated academic text has a recognizable style: hedge-heavy, filler-laden, and structurally repetitive. A referee -- or any experienced reader -- spots it immediately. These rules produce writing that sounds like a senior researcher, not a language model.

---

## Rule 1: Cut Filler Phrases

Delete these on sight. They add no information.

| Bad | Fix |
|-----|-----|
| "It is important to note that X" | X |
| "It is worth mentioning that X" | X |
| "It should be noted that X" | X |
| "As previously discussed" | [delete -- if the reader needs a reminder, give a specific reference like "as shown in equation (3)"] |
| "In this section, we discuss X" | [delete -- just discuss X] |
| "The remainder of this paper is organized as follows" | [acceptable only in introductions; keep it to one sentence] |
| "In the context of our analysis" | [delete] |
| "This highlights the importance of" | [delete; if something is important, the evidence should show it] |
| "Interestingly, ..." | [delete -- let the reader decide what's interesting] |

---

## Rule 2: Replace Hedging with Substance

Hedging is acceptable when it reflects genuine uncertainty. It is unacceptable as a reflex.

| Bad | Fix |
|-----|-----|
| "Further research is needed" | "Three questions remain open: [specific question 1], [specific question 2], and [specific question 3]" |
| "The results suggest that X might be the case" | "The point estimate of 0.03 (SE 0.01) indicates X, though the confidence interval does not rule out [specific alternative]" |
| "This could potentially have implications for policy" | "This implies [specific policy recommendation] because [specific mechanism]" |
| "These findings are broadly consistent with the literature" | "The elasticity of 0.4 aligns with [Author (Year)]'s estimate of 0.35 using [different method]" |

---

## Rule 3: Active Voice for Your Contributions

Use active voice when describing what you do. Passive voice is fine for background or methods that are standard.

| Bad | Fix |
|-----|-----|
| "A model is developed in which..." | "We model X as..." |
| "It was found that..." | "We find that..." |
| "The data was collected from..." | "We collected data from..." (or passive is fine: "Data were obtained from [source]") |
| "An analysis was conducted" | "We analyze..." |

Exception: use passive when the actor doesn't matter ("The survey was administered in March 2019") or when convention demands it ("Standard errors are clustered at the state level").

---

## Rule 4: Vary Sentence Structure

AI text falls into a rhythmic pattern: simple sentence, compound sentence, simple sentence, compound sentence. Break the pattern.

**Techniques:**
- Start some sentences with a subordinate clause: "Because X, we expect Y."
- Use short sentences for emphasis after a complex one.
- Occasionally lead with the result: "The coefficient is negative and significant (Table 3, column 2), consistent with the model's prediction that..."
- Parenthetical asides add rhythm variation: "The effect is large -- roughly twice the cross-sectional standard deviation -- and precisely estimated."

---

## Rule 5: Precision over Generality

| Bad | Fix |
|-----|-----|
| "We use a large dataset" | "We use administrative records covering 2.3 million workers over 2005-2019" |
| "The effect is economically significant" | "A one-standard-deviation increase in X raises Y by 12%, equivalent to $4,200 per year" |
| "Recent studies have shown" | "[Author1 (Year), Author2 (Year)] show" |
| "There is a growing literature on X" | "[delete and cite the specific papers that matter]" |
| "We control for a rich set of covariates" | "We control for age, education, industry, and firm size" |

---

## Rule 6: No Section-Opening Previews

Do not start a section by explaining what the section will do. Just do it.

| Bad | Good |
|-----|------|
| "In this section, we present our empirical strategy. We begin by describing the data, then outline our identification approach, and finally discuss potential threats." | "Our identification exploits the 2012 reform as a natural experiment..." |
| "This section develops the theoretical model. We first set up the environment, then characterize the equilibrium, and derive comparative statics." | "Consider an economy with N firms, each choosing..." |

Exception: a one-sentence roadmap at the end of the introduction is standard practice.

---

## Rule 7: No Redundant Explanations

Trust the reader. If you've defined notation, don't re-explain it every time you use it.

| Bad | Good |
|-----|------|
| "We estimate equation (1), where Y is the outcome variable, X is the treatment indicator, and Z is the vector of controls, as previously defined" | "We estimate equation (1)" |
| "Recall that beta represents the treatment effect. The estimated beta is..." | "The estimated treatment effect is..." |

---

## Rule 8: Specific Before/After Examples

### Example 1: Introduction paragraph

**Before (AI-sounding):**
"This paper contributes to the growing literature on the effects of minimum wage policies on employment outcomes. Using a novel dataset and an innovative identification strategy, we find that minimum wage increases have heterogeneous effects across different types of workers. These findings have important implications for policymakers considering minimum wage adjustments."

**After (researcher-sounding):**
"We estimate the employment effect of the 2016 Seattle minimum wage increase using matched employer-employee records. The staggered rollout across firm sizes provides a difference-in-differences design. Hours worked fell by 9% among jobs paying below $19/hour, offsetting the 3% hourly wage gain and reducing monthly earnings by $125. The reductions concentrate among workers with fewer than three months of tenure."

### Example 2: Results discussion

**Before (AI-sounding):**
"The results presented in Table 3 reveal several interesting patterns. First, we find that the coefficient on our variable of interest is positive and statistically significant, suggesting that there is indeed a positive relationship between X and Y. Second, the magnitude of the effect is economically meaningful, indicating that X plays an important role in determining Y."

**After (researcher-sounding):**
"Column 3 of Table 3 shows our preferred specification. A one-standard-deviation increase in local labor market concentration reduces wages by 2.1% (SE 0.8%). This is smaller than the 3.4% estimate in [Author (Year)], likely because our instrument isolates variation in concentration driven by plant closures rather than mergers, which may have different wage effects."

### Example 3: Conclusion

**Before (AI-sounding):**
"In conclusion, this paper has made several important contributions to the literature. We have demonstrated that X affects Y through a novel mechanism. While our study has some limitations, including potential concerns about external validity, our findings nonetheless provide valuable insights for both researchers and policymakers. Future research should explore these questions in other contexts."

**After (researcher-sounding):**
"Local labor market concentration depresses wages. The effect operates through reduced outside options rather than monopsony pricing: workers in concentrated markets receive fewer competing offers (Table 5), and the wage penalty disappears for workers with portable skills who can credibly threaten to leave (Table 6). Our estimates are identified from plant closures in tradable industries and may not generalize to service-sector concentration."
