from rest_framework import generics, status
from rest_framework.response import Response

from django.http import Http404

from api.models.item import Item
from api.models.order_item import OrderItem
from api.serializers.order_item_serializer import OrderItemSerializer

class ItemOrderList(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self, *args, **kwargs):
        item_pk = self.kwargs['pk']
        
        try:
            item = Item.objects.get(pk=item_pk)
            return OrderItem.objects.filter(item=item)
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


class ItemOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer

    def get_object(self, *args, **kwargs):
        item_pk = self.kwargs['pk']
        order_pk = self.kwargs['order_pk']

        try:
            item = Item.objects.get(pk=item_pk)
        except Item.DoesNotExist:
            raise Http404('Item does not exist!')
        
        try:
            order_item = OrderItem.objects.get(item=item, order=order_pk)
        except OrderItem.DoesNotExist:
            return Http404('Order does not exist!')

        return order_item