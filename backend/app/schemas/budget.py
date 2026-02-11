from pydantic import BaseModel, Field

class BudgetCreate(BaseModel):
    year: int
    category_id: int
    allocated_budget: float = Field(gt=0)

class BudgetRead(BudgetCreate):
    id: int
    actual_spent: float

    class Config:
        from_attributes = True
