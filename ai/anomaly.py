import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(sales_df):
    df = sales_df.copy()
    model = IsolationForest(contamination=0.10, random_state=42)
    df["anomaly"] = model.fit_predict(df[["sales"]])
    df["anomaly_label"] = df["anomaly"].map({1: "normal", -1: "anomaly"})
    return df
