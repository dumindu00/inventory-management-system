import pandas as pd

def build_inventory_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year
    df["dayofweek"] = df["date"].dt.dayofweek
    
    df["lag_1"] = df.groupby("product_id")["quantity"].shift(1)
    df["lag_3"] = df.groupby("product_id")["quantity"].shift(3)
    df["rolling_3"] = (
        df.groupby("product_id")["quantity"]
        .rolling(3)
        .mean()
        .reset_index(level=0, drop=True)
        )
    
    df = df.dropna()
    return df