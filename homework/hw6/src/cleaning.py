import pandas as pd
import numpy as np

def fill_missing_median(df, columns):
    """
    Fill missing values in specified columns with their median.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of column names to fill with median.
        
    Returns:
        pd.DataFrame: DataFrame with missing values filled.
        
    Raises:
        KeyError: If specified columns are not in DataFrame.
    """
    df = df.copy()
    for col in columns:
        if col not in df.columns:
            raise KeyError(f"Column {col} not found in DataFrame")
        if df[col].dtype in [np.float64, np.int64]:
            median = df[col].median()
            df[col].fillna(median, inplace=True)
    return df

def drop_missing(df):
    """
    Drop rows with any missing values.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        
    Returns:
        pd.DataFrame: DataFrame with no missing values.
    """
    return df.dropna()

def normalize_data(df, columns):
    """
    Apply Min-Max normalization to specified columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of column names to normalize.
        
    Returns:
        pd.DataFrame: DataFrame with normalized columns.
        
    Raises:
        KeyError: If specified columns are not in DataFrame.
    """
    df = df.copy()
    for col in columns:
        if col not in df.columns:
            raise KeyError(f"Column {col} not found in DataFrame")
        if df[col].dtype in [np.float64, np.int64]:
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val != min_val:  # Avoid division by zero
                df[col] = (df[col] - min_val) / (max_val - min_val)
    return df