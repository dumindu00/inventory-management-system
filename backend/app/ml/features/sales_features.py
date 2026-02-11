import pandas as pd

def build_sales_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["product_id", "date"])

    df["lag_1"] = df.groupby("product_id")["sales_qty"].shift(1)
    df["lag_7"] = df.groupby("product_id")["sales_qty"].shift(7)

    df["rolling_7"] = (
        df.groupby("product_id")["sales_qty"]
        .rolling(7)
        .mean()
        .reset_index(level=0, drop=True)
    )

    df = df.dropna()
    return df
