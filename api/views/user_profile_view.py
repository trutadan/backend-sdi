from api.authentication import CustomUserAuthentication
from api.models.user_profile import UserProfile
from api.permissions import IsAdmin, IsAdminOrModerator, IsModeratorWithNoDeletePrivilege, IsUserProfileOwner
from api.serializers.user_profile_serializer import UserProfileSerializer

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, filters


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'country_code': ['exact']}
    ordering_fields = ['date_of_birth', 'created_at', 'updated_at']
    search_fields = ['$phone']

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminOrModerator,)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (IsUserProfileOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)
    