---
type: summary
title: "Lecture 12: One-way ANOVA"
description: "Summary of Lecture 12 on Analysis of Variance for comparing more than two groups."
tags: [statistics, anova, quantitative methods]
timestamp: 2026-07-18
sources: ["Lecture 12. One-way ANOVA - slides.pdf"]
---
# Lecture 12: One-way ANOVA

## Overview
While [[T_Test]]s are used for comparing two groups, **ANOVA** (Analysis of Variance) is used when comparing more than two groups. A One-way ANOVA has one categorical independent variable (with >2 levels) and one continuous dependent variable.
*(Source: Lecture 12. One-way ANOVA - slides.pdf)*

## Hypothesis Testing and F-Statistic
- **Null Hypothesis**: Population means are equal (all groups are best described by the grand mean).
- **F-statistic**: Ratio of variance explained by the model to the unexplained (residual) variance.
- **Effect Size**: Eta squared represents the proportion of total variation explained by group membership.

## Post-Hoc Analysis
A significant F-test indicates a difference exists, but not *where* it lies. Post-hoc pairwise comparisons (e.g., Bonferroni correction) are required to compare individual groups while controlling for the false-positive rate.

## Assumptions
- DV is interval/ratio.
- Independent observations.
- Homogeneity of variance of residuals.
- Normal distribution of residuals.

See also: [[ANOVA]], [[Hypothesis_Testing]]
