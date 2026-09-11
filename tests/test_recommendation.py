import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai.recommendation import recommendation

def test_high_stock_low_risk():
    result = recommendation(100, 50, 3)
    assert result["stockout_risk"] == "LOW"
    assert result["recommended_order"] == 0

def test_low_stock_high_risk():
    result = recommendation(20, 50, 3)
    assert result["stockout_risk"] == "HIGH"
    assert result["recommended_order"] == 40

def test_zero_stock():
    result = recommendation(0, 50, 3)
    assert result["stockout_risk"] == "HIGH"
    assert result["recommended_order"] == 60
