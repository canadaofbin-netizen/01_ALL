---
type: concept
title: "Non-Parametric Tests"
description: "Statistical tests that do not assume data follow a specific (normal) distribution. They make weak assumptions about the underlying population distribution and operate primarily on ranked data."
tags: [statistics, non-parametric, concept]
timestamp: "2026-08-01"
sources:
  - "Lecture 14. Non-parametric tests - notes.pdf"
  - "scratch_3.txt"
---
# Non-Parametric Tests

Non-parametric tests are "distribution-free" alternatives to standard parametric tests (like [[ANOVA]] or [[T_Test]]). They are highly useful when data violate normality, contain severe outliers, or when analyzing small sample sizes. They make weak assumptions about the underlying population distribution and operate primarily on ranked data.

## Common Methods
Instead of raw scores, these tests often rank data points:
- **Wilcoxon Rank-Sum / Mann-Whitney U**: For independent samples.
- **Wilcoxon Signed-Rank**: For paired samples.
- **Kruskal-Wallis**: For comparing three or more groups.

See [[Lecture_14_Non_Parametric_Tests]].
