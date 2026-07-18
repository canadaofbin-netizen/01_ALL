---
type: summary
title: "Lecture 07: Hypothesis Testing"
description: "Summary of Lecture 7 on hypothesis testing, p-values, errors, and power."
tags: [hypothesis testing, p-value, alpha, power, errors]
timestamp: 2026-07-18
sources: ["Lecture 7. Hypothesis Testing - notes.pdf"]
---

# Lecture 07: Hypothesis Testing

Hypothesis testing allows us to infer whether an effect or relationship is likely to exist in the real world based on sample data.

## Steps of Hypothesis Testing
1. **Formulate Hypotheses**: 
   - **Null hypothesis ($H_0$)**: Expected result if there is no effect.
   - **Alternative hypothesis ($H_1$)**: Expected result if there is an effect.
2. **Choose a Test Statistic**: A value describing the data (e.g., number of successes).
3. **Calculate Likelihood**: Determine how likely the data is if the null hypothesis is true, using theoretical or empirical probability.
4. **Compare to Threshold**: Compare the p-value to the $\alpha$ level (typically .05). If $p < .05$, we reject $H_0$.

## Errors and Power
- **Type I Error (False Positive)**: Rejecting $H_0$ when it is true. The risk is determined by the alpha ($\alpha$) level.
- **Type II Error (False Negative)**: Retaining $H_0$ when it is false. The risk is determined by beta ($\beta$).
- **Statistical Power**: The capacity of a test to detect a true effect, calculated as $1 - \beta$.

## Interpreting p-values
- A p-value is the probability of observing a test statistic (or one more extreme) if the null hypothesis were true.
- It is **not** the probability that $H_0$ is true, nor the probability of making a wrong decision, nor a measure of effect size.

## Multiple Comparisons
Testing multiple hypotheses increases the chance of finding a spurious result (Type I error). A **Bonferroni correction** adjusts the critical threshold by dividing the original $\alpha$ by the number of comparisons.

*(Source: Lecture 7. Hypothesis Testing - notes.pdf)*
