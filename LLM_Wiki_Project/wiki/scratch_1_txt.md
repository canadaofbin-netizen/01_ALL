---
title: "scratch_1.txt"
description: "This document presents lecture slides by Dr. Metodi Siromahov on One-Way Between-Subjects ANOVA. It explains the distinction between t-tests and ANOVA, demonstrates how total variance is partitioned into model and error sums of squares, and walks through calculating degrees of freedom, the F-statistic, and eta-squared effect size using a running speed dataset across three music tempo conditions. Additionally, it details executing ANOVA in R using the afex package, performing Bonferroni-corrected post-hoc pairwise comparisons, testing statistical assumptions, and structuring standard academic write-ups."
type: "summary"
tags: ["source"]
timestamp: "2026-08-01"
sources: ["scratch_1.txt"]
---
# scratch_1.txt

This document presents lecture slides by Dr. Metodi Siromahov on One-Way Between-Subjects ANOVA. It explains the distinction between t-tests and ANOVA, demonstrates how total variance is partitioned into model and error sums of squares, and walks through calculating degrees of freedom, the F-statistic, and eta-squared effect size using a running speed dataset across three music tempo conditions. Additionally, it details executing ANOVA in R using the afex package, performing Bonferroni-corrected post-hoc pairwise comparisons, testing statistical assumptions, and structuring standard academic write-ups.

## Information

### Added from [[scratch_1.txt]] on 2026-08-01
- t-tests are appropriate for comparing two groups, while ANOVAs are required when comparing more than two groups or conditions. ([scratch_1.txt])
- The total variance in a dependent variable is partitioned into variance explained by group membership (SSmodel) and residual variance (SSerror). ([scratch_1.txt])
- A statistically significant F-statistic indicates overall group differences exist, but post-hoc pairwise tests are needed to pinpoint which specific groups differ. ([scratch_1.txt])
- Performing multiple post-hoc t-tests increases the risk of Type I errors (false positives), requiring p-value adjustments like the Bonferroni correction. ([scratch_1.txt])
- ANOVA is robust to violations of normality and homogeneity of variance assumptions when sample sizes across groups are equal. ([scratch_1.txt])
