from api.models.order import Order
from api.serializers.order_serializer import OrderSerializer
from api.serializers.order_serializer import OrderDetailSerializer
from api.permissions import GetIfUserIsOrderOwner, IsAdmin, IsModeratorWithNoDeletePrivilege
from api.authentication import CustomUserAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # authentication_classes = (CustomUserAuthentication,)
    # permission_classes = (IsAuthenticated, (GetIfUserIsOrderOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'order_placed_date': ['gte', 'lte'], 
                        'received_date': ['gte', 'lte'],
                        'being_delivered': ['exact'],
                        'received': ['exact'],
                        'refund_requested': ['exact'],
                        'refund_granted': ['exact']
                        }
    ordering_fields = ['start_date', 'ordered_date']


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (GetIfUserIsOrderOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)