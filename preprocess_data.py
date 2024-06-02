import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(data_frames):
    for name, df in data_frames.items():
        # Check for missing values
        print(f"\nMissing values in {name}:")
        print(df.isnull().sum())

        # Drop rows or columns with excessive missing values
        df_cleaned = df.dropna()  # This is a simple approach; you might want to be more selective

        # Check data types
        print(f"\nData types in {name}:")
        print(df.dtypes)

        # Store cleaned dataframe back to the dictionary
        data_frames[name] = df_cleaned
    return data_frames

def normalize_data(data_frames):
    for name, df in data_frames.items():
         # Select only numeric columns for normalization
        numeric_columns = df.select_dtypes(include=[float, int]).columns
        
        if not df.empty and not numeric_columns.empty:
            scaler = StandardScaler()
            df_scaled = df.copy()
            df_scaled[numeric_columns] = scaler.fit_transform(df[numeric_columns])
            
            # Store normalized dataframe back to the dictionary
            data_frames[name] = df_scaled
    return data_frames

if __name__ == "__main__":
    # Example usage:
    from load_data import load_all
    import os

    # Load all full data files and series family metadata files
    data_frames = load_all()

    # Clean and normalize the data
    data_frames = clean_data(data_frames)
    data_frames = normalize_data(data_frames)

    # Print the processed dataframes' keys to see what has been processed
    print("Processed dataframes:", data_frames.keys())
