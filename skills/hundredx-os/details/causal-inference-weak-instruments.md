# Weak Instruments

## The Problem

An instrument is "weak" when it is only slightly correlated with the endogenous variable. Formally, the concentration parameter (a function of the first-stage coefficients and the covariance structure) is small. Under weak instruments:

- The 2SLS estimator is biased toward the OLS estimate. The bias is approximately (1/F) times the OLS bias, where F is the first-stage F-statistic.
- Standard Wald-based confidence intervals have incorrect coverage. Nominal 95% intervals may cover the true parameter far less often.
- The distribution of the 2SLS t-statistic is non-normal, even in large samples.
- Point estimates become unreliable; inference based on them is misleading.

Weak instruments are not a small-sample problem. They persist in large samples because the issue is the signal-to-noise ratio in the first stage, not the sample size per se.

## First-Stage F-Statistic

### Conventional F-stat
The F-statistic from the first-stage regression testing the null that all excluded instruments have zero coefficients.

**Staiger and Stock (1997) rule of thumb**: F > 10. This threshold ensures that 2SLS bias is no more than approximately 10% of the OLS bias and that the Wald test has size distortion of no more than about 10 percentage points (actual size no more than 15% at 5% nominal level).

**Limitations of the rule of thumb**:
- Applies to the non-robust (homoskedastic) F-statistic with a single endogenous regressor.
- With heteroskedasticity or clustering, the conventional F is not the appropriate diagnostic.
- With multiple endogenous regressors, the single-equation F is insufficient.

### Effective F-Statistic (Olea and Pflueger 2013)
- Robust to heteroskedasticity, serial correlation, and clustering.
- Defined as F_eff = (beta_hat' * V^{-1} * beta_hat) / K, where the variance matrix V is robust.
- Compare to critical values from Olea and Pflueger tables, which depend on the number of instruments, the desired maximum bias/size distortion, and the estimator (2SLS vs LIML).
- For 2SLS with one endogenous variable, the critical value for 10% worst-case bias is approximately 23.1 (stricter than the Staiger-Stock threshold).

### Sanderson-Windmeijer (2016) F-statistics
- For models with multiple endogenous regressors, report a conditional first-stage F-statistic for each endogenous variable.
- Tests whether each endogenous variable is identified, holding the others fixed.
- A single weak instrument for one endogenous regressor contaminates all coefficient estimates in the system.

## Stock-Yogo Critical Values

Stock and Yogo (2005) provide formal critical values for weak instrument tests based on two criteria:

### Relative bias criterion
- The null: the bias of 2SLS relative to OLS exceeds a threshold b (e.g., 5%, 10%, 20%, 30%).
- Critical values depend on the number of endogenous regressors (n) and the number of instruments (K).
- For n = 1, K = 1: the critical value for 10% max relative bias is 16.38.
- More instruments lower the critical value but increase bias from many instruments.

### Size distortion criterion
- The null: the actual rejection rate of a 5% Wald test exceeds a threshold r (e.g., 10%, 15%, 20%, 25%).
- For n = 1, K = 1: the critical value for 10% max size distortion is 16.38 (same as bias criterion in this case).
- These critical values are specific to 2SLS. LIML has different (typically lower) critical values.

**Key table entries (n = 1, 2SLS, 10% relative bias)**:
| K (instruments) | Critical value |
|-----------------|----------------|
| 1               | 16.38          |
| 2               | 19.93          |
| 3               | 22.30          |
| 5               | 26.87          |
| 10              | 35.19          |

With more instruments, the critical value increases because each additional instrument adds bias from overfitting.

## Anderson-Rubin Test

The Anderson-Rubin (AR) test provides valid inference on the structural parameter regardless of instrument strength.

**Procedure**: Test the null H0: beta = beta_0 by regressing Y - beta_0 * X on the instruments Z and controls W. Under H0, the instruments should have no explanatory power for Y - beta_0 * X. The F-statistic from this regression is the AR statistic.

**Properties**:
- Correct size regardless of instrument strength (even with completely irrelevant instruments).
- Inverted AR test yields a confidence set: the set of beta_0 values that are not rejected.
- With strong instruments, the AR confidence set is close to the Wald confidence interval.
- With weak instruments, the AR confidence set may be much wider, empty, or even unbounded (the entire real line), correctly reflecting the lack of identification.

**Limitations**:
- With many instruments, the AR test loses power because it tests all instruments jointly.
- The conditional likelihood ratio (CLR) test of Moreira (2003) is more powerful while maintaining correct size.

## The tF Procedure (Lee, McCrary, Moreira, and Porter 2022)

A simple and practical approach to inference under potentially weak instruments.

**Procedure**:
1. Compute the first-stage F-statistic.
2. Compute the standard 2SLS t-ratio.
3. Use adjusted critical values from Lee et al. (2022) tables that depend on F.
4. For F > 104.7, use standard critical values (1.96 for 5%).
5. For smaller F, use inflated critical values. For example, at F = 10, the adjusted critical value is approximately 3.43.

**Properties**:
- Correct size in large samples regardless of instrument strength.
- Simple to implement: just look up the critical value given F and compare to the t-statistic.
- More powerful than the AR test when instruments are moderately weak.
- Does not require specialized software.

**Practical implication**: Many existing IV results with F-statistics between 10 and 20 would lose significance under the tF procedure. This highlights that the Staiger-Stock rule of thumb, while useful, is not sufficient for reliable inference.

## LIML vs 2SLS Under Weak Identification

### 2SLS under weak instruments
- Biased toward OLS.
- Bias proportional to the number of instruments (K) divided by the concentration parameter.
- Can be severely misleading: point estimates close to OLS with narrow confidence intervals that miss the true parameter.

### LIML under weak instruments
- Approximately median-unbiased (the median of the LIML sampling distribution is close to the true parameter).
- No finite moments (mean and variance do not exist), so mean bias is undefined.
- Much less biased than 2SLS in simulations.
- Wider confidence intervals than 2SLS, but better coverage.

### Fuller estimator
- Modified LIML: k = k_LIML - c/(n - K), where c is a user-chosen constant.
- Fuller(1) minimizes mean squared error and has finite moments.
- Fuller(4) provides approximately unbiased estimates.
- Practical choice when LIML confidence intervals are erratic.

### Recommendation
When the effective F is below 20-25, report LIML alongside 2SLS. If they diverge substantially, weak instruments are a real concern. Use AR or tF for inference rather than relying on the LIML point estimate alone.

## Many Instruments

When the number of instruments K is large relative to the sample size n, additional problems arise:

- **2SLS bias**: With K instruments, the bias of 2SLS is approximately K/(n*pi^2), where pi^2 is the concentration parameter per instrument. Many instruments amplify bias even when each instrument is individually strong.
- **LIML**: Less affected by many instruments than 2SLS, but can become erratic.
- **JIVE (Jackknife IV)**: Uses leave-one-out first-stage fitted values, eliminating the many-instruments bias. Consistent as K/n -> alpha for some alpha < 1.
- **RJIVE (Regularized JIVE)**: Adds ridge regularization to JIVE for better finite-sample performance.
- **UJIVE (Unbiased JIVE)**: Chao et al. (2012) variant that is consistent even as K/n -> 1.

**Practical guidance**: If you have more than a handful of instruments, compare 2SLS, LIML, and JIVE. Agreement suggests the many-instruments problem is minor. Divergence signals trouble. Consider reducing the instrument count (use fewer lags, collapse the instrument matrix, use factor analysis to extract a few strong instruments).

## Diagnostic Summary

| Diagnostic | Purpose | Threshold / Reference |
|------------|---------|----------------------|
| Conventional F | Quick screen for weak ID (homoskedastic case) | F > 10 (Staiger-Stock) |
| Effective F | Robust weak ID test | Olea-Pflueger tables |
| Stock-Yogo critical values | Formal size/bias thresholds | Depends on K, n, estimator |
| AR test | Inference robust to weak ID | Chi-sq or F critical values |
| CLR test (Moreira) | More powerful weak-ID-robust inference | Simulated critical values |
| tF procedure | Adjusted t-test critical values | Lee et al. (2022) tables |
| Kleibergen-Paap rk statistic | Robust rank test for underidentification | Critical values from KP tables |

## Practical Checklist

1. Always report the first-stage F-statistic. Use the effective F (Olea-Pflueger) with robust/clustered SEs.
2. Compare F to Stock-Yogo critical values appropriate for your number of instruments and estimator.
3. If F < 20, report LIML alongside 2SLS. If they disagree, weak instruments are a problem.
4. Use the tF procedure for inference: adjust critical values based on the first-stage F.
5. Report Anderson-Rubin confidence sets, especially if F < 10.
6. With many instruments, report JIVE and consider instrument reduction.
7. Always report the reduced form. It is valid regardless of instrument strength.
8. If weak instruments are unavoidable, be honest about it. Present bounds and sensitivity analysis rather than pretending the problem does not exist.

## Key References

- Staiger, D. and Stock, J. (1997). Instrumental variables regression with weak instruments. Econometrica.
- Stock, J. and Yogo, M. (2005). Testing for weak instruments in linear IV regression. In Andrews and Stock (eds.), Identification and Inference for Econometric Models. Cambridge.
- Olea, J.L.M. and Pflueger, C. (2013). A robust test for weak instruments. Journal of Business and Economic Statistics.
- Lee, D., McCrary, J., Moreira, M., and Porter, J. (2022). Valid t-ratio inference for IV. American Economic Review.
- Andrews, I., Stock, J., and Sun, L. (2019). Weak instruments in IV regression: Theory and practice. Annual Review of Economics.
- Moreira, M. (2003). A conditional likelihood ratio test for structural models. Econometrica.
