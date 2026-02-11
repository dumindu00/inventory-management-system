# app/schemas/purchase.py
from pydantic import BaseModel

class PurchaseCreate(BaseModel):
    supplier_id: int
    product_id: int
    quantity: int
    unit_cost: float
    invoice_ref: str | None = None
