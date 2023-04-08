from django.db import models


class Coupon(models.Model):
    code = models.CharField(max_length=15, db_column="code")
    amount = models.FloatField(db_column="amount")

    def __str__(self):
        return f"coupon code {self.code} for the amount of {self.amount}"
   