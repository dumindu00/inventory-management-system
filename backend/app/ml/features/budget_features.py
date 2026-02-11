import pandas as pd


def build_budget_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])

    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    df["lag_1"] = df["amount"].shift(1)
    df["lag_3"] = df["amount"].shift(3)

    df["rolling_3"] = df["amount"].rolling(3).mean()

    df = df.dropna()
    return df
