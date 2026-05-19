# LaTeX Conventions for Economic Models

Guidelines for typesetting economic theory in LaTeX. Follow these conventions to
produce clean, readable, publication-quality mathematical economics.

## Preamble essentials

```latex
\usepackage{amsmath}      % Core math environments
\usepackage{amssymb}      % Additional math symbols
\usepackage{amsthm}       % Theorem environments
\usepackage{mathtools}    % Extensions to amsmath (dcases, coloneqq, etc.)
\usepackage{bbm}          % Blackboard bold for indicator functions: \mathbbm{1}
\usepackage{bm}           % Bold math symbols (for vectors if needed)
```

## Equation environments

### Single equations

Use `equation` for numbered, `equation*` for unnumbered. Never use `$$...$$`.

```latex
% Numbered equation (use when you will reference it)
\begin{equation}\label{eq:utility}
  U_i = \sum_{t=0}^{\infty} \beta^t u(c_{it})
\end{equation}

% Unnumbered (use sparingly; most equations in a theory paper should be numbered)
\begin{equation*}
  \pi_f = p \cdot q - C(q)
\end{equation*}
```

### Multi-line aligned equations

Use `align` for related equations that should be aligned (typically at `=` or
inequality signs). Use `aligned` inside `equation` when you want a single
equation number for the group.

```latex
% Multiple related equations, each numbered
\begin{align}
  \max_{c_t, k_{t+1}} \quad & \sum_{t=0}^{\infty} \beta^t u(c_t) \label{eq:objective} \\
  \text{s.t.} \quad & c_t + k_{t+1} = f(k_t) + (1-\delta) k_t \label{eq:budget} \\
                     & c_t \geq 0, \quad k_0 \text{ given} \label{eq:constraints}
\end{align}

% Single equation number for a system
\begin{equation}\label{eq:foc-system}
  \begin{aligned}
    u'(c_t) &= \beta u'(c_{t+1}) \bigl[ f'(k_{t+1}) + 1 - \delta \bigr] \\
    c_t + k_{t+1} &= f(k_t) + (1 - \delta) k_t
  \end{aligned}
\end{equation}
```

### Cases (piecewise functions)

Use `cases` from amsmath or `dcases` from mathtools (the latter provides
displaystyle inside cases, which looks better for fractions).

```latex
\begin{equation}\label{eq:tax-schedule}
  T(y) =
  \begin{dcases}
    0                          & \text{if } y \leq \bar{y} \\
    \tau (y - \bar{y})         & \text{if } y > \bar{y}
  \end{dcases}
\end{equation}
```

## Standard notation conventions

### Agents, goods, time

| Symbol | Convention | Example |
|--------|-----------|---------|
| `i, h` | Individual agents, households | $i \in \{1, \ldots, N\}$ |
| `f, j` | Firms | $f \in \{1, \ldots, F\}$ |
| `j, k` | Goods, sectors | $j \in \{1, \ldots, J\}$ |
| `t`    | Time period | $t = 0, 1, 2, \ldots$ |
| `s`    | State of the world | $s \in S$ |

### Core economic objects

```latex
% Preferences
u(\cdot)              % Utility function (lowercase)
U_i                   % Lifetime/indirect utility
\beta                 % Discount factor (0 < \beta < 1)
\delta                % Depreciation rate

% Prices and quantities
p_j                   % Price of good j
w                     % Wage
r                     % Interest rate / rental rate of capital
c_{it}                % Consumption of agent i at time t
k_t                   % Capital stock at time t
\ell_i                % Labor supply (use \ell, not l, to avoid confusion with 1)
y_i                   % Income of agent i
Y                     % Aggregate output (uppercase for aggregates)

% Production
f(k, \ell)            % Production function (lowercase)
F(K, L)               % Aggregate production function (uppercase)
A_t                   % Total factor productivity

% Probability and expectations
\Pr(\cdot)            % Probability
\mathbb{E}[\cdot]     % Expectation operator
\mathbb{E}_t[\cdot]   % Conditional expectation given info at t
\mathbb{V}[\cdot]     % Variance (use \operatorname{Var} as alternative)

% Sets
\mathbb{R}            % Real numbers
\mathbb{R}_+          % Non-negative reals
\mathbb{R}^n          % n-dimensional Euclidean space
\Delta^{n-1}          % Simplex (for mixed strategies, distributions)
```

### Operators and functions

Define custom operators in the preamble to get proper spacing:

```latex
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator{\Var}{Var}
\DeclareMathOperator{\Cov}{Cov}
\DeclareMathOperator{\Corr}{Corr}
\DeclareMathOperator{\plim}{plim}
\DeclareMathOperator{\tr}{tr}
\DeclareMathOperator{\diag}{diag}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\sgn}{sgn}
```

Usage:

```latex
x^* = \argmax_{x \in X} f(x)
```

### Indicator functions

```latex
\mathbbm{1}\{x > 0\}        % Preferred: blackboard bold 1
\mathbf{1}\{x > 0\}         % Alternative: bold 1
\mathbbm{1}_{x > 0}         % Subscript notation (also common)
```

## Optimization problems

Economics papers are full of optimization problems. Typeset them consistently:

```latex
% Consumer's problem
\begin{equation}\label{eq:consumer}
  \max_{\{c_t, \ell_t\}_{t=0}^{\infty}} \sum_{t=0}^{\infty}
    \beta^t u(c_t, 1 - \ell_t)
  \quad \text{s.t.} \quad
  c_t + a_{t+1} = (1+r_t) a_t + w_t \ell_t
\end{equation}

% Firm's problem (static)
\begin{equation}\label{eq:firm}
  \max_{K, L \geq 0} \; F(K, L) - rK - wL
\end{equation}

% Planner's problem with Lagrangian
\begin{equation}\label{eq:lagrangian}
  \mathcal{L} = \sum_{t=0}^{\infty} \beta^t
    \Bigl[ u(c_t) + \lambda_t \bigl( f(k_t) + (1-\delta)k_t - c_t - k_{t+1} \bigr) \Bigr]
\end{equation}
```

For multi-line constraints, use the `align` approach shown earlier.

## Equilibrium definitions

Use the `definition` environment from amsthm. Define it in the preamble:

```latex
\theoremstyle{definition}
\newtheorem{definition}{Definition}
\newtheorem{assumption}{Assumption}
\newtheorem{proposition}{Proposition}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{corollary}{Corollary}
\newtheorem{remark}{Remark}
\newtheorem{example}{Example}
```

### Competitive equilibrium

```latex
\begin{definition}[Competitive Equilibrium]\label{def:ce}
  A competitive equilibrium is a collection of allocations
  $\{c_t^*, k_{t+1}^*\}_{t=0}^{\infty}$ and prices
  $\{r_t^*, w_t^*\}_{t=0}^{\infty}$ such that:
  \begin{enumerate}
    \item \textbf{Household optimality:} Given prices $\{r_t^*, w_t^*\}$,
      the allocation $\{c_t^*, k_{t+1}^*\}$ solves the household's problem
      \eqref{eq:consumer}.
    \item \textbf{Firm optimality:} In each period $t$, factor prices satisfy
      $r_t^* = F_K(K_t, L_t)$ and $w_t^* = F_L(K_t, L_t)$.
    \item \textbf{Market clearing:} For all $t$,
      \begin{align*}
        c_t^* + k_{t+1}^* &= F(k_t^*, 1) + (1 - \delta) k_t^*
          && \text{(goods market)} \\
        L_t &= 1 && \text{(labor market, inelastic supply)}
      \end{align*}
  \end{enumerate}
\end{definition}
```

### Nash equilibrium (game theory)

```latex
\begin{definition}[Nash Equilibrium]\label{def:nash}
  A strategy profile $\sigma^* = (\sigma_1^*, \ldots, \sigma_N^*)$ is a Nash
  equilibrium if for every player $i \in \{1, \ldots, N\}$ and every
  alternative strategy $\sigma_i' \in \Sigma_i$:
  \begin{equation*}
    u_i(\sigma_i^*, \sigma_{-i}^*) \geq u_i(\sigma_i', \sigma_{-i}^*)
  \end{equation*}
\end{definition}
```

## Proofs

Use the `proof` environment from amsthm. It automatically adds a QED symbol.

```latex
\begin{proposition}\label{prop:euler}
  In any interior solution, the Euler equation holds:
  \begin{equation*}
    u'(c_t) = \beta (1 + r_{t+1}) u'(c_{t+1})
  \end{equation*}
\end{proposition}

\begin{proof}
  The first-order conditions of \eqref{eq:lagrangian} with respect to $c_t$
  and $k_{t+1}$ are:
  \begin{align}
    \frac{\partial \mathcal{L}}{\partial c_t}:     \quad & u'(c_t) = \lambda_t \label{eq:foc-c} \\
    \frac{\partial \mathcal{L}}{\partial k_{t+1}}: \quad & \lambda_t = \beta \lambda_{t+1} \bigl[ f'(k_{t+1}) + 1 - \delta \bigr] \label{eq:foc-k}
  \end{align}
  Substituting \eqref{eq:foc-c} into \eqref{eq:foc-k} and using
  $r_{t+1} = f'(k_{t+1}) - \delta$ yields the result.
\end{proof}
```

### Proof sketches and appendix proofs

```latex
% In the main text
\begin{proof}[Proof sketch]
  The argument proceeds in three steps. First, we show existence by
  Brouwer's fixed point theorem. Second, we establish uniqueness via
  contraction mapping. The full proof is in Appendix~\ref{app:proofs}.
\end{proof}
```

## Common patterns in economics papers

### First-order conditions (FOCs)

```latex
% Vertically aligned FOCs
\begin{align}
  [c_t]: \quad & u'(c_t) = \lambda_t \label{eq:foc1} \\
  [k_{t+1}]: \quad & \lambda_t = \beta \lambda_{t+1} [f'(k_{t+1}) + 1 - \delta] \label{eq:foc2} \\
  [\lambda_t]: \quad & c_t + k_{t+1} = f(k_t) + (1-\delta)k_t \label{eq:foc3}
\end{align}
```

### Value functions (dynamic programming)

```latex
\begin{equation}\label{eq:bellman}
  V(k) = \max_{k' \in [0, f(k) + (1-\delta)k]}
    \left\{ u\bigl(f(k) + (1-\delta)k - k'\bigr) + \beta V(k') \right\}
\end{equation}
```

### Welfare and surplus

```latex
% Compensating variation
\begin{equation}\label{eq:cv}
  V(p^1, y - CV) = V(p^0, y)
\end{equation}

% Social welfare function
\begin{equation}\label{eq:swf}
  W = \sum_{i=1}^{N} \omega_i \, u_i(x_i)
  \quad \text{where } \sum_{i} \omega_i = 1, \; \omega_i \geq 0
\end{equation}
```

### Elasticities

```latex
\varepsilon_{x,p} = \frac{\partial x}{\partial p} \cdot \frac{p}{x}
  = \frac{\partial \ln x}{\partial \ln p}
```

## Cross-referencing

Use `\eqref` for equations (adds parentheses automatically) and `\ref` for
theorems, propositions, and definitions. Use the `cleveref` package for
automatic formatting:

```latex
\usepackage[capitalise,noabbrev]{cleveref}

% Then in text:
As shown in \cref{eq:euler}, the Euler equation implies...
By \cref{prop:euler,prop:tvc}, the solution is characterized by...
```

## Style tips

- Use `\left( ... \right)` sparingly. Prefer `\bigl( ... \bigr)` or manual
  sizing for better control. `\left/\right` can produce ugly spacing.
- Use `\text{}` inside math for short verbal descriptions (e.g., "s.t.", "if",
  "for all"). Use `\quad` for spacing around these.
- Use `\cdot` for multiplication when needed (not `\times` unless for
  cross products or dimensions).
- Use `\ldots` for comma-separated lists ($x_1, \ldots, x_n$) and `\cdots`
  for operator-separated lists ($x_1 + \cdots + x_n$).
- Subscripts for identity, superscripts for indices when both are needed:
  $c_i^t$ (consumption of agent $i$ at time $t$), though $c_{it}$ is also
  common and acceptable.
- Bold lowercase for vectors ($\bm{x}$), bold uppercase for matrices ($\bm{A}$),
  but many economics papers avoid bold entirely and just state "let $x$ be a vector."
- Calligraphic letters for sets, information sets, or Lagrangians:
  $\mathcal{I}$, $\mathcal{F}$, $\mathcal{L}$.
