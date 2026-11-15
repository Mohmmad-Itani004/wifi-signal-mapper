import pandas as pd
import sys

def load_rssi_data(filepath):
    """Loads and validates RSSI measurement data from a CSV file (Requirement R1 & R5)."""
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"Error: Could not read file {filepath}. Details: {e}")
        sys.exit(1)
        
    expected_columns = {'x', 'y', 'rssi'}
    if not expected_columns.issubset(df.columns):
        print(f"Error: CSV missing required columns. Expected {expected_columns}, got {set(df.columns)}")
        sys.exit(1)
        
    if len(df) < 20:
        print(f"Error: Dataset contains {len(df)} points. Minimum required is 20 points (Requirement R5).")
        sys.exit(1)
        
    print(f"Success: Loaded {len(df)} valid spatial data points from {filepath}.")
    return df

if __name__ == "__main__":
    # Test loading our sample data
    data_path = "data/measurements.csv"
    load_rssi_data(data_path)