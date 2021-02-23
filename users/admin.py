from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):

    """ User Admin Definition """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "superhost",
                    "avatar",
                    "birthday",
                    "mobile",
                    "gender",
                )
            },
        ),
    )

    list_display = ("username", "mobile", "birthday", "gender", "superhost", "avatar")
