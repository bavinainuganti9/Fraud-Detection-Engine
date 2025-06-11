import pandas as pd
from sklearn.ensemble import IsolationForest
from utils import load_features
import joblib
import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")

def train_model():
    X = load_features("sample_data.csv")
    model = IsolationForest(n_estimators=100, contamination=0.15, random_state=42)
    model.fit(X)
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model trained and saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
