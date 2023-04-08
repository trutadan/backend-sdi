from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.refund import Refund
from api.serializers.refund_serializer import RefundSerializer


class RefundList(generics.ListCreateAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'accepted': ['exact']}
    search_fields = ['$reason']


class RefundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer