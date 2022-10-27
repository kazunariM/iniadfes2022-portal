from rest_framework import serializers

from ... import models


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NamecardDesign
        fields = [
            'name'
        ]


class PreRegSerializer(serializers.ModelSerializer):
    design = DesignSerializer()
    
    class Meta:
        model = models.Visitor
        fields = [
            'design', 'nickname', 'identifying', 'userid'
        ]
        
        
class PrintedQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = [
            'is_printed'
        ]