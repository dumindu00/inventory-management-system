# app/models/alert.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    alert_type = Column(String(50), nullable=False)
    message = Column(String(255), nullable=False)
    status = Column(String(20), default="ACTIVE")  # ACTIVE / RESOLVED

    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")
