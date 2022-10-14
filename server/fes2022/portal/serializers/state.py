from rest_framework import serializers

from .. import models


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Term
        fields = ["non_public", "pre", "fes", "finished"]
        