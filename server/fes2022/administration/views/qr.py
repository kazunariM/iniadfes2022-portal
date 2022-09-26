from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from django.shortcuts import get_list_or_404
from django.utils import timezone

from ..serializers import qr as serializers
from ..models import ReadyRoomQRdevice
from ... import models


class ReadyRoomQRAPI(RetrieveUpdateAPIView):
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


class RoomQRAPI(APIView):
    serializer_class = serializers.RoomQRSerializer

    def post(self, request, format=None):
        serializer = serializers.RoomQRSerializer(data=request.data)
        if serializer.is_valid():
            visitor = models.Visitor.objects.get(userid=serializer.data['visitor'])
            history_last = models.NowRoom.objects.filter(visitor=visitor).last()
            inorout = (not history_last.inorout) if history_last else True

            nowroom = models.NowRoom(
                visitor=visitor,
                room=models.PlaceID.objects.get(placeid=serializer.data['placeid']).room,
                inorout=inorout,
            )
            nowroom.save()

            return Response({'nickname':nowroom.visitor.nickname, 'inorout':nowroom.inorout}, status=201)

        return Response({}, status=404)