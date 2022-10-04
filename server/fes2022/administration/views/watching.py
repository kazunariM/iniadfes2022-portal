from rest_framework.generics import ListAPIView, RetrieveAPIView

from django.contrib.auth.mixins import UserPassesTestMixin

from ..serializers.watching import CampusPeopleSerializer, RoomPeopleSerializer
from ..models import PagesPermission
from ...models import NowCampus, Room


class CampusPeopleAPI(UserPassesTestMixin, RetrieveAPIView):
    serializer_class = CampusPeopleSerializer
    
    def get_object(self):
        return NowCampus.objects.all().order_by("pk").last()
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='Watching').users.all()


class RoomPeopleAPI(UserPassesTestMixin, ListAPIView):
    serializer_class = RoomPeopleSerializer
    queryset = Room.objects.all().order_by("campus", "floor", "room_number")
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user in PagesPermission.objects.get(page='Watching').users.all()
