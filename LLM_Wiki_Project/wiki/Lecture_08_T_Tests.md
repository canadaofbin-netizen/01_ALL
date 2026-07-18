---
type: summary
title: "Lecture 08: T-tests"
description: "Summary of Lecture 8 on t-tests, types of t-tests, and Cohen's d."
tags: [t-test, cohens d, effect size]
timestamp: 2026-07-18
sources: ["Lecture 8. T-tests - slides.pdf"]
---

# Lecture 08: T-tests

T-tests compare a binary independent variable to a numeric dependent variable.

## Types of T-tests
- **One-sample t-test**: Compares a sample mean to a known or specified population mean.
- **Two-samples t-test**: Compares the means of two independent groups (between-subjects design). Uses Welch's t-test by default in R to account for unequal variances.
- **Paired samples t-test**: Compares the means of two paired samples (within-subjects design), effectively a one-sample t-test on the difference scores.

## T-statistic
The t-statistic measures the difference between means relative to data variability:
$$t = \frac{\text{effect (mean difference)}}{\text{error (variation)}}$$
For a one-sample test, error is the Standard Error ($SE = SD / \sqrt{N}$).
Larger differences yield larger *t* values, while greater variability yields smaller *t* values.

## Hypothesis Testing with t-tests
By comparing the calculated t-value to a critical t-value from the t-distribution (which depends on degrees of freedom), we obtain a p-value.
- **One-tailed vs Two-tailed**: Two-tailed tests test for any difference, whereas one-tailed tests have a directional hypothesis.

## Assumptions
All t-tests require:
- An interval or ratio level outcome variable.
- Normal distribution of the outcome (tested via histograms, Q-Q plots, or the Shapiro-Wilk test).
- Independence of observations (for two-sample tests) or paired data (for paired-sample tests).

## Effect Size (Cohen's d)
Effect size estimates the magnitude of the difference independently of sample size. **Cohen's d** is the mean difference divided by the standard deviation. A common rule of thumb: 0.2 (small), 0.5 (medium), 0.8 (large).

*(Source: Lecture 8. T-tests - slides.pdf)*
