from pydantic import BaseModel
from typing import List
from datetime import date


class InventoryDemandRequest(BaseModel):
    day: int
    month: int
    year: int
    dayofweek: int
    lag_1: float
    lag_3: float
    rolling_3: float


class InventoryDemandResponse(BaseModel):
    predicted_demand: float
    anomaly: bool


class InventoryChartPoint(BaseModel):
    date: date
    actual: float | None
    predicted: float | None
    anomaly: bool = False


class InventoryChartResponse(BaseModel):
    product_id: int
    data: List[InventoryChartPoint]
