from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response

from django.shortcuts import get_list_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils import timezone

from ..serializers import qr as serializers
from ..models import PagesPermission, ReadyRoomQRdevice
from ... import models
from ... import event_data


class ExistPlaceid(UserPassesTestMixin, RetrieveAPIView):
    serializer_class = serializers.PlaceidSerializer
    queryset = models.PlaceID
    lookup_field = 'placeid'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='ReadQRinRoom').users.all()


class ReadyRoomQRAPI(UserPassesTestMixin, RetrieveUpdateAPIView):
    queryset = ReadyRoomQRdevice
    serializer_class = serializers.ReadyRoomQRSerializer
    lookup_field = 'placeid'

    def get_object(self):
        query = get_list_or_404(
            self.queryset,
            placeid__placeid=self.kwargs[self.lookup_field],
            readyroomqr__ready=False,
        )
        return query[-1]

    def perform_update(self, serializer):
        serializer.save(ts=timezone.now() if serializer.validated_data['ready'] else None)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='ReadQRinRoom').users.all()


class RoomQRAPI(UserPassesTestMixin, APIView):
    serializer_class = serializers.RoomQRSerializer

    def post(self, request, format=None):
        serializer = serializers.RoomQRSerializer(data=request.data)

        if serializer.is_valid():
            
            visitor = models.Visitor.objects.filter(userid=serializer.data['visitor']).last()
            place = models.PlaceID.objects.filter(placeid=serializer.data['placeid']).last()

            if not (visitor and place):
                return Response({"detail": "来場者または部屋のデータが見つかりません", "err": 0}, status=404)
            
            room = place.room
            visitor_histroy = models.NowRoom.objects.filter(visitor=visitor, scanned_at__date=timezone.localdate(timezone.now()))
            
            if visitor_histroy:
                if (timezone.now() - visitor_histroy.last().scanned_at).seconds < event_data.ROOMQR_INTERVAL:
                    return Response({"detail": "重複して読み取られてしまっています", "err": 1}, status=400)

            if not visitor_histroy:
                inorout = True
                count = +1
                unique = +1
                total = +1
            
            elif (visitor_histroy.last().room == room):
                unique = 0
                
                if visitor_histroy.last().inorout:
                    inorout = False
                    count = -1
                    total = 0
                    
                else:
                    inorout = True
                    count = +1
                    total = +1
            
            elif (visitor_histroy.last().room != room):
                inorout = True
                count = +1
                total = +1
                
                if room.uuid in visitor_histroy.values_list('room', flat=True):
                    unique = 0
                else:
                    unique = +1
                
                if visitor_histroy.last().inorout: # 他部屋入室したまま
                    if visitor_histroy.last().room.collaboration == room:
                        nowroom_data1 = models.NowRoom(
                            visitor=visitor,
                            room=visitor_histroy.last().room,
                            inorout=False,
                            count=-1,
                            unique_count=0,
                            total_count=0,
                        )
                        nowroom_data1.save()
                
                        nowroom_data2 = models.NowRoom(
                            visitor=visitor,
                            room=room,
                            inorout=True,
                            count=+1,
                            unique_count=unique,
                            total_count=+1,
                        )
                        nowroom_data2.save()
                
                        nowroom_data3 = models.NowRoom(
                            visitor=visitor,
                            room=room,
                            inorout=False,
                            count=-1,
                            unique_count=0,
                            total_count=0,
                        )
                        nowroom_data3.save()
                        
                        return Response({'nickname':nowroom_data3.visitor.nickname, 'inorout':nowroom_data3.inorout}, status=201)
                
                    nowroom_data0 = models.NowRoom(
                        visitor=visitor,
                        room=visitor_histroy.last().room,
                        inorout=False,
                        count=-1,
                        unique_count=0,
                        total_count=0,
                    )
                    nowroom_data0.save()
                 
            
            else:
                print(f"入退室記録で不正 {serializer.data['visitor']} {serializer.data['visitor']} {timezone.now()}")
                return Response({"detail": "何かがおかしいです", "err": 2}, status=400)
            
            nowroom = models.NowRoom(
                visitor=visitor,
                room=room,
                inorout=inorout,
                count=count,
                unique_count=unique,
                total_count=total,
            )
            nowroom.save()
            
            return Response({'nickname':nowroom.visitor.nickname, 'inorout':nowroom.inorout}, status=201)

        return Response({}, status=400)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='ReadQRinRoom').users.all()


class RoomPeopleAPI(UserPassesTestMixin, RetrieveAPIView):
    serializer_class = serializers.RoomPeopleSerializer
    queryset = models.Room
    lookup_field = 'placeid'
    
    def get_object(self):
        return models.PlaceID.objects.get(placeid=self.kwargs[self.lookup_field]).room

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='ReadQRinRoom').users.all()
