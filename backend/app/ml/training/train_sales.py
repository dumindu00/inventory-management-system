import joblib
from app.ml.datasets.sales_dataset import build_sales_dataset
from app.ml.features.sales_features import build_sales_features
from app.ml.pipelines.sales_pipeline import sales_pipeline

def train():
    df = build_sales_dataset()
    df = build_sales_features(df)

    X = df[["lag_1", "lag_7", "rolling_7"]]
    y = df["sales_qty"]

    model = sales_pipeline()
    model.fit(X, y)

    joblib.dump(model, "app/ml/models/artifacts/sales_model.pkl")
    print("Sales model trained")

if __name__ == "__main__":
    train()
