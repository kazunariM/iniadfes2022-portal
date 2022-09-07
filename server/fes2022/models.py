from django.db import models
import uuid, os
from django.utils import timezone
from django.contrib.sessions.models import Session

# Create your models here.


CAMPUS_CHOICES = (
    (0, 'INIAD'),
    (1, 'WELLB'),
)


class NamecardDesign(models.Model):
    def get_image_path(self, filename):
        result = 'stampbg/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
        return result

    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    serial = models.IntegerField(verbose_name="通し番号")
    img = models.ImageField(upload_to=get_image_path, verbose_name="デザイン画像")
    name = models.CharField(max_length=50, verbose_name="ネームカードデザインの名前")
    campus = models.IntegerField(default=0, choices=CAMPUS_CHOICES, verbose_name="INIAD or WELLB")
    numofprints = models.IntegerField(default=500, verbose_name="印刷数")
    numofremaining = models.IntegerField(default=-1, verbose_name="残り")
    is_subject_secret = models.BooleanField(default=False, verbose_name="シークレットか")
    is_only_advance = models.BooleanField(default=False, verbose_name="事前登録限定か")
    text = models.TextField(verbose_name="デザインの説明")

    def __str__(self):
        return f'{"WELLB" if self.campus else "INIAD"} - {self.name}'


class Visitor(models.Model):
    userid = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, verbose_name="QRコードのID")
    management_uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name="管理用uuid")
    date = models.DateField(verbose_name="入場日")
    nickname = models.CharField(max_length=20, verbose_name="ニックネーム")
    first_name = models.CharField(max_length=20, verbose_name="名")
    last_name = models.CharField(max_length=20, verbose_name="姓")
    ruby_first_name = models.CharField(max_length=20, verbose_name="メイ")
    ruby_last_name = models.CharField(max_length=20, verbose_name="セイ")
    email = models.EmailField(max_length=200, verbose_name="E-mail", blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name="電話番号", blank=True, null=True)
    address = models.CharField(max_length=20, verbose_name="住所")
    age = models.IntegerField(default=0, verbose_name="年代")
    gender = models.CharField(max_length=8, verbose_name="性別")
    major_subject = models.CharField(max_length=20, verbose_name="専攻/希望分野")
    job = models.CharField(max_length=20, verbose_name="職業")
    design = models.ForeignKey(NamecardDesign, related_name="visitors_select", on_delete=models.PROTECT, verbose_name="ネームカードのデザイン")
    remark = models.TextField(verbose_name="備考欄", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="初回登録日時")
    is_verified_email = models.BooleanField(default=False, verbose_name="使用可能なメールアドレスかどうか")
    is_preregistration = models.BooleanField(default=False, verbose_name="事前登録かどうか")
    is_printed = models.BooleanField(default=False, verbose_name="印刷完了かどうか")
    is_handedover = models.BooleanField(default=False, verbose_name="お渡し済みかどうか")
    session = models.ForeignKey(Session, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.number} - {self.nickname}'


class Room(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    groupname = models.CharField(max_length=100, verbose_name="団体名")
    campus = models.IntegerField(default=0, choices=CAMPUS_CHOICES, verbose_name="INIAD or WELLB")
    floor = models.IntegerField(default=1, verbose_name="階")
    room_number = models.IntegerField(verbose_name="教室名かドア番号の小さいほう")
    only_stamp = models.BooleanField(default=False, verbose_name="スタンプラリー専用かどうか(優先度高:こちらがTrueの場合強制的にスタンプラリー専用になります)")
    have_a_stamp = models.BooleanField(default=False, verbose_name="スタンプラリー対象団体かどうか")
    pop = models.ImageField(upload_to='ipad_pop/', verbose_name="QRコード読み取りiPadに表示する画像")

    def __str__(self):
        return f'{"WELLB" if self.campus else "INIAD"} - {self.groupname}'
        

class PlaceID(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    placeid = models.CharField(max_length=20, db_index=True, verbose_name="場所ID")
    placenum = models.IntegerField(verbose_name="場所番号")
    door_number = models.IntegerField(verbose_name="教室番号かドア番号")
    room = models.ForeignKey(Room, related_name="PlaceIDs", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.door_number} - {self.placeid}'


class NowCampus(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT, related_name="nowcampus", verbose_name="VisitorのユーザID(id)との紐づけ")
    scanned_at = models.DateTimeField(default=timezone.now, verbose_name="日時")
    inorout = models.BooleanField(default=True, verbose_name="入構or退構")

    def __str__(self):
        return f'{"入構" if self.inorout else "退構"} - {self.scanned_at}'
        

class NowRoom(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT, related_name="nowroom", verbose_name="VisitorのユーザID(id)との紐づけ")
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name="nowroom", verbose_name="Roomの教室ID(id)との紐づけ")
    scanned_at = models.DateTimeField(default=timezone.now, verbose_name="日時")
    inorout = models.BooleanField(default=True, verbose_name="入室or退室")

    def __str__(self):
        return f'{self.scanned_at} - {"入室" if self.inorout else "退室"} - {self.room.groupname}'


class StampCourse(models.Model):
    def get_image_path(self, filename):
        result = 'stampbg/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
        return result

    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    title = models.CharField(max_length=50, verbose_name="スタンプラリーコースの名称")
    main_color = models.CharField(max_length=6, verbose_name="サイトデザインの色(メイン)")
    sub_color = models.CharField(max_length=6, verbose_name="サイトデザインの色(サブ)")
    activation = models.BooleanField(default=False, verbose_name="スタンプラリーを有効化するかどうか") 
    finished = models.BooleanField(default=False, verbose_name="終了後スタンプラリーを見れるかどうか")
    background = models.ImageField(upload_to=get_image_path, verbose_name="スタンプラリーの背景画像")

    def __str__(self):
        return f'{self.title}'


class Stamp(models.Model):
    def get_image_path(self, filename):
        result = 'stamp/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
        return result

    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    stampcourse = models.ForeignKey(StampCourse, related_name="stamps", on_delete=models.CASCADE)
    room = models.OneToOneField(Room, related_name="stamp", on_delete=models.CASCADE)
    img = models.ImageField(upload_to=get_image_path, verbose_name="スタンプの素材画像")
    serial = models.IntegerField(verbose_name="表示順序")   
    position_y = models.IntegerField(default=0, verbose_name="素材の上側のポジション(px)")
    position_x = models.IntegerField(default=0, verbose_name="素材の左側のポジション(px)")
    story = models.TextField(blank=True, null=True, verbose_name="ストーリー用")
    
    def __str__(self):
        return f'{self.stampcourse.title} - {self.room.groupname}'


class StampHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    visitor = models.ForeignKey(Visitor, related_name="stamp_history", on_delete=models.PROTECT)
    stampcourse = models.ForeignKey(StampCourse, related_name="history", on_delete=models.PROTECT)
    got =  models.ManyToManyField(Stamp, related_name="history", blank=True)

    def __str__(self):
        return f'{self.visitor.nickname} - {self.stampcourse.title}'


class Inset(models.Model):
    def get_image_path(self, filename):
        result = 'images/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
        return result

    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    img = models.ImageField(upload_to=get_image_path, verbose_name="画像アップロード用")
    alt = models.TextField(verbose_name="画像の説明(alt属性)")

