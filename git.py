import pandas as pd
import numpy as np

def load_data(filepath):
    """Load data from CSV file"""
    return pd.read_csv(filepath)

def clean_data(df):
    """Clean and preprocess data"""
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna()  # or use df.fillna(method='ffill')
    
    # Remove leading/trailing whitespace
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Convert data types if needed
    # df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')
    
    return df

def save_data(df, filepath):
    """Save cleaned data to CSV"""
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    # Example usage
    df = load_data("input_data.csv")
    df_cleaned = clean_data(df)
    save_data(df_cleaned, "cleaned_data.csv")
    print("Data cleaning complete!")