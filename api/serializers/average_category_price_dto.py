from rest_framework import serializers


class AverageCategoryPriceDTO(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    average_price = serializers.IntegerField()