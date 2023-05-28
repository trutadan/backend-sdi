from api.ml_models.predict_shipping_time.integration import get_shipping_time_prediction
from api.models.order import Order


def estimate_delivery_date(order_id):
    order = Order.objects.get(id=order_id)
    shipping_time = get_shipping_time_prediction(order_id)
    
    delivery_date = order.ordered_date + shipping_time

    return delivery_date
