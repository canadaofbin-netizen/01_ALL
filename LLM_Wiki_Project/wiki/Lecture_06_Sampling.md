---
type: summary
title: "Lecture 06: Sampling"
description: "Summary of Lecture 6 covering types of sampling, sampling distributions, and standard error."
tags: [sampling, standard error, confidence intervals]
timestamp: 2026-07-18
sources: ["Lecture 6. Sampling - notes.pdf"]
---

# Lecture 06: Sampling

This lecture covers how to draw inferences from a sample to a population.

## Types of Sampling
- **Random sampling**: Selecting members of the population at random (e.g., from a list). This ensures the sample approximates the population, though true randomness is difficult to achieve.
- **Convenience sampling**: Recruiting subpopulations that are easily accessible (e.g., undergraduates).

Sampling bias matters if the non-randomness is associated with the outcome, but it may not matter if it is theoretically unassociated.

## Sampling Distribution
When drawing multiple samples of size *N* from a population, the means of these samples form a **sampling distribution**.
- The mean of sample means equals the population mean.
- The standard deviation (SD) of sample means equals the population SD divided by the square root of *N*.
- According to the **central limit theorem**, the means of all samples are normally distributed, even if the underlying data are not.

## Standard Error (SE)
The **Standard Error** is the standard deviation of the sampling distribution of the mean.
It is estimated using the formula: $SE = \frac{SD_{sample}}{\sqrt{N}}$
Larger sample sizes produce narrower sampling distributions and thus smaller standard errors.

## Confidence Intervals (CI)
Using rules from [[Probability_Theory]], 95% of sample means fall within ±1.96 SEs of the population mean in a normal distribution.
A 95% confidence interval for a sample mean is constructed as: $M \pm 1.96 \times SE$.

*(Source: Lecture 6. Sampling - notes.pdf)*
