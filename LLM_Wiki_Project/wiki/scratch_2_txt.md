---
title: "scratch_2.txt"
description: "Lecture notes by M. Siromahov covering statistical analysis of categorical data using Chi-Squared (χ²) tests. The material defines nominal and ordinal variables, details the Chi-Squared goodness-of-fit test with seasonal birth data, and explains the Chi-Squared test of independence using a political view and pet preference example. It provides formulas for calculating expected frequencies, test statistics, degrees of freedom, and effect sizes (Phi coefficient and Cramer's V), outlines key test assumptions, and explains R software execution."
type: "summary"
tags: ["source"]
timestamp: "2026-08-01"
sources: ["scratch_2.txt"]
---
# scratch_2.txt

Lecture notes by M. Siromahov covering statistical analysis of categorical data using Chi-Squared (χ²) tests. The material defines nominal and ordinal variables, details the Chi-Squared goodness-of-fit test with seasonal birth data, and explains the Chi-Squared test of independence using a political view and pet preference example. It provides formulas for calculating expected frequencies, test statistics, degrees of freedom, and effect sizes (Phi coefficient and Cramer's V), outlines key test assumptions, and explains R software execution.

## Information

### Added from [[scratch_2.txt]] on 2026-08-01
- Categorical variables are divided into nominal variables without natural ordering and ordinal variables with natural ordering. ([scratch_2.txt])
- A Chi-Squared goodness-of-fit test on 4,700 births at St. Margaret's Hospital demonstrated a statistically significant deviation from equal seasonal distribution (χ²(3, N=4700) = 15.7, p < .001). ([scratch_2.txt])
- The Chi-Squared test statistic is always non-negative because it sums squared differences between observed and expected frequencies relative to expected frequencies. ([scratch_2.txt])
- A Chi-Squared test of independence demonstrated a significant association between political views and pet choice (χ²(1, N=100) = 14.18, p < .001, φ = .38), with liberals preferring cats and conservatives preferring dogs. ([scratch_2.txt])
- In R, the chisq function applies continuity correction by default, which can be overridden by setting correct = FALSE. ([scratch_2.txt])
- Valid Chi-Squared tests require count data, mutually exclusive categories, independent observations, and expected cell frequencies greater than 5. ([scratch_2.txt])
