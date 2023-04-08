from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.coupon import Coupon
from api.serializers.coupon_serializer import CouponSerializer


class CouponList(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'amount': ['gte', 'lte']}
    search_fields = ['$code']
    ordering_fields = ['amount']


class CouponDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer