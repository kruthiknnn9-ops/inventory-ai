import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.app import app

def test_inventory_endpoint():
    client = app.test_client()
    response = client.get("/api/inventory")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_valid_prediction_endpoint():
    client = app.test_client()
    response = client.get("/api/predict/P001")
    assert response.status_code == 200
    body = response.get_json()
    assert "predicted_7_day_demand" in body
    assert "recommended_order" in body

def test_invalid_product_endpoint():
    client = app.test_client()
    response = client.get("/api/predict/INVALID")
    assert response.status_code == 404
