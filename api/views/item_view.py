from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.item import Item
from api.serializers.item_serializer import ItemSerializer
from api.serializers.item_serializer import ItemDetailSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'price': ['gte', 'lte'], 
                        'category': ['exact']
                        }
    search_fields = ['$title', '$description']
    ordering_fields = ['price', 'discount_price']


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer