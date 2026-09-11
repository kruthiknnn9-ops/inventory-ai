import sys
from pathlib import Path
import pandas as pd
sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai.forecast import forecast_demand

def test_forecast_returns_non_negative_number():
    sales = pd.DataFrame({
        "product_id": ["P1"] * 7,
        "day": list(range(1, 8)),
        "sales": [5, 6, 7, 6, 8, 7, 9]
    })
    result = forecast_demand(sales, "P1", 7)
    assert isinstance(result, float)
    assert result >= 0

def test_unknown_product_returns_zero():
    sales = pd.DataFrame({
        "product_id": ["P1"] * 2,
        "day": [1, 2],
        "sales": [5, 6]
    })
    assert forecast_demand(sales, "UNKNOWN", 7) == 0.0
