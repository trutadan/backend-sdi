from api.permissions import GetIfUserIsPaymentOwner, IsAdmin, IsModeratorWithNoDeletePrivilege
from api.models.payment import Payment
from api.serializers.payment_serializer import PaymentSerializer
from api.authentication import CustomUserAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (GetIfUserIsPaymentOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'amount': ['gte', 'lte'], 
                        'timestamp': ['gte', 'lte']
                        }
    ordering_fields = ['amount', 'timestamp']


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated, (GetIfUserIsPaymentOwner|IsAdmin|IsModeratorWithNoDeletePrivilege),)