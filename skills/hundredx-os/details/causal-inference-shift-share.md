# Shift-Share (Bartik) Instruments

## Structure

A shift-share instrument has the form:

B_i = sum_k s_{ik} * g_k

where:
- s_{ik} is the "share" or "exposure" of unit i to sector/group k (e.g., industry employment share in region i)
- g_k is the "shift" (e.g., national employment growth in industry k)
- The product captures how much each unit is affected by aggregate shocks, weighted by its initial composition

The instrument varies across units because different units have different exposure compositions (shares), even though the shifts are common to all units.

## Canonical Applications

- **Labor demand (Bartik 1991)**: s_{ik} = share of employment in industry k in region i at baseline. g_k = national growth rate of industry k employment (excluding region i). Instruments for local labor demand shocks.
- **Immigration (Card 2001)**: s_{ik} = share of immigrants from origin country k living in region i at baseline. g_k = national inflow of immigrants from country k. Instruments for immigration inflows to a region.
- **Trade shocks (Autor, Dorn, and Hanson 2013)**: s_{ik} = share of employment in industry k in commuting zone i. g_k = change in Chinese imports per worker in industry k (using imports to other high-income countries as shifts). Instruments for local exposure to import competition.
- **Technology shocks**: Exposure to automation based on local occupation shares times national adoption of robots/AI.

## Three Modern Interpretations

The recent econometric literature has clarified that there are fundamentally different ways to justify shift-share instruments, each with different assumptions and implications.

### 1. Goldsmith-Pinkham, Sorkin, and Swift (2020) — Share Exogeneity

**Core idea**: The Bartik instrument is equivalent to a GMM estimator using the initial shares {s_{ik}} as individual instruments with shifts {g_k} as weights.

**Identifying assumption**: The shares are exogenous — uncorrelated with the structural error. This is a cross-sectional assumption about the initial composition of units.

**When this applies**: When the shares represent pre-determined, quasi-random variation in exposure. For example, if initial industry composition is plausibly orthogonal to future labor market shocks (conditional on controls).

**Diagnostics**:
- Rotemberg weights: decompose the overall Bartik estimate into contributions from each industry-specific instrument (each share). Some shares may receive negative weights (analogous to negative weights in TWFE DiD).
- Identify the top contributing shares and argue their exogeneity individually.
- Test balance: are the high-weight shares correlated with pre-trends or observable confounders?

**Inference**: Standard IV standard errors are valid for the Bartik estimator under share exogeneity, but must account for the correct number of overidentifying restrictions (which equals the number of shares minus the number of endogenous variables).

### 2. Borusyak, Hull, and Jaravel (2022) — Shift Exogeneity

**Core idea**: Identification comes from the exogeneity of the shifts (g_k), not the shares. The shifts are as-if randomly assigned across sectors/groups.

**Identifying assumption**: The shifts g_k are independent of the potential outcomes, conditional on observables. This is a sectoral-level assumption.

**When this applies**: When the shifts represent quasi-random shocks to sectors/groups. For example, if national demand shocks to industries are plausibly exogenous from the perspective of any individual region.

**Key results**:
- The shift-share regression can be rewritten as an equivalent shift-level regression with exposure-weighted observations.
- Standard errors should account for correlation at the shift (sector) level, not the unit (region) level.
- With few sectors (fewer than ~40-50), inference must be adjusted (sector-level clustering with few clusters).

**Exposure robustness**: Even if individual shares are endogenous, the Bartik instrument is valid as long as shifts are exogenous and no single share dominates the instrument (the Herfindahl index of shares is small). This makes shift exogeneity applicable to many settings where arguing share exogeneity is difficult.

### 3. Adao, Kolesar, and Morales (2019) — Inference Correction

**Core idea**: Standard errors for shift-share regressions are typically too small because they ignore correlation in residuals induced by the structure of the instrument.

**The problem**: Regions with similar industry compositions (similar shares) have correlated instruments and correlated residuals. Standard cluster-robust SEs (clustering by region) do not account for this cross-regional correlation.

**Solution**: Compute standard errors that account for the exposure-driven correlation structure. Specifically, allow residuals to be correlated across regions proportionally to the similarity of their share vectors.

**AKM standard errors**: These are conservative and valid under both shift and share exogeneity interpretations. They are the recommended default for shift-share IV regressions.

**Practical implication**: AKM standard errors are often substantially larger than conventional cluster-robust SEs, potentially overturning previously significant findings.

## Choosing the Right Framework

| Feature | GPSS (Share exogeneity) | BHJ (Shift exogeneity) | AKM (Inference) |
|---------|------------------------|------------------------|-----------------|
| Key assumption | Shares are exogenous | Shifts are exogenous | Either |
| Applicable when | Pre-determined shares | Quasi-random sector shocks | General correction |
| Number of units | Many | Can be few | Many |
| Number of sectors | Can be few | Must be many (for CLT) | Many |
| Inference level | Region | Sector | Exposure-robust |
| Key diagnostic | Rotemberg weights | Shift-level balance | SE comparison |

**Decision guide**:
- If you believe the shares are pre-determined and quasi-random: use GPSS framework, report Rotemberg weights.
- If you believe the shifts are quasi-random sectoral shocks: use BHJ framework, cluster at sector level.
- In either case: report AKM standard errors as a conservative baseline.
- If both shares and shifts are potentially endogenous: the design may not be credible.

## Practical Implementation

### Step 1: Describe the instrument
- Clearly define shares and shifts.
- Report summary statistics: number of sectors, Herfindahl index of shares, share of variation from top sectors.
- Show the time structure: are shares from a pre-period? How far back?

### Step 2: First stage
- Regress the endogenous variable on the Bartik instrument and controls.
- Report the effective F-statistic.
- Show the first-stage relationship is not driven by a handful of sectors.

### Step 3: Rotemberg decomposition (GPSS)
- Compute Rotemberg weights for each sector.
- Identify top positive and negative weight sectors.
- Argue exogeneity for the sectors that receive the most weight.
- Show covariate balance for high-weight sectors.

### Step 4: Shift-level analysis (BHJ)
- Run the equivalent shift-level regression.
- Show the shifts are balanced on pre-treatment outcomes and covariates.
- Cluster standard errors at the shift (sector) level.

### Step 5: Inference
- Report standard errors under multiple assumptions:
  - Cluster-robust (by region): the conventional approach, likely too small.
  - AKM (exposure-robust): conservative, accounts for share-driven correlation.
  - Sector-clustered: appropriate under shift exogeneity.
- Compare all three. If conclusions change, discuss which assumption is more credible.

### Step 6: Robustness
- Leave out the top contributing sectors one at a time.
- Use lagged shares from an earlier period.
- Include regional controls (pre-trends, demographic composition).
- Construct a "leave-one-out" version of the shifts (exclude region i from the national shift calculation).

## Common Pitfalls

1. **Leave-out construction**: When computing national shifts, exclude region i's own contribution to avoid mechanical correlation. This is standard practice but still sometimes overlooked.

2. **Stale shares**: Using very old baseline shares reduces endogeneity concerns but may weaken the first stage if composition has changed substantially.

3. **Few effective sectors**: If the instrument variation is driven by a small number of sectors, the CLT may not apply at the sector level (BHJ framework), and Rotemberg weights concentrate on few sectors (GPSS framework).

4. **Negative Rotemberg weights**: Some sectors may receive negative weights, meaning the overall estimate may not be a convex combination of sector-specific effects. This parallels the TWFE negative weight problem in DiD.

5. **Confounding sector-level shocks**: If the shift variable is correlated with other sector-level changes that directly affect regional outcomes, the exclusion restriction fails.

6. **Heterogeneous effects**: With heterogeneous treatment effects across sectors, different frameworks identify different estimands. GPSS identifies a weighted average of sector-specific LATEs. BHJ identifies an exposure-weighted ATE.

## Key References

- Bartik, T. (1991). Who Benefits from State and Local Economic Development Policies? Upjohn Institute.
- Goldsmith-Pinkham, P., Sorkin, I., and Swift, H. (2020). Bartik instruments: What, when, why, and how. American Economic Review.
- Borusyak, K., Hull, P., and Jaravel, X. (2022). Quasi-experimental shift-share research designs. Review of Economic Studies.
- Adao, R., Kolesar, M., and Morales, E. (2019). Shift-share designs: Theory and inference. Quarterly Journal of Economics.
- Card, D. (2001). Immigrant inflows, native outflows, and the local labor market impacts of higher immigration. Journal of Labor Economics.
- Autor, D., Dorn, D., and Hanson, G. (2013). The China syndrome: Local labor market effects of import competition in the United States. American Economic Review.
