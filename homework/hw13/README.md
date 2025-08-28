# Housing Price Prediction Project - Productization

This project develops a machine learning model to predict housing prices in Ames, Iowa, using the Kaggle House Prices dataset, enabling real estate investment analysts to identify high-return opportunities. The final product is a reusable Flask API for predictions and a dashboard for interaction, with serialized model for handoff.

## Stakeholder Context
- **Who**: Real estate investment analysts and portfolio managers at investment firms.
- **What They Care About**: Accurate housing price predictions with easy access via API or dashboard, interpretable results, and reliable performance metrics (e.g., RMSE, R²).
- **Needs**: A robust, reproducible system for querying predictions, visualizing results, and understanding risks.

## Project Structure
- **/data/**: Stores datasets.
  - **/data/raw/**: Raw data files (e.g., `train.csv`, `test.csv` from Kaggle).
  - **/data/processed/**: Cleaned and processed data (e.g., `updated_encoded_train.csv`).
- **/notebooks/**: Jupyter notebooks for analysis, modeling, and deployment (e.g., `stage13_productization_homework-starter.ipynb`, `utils.py`).
- **/src/**: Python scripts for data processing and modeling (legacy files, if any).
- **/reports/**: Generated reports or logs (empty by default).
- **/model/**: Serialized models (e.g., `linear_model.pkl`).
- **/docs/**: Documentation, including stakeholder memos (e.g., `stakeholder_memo.md`).
- **app.py**: Flask API for predictions.
- **README.md**: Project overview and setup instructions.
- **requirements.txt**: Lists dependencies for reproducible environment.
- **.env**: Local environment variables (e.g., `DATA_DIR_RAW`, `MODEL_DIR`).
- **.env.example**: Template for environment variables, safe for version control.

## Tooling Setup
- **Environment**: Managed via Conda (`fe-course` environment, Python 3.11) with dependencies in `requirements.txt` (e.g., `pandas`, `flask`, `joblib`).
- **Version Control**: GitHub repository initialized with `.gitignore` to exclude sensitive files (e.g., `.env`, raw data).
- **Reproducibility**: Absolute paths in `.env` ensure consistent file handling. Install dependencies with `pip install -r requirements.txt`.

## Data Preprocessing
- **Notebook**: `notebooks/utils.py` provides:
  - `fill_missing_values`: Median for numeric, 'None' for categorical.
  - `remove_duplicates`: Removes duplicate rows.
  - `scale_numeric_features`: Min-Max normalization.
  - `encode_categorical_features`: One-hot encoding.
  - `train_model`: Trains a linear regression model.
  - `save_model`: Pickles the trained model.
- **Assumptions**: Numeric missing values suit median imputation; categorical 'None' indicates absence; normalization assumes no extreme outliers.
- **Tradeoffs**: Median vs. KNN imputation (simplicity vs. accuracy); one-hot encoding increases dimensionality.

## Modeling & Deployment
- **Notebook**: `notebooks/stage13_productization_homework-starter.ipynb` demonstrates:
  - Basic analysis and cleanup.
  - Model training and pickling to `model/linear_model.pkl`.
  - Flask API deployment with /predict endpoints for features input.
  - Testing API from notebook using requests.
- **API Endpoints**:
  - POST /predict: Accepts JSON features, returns prediction.
  - GET /predict/<input1>: Single feature prediction.
  - GET /predict/<input1>/<input2>: Two features prediction.
  - GET /plot: Returns a simple chart.
- **Assumptions**: Linear relationships; features like LotArea, OverallQual are key predictors.
- **Tradeoffs**: Flask for simplicity; more complex dashboards (e.g., Streamlit) optional.

## Handoff Best Practices
- Clone the repo: `git clone <repo_url>`.
- Install dependencies: `pip install -r requirements.txt`.
- Train and pickle model: Run `notebooks/stage13_productization_homework-starter.ipynb`.
- Run API: `python app.py`, test endpoints with curl or requests.
- Reproduce: Use `.env` for paths; all notebooks are self-contained.
- Risks: Data distribution changes may affect accuracy; validate on new data.

## Assumptions and Risks
- **Assumptions**: Features (e.g., LotArea, Neighborhood) are predictive; model generalizes in Ames, Iowa.
- **Risks**: Missing data or outliers may reduce accuracy; market-specific features limit generalizability. Mitigated by preprocessing and validation.

## Next Steps
- Deploy API to cloud (e.g., Heroku) for production use.
- Add advanced features like authentication or batch prediction.
- Integrate with dashboard for user-friendly interaction.
