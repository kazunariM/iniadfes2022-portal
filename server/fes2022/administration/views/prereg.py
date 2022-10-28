from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from django.contrib.auth.mixins import UserPassesTestMixin

from ... import models
from ..models import PagesPermission
from ..serializers import prereg as serializers


class AllocationQRIDAPI(UserPassesTestMixin, APIView):
    def get(self, request):
        pre_visitors = models.Visitor.objects.filter(is_preregistration=True, id_data=None)
        namecards = models.NamecardDesign.objects.all()
        
        count = 0
        
        for namecard in namecards:
            visitors = pre_visitors.filter(design=namecard).order_by("pk")
            if visitors:
                namecardids = models.NamecardPool.objects.filter(namecard=namecard, used=False).order_by("pk")[:len(visitors)]
                for visitor, namecardid in zip(visitors, namecardids):
                    visitor.userid = namecardid.qrid
                    visitor.identifying = namecardid.pk
                    visitor.id_data = namecardid
                    visitor.save()
                    
                    namecardid.used = True
                    namecardid.save()
                    
                    count += 1
    
        return Response({"cards": count}, status=200)
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='AllocationQRID').users.all()


class PreRegListAPI(UserPassesTestMixin, ListAPIView):
    serializer_class = serializers.PreRegSerializer
    queryset = models.Visitor
    
    def get_queryset(self):
        return models.Visitor.objects.filter(is_preregistration=True, is_printed=False, id_data__isnull=False).order_by('design')[:50]

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='AllocationQRID').users.all()


class PrintedQRAPI(UserPassesTestMixin, RetrieveUpdateAPIView):
    serializer_class = serializers.PrintedQRSerializer
    queryset = models.Visitor
    lookup_field = 'userid'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='AllocationQRID').users.all()
