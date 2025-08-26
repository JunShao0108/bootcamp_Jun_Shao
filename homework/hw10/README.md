# Housing Price Prediction Project - Modeling Regression

This project develops a machine learning model to predict housing prices in Ames, Iowa, using the Kaggle House Prices dataset, enabling real estate investment analysts to identify high-return opportunities. By analyzing 79 features (e.g., lot area, neighborhood, overall quality), the model delivers accurate predictions, evaluated with RMSE and R², to support data-driven decisions. The primary stakeholders are real estate analysts and portfolio managers who value interpretable results and risk insights. The project follows a full lifecycle, with deliverables in structured folders.

## Stakeholder Context
- **Who**: Real estate investment analysts and portfolio managers at investment firms.
- **What They Care About**: Accurate housing price predictions, interpretable results (e.g., visualizations of price trends and key features like GrLivArea, Neighborhood), and reliable performance metrics (e.g., RMSE, R²).
- **Needs**: A robust, reproducible pipeline handling missing data, outliers, and diverse features, delivering clear reports and visualizations.

## Project Structure
- **/data/**: Stores datasets.
  - **/data/raw/**: Raw data files (e.g., `train.csv`, `test.csv` from Kaggle).
  - **/data/processed/**: Cleaned and processed data (e.g., `preprocessed_train.csv`).
- **/notebooks/**: Jupyter notebooks for analysis, modeling, and evaluation (e.g., `modeling_regression_team.ipynb`).
- **/src/**: Python scripts for data processing and modeling (e.g., `cleaning.py`).
- **/docs/**: Documentation, including stakeholder memos (e.g., `stakeholder_memo.md`).
- **README.md**: Project overview and setup instructions.
- **requirements.txt**: Lists dependencies for reproducible environment.
- **.env**: Local environment variables (e.g., `DATA_DIR_RAW`, `DATA_DIR_PROCESSED`).
- **.env.example**: Template for environment variables, safe for version control.

## Tooling Setup
- **Environment**: Managed via Conda (`fe-course` environment, Python 3.11) with dependencies in `requirements.txt` (e.g., `pandas`, `numpy`, `scikit-learn`, `seaborn`).
- **Version Control**: GitHub repository initialized with `.gitignore` to exclude sensitive files (e.g., `.env`, data files). Resolved 'origin' errors by setting `git remote add origin <URL>` and pushing with `git push -u origin main`.
- **Reproducibility**: Environment variables in `.env` define absolute paths (e.g., `/Users/junshao/bootcamp_Jun_Shao/homework/hw10/data/raw`), ensuring consistent file handling.

## Data Preprocessing
- **Notebook**: `notebooks/data_preprocessing.ipynb` demonstrates cleaning and transformation using `train.csv`. It includes:
  - Loading data with pandas.
  - Handling missing values, duplicates, normalizing numeric features, and encoding categorical features using `src/cleaning.py`.
  - Saving to `data/processed/preprocessed_train.csv`.
- **Cleaning Functions**: `src/cleaning.py` contains:
  - `fill_missing`: Median for numeric, 'None' for categorical.
  - `drop_duplicates`: Removes duplicate rows.
  - `normalize_data`: Min-Max normalization for numeric columns.
  - `encode_categorical`: One-hot encodes categorical columns.
  - Markdown documentation with assumptions (e.g., median imputation for skewness).
- **Assumptions**:
  - Numeric missing values (e.g., LotFrontage) suitable for median imputation due to skewness.
  - Categorical missing values represent 'None' (e.g., no basement).
  - Normalization for model compatibility, assuming no extreme outliers post-cleaning.
  - One-hot encoding for nominal categorical features.
- **Tradeoffs**:
  - Median imputation vs. KNN: Simple but may miss relationships.
  - One-hot encoding increases dimensionality, may need reduction.
  - Normalization vs. standardization: Min-Max chosen for simplicity.

## Modeling Regression
- **Notebook**: `notebooks/modeling_regression_team.ipynb` demonstrates:
  - Loading preprocessed data (`preprocessed_train.csv`).
  - Fitting a linear regression model to predict `SalePrice` using selected features (e.g., `GrLivArea`, `OverallQual`).
  - Adding a transformed feature (e.g., `GrLivArea²`) to capture non-linear effects.
  - Computing R² and RMSE, analyzing residuals for linearity, independence, homoscedasticity, and normality.
  - Visualizing residuals (vs. fitted, histogram, Q-Q plot, vs. key predictor).
- **Assumptions**:
  - Linear relationship between features (e.g., GrLivArea, OverallQual) and SalePrice.
  - Residuals are independent, homoscedastic, and normally distributed.
  - Transformed feature (e.g., GrLivArea²) captures non-linear patterns while maintaining linear regression framework.
- **Tradeoffs**:
  - Linear regression assumes linearity; non-linear models (e.g., random forests) may capture complex patterns better.
  - High dimensionality from one-hot encoding may require regularization (e.g., Ridge).

## Goals → Lifecycle → Deliverables Mapping
- **Goal**: Predict housing prices for investment decisions.
  - **Lifecycle**:
    - **Data Collection**: Kaggle datasets in `data/raw/`.
    - **Data Preprocessing**: Clean data in `data/processed/`.
    - **Modeling**: Build and evaluate models in `notebooks/`.
    - **Evaluation**: Assess RMSE, R² in `notebooks/`.
    - **Reporting**: Visualizations and memos in `docs/`.
  - **Deliverables**:
    - Preprocessed dataset (`data/processed/preprocessed_train.csv`).
    - Python scripts (`src/`).
    - Jupyter notebooks (`notebooks/`).
    - Stakeholder memo (`docs/`).

## Assumptions and Risks
- **Assumptions**: Features (e.g., GrLivArea, Neighborhood, OverallQual) are predictive; models generalize in Ames, Iowa.
- **Risks**: Missing values or outliers may reduce accuracy; market-specific features may limit generalizability. Mitigated by robust preprocessing, feature selection, and residual analysis.
