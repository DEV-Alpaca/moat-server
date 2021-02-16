from django.contrib import admin

from . import models


@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "photo_number",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
