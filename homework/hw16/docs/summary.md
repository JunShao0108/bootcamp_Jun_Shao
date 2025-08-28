# Project Summary - Housing Price Prediction

## Overview
This project develops a linear regression model to predict housing prices in Ames, Iowa, using the Kaggle dataset, supporting real estate investment with an R² of 0.68 and RMSE of 0.067.

## Key Results
- **Model Performance**: R² ≈ 0.68, RMSE ≈ 0.067, with improvements from feature engineering.
- **Visuals**: Risk-Return scatter, Scenario Impact bar, and MetricA Trend line charts.
- **API**: Accessible at `http://127.0.0.1:5001/predict` with 28 features.

## Assumptions & Risks
- **Assumptions**: Linear model is appropriate; key features are stable.
- **Risks**: Data drift or null rates (>5%) may affect accuracy; mitigated by preprocessing.

## Next Steps
- Deploy API to a cloud environment.
- Implement automated monitoring for performance.
- Schedule regular model retraining.
