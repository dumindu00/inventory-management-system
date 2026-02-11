from sqlalchemy.orm import Session
from app.models.budget import Budget
from app.ml.prediction.predict_budget import predict_budget


def predict_next_budget(db: Session, category_id: int):
    history = (
        db.query(Budget)
        .filter(Budget.category_id == category_id)
        .order_by(Budget.date.desc())
        .limit(3)
        .all()
    )

    if len(history) < 3:
        return None, False

    history = list(reversed(history))

    features = {
        "month": history[-1].date.month + 1,
        "year": history[-1].date.year,
        "lag_1": history[-1].amount,
        "lag_3": history[0].amount,
        "rolling_3": sum(h.amount for h in history) / 3,
    }

    predicted = predict_budget(features)
    avg = features["rolling_3"]

    overspend_risk = predicted > avg * 1.2
    return predicted, overspend_risk
