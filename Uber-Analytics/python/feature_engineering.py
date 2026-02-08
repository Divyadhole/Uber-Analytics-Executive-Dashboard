import pandas as pd
import numpy as np

def create_features(df):
    print("Engineering features...")
    
    # Temporal Features
    df['Month'] = df['Date'].dt.month_name()
    df['Day_of_Week'] = df['Date'].dt.day_name()
    df['Hour'] = df['Time'].dt.components['hours']
    
    # Time of Day
    df['Time_of_Day'] = pd.cut(df['Hour'], 
                               bins=[0, 6, 12, 18, 24], 
                               labels=['Late Night', 'Morning', 'Afternoon', 'Evening'], 
                               include_lowest=True)
    
    # Revenue metrics
    df['Revenue_per_KM'] = df['Booking Value'] / df['Ride Distance']
    
    # Binary target for ML (e.g., High Value Ride > 500)
    # Or Cancellation Prediction (Status != Completed)
    df['Is_Completed'] = (df['Booking Status'] == 'Completed').astype(int)
    
    # Encoding Categorical (Simple mapping for demo)
    # In a real pipeline, use Sklearn encoders fits
    
    return df

if __name__ == "__main__":
    try:
        df = pd.read_csv('data/uber_data_cleaned.csv')
        df['Date'] = pd.to_datetime(df['Date']) # Reload types
        df['Time'] = pd.to_timedelta(df['Time'])
        
        df = create_features(df)
        df.to_csv('data/uber_data_features.csv', index=False)
        print("Features created and saved.")
    except Exception as e:
        print(f"Error: {e}")
