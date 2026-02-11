from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException

from app.models import Product, Sale, InventoryTransaction


def process_sale(db: Session, product_id: int, quantity: int) -> Sale:
    try:
        # Lock row for concurrency safety
        product = (
            db.execute(
                select(Product)
                .where(Product.id == product_id)
                .with_for_update()
            )
            .scalars()
            .first()
        )

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if product.current_stock < quantity:
            raise HTTPException(status_code=400, detail="Insufficient stock")

        # Update stock
        product.current_stock -= quantity

        # Create sale record
        sale = Sale(
            product_id=product.id,
            quantity=quantity,
            revenue=quantity * product.selling_price
        )
        db.add(sale)

        # Inventory OUT transaction
        inventory_tx = InventoryTransaction(
            product_id=product.id,
            quantity=quantity,
            transaction_type="OUT",
            reference="SALE"
        )
        db.add(inventory_tx)

        db.commit()
        db.refresh(sale)

        return sale

    except Exception:
        db.rollback()
        raise
