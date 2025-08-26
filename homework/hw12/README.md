# Housing Price Prediction Project - Final Reporting

This project develops a machine learning model to predict housing prices in Ames, Iowa, using the Kaggle House Prices dataset, enabling real estate investment analysts to identify high-return opportunities. The final report communicates predictions, uncertainty, and risks, evaluated with RMSE, R², and MAE metrics, supporting data-driven investment decisions. Stakeholders are real estate analysts and portfolio managers seeking interpretable insights.

## Stakeholder Context
- **Who**: Real estate investment analysts and portfolio managers at investment firms.
- **What They Care About**: Accurate housing price predictions with clear risk assessments, visualizations of trends (e.g., LotArea, Neighborhood), and actionable insights.
- **Needs**: A concise, professional report quantifying uncertainty and guiding investment decisions.

## Project Structure
- **/data/**: Stores datasets.
  - **/data/raw/**: Raw data files (e.g., `train.csv`, `test.csv` from Kaggle).
  - **/data/processed/**: Cleaned and processed data (e.g., `updated_encoded_train.csv`).
- **/notebooks/**: Jupyter notebooks for analysis, modeling, and reporting (e.g., `final_reporting_template.ipynb`, `cleaning.py`, `evaluation.py`).
- **/src/**: Python scripts for data processing and evaluation (legacy files, if any).
- **/docs/**: Documentation, including stakeholder memos (e.g., `stakeholder_memo.md`).
- **/deliverables/**: Final report and images (e.g., `final_report.md`, `deliverables/images/`).
- **README.md**: Project overview and setup instructions.
- **requirements.txt**: Lists dependencies for reproducible environment.
- **.env**: Local environment variables (e.g., `DATA_DIR_RAW`, `DATA_DIR_PROCESSED`).
- **.env.example**: Template for environment variables, safe for version control.

## Tooling Setup
- **Environment**: Managed via Conda (`fe-course` environment, Python 3.11) with dependencies in `requirements.txt` (e.g., `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`).
- **Version Control**: GitHub repository initialized with `.gitignore` to exclude sensitive files (e.g., `.env`, raw data). Commits are tracked with descriptive messages.
- **Reproducibility**: Absolute paths in `.env` ensure consistent file handling across sessions.

## Final Reporting
- **Notebook**: `notebooks/final_reporting_template.ipynb` generates:
  - Executive summary with decision-oriented bullets.
  - 3 polished visualizations: Risk-Return scatter plot, Return by Scenario bar chart, and MetricA over time line chart, reflecting R² (0.72), RMSE (0.063, 0.057), and SalePrice trends.
  - Assumptions & Risks section, detailing linear model assumptions and data limitations.
  - Sensitivity analysis table comparing baseline (R² ≈ 0.72, RMSE ≈ 0.063) with alternate scenarios (e.g., imputation RMSE ≈ 0.057, polynomial fit RMSE ≈ 0.055).
  - Decision implications with actionable insights for stakeholders.
- **Deliverable**: Saved as `deliverables/final_report.md` with images in `deliverables/images/`.
- **Audience**: Real estate analysts and portfolio managers, preferring a concise Markdown report.
- **Rationale**: Markdown is lightweight, version-controllable, and easily shared, aligning with stakeholders' need for quick, actionable insights without interactive tools.

## Data Preprocessing
- **Notebook**: `notebooks/cleaning.py` provides:
  - `fill_missing_values`: Median for numeric, 'None' for categorical.
  - `remove_duplicates`: Removes duplicate rows.
  - `scale_numeric_features`: Min-Max normalization.
  - `encode_categorical_features`: One-hot encoding.
- **Assumptions**: Numeric missing values suit median imputation; categorical 'None' indicates absence; normalization assumes no extreme outliers.
- **Tradeoffs**: Median vs. KNN imputation (simplicity vs. accuracy); one-hot encoding increases dimensionality.

## Modeling & Evaluation
- **Notebooks**: `notebooks/modeling_regression_team.ipynb`, `notebooks/modeling_team.ipynb`, and `notebooks/stage11_eval_risk_homework.ipynb` contribute:
  - Regression: R² = 0.72, RMSE = 0.063.
  - Time Series: MAE = 0.122, RMSE = 0.163.
  - Evaluation: Baseline RMSE = 0.057 [0.052, 0.062], sensitivity to imputation and polynomial fit.
- **Assumptions**: Linear relationships; residuals are independent and normally distributed.
- **Tradeoffs**: Linear model simplicity vs. non-linear accuracy; limited temporal data.

## Final Results
- **Key Metrics**: Baseline R² ≈ 0.72, RMSE ≈ 0.063; imputation reduces RMSE to 0.057; polynomial fit improves MAE to 0.032206.
- **Visuals**: Reflect steady returns with moderate volatility, slight sensitivity to preprocessing.
- **Risks**: Non-linear patterns or outliers may skew results; mitigated by sensitivity analysis.

## Assumptions and Risks
- **Assumptions**: Features (e.g., LotArea, Neighborhood) are predictive; linear regression generalizes in Ames, Iowa.
- **Risks**: Missing data, outliers, or limited temporal data may reduce accuracy; market-specific features limit generalizability. Mitigated by preprocessing, feature engineering, and uncertainty quantification.

## Next Steps
- Validate on `test.csv` to confirm generalizability.
- Explore non-linear models (e.g., random forests) for enhanced predictions.
- Collect additional data to improve trend analysis and reduce uncertainty.
