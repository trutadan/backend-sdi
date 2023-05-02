from django.db import models

from django.contrib.auth.models import AbstractUser

from api.models.user_address import UserAddress
from api.models.user_profile import UserProfile


class User(AbstractUser):
    first_name = models.CharField(max_length=20, db_column="first_name")
    last_name = models.CharField(max_length=20, db_column="last_name")
    email = models.EmailField(unique=True, db_column="email")
    username = models.CharField(unique=True, db_index=True, max_length=50, db_column="username")
    password = models.CharField(max_length=50, db_column="password")
    address = models.OneToOneField(UserAddress, blank=True, null=True, on_delete=models.SET_NULL, db_column="address")
    profile = models.OneToOneField(UserProfile, blank=True, null=True, on_delete=models.SET_NULL, db_column="profile")
    is_active = models.BooleanField(default=False, db_column="is_active")
    confirmation_code = models.CharField(max_length=50, blank=True, null=True, unique=True)
    confirmation_code_expiration = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")

    REQUIRED_FIELDS = []

    class Role(models.TextChoices):    
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Moderator"
        REGULAR = "REGULAR", "Regular"
        ANONYMOUS = "ANONYMOUS", "Anonymous"

    role = models.CharField(max_length=50, choices=Role.choices, blank=True, null=True, db_column="role")

    def __str__(self):
        return f"user {self.username}" 
    