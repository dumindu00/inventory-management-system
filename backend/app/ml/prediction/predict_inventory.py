import joblib
import pandas as pd
from pathlib import Path

BASE_PATH = Path("app/ml/models/artifacts")

_demand_model = None
_anomaly_model = None


def load_models():
    global _demand_model, _anomaly_model
    if _demand_model is None:
        _demand_model = joblib.load(BASE_PATH / "inventory_demand_model.pkl")
    if _anomaly_model is None:
        _anomaly_model = joblib.load(BASE_PATH / "inventory_anomaly_model.pkl")
    return _demand_model, _anomaly_model


def predict_demand(features: dict) -> float:
    demand_model, _ = load_models()
    df = pd.DataFrame([features])
    return float(demand_model.predict(df)[0])


def detect_anomaly(features: dict) -> bool:
    _, anomaly_model = load_models()
    df = pd.DataFrame([features])
    return anomaly_model.predict(df)[0] == -1
