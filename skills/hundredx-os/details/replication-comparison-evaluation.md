# Skill: Comparison & Evaluation

You are evaluating whether a replication successfully reproduces the original results.

## Match Quality Categories

### Direction and Significance Match
- Same sign of coefficient AND same significance level
- This is a "successful replication" even if magnitudes differ
- Deviation in magnitude is expected with different data/period

### Direction Only Match
- Same sign but different significance (e.g., *** becomes * or n.s.)
- This is a "partial replication" — the effect exists but is weaker
- Investigate: smaller sample? less variation? different period?

### No Match
- Different sign OR completely insignificant when original was highly significant
- This is a "failed replication" — requires careful analysis
- Do NOT immediately blame the replication — the original might be fragile

## Deviation Analysis Framework

### Expected Deviations (planned)
- Different sample period → expect magnitude differences
- Different winsorization → affects outlier-sensitive estimates
- Different data source → expect level differences, same patterns
- Package differences → minor numerical differences (< 1%)

### Unexpected Deviations (investigate)
- Sign flips → check variable construction, coding errors
- Large magnitude differences (> 50%) → check sample selection
- Significance changes → check SE computation, clustering

## Assumption Testing
For each key assumption:
1. Can it be tested? (parallel trends → yes; exclusion restriction → usually no)
2. Was it tested in the original? How?
3. Does it hold in the replication data?
4. If violated, what does that imply for the results?

## Overall Assessment Criteria
- **Successful**: >80% of primary results replicate in direction and significance
- **Partial**: 50-80% of primary results replicate, or all replicate in direction only
- **Failed**: <50% of primary results replicate

## Robustness Assessment of Original
After all comparisons:
- Are results robust to different data? → Strong external validity
- Are results robust to different specifications? → Strong internal validity
- Do results depend on specific coding choices? → Fragile
