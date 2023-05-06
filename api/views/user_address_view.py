from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from api.authentication import CustomUserAuthentication
from api.models.user_address import UserAddress
from api.permissions import IsAdminOrModerator, UserAddressIsOwner, IsAdmin, IsAdminOrModerator, IsModeratorWithNoDeletePrivilege
from api.serializers.user_address_serializer import UserAddressSerializer


class UserAddressList(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'country': ['exact'], 
                        'state': ['icontains']
                        }
    search_fields = ['$city']
    
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminOrModerator,)


class UserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (UserAddressIsOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)