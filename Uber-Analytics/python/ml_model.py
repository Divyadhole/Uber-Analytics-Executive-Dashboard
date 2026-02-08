import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
import joblib
import os

def train_model():
    print("Training ML model...")
    
    try:
        df = pd.read_csv('data/uber_data_features.csv')
    except Exception as e:
        print("Feature data not found. Run feature_engineering.py first.")
        return

    # Task: Predict if a ride will be Completed (Target: Is_Completed)
    # Features: Vehicle Type (encoded), Ride Distance, Booking Value (maybe leakage?), Hour
    
    # Simple encoding
    df_encoded = pd.get_dummies(df, columns=['Vehicle Type', 'Payment Method'], drop_first=True)
    
    features = ['Ride Distance', 'Hour', 'Booking Value'] + [c for c in df_encoded.columns if 'Vehicle Type_' in c]
    target = 'Is_Completed'
    
    # Handle NaNs
    df_clean = df_encoded.dropna(subset=features + [target])
    
    X = df_clean[features]
    y = df_clean[target]
    
    if len(X) < 100:
        print("Not enough data to train.")
        return

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    roc = roc_auc_score(y_test, y_prob)
    
    print(f"Model Trained. Accuracy: {acc:.2f}, ROC-AUC: {roc:.2f}")
    
    # Save model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/rf_completion_model.pkl')
    
    # Save metrics for poster
    with open('models/metrics.txt', 'w') as f:
        f.write(f"Accuracy: {acc:.1%}\nROC-AUC: {roc:.1%}")

if __name__ == "__main__":
    train_model()
