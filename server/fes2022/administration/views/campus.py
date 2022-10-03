from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils import timezone

from ..serializers import campus as serializers
from ... import models
from ..models import PagesPermission
from ... import event_data


class CampusAPI(UserPassesTestMixin, APIView):
    serializer_class = serializers.CampusVisitorSerializer

    def post(self, request, mode):
        serializer = serializers.CampusVisitorSerializer(data=request.data)

        if serializer.is_valid():
            visitor = models.Visitor.objects.filter(userid=serializer.data['visitor']).last()

            if visitor:
                history_visitor_last = models.NowCampus.objects.filter(visitor=visitor).last()
                history_last = models.NowCampus.objects.all().order_by("pk").last()

                history_last_count = history_last.count if history_last else 0
                history_last_unique_count = history_last.unique_count if history_last else 0
                history_last_total_count = history_last.total_count if history_last else 0

                if not history_visitor_last:
                    inorout = True
                    count = history_last_count + 1
                    unique_count = history_last_unique_count + 1
                    total_count = history_last_total_count + 1

                elif (history_visitor_last.inorout and (mode == "Exit")) or (not history_visitor_last.inorout and (mode == "Enter")):
                    inorout = (mode == "Enter")
                    count = history_last_count + (1 if inorout else -1)
                    unique_count = history_last_unique_count
                    total_count = history_last_total_count + (1 if inorout else 0)

                elif (history_visitor_last.inorout and (mode == "Enter")) or (not history_visitor_last.inorout and (mode == "Exit")):
                    if (timezone.now() - history_visitor_last.scanned_at).seconds < event_data.CAMPUSQR_INTERVAL:
                        return Response({"detail":"重複して読み取られてしまっています"}, status=400)

                    count_tmp = history_last_count + (1 if not history_visitor_last.inorout else -1)
                    total_count_tmp = history_last_total_count + (1 if not history_visitor_last.inorout else 0)

                    tmp = models.NowCampus(
                        visitor=visitor,
                        inorout= not history_visitor_last.inorout,
                        count=count_tmp,
                        unique_count=history_last_unique_count,
                        total_count=total_count_tmp
                    )
                    tmp.save()
                    inorout = (mode == "Enter")
                    count = count_tmp + (1 if inorout else -1)
                    unique_count = history_last_unique_count
                    total_count = total_count_tmp + (1 if inorout else 0)

                else:
                    return Response({"detail":"URLが不正です"}, status=400)
                
                nowcampus = models.NowCampus(
                    visitor=visitor,
                    inorout=inorout,
                    count=count,
                    unique_count=unique_count,
                    total_count=total_count
                )
                nowcampus.save()

                return Response({'nickname':visitor.nickname, 'inorout':inorout}, status=201)
        
        return Response({"detail":"IDが見つかりませんでした"}, status=404)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='EnterCampusQR').users.all() or self.request.user in PagesPermission.objects.get(page='ExitCampusQR').users.all()