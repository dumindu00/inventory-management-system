import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from app.ml.datasets.budget_dataset import load_budget_data
from app.ml.features.budget_features import build_budget_features
from app.core.database import SessionLocal

MODEL_PATH = Path("app/ml/models/artifacts/budget_model.pkl")

def train_budget_model():
    db = SessionLocal()
    
    df = load_budget_data(db)
    df = build_budget_features(df)
    
    X = df[["month", "year", "lag_1", "lag_3", "rolling_3"]]
    y = df["amount"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    
    
    print("✅ Budget model trained & saved")
    
    if __name__ == "__main__":
        train_budget_model()