---
citekey: liang2024mapping
title: 'Mapping the Increasing Use of LLMs in Scientific Papers'
authors:
  - 'Liang, W.'
  - 'Zhang, Y.'
  - 'Wu, Z.'
  - 'Lepp, H.'
  - 'Ji, W.'
  - 'Zhao, X.'
  - 'et al.'
year: 2024
venue: 'arXiv:2404.01268'
doi: ""
url: ""
kind: paper
themes:
  - research-productivity
  - evaluation-of-ai-research
methods:
  - empirical
relates_to_projects: []
status: read
---

## Summary

A large-scale corpus study estimating the prevalence of LLM-modified content in academic writing across 950,965 papers published between January 2020 and February 2024 on arXiv, bioRxiv, and the Nature portfolio. Using a population-level distributional GPT-quantification framework (rather than per-document AI detection), the authors track the estimated fraction of LLM-modified sentences over time and across venues. They report a steady post-ChatGPT increase, with Computer Science papers showing the fastest growth (up to 17.5%) and Mathematics and Nature portfolio venues showing the smallest (up to 6.3%).

## Contribution

The first systematic, large-scale, longitudinal measurement of LLM-modified content in scientific writing across multiple venues and disciplines, plus correlational evidence on which structural features of papers (preprint posting frequency, research crowdedness, paper length) are associated with higher LLM use.

## Method

Population-level statistical framework using the distributional GPT quantification estimator (companion to Liang et al. 2024 on peer reviews). Independent point-in-time estimates with bootstrap 95% CIs; no temporal smoothing imposed. Applied to abstracts and introductions of papers across five arXiv categories, bioRxiv, and 15 Nature portfolio journals.

## Relevance to RISE

Provides the empirical denominator for how widely LLMs are already infused into human-authored scientific writing, which RISE-style fully agentic pipelines (such as [`e2er`](../../projects/e2er.md) and [`sakana-ai-scientist`](../../projects/sakana-ai-scientist.md)) extend further. The discipline-level heterogeneity (CS leading, Math and Nature lagging) is directly relevant to scoping the evaluation-of-ai-research thread and to interpreting productivity-cluster results from filimonovic2025genai, noy2023experimental, kwon2025inequality, and brynjolfsson2025genaiwork.

## Critique / open questions

The estimator measures LLM "modification" but cannot distinguish polishing from substantive generation, and the alpha is sensitive to the choice of reference distributions. Cross-discipline differences may partly reflect stylistic baselines rather than true differential adoption.

## Key quotes

> "We conduct the first systematic, large-scale analysis across 950,965 papers published between January 2020 and February 2024 on the arXiv, bioRxiv, and Nature portfolio journals, using a population-level statistical framework to measure the prevalence of LLM-modified content over time."

> "Our findings reveal a steady increase in LLM usage, with the largest and fastest growth observed in Computer Science papers (up to 17.5%). In comparison, Mathematics papers and the Nature portfolio showed the least LLM modification (up to 6.3%)."

> "Higher levels of LLM-modification are associated with papers whose first authors post preprints more frequently, papers in more crowded research areas, and papers of shorter lengths."
