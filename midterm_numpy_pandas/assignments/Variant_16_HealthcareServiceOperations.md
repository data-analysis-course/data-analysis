You are a data analyst for a company operating in the **Healthcare Service Operations** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `16_healthcare_raw.csv` — main dataset, 820 rows, 12 columns, with intentional data quality problems.
- `16_healthcare_lookup.csv` — reference table; merge key: `Department`.

Key columns: `Department` (merge key), `Consultation Fee` (main monetary indicator), `Waiting Time Min` (quantity-type column, stored as text), `Visit Date` (mixed date formats), `Clinic` (location).

## Data quality notes
- `Waiting Time Min` is stored as text but must be numeric.
- `Department` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Department` values are missing; some name values are recorded as "N/A".
- `Visit Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `Consultation Fee` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `16_healthcare_raw.csv` and `16_healthcare_lookup.csv` with `pd.read_csv()`.

1. List data types of all columns using `.dtypes`.
2. Report the number of rows and columns using `.shape`.
3. Display the first 10 rows using `.head(10)`.
4. Identify duplicate records using `.duplicated().sum()` and show several examples.
5. Identify missing values in every column using `.isna().sum()`.
6. Investigate unique values of `Department` and `Follow-up Required` to find inconsistent entries.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
2. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
3. Convert `Visit Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
4. Standardize inconsistent values in `Department`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
5. Convert `Waiting Time Min` from text to a numeric type using `astype()`.
6. Identify outliers in `Consultation Fee` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
7. Rename `Consultation Fee` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
8. Merge the lookup dataset `16_healthcare_lookup.csv` with the main dataset on `Department` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Waiting Time Min` and `Consultation Fee` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 6 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `Consultation Fee` array extract the first eight values by slicing and elements at even positions using a step (`arr[:8]`, `arr[::2]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **transaction value = Waiting Time Min × Consultation Fee** (`value = qty_arr * price_arr`). State the units of the result and interpret what it means for one record in the Healthcare Service Operations scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 6 values of your calculated metric as an array of shape (6, 1). Multiply it by a coefficient array of shape (3,) with values 0.90, 1.00, 1.10 using broadcasting. Explain why shapes (6, 1) and (3,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Consultation Fee` is at least 3000 KGS AND NOT (`Waiting Time Min` is above 25). Use the `&` with `~` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute row means with `mean(axis=1)` and column standard deviations with `std(axis=0)`; explain both axes. Then calculate variance, standard deviation and range using `np.var`, `np.std`, max-minus-min. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Category leaders.** Using `groupby()` and `agg()`, calculate total and mean `Consultation Fee` for each `Department`; identify the leader by total and by average.
2. **Pivot comparison.** Using `pivot_table()` with `values="Consultation Fee"`, `index="Clinic"`, `columns="Department"`, `aggfunc="mean"` and `fill_value=0`, compare average performance across the matrix.
3. **Crosstab.** Using `pd.crosstab()`, show counts by `Clinic` and `Follow-up Required`; interpret the structure.
4. **Smallest values.** Using `nsmallest(5, "Consultation Fee")`, find the weakest records and discuss their business meaning.
5. **Ranking.** Using `groupby()` and `rank(method="dense")`, rank `Consultation Fee` within each `Clinic` and find the top 3 per Clinic.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `Clinic` and `Department` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Box:** Box plot of Consultation Fee by `Department`. Insight: differences in spread and outliers between categories.
2. **Hbar:** Horizontal bar chart of total Consultation Fee by `Department`. Insight: which category dominates.
3. **Line:** Line chart of total Consultation Fee by month, grouping `Visit Date` by month with covered Pandas grouping. Insight: the trend over time.
4. **Hist:** Histogram of Consultation Fee per record. Insight: typical value and skewness.
5. **Grouped Bar:** Grouped bar chart of total Consultation Fee by `Clinic` for the two largest `Department` values. Insight: category performance differs by Clinic.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Average (Mean)

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
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
- `Variant_16.ipynb` with code, Markdown explanations and interpretations.
- `16_healthcare_raw.csv` and `16_healthcare_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
