from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class InventoryTransactionBase(BaseModel):
    product_id: int
    quantity: int = Field(..., ne=0)
    reference: Optional[str] = None


class StockIn(InventoryTransactionBase):
    quantity: int = Field(..., gt=0)


class StockOut(InventoryTransactionBase):
    quantity: int = Field(..., gt=0)


class InventoryTransactionOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    transaction_type: str
    reference: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
