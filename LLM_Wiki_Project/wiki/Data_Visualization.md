---
type: concept
title: "Data Visualization"
description: "Techniques and principles for visually exploring and presenting data."
tags: [graphs, data visualization, ggplot2, distributions]
timestamp: 2026-07-18
sources: ["Lecture 3. Summarising data - notes.pdf", "Lecture 4. Visualising data - notes.pdf"]
---

# Data Visualization

Visualizing data is a critical early step in the [[Research_Process]] to spot outliers, check distribution assumptions, and inform further [[Descriptive_Statistics]] and inferential analysis.

## Graph Selection
The appropriate graph heavily depends on the data type (see [[Variables_and_Measurement]]):

### Single Numeric Variable
- **Histogram**: Visualizes the frequencies of numeric data by grouping continuous variables into 'bins'. It can display absolute values, percentages (density), or cumulative totals.
- **Density Plot**: A smoothed continuous version of a histogram, showing the 'shape' of the data.
- **Box Plot**: Summarises distribution through the median, interquartile range, and outliers.

### Single Categorical Variable
- **Bar Chart**: Visualizes frequencies or proportions of categories. Bar charts are preferred over pie charts, as human perception struggles to accurately judge angles.

### Mixed Variables (Numeric and Categorical)
- **Box Plot / Violin Plot**: When comparing a numeric outcome across categorical groups, box plots and violin plots are recommended. *Bar charts should be avoided* for showing group means, as they obscure the underlying data distribution and variance.

### Two Numeric Variables
- **Scatterplot**: Visualizes the association between two continuous variables. Each point represents an observation.

## Anscombe's Quartet
Visualising early is crucial. Anscombe’s quartet consists of four datasets that share identical summary statistics (mean, variance, correlation), but look radically different when plotted on a scatterplot.

*(Sources: Lecture 3. Summarising data - notes.pdf, Lecture 4. Visualising data - notes.pdf)*
