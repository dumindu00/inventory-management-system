from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from app.api.deps import get_db
from app.schemas.ml_budget import (
    BudgetPredictionRequest,
    BudgetPredictionResponse,
    BudgetChartResponse,
    BudgetChartPoint,
)
from app.services.budget_ml_service import predict_next_budget
from app.models.budget import Budget

router = APIRouter(prefix="/ml/budget", tags=["ML Budget"])


@router.post("/predict", response_model=BudgetPredictionResponse)
def predict_budget_api(payload: BudgetPredictionRequest):
    from app.ml.prediction.predict_budget import predict_budget

    value = predict_budget(payload.dict())
    overspend = value > payload.rolling_3 * 1.2

    return {
        "predicted_amount": value,
        "overspend_risk": overspend,
    }


@router.get("/chart/{category_id}", response_model=BudgetChartResponse)
def budget_chart(category_id: int, db: Session = Depends(get_db)):
    budgets = (
        db.query(Budget)
        .filter(Budget.category_id == category_id)
        .order_by(Budget.date)
        .all()
    )

    if not budgets:
        raise HTTPException(status_code=404, detail="No budget data")

    data = [
        BudgetChartPoint(
            date=b.date,
            actual=b.amount,
            predicted=None,
        )
        for b in budgets
    ]

    predicted, _ = predict_next_budget(db, category_id)
    if predicted:
        data.append(
            BudgetChartPoint(
                date=data[-1].date + timedelta(days=30),
                actual=None,
                predicted=predicted,
            )
        )

    return {
        "category_id": category_id,
        "data": data,
    }
