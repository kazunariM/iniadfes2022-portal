from django.db import models

from ..models import Visitor

import uuid, os

# Create your models here.


class Term(models.Model):
    non_public = models.BooleanField(verbose_name="公開前")
    pre = models.BooleanField(verbose_name="事前登録期間")
    fes = models.BooleanField(verbose_name="当日")
    finished = models.BooleanField(verbose_name="終了後")
    
    
class Team3(models.Model):
    page = models.CharField(max_length=30, verbose_name="ページ名")
    move_to = models.CharField(null=True, blank=True, max_length=30, verbose_name="非公開時の遷移先")
    is_published = models.BooleanField(default=False, verbose_name="公開設定")


class Clatter_item(models.Model):
    def get_image_path(self, filename):
        result = 'stampbg/{}{}'.format(str(uuid.uuid4().hex), os.path.splitext(filename)[-1])
        return result
    
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True)
    title = models.CharField(max_length=100, verbose_name="アイテム名")
    img = models.ImageField(null=True, blank=True, upload_to=get_image_path, verbose_name="画像")
    text = models.TextField(null=True, blank=True, verbose_name="テキスト")
    is_html = models.BooleanField(default=False, verbose_name="テキストをHTMLとして解釈するかどうか")
    position_x = models.IntegerField(verbose_name="取得後の展示位置(x)")
    position_y = models.IntegerField(verbose_name="取得後の展示位置(y)")
    is_published = models.BooleanField(default=True, verbose_name="公開設定")
    
    
class Got_item(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    items = models.ManyToManyField(Clatter_item, blank=True, related_name="取得したアイテム")
    