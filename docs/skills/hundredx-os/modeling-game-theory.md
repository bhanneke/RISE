<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/modeling-game-theory.md -->

# `game-theory`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

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


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/modeling/game-theory.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>modeling</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>formal-modeling</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/modeling-game-theory/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
