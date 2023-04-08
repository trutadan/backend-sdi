from rest_framework import serializers

from api.models.order import Order

from api.serializers.order_item_serializer import OrderItemDetailsSerializer


class OrderSerializer(serializers.ModelSerializer):
    items_count = serializers.SerializerMethodField()

    def get_items_count(self, obj):
        return obj.order_items.count()

    def validate(self, data):
        if data['being_delivered'] == data['received']:
            raise serializers.ValidationError('The order is either being delivered or already received!')
        
        if data['received'] is False and data['refund_requested'] is True:
            raise serializers.ValidationError('The order must be delivered before a refund to be requested!')

        if data['received'] is False and data['refund_granted'] is True:
            raise serializers.ValidationError('The order must be delivered before a refund to be granted!')
        
        if data['refund_requested'] is False and data['refund_granted'] is True:
             raise serializers.ValidationError('The refund must be requested before being granted!')

        return data

    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'