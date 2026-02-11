from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from app.api.deps import get_db
from app.schemas.ml_inventory import (
    InventoryDemandRequest,
    InventoryDemandResponse,
    InventoryChartResponse,
    InventoryChartPoint,
)
from app.services.inventory_ml_service import inventory_forecast
from app.models.inventory import InventoryTransaction

router = APIRouter(prefix="/ml/inventory", tags=["ML Inventory"])


@router.post("/demand", response_model=InventoryDemandResponse)
def predict_inventory_demand(payload: InventoryDemandRequest):
    from app.ml.prediction.predict_inventory import (
        predict_demand,
        detect_anomaly,
    )

    demand = predict_demand(payload.dict())
    anomaly = detect_anomaly(payload.dict())

    return {
        "predicted_demand": demand,
        "anomaly": anomaly,
    }


@router.get("/chart/{product_id}", response_model=InventoryChartResponse)
def inventory_chart(product_id: int, db: Session = Depends(get_db)):
    tx = (
        db.query(InventoryTransaction)
        .filter(InventoryTransaction.product_id == product_id)
        .order_by(InventoryTransaction.created_at)
        .all()
    )

    if not tx:
        raise HTTPException(status_code=404, detail="No inventory data")

    data = []
    for t in tx:
        qty = t.quantity if t.transaction_type == "OUT" else -t.quantity
        data.append(
            InventoryChartPoint(
                date=t.created_at.date(),
                actual=qty,
                predicted=None,
                anomaly=False,
            )
        )

    predicted, anomaly = inventory_forecast(db, product_id)
    if predicted is not None:
        data.append(
            InventoryChartPoint(
                date=data[-1].date + timedelta(days=1),
                actual=None,
                predicted=predicted,
                anomaly=anomaly,
            )
        )

    return {
        "product_id": product_id,
        "data": data,
    }
