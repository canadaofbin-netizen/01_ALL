---
type: concept
title: "Probability Theory"
description: "The mathematical framework for quantifying uncertainty and making statistical inferences."
tags: [probability, frequentist, bayesian, probability distributions, normal distribution, binomial distribution]
timestamp: 2026-07-18
sources: ["Lecture 5. Probability theory - notes.pdf"]
---

# Probability Theory

Probability forms the backbone of inferential statistics in the [[Research_Process]], providing a framework to assess whether observed differences are due to random chance or reflect real psychological phenomena.

## Core Terminology
- **Experiment**: An activity that produces a new outcome.
- **Sample Space**: The complete set of possible outcomes.
- **Elementary Event**: One specific outcome within the sample space.

## Perspectives on Probability
- **Bayesian Approach**: Probability is a subjective degree of belief based on prior experience.
- **Frequentist Approach**: Probability is the long-run frequency of an event over repeated trials. Related to the **Law of Large Numbers**, which dictates that as the number of trials increases, the empirical probability converges to the true theoretical probability.

## The Rules of Probability
1. **Range**: Any probability `P(A)` is between 0 and 1.
2. **Sum to 1**: All elementary events in a sample space sum to 1.
3. **Subtraction Rule**: The probability of an event *not* happening is `1 - P(A)`.
4. **Addition Rule (OR)**: `P(A ∪ B) = P(A) + P(B) - P(A ∩ B)`. If mutually exclusive, the subtraction term is zero.
5. **Multiplication Rule (AND)**: If events A and B are independent, `P(A ∩ B) = P(A) * P(B)`.

## Probability Distributions
Theoretical probability distributions dictate the shape of expected outcomes.
- **Binomial Distribution**: Used for discrete events (e.g., answering a multiple-choice quiz). Defined by the number of trials and the probability of success on a single trial.
- **Normal Distribution**: Used for continuous data (e.g., human height). Defined by the mean and standard deviation (see [[Descriptive_Statistics]]). In continuous distributions, the probability of an exact value is zero; probabilities are calculated over ranges (the area under the curve).

## Applications in Inference
Probability theory is the basis for key inferential tools:
- **Confidence Intervals**: The range of values within which a population parameter is expected to lie with a certain probability (e.g., 95%). See [[Sampling]].
- **P-values**: The probability of observing a test statistic as extreme or more extreme than the one from the sample, assuming the null hypothesis is true. See [[Hypothesis_Testing]].

*(Source: Lecture 5. Probability theory - notes.pdf; Lecture 6. Sampling - notes.pdf; Lecture 7. Hypothesis Testing - notes.pdf)*
