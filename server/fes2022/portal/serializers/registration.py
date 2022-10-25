from rest_framework import serializers

import datetime

from ... import models
from ... import event_data
from ..models import Term


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = [
            'nickname', 'email', 
            'address', 'age', 'gender', 'major_subject', 'job', 'know_about', 'design',
        ]
        
    def validate_nickname(self, value):
        if len(value) > 17:
            raise serializers.ValidationError('ニックネームは16字以内で入力してください')
        return value

    def validate_email(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('正しいメールアドレスを入力してください')
        return value

    def validate_design(self, value):
        if value.numofremaining <= 0:
            raise serializers.ValidationError('カードの選択に誤りがあります')
        if value.is_only_advance and (not Term.objects.all().order_by("pk").first().pre):
            raise serializers.ValidationError('カードの選択に誤りがあります')
        return value

    def create(self, validated_data):
        return models.Visitor.objects.create(
            **validated_data,
            is_preregistration=(Term.objects.all().order_by("pk").first().pre),
        )


class NamecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NamecardDesign
        fields = [
            'uuid', 'name', 'img', 'text',
        ]


class CompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = [
            'nickname', 'management_uuid'
        ]

