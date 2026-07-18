---
type: summary
title: "Lecture 11: Linear Regression"
description: "Summary of Lecture 11 covering simple linear regression, model fitting, and assumptions."
tags: [statistics, linear regression, quantitative methods]
timestamp: 2026-07-18
sources: ["Lecture 11. Linear Regression - notes.pdf"]
---
# Lecture 11: Linear Regression

## Overview
A linear regression is a statistical model describing how changes in one variable (predictor X) correspond to changes in another variable (outcome Y). Unlike [[Correlation]], it allows for predicting the value of Y based on X.

## The Linear Model
The regression line is mathematically expressed as:
`Y = a + (b * X)` where `a` is the intercept and `b` is the slope.
- **Intercept**: The value of Y when X=0.
- **Slope**: How much Y changes with each unit increase in X.
- **Error**: The discrepancy between the model's predicted values and the actual observed data (residuals).
*(Source: Lecture 11. Linear Regression - notes.pdf)*

## Hypothesis Testing in Regression
1. **Model Fit**: Tested using an F-test to see if variance explained by the model is greater than residual variance. 
2. **Predictor Significance**: Tested using a t-test to see if the slope is significantly different from 0.
- **Effect Size (R-squared)**: The proportion of variance in Y accounted for by the model.

## Assumptions
- Interval or ratio level data.
- Linear relationship.
- Homogeneity of variance.
- No extreme outliers.
- Residuals must be normally distributed.

See also: [[Linear_Regression]]
