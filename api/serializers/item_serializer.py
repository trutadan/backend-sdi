from rest_framework import serializers

from api.models.order_item import OrderItem
from api.models.item import Item

from api.serializers.item_order_serializer import ItemOrderDetailsSerializer
from api.serializers.item_cart_serializer import ItemCartDetailsSerializer


class ItemSerializer(serializers.ModelSerializer):
    orders_count = serializers.SerializerMethodField()
    refunds_requested_count = serializers.SerializerMethodField()

    def get_refunds_requested_count(self, obj):
        return OrderItem.objects.filter(item=obj, order__refund_requested=True).count()

    def get_orders_count(self, obj):
        return obj.item_orders.count()

    def validate(self, data):
        if data['price'] <= 0:
            raise serializers.ValidationError('Price must be greater than 0!')
        
        if data['discount_price'] is not None and data['discount_price'] <= 0:
            raise serializers.ValidationError('Discount price must be greater than 0!')

        if data['discount_price'] is not None and data['discount_price'] > data['price']:
            raise serializers.ValidationError("Discount price can't be greater than the regular price!")
    
        if data['available_number'] > data['total_number']:
            raise serializers.ValidationError("Available number of items can't be greater than total number!")
        
        return data

    class Meta:
        model = Item
        fields = "__all__"


class ItemDetailSerializer(serializers.ModelSerializer):
    item_orders = ItemOrderDetailsSerializer(many=True, read_only=True)
    item_carts = ItemCartDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'