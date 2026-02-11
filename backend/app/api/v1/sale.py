from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import SaleCreate, SaleRead
from app.services.sales_service import process_sale
from app.api.deps import get_db_session

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/", response_model=SaleRead)
def create_sale(
    payload: SaleCreate,
    db: Session = Depends(get_db_session)
):
    return process_sale(
        db=db,
        product_id=payload.product_id,
        quantity=payload.quantity
    )
