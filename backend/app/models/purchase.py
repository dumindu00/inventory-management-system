# app/models/purchase.py
from sqlalchemy import String, Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    quantity = Column(Integer, nullable=False)
    unit_cost = Column(Float, nullable=False)
    total_cost = Column(Float, nullable=False)

    invoice_ref = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    supplier = relationship("Supplier")
    product = relationship("Product")
