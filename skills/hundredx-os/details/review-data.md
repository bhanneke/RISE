# Data Review Checklist for Empirical Economics

## Purpose

Data quality determines the credibility of empirical research. No econometric method can fix fundamentally flawed data. This checklist provides a systematic approach to reviewing data used in economics research -- whether you are checking your own work, reviewing a coauthor's data preparation, or assessing the data quality in a paper you are refereeing.

---

## 1. Source Documentation

Every dataset used in a paper must be traceable to its origin. A reader or replicator should be able to understand exactly where the data came from and how it was obtained.

**Check these items:**

- [ ] The data source is fully identified: name of the survey, administrative agency, or data provider.
- [ ] The citation includes a persistent identifier (DOI, URL, or official reference) where applicable.
- [ ] The data vintage or version is specified. Administrative datasets and surveys are updated and revised; results may differ across vintages.
- [ ] Access conditions are documented. Is the data publicly available? Restricted-access? Proprietary? If restricted, is enough information provided for another researcher to apply for access?
- [ ] The geographic scope and time coverage are clearly stated: "Firm-level data from the Dutch Chamber of Commerce, covering all registered firms in the Netherlands, 2005--2019."
- [ ] The unit of observation is defined: individual, household, firm, establishment, municipality, country-year, etc.
- [ ] If multiple datasets are merged, each source is documented separately and the merge key is specified.
- [ ] The population the data is intended to represent is described. Is this a census, a representative sample, or a convenience sample?

---

## 2. Sample Construction

The path from the raw data to the analysis sample must be transparent and justified.

**Check these items:**

- [ ] Every sample restriction is explicitly stated and justified: "We drop observations with missing wage data (N = 1,234, 3.2% of the sample)."
- [ ] A sample flow diagram or table shows the number of observations at each stage of filtering. Example:

  | Step | N (observations) | N (firms) |
  |------|-----------------|-----------|
  | Raw data | 500,000 | 45,000 |
  | Drop if missing outcome | 485,000 | 44,200 |
  | Drop if outside age range | 412,000 | 41,000 |
  | Drop if fewer than 3 years | 380,000 | 38,500 |
  | **Analysis sample** | **380,000** | **38,500** |

- [ ] The analysis sample is large enough for the intended analysis. Small samples raise power concerns and make results fragile.
- [ ] Sample restrictions are not endogenous to treatment. Dropping observations based on outcomes or post-treatment variables introduces selection bias.
- [ ] If the sample is a subset of a larger population, the paper discusses whether results generalize beyond the sample.
- [ ] Panel attrition is documented and tested: are the units that leave the sample systematically different from those that stay?

---

## 3. Missing Values

Missing data is ubiquitous and must be handled deliberately, not by default.

**Check these items:**

- [ ] The extent of missing data is reported for all key variables: "Wages are missing for 8.3% of observations."
- [ ] The pattern of missingness is analyzed. Is it missing completely at random (MCAR), missing at random (MAR), or missing not at random (MNAR)? The treatment strategy depends on this.
- [ ] The treatment of missing values is stated explicitly:
  - Listwise deletion (dropping all observations with any missing value): appropriate if MCAR, but reduces sample size and may introduce bias.
  - Indicator approach (including a missing-data dummy): common in economics, but can introduce bias if missingness is correlated with the outcome.
  - Imputation (single or multiple): appropriate for MAR, but assumptions must be stated.
- [ ] The paper shows that results are robust to alternative treatments of missing data.
- [ ] Coded missing values are not mistaken for real values. Many datasets use -9, -99, 999, or 0 to indicate missing data. These must be recoded to proper missing values before analysis.
- [ ] Missing values in categorical variables are not silently dropped by the software. In Stata, missing for numeric variables is treated as positive infinity in comparisons. In R, `NA` propagates through calculations unless explicitly handled.

---

## 4. Variable Definitions

Every variable in the analysis must be defined precisely enough that another researcher could construct it independently.

**Check these items:**

- [ ] The outcome variable is defined unambiguously: "Log hourly wages, defined as annual labor earnings divided by annual hours worked, deflated to 2015 euros using the CPI."
- [ ] Treatment/explanatory variables are defined with the same precision.
- [ ] Constructed variables (indices, ratios, aggregates) have their construction documented step by step.
- [ ] Timing is clear: when is each variable measured? For treatment-control studies, are variables measured pre- or post-treatment?
- [ ] Variable transformations are appropriate:
  - Logarithms: are zeros handled? `log(1+x)` introduces a scaling assumption. Consider inverse hyperbolic sine (`asinh`) or Poisson pseudo-maximum likelihood for count/skewed data.
  - Winsorizing/trimming: at what percentiles? Applied to which variables? Justified by outlier analysis, not arbitrarily?
  - Standardization: mean-zero, unit-SD? If so, computed over which sample?
- [ ] Top-coded or bottom-coded variables are acknowledged. Survey data on income is often top-coded. Administrative wage data may be censored at the social security maximum.
- [ ] Units are stated for every variable: euros, dollars (which year?), years, percentage points, log points, standard deviations.

---

## 5. Outliers

Outliers can dominate regression estimates, particularly in small samples or with skewed distributions.

**Check these items:**

- [ ] The distribution of key variables is examined: histograms, box plots, or summary statistics including min, max, p1, p5, p95, p99.
- [ ] Extreme values are investigated: are they data errors, or genuine extreme observations?
- [ ] Outlier treatment is documented and justified:
  - Winsorizing (replacing values beyond a threshold with the threshold value) at stated percentiles.
  - Trimming (dropping observations beyond a threshold).
  - Robust regression methods (e.g., median regression, M-estimation).
- [ ] Results are shown to be robust to alternative outlier treatments. If trimming at the 1st/99th percentile matters for the result, the result is fragile.
- [ ] Leverage and influence statistics are considered for key regressions: Cook's distance, DFBETAS, or leave-one-out analysis.
- [ ] For cross-country or cross-state regressions: does dropping any single country/state change the results substantively?

---

## 6. Measurement Quality

The quality of measurement directly affects the interpretability of estimates. Measurement error in the outcome variable reduces precision. Measurement error in the explanatory variable biases estimates (attenuation bias in the classical case).

**Check these items:**

- [ ] The paper discusses the likely quality of the key measurements. Administrative data on wages is generally more accurate than survey self-reports. Self-reported health measures are noisier than clinical measurements.
- [ ] If measurement error is a concern, the paper discusses the direction of bias. Classical measurement error in the explanatory variable biases OLS toward zero. Non-classical measurement error can bias in either direction.
- [ ] Proxy variables are acknowledged as proxies. If "years of education" proxies for "human capital," the paper should discuss what the proxy misses.
- [ ] Survey response rates and potential non-response bias are discussed for survey data.
- [ ] Administrative data: are there known data quality issues? Reporting incentives that might distort the data?
- [ ] If the paper uses a constructed measure (e.g., a sentiment index, a trade exposure measure), its validity is discussed: does it correlate with external benchmarks? Has it been validated in prior work?

---

## 7. Time and Currency

**Check these items:**

- [ ] Monetary values are inflation-adjusted with a documented deflator (CPI, GDP deflator, PPI) and base year.
- [ ] Exchange rate conversions (if applicable) use a documented rate and date. PPP-adjusted or market rates? The choice matters.
- [ ] Time periods are consistently defined. "Year" can mean calendar year, fiscal year, or academic year depending on the context.
- [ ] Seasonal adjustment is applied where relevant (monthly or quarterly data).
- [ ] Date formats are unambiguous: "2019-Q1" is clear; "1/2/19" could mean January 2 or February 1.

---

## 8. Panel Data Specific Checks

**Check these items:**

- [ ] Panel dimensions are reported: how many units? How many periods? Is the panel balanced or unbalanced?
- [ ] Entry and exit patterns are documented. Firms enter and exit markets; individuals enter and exit the labor force. This is not random.
- [ ] Duplicate observations are checked: is each unit observed exactly once per period?
- [ ] Serial correlation in the outcome variable is examined (relevant for clustering decisions).
- [ ] Time-invariant variables are identified and handled appropriately (they are absorbed by unit fixed effects).

---

## 9. Cross-Sectional Data Specific Checks

**Check these items:**

- [ ] Sampling weights are used if the data is from a complex survey design (e.g., CPS, SIPP, SOEP).
- [ ] Stratification and clustering in the survey design are accounted for in standard error calculations.
- [ ] The sampling frame is documented: who is included in the population? Who is potentially excluded (non-coverage)?
- [ ] Response rates are reported and non-response bias is discussed.

---

## 10. Data Integrity and Replication

**Check these items:**

- [ ] Raw data is stored separately from processed data and never overwritten.
- [ ] Data processing scripts are version-controlled and documented.
- [ ] Checksums or row counts are used to verify data integrity after transfers or transformations.
- [ ] The analysis can be run from raw data to final results using documented code.
- [ ] Summary statistics in the paper match those produced by the code (spot-check specific numbers).
- [ ] If data cannot be shared (confidentiality), a synthetic or simulated dataset is provided that allows code verification.

---

## Red Flags in Data Descriptions

These patterns in a paper's data section should raise concern during review:

- **Vague sample descriptions:** "We use firm-level data" without specifying the country, time period, or source.
- **No summary statistics table:** A paper that does not show you the basic features of the data is hiding something or was careless.
- **Round numbers in sample sizes:** If N = 10,000 exactly, someone probably rounded. What happened to the observations that made it 9,847 or 10,123?
- **Missing data not discussed:** If the paper never mentions missing values, either the data is unusually complete (rare) or the authors did not check.
- **No balance table in treatment-control designs:** Without evidence of baseline comparability, treatment effects are uninterpretable.
- **Implausible summary statistics:** Mean income of $1 million in a population survey, negative standard deviations, minimum values above the mean.
- **Outcome and treatment variables from different time periods:** The treatment must precede the outcome. This seems obvious but is occasionally violated.
