from rest_framework import serializers

from ... import models


class PortalTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = ["nickname", ]