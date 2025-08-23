Housing Price Prediction Project - HW5

This project implements a reproducible data storage layer for a housing dataset, following the lecture on environment-driven IO, CSV vs Parquet, and folder conventions. The notebook notebooks/stage05_data-storage-preview.ipynb creates a sample DataFrame, saves it as CSV to data/raw/ and Parquet to data/processed/, reloads and validates both files, and uses utility functions from src/utils.py for read/write operations. Environment variables from .env define storage paths, ensuring flexibility. The project includes detailed documentation in the README and notebook, with validation results for shape and data types.

Data Storage

Folder Structure





data/raw/: Stores raw data in CSV format (e.g., sample_20250820-1811.csv). Used for unprocessed data directly from sources.



data/processed/: Stores processed data in Parquet format (e.g., sample_20250820-1811.parquet). Used for optimized, analysis-ready data.

File Formats





CSV: Used in data/raw/ for human-readable, portable storage of raw data. Suitable for initial ingestion but less efficient for large datasets.



Parquet: Used in data/processed/ for columnar storage, efficient compression, and fast querying. Ideal for processed data in analytical workflows.

Read/Write with Environment Variables





The code uses DATA_DIR_RAW and DATA_DIR_PROCESSED from .env to define storage paths (e.g., data/raw, data/processed).



Utility functions write_df and read_df in src/utils.py handle saving/loading based on file suffix (.csv or .parquet), creating directories if missing and handling missing Parquet engines with clear errors.



Example: write_df(df, 'sample_20250820-1811.csv', DATA_DIR_RAW) saves to data/raw/.
