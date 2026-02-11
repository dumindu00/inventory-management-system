# app/api/v1/purchase.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.purchase import PurchaseCreate
from app.services.purchase_service import create_purchase

router = APIRouter(prefix="/purchases", tags=["Purchases"])

@router.post("/")
def create_supplier_purchase(data: PurchaseCreate, db: Session = Depends(get_db)):
    return create_purchase(db, data)
