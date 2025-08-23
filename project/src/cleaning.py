"""
Reusable data cleaning/preprocessing functions for the Housing Price Prediction Project.

These functions are designed for the Kaggle House Prices dataset but can be adapted for similar datasets.

Functions:
- fill_missing(df, numeric_strategy='median', categorical_strategy='None'): Handles missing values in numeric and categorical columns.
  Assumptions: Numeric missing values are suitable for median imputation due to skewness; categorical missing values represent 'None' (e.g., no basement).
  Rationale: Median reduces outlier bias; 'None' aligns with data_description.txt.

- drop_duplicates(df): Removes duplicate rows.
  Assumptions: Duplicates are errors and can be safely removed without significant data loss.

- normalize_data(df, columns=None): Applies Min-Max normalization to numeric columns.
  Assumptions: Normalization is appropriate for model compatibility; no extreme outliers after cleaning.

- encode_categorical(df, columns=None): One-hot encodes categorical columns.
  Assumptions: Categorical features are nominal; one-hot encoding is suitable for models like linear regression.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def fill_missing(df, numeric_strategy='median', categorical_strategy='None'):
    """
    Handle missing values in numeric and categorical columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        numeric_strategy (str): Strategy for numeric columns ('mean', 'median').
        categorical_strategy (str): Strategy for categorical columns ('None', 'mode').
        
    Returns:
        pd.DataFrame: DataFrame with missing values filled.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=[object]).columns
    
    # Fill numeric
    for col in numeric_cols:
        if numeric_strategy == 'mean':
            fill_value = df[col].mean()
        elif numeric_strategy == 'median':
            fill_value = df[col].median()
        df[col].fillna(fill_value, inplace=True)
    
    # Fill categorical
    for col in categorical_cols:
        if categorical_strategy == 'None':
            fill_value = 'None'
        elif categorical_strategy == 'mode':
            fill_value = df[col].mode()[0]
        df[col].fillna(fill_value, inplace=True)
    
    return df

def drop_duplicates(df):
    """
    Remove duplicate rows.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        
    Returns:
        pd.DataFrame: DataFrame without duplicates.
    """
    df = df.copy()
    return df.drop_duplicates()

def normalize_data(df, columns=None):
    """
    Apply Min-Max normalization to specified numeric columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of column names to normalize (default: all numeric).
        
    Returns:
        pd.DataFrame: DataFrame with normalized columns.
    """
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def encode_categorical(df, columns=None):
    """
    One-hot encode specified categorical columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of column names to encode (default: all object).
        
    Returns:
        pd.DataFrame: DataFrame with encoded columns.
    """
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=[object]).columns
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded = encoder.fit_transform(df[columns])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(columns))
    df = pd.concat([df.drop(columns, axis=1), encoded_df], axis=1)
    return df
