from django.db import models

from django.contrib.auth.models import AbstractUser

from api.models.user_address import UserAddress
from api.models.user_profile import UserProfile


class User(AbstractUser):
    first_name = models.CharField(max_length=20, db_column="first_name")
    last_name = models.CharField(max_length=20, db_column="last_name")
    email = models.EmailField(unique=True, db_column="email")
    username = models.CharField(unique=True, db_index=True, max_length=50, db_column="username")
    password = models.CharField(max_length=100, db_column="password")
    address = models.OneToOneField(UserAddress, blank=True, null=True, on_delete=models.SET_NULL, db_column="address")
    profile = models.OneToOneField(UserProfile, blank=True, null=True, on_delete=models.SET_NULL, db_column="profile")
    is_active = models.BooleanField(default=False, db_column="is_active")
    confirmation_code = models.CharField(max_length=50, blank=True, null=True, unique=True)
    confirmation_code_expiration = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")

    REQUIRED_FIELDS = []

    class Role(models.TextChoices):    
        ADMIN = "ADMIN", "Admin"
        MODERATOR = "MODERATOR", "Moderator"
        REGULAR = "REGULAR", "Regular"

    role = models.CharField(max_length=50, choices=Role.choices, blank=True, null=True, db_column="role")

    def save(self, *args, **kwargs):
        # User is being created
        if not self.pk: 
            if self.is_superuser:
                self.is_staff = True
                self.role = self.Role.ADMIN
            else:
                self.is_staff = False
                self.role = self.Role.REGULAR
        # User is being updated
        else:  
            if self.role == self.Role.REGULAR:
                self.is_staff = False
                self.is_superuser = False
            if self.role == self.Role.MODERATOR:
                self.is_staff = True
                self.is_superuser = False
            if self.role == self.Role.ADMIN:
                self.is_staff = True
                self.is_superuser = True
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"user {self.username}" 
    