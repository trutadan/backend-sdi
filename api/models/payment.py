from django.db import models

from api.models.order import Order


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, db_column="order")
    timestamp = models.DateTimeField(auto_now_add=True, db_column="timestamp")
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.amount = self.get_amount()
        super().save(*args, **kwargs)

    def get_amount(self):
        total_amount = 0
        for item in self.order.orderitem_set.all():
            if item.item.discount_price:
                total_amount += item.item.discount_price * item.quantity
            else:
                total_amount += item.item.price * item.quantity

        if self.order.coupon:
            total_amount *= (1 - (self.order.coupon.amount / 100))

        return total_amount

    def __str__(self):
        return f"payment for the {self.order} for the amount {self.amount}"
