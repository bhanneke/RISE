<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/modeling-risk-management.md -->

# `risk-management`

*Pack: [100xOS shared skills](../hundredx-os.md) · category `modeling` · field `economics`*

---

# Risk Management

## Overview

Quantitative risk management measures, models, and manages financial risk — the possibility that investment returns deviate from expectations. The field connects probability theory (tail risk modeling), statistics (estimation under uncertainty), and regulation (Basel/Solvency capital requirements).

## Risk Measures

### Value at Risk (VaR)

VaR_alpha: the loss threshold such that the probability of exceeding it is alpha.

P(L > VaR_alpha) = alpha

Equivalently: VaR_alpha = -F_L^{-1}(alpha), where F_L is the loss distribution CDF.

- alpha is typically 1% or 5%.
- Horizon: 1-day (trading), 10-day (Basel), 1-year (economic capital).
- Interpretation: "With 99% confidence, losses will not exceed VaR over the next day."

**Limitations**:
- Not subadditive: VaR(A+B) can exceed VaR(A) + VaR(B). Diversification may appear to increase risk.
- Tells nothing about the magnitude of losses beyond VaR (tail risk).
- Sensitive to distributional assumptions.

### Expected Shortfall (CVaR / Conditional VaR)

ES_alpha = E[L | L > VaR_alpha]

The expected loss conditional on exceeding VaR. Also called Conditional VaR (CVaR) or Tail VaR.

- Coherent risk measure (subadditive, monotone, positive homogeneous, translation invariant).
- Required by Basel III/IV for market risk capital.
- More informative about tail severity than VaR.

For continuous distributions: ES_alpha = (1/alpha) * integral_0^alpha VaR_u du.

### Estimation Methods

**Historical Simulation**:
- Sort historical P&L. VaR = the (alpha * N)-th worst loss.
- ES = average of all losses worse than VaR.
- No distributional assumptions. But: assumes past represents future.

```python
def historical_var_es(returns, alpha=0.01):
    """Historical simulation VaR and ES."""
    sorted_returns = np.sort(returns)
    n = len(sorted_returns)
    var_idx = int(np.floor(alpha * n))
    var = -sorted_returns[var_idx]
    es = -sorted_returns[:var_idx].mean()
    return var, es
```

**Parametric (Variance-Covariance)**:
- Assume returns ~ N(mu, sigma^2).
- VaR_alpha = -(mu + z_alpha * sigma) where z_alpha = Phi^{-1}(alpha).
- ES_alpha = -(mu - sigma * phi(z_alpha) / alpha).
- Fast but assumes normality (underestimates tail risk for financial returns).

```python
from scipy.stats import norm

def parametric_var_es(mu, sigma, alpha=0.01):
    """Parametric (normal) VaR and ES."""
    z = norm.ppf(alpha)
    var = -(mu + z * sigma)
    es = -(mu - sigma * norm.pdf(z) / alpha)
    return var, es
```

**Monte Carlo Simulation**:
- Simulate many scenarios from a fitted model (GARCH, multivariate normal, copula).
- Compute portfolio P&L for each scenario.
- VaR and ES from simulated distribution.
- Flexible: handles non-linear payoffs (options), complex dependence structures.

**GARCH-based**:
- Fit GARCH to returns. Use conditional volatility for VaR:
  VaR_t = -(mu_t + z_alpha * sigma_t) where sigma_t is GARCH conditional volatility.
- Captures time-varying risk.

### Backtesting VaR

**Unconditional coverage** (Kupiec, 1995):
- Count exceptions (days where loss > VaR). Under correct VaR, exceptions ~ Binomial(T, alpha).
- Likelihood ratio test.

**Conditional coverage** (Christoffersen, 1998):
- Exceptions should be independent (no clustering). Test both correct frequency and independence.

**Traffic light system** (Basel):
- Green (0-4 exceptions in 250 days at 99%): model accepted.
- Yellow (5-9): increased capital multiplier.
- Red (10+): model rejected, penalty.

## Tail Risk Modeling

### Extreme Value Theory (EVT)

Models the tail of the distribution directly, without assuming a specific distribution for the entire return series.

**Block Maxima (GEV distribution)**: Fit Generalized Extreme Value distribution to period maxima (e.g., monthly minimum returns).

**Peaks Over Threshold (POT)**: Model exceedances over a high threshold u using the Generalized Pareto Distribution (GPD):

P(X - u > x | X > u) = (1 + xi * x / beta)^{-1/xi}

- xi (shape): controls tail heaviness. xi > 0: heavy tail (Pareto). xi = 0: exponential. xi < 0: bounded tail.
- beta (scale): scaling parameter.
- Financial returns typically have xi in [0.1, 0.5] — heavy tails.

```python
from scipy.stats import genpareto

# Fit GPD to exceedances over threshold
threshold = np.percentile(losses, 95)  # or use mean excess plot
exceedances = losses[losses > threshold] - threshold

# Fit parameters
xi, loc, beta = genpareto.fit(exceedances, floc=0)

# VaR and ES from GPD
n = len(losses)
n_u = len(exceedances)
p_u = n_u / n

def gpd_var(alpha, xi, beta, p_u, threshold):
    return threshold + (beta / xi) * ((alpha / p_u) ** (-xi) - 1)

def gpd_es(var, xi, beta, threshold):
    return (var + beta - xi * threshold) / (1 - xi)
```

**Threshold selection**: Use the mean excess plot (should be linear above threshold) or Hill plot (xi estimate should stabilize).

### Fat Tails in Finance

Financial returns exhibit:
- Excess kurtosis (kurtosis >> 3).
- Power law tails: P(|R| > x) ~ x^{-alpha} with alpha typically 3-5 (finite variance but infinite higher moments).
- Asymmetry: left tail often heavier than right (crash risk).

Alternative distributions:
- Student-t: captures kurtosis via degrees of freedom parameter.
- Generalized hyperbolic: flexible family nesting t, normal, and other distributions.
- Stable distributions: can model infinite variance (alpha-stable), but controversial.

## Copulas

Model dependence between random variables separately from their marginal distributions.

### Sklar's Theorem
Any joint distribution F(x1, ..., xn) can be written as:

F(x1, ..., xn) = C(F_1(x1), ..., F_n(x_n))

where C is a copula and F_i are marginal CDFs.

### Common Copulas

**Gaussian copula**: Dependence structure of the multivariate normal. Symmetric, no tail dependence.

**Student-t copula**: Like Gaussian but with tail dependence (joint extreme events more likely). Controlled by degrees of freedom.

**Clayton copula**: Lower tail dependence. Captures joint crashes.

**Gumbel copula**: Upper tail dependence. Captures joint booms.

**Frank copula**: Symmetric, no tail dependence. Intermediate between Clayton and Gumbel.

### Tail Dependence

lambda_L = lim_{u->0} P(U_2 < u | U_1 < u) — probability of joint extreme negative events.
lambda_U = lim_{u->1} P(U_2 > u | U_1 > u) — probability of joint extreme positive events.

- Gaussian copula: lambda_L = lambda_U = 0 (no tail dependence, regardless of correlation).
- t copula: lambda_L = lambda_U > 0 (symmetric tail dependence).
- This matters critically for portfolio risk: Gaussian copula underestimates joint crash risk.

```python
from scipy.stats import kendalltau
from copulas.bivariate import Clayton, Gumbel, Frank

# Fit copula to pseudo-observations (rank-transformed data)
u = np.column_stack([
    rankdata(returns_1) / (len(returns_1) + 1),
    rankdata(returns_2) / (len(returns_2) + 1)
])

# Fit Clayton copula (lower tail dependence)
cop = Clayton()
cop.fit(u)
```

## Risk Decomposition

### Marginal and Component VaR

**Marginal VaR**: Change in portfolio VaR from a small increase in position i.
MVaR_i = dVaR / dw_i

**Component VaR**: Contribution of position i to total portfolio VaR.
CVaR_i = w_i * MVaR_i

Sum of component VaRs equals total VaR (Euler decomposition).

### Factor Risk Decomposition

Decompose portfolio variance into factor contributions:

Var(R_p) = beta_p' * Sigma_f * beta_p + sigma^2_epsilon

- Systematic risk: from factor exposures.
- Idiosyncratic risk: from residual.

## Stress Testing and Scenario Analysis

### Historical Scenarios
- Replay specific crisis periods (2008 GFC, COVID crash, dot-com bust).
- Apply historical factor movements to current portfolio.

### Hypothetical Scenarios
- Define extreme but plausible scenarios (e.g., rates +300bp, equities -30%, credit spreads +500bp).
- Compute portfolio P&L under each scenario.

### Reverse Stress Testing
- Start from a loss threshold (e.g., "what scenario causes a $X million loss?").
- Work backward to find the scenarios.

## Practical Checklist

1. Compute VaR and ES at 1% and 5% levels. Report both.
2. Use GARCH-based VaR for time-varying risk (not static historical simulation for actively traded portfolios).
3. Backtest VaR: Kupiec and Christoffersen tests. Report number of exceptions.
4. For tail modeling: use EVT/GPD rather than assuming normality.
5. For portfolio risk: use copulas to model non-linear dependence, especially tail dependence. Do not rely on linear correlation alone.
6. Decompose risk into systematic (factor) and idiosyncratic components.
7. Stress test against historical crises and plausible hypothetical scenarios.
8. Report risk in multiple units: percentage, dollar amount, number of standard deviations.
9. For academic papers: discuss model risk — how sensitive are risk estimates to distributional assumptions?
10. Compare risk estimates across methods (historical, parametric, Monte Carlo, EVT). Disagreement signals model uncertainty.

## Key References

- McNeil, A.J., Frey, R., and Embrechts, P. (2015). Quantitative Risk Management, revised ed. Princeton University Press.
- Jorion, P. (2006). Value at Risk, 3rd ed. McGraw-Hill.
- Christoffersen, P. (1998). Evaluating interval forecasts. International Economic Review.
- Kupiec, P. (1995). Techniques for verifying the accuracy of risk measurement models. Journal of Derivatives.
- Embrechts, P., Kluppelberg, C., and Mikosch, T. (1997). Modelling Extremal Events. Springer.
- Joe, H. (2014). Dependence Modeling with Copulas. Chapman & Hall.
- Artzner, P., Delbaen, F., Eber, J.M., and Heath, D. (1999). Coherent measures of risk. Mathematical Finance.
