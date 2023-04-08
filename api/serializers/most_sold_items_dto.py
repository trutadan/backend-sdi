from rest_framework import serializers


class MostSoldItemsDTO(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    total_pieces_sold = serializers.IntegerField()