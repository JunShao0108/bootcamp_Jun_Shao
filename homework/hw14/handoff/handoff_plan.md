# Handoff Plan - Housing Price Prediction Project

- **Deployment Path**: Deploy API to staging server via GitHub Actions.
- **Runbook Link**: [Jira Issue Tracker](https://your-jira-instance.com) for logging issues.
- **Ownership**: Data Science team owns model updates, Platform Engineer handles system alerts.
- **Retraining Schedule**: Biweekly or on 5% PSI trigger, approved by Lead Data Scientist.
- **Rollback Procedure**: Analyst reviews metrics, Lead Data Scientist approves rollback within 24 hours.
- **Monitoring Dashboard**: Hosted on internal Grafana, updated daily.
- **Alert Recipients**: Platform Engineer (system), Analyst (model), emailed on threshold breach.
- **Documentation**: `README.md` and `reflection.md` in repo.
- **Testing**: Validate on `test.csv` post-deployment.
- **Escalation**: Escalate to CTO if downtime exceeds 1 hour.
