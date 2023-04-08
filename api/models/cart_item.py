from django.db import models

from api.models.item import Item
from api.models.cart import Cart


class CartItem(models.Model):
    item = models.ForeignKey(Item, related_name='item_carts', on_delete=models.CASCADE, db_column="item")
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE, db_column="cart")
    quantity = models.PositiveIntegerField(default=1, db_column="quantity")

    def __str__(self):
        return f"{self.quantity} piece(s) of {self.item} for the cart {self.cart}"
