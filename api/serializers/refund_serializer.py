from rest_framework import serializers

from api.models.refund import Refund


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = "__all__"