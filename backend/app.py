from pathlib import Path
import pandas as pd
from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE))

from ai.forecast import forecast_demand
from ai.anomaly import detect_anomalies
from ai.recommendation import recommendation

app = Flask(__name__)
CORS(app)

inventory = pd.read_csv(BASE / "data" / "inventory.csv")
sales = pd.read_csv(BASE / "data" / "sales_history.csv")

@app.get("/")
def home():
    return render_template_string((BASE / "frontend" / "index.html").read_text())

@app.get("/api/inventory")
def get_inventory():
    return jsonify(inventory.to_dict(orient="records"))

@app.get("/api/predict/<product_id>")
def predict(product_id):
    row = inventory[inventory["product_id"] == product_id]
    if row.empty:
        return jsonify({"error": "Product not found"}), 404
    r = row.iloc[0]
    predicted = forecast_demand(sales, product_id, 7)
    result = recommendation(float(r.current_stock), predicted,
                            int(r.lead_time_days))
    return jsonify({
        "product_id": product_id,
        "product_name": r.product_name,
        "current_stock": int(r.current_stock),
        "predicted_7_day_demand": predicted,
        **result
    })

@app.get("/api/anomalies")
def anomalies():
    result = detect_anomalies(sales)
    return jsonify(result.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
