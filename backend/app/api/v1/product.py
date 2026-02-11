from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db_session
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductOut
)
from app.services.product_service import (
    create_product,
    get_products,
    get_product,
    update_product,
    delete_product
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductOut)
def create(data: ProductCreate, db: Session = Depends(get_db_session)):
    return create_product(db, data)


@router.get("/", response_model=List[ProductOut])
def list_all(db: Session = Depends(get_db_session)):
    return get_products(db)


@router.get("/{product_id}", response_model=ProductOut)
def retrieve(product_id: int, db: Session = Depends(get_db_session)):
    return get_product(db, product_id)


@router.put("/{product_id}", response_model=ProductOut)
def update(product_id: int, data: ProductUpdate, db: Session = Depends(get_db_session)):
    return update_product(db, product_id, data)


@router.delete("/{product_id}", status_code=204)
def delete(product_id: int, db: Session = Depends(get_db_session)):
    delete_product(db, product_id)
