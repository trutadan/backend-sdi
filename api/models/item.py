from django.db import models

from api.models.item_category import ItemCategory


class Item(models.Model):
    title = models.CharField(max_length=100, db_column="title")
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, db_column="category")
    price = models.FloatField(db_column="price")
    discount_price = models.FloatField(blank=True, null=True, db_column="discount_price")
    available_number = models.PositiveIntegerField(db_column="available_number")
    total_number = models.PositiveIntegerField(db_column="total_number")
    description = models.TextField(db_column="description")
    picture = models.ImageField(blank=True, null=True, db_column="picture")

    def __str__(self):
        return f"{self.title} from {self.category} with the price {self.price} and discount price {self.discount_price}"
 