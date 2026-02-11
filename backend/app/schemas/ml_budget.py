from pydantic import BaseModel
from typing import List
from datetime import date


class BudgetPredictionRequest(BaseModel):
    month: int
    year: int
    lag_1: float
    lag_3: float
    rolling_3: float


class BudgetPredictionResponse(BaseModel):
    predicted_amount: float
    overspend_risk: bool


class BudgetChartPoint(BaseModel):
    date: date
    actual: float | None
    predicted: float | None


class BudgetChartResponse(BaseModel):
    category_id: int
    data: List[BudgetChartPoint]
