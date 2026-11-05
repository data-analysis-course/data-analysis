# Variant 19. Fashion Retail Analytics
You are a data analyst for a company operating in the **Fashion Retail Analytics** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `19_fashion_raw.csv` — main dataset, 840 rows, 12 columns, with intentional data quality problems.
- `19_fashion_lookup.csv` — reference table; merge key: `Season`.

Key columns: `Season` (merge key), `Unit Price` (main monetary indicator), `Units Sold` (quantity-type column, stored as text), `Sale Date` (mixed date formats), `Store` (location).

## Data quality notes
- `Units Sold` is stored as text but must be numeric.
- `Season` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Season` values are missing; some name values are recorded as "N/A".
- `Sale Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `Unit Price` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `19_fashion_raw.csv` and `19_fashion_lookup.csv` with `pd.read_csv()`.

1. Examine column names and data types using `.info()`.
2. Report the number of rows and columns using `.shape`.
3. Display the first 10 rows using `.head(10)`.
4. Investigate unique values of `Season` and `Sale ID` to find inconsistent entries.
5. Identify missing values in every column using `.isna().sum()`.
6. Identify duplicate records using `.duplicated().sum()` and show several examples.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Identify outliers in `Unit Price` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
2. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
3. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
4. Standardize inconsistent values in `Season`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
5. Convert `Sale Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
6. Convert `Units Sold` from text to a numeric type using `astype()`.
7. Rename `Unit Price` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
8. Merge the lookup dataset `19_fashion_lookup.csv` with the main dataset on `Season` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Units Sold` and `Unit Price` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 8 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `Unit Price` array extract rows 10-14 by slicing and the element with the highest value using `np.argmax` (`arr[10:15]`, `arr[np.argmax(arr)]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **net value = (Units Sold × Unit Price) − Discount Percent** (`net = qty_arr * price_arr - extra_arr`). State the units of the result and interpret what it means for one record in the Fashion Retail Analytics scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 8 values of your calculated metric as an array of shape (8, 1). Multiply it by a coefficient array of shape (3,) with values 0.90, 1.00, 1.10 using broadcasting. Explain why shapes (8, 1) and (3,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Units Sold` is between 3 and 15 AND `Unit Price` is below 8000 KGS. Use the `&` with two bounds operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute column minimums with `min(axis=0)` and row totals with `sum(axis=1)`; explain both axes. Then calculate mean, median, standard deviation, minimum and maximum using `np.mean`, `np.median`, `np.std`, `np.min`, `np.max`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Monthly trend.** Group `Sale Date` by month and calculate total `Unit Price` with `groupby()` and `agg()`. Identify the best and worst month.
2. **Pivot table.** Using `pivot_table()` with `values="Unit Price"`, `index="Season"`, `columns="Store"`, `aggfunc="sum"` and `fill_value=0`, find which category leads in each Store.
3. **Ranking.** Using `groupby()` and `rank(method="first")`, rank `Unit Price` within each `Season` and find the top 3 per category.
4. **Crosstab.** Using `pd.crosstab()`, show counts by `Store` and `Sale ID`; interpret the structure.
5. **Reshaping.** Melt the Season-by-Store pivot to long format and restore it with `pivot()`; verify equality.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `Store` and `Season` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Bar:** Bar chart of total Unit Price by `Store`. Insight: which Store leads.
2. **Line:** Line chart of total Unit Price by month, grouping `Sale Date` by month with covered Pandas grouping. Insight: the trend over time.
3. **Scatter:** Scatter plot of `Units Sold` versus `Unit Price`. Insight: whether larger orders tend to have higher values.
4. **Hist:** Histogram of Unit Price per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total Unit Price by `Season`. Insight: concentration of Unit Price.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Minimum

$$
\min(x_1, \dots, x_n)
$$

### Total

$$
\text{Total} = \sum_{i=1}^{n} x_i
$$

### Share of Total

$$
\text{Share, \%} = \frac{\text{Group Total}}{\text{Total}} \times 100\%
$$

**Transaction Value**

$$
\text{Transaction Value} = \text{Quantity} \times \text{Unit Price}
$$

## Expected deliverables
- `Variant_19.ipynb` with code, Markdown explanations and interpretations.
- `19_fashion_raw.csv` and `19_fashion_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
