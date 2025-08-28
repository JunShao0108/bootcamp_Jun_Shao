# Housing Price Prediction Project - Lifecycle Finalization

This project builds a predictive model for housing prices in Ames, Iowa, using linear regression, providing a Flask API and detailed lifecycle documentation for real estate insights.

## Stakeholder Context
- **Who**: Real estate analysts and managers.
- **What They Care About**: Accurate predictions, API ease, and risk evaluation.
- **Needs**: Reproducible, documented system for use.

## Project Structure
- **/data/**: Raw and processed data (e.g., `train.csv`).
- **/notebooks/**: Analysis files (e.g., `stage16_lifecycle-review_homework-starter.ipynb`, `utils.py`).
- **/src/**: Future script space (currently empty).
- **/reports/**: Metrics and plans (e.g., `evaluation_metrics.json`).
- **/model/**: Model file (e.g., `linear_model.pkl`).
- **/docs/**: Documentation (e.g., `summary.md`, `stakeholder_memo.md`).
- **app.py**: Flask API implementation.
- **README.md**: Project and lifecycle overview.
- **requirements.txt**: Package dependencies.
- **.env**: Environment settings.
- **.env.example**: Settings template.

## Lifecycle Mapping
- **Definition**: Outlined in `README.md` (Stage 1).
- **Data**: Sourced in `/data/raw/` (Stage 2).
- **Cleaning**: Managed in `utils.py` (Stage 3).
- **Exploration**: Conducted in `/notebooks/` (Stage 4).
- **Feature Engineering**: Handled in `utils.py` (Stage 5).
- **Modeling**: Completed in `/model/` (Stage 6).
- **Evaluation**: Recorded in `/reports/` (Stage 7).
- **Deployment**: Enabled via `app.py` (Stage 8).
- **Monitoring**: Planned in `reflection.md` (Stage 9).
- **Iteration**: Scheduled for updates (Stage 10).

## Setup Guide
- **Environment**: Conda (`fe-course`, Python 3.11), use `pip install -r requirements.txt`.
- **Run**: Execute `python app.py` (port 5001), launch `jupyter notebook` for analysis.

## Handoff Instructions
- Clone: `git clone <repo_url>`.
- Install: `pip install -r requirements.txt`.
- Test: Access `http://127.0.0.1:5001/predict`.

## Future Plans
- Cloud API deployment.
- Automated monitoring system.
- Regular model updates.
