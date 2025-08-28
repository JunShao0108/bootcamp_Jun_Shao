"""
Reusable functions for the Housing Price Prediction Project.

Functions:
- fill_missing_values(df): Handles missing values in numeric and categorical columns.
- remove_duplicates(df): Removes duplicate rows.
- scale_numeric_features(df, columns=None): Applies Min-Max scaling to numeric columns.
- encode_categorical_features(df, columns=None): One-hot encodes categorical columns.
- train_model(df): Trains a linear regression model on preprocessed data.
- save_model(model, path): Pickles the trained model.
- get_features(df): Returns consistent feature list for prediction.
- preprocess_test_data(df, features): Preprocesses test data to match training features.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def fill_missing_values(df):
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=[object]).columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
    for col in categorical_cols:
        df[col].fillna('None', inplace=True)
    return df

def remove_duplicates(df):
    df = df.copy()
    return df.drop_duplicates()

def scale_numeric_features(df, columns=None):
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def encode_categorical_features(df, columns=None):
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=[object]).columns
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded_data = encoder.fit_transform(df[columns])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(columns))
    df = pd.concat([df.drop(columns, axis=1), encoded_df], axis=1)
    return df

def get_features(df):
    """
    Returns consistent feature list for prediction.
    
    Args:
        df (pd.DataFrame): Preprocessed DataFrame.
        
    Returns:
        list: Feature names.
    """
    features = ['LotFrontage', 'LotArea', 'OverallQual']
    df['LotArea_squared'] = df['LotArea'] ** 2
    features.append('LotArea_squared')
    features.extend([col for col in df.columns if 'Neighborhood_' in col or 'MSSubClass_' in col or 'MSZoning_' in col])
    return features

def preprocess_test_data(df, features):
    """
    Preprocess test data to match training features.
    
    Args:
        df (pd.DataFrame): Raw test DataFrame.
        features (list): Training feature names.
        
    Returns:
        pd.DataFrame: Preprocessed test data.
    """
    df = df.copy()
    df = fill_missing_values(df)
    df = scale_numeric_features(df, ['LotFrontage', 'LotArea', 'OverallQual'])
    df = encode_categorical_features(df, ['MSSubClass', 'MSZoning', 'Neighborhood'])
    df['LotArea_squared'] = df['LotArea'] ** 2
    test_data = pd.DataFrame(columns=features)
    for col in features:
        if col in df.columns:
            test_data[col] = df[col]
        else:
            test_data[col] = 0  # Fill missing features with 0
    return test_data

def train_model(df):
    features = get_features(df)
    X = df[features]
    y = df['SalePrice']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f'R²: {r2:.2f}')
    print(f'RMSE: {rmse:.3f}')
    return model

def save_model(model, path):
    joblib.dump(model, path)
    print(f'Model saved to {path}')