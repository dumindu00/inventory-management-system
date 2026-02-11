import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("app/ml/models/artifacts/sales_model.pkl")

_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_sales(features: dict) -> float:
    model = load_model()
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    return float(prediction[0])
