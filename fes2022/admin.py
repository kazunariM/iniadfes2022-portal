from django.contrib import admin
from . import models

# Register your models here.


class VisitorAdmin(admin.ModelAdmin):
    readonly_fields = ('id', "userid", "created_at", "session")
    list_display = ("number", "last_name", "first_name", "is_handedover", "created_at")
    list_filter = ("is_handedover", )
    list_display_links = ('number', "last_name", )
    search_fields = ("nickname", "last_name", "first_name")


class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ("roomid", "campus", "groupname",)
    list_filter = ("only_stamp", "have_a_stamp", "campus",)
    list_display_links = ('roomid', "groupname",)
    search_fields = ("roomid", "groupname",)


admin.site.register(models.Visitor, VisitorAdmin)
admin.site.register(models.Room, RoomAdmin)