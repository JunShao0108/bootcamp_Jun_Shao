"""
Data cleaning and preprocessing utilities for the Housing Price Prediction Project.

Designed for the Kaggle House Prices dataset, these functions handle missing values, duplicates, normalization, and encoding to prepare data for modeling.

Functions:
- fill_missing_values(df, num_strategy='median', cat_strategy='None'): Fills missing values in numeric and categorical columns.
  Assumptions: Numeric missing values are random and suitable for median imputation due to skewness; categorical missing values indicate absence (e.g., no basement).
  Rationale: Median is robust to outliers; 'None' aligns with dataset semantics.

- remove_duplicates(df): Removes duplicate rows.
  Assumptions: Duplicates are errors and can be safely removed.
  Rationale: Ensures data integrity without significant loss.

- scale_numeric_features(df, columns=None): Applies Min-Max scaling to numeric columns.
  Assumptions: Normalization improves model convergence; no extreme outliers post-cleaning.
  Rationale: Min-Max scaling is simple and effective for linear models.

- encode_categorical_features(df, columns=None): One-hot encodes categorical columns.
  Assumptions: Categorical features are nominal; high dimensionality is manageable.
  Rationale: One-hot encoding is standard for categorical data in regression.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def fill_missing_values(df, num_strategy='median', cat_strategy='None'):
    """
    Fill missing values in numeric and categorical columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        num_strategy (str): Strategy for numeric columns ('mean', 'median').
        cat_strategy (str): Strategy for categorical columns ('None', 'mode').
        
    Returns:
        pd.DataFrame: DataFrame with missing values filled.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=[object]).columns
    
    for col in numeric_cols:
        if num_strategy == 'median':
            df[col].fillna(df[col].median(), inplace=True)
        elif num_strategy == 'mean':
            df[col].fillna(df[col].mean(), inplace=True)
    
    for col in categorical_cols:
        if cat_strategy == 'None':
            df[col].fillna('None', inplace=True)
        elif cat_strategy == 'mode':
            df[col].fillna(df[col].mode()[0], inplace=True)
    
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
