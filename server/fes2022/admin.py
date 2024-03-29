from django.contrib import admin
from . import models

# Register your models here.


class NamecardDesignAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'numofremaining', )
    list_display = ('serial', 'name', 'numofprints', 'numofremaining')
    list_display_links = ('serial', 'name',)
    ordering = ('serial', )


class NamecardPool(admin.ModelAdmin):
    list_display = ('pk', 'namecard', 'used')
    list_display_links = ('pk', 'namecard',)
    ordering = ('-pk', )


class VisitorAdmin(admin.ModelAdmin):
    fieldsets = (
        ("必須", {"fields": ("nickname", "design", )}),
        ("いずれかが必要", {"fields": ("email", "phone", "remark", )}),
        ("アンケート", {"fields": ("address", "age", "gender", "major_subject", "job", "know_about", )}),
        ("ステータス", {"fields": ("is_verified_email", "is_preregistration", "is_printed", "is_handedover",)}),
        ("情報", {"fields": ("pk", "identifying", "userid", "management_uuid", "created_at", "id_data", )}),
    )
    readonly_fields = ("pk", "identifying", "userid", "management_uuid", "created_at", "id_data", )
    list_display = ("pk", "nickname", "is_printed", "is_preregistration", "is_verified_email", "design", "identifying", "userid", "is_handedover", "created_at")
    list_filter = ("is_handedover", "is_preregistration",)
    list_display_links = ("pk", "nickname", )
    search_fields = ("nickname",)


class CampusAdmin(admin.ModelAdmin):
    list_display = ("day", "count", "unique_count", "total_count")


class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)
    list_display = ("campus", "groupname", "count", "unique_count", "total_count", "only_stamp")
    list_filter = ("only_stamp", "have_a_stamp", "campus",)
    list_display_links = ("groupname",)
    search_fields = ("groupname",)
    ordering = ("campus", "floor", "room_number")


class PlaceIDAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)
    list_display = ("room_campus", "placeid", "door_number", "placenum")
    ordering = ("placeid",)
    
    def room_campus(self, obj):
        return obj.room.campus
    
    room_campus.admin_order_field = "room__campus"


class NowCampusAdmin(admin.ModelAdmin):
    list_display = ("pk", "visitor", "inorout", "scanned_at")
    readonly_fields = ("pk", "scanned_at")
    ordering = ("-pk", )


class NowRoomAdmin(admin.ModelAdmin):
    list_display = ("pk", "visitor", "inorout", "room", "scanned_at")
    list_filter = ("room",)
    readonly_fields = ("pk", "scanned_at")
    ordering = ("-pk", )

    
class AreaAdmin(admin.ModelAdmin):
    pass


class StampCourseAdmin(admin.ModelAdmin):
    pass


class StoryAdmin(admin.ModelAdmin):
    pass


class StampAdmin(admin.ModelAdmin):
    pass


class StampHistoryAdmin(admin.ModelAdmin):
    pass


class InsetAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.NamecardDesign, NamecardDesignAdmin)
admin.site.register(models.NamecardPool, NamecardPool)
admin.site.register(models.Visitor, VisitorAdmin)
admin.site.register(models.Campus, CampusAdmin)
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.PlaceID, PlaceIDAdmin)
admin.site.register(models.NowCampus, NowCampusAdmin)
admin.site.register(models.NowRoom, NowRoomAdmin)
admin.site.register(models.Area, AreaAdmin)
admin.site.register(models.StampCourse, StampCourseAdmin)
admin.site.register(models.Story, StoryAdmin)
admin.site.register(models.Stamp, StampAdmin)
admin.site.register(models.StampHistory, StampHistoryAdmin)
admin.site.register(models.Inset, InsetAdmin)
