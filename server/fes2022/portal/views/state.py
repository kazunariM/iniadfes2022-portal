from rest_framework.generics import RetrieveAPIView

from .. import models
from ..serializers import state as serializers


class State(RetrieveAPIView):
    queryset = models.Term
    serializer_class = serializers.StateSerializer

    def get_object(self):
        return self.queryset.objects.filter().order_by('pk').first()
    