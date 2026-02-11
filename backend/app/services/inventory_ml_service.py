from sqlalchemy.orm import Session
from datetime import timedelta
from app.models.inventory import InventoryTransaction
from app.ml.prediction.predict_inventory import predict_demand, detect_anomaly


def inventory_forecast(db: Session, product_id: int):
    tx = (
        db.query(InventoryTransaction)
        .filter(InventoryTransaction.product_id == product_id)
        .order_by(InventoryTransaction.created_at.desc())
        .limit(3)
        .all()
    )

    if len(tx) < 3:
        return None, False

    tx = list(reversed(tx))

    quantities = [
        -t.quantity if t.transaction_type == "OUT" else t.quantity
        for t in tx
    ]

    last_date = tx[-1].created_at

    features = {
        "day": last_date.day,
        "month": last_date.month,
        "year": last_date.year,
        "dayofweek": last_date.weekday(),
        "lag_1": quantities[-1],
        "lag_3": quantities[0],
        "rolling_3": sum(quantities) / 3,
    }

    prediction = predict_demand(features)
    anomaly = detect_anomaly(features)

    return prediction, anomaly
