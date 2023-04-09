from django.db import models


class ItemCategory(models.Model):
    name = models.CharField(max_length=30, db_index=True, db_column="name")
    subcategory = models.CharField(max_length=30, blank=True, null=True, db_column="subcategory")

    def __str__(self):
        return f"category {self.name} and subcategory {self.subcategory}"
    
    class Meta:
        unique_together = ('name', 'subcategory',)