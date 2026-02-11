import pandas as pd
from sqlalchemy.orm import Session
from app.models.inventory import InventoryTransaction


def load_inventory_data(db: Session) -> pd.DataFrame:
    rows = (
        db.query(InventoryTransaction)
        .order_by(InventoryTransaction.created_at)
        .all()
    )

    data = [
        {
            "product_id": r.product_id,
            "date": r.created_at.date(),
            "quantity": r.quantity if r.transaction_type == "OUT" else -r.quantity,
        }
        for r in rows
    ]

    df = pd.DataFrame(data)

    if df.empty:
        return df

    df = (
        df.groupby(["product_id", "date"])
        .sum()
        .reset_index()
    )

    return df
