

Housing Price Prediction Project
This project builds a machine learning model to predict housing prices in Ames, Iowa, using the Kaggle House Prices dataset. It helps real estate investors identify undervalued properties and optimize returns by analyzing features like lot size, neighborhood, and overall quality. The model uses metrics like RMSE for evaluation and supports data-driven decisions.
Stakeholder Context

Who: Real estate analysts and portfolio managers.
Needs: Accurate predictions, interpretable results (e.g., key feature visualizations), reliable metrics (e.g., RMSE), and risk insights (e.g., data quality issues).
Focus: Robust pipeline for missing data, outliers, and features, with clear reports.

Project Structure

/data/: Datasets.

/data/raw/: Original files (e.g., train.csv, test.csv).
/data/processed/: Cleaned data (e.g., preprocessed_train.csv, selected_train.csv, updated_encoded_train.csv).


/notebooks/: Analysis notebooks (e.g., feature_selection.ipynb, encoding.ipynb).
/src/: Scripts (e.g., utils.py, cleaning.py).
/docs/: Documentation (e.g., stakeholder_memo.md).
README.md: Overview.
requirements.txt: Dependencies.
.env: Environment variables (e.g., DATA_DIR_RAW).
.env.example: Template.

Tooling Setup

Environment: Conda (fe-course, Python 3.11) with dependencies (pandas, numpy, scikit-learn).
Version Control: GitHub with .gitignore for sensitive files.
Reproducibility: Use .env for paths (e.g., ../data/raw/ from notebooks).

Python Fundamentals

Notebook: /notebooks/python_fundamentals_summary.ipynb loads train.csv, performs NumPy/pandas operations (e.g., stats on SalePrice by Neighborhood), and uses src/utils.py (e.g., clean_column_names, convert_year_to_age).

Data Storage

Structure: Raw in /data/raw/, processed in /data/processed/.
Formats: CSV for readability.
Reading/Writing: Use os.getenv for paths; pd.read_csv for input; save_data in src/utils.py for output.

Data Preprocessing

Notebook: /notebooks/data_preprocessing.ipynb cleans train.csv (missing values via median/'None', duplicates, normalization, one-hot encoding) using src/cleaning.py, saves to preprocessed_train.csv.
Recent Operations (in /notebooks/feature_selection.ipynb and encoding.ipynb):

Feature Selection: From preprocessed_train.csv, retain ~40 high-impact columns (e.g., OverallQual, GrLivArea, Neighborhood_* one-hot) based on correlation (>0.5 with SalePrice) and domain knowledge; save to selected_train.csv.
Feature Engineering: Add 'age' = YearRemodAdd - YearBuilt (remodel interval).
Encoding Non-Numeric Columns:

Ordinal: BsmtQual (Ex=5, Gd=4, etc.), BsmtExposure (Gd=4, Av=3, etc.), KitchenQual (Ex=5, etc.), GarageFinish (Fin=3, etc.); None/NA=0.
Nominal: One-hot with drop_first=True (e.g., BldgType_TwnhsE=1 if TwnhsE).


Column Removal: Drop year-related ('YearBuilt', 'YearRemodAdd', 'GarageYrBlt', 'YrSold') and month ('MoSold') to avoid regression issues (e.g., trends, multicollinearity); retain 'age'.
Output: updated_encoded_train.csv (fully numeric, ready for modeling).


Assumptions: Median imputation for skewed numerics; 'None' for categoricals; normalization for scaling.
Tradeoffs: Simple imputation vs. advanced (e.g., KNN); one-hot increases dimensions but preserves info.

Goals → Lifecycle → Deliverables

Goal: Predict prices for investment insights.
Lifecycle:

Collection: Kaggle data to /data/raw/.
Preprocessing: Clean/feature engineer in /data/processed/.
Modeling: Train/evaluate in notebooks (e.g., regression).
Evaluation: RMSE/R².
Reporting: Visuals/memos in /docs/.


Deliverables: Cleaned CSVs, scripts, notebooks, memos/visuals.

Assumptions and Risks

Assumptions: Dataset features predict prices; cleaned data generalizes to Ames.
Risks: Missing/outliers reduce accuracy; Ames-specific limits broader use. Mitigate via validation and updates.


### Outlier Handling
- Definition: Outliers detected via IQR (k=1.5) or Z-score (threshold=3.0) on key columns like GrLivArea.
- Assumptions: Data roughly summarized by quartiles (IQR) or normal (Z-score); extremes are anomalies, not regime shifts.
- Risks: Removing true extremes (e.g., luxury homes) underestimates variance; keeping inflates models. Sensitivity tests mitigate.
- Integration: Use src/outliers.py in preprocessing pipeline.

# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

## AI use
I maily used AI for the integrity of the code and the organization of the README file, making the text and code neat and clear.

## the project 9-13 
Please refer to hw9-13 in the homework folder. 

