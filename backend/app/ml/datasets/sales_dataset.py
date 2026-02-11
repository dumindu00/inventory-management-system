import pandas as pd
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.sale import Sale
from app.models.product import Product

def build_sales_dataset() -> pd.DataFrame:
    db: Session = SessionLocal()

    query = (
        db.query(
            Sale.product_id,
            Sale.quantity,
            Sale.revenue,
            Sale.created_at,
            Product.category_id
        )
        .join(Product, Product.id == Sale.product_id)
    )

    df = pd.read_sql(query.statement, db.bind)
    db.close()

    df["date"] = pd.to_datetime(df["created_at"]).dt.date

    dataset = (
        df.groupby(["date", "product_id", "category_id"])
        .agg(
            sales_qty=("quantity", "sum"),
            revenue=("revenue", "sum")
        )
        .reset_index()
    )

    return dataset
