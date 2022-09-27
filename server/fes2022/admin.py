from django.contrib import admin
from . import models

# Register your models here.


class VisitorAdmin(admin.ModelAdmin):
    readonly_fields = ("pk", "management_uuid", "userid", "created_at",)
    list_display = ("pk", "last_name", "first_name", "is_handedover", "is_preregistration", "is_verified_email","created_at")
    list_filter = ("is_handedover", "is_preregistration",)
    list_display_links = ("pk", "last_name", )
    search_fields = ("nickname", "last_name", "first_name")


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
