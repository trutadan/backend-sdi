from api.authentication import CustomUserAuthentication
from api.models.user_address import UserAddress
from api.permissions import IsAdminOrModerator, IsUserAddressOwner, IsAdmin, IsAdminOrModerator, IsModeratorWithNoDeletePrivilege
from api.serializers.user_address_serializer import UserAddressSerializer

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated


class UserAddressList(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminOrModerator,)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'country': ['exact'], 
                        'state': ['icontains']
                        }
    search_fields = ['$city']
    

class UserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (IsUserAddressOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)