from django.db import models

from api.models.user import User
from api.models.order_address import OrderAddress
from api.models.coupon import Coupon


class Order(models.Model):
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE, db_column="user")
    start_date = models.DateTimeField(auto_now_add=True, db_column="start_date")
    ordered_date = models.DateTimeField(db_column="ordered_date")
    shipping_address = models.ForeignKey(OrderAddress, related_name="shipping_address", blank=True, null=True, on_delete=models.SET_NULL, db_column="shipping_address")
    billing_address = models.ForeignKey(OrderAddress, related_name="billing_address", blank=True, null=True, on_delete=models.SET_NULL, db_column="billing_address")
    coupon = models.ForeignKey(Coupon, blank=True, null=True, on_delete=models.SET_NULL, db_column="coupon")
    being_delivered = models.BooleanField(default=False, db_column="delivered_status")
    received = models.BooleanField(default=False, db_column="received")
    refund_requested = models.BooleanField(default=False, db_column="refund_requested")
    refund_granted = models.BooleanField(default=False, db_column="refund_granted")

    def __str__(self):
        return f"{self.user}'s order with the id #{self.id}"
