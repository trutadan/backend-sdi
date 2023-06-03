from datetime import timedelta
import math

from api.ml_model.integration import get_shipping_time_prediction
from api.models.order import Order


def estimate_delivery_date(order_id):
    order = Order.objects.get(pk=order_id)
    shipping_time = get_shipping_time_prediction(order_id)

    delivery_date = order.order_placed_date + timedelta(days=(math.ceil(shipping_time)))

    return delivery_date
