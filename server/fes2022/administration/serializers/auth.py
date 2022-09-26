from rest_framework import serializers

from ..models import PagesPermission


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagesPermission
        fields = ['func', 'page']

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, style={'input_type': 'password'})

    class Meta:
        fields = ["username", "password"]