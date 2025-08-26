# Housing Price Prediction Project - Final Reporting

This project develops a machine learning model to predict housing prices in Ames, Iowa, using the Kaggle House Prices dataset, enabling real estate investment analysts to identify high-return opportunities. The final report communicates predictions, uncertainty, and risks, evaluated with RMSE, R², and MAE, supporting data-driven decisions. Stakeholders are real estate analysts and portfolio managers seeking interpretable insights.

## Stakeholder Context
- **Who**: Real estate investment analysts and portfolio managers at investment firms.
- **What They Care About**: Accurate housing price predictions with clear risk assessments, visualizations of trends (e.g., LotArea, Neighborhood), and actionable insights.
- **Needs**: A concise, professional report quantifying uncertainty and guiding investment decisions.

## Project Structure
- **/data/**: Stores datasets.
  - **/data/raw/**: Raw data files (e.g., `train.csv`, `test.csv` from Kaggle).
  - **/data/processed/**: Cleaned and processed data (e.g., `updated_encoded_train.csv`).
- **/notebooks/**: Jupyter notebooks for analysis, modeling, and reporting (e.g., `final_reporting_template.ipynb`).
- **/src/**: Python scripts for data processing and evaluation (e.g., `evaluation.py`, `cleaning.py`).
- **/docs/**: Documentation, including stakeholder memos (e.g., `stakeholder_memo.md`).
- **/deliverables/**: Final report and images (e.g., `final_report.md`, `deliverables/images/`).
- **README.md**: Project overview and setup instructions.
- **requirements.txt**: Lists dependencies for reproducible environment.
- **.env**: Local environment variables (e.g., `DATA_DIR_RAW`, `DATA_DIR_PROCESSED`).
- **.env.example**: Template for environment variables, safe for version control.

## Tooling Setup
- **Environment**: Managed via Conda (`fe-course` environment, Python 3.11) with dependencies in `requirements.txt`.
- **Version Control**: GitHub repository initialized with `.gitignore` to exclude sensitive files.
- **Reproducibility**: Absolute paths in `.env` ensure consistent file handling.

## Final Reporting
- **Notebook**: `notebooks/final_reporting_template.ipynb` generates:
  - Executive summary with decision-oriented bullets.
  - 3 polished visualizations: Risk-Return scatter, Return by Scenario bar chart, MetricA over time line chart.
  - Assumptions & Risks section.
  - Sensitivity analysis table comparing baseline and alternate scenarios.
  - Decision implications with actionable insights.
- **Deliverable**: Saved as `deliverables/final_report.md` with images in `deliverables/images/`.
- **Audience**: Real estate analysts and portfolio managers, preferring a concise Markdown report for quick decision-making.
- **Rationale**: Markdown format is lightweight, version-controllable, and easily shared, fitting stakeholders' need for actionable insights without complex interactivity.

## Assumptions and Risks
- **Assumptions**: Features (e.g., LotArea, OverallQual) are predictive; linear regression captures key relationships.
- **Risks**: Missing data or outliers may skew results; limited temporal data affects trend analysis. Mitigated by imputation and sensitivity checks.

