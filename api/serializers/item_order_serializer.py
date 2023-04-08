from rest_framework import serializers

from api.models.order_item import OrderItem


class ItemOrderDetailsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='order.user.username', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['order', 'user', 'quantity']