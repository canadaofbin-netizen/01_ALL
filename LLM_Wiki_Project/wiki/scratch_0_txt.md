---
title: "scratch_0.txt"
description: "This document (Lecture 11 by M. Siromahov) introduces simple linear regression as a statistical modeling tool for predicting an outcome variable from a continuous predictor variable. It explains model components (intercept, slope, residual error), hypothesis testing (F-test for overall model fit and t-tests for slope significance), effect size via R², R implementation using lm() and summary(), standardized reporting guidelines, and core statistical assumptions."
type: "summary"
tags: ["source"]
timestamp: "2026-08-01"
sources: ["scratch_0.txt"]
---
# scratch_0.txt

This document (Lecture 11 by M. Siromahov) introduces simple linear regression as a statistical modeling tool for predicting an outcome variable from a continuous predictor variable. It explains model components (intercept, slope, residual error), hypothesis testing (F-test for overall model fit and t-tests for slope significance), effect size via R², R implementation using lm() and summary(), standardized reporting guidelines, and core statistical assumptions.

## Information

### Added from [[scratch_0.txt]] on 2026-08-01
- Linear regression creates a predictive statistical model for Y based on X, unlike correlation which only tests for association without predictive directionality. ([scratch_0.txt])
- A linear model can be expressed mathematically as Y = Intercept + (Slope * X) plus residual error. ([scratch_0.txt])
- Goodness of fit is tested using an F-test comparing model variance (MS_model) to residual variance (MS_error). ([scratch_0.txt])
- R² quantifies the proportion of variance in the outcome variable Y explained by the predictor X. ([scratch_0.txt])
- A t-test for the slope coefficient evaluates the null hypothesis that there is no relationship between predictor X and outcome Y. ([scratch_0.txt])
- Assumptions for linear regression include continuous data, linear relationship, homoscedasticity, lack of extreme outliers, and normally distributed residuals. ([scratch_0.txt])
