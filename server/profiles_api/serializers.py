from rest_framework import serializers
from django.contrib.postgres.fields import ArrayField


class GameOfLiveSerializer(serializers.Serializer):

    board = serializers.ListField()
    width = serializers.DictField()
    height = serializers.DictField()
