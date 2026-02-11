import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("app/ml/models/artifacts/budget_model.pkl")
_model = None


def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_budget(features: dict) -> float:
    model = load_model()
    df = pd.DataFrame([features])
    return float(model.predict(df)[0])
