from rest_framework.generics import RetrieveAPIView, ListAPIView

from django.shortcuts import get_object_or_404

from ..serializers import stamprally as serializers
from ... import models


class StamprallyList(ListAPIView):
    serializer_class = serializers.StamprallySerializer
    queryset = models.StampCourse.objects.all()


class StampSheetAPI(RetrieveAPIView):
    serializer_class = serializers.StampSheetSerializer
    queryset = models.StampCourse
    lookup_field = "stampcourse"
    
    def get_object(self):
        return self.queryset.objects.filter(uuid=self.kwargs[self.lookup_field]).first()


class AllStampAPI(ListAPIView):
    serializer_class = serializers.NoImgStampSerializer
    queryset = models.Stamp
    lookup_field = "stampcourse"
    
    def get_queryset(self):
        return models.Stamp.objects.filter(stampcourse=self.kwargs[self.lookup_field]).order_by("serial")


class StampHistroyAPI(RetrieveAPIView):
    serializer_class = serializers.GotStampSerializer
    queryset = models.StampHistory
    lookup_fields = ["userid", "stampcourse"]
    
    def get_object(self):
        stamphistory = self.queryset.objects.filter(
            visitor__userid=self.kwargs[self.lookup_fields[0]], 
            stampcourse__uuid=self.kwargs[self.lookup_fields[1]],
        ).last()
        
        if not stamphistory:
            
            visitor = get_object_or_404(
                models.Visitor,
                userid=self.kwargs[self.lookup_fields[0]],
            )
            
            stampcourse = get_object_or_404(
                models.StampCourse,
                uuid=self.kwargs[self.lookup_fields[1]],
            )
            
            stamphistory = models.StampHistory(
                visitor=visitor,
                stampcourse=stampcourse,
            )
            stamphistory.save()
            
        return stamphistory
    