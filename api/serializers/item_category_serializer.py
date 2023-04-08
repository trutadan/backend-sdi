from rest_framework import serializers

from api.models.item_category import ItemCategory


class ItemCategorySerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not all(x.isalpha() or x.isspace() for x in data['name']):
            raise serializers.ValidationError('Category name must contain only letters and spaces!')
        
        return data
    
    class Meta:
        model = ItemCategory
        fields = ('id', 'name', 'subcategory')