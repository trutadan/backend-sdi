from django.db import models

from api.models.user_address import UserAddress
from api.models.user_profile import UserProfile


class User(models.Model):
    first_name = models.CharField(max_length=20, db_column="first_name")
    last_name = models.CharField(max_length=20, db_column="last_name")
    email = models.EmailField(unique=True, db_column="email")
    username = models.CharField(unique=True, db_index=True, max_length=50, db_column="username")
    address = models.OneToOneField(UserAddress, blank=True, null=True, on_delete=models.SET_NULL, db_column="address")
    profile = models.OneToOneField(UserProfile, blank=True, null=True, on_delete=models.SET_NULL, db_column="profile")
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")

    def __str__(self):
        return f"user {self.username}" 