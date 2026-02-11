from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.product import Product
from app.models import InventoryTransaction
from app.schemas.inventory import StockIn, StockOut
# app/services/sales_service.py
from app.services.alert_service import evaluate_stock_alerts


def stock_in(db: Session, data: StockIn):
    try:
        product = db.query(Product).filter(Product.id == data.product_id).with_for_update().first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        product.current_stock += data.quantity
        
        tx = InventoryTransaction(
            product_id=product.id,
            quantity=data.quantity,
            transaction_type="IN",
            reference=data.reference
        )
        
        db.add(tx)
        db.commit()
        db.refresh(tx)
        return tx
    except Exception:
        db.rollback()
        raise
    
def stock_out(db: Session, data: StockOut):
    try:
        product = db.query(Product).filter(Product.id == data.product_id).with_for_update().first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        if product.current_stock < data.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient stock"
            )
            
        product.current_stock -= data.quantity
        
        tx = InventoryTransaction(
            product_id=product.id,
            quantity=-data.quantity,
            transaction_type="OUT",
            reference=data.reference
        )
        
        db.add(tx)
        db.commit()
        db.refresh(tx)
        return tx
    
    except Exception:
        db.rollback()
        raise
