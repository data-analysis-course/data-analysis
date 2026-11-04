You are a data analyst for a company operating in the **Hotel Booking Analysis** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `05_hotel_raw.csv` — main dataset, 840 rows, 12 columns, with intentional data quality problems.
- `05_hotel_lookup.csv` — reference table; merge key: `Room Type`.

Key columns: `Room Type` (merge key), `room_price_raw` (main monetary indicator), `Nights` (quantity-type column, stored as text), `Booking Date` (mixed date formats), `City` (location).

## Data quality notes
- `Nights` is stored as text but must be numeric.
- `Room Type` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Room Type` values are missing; some name values are recorded as "N/A".
- `Booking Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `room_price_raw` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `05_hotel_raw.csv` and `05_hotel_lookup.csv` with `pd.read_csv()`.

1. Display the first 10 rows using `.head(10)`.
2. Examine column names and data types using `.info()`.
3. Report the number of rows and columns using `.shape`.
4. Identify missing values in every column using `.isna().sum()`.
5. Investigate unique values of `Room Type` and `Payment Method` to find inconsistent entries.
6. Identify duplicate records using `.duplicated().sum()` and show several examples.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
2. Standardize inconsistent values in `Room Type`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
3. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
4. Convert `Booking Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
5. Rename `room_price_raw` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
6. Convert `Nights` from text to a numeric type using `astype()`.
7. Identify outliers in `room_price_raw` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
8. Merge the lookup dataset `05_hotel_lookup.csv` with the main dataset on `Room Type` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Nights` and `room_price_raw` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 10 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `room_price_raw` array extract the first five values by indexing and rows 5-9 by slicing (`arr[:5]`, `arr[5:10]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **transaction value = Nights × room_price_raw** (`value = qty_arr * price_arr`). State the units of the result and interpret what it means for one record in the Hotel Booking Analysis scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 10 values of your calculated metric as an array of shape (10, 1). Multiply it by a coefficient array of shape (4,) with values 0.85, 1.00, 1.15, 1.30 using broadcasting. Explain why shapes (10, 1) and (4,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Nights` is at least 5 AND `room_price_raw` is at least 2000 KGS. Use the `&` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute column totals with `sum(axis=0)` and row means with `mean(axis=1)`; explain both axes. Then calculate mean, median and interquartile range (Q3 - Q1) using `np.mean`, `np.median`, `np.percentile`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Quarterly aggregation.** Group `Booking Date` by quarter using `groupby()` on a derived period column, then calculate total `room_price_raw` per quarter with `agg()`. Describe the trend.
2. **Pivot by branch.** Using `pivot_table()` with `values="room_price_raw"`, `index="City"`, `columns="Room Type"`, `aggfunc="mean"` and `fill_value=0`, find the strongest City-Room Type combination by average.
3. **Crosstab.** Using `pd.crosstab()`, show record counts by `Room Type` and `Payment Method`; identify the dominant combination.
4. **Ranking.** Using `groupby()` and `rank(method="dense")`, rank `room_price_raw` within each `City` and find the top 3 per City.
5. **Reshaping.** Melt the City-by-Room Type pivot into long format and explain the uniqueness requirement for `pivot()`.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `City` and `Room Type` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Hbar:** Horizontal bar chart of total room_price_raw by `Room Type`. Insight: which category dominates.
2. **Scatter:** Scatter plot of `Nights` versus `room_price_raw`. Insight: whether larger orders tend to have higher values.
3. **Line:** Line chart of total room_price_raw by month, grouping `Booking Date` by month with covered Pandas grouping. Insight: the trend over time.
4. **Hist:** Histogram of room_price_raw per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total room_price_raw by `Room Type`. Insight: concentration of room_price_raw.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Standard Deviation

$$
s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}
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
- `Variant_05.ipynb` with code, Markdown explanations and interpretations.
- `05_hotel_raw.csv` and `05_hotel_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
