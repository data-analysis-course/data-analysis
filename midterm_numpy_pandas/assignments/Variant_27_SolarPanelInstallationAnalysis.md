You are a data analyst for a company operating in the **Solar Panel Installation Analysis** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `27_solar_raw.csv` — main dataset, 840 rows, 12 columns, with intentional data quality problems.
- `27_solar_lookup.csv` — reference table; merge key: `Panel Type`.

Key columns: `Panel Type` (merge key), `installation_cost_raw` (main monetary indicator), `System Capacity KW` (quantity-type column, stored as text), `Installation Date` (mixed date formats), `System Capacity KW` (location).

## Data quality notes
- `System Capacity KW` is stored as text but must be numeric.
- `Panel Type` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Panel Type` values are missing; some name values are recorded as "N/A".
- `Installation Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `installation_cost_raw` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `27_solar_raw.csv` and `27_solar_lookup.csv` with `pd.read_csv()`.

1. Report the number of rows and columns using `.shape`.
2. Examine column names and data types using `.info()`.
3. Display the first 10 rows using `.head(10)`.
4. Investigate unique values of `Panel Type` and `Payment Method` to find inconsistent entries.
5. Identify duplicate records using `.duplicated().sum()` and show several examples.
6. Identify missing values in every column using `.isna().sum()`.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Standardize inconsistent values in `Panel Type`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
2. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
3. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
4. Convert `System Capacity KW` from text to a numeric type using `astype()`.
5. Identify outliers in `installation_cost_raw` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
6. Convert `Installation Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
7. Rename `installation_cost_raw` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
8. Merge the lookup dataset `27_solar_lookup.csv` with the main dataset on `Panel Type` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `System Capacity KW` and `installation_cost_raw` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 8 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `installation_cost_raw` array extract rows 10-14 by slicing and the element with the highest value using `np.argmax` (`arr[10:15]`, `arr[np.argmax(arr)]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **average value per unit = installation_cost_raw ÷ System Capacity KW** (`unit_value = price_arr / qty_arr`). State the units of the result and interpret what it means for one record in the Solar Panel Installation Analysis scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 8 values of your calculated metric as an array of shape (8, 1). Multiply it by a coefficient array of shape (5,) with values 0.80, 0.90, 1.00, 1.10, 1.25 using broadcasting. Explain why shapes (8, 1) and (5,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `System Capacity KW` is between 3 and 15 AND `installation_cost_raw` is below 8000 KGS. Use the `&` with two bounds operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute column minimums with `min(axis=0)` and row totals with `sum(axis=1)`; explain both axes. Then calculate cumulative sum of the first 10 values and the total sum using `np.cumsum` and `np.sum`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Quarterly aggregation.** Group `Installation Date` by quarter and calculate total `installation_cost_raw` with `groupby()` and `agg()`. Describe the trend.
2. **Pivot by branch.** Using `pivot_table()` with `values="installation_cost_raw"`, `index="System Capacity KW"`, `columns="Panel Type"`, `aggfunc="sum"` and `fill_value=0`, find the strongest System Capacity KW-Panel Type cell.
3. **Crosstab.** Using `pd.crosstab()` with `normalize="index"`, show the `Payment Method` structure within each `Panel Type`.
4. **Ranking.** Using `groupby()` and `rank(method="min")`, rank `installation_cost_raw` within each `Panel Type` and find the top 3 per category.
5. **Descriptive statistics.** Using `describe()` and `agg()`, report total, mean, median and standard deviation of `installation_cost_raw`; interpret the spread.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `System Capacity KW` and `Panel Type` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Bar:** Bar chart of total installation_cost_raw by `System Capacity KW`. Insight: which System Capacity KW leads.
2. **Line:** Line chart of total installation_cost_raw by month, grouping `Installation Date` by month with covered Pandas grouping. Insight: the trend over time.
3. **Scatter:** Scatter plot of `System Capacity KW` versus `installation_cost_raw`. Insight: whether larger orders tend to have higher values.
4. **Hist:** Histogram of installation_cost_raw per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total installation_cost_raw by `Panel Type`. Insight: concentration of installation_cost_raw.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Mode

$$
\text{Mode} = \arg\max_c \; \text{count}(c)
$$

### Total

$$
\text{Total} = \sum_{i=1}^{n} x_i
$$

### Share of Total

$$
\text{Share, \%} = \frac{\text{Group Total}}{\text{Total}} \times 100\%
$$



## Expected deliverables
- `Variant_27.ipynb` with code, Markdown explanations and interpretations.
- `27_solar_raw.csv` and `27_solar_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
