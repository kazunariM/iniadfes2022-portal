from rest_framework import serializers

import datetime

from ... import models
from ... import event_data


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = [
            'nickname', 'first_name', 'last_name', 'ruby_first_name', 'ruby_last_name', 'email', 
            'address', 'age', 'gender', 'major_subject', 'job', 'know_about', 'design',
        ]
        
    def validate_nickname(self, value):
        if len(value) > 16:
            raise serializers.ValidationError('ニックネームは16字以内で入力してください')
        return value

    def validate_email(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('正しいメールアドレスを入力してください')
        return value

    def validate_age(self, value):
        if not 0 <= value <= 8:
            raise serializers.ValidationError('正しく選択してください')
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

