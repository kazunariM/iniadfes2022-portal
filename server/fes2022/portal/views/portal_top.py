from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from ... import models
from ..serializers import portal_top as serializers


class OpenAPI(APIView):
    def get(self, request, qrid):
        visitor = get_object_or_404(
            models.Visitor,
            userid=qrid
        )
        return Response({'qrid': visitor.userid, 'nickname': visitor.nickname})


class PortalTopAPI(RetrieveAPIView):
    queryset = models.Visitor
    lookup_field = 'userid'
    serializer_class = serializers.PortalTopSerializer
    