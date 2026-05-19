# Option Pricing

## Overview

Option pricing theory values contingent claims — contracts whose payoff depends on the future value of an underlying asset. The fundamental insight is that options can be priced by constructing replicating portfolios (no-arbitrage) or by computing expected payoffs under the risk-neutral measure.

## Foundations

### Option Basics

**Call option**: Right to buy the underlying at strike K at/before expiration T.
- Payoff at expiration: max(S_T - K, 0)

**Put option**: Right to sell the underlying at strike K at/before expiration T.
- Payoff at expiration: max(K - S_T, 0)

**European**: Exercisable only at expiration.
**American**: Exercisable at any time up to expiration.

**Moneyness**: S/K ratio.
- In-the-money (ITM): S > K for calls, S < K for puts.
- At-the-money (ATM): S ~ K.
- Out-of-the-money (OTM): S < K for calls, S > K for puts.

### Put-Call Parity

For European options on a non-dividend-paying stock:

C - P = S - K * exp(-rT)

This is a no-arbitrage relationship. Violations indicate mispricing, transaction costs, or early exercise premium (American options).

### Risk-Neutral Pricing

Under no-arbitrage, there exists a risk-neutral probability measure Q such that:

V_0 = exp(-rT) * E^Q[Payoff(S_T)]

The underlying grows at the risk-free rate under Q:
E^Q[S_T] = S_0 * exp(rT)

This does NOT mean investors are risk-neutral — it is a mathematical equivalence derived from no-arbitrage.

## Black-Scholes-Merton Model

### Assumptions
1. Geometric Brownian Motion: dS/S = mu*dt + sigma*dW
2. Constant volatility sigma
3. Constant risk-free rate r
4. No dividends (or continuous dividend yield q)
5. No transaction costs or taxes
6. Continuous trading
7. No arbitrage opportunities

### Black-Scholes Formula

**Call**: C = S * N(d1) - K * exp(-rT) * N(d2)
**Put**: P = K * exp(-rT) * N(-d2) - S * N(-d1)

where:
- d1 = [ln(S/K) + (r + sigma^2/2) * T] / (sigma * sqrt(T))
- d2 = d1 - sigma * sqrt(T)
- N(.) = standard normal CDF

With continuous dividend yield q:
- Replace S with S * exp(-qT) everywhere.
- d1 = [ln(S/K) + (r - q + sigma^2/2) * T] / (sigma * sqrt(T))

```python
import numpy as np
from scipy.stats import norm

def bs_price(S, K, T, r, sigma, q=0, option_type='call'):
    """Black-Scholes European option price."""
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        return S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
```

## The Greeks

Sensitivities of option price to model inputs.

| Greek | Definition | Call | Put |
|-------|-----------|------|-----|
| Delta | dV/dS | N(d1) | N(d1) - 1 |
| Gamma | d^2V/dS^2 | n(d1) / (S*sigma*sqrt(T)) | same |
| Theta | dV/dT | -(S*sigma*n(d1))/(2*sqrt(T)) - r*K*exp(-rT)*N(d2) | ... + r*K*exp(-rT)*N(-d2) |
| Vega | dV/dsigma | S * sqrt(T) * n(d1) | same |
| Rho | dV/dr | K*T*exp(-rT)*N(d2) | -K*T*exp(-rT)*N(-d2) |

where n(.) = standard normal PDF.

```python
def bs_greeks(S, K, T, r, sigma, q=0):
    """Compute all Greeks for a European call."""
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = np.exp(-q * T) * norm.cdf(d1)
    gamma = np.exp(-q * T) * norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * np.exp(-q * T) * np.sqrt(T) * norm.pdf(d1)
    theta = (-(S * sigma * np.exp(-q * T) * norm.pdf(d1)) / (2 * np.sqrt(T))
             - r * K * np.exp(-r * T) * norm.cdf(d2)
             + q * S * np.exp(-q * T) * norm.cdf(d1))
    rho = K * T * np.exp(-r * T) * norm.cdf(d2)

    return {'delta': delta, 'gamma': gamma, 'vega': vega, 'theta': theta, 'rho': rho}
```

### Delta Hedging
- A delta-neutral portfolio: hold the option and short Delta shares.
- Rebalance as Delta changes (Gamma measures how fast Delta moves).
- Hedging error arises from discrete rebalancing, transaction costs, and vol misspecification.

## Implied Volatility

The volatility sigma_imp that, when plugged into Black-Scholes, reproduces the observed market price. Found by numerical inversion (Newton-Raphson or bisection).

```python
from scipy.optimize import brentq

def implied_vol(market_price, S, K, T, r, q=0, option_type='call'):
    """Compute implied volatility via root-finding."""
    def objective(sigma):
        return bs_price(S, K, T, r, sigma, q, option_type) - market_price

    return brentq(objective, 1e-6, 5.0)
```

### Volatility Surface

IV varies across strike (K) and maturity (T):

**Volatility smile/skew**: IV is higher for OTM puts and ITM calls (especially in equity indices). Reflects crash risk / fat tails not captured by BS.

**Term structure**: IV varies with maturity. Short-term IV reacts more to current events; long-term IV is more stable.

**The surface**: IV(K, T) is a 2D object. Interpolation methods: SVI (Stochastic Volatility Inspired) parameterization, SABR model, or spline interpolation.

## Binomial Tree (Cox-Ross-Rubinstein)

Discrete-time model. The stock moves up by factor u or down by factor d each period.

u = exp(sigma * sqrt(dt))
d = 1/u
p = (exp((r-q)*dt) - d) / (u - d)   # risk-neutral probability

### European Options
- Build tree forward: compute stock prices at each node.
- Work backward: at expiration, option value = payoff. At each prior node, discount expected value.

### American Options
- Same backward induction, but at each node compare continuation value with immediate exercise value.
- Take the maximum: V = max(payoff_if_exercise, discounted_expected_continuation)

```python
def binomial_tree(S, K, T, r, sigma, q, N, option_type='call', american=False):
    """CRR binomial tree for European or American options."""
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp((r - q) * dt) - d) / (u - d)
    disc = np.exp(-r * dt)

    # Terminal stock prices
    ST = S * u ** np.arange(N, -1, -1) * d ** np.arange(0, N + 1)

    # Terminal option values
    if option_type == 'call':
        V = np.maximum(ST - K, 0)
    else:
        V = np.maximum(K - ST, 0)

    # Backward induction
    for i in range(N - 1, -1, -1):
        V = disc * (p * V[:-1] + (1 - p) * V[1:])
        if american:
            Si = S * u ** np.arange(i, -1, -1) * d ** np.arange(0, i + 1)
            if option_type == 'call':
                V = np.maximum(V, Si - K)
            else:
                V = np.maximum(V, K - Si)

    return V[0]
```

## Monte Carlo Option Pricing

Simulate paths of the underlying under Q, compute payoffs, and average.

### Geometric Brownian Motion Simulation

S_T = S_0 * exp((r - q - sigma^2/2)*T + sigma*sqrt(T)*Z),  Z ~ N(0,1)

```python
def monte_carlo_european(S, K, T, r, sigma, q, n_paths=100000, option_type='call'):
    """Monte Carlo pricing for European options."""
    Z = np.random.standard_normal(n_paths)
    ST = S * np.exp((r - q - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    else:
        payoffs = np.maximum(K - ST, 0)

    price = np.exp(-r * T) * payoffs.mean()
    se = np.exp(-r * T) * payoffs.std() / np.sqrt(n_paths)

    return price, se
```

### Variance Reduction
- **Antithetic variates**: Use both Z and -Z. Halves variance for monotonic payoffs.
- **Control variates**: Use a correlated variable with known expectation (e.g., the stock itself, or a simpler option with closed-form price).
- **Importance sampling**: Shift the distribution to sample more from regions that matter for the payoff.

### Path-Dependent Options
Monte Carlo is the natural method for path-dependent exotics:
- Asian options (average price)
- Barrier options (knock-in/knock-out)
- Lookback options (max/min price)

For path simulation, discretize: S_{t+dt} = S_t * exp((r-q-sigma^2/2)*dt + sigma*sqrt(dt)*Z_t)

## Stochastic Volatility Models

### Heston Model (1993)

dS_t = (r - q) * S_t * dt + sqrt(V_t) * S_t * dW_1
dV_t = kappa * (theta - V_t) * dt + xi * sqrt(V_t) * dW_2
Corr(dW_1, dW_2) = rho

Parameters:
- V_0: initial variance
- theta: long-run variance
- kappa: mean reversion speed
- xi: vol of vol
- rho: correlation between stock and variance shocks (typically rho < 0 for equities — leverage effect)

The Heston model has a semi-closed-form solution via characteristic functions, making calibration feasible.

### SABR Model

Popular in interest rate derivatives:
dF = sigma * F^beta * dW_1
dsigma = alpha * sigma * dW_2
Corr(dW_1, dW_2) = rho

- beta: controls backbone (beta=1 lognormal, beta=0 normal)
- alpha: vol of vol
- rho: correlation

Hagan et al. (2002) provide an approximate implied vol formula, widely used for interpolation.

## Jump-Diffusion Models

### Merton (1976)

dS/S = (r - q - lambda*k)*dt + sigma*dW + J*dN

- dN: Poisson process with intensity lambda (average number of jumps per year).
- J: jump size, typically log(1+J) ~ N(mu_J, sigma_J^2).
- k = E[J] = exp(mu_J + sigma_J^2/2) - 1.

Option price is an infinite sum of BS prices weighted by Poisson probabilities:

C = Sum_{n=0}^{inf} (exp(-lambda'*T) * (lambda'*T)^n / n!) * BS(S, K, T, r_n, sigma_n)

where lambda' = lambda*(1+k), r_n = r - lambda*k + n*mu_J/T, sigma_n^2 = sigma^2 + n*sigma_J^2/T.

In practice, truncate at n=20-50.

## Calibration

### Fitting to Market Data
1. Collect market option prices (or implied vols) across strikes and maturities.
2. Define objective: minimize sum of squared differences between model and market prices (or implied vols).
3. Use optimization (Levenberg-Marquardt, differential evolution, or basin-hopping for global search).
4. Check fit quality: root mean squared error, examine residuals across the surface.

### Heston Calibration Example
```python
from scipy.optimize import differential_evolution

def heston_objective(params, market_data):
    """Sum of squared implied vol errors."""
    v0, theta, kappa, xi, rho = params
    total_error = 0
    for K, T, market_iv in market_data:
        model_price = heston_call_price(S, K, T, r, v0, theta, kappa, xi, rho)
        model_iv = implied_vol(model_price, S, K, T, r)
        total_error += (model_iv - market_iv) ** 2
    return total_error

bounds = [(0.001, 1), (0.001, 1), (0.1, 10), (0.01, 2), (-0.99, 0.99)]
result = differential_evolution(heston_objective, bounds, args=(market_data,))
```

## Practical Checklist

1. For European options on liquid underlyings: start with Black-Scholes.
2. Compute implied volatilities. If the surface shows significant smile/skew, BS is insufficient for pricing but useful as a quoting convention.
3. For American options: use binomial trees (or finite differences). BS does not apply directly.
4. For path-dependent exotics: use Monte Carlo with variance reduction.
5. For calibration to market data: Heston or SABR depending on asset class (equity vs rates).
6. Always check put-call parity as a sanity check.
7. Use Greeks for hedging and risk management. Delta-hedge and monitor Gamma exposure.
8. In empirical work: implied vol is often the object of study (not the option price itself).
9. Report moneyness (K/S or delta), not just strike, for comparability across firms/dates.
10. For academic papers: cite the model clearly, state all assumptions, and discuss their violations in your setting.

## Key References

- Black, F. and Scholes, M. (1973). The pricing of options and corporate liabilities. Journal of Political Economy.
- Merton, R.C. (1973). Theory of rational option pricing. Bell Journal of Economics.
- Cox, J.C., Ross, S.A., and Rubinstein, M. (1979). Option pricing: A simplified approach. Journal of Financial Economics.
- Heston, S.L. (1993). A closed-form solution for options with stochastic volatility. Review of Financial Studies.
- Merton, R.C. (1976). Option pricing when underlying stock returns are discontinuous. Journal of Financial Economics.
- Hull, J.C. (2021). Options, Futures, and Other Derivatives, 11th ed. Pearson.
- Gatheral, J. (2006). The Volatility Surface: A Practitioner's Guide. Wiley.
