from pydantic import BaseModel
from typing import Optional

class DailyRevenueReport(BaseModel):
    date: str
    total_revenue: float
    total_quantity: int


class MonthlyRevenueReport(BaseModel):
    month: str
    total_revenue: float
    total_quantity: int


class ProductSalesReport(BaseModel):
    id: int
    name: str
    units_sold: int
    total_revenue: float
