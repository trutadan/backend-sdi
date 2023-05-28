from api.models.cart import Cart
from api.serializers.cart_serializer import CartSerializer
from api.authentication import CustomUserAuthentication
from api.permissions import GetIfUserIsCartOwner, IsAdmin, IsModeratorWithNoDeletePrivilege

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (IsAdmin|IsModeratorWithNoDeletePrivilege),)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'created_at': ['gte', 'lte']}
    ordering_fields = ['created_at']


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (GetIfUserIsCartOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)


@api_view(['GET'])
@authentication_classes([CustomUserAuthentication])
@permission_classes([IsAuthenticated, GetIfUserIsCartOwner|IsAdmin|IsModeratorWithNoDeletePrivilege])
def get_cart_by_user(request):
    # Get the user object using the authenticated user from the request
    user = request.user

    # Get the cart object using the user object
    cart = get_object_or_404(Cart, user=user)

    return cart
