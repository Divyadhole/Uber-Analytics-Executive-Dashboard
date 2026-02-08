import pandas as pd
import numpy as np
import os

def load_and_transform():
    print("Loading data...")
    # Adjust path if needed. Assuming user runs from project root.
    # The file is in ../archive if running from Uber-Analytics/python
    # But for simplicity, let's assume we copy data or read from absolute path
    # Or relative: ../../archive/ncr_ride_bookings.csv
    
    try:
        # Try relative path first (assuming running from Uber-Analytics)
        df = pd.read_csv('../archive/ncr_ride_bookings.csv')
    except FileNotFoundError:
        try:
             # Try absolute path based on user environment
             df = pd.read_csv('/Users/divyadhole/Desktop/Uber Data Analytics Dashboard/archive/ncr_ride_bookings.csv')
        except FileNotFoundError:
            print("Error: Could not find data file.")
            return None

    # 1.1 Data Standardisation
    # Remove triple quotes
    df = df.apply(lambda x: x.str.replace('"', '', regex=False) if x.dtype == "object" else x)
    
    # Handle 'null' strings
    df.replace('null', np.nan, inplace=True)
    
    # 1.2 Type Casting
    numeric_cols = ['Booking Value', 'Ride Distance', 'Driver Ratings', 'Customer Rating', 'Avg VTAT', 'Avg CTAT']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Time'] = pd.to_timedelta(df['Time'], errors='coerce')
    
    # Save transformed data
    os.makedirs('data', exist_ok=True)
    output_path = 'data/uber_data_cleaned.csv'
    df.to_csv(output_path, index=False)
    print(f"Data transformed and saved to {output_path}")
    return df

if __name__ == "__main__":
    load_and_transform()
