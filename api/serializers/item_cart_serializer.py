from rest_framework import serializers

from api.models.cart_item import CartItem


class ItemCartDetailsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='cart.user.username', read_only=True)

    class Meta:
        model = CartItem
        fields = ['cart', 'user', 'quantity']