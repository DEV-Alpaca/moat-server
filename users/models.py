from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    """ User Model Definition """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    name = models.CharField(_("name"), max_length=150, blank=True)
    superhost = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    birthday = models.DateField(blank=True, null=True)
    mobile = models.CharField(verbose_name="휴대폰 번호", primary_key=True, max_length=11)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
