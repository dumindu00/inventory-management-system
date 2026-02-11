from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.models.base import Base

class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship(
        "Category",
        back_populates="subcategories"
    )

    __table_args__ = (
        UniqueConstraint("name", "category_id", name="uq_subcategory_name_category"),
    )
