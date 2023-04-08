from rest_framework import serializers

from api.models.order_address import OrderAddress


class OrderAddressSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not data['zip_code'].isdigit():
            raise serializers.ValidationError('Zip code must contain only digits!')
        
        return data

    class Meta:
        model = OrderAddress
        fields = "__all__"