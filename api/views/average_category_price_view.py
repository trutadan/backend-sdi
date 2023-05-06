from api.models.item_category import ItemCategory
from api.serializers.average_category_price_dto import AverageCategoryPriceDTO

from django.db.models import Avg

from rest_framework import generics
from rest_framework.permissions import AllowAny


class AverageCategoryPriceView(generics.ListAPIView):
    serializer_class = AverageCategoryPriceDTO

    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = ItemCategory.objects.annotate(
            average_price=Avg('item__price')
        ).exclude(average_price=None)

        # filter by average_price equal to a certain value
        average_price = self.request.query_params.get('average_price', None)
        if average_price is not None:
            queryset = queryset.filter(average_price=average_price)

        # filter by average_price greater than a certain value
        average_price__gt = self.request.query_params.get('average_price__gt')
        if average_price__gt:
            queryset = queryset.filter(average_price__gt=average_price__gt)

        # filter by average_price greater than or equal to a certain value
        average_price__gte = self.request.query_params.get('average_price__gte')
        if average_price__gte:
            queryset = queryset.filter(average_price__gte=average_price__gte)

        # filter by average_price less than a certain value
        average_price__lt = self.request.query_params.get('average_price__lt')
        if average_price__lt:
            queryset = queryset.filter(average_price__lt=average_price__lt)

        # filter by average_price less than or equal to a certain value
        average_price__lte = self.request.query_params.get('average_price__lte')
        if average_price__lte:
            queryset = queryset.filter(average_price__lte=average_price__lte)

        # filter by average_price in a range of values
        average_price__range = self.request.query_params.get('average_price__range')
        if average_price__range:
            start, end = average_price__range.split(',')
            queryset = queryset.filter(average_price__range=(start, end))

        # order by average_price in ascending/descending order
        ordering = self.request.query_params.get('ordering')
        if ordering == 'average_price':
            queryset = queryset.order_by('average_price')
        elif ordering == '-average_price':
            queryset = queryset.order_by('-average_price')

        return queryset.values('id', 'name', 'average_price')