from rest_framework import serializers

import datetime

from ... import models
from ... import event_data


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
        if value.numofremaining <= 0 or datetime.date.today() > event_data.PREREGISTRATION:
            raise serializers.ValidationError('カードの選択に誤りがあります')
        return value

    def create(self, validated_data):
        return models.Visitor.objects.create(
            **validated_data,
            is_preregistration=(datetime.date.today() < event_data.PREREGISTRATION),
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

