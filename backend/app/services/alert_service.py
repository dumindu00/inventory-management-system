# app/services/alert_service.py
from sqlalchemy.orm import Session
from app.models.alert import Alert

def evaluate_stock_alerts(db: Session, product):
    # Resolve existing alerts first
    db.query(Alert).filter(
        Alert.product_id == product.id,
        Alert.status == "ACTIVE"
    ).update({"status": "RESOLVED"})

    alerts = []

    if product.current_stock <= product.lower_threshold:
        alerts.append(Alert(
            product_id=product.id,
            alert_type="LOW_STOCK",
            message=f"Low stock: {product.current_stock} remaining"
        ))

    if product.current_stock >= product.upper_threshold:
        alerts.append(Alert(
            product_id=product.id,
            alert_type="OVER_STOCK",
            message=f"Overstock: {product.current_stock} units"
        ))

    for alert in alerts:
        db.add(alert)

    db.flush()
