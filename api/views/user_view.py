from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.user import User
from api.serializers.user_serializer import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'created_at': ['gte', 'lte']}
    search_fields = ['$first_name', '$last_name', '$username']
    ordering_fields = ['created_at']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer