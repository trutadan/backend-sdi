from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import Http404

from api.models.cart import Cart
from api.models.item import Item
from api.models.cart_item import CartItem
from api.serializers.cart_item_serializer import CartItemSerializer
from api.serializers.cart_serializer import CartSerializer


class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self, *args, **kwargs):
        cart_pk = self.kwargs['pk']

        try:
            cart = Cart.objects.get(pk=cart_pk)
            return CartItem.objects.filter(cart=cart)
        except Cart.DoesNotExist:
            return Http404('Cart does not exist!')

    def post(self, request, pk, *args, **kwargs):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    lookup_url_kwarg = 'item_pk'

    def get_object(self, *args, **kwargs):
        cart_pk = self.kwargs['pk']
        item_pk = self.kwargs['item_pk']

        try:
            cart = Cart.objects.get(pk=cart_pk)
        except Cart.DoesNotExist:
            raise Http404('Cart does not exist!')
        
        try:
            cart_item = CartItem.objects.get(cart=cart, item=item_pk)
        except CartItem.DoesNotExist:
            return Http404('Item does not exist!')

        return cart_item
    

class AddMultipleItemsToCartView(APIView):
    def post(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        items = request.data.get('items', [])

        for item_data in items:
            item_id = item_data.get('id')
            quantity = item_data.get('quantity', 1)
            item = Item.objects.get(pk=item_id)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity

            cart_item.save()
        
        serializer = CartSerializer(cart)
        
        return Response(serializer.data)