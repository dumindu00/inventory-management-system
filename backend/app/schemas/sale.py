from pydantic import BaseModel, Field
from datetime import datetime
class SaleCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class SaleRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    revenue: float
    created_at: datetime

    class Config:
        from_attributes = True
