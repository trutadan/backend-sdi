from rest_framework import serializers

from api.models.coupon import Coupon


class CouponSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not data['code'].isalnum():
            raise serializers.ValidationError('Coupon code must contain only letters and numbers!')

        if data['amount'] <= 0:
            raise serializers.ValidationError('Coupon amount must be greater than 0!')
        
        return data
    
    class Meta:
        model = Coupon
        fields = "__all__"