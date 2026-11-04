You are a data analyst for a company operating in the **Travel Agency Booking Analysis** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `29_travel_agency_raw.csv` — main dataset, 820 rows, 12 columns, with intentional data quality problems.
- `29_travel_agency_lookup.csv` — reference table; merge key: `Tour Type`.

Key columns: `Tour Type` (merge key), `Tour Price` (main monetary indicator), `Destination Country` (quantity-type column, stored as text), `Booking Date` (mixed date formats), `Office` (location).

## Data quality notes
- `Destination Country` is stored as text but must be numeric.
- `Tour Type` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Tour Type` values are missing; some name values are recorded as "N/A".
- `Booking Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `Tour Price` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `29_travel_agency_raw.csv` and `29_travel_agency_lookup.csv` with `pd.read_csv()`.

1. Examine column names and data types using `.info()`.
2. Report the number of rows and columns using `.shape`.
3. Display the first 10 rows using `.head(10)`.
4. Investigate unique values of `Tour Type` and `Payment Method` to find inconsistent entries.
5. Identify missing values in every column using `.isna().sum()`.
6. Identify duplicate records using `.duplicated().sum()` and show several examples.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Identify outliers in `Tour Price` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
2. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
3. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
4. Standardize inconsistent values in `Tour Type`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
5. Convert `Booking Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
6. Convert `Destination Country` from text to a numeric type using `astype()`.
7. Rename `Tour Price` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
8. Merge the lookup dataset `29_travel_agency_lookup.csv` with the main dataset on `Tour Type` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Destination Country` and `Tour Price` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 10 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `Tour Price` array extract the first five values by indexing and rows 5-9 by slicing (`arr[:5]`, `arr[5:10]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **transaction value = Destination Country × Tour Price** (`value = qty_arr * price_arr`). State the units of the result and interpret what it means for one record in the Travel Agency Booking Analysis scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 10 values of your calculated metric as an array of shape (10, 1). Multiply it by a coefficient array of shape (4,) with values 0.85, 1.00, 1.15, 1.30 using broadcasting. Explain why shapes (10, 1) and (4,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Destination Country` is at least 5 AND `Tour Price` is at least 2000 KGS. Use the `&` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute column totals with `sum(axis=0)` and row means with `mean(axis=1)`; explain both axes. Then calculate mean, median and interquartile range (Q3 - Q1) using `np.mean`, `np.median`, `np.percentile`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Branch totals.** Using `groupby()` and `agg()`, calculate total, mean and count of `Tour Price` for each `Office`. Which Office leads in total and which in average?
2. **Pivot comparison.** Using `pivot_table()` with `values="Tour Price"`, `index="Tour Type"`, `columns="Payment Method"`, `aggfunc="sum"` and `fill_value=0`, identify the strongest category-payment cell.
3. **Ranking.** Using `groupby()` and `rank(method="average")`, rank `Tour Price` within each `Tour Type` and find the top 3 per category.
4. **Descriptive statistics.** Using `describe()` and `agg()`, report total, mean, median, minimum and maximum of `Tour Price`; interpret the spread.
5. **Reshaping.** Melt the Office-by-Tour Type pivot into long format and explain the difference between wide and long data.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `Office` and `Tour Type` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Hbar:** Horizontal bar chart of total Tour Price by `Tour Type`. Insight: which category dominates.
2. **Scatter:** Scatter plot of `Destination Country` versus `Tour Price`. Insight: whether larger orders tend to have higher values.
3. **Line:** Line chart of total Tour Price by month, grouping `Booking Date` by month with covered Pandas grouping. Insight: the trend over time.
4. **Hist:** Histogram of Tour Price per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total Tour Price by `Tour Type`. Insight: concentration of Tour Price.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Top-3 Concentration

$$
\text{Top-3 Share} = \frac{\sum_{i=1}^{3} x_{(i)}}{\sum_{i=1}^{n} x_i} \times 100\%
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
- `Variant_29.ipynb` with code, Markdown explanations and interpretations.
- `29_travel_agency_raw.csv` and `29_travel_agency_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
