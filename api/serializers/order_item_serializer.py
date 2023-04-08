from rest_framework import serializers

from api.models.order_item import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemDetailsSerializer(serializers.ModelSerializer):
    item_title = serializers.CharField(source='item.title', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['item', 'item_title', 'quantity']