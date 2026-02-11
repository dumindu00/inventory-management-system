from sqlalchemy.orm import Session
from datetime import timedelta
from app.models.sale import Sale
from app.ml.prediction.predict_sales import predict_sales


def get_sales_history(db: Session, product_id: int, days: int = 30):
    sales = (
        db.query(Sale)
        .filter(Sale.product_id == product_id)
        .order_by(Sale.created_at.desc())
        .limit(days)
        .all()
    )
    return sales


def predict_next_day_sales(db: Session, product_id: int):
    history = get_sales_history(db, product_id, days=7)

    if len(history) < 7:
        return None

    quantities = [s.quantity for s in reversed(history)]

    features = {
        "lag_1": quantities[-1],
        "lag_7": quantities[0],
        "rolling_7": sum(quantities) / 7,
    }

    return predict_sales(features)
