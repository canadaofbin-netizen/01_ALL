---
type: summary
title: "Lecture 09: Correlations"
description: "Summary of Lecture 9 on variance, covariance, Pearson's r, and Spearman's rho."
tags: [correlation, covariance, variance, pearsons r]
timestamp: 2026-07-18
sources: ["Lecture 9. Correlations - notes.pdf"]
---

# Lecture 09: Correlations

Correlations assess whether two variables vary together systematically (covariance).

## Variance and Covariance
- **Variance**: Average squared difference from the mean, calculated as $\frac{\sum (Y_i - \bar{Y})^2}{N-1}$.
- **Covariance**: Product of differences from the mean for two variables, calculated as $\frac{\sum (Y_i - \bar{Y})(X_i - \bar{X})}{N-1}$. Positive values mean variables move in the same direction; negative means opposite directions.

## Pearson's Correlation Coefficient ($r$)
Covariance depends on variable scales. **Pearson's r** standardizes this measure between -1 and 1 by dividing covariance by the product of both variables' standard deviations.
- Rules of thumb: .30 (Weak), .50 (Moderate), .70 (Strong).

## Hypothesis Testing
The null hypothesis ($H_0$) states the population correlation ($\rho$) is 0. 
The t-statistic for $r$ is: $t = r \times \sqrt{\frac{n-2}{1-r^2}}$.
Note: Correlation does not equal causation.

## Assumptions
Pearson's $r$ requires:
- Interval or ratio level data.
- Normal distribution for both variables.
- Linear relationship.
- Homoscedasticity (similar variation of Y at each value of X).
- No extreme outliers.

## Spearman's rho
If assumptions are violated, use **Spearman's rho**, a non-parametric alternative based on ranked data.

*(Source: Lecture 9. Correlations - notes.pdf)*
