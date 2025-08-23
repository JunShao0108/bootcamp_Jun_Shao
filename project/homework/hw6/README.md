Housing Price Prediction Project - HW6
This project implements a modular data cleaning workflow for a stock dataset from Alpha Vantage (AAPL daily data), extending lecture concepts on systematic data cleaning. The notebook notebooks/stage06_data-cleaning.ipynb loads the raw dataset from data/raw/api_alphavantage_AAPL_20250820-1804.csv, applies cleaning functions from src/cleaning.py (fill missing values, drop missing rows, normalize data), saves the cleaned dataset to data/processed/, and compares original vs. cleaned data. Environment variables from .env define paths, ensuring reproducibility. The cleaning strategy and assumptions are documented below and in the notebook.
Cleaning Strategy
Cleaning Functions

fill_missing_median(df, columns): Fills missing values in numeric columns (open, high, low, close, volume) with their median to preserve distribution and avoid outlier bias.
drop_missing(df): Drops rows with any remaining missing values to ensure a complete dataset, applied after filling.
normalize_data(df, columns): Applies Min-Max normalization to scale numeric columns to [0, 1], improving suitability for machine learning models.

Processing Logic

Load raw dataset from data/raw/api_alphavantage_AAPL_20250820-1804.csv (columns: date, open, high, low, close, volume).
Apply fill_missing_median to numeric columns to handle missing values.
Apply drop_missing to ensure no remaining NAs.
Apply normalize_data to numeric columns for scaling.
Save cleaned data to data/processed/cleaned_alphavantage_AAPL_<timestamp>.csv.

Assumptions

Missing values in numeric columns (open, high, low, close, volume) are suitable for median imputation due to potential skewness in stock data.
Dropping rows after median imputation is safe, as Alpha Vantage data typically has minimal missingness.
Normalization is applied to numeric columns only, as date is non-numeric.
CSV output is chosen for readability, though Parquet could be used for efficiency.

Tradeoffs

Median vs. Mean Imputation: Median reduces sensitivity to outliers but may oversimplify distribution.
Dropping Rows: Ensures data completeness but risks losing data if missingness is significant.
Normalization: Min-Max scaling is simple but sensitive to outliers; standardization might be better for some models.
CSV Output: Readable but less efficient than Parquet for large datasets.

Environment-Driven IO

Paths are defined in .env (DATA_DIR_RAW=data/raw, DATA_DIR_PROCESSED=data/processed).
Functions in src/cleaning.py are reusable and modular, supporting different datasets.

