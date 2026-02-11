
from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    contact_info = Column(String(255), nullable=True)
