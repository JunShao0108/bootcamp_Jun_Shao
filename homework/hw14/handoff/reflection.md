# Reflection on Deployment & Monitoring - Housing Price Prediction Project

## Risks if Deployed
Deploying the current linear regression model for housing price prediction poses several risks. Schema drift could occur if new data introduces unseen categorical values (e.g., new Neighborhoods), skewing predictions. Increased null rates in features like LotFrontage (>10%) may reduce model accuracy. Label delay in SalePrice could lead to outdated training data, affecting real-time predictions. Server downtime or latency spikes (>250ms p95) could disrupt API availability, and business misalignment might occur if predicted prices fail to reflect market trends (e.g., approval rate < 70%).

## Monitoring Metrics Across Layers
- **Data**: Monitor data freshness (max 24 hours since last batch), null rate (<5% per feature), and schema hash (mismatch triggers alert).
- **Model**: Track rolling MAE (7-day window, threshold >0.12 triggers retraining) and calibration error (>0.05 signals drift).
- **System**: Measure p95 latency (<200ms) and error rate (<1%) for API requests.
- **Business**: Monitor approval rate (>75%) and bad rate (<5%) to assess prediction utility.

## Ownership & Handoffs
Ownership lies with the Data Science team, with the Platform Engineer on-call for system alerts and the Analyst for weekly model reviews. Handoffs involve deploying the API to a staging server, logging issues in Jira, and approving rollbacks by the Lead Data Scientist. Retraining triggers include 5% PSI on key features or 2-week rolling MAE >0.12, executed biweekly or on alert.

(Word count: 213)
