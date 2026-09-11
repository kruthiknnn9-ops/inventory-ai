import sys
from pathlib import Path
import pandas as pd
sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai.anomaly import detect_anomalies

def test_anomaly_output_columns():
    sales = pd.DataFrame({
        "product_id": ["P1"] * 10,
        "day": list(range(1, 11)),
        "sales": [5, 5, 6, 5, 7, 5, 6, 5, 100, 5]
    })
    result = detect_anomalies(sales)
    assert "anomaly_label" in result.columns
    assert set(result["anomaly_label"]).issubset({"normal", "anomaly"})
