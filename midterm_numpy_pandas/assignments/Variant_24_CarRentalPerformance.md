# Variant 24. Car Rental Performance Analysis
You are a data analyst for a company operating in the **Car Rental Performance** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `24_car_rental_raw.csv` — main dataset, 840 rows, 12 columns, with intentional data quality problems.
- `24_car_rental_lookup.csv` — reference table; merge key: `Car Type`.

Key columns: `Car Type` (merge key), `Daily Rate` (main monetary indicator), `rental_days_raw` (quantity-type column, stored as text), `Return Date` (mixed date formats), `City` (location).

## Data quality notes
- `rental_days_raw` is stored as text but must be numeric.
- `Car Type` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Car Type` values are missing; some name values are recorded as "N/A".
- `Return Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `Daily Rate` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `24_car_rental_raw.csv` and `24_car_rental_lookup.csv` with `pd.read_csv()`.

1. Report the number of rows and columns using `.shape`.
2. Display the first 10 rows using `.head(10)`.
3. Examine column names and data types using `.info()`.
4. Investigate unique values of `Car Type` and `Payment Method` to find inconsistent entries.
5. Identify missing values in every column using `.isna().sum()`.
6. Identify duplicate records using `.duplicated().sum()` and show several examples.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
2. Standardize inconsistent values in `Car Type`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
3. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
4. Identify outliers in `Daily Rate` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
5. Convert `rental_days_raw` from text to a numeric type using `astype()`.
6. Convert `Return Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
7. Rename `Daily Rate` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
8. Merge the lookup dataset `24_car_rental_lookup.csv` with the main dataset on `Car Type` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `rental_days_raw` and `Daily Rate` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 6 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `Daily Rate` array extract the first eight values by slicing and elements at even positions using a step (`arr[:8]`, `arr[::2]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **average value per unit = Daily Rate ÷ rental_days_raw** (`unit_value = price_arr / qty_arr`). State the units of the result and interpret what it means for one record in the Car Rental Performance scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 6 values of your calculated metric as an array of shape (6, 1). Multiply it by a coefficient array of shape (5,) with values 0.80, 0.90, 1.00, 1.10, 1.25 using broadcasting. Explain why shapes (6, 1) and (5,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Daily Rate` is at least 3000 KGS AND NOT (`rental_days_raw` is above 25). Use the `&` with `~` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute row means with `mean(axis=1)` and column standard deviations with `std(axis=0)`; explain both axes. Then calculate maximum, minimum, mean and the index of the maximum (`np.argmax`) using `np.max`, `np.min`, `np.mean`, `np.argmax`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Multi-group aggregation.** Using `groupby()` and `agg()` with a dictionary of functions, calculate total, mean and count of `Daily Rate` for each `City` and `Car Type`. Identify the strongest and weakest cells.
2. **Pivot ranking.** Using `pivot_table()` with `values="Daily Rate"`, `index="City"`, `columns="Car Type"`, `aggfunc="sum"` and `fill_value=0`, rank the row totals with `rank(ascending=False)`.
3. **Crosstab.** Using `pd.crosstab()`, show counts by `Car Type` and `Payment Method`; interpret the dominant combination.
4. **Smallest values.** Using `nsmallest(3, "Daily Rate")`, find the weakest records and discuss their business meaning.
5. **Reshaping.** Melt the City-by-Car Type pivot to long format and explain the uniqueness requirement for `pivot()`.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `City` and `Car Type` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Box:** Box plot of Daily Rate by `Car Type`. Insight: differences in spread and outliers between categories.
2. **Hbar:** Horizontal bar chart of total Daily Rate by `Car Type`. Insight: which category dominates.
3. **Line:** Line chart of total Daily Rate by month, grouping `Return Date` by month with covered Pandas grouping. Insight: the trend over time.
4. **Hist:** Histogram of Daily Rate per record. Insight: typical value and skewness.
5. **Grouped Bar:** Grouped bar chart of total Daily Rate by `City` for the two largest `Car Type` values. Insight: category performance differs by City.

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

**Transaction Value**

$$
\text{Transaction Value} = \text{Quantity} \times \text{Unit Price}
$$

## Expected deliverables
- `Variant_24.ipynb` with code, Markdown explanations and interpretations.
- `24_car_rental_raw.csv` and `24_car_rental_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
