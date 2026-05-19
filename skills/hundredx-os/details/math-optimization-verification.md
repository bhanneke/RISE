# Optimization Verification

## Overview

This skill covers computational verification of optimization problems:
KKT conditions, second-order conditions, comparative statics, and economic
applications. All code should be self-contained Python using numpy, scipy, sympy.

## KKT Condition Verification

### Structure

For the problem:
```
max f(x)
s.t. g_j(x) <= 0,  j = 1, ..., m
     h_k(x) = 0,  k = 1, ..., p
```

The KKT conditions are:
1. **Stationarity**: nabla f(x*) = sum_j lambda_j * nabla g_j(x*) + sum_k mu_k * nabla h_k(x*)
2. **Primal feasibility**: g_j(x*) <= 0, h_k(x*) = 0
3. **Dual feasibility**: lambda_j >= 0
4. **Complementary slackness**: lambda_j * g_j(x*) = 0

### Numerical Verification

```python
import numpy as np
from scipy.optimize import minimize

def verify_kkt(x_star, f, g_list, h_list, lambda_star, mu_star, epsilon=1e-6):
    """Verify KKT conditions at a candidate solution."""
    n = len(x_star)

    # 1. Stationarity: check gradient condition numerically
    grad_f = numerical_gradient(f, x_star)
    grad_constraint_sum = np.zeros(n)
    for j, (g_j, lam_j) in enumerate(zip(g_list, lambda_star)):
        grad_constraint_sum += lam_j * numerical_gradient(g_j, x_star)
    for k, (h_k, mu_k) in enumerate(zip(h_list, mu_star)):
        grad_constraint_sum += mu_k * numerical_gradient(h_k, x_star)

    stationarity_error = np.linalg.norm(grad_f - grad_constraint_sum)

    # 2. Primal feasibility
    primal_viol = max(max(g_j(x_star) for g_j in g_list) if g_list else 0,
                      max(abs(h_k(x_star)) for h_k in h_list) if h_list else 0)

    # 3. Dual feasibility
    dual_feasible = all(lam >= -epsilon for lam in lambda_star)

    # 4. Complementary slackness
    cs_error = max(abs(lam * g_j(x_star))
                   for lam, g_j in zip(lambda_star, g_list)) if g_list else 0

    return {
        "stationarity_error": stationarity_error,
        "primal_violation": primal_viol,
        "dual_feasible": dual_feasible,
        "complementary_slackness_error": cs_error,
        "is_kkt": (stationarity_error < epsilon and
                   primal_viol < epsilon and
                   dual_feasible and
                   cs_error < epsilon),
    }
```

### Symbolic Verification

```python
import sympy as sp

def verify_kkt_symbolic(f, constraints_ineq, constraints_eq, variables):
    """Verify KKT using SymPy Lagrangian."""
    # Create multipliers
    lambdas = [sp.Symbol(f'lambda_{j}', nonneg=True)
               for j in range(len(constraints_ineq))]
    mus = [sp.Symbol(f'mu_{k}') for k in range(len(constraints_eq))]

    # Form Lagrangian
    L = f
    for lam, g in zip(lambdas, constraints_ineq):
        L -= lam * g
    for mu, h in zip(mus, constraints_eq):
        L -= mu * h

    # Stationarity: dL/dx_i = 0
    stationarity = [sp.diff(L, x) for x in variables]

    # Solve the full system
    system = stationarity + constraints_eq + [lam * g for lam, g in zip(lambdas, constraints_ineq)]
    solutions = sp.solve(system, variables + lambdas + mus, dict=True)

    return solutions
```

## Second-Order Conditions

### Bordered Hessian

For constrained optimization with equality constraints:

```
The bordered Hessian is:
    | 0    ... 0    dg1/dx1 ... dg1/dxn |
    | :         :   :            :       |
    | 0    ... 0    dgm/dx1 ... dgm/dxn |
    | dg1/dx1 ...   d2L/dx1dx1  ...      |
    | :              :                    |
    | dgm/dxn ...           d2L/dxndxn   |

For maximization with m equality constraints:
- Check signs of last (n-m) leading principal minors of bordered Hessian
- They should alternate in sign, starting with (-1)^(m+1) > 0

For minimization: signs should all be (-1)^m times the above
```

### Implementation

```python
def bordered_hessian(L, g_list, variables):
    """Compute the bordered Hessian symbolically."""
    n = len(variables)
    m = len(g_list)

    # Build the bordered Hessian matrix
    BH = sp.zeros(m + n, m + n)

    # Top-left block: zeros
    # Top-right and bottom-left: constraint gradients
    for i, g in enumerate(g_list):
        for j, x in enumerate(variables):
            dg = sp.diff(g, x)
            BH[i, m + j] = dg
            BH[m + j, i] = dg

    # Bottom-right block: Hessian of Lagrangian
    for i, xi in enumerate(variables):
        for j, xj in enumerate(variables):
            BH[m + i, m + j] = sp.diff(L, xi, xj)

    return BH

def check_soc_max(BH, m, n):
    """Check second-order conditions for maximization."""
    # Check last (n-m) leading principal minors
    passed = True
    for k in range(1, n - m + 1):
        size = 2 * m + k
        minor = BH[:size, :size].det()
        expected_sign = (-1)**(m + k)
        if sp.sign(minor) != expected_sign:
            passed = False
    return passed
```

### Convexity via Eigenvalues

```python
def verify_convexity(f, variables, test_points, epsilon=1e-8):
    """Numerically verify convexity by checking Hessian eigenvalues."""
    f_lambda = sp.lambdify(variables, f, 'numpy')

    # Compute numerical Hessian at each test point
    for point in test_points:
        H = numerical_hessian(f_lambda, point)
        eigenvalues = np.linalg.eigvalsh(H)
        if np.min(eigenvalues) < -epsilon:
            return False, point, eigenvalues
    return True, None, None
```

## Comparative Statics

### Implicit Function Theorem

For a system F(x, theta) = 0 where x is endogenous and theta is a parameter:

```
dx/d(theta) = -[dF/dx]^{-1} * [dF/d(theta)]
```

### Implementation

```python
def comparative_statics_imt(F_system, x_vars, theta_vars, equilibrium):
    """Compute comparative statics using the Implicit Function Theorem."""
    # Jacobian w.r.t. endogenous variables
    J_x = sp.Matrix([
        [sp.diff(F, x) for x in x_vars]
        for F in F_system
    ])

    # Jacobian w.r.t. parameters
    J_theta = sp.Matrix([
        [sp.diff(F, t) for t in theta_vars]
        for F in F_system
    ])

    # dx/dtheta = -J_x^{-1} * J_theta
    dx_dtheta = -J_x.inv() * J_theta

    # Evaluate at equilibrium
    dx_dtheta_eval = dx_dtheta.subs(equilibrium)

    return dx_dtheta_eval
```

### Envelope Theorem

For the value function V(theta) = max_x f(x, theta) s.t. g(x, theta) <= 0:

```
dV/d(theta) = dL/d(theta)|_{x=x*(theta)}
            = df/d(theta) + sum_j lambda_j * dg_j/d(theta)  evaluated at optimum
```

```python
def envelope_theorem(f, constraints, multipliers, theta, x_star_subs):
    """Compute dV/dtheta using the envelope theorem."""
    L = f
    for lam, g in zip(multipliers, constraints):
        L -= lam * g

    dV_dtheta = sp.diff(L, theta).subs(x_star_subs)
    return sp.simplify(dV_dtheta)
```

## Economic Applications

### Consumer Optimization

```
max u(x1, x2, ..., xn)
s.t. p1*x1 + p2*x2 + ... + pn*xn <= I
     x_i >= 0

Marshallian demand: x_i*(p, I)
Indirect utility: V(p, I) = u(x*(p, I))
Roy's identity: x_i*(p, I) = -(dV/dp_i) / (dV/dI)

Verification:
1. Check adding-up: sum(p_i * x_i*) = I (Walras' law)
2. Check homogeneity of degree 0 in (p, I)
3. Check Slutsky symmetry and negative semi-definiteness
4. Check Roy's identity holds
```

### Producer Optimization

```
max p*f(K, L) - r*K - w*L    (profit maximization)
min r*K + w*L s.t. f(K, L) >= q  (cost minimization)

Verification:
1. FOC: p * MP_K = r, p * MP_L = w
2. SOC: Hessian of profit function is negative semi-definite
3. Shephard's lemma: dC/dr = K*(r,w,q), dC/dw = L*(r,w,q)
4. Cost function is concave in (r, w)
```

### Mechanism Design IC/IR Constraints

```
Incentive Compatibility (IC):
u_i(theta_i, theta_i) >= u_i(theta_i', theta_i) for all theta_i, theta_i'

Individual Rationality (IR):
u_i(theta_i, theta_i) >= u_bar_i for all theta_i

Verification:
1. Check IC pairwise for all type pairs
2. Check IR for all types
3. For continuous types: check the envelope condition
   U'(theta) = du/dtheta(x(theta), theta) and U''(theta) is appropriate sign
4. Revenue equivalence: two mechanisms with same allocation rule
   yield the same expected revenue (up to a constant)
```

## Verification Output Format

When verifying optimization results, report:

```
============================================
OPTIMIZATION PROBLEM: [description]
============================================

CANDIDATE SOLUTION: x* = [values]
OBJECTIVE VALUE: f(x*) = [value]

KKT CONDITIONS:
  Stationarity error: [value]
  Primal feasibility: [satisfied/violated]
  Dual feasibility: [satisfied/violated]
  Complementary slackness: [satisfied/violated]

SECOND-ORDER CONDITIONS:
  Hessian eigenvalues: [values]
  [Definite/Semi-definite/Indefinite]

COMPARATIVE STATICS:
  dx*/d(param) = [values and signs]

============================================
VERDICT: OPTIMAL / NOT OPTIMAL / INCONCLUSIVE
============================================
```
