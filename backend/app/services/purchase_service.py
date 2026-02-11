# app/services/purchase_service.py
from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.purchase import Purchase
from app.models.inventory import InventoryTransaction
from fastapi import HTTPException

def create_purchase(db: Session, data):
    product = db.get(Product, data.product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    purchase = Purchase(
        supplier_id=data.supplier_id,
        product_id=data.product_id,
        quantity=data.quantity,
        unit_cost=data.unit_cost,
        total_cost=data.quantity * data.unit_cost,
        invoice_ref=data.invoice_ref
    )

    inventory_tx = InventoryTransaction(
        product_id=data.product_id,
        quantity=data.quantity,
        transaction_type="IN",
        reference=f"PURCHASE:{data.invoice_ref}"
    )

    try:
        product.current_stock += data.quantity

        db.add(purchase)
        db.add(inventory_tx)
        db.commit()
        db.refresh(purchase)

    except Exception:
        db.rollback()
        raise

    return purchase
