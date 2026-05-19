# Mathematical Proof Strategies

## Overview

This skill guides the selection and implementation of computational proof methods.
The goal is to translate mathematical propositions into self-contained Python scripts
that produce a clear VERDICT: PROVED, DISPROVED, or INCONCLUSIVE.

## Proof Method Selection

### When to Use Monte Carlo Simulation

Use Monte Carlo when:
- The proposition involves probabilistic statements (expectations, variances, convergence in probability)
- Analytical solutions are intractable or unknown
- The parameter space is high-dimensional
- You need to verify a theoretical result numerically

Do NOT use Monte Carlo when:
- An exact symbolic proof is feasible (use SymPy instead)
- The proposition is about worst-case behavior (Monte Carlo finds average cases)
- The required precision is extreme (convergence is O(1/sqrt(N)))

#### Implementation Guide

```
Sample Size Selection:
- Quick check: N = 10,000
- Standard verification: N = 100,000
- High-confidence: N = 1,000,000
- Always report the standard error

Convergence Diagnostics:
- Run multiple independent replications (e.g., 10 runs of N/10)
- Plot running mean to verify stabilization
- Report 95% confidence interval: mean +/- 1.96 * (std / sqrt(N))
- If CI does not exclude the threshold, report INCONCLUSIVE

Variance Reduction Techniques:
- Antithetic variates: pair (U, 1-U) to reduce variance
- Control variates: subtract correlated known-mean variable
- Importance sampling: reweight samples from a better distribution
- Stratified sampling: partition the domain, sample within each stratum

Reproducibility:
- Always set np.random.seed(42) at the top
- Report the seed in output
```

### When to Use Symbolic Computation (SymPy)

Use SymPy when:
- The proposition involves algebraic identities
- You need to verify limits, series expansions, or integrals
- The proposition is about convergence of sequences or series
- Inequality verification via simplification is feasible

#### Implementation Guide

```
Key SymPy Functions:
- sympy.simplify(expr1 - expr2) == 0   # Identity verification
- sympy.limit(expr, x, val)            # Limit evaluation
- sympy.series(expr, x, n=k)           # Taylor expansion
- sympy.integrate(expr, (x, a, b))     # Definite integrals
- sympy.solve(expr, x)                 # Equation solving
- sympy.diff(expr, x)                  # Differentiation
- sympy.summation(expr, (n, 0, oo))    # Series summation

Proving Inequalities:
1. Let d = LHS - RHS
2. Try sympy.simplify(d) to see if it reduces to a known sign
3. Try sympy.minimum(d, x, domain=S.Reals) to find the minimum
4. If minimum >= 0, the inequality holds
5. For conditional inequalities, substitute boundary values

Limitations:
- SymPy cannot always determine the sign of complex expressions
- Numeric verification with mpmath can complement symbolic results
- For transcendental expressions, use interval arithmetic via mpmath.iv
```

### When to Use Numerical Optimization

Use numerical methods when:
- The proposition involves optimization (min, max, saddle points)
- KKT conditions need verification
- You need to verify convexity, concavity, or quasi-concavity
- Game-theoretic equilibrium existence is the question

#### Implementation Guide

```
Optimization Tools:
- scipy.optimize.minimize    # Unconstrained and constrained minimization
- scipy.optimize.linprog     # Linear programming
- scipy.optimize.root        # System of nonlinear equations
- scipy.optimize.fsolve      # Legacy nonlinear solver

For Verification of Optima:
1. Find candidate via optimization
2. Check first-order conditions (gradient = 0 or KKT)
3. Check second-order conditions (Hessian positive/negative definite)
4. Perturb the solution: verify objective worsens in all directions
5. Try multiple starting points to check for multiple optima

Convexity Verification:
1. Compute the Hessian numerically at multiple points
2. Check eigenvalues: all non-negative => convex
3. For quasi-convexity: check that sublevel sets are convex
```

## Output Format

Every proof script MUST produce this output format:

```
============================================
PROPOSITION: [statement in plain English]
METHOD: [Monte Carlo / Symbolic / Numerical / Mixed]
============================================

[Results section with numerical evidence]

============================================
VERDICT: PROVED | DISPROVED | INCONCLUSIVE
CONFIDENCE: [for Monte Carlo: p-value or CI; for symbolic: exact/verified]
LIMITATIONS: [any caveats]
============================================
```

## Code Quality Requirements

1. **Self-contained**: Only use numpy, scipy, sympy, matplotlib, itertools, functools
2. **Reproducible**: Set random seed, report all parameters
3. **Clear output**: Print VERDICT line that can be parsed programmatically
4. **Visualization**: Include at least one plot when Monte Carlo is used
5. **Error handling**: Catch numerical issues (overflow, NaN, singular matrices)
6. **Documentation**: Include docstring explaining the proposition and strategy

## Common Proof Patterns

### Verify an Identity: f(x) = g(x)

```python
# Symbolic: simplify f - g to 0
d = sympy.simplify(f_expr - g_expr)
assert d == 0, f"Difference is {d}"

# Numerical: sample random points, check |f(x) - g(x)| < epsilon
xs = np.random.uniform(-10, 10, 100000)
diffs = np.abs(f(xs) - g(xs))
assert np.all(diffs < 1e-10)
```

### Verify an Inequality: f(x) >= g(x) for all x in D

```python
# Try to find a counterexample via optimization
from scipy.optimize import minimize
result = minimize(lambda x: f(x) - g(x), x0=..., bounds=D)
if result.fun < -1e-10:
    print(f"COUNTEREXAMPLE at x={result.x}: f-g = {result.fun}")
    print("VERDICT: DISPROVED")
else:
    print(f"Minimum of f-g = {result.fun:.10f} >= 0")
    print("VERDICT: PROVED (numerically)")
```

### Verify Convergence: lim_{n->inf} a_n = L

```python
# Compute terms for increasing n
ns = [10**k for k in range(1, 8)]
terms = [a(n) for n in ns]
errors = [abs(t - L) for t in terms]

# Check if errors decrease toward 0
converging = all(errors[i+1] < errors[i] for i in range(len(errors)-1))
final_error = errors[-1]

if final_error < 1e-10 and converging:
    print("VERDICT: PROVED (numerical convergence)")
elif not converging:
    print("VERDICT: DISPROVED (not converging)")
else:
    print("VERDICT: INCONCLUSIVE")
```

### Verify a Probability Statement: P(X > c) = p

```python
np.random.seed(42)
N = 1_000_000
samples = generate_X(N)
empirical_p = np.mean(samples > c)
se = np.sqrt(empirical_p * (1 - empirical_p) / N)
ci = (empirical_p - 1.96 * se, empirical_p + 1.96 * se)

if ci[0] <= p <= ci[1]:
    print(f"VERDICT: PROVED (95% CI [{ci[0]:.6f}, {ci[1]:.6f}] contains {p})")
else:
    print(f"VERDICT: DISPROVED (95% CI [{ci[0]:.6f}, {ci[1]:.6f}] excludes {p})")
```

## Decision Tree

```
Is the proposition algebraic/symbolic?
  YES -> Try SymPy first, fall back to numerical if SymPy can't simplify
  NO  -> Continue

Is it about probabilities/expectations?
  YES -> Monte Carlo with variance reduction
  NO  -> Continue

Is it about optimization/equilibria?
  YES -> Numerical optimization + KKT verification
  NO  -> Continue

Is it about convergence?
  YES -> Numerical sequence computation + rate estimation
  NO  -> Mixed approach: symbolic + numerical verification
```
