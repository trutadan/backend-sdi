from rest_framework import serializers

from api.models.user_address import UserAddress
from api.models.user import User


class UserAddressSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not data['zip_code'].isdigit():
            raise serializers.ValidationError('Zip code must contain only digits!')
        
        return data

    class Meta:
        model = UserAddress
        fields = "__all__"
