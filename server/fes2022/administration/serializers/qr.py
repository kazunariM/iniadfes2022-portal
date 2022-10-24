from rest_framework import serializers

from ..models import ReadyRoomQRdevice
from ... import models


class RoomGroupnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['groupname', 'campus', 'floor']


class PlaceidSerializer(serializers.ModelSerializer):
    room = RoomGroupnameSerializer()
    
    class Meta:
        model = models.PlaceID
        fields = ['placeid', 'room']


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
        
        
class RoomPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = [
            'count', 'pop'
        ]
        