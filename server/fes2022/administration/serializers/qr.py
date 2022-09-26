from rest_framework import serializers

from ..models import ReadyRoomQRdevice
from ... import models


class ReadyRoomQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyRoomQRdevice
        fields = ['ready']
        

class RoomQRSerializer(serializers.Serializer):
    visitor = serializers.UUIDField()
    placeid = serializers.IntegerField()

    class Meta:
        fields = [
            'visitor', 'placeid'
        ]