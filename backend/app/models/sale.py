from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    quantity = Column(Integer, nullable=False)
    revenue = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="sales")
