from api.models.item_category import ItemCategory
from api.serializers.item_category_serializer import ItemCategorySerializer
from api.permissions import IsAdmin, IsAdminOrModerator, IsModeratorWithNoDeletePrivilege
from api.authentication import CustomUserAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class ItemCategoryList(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer

    def get_authenticators(self):
        if self.request.method == 'GET':
            return ()
        else:
            return (CustomUserAuthentication(),)
        
    def get_permission(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        else:
            return (IsAuthenticated(), IsAdminOrModerator(),)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['$name', '$subcategory']


class ItemCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer

    def get_authenticators(self):
        if self.request.method == 'GET':
            return ()
        else:
            return (CustomUserAuthentication(),)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        else:
            return [IsAuthenticated(), (IsAdmin | IsModeratorWithNoDeletePrivilege)()]


class ItemCategoryAutocomplete(APIView):
    serializer_class = ItemCategorySerializer

    def get_authenticators(self):
        if self.request.method == 'GET':
            return ()
        else:
            return (CustomUserAuthentication(),)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        else:
            return [IsAuthenticated(), (IsAdmin | IsModeratorWithNoDeletePrivilege)()]

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')

        categories = ItemCategory.objects.filter(name__icontains=query).order_by('name')[:20]
        serializer = ItemCategorySerializer(categories, many=True)
        
        return Response(serializer.data)
        