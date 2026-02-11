from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.budget import Budget

router = APIRouter(prefix="/budgets", tags=["Budgets"])


@router.get("/", response_model=List[dict])
def list_budgets(db: Session = Depends(get_db)):
    return db.query(Budget).all()
