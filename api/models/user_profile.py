from django.db import models


class UserProfile(models.Model):
    picture = models.ImageField(blank=True, null=True, db_column="profile_picture")
    date_of_birth = models.DateField(db_column="date_of_birth")
    phone = models.CharField(max_length=10, db_column="phone_number")
    country_code = models.CharField(default="+40", max_length=5, db_column="country_code")
    created_at = models.DateTimeField(auto_now=True, db_column="created_at")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self):
        return f"{self.country_code} {self.phone} for the date of birth {self.date_of_birth}"
  