from rest_framework import generics, status
from rest_framework.response import Response

from django.http import Http404

from api.models.order import Order
from api.models.order_item import OrderItem
from api.serializers.order_item_serializer import OrderItemSerializer

class OrderItemList(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self, *args, **kwargs):
        order_pk = self.kwargs['pk']

        try:
            order = Order.objects.get(pk=order_pk)
            return OrderItem.objects.filter(order=order)
        except Order.DoesNotExist:
            return Http404('Order does not exist!')

    def post(self, request, pk, *args, **kwargs):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({'error': 'Order does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(order=order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    lookup_url_kwarg = 'item_pk'

    def get_object(self, *args, **kwargs):
        order_pk = self.kwargs['pk']
        item_pk = self.kwargs['item_pk']

        try:
            order = Order.objects.get(pk=order_pk)
        except Order.DoesNotExist:
            raise Http404('Order does not exist!')
        
        try:
            order_item = OrderItem.objects.get(order=order_pk, item=item_pk)
        except OrderItem.DoesNotExist:
            return Http404('Item does not exist!')

        return order_item