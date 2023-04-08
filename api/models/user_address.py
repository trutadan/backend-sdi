from django.db import models


class UserAddress(models.Model):
    street = models.TextField(db_column="street")
    city = models.CharField(max_length=25, db_column="city")
    state = models.CharField(max_length=25, db_column="state")
    country = models.CharField(max_length=25, default="Romania", db_column="country")
    zip_code = models.CharField(max_length=10, db_column="zip_code")

    def __str__(self):
        return f"{self.zip_code}, {self.street}, {self.city}, {self.country}"
  