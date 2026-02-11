import pandas as pd
from sqlalchemy.orm import Session
from app.models.budget import Budget

def load_budget_data(db: Session) -> pd.DataFrame:
    budgets = db.query(Budget).order_by(Budget.date).all()
    
    data = [
        {
            "date": b.date,
            "category_id": b.category_id,
            "amount": b.amount,
        }
        for b in budgets
    ]
    
    return pd.DataFrame(data)