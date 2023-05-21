from django.db import models

from api.models.user import User


class Cart(models.Model):
    user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE, db_column="user")
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")

    def __str__(self):
        return f"{self.user}'s cart"

