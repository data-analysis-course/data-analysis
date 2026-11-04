You are a data analyst for a company operating in the **Online Education Platform Analysis** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `25_education_raw.csv` — main dataset, 840 rows, 12 columns, with intentional data quality problems.
- `25_education_lookup.csv` — reference table; merge key: `Course Category`.

Key columns: `Course Category` (merge key), `course_fee_raw` (main monetary indicator), `Progress Percent` (quantity-type column, stored as text), `Enrollment Date` (mixed date formats), `City` (location).

## Data quality notes
- `Progress Percent` is stored as text but must be numeric.
- `Course Category` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Course Category` values are missing; some name values are recorded as "N/A".
- `Enrollment Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `course_fee_raw` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `25_education_raw.csv` and `25_education_lookup.csv` with `pd.read_csv()`.

1. Display the first 10 rows using `.head(10)`.
2. Examine column names and data types using `.info()`.
3. Report the number of rows and columns using `.shape`.
4. Identify missing values in every column using `.isna().sum()`.
5. Investigate unique values of `Course Category` and `Enrollment ID` to find inconsistent entries.
6. Identify duplicate records using `.duplicated().sum()` and show several examples.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
2. Standardize inconsistent values in `Course Category`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
3. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
4. Convert `Enrollment Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
5. Rename `course_fee_raw` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
6. Convert `Progress Percent` from text to a numeric type using `astype()`.
7. Identify outliers in `course_fee_raw` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
8. Merge the lookup dataset `25_education_lookup.csv` with the main dataset on `Course Category` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Progress Percent` and `course_fee_raw` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 10 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `course_fee_raw` array extract the first five values by indexing and rows 5-9 by slicing (`arr[:5]`, `arr[5:10]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **transaction value = Progress Percent × course_fee_raw** (`value = qty_arr * price_arr`). State the units of the result and interpret what it means for one record in the Online Education Platform Analysis scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 10 values of your calculated metric as an array of shape (10, 1). Multiply it by a coefficient array of shape (3,) with values 0.90, 1.00, 1.10 using broadcasting. Explain why shapes (10, 1) and (3,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Progress Percent` is at least 5 AND `course_fee_raw` is at least 2000 KGS. Use the `&` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute column totals with `sum(axis=0)` and row means with `mean(axis=1)`; explain both axes. Then calculate mean, median, standard deviation, minimum and maximum using `np.mean`, `np.median`, `np.std`, `np.min`, `np.max`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Monthly dynamics.** Group `Enrollment Date` by month and calculate total `course_fee_raw` with `groupby()` and `agg()`. Identify the peak month.
2. **Pivot comparison.** Using `pivot_table()` with `values="course_fee_raw"`, `index="City"`, `columns="Course Category"`, `aggfunc="mean"` and `fill_value=0`, find the strongest City-Course Category combination by average.
3. **Crosstab.** Using `pd.crosstab()`, show counts by `Course Category` and `Enrollment ID`; interpret the structure.
4. **Ranking.** Using `groupby()` and `rank(method="dense")`, rank `course_fee_raw` within each `Course Category` and find the top 3 per category.
5. **Top and bottom.** Using `nlargest(3, "course_fee_raw")` and `nsmallest(3, "course_fee_raw")`, compare the extremes and interpret the gap.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `City` and `Course Category` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Bar:** Bar chart of total course_fee_raw by `City`. Insight: which City leads.
2. **Grouped Bar:** Grouped bar chart of total course_fee_raw by `City` for the two largest `Course Category` values. Insight: category performance differs by City.
3. **Line:** Line chart of total course_fee_raw by month, grouping `Enrollment Date` by month with covered Pandas grouping. Insight: the trend over time.
4. **Hist:** Histogram of course_fee_raw per record. Insight: typical value and skewness.
5. **Pie:** Pie chart of the share of total course_fee_raw by `Course Category`. Insight: concentration of course_fee_raw.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Variance

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
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
- `Variant_25.ipynb` with code, Markdown explanations and interpretations.
- `25_education_raw.csv` and `25_education_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
