You are a data analyst for a company operating in the **Mobile App Sales and Usage** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `14_mobile_app_raw.csv` — main dataset, 840 rows, 12 columns, with intentional data quality problems.
- `14_mobile_app_lookup.csv` — reference table; merge key: `App Category`.

Key columns: `App Category` (merge key), `In-App Purchases` (main monetary indicator), `sessions_raw` (quantity-type column, stored as text), `Last Active Date` (mixed date formats), `City` (location).

## Data quality notes
- `sessions_raw` is stored as text but must be numeric.
- `App Category` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `App Category` values are missing; some name values are recorded as "N/A".
- `Last Active Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `In-App Purchases` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `14_mobile_app_raw.csv` and `14_mobile_app_lookup.csv` with `pd.read_csv()`.

1. Report the number of rows and columns using `.shape`.
2. Display the first 10 rows using `.head(10)`.
3. Examine column names and data types using `.info()`.
4. Investigate unique values of `App Category` and `User ID` to find inconsistent entries.
5. Identify missing values in every column using `.isna().sum()`.
6. Identify duplicate records using `.duplicated().sum()` and show several examples.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
2. Standardize inconsistent values in `App Category`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
3. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
4. Identify outliers in `In-App Purchases` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
5. Convert `sessions_raw` from text to a numeric type using `astype()`.
6. Convert `Last Active Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
7. Rename `In-App Purchases` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
8. Merge the lookup dataset `14_mobile_app_lookup.csv` with the main dataset on `App Category` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `sessions_raw` and `In-App Purchases` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 12 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `In-App Purchases` array extract the last four values using negative indexing and every third element using a step (`arr[-4:]`, `arr[::3]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **transaction value = sessions_raw × In-App Purchases** (`value = qty_arr * price_arr`). State the units of the result and interpret what it means for one record in the Mobile App Sales and Usage scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 12 values of your calculated metric as an array of shape (12, 1). Multiply it by a coefficient array of shape (4,) with values 0.85, 1.00, 1.15, 1.30 using broadcasting. Explain why shapes (12, 1) and (4,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `In-App Purchases` is above 5000 KGS OR `sessions_raw` is greater than 20. Use the `|` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute row maximums with `max(axis=1)` and column means with `mean(axis=0)`; explain both axes. Then calculate 25th, 50th and 75th percentiles using `np.percentile` with q=25, 50, 75. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Payment structure.** Using `pd.crosstab()` with `normalize="columns"`, show how `App Category` is distributed within each `User ID`. Interpret the column percentages.
2. **Group aggregation.** Using `groupby()` and `agg()`, calculate total, mean and record count of `In-App Purchases` for each `City`. Which City leads in total and which in average?
3. **Pivot with sum.** Using `pivot_table()` with `values="In-App Purchases"`, `index="App Category"`, `columns="City"`, `aggfunc="sum"` and `margins=True`, find the grand total and the leading cell.
4. **Ranking.** Using `groupby()` and `rank(method="first")`, rank `In-App Purchases` within each `City` and find the top 3 per City.
5. **Reshaping.** Convert the App Category-by-City pivot to long format with `melt()` and back with `pivot()`.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `City` and `App Category` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Bar:** Bar chart of total In-App Purchases by `City`. Insight: which City leads.
2. **Box:** Box plot of In-App Purchases by `App Category`. Insight: differences in spread and outliers between categories.
3. **Line:** Line chart of total In-App Purchases by month, grouping `Last Active Date` by month with covered Pandas grouping. Insight: the trend over time.
4. **Hist:** Histogram of In-App Purchases per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total In-App Purchases by `App Category`. Insight: concentration of In-App Purchases.

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



## Expected deliverables
- `Variant_14.ipynb` with code, Markdown explanations and interpretations.
- `14_mobile_app_raw.csv` and `14_mobile_app_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
