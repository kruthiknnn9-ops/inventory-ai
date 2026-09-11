import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_demand(sales_df, product_id, horizon_days=7):
    df = sales_df[sales_df["product_id"] == product_id].copy()
    if len(df) < 2:
        return 0.0
    X = df[["day"]]
    y = df["sales"]
    model = LinearRegression()
    model.fit(X, y)
    future = pd.DataFrame({"day": range(int(df["day"].max()) + 1,
                                        int(df["day"].max()) + 1 + horizon_days)})
    prediction = model.predict(future)
    return round(float(prediction.clip(min=0).sum()), 2)
