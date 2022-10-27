from rest_framework import serializers

from ... import models


class StamprallySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StampCourse
        fields = [
            'uuid', 'title'
        ]


class StampSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StampCourse
        fields = [
            'title', 'background'
        ]


class NoImgStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stamp
        fields = [
            'room', 'serial'
        ]
        

class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stamp
        fields = [
            'img', 'room', 'serial'
        ]


class GotStampSerializer(serializers.ModelSerializer):
    got_stamp = StampSerializer(many=True)
    
    class Meta:
        model = models.StampHistory
        fields = [
            'got_stamp'
        ]
        