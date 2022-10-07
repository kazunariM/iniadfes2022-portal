from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response

from django.shortcuts import get_list_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils import timezone
from django.db import transaction

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

    @transaction.atomic
    def post(self, request, placeid, format=None):
        serializer = serializers.RoomQRSerializer(data=request.data)

        if serializer.is_valid():
            visitor = models.Visitor.objects.filter(userid=serializer.data['visitor']).last()
            place_data = models.PlaceID.objects.filter(placeid=placeid).last()

            if visitor and place_data:
                room = place_data.room
                history_last = models.NowRoom.objects.filter(visitor=visitor).last()

                if history_last:

                    if history_last.room == room:
                        if (timezone.now() - history_last.scanned_at).seconds < event_data.ROOMQR_INTERVAL:
                            return Response({"detail":"重複して読み取られてしまっています"}, status=400)

                        if history_last.inorout:
                            inorout = False
                            count = room.count - 1
                            unique_count = room.unique_count
                            total_count = room.total_count
                        else:
                            inorout = True
                            count = room.count + 1
                            unique_count = room.unique_count
                            total_count = room.total_count + 1
                    else:
                        history_visitor_room_last = models.NowRoom.objects.filter(visitor=visitor, room=room)

                        if history_last.inorout:
                            nowroom_tmp = models.NowRoom(
                                visitor=visitor,
                                room=history_last.room,
                                inorout=False,
                                count=history_last.room.count - 1,
                                unique_count=history_last.room.unique_count,
                                total_count=history_last.room.total_count
                            )
                            nowroom_tmp.save()

                            room_tmp = history_last.room
                            room_tmp.count = room_tmp.count - 1
                            room_tmp.save()
                        
                        inorout = True
                        count=room.count + 1
                        total_count = room.total_count + 1
                        unique_count = room.unique_count + (0 if history_visitor_room_last else 1)
                                                    
                else:
                    inorout = True
                    count = room.count + 1
                    unique_count = room.unique_count + 1
                    total_count = room.total_count + 1

                nowroom = models.NowRoom(
                    visitor=visitor,
                    room=room,
                    count=count,
                    inorout=inorout,
                    unique_count=unique_count,
                    total_count=total_count
                )
                nowroom.save()

                room.count=count
                room.unique_count=unique_count
                room.total_count=total_count
                room.save()

                return Response({'nickname':nowroom.visitor.nickname, 'inorout':nowroom.inorout}, status=201)

        return Response({}, status=404)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='ReadQRinRoom').users.all()

