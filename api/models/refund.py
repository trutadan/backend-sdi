from django.db import models

from api.models.order import Order


class Refund(models.Model):
    order = models.OneToOneField(Order, blank=True, null=True, on_delete=models.CASCADE, db_column="order")
    reason = models.TextField(db_column="reason")
    accepted = models.BooleanField(default=False, db_column="status")

    def __str__(self):
        return f"refund for the order {self.order} with the accepted status '{self.accepted}'"
   