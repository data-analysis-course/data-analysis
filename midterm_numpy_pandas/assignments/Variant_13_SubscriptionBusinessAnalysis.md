You are a data analyst for a company operating in the **Subscription Business Analysis** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `13_subscription_raw.csv` — main dataset, 820 rows, 12 columns, with intentional data quality problems.
- `13_subscription_lookup.csv` — reference table; merge key: `Plan Type`.

Key columns: `Plan Type` (merge key), `Monthly Fee` (main monetary indicator), `Churn Date` (quantity-type column, stored as text), `Start Date` (mixed date formats), `City` (location).

## Data quality notes
- `Churn Date` is stored as text but must be numeric.
- `Plan Type` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Plan Type` values are missing; some name values are recorded as "N/A".
- `Start Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `Monthly Fee` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `13_subscription_raw.csv` and `13_subscription_lookup.csv` with `pd.read_csv()`.

1. Examine column names and data types using `.info()`.
2. Display the first 10 rows using `.head(10)`.
3. Report the number of rows and columns using `.shape`.
4. Identify duplicate records using `.duplicated().sum()` and show several examples.
5. Identify missing values in every column using `.isna().sum()`.
6. Investigate unique values of `Plan Type` and `Auto Renewal` to find inconsistent entries.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Standardize inconsistent values in `Plan Type`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
2. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
3. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
4. Convert `Churn Date` from text to a numeric type using `astype()`.
5. Convert `Start Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
6. Identify outliers in `Monthly Fee` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
7. Rename `Monthly Fee` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
8. Merge the lookup dataset `13_subscription_lookup.csv` with the main dataset on `Plan Type` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Churn Date` and `Monthly Fee` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 10 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `Monthly Fee` array extract the first five values by indexing and rows 5-9 by slicing (`arr[:5]`, `arr[5:10]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **transaction value = Churn Date × Monthly Fee** (`value = qty_arr * price_arr`). State the units of the result and interpret what it means for one record in the Subscription Business Analysis scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 10 values of your calculated metric as an array of shape (10, 1). Multiply it by a coefficient array of shape (3,) with values 0.90, 1.00, 1.10 using broadcasting. Explain why shapes (10, 1) and (3,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Churn Date` is at least 5 AND `Monthly Fee` is at least 2000 KGS. Use the `&` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute column totals with `sum(axis=0)` and row means with `mean(axis=1)`; explain both axes. Then calculate mean, median, standard deviation, minimum and maximum using `np.mean`, `np.median`, `np.std`, `np.min`, `np.max`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Monthly dynamics.** Group `Start Date` by month and calculate total `Monthly Fee` with `groupby()` and `agg()`. Identify the peak month.
2. **Pivot comparison.** Using `pivot_table()` with `values="Monthly Fee"`, `index="City"`, `columns="Plan Type"`, `aggfunc="mean"` and `fill_value=0`, find the strongest City-Plan Type combination by average.
3. **Crosstab.** Using `pd.crosstab()`, show counts by `Plan Type` and `Auto Renewal`; interpret the structure.
4. **Ranking.** Using `groupby()` and `rank(method="dense")`, rank `Monthly Fee` within each `Plan Type` and find the top 3 per category.
5. **Top and bottom.** Using `nlargest(3, "Monthly Fee")` and `nsmallest(3, "Monthly Fee")`, compare the extremes and interpret the gap.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `City` and `Plan Type` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Hbar:** Horizontal bar chart of total Monthly Fee by `Plan Type`. Insight: which category dominates.
2. **Scatter:** Scatter plot of `Churn Date` versus `Monthly Fee`. Insight: whether larger orders tend to have higher values.
3. **Line:** Line chart of total Monthly Fee by month, grouping `Start Date` by month with covered Pandas grouping. Insight: the trend over time.
4. **Hist:** Histogram of Monthly Fee per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total Monthly Fee by `Plan Type`. Insight: concentration of Monthly Fee.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Coefficient of Variation

$$
CV = \frac{s}{\bar{x}} \times 100\%
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
- `Variant_13.ipynb` with code, Markdown explanations and interpretations.
- `13_subscription_raw.csv` and `13_subscription_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
