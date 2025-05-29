# PandasDataAnalysis

A beginner-friendly data analysis script built with **Pandas 2.2.3** that demonstrates essential DataFrame operations, data cleaning techniques, and basic statistical analysis using Python.

## Features

- Creating and viewing DataFrames
- Inspecting structure with `.info()`, `.head()`, `.tail()`
- Handling missing values:
- Replacing `NaN` with custom values (`"Unknown"` or mean)
- Parsing and formatting dates safely (with error handling)
- Clamping numeric columns within defined ranges
- Calculating correlations (only between numeric columns)
- Manual DataFrame testing

##  Sample Data Used

```text
Name    Score   Date
Alice   88.0    2022-01-01
Bob     92.0    invalid-date
Charlie NaN     2022-01-03
None    70.0    2022-01-04
Eve     85.0    2022-01-05
