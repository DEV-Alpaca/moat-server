from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ User Model Definition """

    avatar = models.ImageField(upload_to="avatars", blank=True)
    superhost = models.BooleanField(default=False)
    favs = models.ManyToManyField("clubs.Club", related_name="favs")
