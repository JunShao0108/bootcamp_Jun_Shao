import pandas as pd
import numpy as np

def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Return boolean mask for IQR-based outliers.
    Assumptions: distribution reasonably summarized by quartiles; k controls strictness.
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return (series < lower) | (series > upper)

def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Return boolean mask for Z-score outliers where |z| > threshold.
    Assumptions: roughly normal distribution; sensitive to heavy tails.
    """
    mu = series.mean()
    sigma = series.std(ddof=0)
    z = (series - mu) / (sigma if sigma != 0 else 1.0)
    return z.abs() > threshold

def handle_outliers(df: pd.DataFrame, column: str, method: str = 'iqr', action: str = 'flag', threshold: float = 3.0, k: float = 1.5) -> pd.DataFrame:
    """
    Detect and handle outliers in a specified column.
    
    Parameters:
    - df: DataFrame to process.
    - column: Column name to check for outliers.
    - method: 'iqr' or 'zscore' for detection.
    - action: 'flag' (add boolean column), 'remove' (drop rows), or 'winsorize' (cap values).
    - threshold: For zscore.
    - k: For iqr.
    
    Returns: Modified DataFrame.
    """
    if method == 'iqr':
        outliers = detect_outliers_iqr(df[column], k=k)
    elif method == 'zscore':
        outliers = detect_outliers_zscore(df[column], threshold=threshold)
    else:
        raise ValueError("Method must be 'iqr' or 'zscore'.")
    
    if action == 'flag':
        df[f'{column}_outlier'] = outliers
    elif action == 'remove':
        df = df[~outliers]
    elif action == 'winsorize':
        lo = df[column].quantile(0.05)
        hi = df[column].quantile(0.95)
        df[column] = df[column].clip(lower=lo, upper=hi)
    else:
        raise ValueError("Action must be 'flag', 'remove', or 'winsorize'.")
    
    return df