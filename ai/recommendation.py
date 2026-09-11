def recommendation(current_stock, predicted_demand, lead_time_days, safety_stock=10):
    required = predicted_demand + safety_stock
    order_qty = max(0, round(required - current_stock))
    risk = "HIGH" if current_stock < predicted_demand else "LOW"
    return {"stockout_risk": risk, "recommended_order": order_qty}
