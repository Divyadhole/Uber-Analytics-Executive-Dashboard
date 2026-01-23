import pandas as pd
import os

# Paths
source_csv = '/Users/divyadhole/Desktop/Uber Data Analytics Dashboard/archive/ncr_ride_bookings.csv'
target_csv = '/Users/divyadhole/Desktop/Uber Data Analytics Dashboard/archive/ncr_ride_bookings_sampled.csv'

if os.path.exists(source_csv):
    print(f"Loading data from {source_csv}...")
    df = pd.read_csv(source_csv)
    
    # Sample 5,000 rows for instant web loading
    # We use random_state for reproducibility
    sampled_df = df.sample(n=min(5000, len(df)), random_state=42)
    
    # Save optimized version
    sampled_df.to_csv(target_csv, index=False)
    print(f"Successfully created sampled dataset at {target_csv} ({len(sampled_df)} rows)")
else:
    print(f"Error: Source file {source_csv} not found.")
