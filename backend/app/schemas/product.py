from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=200)
    category_id: int
    subcategory_id: int

    unit_cost: float = Field(..., gt=0)
    selling_price: float = Field(..., gt=0)
    lower_threshold: int = Field(..., ge=0)
    upper_threshold: int = Field(..., gt=0)

class ProductCreate(ProductBase):
    initial_stock: int = Field(ge=0, default=0)

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=200)
    unit_cost: Optional[float] = Field(None, gt=0)
    selling_price: Optional[float] = Field(None, gt=0)
    lower_threshold: Optional[int] = Field(None, ge=0)
    upper_threshold: Optional[int] = Field(None, gt=0)

class ProductOut(ProductBase):
    id: int
    current_stock: int

    class Config:
        from_attributes = True

