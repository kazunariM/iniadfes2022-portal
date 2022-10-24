from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils import timezone

from ..serializers import campus as serializers
from ... import models
from ..models import PagesPermission
from ... import event_data


class EnterCampusAPI(UserPassesTestMixin, APIView):
    serializer_class = serializers.CampusVisitorSerializer
    
    def post(self, request):
        serializer = serializers.CampusVisitorSerializer(data=request.data)

        if serializer.is_valid():
            visitor = models.Visitor.objects.filter(userid=serializer.data['visitor']).last()
            
            if not visitor:
                return Response({"detail": "来場者のデータが見つかりません", "err": 0}, status=404)
            
            visitor_histroy = models.NowCampus.objects.filter(visitor=visitor, scanned_at__date=timezone.localdate(timezone.now()))

            
            if not visitor_histroy:
                unique_count = +1
            elif visitor_histroy:
                if (timezone.now() - visitor_histroy.last().scanned_at).seconds < event_data.CAMPUSQR_INTERVAL:
                    return Response({"detail": "重複して読み取られてしまっています", "err": 1}, status=400)
                
                unique_count = 0
                
                if visitor_histroy.last().inorout:
                    nowcampus_data = models.NowCampus(
                        visitor=visitor,
                        inorout=False,
                        count=-1,
                        unique_count=0,
                        total_count=0
                    )
                    nowcampus_data.save()
            
            nowcampus = models.NowCampus(
                visitor=visitor,
                inorout=True,
                count=+1,
                unique_count=unique_count,
                total_count=+1
            )
            nowcampus.save()
            
            return Response({'nickname':nowcampus.visitor.nickname, 'inorout':nowcampus.inorout}, status=201)

        return Response({}, status=400)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='EnterCampusQR').users.all()


class ExitCampusAPI(UserPassesTestMixin, APIView):
    serializer_class = serializers.CampusVisitorSerializer
    
    def post(self, request):
        serializer = serializers.CampusVisitorSerializer(data=request.data)
        
        if serializer.is_valid():
            visitor = models.Visitor.objects.filter(userid=serializer.data['visitor']).last()
            
            if not visitor:
                return Response({"detail": "来場者のデータが見つかりません", "err": 0}, status=404)
            
            visitor_histroy = models.NowCampus.objects.filter(visitor=visitor, scanned_at__date=timezone.localdate(timezone.now()))

            
            if not visitor_histroy:
                nowcampus_data = models.NowCampus(
                    visitor=visitor,
                    inorout=True,
                    count=+1,
                    unique_count=+1,
                    total_count=+1
                )
                nowcampus_data.save()
                
            elif visitor_histroy:
                if (timezone.now() - visitor_histroy.last().scanned_at).seconds < event_data.CAMPUSQR_INTERVAL:
                    return Response({"detail": "重複して読み取られてしまっています", "err": 1}, status=400)
                
                if not visitor_histroy.last().inorout:
                    nowcampus_data2 = models.NowCampus(
                        visitor=visitor,
                        inorout=True,
                        count=+1,
                        unique_count=0,
                        total_count=+1
                    )
                    nowcampus_data2.save()
            
            nowcampus = models.NowCampus(
                visitor=visitor,
                inorout=False,
                count=-1,
                unique_count=0,
                total_count=0
            )
            nowcampus.save()
            
            return Response({'nickname':nowcampus.visitor.nickname, 'inorout':nowcampus.inorout}, status=201)
            
        return Response({}, status=400)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='ExitCampusQR').users.all()
