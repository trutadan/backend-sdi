from api.authentication import CustomUserAuthentication
from api.models.item import Item
from api.models.cart_item import CartItem
from api.serializers.cart_item_serializer import CartItemSerializer
from api.serializers.order_item_serializer import OrderItemSerializer
from api.permissions import IsAdmin, IsAdminOrModerator, IsModeratorWithNoDeletePrivilege

from django.http import Http404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ItemCartList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminOrModerator,)

    def get_queryset(self, *args, **kwargs):
        item_pk = self.kwargs['pk']
        
        try:
            item = Item.objects.get(pk=item_pk)
            return CartItem.objects.filter(item=item)
        except Item.DoesNotExist:
            raise Http404('Item does not exist!')

    def post(self, request, pk, *args, **kwargs):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Response({'error': 'Item does not exist!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(item=item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemCartDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (IsAdmin|IsModeratorWithNoDeletePrivilege),)

    def get_object(self, *args, **kwargs):
        item_pk = self.kwargs['pk']
        cart_pk = self.kwargs['cart_pk']

        try:
            item = Item.objects.get(pk=item_pk)
        except Item.DoesNotExist:
            raise Http404('Item does not exist!')
        
        try:
            cart_item = CartItem.objects.get(item=item, cart=cart_pk)
        except CartItem.DoesNotExist:
            return Http404('Cart does not exist!')

        return cart_item