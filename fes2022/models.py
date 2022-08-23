from django.db import models
import uuid
from django.utils import timezone

# Create your models here.


class Visitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    userid = models.UUIDField(default=uuid.uuid4, verbose_name="QRコードのID")
    nickname = models.CharField(max_length=20, verbose_name="ニックネーム")
    first_name = models.CharField(max_length=20, verbose_name="名")
    last_name = models.CharField(max_length=20, verbose_name="姓")
    ruby_first_name = models.CharField(max_length=20, verbose_name="メイ")
    ruby_last_name = models.CharField(max_length=20, verbose_name="セイ")
    email = models.EmailField(max_length=100, verbose_name="E-mail", blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name="電話番号", blank=True, null=True)
    address = models.CharField(max_length=30, verbose_name="都道府県市区町村")
    age = models.IntegerField(default=0, verbose_name="年代")
    job = models.CharField(max_length=20, verbose_name="職業")
    design = models.IntegerField(default=0, verbose_name="ネームカードのデザイン")
    remark = models.TextField(verbose_name="備考欄", blank=True, null=True)
    number = models.IntegerField(verbose_name="ネームカードにプリントされるID")

class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    roomid = models.CharField(max_length=20, verbose_name="教室ID")
    groupname = models.CharField(max_length=100, verbose_name="団体名")
    campus = models.IntegerField(default=0, verbose_name="INIAD or WELLB")
    floor = models.IntegerField(default=1, verbose_name="階")

class NowCampus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT, verbose_name="VisitorのユーザID(id)との紐づけ")
    scanned_at = models.DateTimeField(default=timezone.now, verbose_name="日時")
    inorout = models.BooleanField(default=True, verbose_name="入構or退構")

class NowRoom(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT, verbose_name="VisitorのユーザID(id)との紐づけ")
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name="Roomの教室ID(id)との紐づけ")
    scanned_at = models.DateTimeField(default=timezone.now, verbose_name="日時")
    inorout = models.BooleanField(default=True, verbose_name="入室or退室")