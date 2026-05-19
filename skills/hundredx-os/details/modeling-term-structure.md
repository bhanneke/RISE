# Term Structure Models

## Overview

Term structure models describe how interest rates vary across maturities. The yield curve — the relationship between yield and maturity — is fundamental to fixed income pricing, monetary policy transmission, and macroeconomic forecasting. Models range from purely statistical curve-fitting (Nelson-Siegel) to no-arbitrage dynamic models (Vasicek, CIR, HJM).

## Yield Curve Basics

### Definitions

**Zero-coupon yield** (spot rate) y(t,T): the annualized return from buying a zero-coupon bond at t maturing at T.

P(t,T) = exp(-y(t,T) * (T-t))

**Forward rate** f(t,T): the instantaneous rate at future time T implied by today's curve.

f(t,T) = -d/dT [ln P(t,T)]

**Yield curve shapes**:
- Normal (upward sloping): most common, reflects term premium and/or expected rate increases.
- Inverted: short rates > long rates, historically precedes recessions.
- Flat: transition between normal and inverted.
- Humped: peaks at intermediate maturity.

### Stylized Facts
1. Yields are persistent (near unit root) but mean-reverting.
2. The yield curve shifts roughly in parallel (level factor explains ~85% of variation).
3. Slope and curvature factors explain most of the remaining variation.
4. The spread (10Y - 2Y) predicts recessions and future economic activity.
5. Term premia are time-varying and countercyclical.

## Nelson-Siegel Model (1987)

A parsimonious 4-parameter model for the yield curve:

y(tau) = beta_0 + beta_1 * [(1 - exp(-tau/lambda)) / (tau/lambda)]
         + beta_2 * [(1 - exp(-tau/lambda)) / (tau/lambda) - exp(-tau/lambda)]

where tau = T - t is time to maturity.

**Factor interpretation**:
- beta_0: level (long-term rate). Loading = 1 for all maturities.
- beta_1: slope (short vs long). Loading decays from 1 to 0.
- beta_2: curvature (hump). Loading starts at 0, peaks at medium maturity, returns to 0.
- lambda: decay parameter controlling where the hump peaks.

### Svensson Extension (1994)

Adds a second curvature factor:

y(tau) = beta_0 + beta_1 * L1(tau, lambda_1) + beta_2 * L2(tau, lambda_1) + beta_3 * L2(tau, lambda_2)

Two decay parameters (lambda_1, lambda_2) allow richer curvature shapes. Used by many central banks.

### Estimation

```python
import numpy as np
from scipy.optimize import minimize

def nelson_siegel(tau, beta0, beta1, beta2, lam):
    """Nelson-Siegel yield curve."""
    x = tau / lam
    factor1 = (1 - np.exp(-x)) / x
    factor2 = factor1 - np.exp(-x)
    return beta0 + beta1 * factor1 + beta2 * factor2

def fit_ns(maturities, yields):
    """Fit Nelson-Siegel to observed yields."""
    def objective(params):
        beta0, beta1, beta2, lam = params
        fitted = nelson_siegel(maturities, beta0, beta1, beta2, lam)
        return np.sum((yields - fitted) ** 2)

    # Initial guess
    x0 = [yields[-1], yields[0] - yields[-1], 0.0, 1.5]
    bounds = [(-5, 20), (-20, 20), (-20, 20), (0.1, 10)]
    result = minimize(objective, x0, bounds=bounds, method='L-BFGS-B')
    return result.x
```

### Dynamic Nelson-Siegel (Diebold-Li, 2006)

Treat beta_0, beta_1, beta_2 as time-varying latent factors following a VAR(1):

[beta_0t]     [mu]       [beta_{0,t-1} - mu]
[beta_1t]  =  [mu]  + A * [beta_{1,t-1} - mu]  + eta_t
[beta_2t]     [mu]       [beta_{2,t-1} - mu]

- Estimate via two-step (OLS cross-section + VAR on factors) or state-space (Kalman filter).
- Excellent out-of-sample forecasting performance.
- lambda is typically fixed at lambda = 0.0609 (Diebold-Li calibration).

## Short-Rate Models

### Vasicek (1977)

dr_t = kappa * (theta - r_t) * dt + sigma * dW_t

- Mean-reverting Ornstein-Uhlenbeck process.
- kappa: speed of mean reversion.
- theta: long-run mean of the short rate.
- sigma: volatility.
- Closed-form bond prices and yields.
- Allows negative rates (feature or bug depending on context).

**Bond price**: P(t,T) = A(t,T) * exp(-B(t,T) * r_t)

where B(t,T) = (1 - exp(-kappa*(T-t))) / kappa

### Cox-Ingersoll-Ross (CIR, 1985)

dr_t = kappa * (theta - r_t) * dt + sigma * sqrt(r_t) * dW_t

- Square root diffusion ensures r_t >= 0 (if 2*kappa*theta >= sigma^2, Feller condition).
- Closed-form bond prices.
- Volatility proportional to sqrt(r), capturing the empirical feature that rate volatility increases with level.

### Hull-White (1990)

dr_t = [theta(t) - a * r_t] * dt + sigma * dW_t

- Time-dependent theta(t) allows exact fit to the initial yield curve.
- Analytically tractable.
- Widely used in practice for derivatives pricing.

### Calibration

Short-rate models are calibrated to:
1. **Yield curve**: Match observed zero-coupon yields.
2. **Caps/swaptions**: Match observed option prices (for implied volatility).
3. **Historical dynamics**: Estimate kappa, theta, sigma from historical rate data.

```python
# Vasicek calibration from historical data (maximum likelihood)
from scipy.optimize import minimize

def vasicek_loglik(params, rates, dt):
    """Log-likelihood for discretized Vasicek."""
    kappa, theta, sigma = params
    n = len(rates) - 1
    mu = theta + (rates[:-1] - theta) * np.exp(-kappa * dt)
    var = (sigma**2 / (2 * kappa)) * (1 - np.exp(-2 * kappa * dt))
    ll = -0.5 * n * np.log(2 * np.pi * var) - 0.5 * np.sum((rates[1:] - mu)**2 / var)
    return -ll  # minimize negative log-likelihood

result = minimize(vasicek_loglik, x0=[0.5, 0.05, 0.01], args=(rates, 1/252),
                  bounds=[(0.01, 5), (-0.05, 0.20), (0.001, 0.10)])
```

## HJM Framework (Heath-Jarrow-Morton, 1992)

Models the entire forward rate curve f(t,T) directly:

df(t,T) = alpha(t,T) * dt + sigma(t,T) * dW_t

**No-arbitrage drift restriction**: Under Q, the drift is fully determined by the volatility:

alpha(t,T) = sigma(t,T) * integral_{t}^{T} sigma(t,s) ds

Key insight: specifying the volatility structure sigma(t,T) fully determines the model.

### LIBOR Market Model (BGM)

A discrete-tenor version of HJM that models forward LIBOR rates directly. Standard for pricing interest rate derivatives (caps, floors, swaptions).

## Affine Term Structure Models (ATSMs)

General class encompassing Vasicek, CIR, and multi-factor extensions:

The short rate is an affine function of latent state variables X_t:
r_t = delta_0 + delta_1' * X_t

State dynamics under Q:
dX_t = K^Q * (theta^Q - X_t) * dt + Sigma * sqrt(S_t) * dW_t^Q

Bond prices are exponential-affine in the state:
P(t,T) = exp(A(T-t) + B(T-t)' * X_t)

where A and B solve ODEs (Riccati equations).

### Estimation Methods
- **Maximum likelihood** with Kalman filter: treat yields as noisy observations of latent factors.
- **GMM**: match yield moments (means, variances, autocorrelations).
- **Bayesian MCMC**: increasingly common for rich model specifications.

## Term Premium Estimation

### Adrian-Crump-Moench (ACM, 2013)

Widely used term premium decomposition (New York Fed publishes estimates):
1. Extract principal components from the yield curve.
2. Estimate factor dynamics and market prices of risk.
3. Decompose yield into expected future short rates + term premium.

### Kim-Wright (2005)

Three-factor Gaussian ATSM estimated at the Federal Reserve Board. Also produces term premium estimates.

### Cochrane-Piazzesi (2005)

A single return-forecasting factor (tent-shaped linear combination of forward rates) predicts excess bond returns across maturities. Suggests a single risk premium drives bond risk premia at all maturities.

## Bond Pricing

### Duration and Convexity

**Modified duration**: D = -(1/P) * dP/dy. Measures price sensitivity to yield changes.

**Convexity**: C = (1/P) * d^2P/dy^2. Captures the curvature of price-yield relationship.

**Approximation**: Delta_P/P ~ -D * Delta_y + 0.5 * C * (Delta_y)^2

### Credit Spreads

Corporate bond yield = risk-free yield + credit spread.

Credit spread reflects: default probability, loss given default, liquidity premium, and systematic risk.

Structural models (Merton 1974): equity is a call option on firm assets. Default occurs when assets fall below debt.

Reduced-form models (Duffie-Singleton 1999): model default intensity directly as a stochastic process.

## Practical Checklist

1. Start with Nelson-Siegel for cross-sectional curve fitting. Extract level, slope, curvature factors.
2. For forecasting: Dynamic Nelson-Siegel (Diebold-Li) is hard to beat.
3. For derivative pricing: use no-arbitrage models (Hull-White, HJM/LMM).
4. For term premium estimation: cite ACM or Kim-Wright; discuss limitations of any decomposition.
5. Always report the maturity spectrum used (e.g., 3M, 6M, 1Y, 2Y, 5Y, 7Y, 10Y, 30Y).
6. Distinguish between nominal and real yields (TIPS for real, breakeven = nominal - real ~ expected inflation + inflation risk premium).
7. Data sources: FRED (Treasury constant maturity rates), Bloomberg, Gurkaynak-Sack-Wright (2007) smoothed yields.
8. Test for unit roots in yields before running predictive regressions.
9. For panel studies: use Driscoll-Kraay or two-way clustered standard errors.
10. Report out-of-sample forecasting performance against random walk benchmark.

## Key References

- Nelson, C.R. and Siegel, A.F. (1987). Parsimonious modeling of yield curves. Journal of Business.
- Diebold, F.X. and Li, C. (2006). Forecasting the term structure of government bond yields. Journal of Econometrics.
- Vasicek, O. (1977). An equilibrium characterization of the term structure. Journal of Financial Economics.
- Cox, J.C., Ingersoll, J.E., and Ross, S.A. (1985). A theory of the term structure of interest rates. Econometrica.
- Heath, D., Jarrow, R., and Morton, A. (1992). Bond pricing and the term structure of interest rates. Econometrica.
- Adrian, T., Crump, R.K., and Moench, E. (2013). Pricing the term structure with linear regressions. Journal of Financial Economics.
- Cochrane, J.H. and Piazzesi, M. (2005). Bond risk premia. American Economic Review.
- Gurkaynak, R.S., Sack, B., and Wright, J.H. (2007). The U.S. Treasury yield curve: 1961 to the present. Journal of Monetary Economics.
