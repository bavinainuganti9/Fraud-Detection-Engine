import joblib
import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)
