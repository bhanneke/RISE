# Market Microstructure

## Overview

Market microstructure studies how the mechanics of trading — order flow, dealer behavior, information asymmetry, and market design — affect price formation, liquidity, and transaction costs. It bridges financial theory (efficient markets, rational expectations) with the institutional reality of how markets operate.

## Liquidity Measures

### Bid-Ask Spread

The most direct measure of transaction costs and a proxy for information asymmetry.

**Quoted spread**: Ask - Bid. The cost of an immediate round-trip trade.

**Relative (percentage) spread**: (Ask - Bid) / Midpoint * 100.

**Effective spread**: 2 * |Trade Price - Midpoint| * D, where D = +1 for buyer-initiated trades, -1 for seller-initiated. Captures actual execution quality (which may be better or worse than the quoted spread).

**Realized spread**: 2 * D * (Trade Price - Midpoint_{t+delta}) / Midpoint. Measures the dealer's revenue after a time interval delta. The difference between effective and realized spread is the price impact component.

### Trade Classification

**Lee-Ready (1991)**: Classify trades as buyer- or seller-initiated.
1. If trade price > midpoint → buy. If < midpoint → sell.
2. If at midpoint → use tick test: if price > previous price → buy (uptick), if < → sell.

### Amihud (2002) Illiquidity Ratio

ILLIQ_i = (1/D_i) * Sum(|R_id| / DVOL_id)

- |R_id|: absolute daily return.
- DVOL_id: daily dollar volume.
- Average ratio of absolute return to dollar volume.
- Higher = more illiquid (prices move more per unit of trading).
- Widely used because it only requires daily return and volume data.

```python
def amihud_illiquidity(returns, dollar_volume, min_days=15):
    """Compute Amihud illiquidity ratio."""
    valid = (dollar_volume > 0) & returns.notna()
    if valid.sum() < min_days:
        return np.nan
    ratio = np.abs(returns[valid]) / dollar_volume[valid]
    return ratio.mean() * 1e6  # scale for readability
```

### Roll (1984) Effective Spread Estimate

Estimated from serial covariance of price changes:

Spread_Roll = 2 * sqrt(-Cov(Delta_P_t, Delta_P_{t-1}))

- Only valid when serial covariance is negative.
- Assumes bid-ask bounce is the sole source of negative autocorrelation.

### Corwin-Schultz (2012) High-Low Spread Estimator

Estimates effective spread from daily high and low prices:

S = (2 * (exp(alpha) - 1)) / (1 + exp(alpha))

where alpha is derived from the ratio of two-day and one-day high-low ranges. Intuition: the high (low) is more likely to be a buy (sell), so the high-low range reflects both volatility and the spread.

### Pastor-Stambaugh (2003) Liquidity Factor

Measures return reversal following high-volume days (a signed volume effect):

r_{i,t+1}^e = theta_i + phi_i * r_{i,t} + gamma_i * sign(r_{i,t}^e) * v_{i,t} + epsilon_{i,t+1}

- gamma_i measures illiquidity: more negative gamma → more illiquid (larger reversals after volume).
- Aggregate the gammas into a market-wide liquidity measure.
- Innovations in aggregate liquidity are a priced risk factor.

## Information Asymmetry Models

### Kyle (1985) Model

Single informed trader, noise traders, and a market maker.

Key result: **Kyle's lambda** measures price impact:

Delta_P = lambda * (Order Flow)

- lambda = sigma_v / (2 * sigma_u) where sigma_v = std of asset value innovation, sigma_u = std of noise trading.
- Higher lambda = more information asymmetry and less liquidity.

### Estimation of Price Impact (Kyle Lambda)

Regress price changes on signed order flow:

Delta_P_t = c + lambda * OF_t + epsilon_t

where OF = sum of signed trades (buyer-initiated minus seller-initiated volume).

```python
import statsmodels.api as sm

# Using 5-minute intervals
model = sm.OLS(price_changes, sm.add_constant(signed_order_flow)).fit(cov_type='HAC',
    cov_kwds={'maxlags': 5})
kyle_lambda = model.params[1]
```

### Glosten-Milgrom (1985)

Sequential trade model with Bayesian updating.
- Market maker sets bid and ask to break even in expectation.
- Spread reflects adverse selection cost (informed traders) offset by profits from noise traders.
- Wider spread when information asymmetry is higher.

### PIN Model (Easley-Kiefer-O'Hara-Paperman, 1996)

Probability of Informed Trading:

PIN = (alpha * mu) / (alpha * mu + 2 * epsilon)

- alpha: probability of an information event.
- mu: arrival rate of informed trades.
- epsilon: arrival rate of uninformed buy/sell trades.
- Estimated via maximum likelihood on daily buy/sell counts.

High PIN → high information asymmetry.

```python
# PIN estimation requires MLE on the likelihood:
# L = Product over days of:
#   (1-alpha)*P(B|eps)*P(S|eps) + alpha*delta*P(B|eps+mu)*P(S|eps) + alpha*(1-delta)*P(B|eps)*P(S|eps+mu)
# where P(.) are Poisson probabilities
# Typically use numerical optimization (e.g., scipy.optimize.minimize)
```

### VPIN (Volume-Synchronized PIN)

Real-time version of PIN using volume buckets instead of time intervals. Bulk-classifies trades using the BVC (Bulk Volume Classification) algorithm. Easier to compute than traditional PIN.

## Bid-Ask Spread Decomposition

The spread has three components:
1. **Order processing costs**: physical costs of executing trades.
2. **Inventory holding costs**: compensation for bearing inventory risk.
3. **Adverse selection costs**: protection against informed traders.

### Huang-Stoll (1997) Decomposition

Decomposes the effective spread into:
- Adverse selection component (pi)
- Inventory component (1 - pi - phi)
- Order processing component (phi)

Using a regression of trade-to-trade price changes on trade indicators.

### Lin-Sanger-Booth (1995)

Decomposes the effective half-spread:
- Adverse selection = lambda = permanent price impact of a trade.
- Transitory component = 1 - lambda = temporary price effect (reverts).

## Realized Volatility and High-Frequency Data

### Realized Variance

RV_t = Sum(r_{t,i}^2) for i = 1 to M

where r_{t,i} are intraday returns sampled at frequency 1/M (e.g., 5-minute returns).

- Consistent estimator of integrated variance as sampling frequency increases.
- But: microstructure noise (bid-ask bounce) biases RV upward at high frequencies.

### Optimal Sampling Frequency
- **Signature plot**: Plot RV as a function of sampling frequency. RV increases at very high frequencies (noise) and stabilizes at moderate frequencies.
- **5-minute rule of thumb**: 5-minute sampling often balances noise and information.
- **Kernel-based estimators**: Barndorff-Nielsen et al. (2008) realized kernel handles noise.
- **Two-scale estimator**: Zhang-Mykland-Ait-Sahalia (2005) — combines fast and slow scale RV.

### Realized Volatility Variants

**Bipower variation**: BV = (pi/2) * Sum(|r_{t,i}| * |r_{t,i-1}|). Robust to jumps.

**Jump detection**: RV - BV estimates the jump component. Test significance via Barndorff-Nielsen-Shephard (2006) z-test.

**Realized semivariance**: Separate upside and downside realized variance. Captures asymmetric risk.

```python
def realized_variance(intraday_returns):
    """Compute realized variance from intraday returns."""
    return np.sum(intraday_returns ** 2)

def bipower_variation(intraday_returns):
    """Bipower variation (robust to jumps)."""
    abs_ret = np.abs(intraday_returns)
    return (np.pi / 2) * np.sum(abs_ret[1:] * abs_ret[:-1])
```

## Market Design and Structure

### Order Types
- **Market order**: execute immediately at best available price. Demands liquidity.
- **Limit order**: execute only at specified price or better. Supplies liquidity.
- **Stop order**: becomes market order when price reaches trigger.

### Market Types
- **Continuous limit order book (CLOB)**: orders match continuously (most equity exchanges).
- **Call auction**: orders accumulate and clear at a single price (opening/closing auctions).
- **Dealer market**: quotes provided by designated market makers (OTC bonds, forex).
- **Dark pools**: non-displayed liquidity venues for institutional block trades.

### Market Quality Metrics
- Depth: volume available at best bid and ask.
- Resilience: speed at which depth replenishes after a large trade.
- Tightness: bid-ask spread.
- Immediacy: speed of execution.

## Practical Checklist

1. Choose liquidity measure appropriate to data availability:
   - Daily data only: Amihud, Roll, Corwin-Schultz.
   - TAQ/tick data: quoted/effective spread, realized spread, Kyle lambda, PIN.
2. For cross-sectional studies: Amihud illiquidity is the workhorse (requires only CRSP daily data).
3. For time-series liquidity risk: Pastor-Stambaugh or innovations in Amihud.
4. When using TAQ data: apply standard filters (Lee-Ready for trade classification, exclude trades outside NBBO, handle pre/post-market).
5. For high-frequency analysis: choose sampling frequency carefully (signature plot). Consider noise-robust estimators.
6. Report both quoted and effective spreads. Effective spread is the better measure of actual trading costs.
7. PIN estimation is numerically fragile. Use multiple starting values and check for boundary solutions.
8. For market microstructure event studies (e.g., effect of regulation on spreads): use panel regression with time and stock fixed effects.
9. Account for intraday patterns (U-shaped spread pattern: wider at open/close).
10. Discuss whether results are driven by market microstructure artifacts vs genuine economic effects.

## Key References

- Kyle, A.S. (1985). Continuous auctions and insider trading. Econometrica.
- Glosten, L.R. and Milgrom, P.R. (1985). Bid, ask and transaction prices. Journal of Financial Economics.
- Amihud, Y. (2002). Illiquidity and stock returns. Journal of Financial Markets.
- Pastor, L. and Stambaugh, R.F. (2003). Liquidity risk and expected stock returns. Journal of Political Economy.
- Easley, D., Kiefer, N.M., O'Hara, M., and Paperman, J.B. (1996). Liquidity, information, and infrequently traded stocks. Journal of Finance.
- Roll, R. (1984). A simple implicit measure of the effective bid-ask spread. Journal of Finance.
- Lee, C.M.C. and Ready, M.J. (1991). Inferring trade direction from intraday data. Journal of Finance.
- Corwin, S.A. and Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. Journal of Finance.
- Huang, R.D. and Stoll, H.R. (1997). The components of the bid-ask spread. Review of Financial Studies.
- O'Hara, M. (1995). Market Microstructure Theory. Blackwell.
