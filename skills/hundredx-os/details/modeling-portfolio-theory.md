# Portfolio Theory

## Overview

Portfolio theory studies how investors allocate wealth across assets to optimize the risk-return tradeoff. From Markowitz's mean-variance framework to modern factor-based and risk-parity approaches, the field provides both normative guidance (how should you invest?) and positive tools (how do we measure portfolio performance?).

## Mean-Variance Optimization (Markowitz, 1952)

### Setup

Given N assets with:
- Expected returns: mu (N x 1 vector)
- Covariance matrix: Sigma (N x N, positive definite)
- Portfolio weights: w (N x 1, sum to 1)

Portfolio return: E[R_p] = w' * mu
Portfolio variance: Var(R_p) = w' * Sigma * w

### Optimization Problem

Minimize w' * Sigma * w
subject to w' * mu = mu_target, w' * 1 = 1

**Efficient frontier**: the set of portfolios with minimum variance for each target return.

**Global minimum variance (GMV) portfolio**:
w_gmv = (Sigma^{-1} * 1) / (1' * Sigma^{-1} * 1)

**Tangency (maximum Sharpe ratio) portfolio**:
w_tan = (Sigma^{-1} * (mu - r_f * 1)) / (1' * Sigma^{-1} * (mu - r_f * 1))

```python
import numpy as np
from scipy.optimize import minimize

def max_sharpe_portfolio(mu, Sigma, rf=0):
    """Maximum Sharpe ratio portfolio (tangency portfolio)."""
    n = len(mu)
    excess = mu - rf

    def neg_sharpe(w):
        ret = w @ excess
        vol = np.sqrt(w @ Sigma @ w)
        return -ret / vol

    constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
    bounds = [(0, 1)] * n  # long-only
    w0 = np.ones(n) / n
    result = minimize(neg_sharpe, w0, bounds=bounds, constraints=constraints)
    return result.x

def min_variance_portfolio(Sigma):
    """Global minimum variance portfolio."""
    n = Sigma.shape[0]
    ones = np.ones(n)
    Sigma_inv = np.linalg.inv(Sigma)
    w = Sigma_inv @ ones / (ones @ Sigma_inv @ ones)
    return w
```

### Estimation Error Problem

Mean-variance optimization is extremely sensitive to estimation error in mu and Sigma:
- Small errors in expected returns produce large weight swings.
- Estimated optimal portfolios often perform poorly out of sample.
- The "error maximization" critique (Michaud, 1989).

**Remedies**:
- Shrinkage estimators for Sigma (Ledoit-Wolf).
- Bayesian approaches (Black-Litterman).
- Constraints (no short-selling, position limits).
- Resampled efficient frontier (Michaud, 1998).
- Focus on minimum variance (which only needs Sigma, not mu).

## Black-Litterman Model (1992)

Combines market equilibrium (CAPM implied returns) with investor views.

### Steps

1. **Equilibrium returns**: Start from market-cap-weighted implied excess returns:
   pi = delta * Sigma * w_mkt
   where delta = (E[R_m] - r_f) / sigma_m^2.

2. **Investor views**: Express K views as P * mu = q + epsilon, epsilon ~ N(0, Omega).
   - P: K x N pick matrix (e.g., "Asset A outperforms Asset B by 2%").
   - q: K x 1 view returns.
   - Omega: K x K confidence matrix (diagonal: less confident → higher variance).

3. **Posterior returns**:
   mu_BL = [(tau*Sigma)^{-1} + P'*Omega^{-1}*P]^{-1} * [(tau*Sigma)^{-1}*pi + P'*Omega^{-1}*q]

4. **Optimize**: Use mu_BL in standard mean-variance optimization.

tau ~ 0.025 (a scalar controlling prior uncertainty relative to data).

### Advantages
- Starts from a reasonable equilibrium (not zero expected returns).
- Views are blended with equilibrium, not imposed.
- Produces stable, diversified portfolios.
- Investor only needs to express relative or absolute views on specific assets.

## Risk Parity

Allocate portfolio such that each asset contributes equally to total portfolio risk.

### Equal Risk Contribution (ERC)

For asset i, its risk contribution:
RC_i = w_i * (Sigma * w)_i / sqrt(w' * Sigma * w)

Target: RC_i = RC_j for all i, j.

This means: w_i * (Sigma * w)_i = w_j * (Sigma * w)_j.

```python
def risk_parity(Sigma):
    """Equal risk contribution portfolio."""
    n = Sigma.shape[0]

    def risk_contribution(w):
        port_vol = np.sqrt(w @ Sigma @ w)
        marginal = Sigma @ w / port_vol
        rc = w * marginal
        target = port_vol / n
        return np.sum((rc - target) ** 2)

    constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
    bounds = [(0.01, 1)] * n
    w0 = np.ones(n) / n
    result = minimize(risk_contribution, w0, bounds=bounds, constraints=constraints)
    return result.x
```

### Properties
- Does not require expected return estimates (only Sigma).
- Produces more diversified portfolios than mean-variance.
- In practice, often combined with leverage (borrow at risk-free to target a volatility level).
- Bridgewater's "All Weather" strategy is risk-parity-inspired.

## Covariance Estimation

### Sample Covariance
Sigma_hat = (1/(T-1)) * X' * X (where X is demeaned returns matrix)

- Unbiased but noisy, especially when N is large relative to T.
- Eigenvalues are spread out (largest too large, smallest too small).
- If N > T, the matrix is singular.

### Ledoit-Wolf Shrinkage (2003)

Sigma_shrunk = delta * F + (1 - delta) * Sigma_hat

- F: structured target (e.g., diagonal matrix, single-factor model covariance, constant correlation).
- delta: shrinkage intensity (estimated to minimize expected loss).
- Optimal delta has a closed-form formula.

```python
from sklearn.covariance import LedoitWolf

cov_estimator = LedoitWolf().fit(returns)
Sigma_shrunk = cov_estimator.covariance_
print(f"Shrinkage coefficient: {cov_estimator.shrinkage_:.3f}")
```

### Factor Model Covariance

Sigma = B * Sigma_f * B' + D

- B: factor loadings (N x K).
- Sigma_f: factor covariance (K x K).
- D: diagonal idiosyncratic variance (N x N).
- With K << N factors, this is a low-rank plus diagonal structure.
- Better conditioned than the sample covariance when N is large.

## Performance Evaluation

### Return Metrics

**Cumulative return**: Product(1 + R_t) - 1.
**Annualized return**: (1 + cumulative)^(252/T) - 1 for daily data.
**Annualized volatility**: std(R_t) * sqrt(252) for daily data.

### Risk-Adjusted Return Metrics

**Sharpe ratio** (Sharpe, 1966):
SR = (E[R_p] - R_f) / sigma_p

- The standard risk-adjusted performance metric.
- Annualize: SR_annual = SR_daily * sqrt(252) (approximately).
- Bootstrapped confidence intervals recommended (Lo, 2002).
- Beware: SR assumes normal returns. Strategies with negative skewness or fat tails can have high SR but large tail risk.

**Sortino ratio**:
Sortino = (E[R_p] - R_f) / sigma_downside

- Uses only downside deviation (volatility of negative returns).
- Better for asymmetric return distributions.

**Information ratio**:
IR = alpha / sigma_epsilon

- alpha and sigma_epsilon from a regression of portfolio returns on benchmark.
- Measures active return per unit of active risk (tracking error).

**Calmar ratio**: Annualized return / Max drawdown.

### Drawdown Analysis

**Maximum drawdown**: Largest peak-to-trough decline.

MDD = max_{t} (max_{s<=t} V_s - V_t) / max_{s<=t} V_s

```python
def max_drawdown(returns):
    """Compute maximum drawdown from a return series."""
    cumulative = (1 + returns).cumprod()
    running_max = cumulative.cummax()
    drawdowns = (cumulative - running_max) / running_max
    return drawdowns.min()
```

**Drawdown duration**: Time from peak to recovery (or ongoing if not recovered).

### Attribution

**Brinson-Fachler decomposition**: For a benchmark-relative portfolio:
- Allocation effect: being over/underweight in asset classes that performed well/poorly.
- Selection effect: picking better/worse securities within each asset class.
- Interaction effect: the cross-term.

**Factor attribution**: Decompose returns into factor exposures * factor returns + alpha.

R_p = alpha + Sum(beta_k * F_k) + epsilon

Report: what fraction of return came from market, size, value, momentum, etc.

## Portfolio Construction in Practice

### Constraints
- **Long-only**: w_i >= 0. Dramatically changes the efficient frontier.
- **Position limits**: w_i <= w_max (e.g., 5% per stock).
- **Sector limits**: sum of weights in a sector <= threshold.
- **Turnover limits**: constrain sum of |Delta_w_i| to control transaction costs.
- **Tracking error**: sigma(R_p - R_b) <= TE_max.

### Transaction Costs
- Proportional costs: c * |Delta_w_i| * Portfolio_value.
- Market impact: increases with trade size (square-root model: impact ~ sqrt(Volume)).
- Net-of-cost optimization: subtract estimated costs from expected returns.

### Rebalancing
- Calendar rebalancing: monthly, quarterly, annually.
- Threshold rebalancing: rebalance when weights drift beyond bands.
- Tradeoff: more frequent rebalancing keeps weights closer to optimal but incurs higher costs.

## Practical Checklist

1. **Inputs**: Use Ledoit-Wolf or factor model for covariance. For expected returns, use Black-Litterman or skip returns entirely (minimum variance / risk parity).
2. **Constraints**: Always impose long-only and position limits in practice. Unconstrained MVO is unstable.
3. **Out-of-sample testing**: Rolling window or expanding window optimization. Report out-of-sample Sharpe, turnover, and max drawdown.
4. **Performance metrics**: Report annualized return, volatility, Sharpe, max drawdown, Calmar ratio. Include benchmark comparison.
5. **Transaction costs**: Estimate and subtract from returns. Report gross and net performance.
6. **Factor attribution**: Decompose returns into factor contributions and alpha.
7. **Robustness**: Test sensitivity to estimation window, rebalancing frequency, and constraint parameters.
8. **Statistical significance**: Bootstrap Sharpe ratios (Lo 2002). Difference in Sharpe ratios: Ledoit-Wolf (2008) test.
9. **Economic significance**: Report dollar returns, capacity, and scalability.
10. **Visualization**: Efficient frontier, cumulative return plots, drawdown plots, rolling Sharpe.

## Key References

- Markowitz, H. (1952). Portfolio selection. Journal of Finance.
- Black, F. and Litterman, R. (1992). Global portfolio optimization. Financial Analysts Journal.
- Ledoit, O. and Wolf, M. (2003). Improved estimation of the covariance matrix of stock returns with an application to portfolio selection. Journal of Empirical Finance.
- Maillard, S., Roncalli, T., and Teiletche, J. (2010). The properties of equally weighted risk contribution portfolios. Journal of Portfolio Management.
- DeMiguel, V., Garlappi, L., and Uppal, R. (2009). Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy? Review of Financial Studies.
- Lo, A.W. (2002). The statistics of Sharpe ratios. Financial Analysts Journal.
- Michaud, R.O. (1989). The Markowitz optimization enigma: Is 'optimized' optimal? Financial Analysts Journal.
- Brinson, G.P., Hood, L.R., and Beebower, G.L. (1986). Determinants of portfolio performance. Financial Analysts Journal.
