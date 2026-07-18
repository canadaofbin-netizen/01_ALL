---
type: summary
title: "Lecture 3: Summarising Data"
description: "Using descriptive statistics, frequency distributions, and measures of central tendency/dispersion to summarize psychological data."
tags: [descriptive statistics, mean, standard deviation, normal distribution, z-scores]
timestamp: 2026-07-18
sources: ["Lecture 3. Summarising data - notes.pdf"]
---

# Lecture 3: Summarising Data

## Descriptive vs. Inferential Statistics
- **Descriptive statistics**: Describe and summarise data (e.g., averages, variation). Summarising large sets of data is essential for generalisation and prediction.
- **Inferential statistics**: Statistical tests to determine significant differences or associations.
*(Source: Lecture 3. Summarising data - notes.pdf)*

## Frequency Distributions and Visualization
Data can be summarised using absolute frequencies (counts) or relative frequencies (proportions). Histograms (frequency, density, cumulative) visualize these distributions. For continuous data, values are grouped into **bins**. See [[Data_Visualization]] for graph types.
*(Source: Lecture 3. Summarising data - notes.pdf)*

## Symmetrical and Skewed Distributions
- **Symmetrical (Normal)**: Scores are distributed evenly around a midpoint.
- **Skewed**: 
  - *Right skew*: A floor effect, common when values cannot be below 0 (e.g., number of siblings).
  - *Left skew*: A ceiling effect, common when values max out (e.g., 100% on a test).
*(Source: Lecture 3. Summarising data - notes.pdf)*

## Central Tendency and Dispersion
Measures covered in [[Descriptive_Statistics]] include:
- **Central Tendency**: Mode (most common), Mean (sensitive to outliers/skew), Median (middle ordered value).
- **Dispersion**: How far data points are from the mean. Computed using Sum of Squared Differences -> **Variance** -> **Standard Deviation (SD)**. 
- In R, `summarise()` along with `mean()`, `median()`, and `sd()` are used.
*(Source: Lecture 3. Summarising data - notes.pdf)*

## Z-Scores
**Z-scores** standardise individual scores to reflect how many Standard Deviations a score lies from the Mean. In a normal distribution:
- 68.2% of data points fall within 1 SD of the mean.
- 95.4% fall within 2 SDs.
*(Source: Lecture 3. Summarising data - notes.pdf)*
