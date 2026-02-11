from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.schemas.inventory import StockIn, StockOut, InventoryTransactionOut
from app.services.inventory_service import stock_in, stock_out

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/in", response_model=InventoryTransactionOut)
def inventory_in(data: StockIn, db: Session = Depends(get_db_session)):
    return stock_in(db, data)

@router.post("/out", response_model=InventoryTransactionOut)
def inventory_out(data: StockOut, db: Session = Depends(get_db_session)):
    return stock_out(db, data)