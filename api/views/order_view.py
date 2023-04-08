from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.order import Order
from api.serializers.order_serializer import OrderSerializer
from api.serializers.order_serializer import OrderDetailSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'start_date': ['gte', 'lte'], 
                        'ordered_date': ['gte', 'lte'],
                        'being_delivered': ['exact'],
                        'received': ['exact'],
                        'refund_requested': ['exact'],
                        'refund_granted': ['exact']
                        }
    ordering_fields = ['start_date', 'ordered_date']


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer