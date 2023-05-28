from api.models.order import Order

from django.db import models
from django.db.models import F, ExpressionWrapper


def get_data():
    # Fetch the relevant order data
    orders = Order.objects.filter(
        being_delivered=True,
        received=False,
        refund_requested=False,
        refund_granted=False
    ).annotate(
        shipping_duration=ExpressionWrapper(
            F('ordered_date') - F('start_date'),
            output_field=models.DurationField()
        )
    )

    # Split the data into features and target variable
    X = orders.values('shipping_address__city', 'shipping_address__state')
    y = orders.values('shipping_duration')

    return X, y
