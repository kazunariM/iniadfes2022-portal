from rest_framework import serializers

from ... import models


class CampusPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NowCampus
        fields = ["count", "unique_count", "total_count"]


class RoomPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NowCampus
        fields = ["count", "unique_count", "total_count"]

