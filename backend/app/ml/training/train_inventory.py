import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor, IsolationForest

from app.core.database import SessionLocal
from app.ml.datasets.inventory_dataset import load_inventory_data
from app.ml.features.inventory_features import build_inventory_features

BASE_PATH = Path("app/ml/models/artifacts")
DEMAND_MODEL = BASE_PATH / "inventory_demand_model.pkl"
ANOMALY_MODEL = BASE_PATH / "inventory_anomaly_model.pkl"


def train_inventory_models():
    db = SessionLocal()

    df = load_inventory_data(db)
    df = build_inventory_features(df)

    X = df[
        ["day", "month", "year", "dayofweek", "lag_1", "lag_3", "rolling_3"]
    ]
    y = df["quantity"]

    # Demand Forecasting
    demand_model = RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )
    demand_model.fit(X, y)

    # Anomaly Detection
    anomaly_model = IsolationForest(
        contamination=0.05,
        random_state=42
    )
    anomaly_model.fit(X)

    BASE_PATH.mkdir(parents=True, exist_ok=True)
    joblib.dump(demand_model, DEMAND_MODEL)
    joblib.dump(anomaly_model, ANOMALY_MODEL)

    print("✅ Inventory demand & anomaly models trained")


if __name__ == "__main__":
    train_inventory_models()
