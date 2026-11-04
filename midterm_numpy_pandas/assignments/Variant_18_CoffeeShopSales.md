You are a data analyst for a company operating in the **Coffee Shop Sales** domain in Kyrgyzstan. Management needs an evidence-based report to support decisions. All monetary amounts are in KGS. Each row represents one record; the ID column identifies it. Data are synthetic.

## Dataset files
- `18_coffee_raw.csv` — main dataset, 820 rows, 12 columns, with intentional data quality problems.
- `18_coffee_lookup.csv` — reference table; merge key: `Product Category`.

Key columns: `Product Category` (merge key), `Unit Price` (main monetary indicator), `Quantity` (quantity-type column, stored as text), `Order Date` (mixed date formats), `Shop Branch` (location).

## Data quality notes
- `Quantity` is stored as text but must be numeric.
- `Product Category` contains inconsistent entries: different letter cases and leading/trailing spaces.
- Some `Product Category` values are missing; some name values are recorded as "N/A".
- `Order Date` uses mixed date formats (YYYY-MM-DD and DD.MM.YYYY).
- `Unit Price` contains several extreme outliers.
- Column names and order are inconvenient and must be corrected.
- Missing values cannot always be reliably inferred; justify every decision.

## General instructions
Work individually. Use only NumPy, Pandas and Matplotlib methods covered during the course. Preserve the original raw files. Explain every cleaning and analytical decision in Markdown. Interpret every result in business terms. Submit one Jupyter Notebook, both original CSV files and `cleaned_data.csv`. Run the notebook from start to finish before submission.

## TASK 1. Initial Data Exploration
Load `18_coffee_raw.csv` and `18_coffee_lookup.csv` with `pd.read_csv()`.

1. Display the first 10 rows using `.head(10)`.
2. Identify missing values in every column using `.isna().sum()`.
3. Report the number of rows and columns using `.shape`.
4. Examine column names and data types using `.info()`.
5. Identify duplicate records using `.duplicated().sum()` and show several examples.
6. Investigate unique values of `Product Category` and `Payment Method` to find inconsistent entries.
7. Separate numerical and categorical variables, then describe all identified data quality problems in Markdown with examples.

## TASK 2. Data Cleaning and Preparation

1. Convert `Order Date` to datetime with `pd.to_datetime()`. The column uses mixed formats; handle them correctly and explain how.
2. Handle missing values using an appropriate covered method. Justify your choice; do not invent values.
3. Remove duplicate records with `drop_duplicates()` and report how many rows were removed.
4. Standardize inconsistent values in `Product Category`: trim spaces, unify letter case, and merge equivalent names (for example, IT / it / ИТ / Информационные технологии, if present). Document your mapping.
5. Convert `Quantity` from text to a numeric type using `astype()`.
6. Rename `Unit Price` (and any other inconvenient column names) using consistent naming conventions, then reorder columns logically.
7. Identify outliers in `Unit Price` using a simple covered approach. State your threshold, report how many values were treated, and justify your decision.
8. Merge the lookup dataset `18_coffee_lookup.csv` with the main dataset on `Product Category` using the combining method studied in class. Preserve all main records, explain your merge type, and report unmatched categories.
9. Check the cleaned dataset for remaining problems and save it as `cleaned_data.csv` with `to_csv(index=False)`.

## TASK 3. NumPy Practical Application

### 3.1 Array creation and conversion
Convert `Quantity` and `Unit Price` into NumPy arrays with `np.array()`. Report `.shape`, `.ndim`, `.size` and `.dtype` for both. Create a third array of 12 scenario coefficients using `np.linspace()` from 0.8 to 1.2. Explain the difference between a list and a NumPy array.

### 3.2 Indexing and slicing
From the `Unit Price` array extract the last four values using negative indexing and every third element using a step (`arr[-4:]`, `arr[::3]`). Explain what each operation returns and how indexing differs from slicing.

### 3.3 Vectorization
Without Python loops, calculate the business metric: **average value per unit = Unit Price ÷ Quantity** (`unit_value = price_arr / qty_arr`). State the units of the result and interpret what it means for one record in the Coffee Shop Sales scenario. Explain why this vectorized operation is faster than a `for` loop (performance optimization).

### 3.4 Broadcasting
Take the first 12 values of your calculated metric as an array of shape (12, 1). Multiply it by a coefficient array of shape (3,) with values 0.90, 1.00, 1.10 using broadcasting. Explain why shapes (12, 1) and (3,) are compatible, what each resulting column means, and how broadcasting differs from element-wise multiplication of two same-shape arrays.

### 3.5 Boolean indexing
Using NumPy boolean indexing, select records where `Unit Price` is above 5000 KGS OR `Quantity` is greater than 20. Use the `|` operator(s). Report how many records match and their total metric value. Interpret the result for management.

### 3.6 Statistical calculations and aggregation along axes
For your broadcasting result matrix, compute row maximums with `max(axis=1)` and column means with `mean(axis=0)`; explain both axes. Then calculate maximum, minimum, mean and the index of the maximum (`np.argmax`) using `np.max`, `np.min`, `np.mean`, `np.argmax`. Do not add values with different units. Interpret one result in the business context.

### 3.7 Performance optimization
Explain in Markdown why vectorized NumPy operations are faster than Python `for` loops, using concepts covered in class.
## TASK 4. Business-Oriented Data Analysis
Answer each question with Pandas code and a short business interpretation. Use only methods covered during the course.

1. **Categorical relationship.** Using `pd.crosstab()`, build a table of record counts by `Product Category` and `Payment Method`. Identify the most common combination and explain what it means for the business.
2. **Pivot with margins.** Using `pivot_table()` with `values="Unit Price"`, `index="Shop Branch"`, `columns="Product Category"`, `aggfunc="sum"` and `margins=True`, find the grand total and the strongest cell.
3. **Group ranking.** Using `groupby()` and `agg()`, calculate total `Unit Price` per `Shop Branch`; then rank the Shop Branchs with `rank(ascending=False)`.
4. **Top values.** Using `nlargest(5, "Unit Price")`, identify the largest records and interpret their share of the total.
5. **Reshaping.** Convert the Product Category-by-Shop Branch pivot to long format with `melt()` and back with `pivot()`.
## TASK 5. Business Interpretation
In Markdown cells:
1. Identify **three** important business patterns supported by your calculations.
2. Compare key indicators between `Shop Branch` and `Product Category` groups; identify the strongest and weakest areas.
3. Give **1-2 practical recommendations** to management, supported by specific numbers from your analysis.

## Matplotlib Visualization Requirements
Create exactly five visualizations using Matplotlib. Each chart must have a title, axis labels where applicable, and a short interpretation.

1. **Hbar:** Horizontal bar chart of total Unit Price by `Product Category`. Insight: which category dominates.
2. **Line:** Line chart of total Unit Price by month, grouping `Order Date` by month with covered Pandas grouping. Insight: the trend over time.
3. **Hist:** Histogram of Unit Price per record. Insight: typical value and skewness.
4. **Box:** Box plot of Unit Price by `Product Category`. Insight: differences in spread and outliers between categories.
5. **Pie:** Pie chart of the share of total Unit Price by `Product Category`. Insight: concentration of Unit Price.

## FORMULAS USED IN THIS VARIANT

### Key indicator of this variant: Maximum

$$
\max(x_1, \dots, x_n)
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
- `Variant_18.ipynb` with code, Markdown explanations and interpretations.
- `18_coffee_raw.csv` and `18_coffee_lookup.csv` (unmodified).
- `cleaned_data.csv`.
- Five Matplotlib charts inside the notebook.
