---
type: concept
title: "Analysis of Variance (ANOVA)"
description: "Statistical method for comparing means across three or more groups."
tags: [statistics, anova, group differences]
timestamp: 2026-07-18
sources: ["Lecture 12. One-way ANOVA - slides.pdf"]
---
# Analysis of Variance (ANOVA)

ANOVA is an extension of the [[T_Test]] used to compare means when there are more than two groups or conditions.

## Mechanism
It partitions total variance into:
- **Model Variance**: Differences between group means and the grand mean.
- **Error Variance**: Differences between individual data points and their group mean.

The ratio of these variances produces the F-statistic. A significant F-test must be followed by post-hoc tests (e.g., Bonferroni) to determine which specific groups differ.

See [[Lecture_12_One_Way_ANOVA]].
