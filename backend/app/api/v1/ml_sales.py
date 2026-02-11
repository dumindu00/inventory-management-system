from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from app.api.deps import get_db
from app.schemas.ml_sales import (
    SalesPredictionRequest,
    SalesPredictionResponse,
    SalesChartResponse,
    SalesChartPoint,
)
from app.services.sales_ml_service import predict_next_day_sales
from app.models.sale import Sale

router = APIRouter(prefix="/ml/sales", tags=["ML Sales"])


@router.post("/predict", response_model=SalesPredictionResponse)
def predict_sales_api(payload: SalesPredictionRequest):
    from app.ml.prediction.predict_sales import predict_sales

    value = predict_sales(payload.dict())
    return {"predicted_sales": value}


@router.get("/chart/{product_id}", response_model=SalesChartResponse)
def sales_chart(product_id: int, db: Session = Depends(get_db)):
    sales = (
        db.query(Sale)
        .filter(Sale.product_id == product_id)
        .order_by(Sale.created_at)
        .all()
    )

    if not sales:
        raise HTTPException(status_code=404, detail="No sales data")

    data = []
    for s in sales:
        data.append(
            SalesChartPoint(
                date=s.created_at.date(),
                actual=s.quantity,
                predicted=None,
            )
        )

    prediction = predict_next_day_sales(db, product_id)
    if prediction:
        data.append(
            SalesChartPoint(
                date=data[-1].date + timedelta(days=1),
                actual=None,
                predicted=prediction,
            )
        )

    return {
        "product_id": product_id,
        "data": data,
    }
