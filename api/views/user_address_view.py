from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from api.models.user_address import UserAddress
from api.serializers.user_address_serializer import UserAddressSerializer

class UserAddressList(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'country': ['exact'], 
                        'state': ['icontains']
                        }
    search_fields = ['$city']


class UserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer