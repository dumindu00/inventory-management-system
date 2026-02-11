from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, data: ProductCreate) -> Product:
    if data.upper_threshold <= data.lower_threshold:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Upper threshold must be greater than lower threshold"
        )

    product = Product(
        name=data.name,
        category_id=data.category_id,
        subcategory_id=data.subcategory_id,
        unit_cost=data.unit_cost,
        selling_price=data.selling_price,
        lower_threshold=data.lower_threshold,
        upper_threshold=data.upper_threshold,
        current_stock=data.initial_stock,
    )

    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_products(db: Session):
    return db.query(Product).all()


def get_product(db: Session, product_id: int) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def update_product(db: Session, product_id: int, data: ProductUpdate) -> Product:
    product = get_product(db, product_id)

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(product, field, value)

    if product.upper_threshold <= product.lower_threshold:
        raise HTTPException(
            status_code=400,
            detail="Upper threshold must be greater than lower threshold"
        )

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    db.delete(product)
    db.commit()
