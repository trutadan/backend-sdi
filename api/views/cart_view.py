from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.cart import Cart
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