import os
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.mixins import UserPassesTestMixin

from ... import models
from ..models import PagesPermission
from ..serializers import reception as serializers


class ConfirmVisitorAPI(UserPassesTestMixin, RetrieveAPIView):
    serializer_class = serializers.ConfirmVisitorSerializer
    lookup_field = 'management_uuid'
    queryset = models.Visitor

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='HandoverNamecard').users.all()


class SelectNamecardAPI(UserPassesTestMixin, APIView):
    serializer_class = serializers.SelectNamecardSerializer

    def post(self, request):
        visitor = models.Visitor.objects.filter(management_uuid=request.data["management_uuid"]).first()
        namecardpool = models.NamecardPool.objects.filter(qrid=request.data["userid"], used=False).first()
        namecardpool2 = models.NamecardPool.objects.filter(qrid=request.data["userid"], used=True).first()
        if visitor and namecardpool:
            visitor.userid = namecardpool.qrid
            visitor.identifying = namecardpool.pk
            visitor.id_data = namecardpool
            visitor.save()

            namecardpool.used = True
            namecardpool.save()
            
            return Response({"nickname" : visitor.nickname, "identifying" : visitor.identifying})
        
        elif namecardpool2 and visitor:
            os.environ.get("DJANGO_BACKEND_URL")
            return Response({"nickname" : visitor.nickname, "identifying" : visitor.identifying, "img": os.environ.get("DJANGO_BACKEND_URL")+visitor.design.img.url, "pre": True})
        
        return Response({}, status=400)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='HandoverNamecard').users.all()


class HandedoverAPI(UserPassesTestMixin, UpdateAPIView):
    serializer_class = serializers.HandedoverSerializer
    lookup_field = 'management_uuid'
    queryset = models.Visitor

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='HandoverNamecard').users.all()

