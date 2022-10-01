from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.mixins import UserPassesTestMixin

from ..serializers import campus as serializers
from ... import models


class CampusAPI(UserPassesTestMixin, APIView):
    serializer_class = serializers.CampusVisitorSerializer

    def post(self, request, mode):
        serializer = serializers.CampusVisitorSerializer(data=request.data)
        if serializer.is_valid():
            visitor = models.Visitor.objects.filter(userid=serializer.data['visitor']).last()
            if visitor:
                history_last = models.NowCampus.objects.filter(visitor=visitor).last()
                if not history_last:
                    inorout = True
                elif (history_last.inorout and (mode == "Exit")) or (not history_last.inorout and (mode == "Enter")):
                    inorout = (mode == "Enter")
                elif (history_last.inorout and (mode == "Enter")) or (not history_last.inorout and (mode == "Exit")):
                    tmp = models.NowCampus(
                        visitor=visitor,
                        inorout= not history_last.inorout
                    )
                    tmp.save()
                    inorout = (mode == "Enter")
                else:
                    return Response({}, status=400)
                
                nowcampus = models.NowCampus(
                    visitor=visitor,
                    inorout=inorout
                )
                nowcampus.save()

                return Response({'nickname':visitor.nickname, 'inorout':inorout}, status=201)
        
        return Response({}, status=404)

    def test_func(self):
        return True