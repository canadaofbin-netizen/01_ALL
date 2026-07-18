---
type: summary
title: "Lecture 4: Visualising Data"
description: "Principles of creating good graphs, choosing the right graph type, and utilizing ggplot2 in R."
tags: [data visualization, ggplot2, R, histogram, boxplot, scatterplot]
timestamp: 2026-07-18
sources: ["Lecture 4. Visualising data - notes.pdf"]
---

# Lecture 4: Visualising Data

## Principles of a Good Graph
A good graph is simple, highlights important information, has clear labels/keys, shows underlying data distributions where possible, and does not distort scales.
Visualising early is essential to catch outliers, mistakes, check distribution shapes, and understand relationships (e.g., Anscombe’s quartet demonstrates how datasets with identical statistical properties can look radically different).
*(Source: Lecture 4. Visualising data - notes.pdf)*

## Data Visualisation in R
The `ggplot2` package from the `tidyverse` is used for creating graphs in R. The type of graph depends on the variables (see [[Variables_and_Measurement]]):
- **Single numeric variable**: Histogram, density plot, or box plot.
- **Single categorical variable**: Bar chart. (Pie charts are not recommended).
- **One numeric, one categorical variable**: Box plots or Violin plots. The lecture advises against using bar charts for this purpose as they hide underlying distribution details.
- **Two numeric variables**: Scatterplot (often with a line of best fit and confidence intervals).

See [[Data_Visualization]] for a deeper dive into these graph types.
*(Source: Lecture 4. Visualising data - notes.pdf)*
