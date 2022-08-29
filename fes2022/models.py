from django.db import models
import uuid
from django.utils import timezone
from django.contrib.sessions.models import Session

# Create your models here.


class Visitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    userid = models.UUIDField(default=uuid.uuid4, db_index=True, verbose_name="QRコードのID")
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
    created_at = models.DateTimeField(default=timezone.now, verbose_name="初回登録日時")
    is_preregistration = models.BooleanField(default=False, verbose_name="事前登録かどうか")
    is_handedover = models.BooleanField(default=False, verbose_name="お渡し済みかどうか")
    session = models.ForeignKey(Session, blank=True, null=True, on_delete=models.SET_NULL)


class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    roomid = models.CharField(max_length=20, db_index=True, verbose_name="教室ID")
    groupname = models.CharField(max_length=100, verbose_name="団体名")
    campus = models.IntegerField(default=0, verbose_name="INIAD or WELLB")
    floor = models.IntegerField(default=1, verbose_name="階")
    only_stamp = models.BooleanField(default=False, verbose_name="スタンプラリー専用かどうか(優先度高:こちらがTrueの場合強制的にスタンプラリー専用になります)")
    have_a_stamp = models.BooleanField(default=False, verbose_name="スタンプラリー対象団体かどうか")


class NowCampus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT, verbose_name="VisitorのユーザID(id)との紐づけ")
    scanned_at = models.DateTimeField(default=timezone.now, verbose_name="日時")
    inorout = models.BooleanField(default=True, verbose_name="入構or退構")


class NowRoom(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT, verbose_name="VisitorのユーザID(id)との紐づけ")
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name="Roomの教室ID(id)との紐づけ")
    scanned_at = models.DateTimeField(default=timezone.now, verbose_name="日時")
    inorout = models.BooleanField(default=True, verbose_name="入室or退室")


class StampCourse(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    title = models.CharField(max_length=50, verbose_name="スタンプラリーコースの名称")
    main_color = models.CharField(max_length=6, verbose_name="サイトデザインの色(メイン)")
    sub_color = models.CharField(max_length=6, verbose_name="サイトデザインの色(サブ)")
    activation = models.BooleanField(default=False, verbose_name="スタンプラリーを有効化するかどうか") 
    finished = models.BooleanField(default=False, verbose_name="終了後スタンプラリーを見れるかどうか")
    background = models.ImageField(upload_to='stampbg/', verbose_name="スタンプラリーの背景画像")


class Stamp(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    course = models.ForeignKey(StampCourse, related_name="stamps", on_delete=models.PROTECT)
    img = models.ImageField(upload_to='stamp/', verbose_name="スタンプの素材画像")
    serial = models.IntegerField(verbose_name="表示順序")
    position_y = models.IntegerField(default=0, verbose_name="素材の上側のポジション(px)")
    position_x = models.IntegerField(default=0, verbose_name="素材の左側のポジション(px)")
    story = models.TextField(blank=True, null=True, verbose_name="ストーリー用")
    

class StampHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    stampcourse = models.ForeignKey(StampCourse, related_name="history", on_delete=models.PROTECT)
    got =  models.ManyToManyField(Stamp, related_name="history", blank=True)


class Inset(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    img = models.ImageField(upload_to='images/', verbose_name="画像アップロード用")
