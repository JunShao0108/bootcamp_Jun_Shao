"""
Data cleaning utilities for the Housing Price Prediction Project.

Functions:
- fill_missing_values(df): Handles missing values in numeric and categorical columns.
  Assumptions: Numeric missing values are random and suitable for median imputation; categorical missing values indicate absence.
  Rationale: Median is robust to outliers; 'None' aligns with dataset semantics.

- remove_duplicates(df): Removes duplicate rows.
  Assumptions: Duplicates are errors and can be safely removed.
  Rationale: Ensures data integrity.

- scale_numeric_features(df, columns=None): Applies Min-Max scaling to numeric columns.
  Assumptions: Normalization improves model convergence; no extreme outliers post-cleaning.
  Rationale: Min-Max scaling is simple and effective.

- encode_categorical_features(df, columns=None): One-hot encodes categorical columns.
  Assumptions: Categorical features are nominal; high dimensionality is manageable.
  Rationale: One-hot encoding suits regression models.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def fill_missing_values(df):
    """
    Fill missing values in numeric and categorical columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        
    Returns:
        pd.DataFrame: DataFrame with missing values filled.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=[object]).columns
    
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
    for col in categorical_cols:
        df[col].fillna('None', inplace=True)
    
    return df

def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        
    Returns:
        pd.DataFrame: DataFrame without duplicates.
    """
    df = df.copy()
    return df.drop_duplicates()

def scale_numeric_features(df, columns=None):
    """
    Apply Min-Max scaling to specified numeric columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to scale (default: all numeric).
        
    Returns:
        pd.DataFrame: DataFrame with scaled columns.
    """
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def encode_categorical_features(df, columns=None):
    """
    One-hot encode specified categorical columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to encode (default: all categorical).
        
    Returns:
        pd.DataFrame: DataFrame with encoded columns.
    """
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=[object]).columns
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded_data = encoder.fit_transform(df[columns])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(columns))
    df = pd.concat([df.drop(columns, axis=1), encoded_df], axis=1)
    return df
