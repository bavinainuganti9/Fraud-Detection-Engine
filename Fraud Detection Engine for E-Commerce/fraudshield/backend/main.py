from fastapi import FastAPI
from pydantic import BaseModel
from utils import preprocess_order
from model import load_model

app = FastAPI(title="FraudShield API")
model = load_model()

class Order(BaseModel):
    order_value: float
    num_items: int
    time_to_checkout: float
    refund_count: int
    is_bot: int

@app.get("/")
def read_root():
    return {"status": "FraudShield API is live"}

@app.post("/predict")
def predict(order: Order):
    features = preprocess_order(order.dict())
    score = model.decision_function(features)[0]
    label = model.predict(features)[0]

    return {
        "fraud_score": float(score),
        "is_anomalous": bool(label == -1),
        "message": "High fraud risk!" if label == -1 else "Transaction appears normal."
    }
