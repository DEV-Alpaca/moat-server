from django.contrib import admin
from django.utils.html import mark_safe

from . import models


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):

    """ Club Admin Definition """

    inlines = (PhotoInline,)

    list_display = (
        "name",
        "d_date",
        "host",
        "applicant_count",
        "photo_count",
        "address",
    )

    ordering = ("d_date",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.ClubType, models.Address)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.clubs.count()
