You are a data analyst for a company operating in the **Product Inventory Management** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `11_inventory_raw.csv` — main dataset, 840 rows, 12 columns, with intentional data quality problems.
- `11_inventory_lookup.csv` — reference table; merge key: `Product Category`.

Key columns: `Product Category` (merge key), `Unit Cost` (main monetary indicator), `units_in_stock_raw` (quantity-type column, stored as text), `Stock Date` (mixed date formats), `Warehouse` (location).

## Data quality notes
- `units_in_stock_raw` is stored as text but must be numeric.
- `Product Category` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Product Category` values are missing; some name values are recorded as "N/A".
- `Stock Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `Unit Cost` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `11_inventory_raw.csv` and `11_inventory_lookup.csv` with `pd.read_csv()`.

1. Report the number of rows and columns using `.shape`.
2. Examine column names and data types using `.info()`.
3. Display the first 10 rows using `.head(10)`.
4. Identify missing values in every column using `.isna().sum()`.
5. Identify duplicate records using `.duplicated().sum()` and show several examples.
6. Investigate unique values of `Product Category` and `Product ID` to find inconsistent entries.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
2. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
3. Standardize inconsistent values in `Product Category`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
4. Convert `units_in_stock_raw` from text to a numeric type using `astype()`.
5. Rename `Unit Cost` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
6. Identify outliers in `Unit Cost` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
7. Convert `Stock Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
8. Merge the lookup dataset `11_inventory_lookup.csv` with the main dataset on `Product Category` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `units_in_stock_raw` and `Unit Cost` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 8 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `Unit Cost` array extract rows 10-14 by slicing and the element with the highest value using `np.argmax` (`arr[10:15]`, `arr[np.argmax(arr)]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **transaction value = units_in_stock_raw × Unit Cost** (`value = qty_arr * price_arr`). State the units of the result and interpret what it means for one record in the Product Inventory Management scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 8 values of your calculated metric as an array of shape (8, 1). Multiply it by a coefficient array of shape (4,) with values 0.85, 1.00, 1.15, 1.30 using broadcasting. Explain why shapes (8, 1) and (4,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `units_in_stock_raw` is between 3 and 15 AND `Unit Cost` is below 8000 KGS. Use the `&` with two bounds operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute column minimums with `min(axis=0)` and row totals with `sum(axis=1)`; explain both axes. Then calculate mean, median and interquartile range (Q3 - Q1) using `np.mean`, `np.median`, `np.percentile`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Quarterly trend.** Group `Stock Date` by quarter and calculate total `Unit Cost` with `groupby()` and `agg()`. Describe the dynamics.
2. **Pivot by category.** Using `pivot_table()` with `values="Unit Cost"`, `index="Product Category"`, `columns="Warehouse"`, `aggfunc="mean"` and `fill_value=0`, find the strongest category-Warehouse cell by average.
3. **Crosstab.** Using `pd.crosstab()` with `normalize="index"`, show the `Product ID` structure within each `Product Category`.
4. **Ranking.** Using `groupby()` and `rank(method="average")`, rank `Unit Cost` within each `Warehouse` and find the top 3 per Warehouse.
5. **Comparison.** Using `sort_values()` and `head()`, find the 5 largest `Unit Cost` records and their common features.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `Warehouse` and `Product Category` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Bar:** Bar chart of total Unit Cost by `Warehouse`. Insight: which Warehouse leads.
2. **Line:** Line chart of total Unit Cost by month, grouping `Stock Date` by month with covered Pandas grouping. Insight: the trend over time.
3. **Scatter:** Scatter plot of `units_in_stock_raw` versus `Unit Cost`. Insight: whether larger orders tend to have higher values.
4. **Hist:** Histogram of Unit Cost per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total Unit Cost by `Product Category`. Insight: concentration of Unit Cost.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Interquartile Range

$$
\text{IQR} = Q_3 - Q_1
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
- `Variant_11.ipynb` with code, Markdown explanations and interpretations.
- `11_inventory_raw.csv` and `11_inventory_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
