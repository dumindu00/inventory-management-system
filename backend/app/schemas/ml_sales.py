from pydantic import BaseModel
from datetime import date
from typing import List


class SalesPredictionRequest(BaseModel):
    lag_1: float
    lag_7: float
    rolling_7: float


class SalesPredictionResponse(BaseModel):
    predicted_sales: float


class SalesChartPoint(BaseModel):
    date: date
    actual: float | None
    predicted: float | None


class SalesChartResponse(BaseModel):
    product_id: int
    data: List[SalesChartPoint]
