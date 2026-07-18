---
type: concept
title: "T-Test"
description: "A statistical test used to compare the means of two groups or one group against a known mean."
tags: [t-test, means, significance testing, student's t, welch's t]
timestamp: 2026-07-18
sources: ["Lecture 8. T-tests - slides.pdf"]
---

# T-Test

A **t-test** is an inferential statistical test used in [[Hypothesis_Testing]] to determine if there is a significant difference between means. It assesses the relationship between a binary categorical independent variable and a numeric dependent variable.

## The T-Statistic
The fundamental logic behind a t-statistic is scaling the size of the observed effect by the variability (error) in the data:
$$t = \frac{\text{difference between means}}{\text{Standard Error}}$$
A larger difference between means and a smaller variation (Standard Error, see [[Sampling]]) lead to a larger *t*-statistic and a smaller *p*-value.

## Types of T-Tests
1. **One-Sample t-test**: Compares the mean of a single sample to a known or hypothesized population mean.
2. **Independent (Two-Sample) t-test**: Compares the means of two mutually exclusive groups (between-subjects design). 
   - *Student's t-test*: Assumes equal variances between groups.
   - *Welch's t-test*: Does not assume equal variances. This is the default in R and is generally preferred.
3. **Paired Samples t-test**: Compares the means of the same participants across two conditions or time points (within-subjects design). It is mathematically equivalent to a one-sample t-test on the difference scores.

## Assumptions
All t-tests rely on certain assumptions:
- The dependent variable is measured at the interval or ratio level (see [[Variables_and_Measurement]]).
- The data within each group (or the difference scores for paired tests) are normally distributed. This can be checked visually using [[Data_Visualization]] techniques like histograms and Q-Q plots, or formally via the Shapiro-Wilk test.
- Independence of observations (for independent t-tests).

## Effect Size (Cohen's d)
Because *p*-values are highly dependent on sample size, statistically significant results in large samples might not be practically meaningful. **Cohen's d** is an effect size measure used for t-tests that standardizes the mean difference by the standard deviation, providing a scale-free estimate of the effect magnitude (e.g., small = 0.2, medium = 0.5, large = 0.8).

*(Source: Lecture 8. T-tests - slides.pdf)*
