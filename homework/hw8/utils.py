"""
Utility functions for the Housing Price Prediction Project.

These functions support data preprocessing and storage tasks, ensuring consistency and usability in later stages (e.g., data cleaning, EDA, modeling).

Functions:
- clean_column_names(df): Standardizes DataFrame column names by converting to lowercase and
  replacing spaces/special characters with underscores. Useful for consistent data handling.
  Future Use: Applied during data preprocessing to normalize column names across datasets like Kaggle train/test.csv.

- convert_year_to_age(df, year_columns, current_year): Converts year columns (e.g., YearBuilt) to age relative to current_year.
  Future Use: Creates age-based features for modeling, capturing temporal effects in housing data.

- save_data(df, filename, data_dir): Saves DataFrame to CSV in the specified directory, creating folders if needed.
  Future Use: Used for storing raw or processed data reproducibly.
"""

import pandas as pd
import os

def clean_column_names(df):
    """
    Standardize DataFrame column names by converting to lowercase and replacing spaces/special
    characters with underscores.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        
    Returns:
        pd.DataFrame: DataFrame with cleaned column names.
    """
    df = df.copy()
    df.columns = df.columns.str.lower().str.replace(r'[^a-z0-9]', '_', regex=True)
    return df

def convert_year_to_age(df, year_columns, current_year=2025):
    """
    Convert year columns to age relative to current_year.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        year_columns (list): List of year column names (e.g., ['year_built', 'year_remod_add']).
        current_year (int): Reference year for age calculation (default: 2025).
        
    Returns:
        pd.DataFrame: DataFrame with new age columns (e.g., house_age, remodel_age).
        
    Raises:
        KeyError: If specified columns are not in DataFrame.
    """
    df = df.copy()
    for col in year_columns:
        if col not in df.columns:
            raise KeyError(f"Column {col} not found in DataFrame")
        age_col = f"{col.split('_')[0]}_age"
        df[age_col] = current_year - df[col]
    return df

def save_data(df, filename, data_dir):
    """
    Save DataFrame to CSV in the specified directory, creating folders if needed.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        filename (str): Name of the file (e.g., 'train_cleaned.csv').
        data_dir (str): Directory path to save the file.
        
    Returns:
        str: Path to the saved file.
    """
    os.makedirs(data_dir, exist_ok=True)  # Create directory if it doesn't exist
    filepath = os.path.join(data_dir, filename)
    df.to_csv(filepath, index=False)
    return filepath