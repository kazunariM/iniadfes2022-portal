from django.db import models

# Create your models here.


class Schedule(models.Model):
    event = models.CharField(max_length=10, verbose_name="何の日か")
    key = models.CharField(max_length=5, verbose_name="アルファベット")
    date = models.DateField(verbose_name="期限など")
