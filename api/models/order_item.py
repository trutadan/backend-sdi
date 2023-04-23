from django.db import models

from api.models.item import Item
from api.models.order import Order


class OrderItem(models.Model):
    item = models.ForeignKey(Item, related_name='item_orders', on_delete=models.CASCADE, db_column="item")
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE, db_column="order_number")
    quantity = models.PositiveIntegerField(default=1, db_column="quantity")

    def __str__(self):
        return f"{self.quantity} piece(s) of {self.item} for the order {self.order}"
