# app/schemas/alert.py
from pydantic import BaseModel
from datetime import datetime

class AlertRead(BaseModel):
    id: int
    product_id: int
    alert_type: str
    message: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
