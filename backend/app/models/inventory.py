from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base


class InventoryTransaction(Base):
    __tablename__ = "inventory_transactions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    quantity = Column(Integer, nullable=False)
    transaction_type = Column(String(20), nullable=False)
    reference = Column(String(100), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="inventory_transactions")
