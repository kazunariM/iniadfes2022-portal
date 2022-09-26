from django.db.models.signals import post_save

from .models import ReadyRoomQR
from ..models import PlaceID


def ReadyRoomQRSignal(sender, instance, created, **kwargs):
    if created:
        instance.device.set(PlaceID.objects.all())

post_save.connect(ReadyRoomQRSignal, ReadyRoomQR)
