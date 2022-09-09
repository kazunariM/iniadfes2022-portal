from rest_framework.generics import CreateAPIView

from . import serializers

# Create your views here.


class PreRegistrationView(CreateAPIView):
    serializer_class = serializers.PreRegistrationSerializer