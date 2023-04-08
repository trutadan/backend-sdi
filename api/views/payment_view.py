from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.models.payment import Payment
from api.serializers.payment_serializer import PaymentSerializer


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'amount': ['gte', 'lte'], 
                        'timestamp': ['gte', 'lte']
                        }
    ordering_fields = ['amount', 'timestamp']


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer