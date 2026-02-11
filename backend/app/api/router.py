from fastapi import APIRouter
from app.api.v1 import (
    product,
    inventory,
    sale,
    alert,
    purchase,
    report,
    ml_sales,
    ml_budget,
    ml_inventory,
)

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(product.router)
api_router.include_router(inventory.router)
api_router.include_router(sale.router)
api_router.include_router(alert.router)
api_router.include_router(purchase.router)
api_router.include_router(report.router)
api_router.include_router(ml_sales.router)
api_router.include_router(ml_budget.router)
api_router.include_router(ml_inventory.router)
