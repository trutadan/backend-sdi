from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.cart import Cart
from api.models.user import User

from api.serializers.cart_serializer import CartSerializer


class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'created_at': ['gte', 'lte']}
    ordering_fields = ['created_at']


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


def get_cart_by_user_id(user_id):
    # Get the user object using the user_id
    user = get_object_or_404(User, pk=user_id)

    # Get the cart object using the user object
    cart = get_object_or_404(Cart, user=user)

    return cart