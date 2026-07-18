---
type: summary
title: "Lecture 5: Probability Theory"
description: "Foundations of probability, rules of probability, the binomial distribution, and the normal distribution."
tags: [probability, distributions, binomial, normal distribution, inference]
timestamp: 2026-07-18
sources: ["Lecture 5. Probability theory - notes.pdf"]
---

# Lecture 5: Probability Theory

## Introduction to Probability
Probability theory is essential for inferential statistics because it allows researchers to determine if an observed effect (or difference) is likely due to chance. A low probability suggests a real effect.
- Probability ranges from 0 (impossibility) to 1 (certainty).
- Calculated as: (Number of ways event could occur) / (Number of possible outcomes).
*(Source: Lecture 5. Probability theory - notes.pdf)*

## Rules of Probability
Key rules for calculating complex probabilities (see [[Probability_Theory]]):
1. **Rule 1**: Probability is always between 0 and 1.
2. **Rule 2**: Total probability of the sample space sums to 1.
3. **Rule 3 (Subtraction)**: P(not A) = 1 - P(A).
4. **Rule 4 (Addition)**: P(A or B) = P(A) + P(B) - P(A and B).
5. **Rule 5 (Multiplication)**: For independent events, P(A and B) = P(A) * P(B).
*(Source: Lecture 5. Probability theory - notes.pdf)*

## Approaches and Distributions
- **Bayesian vs Frequentist**: Bayesian treats probability as a degree of belief, while Frequentist defines it as the long-run frequency of repeated events. The **law of large numbers** states that empirical probability approaches true theoretical probability as sample size increases.
- **Binomial Distribution**: A discrete distribution modelling the probability of obtaining exactly *N* successes in *X* trials, based on the per-trial probability of success.
- **Normal Distribution**: A continuous distribution defined by its mean and standard deviation. Probabilities correspond to the area under the curve rather than exact points. In R, `pnorm()` and `qnorm()` are used to calculate probabilities and quantiles.
*(Source: Lecture 5. Probability theory - notes.pdf)*
