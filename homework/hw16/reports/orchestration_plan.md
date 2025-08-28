# Orchestration Plan - Housing Price Prediction Project

## 1) Project Task Decomposition
| Task            | Inputs                              | Outputs                              | Idempotent |
|-----------------|-------------------------------------|--------------------------------------|------------|
| Ingest          | `/data/raw/train.csv`              | `/data/processed/prices_raw.json`    | Yes        |
| Clean           | `/data/processed/prices_raw.json`  | `/data/processed/prices_clean.json`  | Yes        |
| Train           | `/data/processed/prices_clean.json`| `/model/linear_model.pkl`            | No         |
| Evaluate        | `/model/linear_model.pkl`          | `/reports/evaluation_metrics.json`   | Yes        |
| Report          | `/reports/evaluation_metrics.json` | `/reports/final_report.md`           | Yes        |

## 2) Dependencies (DAG)
- **Diagram**:  
[Ingest] --> [Clean] --> [Train] --> [Evaluate] --> [Report]
- **Description**: Ingest loads raw data, Clean preprocesses it, Train builds the model, Evaluate computes metrics, and Report generates the final deliverable. All tasks are sequential; no parallelization due to data dependency.

## 3) Logging & Checkpoints Plan
| Task    | Log Messages                          | Checkpoint Artifact             |
|---------|---------------------------------------|---------------------------------|
| Ingest  | Start/end, rows ingested, source URI  | `/data/processed/prices_raw.json` |
| Clean   | Start/end, rows in/out, null rates    | `/data/processed/prices_clean.json` |
| Train   | Start/end, params, R², RMSE           | `/model/linear_model.pkl`       |
| Evaluate| Start/end, MAE, R², RMSE              | `/reports/evaluation_metrics.json` |
| Report  | Start/end, artifact path              | `/reports/final_report.md`      |
- **Failure Points**: Data corruption (Ingest), schema drift (Clean), model divergence (Train).
- **Retry Policy**: 3 retries with 5-second linear backoff for I/O failures (e.g., file access).

## 4) Right-Sizing Automation
- **Automate Now**: Ingest, Clean, Train, Evaluate (via cron job or GitHub Actions) to ensure daily updates and model retraining on new data.
- **Keep Manual**: Report generation, as it requires stakeholder review and manual adjustments for presentation.
- **Rationale**: Automation of data pipeline and modeling ensures consistency and timeliness, while manual reporting allows for quality control and customization.

## 5) (Stretch) Refactor One Task into a Function + CLI
- **Not Implemented**: Optional stretch goal skipped for this submission.
