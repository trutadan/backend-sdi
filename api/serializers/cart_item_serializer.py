from rest_framework import serializers

from api.models.cart_item import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartItemDetailsSerializer(serializers.ModelSerializer):
    item_title = serializers.CharField(source='item.title', read_only=True)

    class Meta:
        model = CartItem
        fields = ['item', 'item_title', 'quantity']