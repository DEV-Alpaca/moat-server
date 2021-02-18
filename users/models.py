from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    """ User Model Definition """

    avatar = models.ImageField(upload_to="avatars", blank=True)
    name = models.CharField(_("name"), max_length=150, blank=True)
    superhost = models.BooleanField(default=False)
    favs = models.ManyToManyField("clubs.Club", related_name="fav_users")
    applicant = models.ManyToManyField("clubs.Club", related_name="applicants")
    mobile = models.CharField(verbose_name="휴대폰 번호", primary_key=True, max_length=11)
