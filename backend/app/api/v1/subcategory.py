from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.subcategory import SubCategory

router = APIRouter(prefix="/subcategories", tags=["SubCategories"])


@router.get("/", response_model=List[dict])
def list_subcategories(db: Session = Depends(get_db)):
    return db.query(SubCategory).all()
