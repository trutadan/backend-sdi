from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from api.authentication import CustomUserAuthentication
from api.models.coupon import Coupon
from api.serializers.coupon_serializer import CouponSerializer
from api.permissions import IsAdmin, IsAdminOrModerator, IsModeratorWithNoDeletePrivilege


class CouponList(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminOrModerator,)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'amount': ['gte', 'lte']}
    search_fields = ['$code']
    ordering_fields = ['amount']


class CouponDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (IsAdmin|IsModeratorWithNoDeletePrivilege),)
    