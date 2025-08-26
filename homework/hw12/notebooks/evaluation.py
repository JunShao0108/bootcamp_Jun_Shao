"""
Evaluation utilities for the Housing Price Prediction Project.

Functions:
- mean_impute(a): Replaces NaN values with the mean of the array.
  Assumptions: Missing values are random and mean is a reasonable substitute.
  Rationale: Simple and effective for small missing data fractions.

- median_impute(a): Replaces NaN values with the median of the array.
  Assumptions: Missing values are random; median is robust to outliers.
  Rationale: Suitable for skewed distributions.

- SimpleLinReg: A basic linear regression class for fitting and prediction.
  Assumptions: Linear relationship between X and y (multi-feature supported).
  Rationale: Provides a lightweight alternative to sklearn.linear_model.

- bootstrap_metric(y_true, y_pred, metric_fn, n_boot=1000): Computes a bootstrap confidence interval for a metric.
  Assumptions: Resamples represent the population distribution.
  Rationale: Quantifies uncertainty without parametric assumptions.

- scenario_sensitivity(X_raw, y, fit_fn, scenarios): Compares model performance across different data scenarios.
  Assumptions: Scenarios capture relevant variations in data handling.
  Rationale: Assesses robustness to imputation or model choices.
"""

import numpy as np
import pandas as pd
from typing import Callable, Dict
from sklearn.metrics import mean_absolute_error

def mean_impute(a: np.ndarray) -> np.ndarray:
    """
    Replace NaN values with the mean of the array.
    
    Args:
        a (np.ndarray): Input array with possible NaN values.
        
    Returns:
        np.ndarray: Array with NaN replaced by mean.
    """
    m = np.nanmean(a)
    out = a.copy()
    out[np.isnan(out)] = m
    return out

def median_impute(a: np.ndarray) -> np.ndarray:
    """
    Replace NaN values with the median of the array.
    
    Args:
        a (np.ndarray): Input array with possible NaN values.
        
    Returns:
        np.ndarray: Array with NaN replaced by median.
    """
    m = np.nanmedian(a)
    out = a.copy()
    out[np.isnan(out)] = m
    return out

class SimpleLinReg:
    """
    A simple linear regression class for fitting and prediction with multi-feature support.
    """
    def fit(self, X, y):
        """
        Fit the linear regression model.
        
        Args:
            X (np.ndarray): Feature array (n_samples, n_features).
            y (np.ndarray): Target array (n_samples,).
        
        Returns:
            self: Fitted model.
        """
        X1 = np.c_[np.ones(len(X)), X]  # Add intercept term
        beta, _, _, _ = np.linalg.lstsq(X1, y, rcond=None)
        self.intercept_ = float(beta[0])
        self.coef_ = np.array([float(b) for b in beta[1:]])
        self.n_features_ = X.shape[1]  # Store number of features
        return self

    def predict(self, X):
        """
        Predict using the fitted model.
        
        Args:
            X (np.ndarray): Feature array (n_samples, n_features).
            If n_features differs, use first feature for compatibility.
        
        Returns:
            np.ndarray: Predicted values.
        """
        if X.shape[1] != self.n_features_:
            X = X[:, [0]]  # Use first feature if dimensions mismatch
        X1 = np.c_[np.ones(len(X)), X]
        return X1 @ np.r_[self.intercept_, self.coef_[:X.shape[1]]]

def bootstrap_metric(y_true: np.ndarray, y_pred: np.ndarray, metric_fn: Callable, n_boot: int = 1000) -> dict:
    """
    Compute bootstrap confidence interval for a metric.
    
    Args:
        y_true (np.ndarray): True target values.
        y_pred (np.ndarray): Predicted values.
        metric_fn (Callable): Metric function (e.g., mean_absolute_error).
        n_boot (int): Number of bootstrap resamples (default: 1000).
        
    Returns:
        dict: Bootstrap statistics (mean, CI lower, CI upper).
    """
    n = len(y_true)
    metrics = []
    for _ in range(n_boot):
        idx = np.random.choice(n, n, replace=True)
        boot_true = y_true[idx]
        boot_pred = y_pred[idx]
        metrics.append(metric_fn(boot_true, boot_pred))
    metrics = np.array(metrics)
    mean_metric = np.mean(metrics)
    ci_lower = np.percentile(metrics, 2.5)
    ci_upper = np.percentile(metrics, 97.5)
    return {'mean': mean_metric, 'ci_lower': ci_lower, 'ci_upper': ci_upper}

def scenario_sensitivity(X_raw: np.ndarray, y: np.ndarray, fit_fn: Callable, scenarios: Dict[str, Callable]) -> pd.DataFrame:
    """
    Compare model performance across different data scenarios.
    
    Args:
        X_raw (np.ndarray): Raw feature array with possible NaN.
        y (np.ndarray): Target array.
        fit_fn (Callable): Fitting function (e.g., SimpleLinReg.fit).
        scenarios (Dict[str, Callable]): Dictionary of scenario functions (e.g., mean_impute, drop_missing).
        
    Returns:
        pd.DataFrame: Results with scenario names, MAE, slope, and intercept.
    """
    results = []
    for name, fn in scenarios.items():
        if name == 'drop_missing' and np.isnan(X_raw).any():
            mask = ~np.isnan(X_raw).any(axis=1)
            Xs, ys = X_raw[mask], y[mask]
        else:
            Xs, ys = fn(X_raw), y
        m = fit_fn(Xs, ys)  # Use multi-feature X directly
        yh = m.predict(Xs)
        results.append({'scenario': name, 'mae': mean_absolute_error(ys, yh), 
                       'slope': m.coef_[0] if m.coef_.size == 1 else m.coef_[0], 
                       'intercept': m.intercept_})
    return pd.DataFrame(results)
