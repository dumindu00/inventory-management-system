from pydantic import BaseModel, Field

class SaleCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class SaleRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    revenue: float
    created_at: str

    class Config:
        from_attributes = True
