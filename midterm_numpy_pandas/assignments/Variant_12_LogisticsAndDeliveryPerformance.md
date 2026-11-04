You are a data analyst for a company operating in the **Logistics and Delivery Performance** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `12_logistics_raw.csv` — main dataset, 820 rows, 12 columns, with intentional data quality problems.
- `12_logistics_lookup.csv` — reference table; merge key: `Delivery Status`.

Key columns: `Delivery Status` (merge key), `Cost` (main monetary indicator), `Weight Kg` (quantity-type column, stored as text), `Dispatch Date` (mixed date formats), `Origin City` (location).

## Data quality notes
- `Weight Kg` is stored as text but must be numeric.
- `Delivery Status` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Delivery Status` values are missing; some name values are recorded as "N/A".
- `Dispatch Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `Cost` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `12_logistics_raw.csv` and `12_logistics_lookup.csv` with `pd.read_csv()`.

1. Display the first 10 rows using `.head(10)`.
2. Report the number of rows and columns using `.shape`.
3. List data types of all columns using `.dtypes`.
4. Identify missing values in every column using `.isna().sum()`.
5. Identify duplicate records using `.duplicated().sum()` and show several examples.
6. Investigate unique values of `Delivery Status` and `Vehicle Type` to find inconsistent entries.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
2. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
3. Standardize inconsistent values in `Delivery Status`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
4. Convert `Dispatch Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
5. Convert `Weight Kg` from text to a numeric type using `astype()`.
6. Rename `Cost` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
7. Identify outliers in `Cost` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
8. Merge the lookup dataset `12_logistics_lookup.csv` with the main dataset on `Delivery Status` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Weight Kg` and `Cost` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 6 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `Cost` array extract the first eight values by slicing and elements at even positions using a step (`arr[:8]`, `arr[::2]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **average value per unit = Cost ÷ Weight Kg** (`unit_value = price_arr / qty_arr`). State the units of the result and interpret what it means for one record in the Logistics and Delivery Performance scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 6 values of your calculated metric as an array of shape (6, 1). Multiply it by a coefficient array of shape (5,) with values 0.80, 0.90, 1.00, 1.10, 1.25 using broadcasting. Explain why shapes (6, 1) and (5,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Cost` is at least 3000 KGS AND NOT (`Weight Kg` is above 25). Use the `&` with `~` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute row means with `mean(axis=1)` and column standard deviations with `std(axis=0)`; explain both axes. Then calculate maximum, minimum, mean and the index of the maximum (`np.argmax`) using `np.max`, `np.min`, `np.mean`, `np.argmax`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Multi-group aggregation.** Using `groupby()` and `agg()` with a dictionary of functions, calculate total, mean and count of `Cost` for each `Origin City` and `Delivery Status`. Identify the strongest and weakest cells.
2. **Pivot ranking.** Using `pivot_table()` with `values="Cost"`, `index="Origin City"`, `columns="Delivery Status"`, `aggfunc="sum"` and `fill_value=0`, rank the row totals with `rank(ascending=False)`.
3. **Crosstab.** Using `pd.crosstab()`, show counts by `Delivery Status` and `Vehicle Type`; interpret the dominant combination.
4. **Smallest values.** Using `nsmallest(3, "Cost")`, find the weakest records and discuss their business meaning.
5. **Reshaping.** Melt the Origin City-by-Delivery Status pivot to long format and explain the uniqueness requirement for `pivot()`.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `Origin City` and `Delivery Status` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Grouped Bar:** Grouped bar chart of total Cost by `Origin City` for the two largest `Delivery Status` values. Insight: category performance differs by Origin City.
2. **Line:** Line chart of total Cost by month, grouping `Dispatch Date` by month with covered Pandas grouping. Insight: the trend over time.
3. **Hist:** Histogram of Cost per record. Insight: typical value and skewness.
4. **Box:** Box plot of Cost by `Delivery Status`. Insight: differences in spread and outliers between categories.
5. **Bar:** Bar chart of total Cost by `Origin City`. Insight: which Origin City leads.

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
- `Variant_12.ipynb` with code, Markdown explanations and interpretations.
- `12_logistics_raw.csv` and `12_logistics_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
