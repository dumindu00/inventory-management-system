from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date
from app.models.sale import Sale
from app.models.product import Product

def daily_revenue(db: Session):
    return (
        db.query(
            cast(Sale.created_at, Date).label("date"),
            func.sum(Sale.revenue).label("total_revenue"),
            func.sum(Sale.quantity).label("total_quantity")
        )
        .group_by(cast(Sale.created_at, Date))
        .order_by(cast(Sale.created_at, Date))
        .all()
    )


def monthly_revenue(db: Session):
    return (
        db.query(
            func.strftime("%Y-%m", Sale.created_at).label("month"),
            func.sum(Sale.revenue).label("total_revenue"),
            func.sum(Sale.quantity).label("total_quantity")
        )
        .group_by(func.strftime("%Y-%m", Sale.created_at))
        .order_by(func.strftime("%Y-%m", Sale.created_at))
        .all()
    )

def product_sales_report(db: Session):
    return (
        db.query(
            Product.id,
            Product.name,
            func.sum(Sale.quantity).label("units_sold"),
            func.sum(Sale.revenue).label("total_revenue")
        )
        .join(Sale, Sale.product_id == Product.id)
        .group_by(Product.id)
        .order_by(func.sum(Sale.revenue).desc())
        .all()
    )
