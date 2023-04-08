from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.item_category import ItemCategory
from api.serializers.item_category_serializer import ItemCategorySerializer


class ItemCategoryList(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['$name', '$subcategory']


class ItemCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
