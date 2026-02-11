from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.sale import Sale

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    subcategory_id = Column(Integer, ForeignKey("subcategories.id"), nullable=False)

    unit_cost = Column(Float, nullable=False)
    selling_price = Column(Float, nullable=False)

    current_stock = Column(Integer, default=0)
    lower_threshold = Column(Integer, nullable=False)
    upper_threshold = Column(Integer, nullable=False)

    category = relationship("Category")
    subcategory = relationship("SubCategory")

    inventory_transactions = relationship(
        "InventoryTransaction",
        back_populates="product",
        cascade="all, delete-orphan"
    )
    
    sales = relationship (
        "Sale",
        back_populates="product",
        cascade="all, delete-orphan"
    )