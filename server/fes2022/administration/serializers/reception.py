from rest_framework import serializers

from ... import models


class NamecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NamecardDesign
        fields = ["img"]


class ConfirmVisitorSerializer(serializers.ModelSerializer):
    design = NamecardSerializer()

    class Meta:
        model = models.Visitor
        fields = ["nickname", "design"]


class SelectNamecardSerializer(serializers.Serializer):
    management_uuid = serializers.UUIDField()
    userid = serializers.UUIDField()


class HandedoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = ["is_handedover"]