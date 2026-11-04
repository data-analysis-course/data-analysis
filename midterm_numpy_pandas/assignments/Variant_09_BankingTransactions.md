You are a data analyst for a company operating in the **Banking Transactions** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `09_banking_raw.csv` — main dataset, 840 rows, 12 columns, with intentional data quality problems.
- `09_banking_lookup.csv` — reference table; merge key: `Transaction Type`.

Key columns: `Transaction Type` (merge key), `amount_raw` (main monetary indicator), `Balance After` (quantity-type column, stored as text), `Transaction Date` (mixed date formats), `Branch` (location).

## Data quality notes
- `Balance After` is stored as text but must be numeric.
- `Transaction Type` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Transaction Type` values are missing; some name values are recorded as "N/A".
- `Transaction Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `amount_raw` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `09_banking_raw.csv` and `09_banking_lookup.csv` with `pd.read_csv()`.

1. Examine column names and data types using `.info()`.
2. Report the number of rows and columns using `.shape`.
3. Display the first 10 rows using `.head(10)`.
4. Investigate unique values of `Transaction Type` and `Payment Method` to find inconsistent entries.
5. Identify missing values in every column using `.isna().sum()`.
6. Identify duplicate records using `.duplicated().sum()` and show several examples.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Identify outliers in `amount_raw` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
2. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
3. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
4. Standardize inconsistent values in `Transaction Type`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
5. Convert `Transaction Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
6. Convert `Balance After` from text to a numeric type using `astype()`.
7. Rename `amount_raw` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
8. Merge the lookup dataset `09_banking_lookup.csv` with the main dataset on `Transaction Type` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Balance After` and `amount_raw` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 10 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `amount_raw` array extract the first five values by indexing and rows 5-9 by slicing (`arr[:5]`, `arr[5:10]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **average value per unit = amount_raw ÷ Balance After** (`unit_value = price_arr / qty_arr`). State the units of the result and interpret what it means for one record in the Banking Transactions scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 10 values of your calculated metric as an array of shape (10, 1). Multiply it by a coefficient array of shape (5,) with values 0.80, 0.90, 1.00, 1.10, 1.25 using broadcasting. Explain why shapes (10, 1) and (5,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Balance After` is at least 5 AND `amount_raw` is at least 2000 KGS. Use the `&` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute column totals with `sum(axis=0)` and row means with `mean(axis=1)`; explain both axes. Then calculate cumulative sum of the first 10 values and the total sum using `np.cumsum` and `np.sum`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Branch totals.** Using `groupby()` and `agg()`, calculate total, mean and count of `amount_raw` for each `Branch`. Which Branch leads in total and which in average?
2. **Pivot comparison.** Using `pivot_table()` with `values="amount_raw"`, `index="Transaction Type"`, `columns="Payment Method"`, `aggfunc="sum"` and `fill_value=0`, identify the strongest category-payment cell.
3. **Ranking.** Using `groupby()` and `rank(method="min")`, rank `amount_raw` within each `Transaction Type` and find the top 3 per category.
4. **Descriptive statistics.** Using `describe()` and `agg()`, report total, mean, median, minimum and maximum of `amount_raw`; interpret the spread.
5. **Reshaping.** Melt the Branch-by-Transaction Type pivot into long format and explain the difference between wide and long data.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `Branch` and `Transaction Type` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Bar:** Bar chart of total amount_raw by `Branch`. Insight: which Branch leads.
2. **Grouped Bar:** Grouped bar chart of total amount_raw by `Branch` for the two largest `Transaction Type` values. Insight: category performance differs by Branch.
3. **Line:** Line chart of total amount_raw by month, grouping `Transaction Date` by month with covered Pandas grouping. Insight: the trend over time.
4. **Hist:** Histogram of amount_raw per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total amount_raw by `Transaction Type`. Insight: concentration of amount_raw.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Range

$$
\text{Range} = \max(x_i) - \min(x_i)
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
- `Variant_09.ipynb` with code, Markdown explanations and interpretations.
- `09_banking_raw.csv` and `09_banking_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
