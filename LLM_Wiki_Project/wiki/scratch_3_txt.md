---
title: "scratch_3.txt"
description: "This document consists of Lecture 14 notes on non-parametric statistical tests from M. Siromahov's 'Introduction to Statistical Methods' course. It explains the rationale for using non-parametric (distribution-free) methods over parametric equivalents (such as t-tests and ANOVA) when assumptions like normality are violated, outliers are present, or sample sizes are small. The lecture details three key non-parametric tests: the Wilcoxon Rank-Sum test (Mann-Whitney U-test) for independent two-sample comparisons, the Wilcoxon Signed-Rank test for paired-sample comparisons, and the Kruskal-Wallis test for comparing three or more independent groups. For each test, it outlines hypotheses, step-by-step data ranking procedures, R execution commands, post-hoc Bonferroni corrections, and standard reporting guidelines. Finally, it notes that while ranking protects against distributional violations, it reduces statistical power relative to parametric tests due to the loss of information regarding score magnitudes."
type: "summary"
tags: ["source"]
timestamp: "2026-08-01"
sources: ["scratch_3.txt"]
---
# scratch_3.txt

This document consists of Lecture 14 notes on non-parametric statistical tests from M. Siromahov's 'Introduction to Statistical Methods' course. It explains the rationale for using non-parametric (distribution-free) methods over parametric equivalents (such as t-tests and ANOVA) when assumptions like normality are violated, outliers are present, or sample sizes are small. The lecture details three key non-parametric tests: the Wilcoxon Rank-Sum test (Mann-Whitney U-test) for independent two-sample comparisons, the Wilcoxon Signed-Rank test for paired-sample comparisons, and the Kruskal-Wallis test for comparing three or more independent groups. For each test, it outlines hypotheses, step-by-step data ranking procedures, R execution commands, post-hoc Bonferroni corrections, and standard reporting guidelines. Finally, it notes that while ranking protects against distributional violations, it reduces statistical power relative to parametric tests due to the loss of information regarding score magnitudes.

## Information

### Added from [[scratch_3.txt]] on 2026-08-01
- Non-parametric tests do not assume data are drawn from a specific normal distribution, making them suitable when normality is violated, extreme outliers exist, sample sizes are small, or medians are preferred over means. ([scratch_3.txt])
- Most non-parametric tests function by ranking raw data and evaluating the ranks, making results robust against extreme scores. ([scratch_3.txt])
- The Wilcoxon rank-sum test (or Mann-Whitney U-test) serves as a non-parametric alternative to the independent two-sample t-test. ([scratch_3.txt])
- The Wilcoxon signed-rank test serves as a non-parametric alternative to the paired-samples t-test, testing whether the median difference between paired observations equals zero. ([scratch_3.txt])
- The Kruskal-Wallis test serves as a non-parametric alternative to one-way ANOVA, testing whether three or more independent groups come from identical populations. ([scratch_3.txt])
- While non-parametric tests avoid distribution assumptions, they are generally less powerful than parametric tests when parametric assumptions are met because ranking loses information about score magnitudes. ([scratch_3.txt])
