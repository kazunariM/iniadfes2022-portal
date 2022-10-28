from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from ..models import NamecardDesign, PlaceID

# Create your models here.


class PagesPermission(models.Model):
    func = models.CharField(max_length=30, verbose_name='機能名')
    page = models.CharField(max_length=30, verbose_name='ページ名')
    users = models.ManyToManyField(get_user_model(), related_name='pages', blank=True)


class ReadyRoomQR(models.Model):
    ts = models.DateTimeField(default=timezone.now, verbose_name='確認時刻')
    device = models.ManyToManyField(PlaceID, through='ReadyRoomQRdevice')
    ready = models.BooleanField(default=False, verbose_name='準備完了かどうか')


class ReadyRoomQRdevice(models.Model):
    readyroomqr = models.ForeignKey(ReadyRoomQR, on_delete=models.CASCADE)
    placeid = models.ForeignKey(PlaceID, on_delete=models.CASCADE)
    ts = models.DateTimeField(null=True, blank=True, verbose_name='準備完了時刻')
    ready = models.BooleanField(default=False, verbose_name='準備完了かどうか')


class PreregConfig(models.Model):
    exclusion = models.ManyToManyField(NamecardDesign, blank=True)
    num = models.IntegerField(default=100, verbose_name='一度に表示される量')