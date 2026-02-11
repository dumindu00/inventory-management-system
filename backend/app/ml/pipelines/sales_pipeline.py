from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def sales_pipeline():
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("model", LinearRegression())
        ]
    )
