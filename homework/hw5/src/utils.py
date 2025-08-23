import pandas as pd
import os

def write_df(df, filename, data_dir):
    """
    Write a DataFrame to a file (CSV or Parquet) in the specified directory.
    
    Args:
        df (pd.DataFrame): DataFrame to save.
        filename (str): Name of the file (e.g., 'sample.csv' or 'sample.parquet').
        data_dir (str): Directory path to save the file.
        
    Returns:
        str: Path to the saved file.
        
    Raises:
        ValueError: If file suffix is not .csv or .parquet.
        ImportError: If Parquet engine (pyarrow) is missing for .parquet files.
    """
    os.makedirs(data_dir, exist_ok=True)  # Create directory if it doesn't exist
    filepath = os.path.join(data_dir, filename)
    
    if filename.endswith('.csv'):
        df.to_csv(filepath, index=False)
    elif filename.endswith('.parquet'):
        try:
            df.to_parquet(filepath, index=False, engine='pyarrow')
        except ImportError:
            raise ImportError("Missing 'pyarrow' library. Install it to save Parquet files.")
    else:
        raise ValueError("Filename must end with .csv or .parquet")
    
    return filepath

def read_df(filename, data_dir):
    """
    Read a DataFrame from a file (CSV or Parquet) in the specified directory.
    
    Args:
        filename (str): Name of the file (e.g., 'sample.csv' or 'sample.parquet').
        data_dir (str): Directory path containing the file.
        
    Returns:
        pd.DataFrame: Loaded DataFrame.
        
    Raises:
        ValueError: If file suffix is not .csv or .parquet.
        ImportError: If Parquet engine (pyarrow) is missing for .parquet files.
        FileNotFoundError: If the file does not exist.
    """
    filepath = os.path.join(data_dir, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    if filename.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filename.endswith('.parquet'):
        try:
            return pd.read_parquet(filepath, engine='pyarrow')
        except ImportError:
            raise ImportError("Missing 'pyarrow' library. Install it to read Parquet files.")
    else:
        raise ValueError("Filename must end with .csv or .parquet")