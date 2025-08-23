import pandas as pd

def get_summary_stats(df):
    """
    Calculate summary statistics for numeric columns in a DataFrame.
    
    This function uses pandas' describe() method to compute various summary statistics 
    such as count, mean, standard deviation, min, max, and quartiles for all numeric 
    columns in the input DataFrame. It is designed to be reusable across different 
    datasets and notebooks.
    
    Args:
        df (pd.DataFrame): Input DataFrame containing the data to summarize.
        
    Returns:
        pd.DataFrame: A DataFrame containing summary statistics for numeric columns.
    """
    return df.describe()