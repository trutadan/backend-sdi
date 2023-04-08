from rest_framework import generics

from django.db.models import Sum

from api.models.item import Item
from api.serializers.most_sold_items_dto import MostSoldItemsDTO

class MostSoldItemsView(generics.ListAPIView):
    serializer_class = MostSoldItemsDTO

    def get_queryset(self):
        queryset = Item.objects.annotate(total_pieces_sold=Sum('item_orders__quantity')).exclude(total_pieces_sold=None)

        # filter by total_pieces_sold equal to a certain value
        total_pieces_sold = self.request.query_params.get('total_pieces_sold', None)
        if total_pieces_sold is not None:
            queryset = queryset.filter(total_pieces_sold=total_pieces_sold)

        # filter by total_pieces_sold greater than a certain value
        total_pieces_sold__gt = self.request.query_params.get('total_pieces_sold__gt')
        if total_pieces_sold__gt:
            queryset = queryset.filter(total_pieces_sold__gt=total_pieces_sold__gt)

        # filter by total_pieces_sold greater than or equal to a certain value
        total_pieces_sold__gte = self.request.query_params.get('total_pieces_sold__gte')
        if total_pieces_sold__gte:
            queryset = queryset.filter(total_pieces_sold__gte=total_pieces_sold__gte)

        # filter by total_pieces_sold less than a certain value
        total_pieces_sold__lt = self.request.query_params.get('total_pieces_sold__lt')
        if total_pieces_sold__lt:
            queryset = queryset.filter(total_pieces_sold__lt=total_pieces_sold__lt)

        # filter by total_pieces_sold less than or equal to a certain value
        total_pieces_sold__lte = self.request.query_params.get('total_pieces_sold__lte')
        if total_pieces_sold__lte:
            queryset = queryset.filter(total_pieces_sold__lte=total_pieces_sold__lte)

        # filter by total_pieces_sold in a range of values
        total_pieces_sold__range = self.request.query_params.get('total_pieces_sold__range')
        if total_pieces_sold__range:
            start, end = total_pieces_sold__range.split(',')
            queryset = queryset.filter(total_pieces_sold__range=(start, end))

        # order by total_pieces_sold in ascending/descending order
        ordering = self.request.query_params.get('ordering')
        if ordering == 'total_pieces_sold':
            queryset = queryset.order_by('total_pieces_sold')
        elif ordering == '-total_pieces_sold':
            queryset = queryset.order_by('-total_pieces_sold')

        return queryset