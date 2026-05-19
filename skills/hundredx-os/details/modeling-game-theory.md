# Game Theory for Platform Economics & IS Research

## Scope

This skill covers game theory as used in IS and platform economics research:
strategic interaction in platform markets, mechanism design for digital systems,
auction theory, and computational methods for verifying equilibria.

## Core Concepts

### Normal Form Game
- Players N, strategy sets S_i, payoff functions u_i(s_1, ..., s_n)
- Nash equilibrium: no player can unilaterally improve payoff
- Mixed strategy NE: players randomize; indifference across support

### Solution Concepts (strongest to weakest)
1. Dominant strategy equilibrium
2. Iterated elimination of dominated strategies
3. Nash equilibrium (pure or mixed)
4. Subgame perfect equilibrium (sequential games)
5. Perfect Bayesian equilibrium (incomplete information)

## Platform-Relevant Models

### Two-Sided Markets
- Platform sets fees (f_b, f_s) to buyers and sellers
- Network effects: utility increases with participation on the other side
- Key trade-off: subsidize one side to attract the other (Rochet-Tirole 2003)
- Equilibrium: solve for participation thresholds on each side given fees

### Platform Competition
- Cournot/Bertrand adapted for platforms: compete on fees, features, or quality
- Multi-homing vs single-homing affects competitive dynamics
- Winner-take-all vs market sharing depends on differentiation and multi-homing

### Token Mechanism Design
- Token as coordination device: participation thresholds, staking equilibria
- ICO/token sale as mechanism: price discovery, adverse selection
- Governance tokens: voting games, delegation, whale capture

## Mechanism Design

- **Social choice function** f: type profiles -> outcomes
- **Revelation principle**: any implementable outcome achievable by direct
  truthful mechanism
- **IC (incentive compatibility)**: truth-telling is equilibrium
  - DSIC: dominant strategy IC (strongest)
  - BIC: Bayesian IC
- **IR (individual rationality)**: participation constraint
- **VCG mechanism**: DSIC for efficient allocation; each agent pays
  externality imposed on others

### Key Impossibility Results
- Gibbard-Satterthwaite: with 3+ alternatives, only DSIC+onto mechanism is
  dictatorship
- Myerson-Satterthwaite: no efficient+IC+IR+budget-balanced bilateral trade

## Auction Theory

### Standard Formats
- **First-price sealed-bid**: b(v) = v - integral [F(t)/F(v)]^(n-1) dt
- **Second-price (Vickrey)**: b(v) = v (dominant strategy)
- **All-pay**: b(v) = integral t*(n-1)*F(t)^(n-2)*f(t) dt
- Revenue equivalence: same expected revenue across standard formats (IPV)

### Relevance for IS
- NFT auctions, DeFi liquidation auctions, ad auctions
- Combinatorial auctions for spectrum/cloud resources
- Dynamic pricing as mechanism

## Computational Methods

### Nash Equilibrium Computation

**Support enumeration (2-player, small games):**
Enumerate support pairs, solve indifference conditions, verify no profitable
deviations. Complexity O(2^(n+m)) -- only for small games.

```python
import nashpy
game = nashpy.Game(A, B)  # payoff matrices
equilibria = list(game.support_enumeration())
```

**Fictitious play:** Converges for 2x2, zero-sum, potential games, strategic
complements. Does NOT converge for all games.

**Backward induction:** Recursive solution for finite extensive-form games
with perfect information.

### Verification Checklist

For any computed equilibrium, verify:
1. **Best response**: no unilateral deviation improves payoff
2. **Probability constraints**: sigma >= 0, sum = 1
3. **Support condition**: strategies in support yield equal expected payoffs
4. **Indifference**: strategies outside support yield weakly lower payoffs

### Common Pitfalls
- Multiple equilibria: always search for all NE
- Numerical precision: use tolerance (1e-8) for equality checks
- Mixed strategies: ensure probabilities sum to 1
- Dynamic games: verify subgame perfection in ALL subgames
