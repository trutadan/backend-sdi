from api.models.item import Item
from api.serializers.item_serializer import ItemSerializer
from api.serializers.item_serializer import ItemDetailSerializer
from api.permissions import IsAdmin, IsAdminOrModerator, IsModeratorWithNoDeletePrivilege, IsGetRequest
from api.authentication import CustomUserAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny



class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

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
    filterset_fields = {'price': ['gte', 'lte'], 
                        'category': ['exact']
                        }
    search_fields = ['$title', '$description']
    ordering_fields = ['price', 'discount_price']


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer

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
