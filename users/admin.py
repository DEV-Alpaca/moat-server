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
                    "phone_number",
                    "gender",
                )
            },
        ),
    )

    list_display = (
        "username",
        "phone_number",
        "birthday",
        "gender",
        "superhost",
        "avatar",
    )
