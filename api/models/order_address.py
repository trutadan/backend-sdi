from django.db import models


class OrderAddress(models.Model):
    country = models.CharField(max_length=25, default="Romania", db_column="country")
    state = models.CharField(max_length=25, db_column="state")
    city = models.CharField(max_length=25, db_column="city")
    street = models.CharField(max_length=25, db_column="street")
    apartment = models.CharField(max_length=25, blank=True, null=True, db_column="apartment")
    zip_code = models.CharField(max_length=10, db_column="zip_code")

    def __str__(self):
        return f"{self.zip_code}, {self.street}, {self.city}, {self.country}"
