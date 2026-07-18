---
type: concept
title: "Hypothesis Testing"
description: "The statistical framework for deciding whether data support a particular hypothesis."
tags: [hypothesis testing, p-value, alpha, power, statistical errors]
timestamp: 2026-07-18
sources: ["Lecture 7. Hypothesis Testing - notes.pdf"]
---

# Hypothesis Testing

Hypothesis testing is a core component of inferential statistics in the [[Research_Process]]. It provides a structured method to decide if an effect or relationship observed in a sample likely exists in the true population.

## The Logic of Hypothesis Testing
1. **Formulate Hypotheses**:
   - **Null Hypothesis ($H_0$)**: The assumption that there is no effect or no difference (e.g., population mean difference is 0).
   - **Alternative Hypothesis ($H_1$)**: The assumption that an effect or difference exists.
2. **Choose a Test Statistic**: e.g., a *t*-statistic for a [[T_Test]], or Pearson's $r$ for [[Correlation]].
3. **Assume $H_0$ is True**: Determine the theoretical distribution of the test statistic if the null hypothesis were true.
4. **Calculate Likelihood (p-value)**: Compute the probability of observing a test statistic as extreme or more extreme than the one from the sample, assuming $H_0$ is true. (See [[Probability_Theory]])
5. **Decide**: Compare the p-value to a pre-defined threshold ($\alpha$, usually .05). If $p < \alpha$, reject $H_0$ in favor of $H_1$.

## P-Values and Their Misinterpretations
A **p-value** is the probability of the *data* (or more extreme data) given the *null hypothesis*.
It is **not**:
- The probability that the null hypothesis is true.
- The probability of making a wrong decision.
- The probability of replicating the exact same result.
- An indicator of the size or practical meaningfulness of the effect (which is measured by effect size).

## Types of Errors
Because we rely on probabilities, hypothesis testing always carries a risk of error:
- **Type I Error (False Positive)**: Rejecting $H_0$ when it is actually true. The risk of this error equals the alpha ($\alpha$) level.
- **Type II Error (False Negative)**: Retaining $H_0$ when it is actually false. The risk is denoted by beta ($\beta$). 

**Statistical Power** ($1 - \beta$) is the probability of correctly rejecting a false null hypothesis (i.e., detecting an effect when there is one). 

## Multiple Comparisons
When running multiple hypothesis tests on the same dataset, the probability of a Type I error increases. To control this, researchers often use the **Bonferroni correction**, dividing the $\alpha$ level by the number of tests performed.

*(Source: Lecture 7. Hypothesis Testing - notes.pdf)*
