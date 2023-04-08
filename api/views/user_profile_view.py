from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.user_profile import UserProfile
from api.serializers.user_profile_serializer import UserProfileSerializer


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'country_code': ['exact']}
    ordering_fields = ['date_of_birth', 'created_at', 'updated_at']
    search_fields = ['$phone']


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer