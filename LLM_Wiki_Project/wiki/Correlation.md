---
type: concept
title: "Correlation"
description: "Statistical measure indicating the extent to which two numeric variables fluctuate together."
tags: [correlation, covariance, pearsons r, spearman, effect size]
timestamp: 2026-07-18
sources: ["Lecture 9. Correlations - notes.pdf"]
---

# Correlation

**Correlation** measures the direction and strength of the association between two continuous variables (see [[Variables_and_Measurement]]). It builds upon the concept of variance (see [[Descriptive_Statistics]]).

## Covariance
While variance measures how a single variable deviates from its mean, **covariance** measures how two variables deviate from their respective means together.
- A **positive covariance** indicates variables move in the same direction.
- A **negative covariance** indicates variables move in opposite directions.
Covariance is sensitive to the scale of the original variables, making it difficult to interpret the magnitude of the relationship.

## Pearson's Correlation Coefficient ($r$)
To solve the scaling issue, covariance is divided by the product of both variables' standard deviations, yielding **Pearson's r**.
- $r$ ranges from -1 (perfect negative correlation) to 1 (perfect positive correlation), with 0 indicating no linear relationship.
- Rules of thumb for interpretation: 0.30 (weak), 0.50 (moderate), 0.70 (strong).
- $r$ serves as its own measure of effect size.

## Hypothesis Testing for Correlation
In [[Hypothesis_Testing]], the null hypothesis ($H_0$) for a correlation is that the population correlation coefficient ($\rho$) is 0. A *t*-statistic can be calculated based on the sample $r$ and the sample size to determine the *p*-value.
*Important constraint*: Correlation does not imply causation.

## Assumptions of Pearson's $r$
- Variables must be interval or ratio level data.
- Both variables should be normally distributed.
- The relationship must be linear.
- **Homoscedasticity**: The variance of one variable should be relatively constant across all levels of the other variable.
- No extreme outliers, as Pearson's $r$ is highly sensitive to them.

## Spearman's rho ($\rho$ or $r_s$)
If the data violate the assumptions of Pearson's correlation (e.g., non-normal distribution, ordinal data, or extreme outliers), the non-parametric **Spearman's rho** can be used. It relies on ranking the data points from smallest to largest and running the correlation on the ranks rather than the raw values.

*(Source: Lecture 9. Correlations - notes.pdf)*
