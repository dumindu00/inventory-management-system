from sqlalchemy import Column, Integer, Float, ForeignKey
from app.models.base import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    allocated_budget = Column(Float, nullable=False)
    actual_spent = Column(Float, default=0)
