from rest_framework import serializers

from ... import models


class CampusVisitorSerializer(serializers.Serializer):
    visitor = serializers.UUIDField()

    class Meta:
        fields = [
            'visitor'
        ]