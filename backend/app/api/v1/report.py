from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.report_service import (
    daily_revenue,
    monthly_revenue,
    product_sales_report
)

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/daily")
def get_daily_revenue(db: Session = Depends(get_db)):
    return daily_revenue(db)

@router.get("/monthly")
def get_monthly_revenue(db: Session = Depends(get_db)):
    return monthly_revenue(db)

@router.get("/products")
def get_product_sales(db: Session = Depends(get_db)):
    return product_sales_report(db)
