from django.contrib import admin
from . import models

# Register your models here.


class VisitorAdmin(admin.ModelAdmin):
    fieldsets = (
        ("必須", {"fields": ("nickname", "design", )}),
        ("いずれかが必要", {"fields": ("email", "phone", "remark", )}),
        ("アンケート", {"fields": ("address", "age", "gender", "major_subject", "job", "know_about", )}),
        ("ステータス", {"fields": ("is_verified_email", "is_preregistration", "is_printed", "is_handedover",)}),
        ("情報", {"fields": ("pk", "identifying", "userid", "management_uuid", "created_at", "id_data", )}),
    )
    readonly_fields = ("pk", "identifying", "userid", "management_uuid", "created_at", "id_data", )
    list_display = ("pk", "nickname", "is_handedover", "is_preregistration", "is_verified_email","created_at")
    list_filter = ("is_handedover", "is_preregistration",)
    list_display_links = ("pk", "nickname", )
    search_fields = ("nickname",)


class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)
    list_display = ("campus", "groupname",)
    list_filter = ("only_stamp", "have_a_stamp", "campus",)
    list_display_links = ("groupname",)
    search_fields = ("groupname",)

admin.site.register(models.NamecardDesign)
admin.site.register(models.NamecardPool)

admin.site.register(models.Visitor, VisitorAdmin)
admin.site.register(models.Room, RoomAdmin)

admin.site.register(models.PlaceID)
admin.site.register(models.NowCampus)
admin.site.register(models.NowRoom)
admin.site.register(models.Area)
admin.site.register(models.StampCourse)
admin.site.register(models.Story)
admin.site.register(models.Stamp)
admin.site.register(models.StampHistory)
admin.site.register(models.Inset)
