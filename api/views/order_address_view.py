from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.order_address import OrderAddress
from api.serializers.order_address_serializer import OrderAddressSerializer


class OrderAddressList(generics.ListCreateAPIView):
    queryset = OrderAddress.objects.all()
    serializer_class = OrderAddressSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'country': ['exact'], 
                        'state': ['icontains']
                        }
    search_fields = ['$zip_code']


class OrderAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderAddress.objects.all()
    serializer_class = OrderAddressSerializer