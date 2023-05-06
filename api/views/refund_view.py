from api.models.refund import Refund
from api.serializers.refund_serializer import RefundSerializer
from api.permissions import IsUserRefundOwner, IsAdmin, IsModeratorWithNoDeletePrivilege
from api.authentication import CustomUserAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated


class RefundList(generics.ListCreateAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (IsUserRefundOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'accepted': ['exact']}
    search_fields = ['$reason']


class RefundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (IsUserRefundOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)