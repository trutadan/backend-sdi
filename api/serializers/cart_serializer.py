from rest_framework import serializers

from api.models.cart import Cart
from api.serializers.cart_item_serializer import CartItemDetailsSerializer


class CartSerializer(serializers.ModelSerializer):
    items_count = serializers.SerializerMethodField()

    def get_items_count(self, obj):
        return obj.cart_items.count()
    
    class Meta:
        model = Cart
        fields = "__all__"


class CartDetailSerializer(serializers.ModelSerializer):
    cart_items = CartItemDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'