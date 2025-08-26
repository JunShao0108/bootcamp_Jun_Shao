# Housing Price Prediction Project - Evaluation & Risk Communication

This project develops a machine learning model to predict housing prices in Ames, Iowa, using the Kaggle House Prices dataset, enabling real estate investment analysts to identify high-return opportunities. By analyzing 79 features (e.g., lot area, neighborhood, overall quality), the model delivers accurate predictions with quantified uncertainty, evaluated with RMSE, R², and MAE, to support data-driven decisions. The primary stakeholders are real estate analysts and portfolio managers who value interpretable results and risk insights. The project follows a full lifecycle, with deliverables in structured folders.

## Stakeholder Context
- **Who**: Real estate investment analysts and portfolio managers at investment firms.
- **What They Care About**: Accurate housing price predictions with uncertainty estimates, interpretable results (e.g., visualizations of price trends and key features like LotArea, Neighborhood), and reliable performance metrics (e.g., RMSE, R², MAE).
- **Needs**: A robust, reproducible pipeline quantifying uncertainty, assessing assumptions, and communicating risks clearly.

## Project Structure
- **/data/**: Stores datasets.
  - **/data/raw/**: Raw data files (e.g., `train.csv`, `test.csv` from Kaggle).
  - **/data/processed/**: Cleaned and processed data (e.g., `updated_encoded_train.csv`).
- **/notebooks/**: Jupyter notebooks for analysis, modeling, and evaluation (e.g., `stage11_eval_risk_homework.ipynb`).
- **/src/**: Python scripts for data processing and evaluation (e.g., `evaluation.py`).
- **/docs/**: Documentation, including stakeholder memos (e.g., `stakeholder_memo.md`).
- **README.md**: Project overview and setup instructions.
- **requirements.txt**: Lists dependencies for reproducible environment.
- **.env**: Local environment variables (e.g., `DATA_DIR_RAW`, `DATA_DIR_PROCESSED`).
- **.env.example**: Template for environment variables, safe for version control.

## Tooling Setup
- **Environment**: Managed via Conda (`fe-course` environment, Python 3.11) with dependencies in `requirements.txt` (e.g., `pandas`, `numpy`, `scikit-learn`, `seaborn`).
- **Version Control**: GitHub repository initialized with `.gitignore` to exclude sensitive files (e.g., `.env`, data files). Resolved 'origin' errors by setting `git remote add origin <URL>` and pushing with `git push -u origin main`.
- **Reproducibility**: Environment variables in `.env` define absolute paths (e.g., `/Users/junshao/bootcamp_Jun_Shao/homework/hw11/data/raw`), ensuring consistent file handling.

## Data Preprocessing
- **Notebook**: `notebooks/data_preprocessing.ipynb` demonstrates cleaning and transformation using `train.csv`. It includes:
  - Loading data with pandas.
  - Handling missing values, duplicates, normalizing numeric features, and encoding categorical features using `src/cleaning.py`.
  - Saving to `data/processed/updated_encoded_train.csv`.
- **Cleaning Functions**: `src/cleaning.py` contains:
  - `fill_missing_values`: Median for numeric, 'None' for categorical.
  - `remove_duplicates`: Removes duplicate rows.
  - `scale_numeric_features`: Min-Max normalization for numeric columns.
  - `encode_categorical_features`: One-hot encodes categorical columns.
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
  - Loading preprocessed data (`updated_encoded_train.csv`).
  - Fitting a linear regression model to predict `SalePrice` using selected features (e.g., `LotArea`, `OverallQual`).
  - Adding a transformed feature (e.g., `LotArea_squared`) to capture non-linear effects.
  - Computing R² and RMSE, analyzing residuals for linearity, independence, homoscedasticity, and normality.
  - Visualizing residuals (vs. fitted, histogram, Q-Q plot, vs. LotArea).
- **Assumptions**:
  - Linear relationship between features (e.g., LotArea, OverallQual) and SalePrice.
  - Residuals are independent, homoscedastic, and normally distributed.
  - Transformed feature (e.g., LotArea_squared) captures non-linear patterns while maintaining linear regression framework.
- **Tradeoffs**:
  - Linear regression assumes linearity; non-linear models (e.g., random forests) may capture complex patterns better.
  - High dimensionality from one-hot encoding may require regularization (e.g., Ridge).

## Time Series Modeling
- **Notebook**: `notebooks/modeling_team.ipynb` demonstrates:
  - Loading raw data (`train.csv`) and applying preprocessing to construct a time series.
  - Aggregating to monthly SalePrice mean using `YrSold` and `MoSold`, computing price change as the target.
  - Creating lag and rolling mean features to capture temporal patterns.
  - Fitting a linear regression model to predict next-step SalePrice change using a scikit-learn Pipeline.
  - Evaluating with MAE, RMSE, and a prediction vs. truth plot.
  - Analyzing model performance and risks.
- **Assumptions**:
  - Monthly SalePrice changes are predictable based on past trends.
  - Lag and rolling features capture relevant temporal patterns.
  - Linear regression is suitable for initial forecasting.
- **Tradeoffs**:
  - Linear regression may miss complex temporal patterns; ARIMA or LSTM models could perform better.
  - Limited temporal data (monthly aggregates) may reduce predictive power.

## Evaluation & Risk Communication
- **Notebook**: `notebooks/stage11_eval_risk_homework.ipynb` demonstrates:
  - Loading preprocessed data (`updated_encoded_train.csv`).
  - Fitting a linear regression model and computing RMSE.
  - Implementing Bootstrap to estimate RMSE confidence intervals (≥500 resamples).
  - Comparing scenarios (e.g., mean vs. median imputation, linear vs. polynomial fit) with sensitivity analysis.
  - Performing subgroup diagnostics by `Neighborhood`.
  - Visualizing CIs, scenario fits, and subgroup residuals.
  - Writing a stakeholder summary with assumptions, risks, and sensitivity results.
- **Assumptions**:
  - Linear relationship between features and SalePrice.
  - Bootstrap resamples represent underlying distribution.
  - Subgroup differences are detectable with current data.
- **Tradeoffs**:
  - Bootstrap vs. parametric CIs: Bootstrap is robust but computationally intensive.
  - Scenario comparison may oversimplify real-world variability.

## Goals → Lifecycle → Deliverables Mapping
- **Goal**: Predict housing prices for investment decisions with quantified uncertainty.
  - **Lifecycle**:
    - **Data Collection**: Kaggle datasets in `data/raw/`.
    - **Data Preprocessing**: Clean data in `data/processed/`.
    - **Modeling**: Build and evaluate models in `notebooks/`.
    - **Evaluation**: Assess performance and uncertainty in `notebooks/`.
    - **Reporting**: Visualizations and memos in `docs/`.
  - **Deliverables**:
    - Preprocessed dataset (`data/processed/updated_encoded_train.csv`).
    - Python scripts (`src/`).
    - Jupyter notebooks (`notebooks/`).
    - Stakeholder memo (`docs/`).

## Assumptions and Risks
- **Assumptions**: Features (e.g., LotArea, Neighborhood, OverallQual) are predictive; models generalize in Ames, Iowa.
- **Risks**: Missing values, outliers, or limited temporal data may reduce accuracy; market-specific features may limit generalizability. Mitigated by robust preprocessing, feature engineering, and uncertainty quantification.
