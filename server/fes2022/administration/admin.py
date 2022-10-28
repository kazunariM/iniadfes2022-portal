from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.PagesPermission)
admin.site.register(models.ReadyRoomQR)
admin.site.register(models.ReadyRoomQRdevice)
admin.site.register(models.PreregConfig)
