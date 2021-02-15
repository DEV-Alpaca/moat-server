from django.db import models

from core.models import CoreModel


class Club(CoreModel):

    """ Club Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    d_date = models.CharField(max_length=20)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="clubs"
    )
    club_type = models.ForeignKey(
        "ClubType", on_delete=models.SET_NULL, null=True, related_name="clubs"
    )
    address = models.ForeignKey(
        "Address", on_delete=models.SET_NULL, null=True, related_name="clubs"
    )

    def __str__(self):
        return self.name

    def photo_number(self):
        return self.photos.count()

    photo_number.short_description = "Photo Count"

    def fav_count(self):
        return self.favs.count()

    fav_count.short_description = "Number of users who like this Club"

    class Meta:
        ordering = ["-pk"]


class Photo(CoreModel):

    """ Photo Model Definition """

    file = models.ImageField()
    club = models.ForeignKey("Club", related_name="photos", on_delete=models.CASCADE)
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.club.name


class AbstractItem(CoreModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ClubType(AbstractItem):

    """ ClubType Model Definition """

    class Meta:
        verbose_name = "Club Type"
        ordering = ["name"]


class Address(CoreModel):

    """ Address Model Definition """

    address = models.CharField(max_length=80)
    area = models.ForeignKey(
        "Area", on_delete=models.SET_NULL, null=True, related_name="locations"
    )
    town = models.ForeignKey(
        "Town", on_delete=models.SET_NULL, null=True, related_name="locations"
    )

    class Meta:
        verbose_name = "Address"
        ordering = ["town"]


class Town(AbstractItem):

    """ Town Model Definition """

    class Meta:
        verbose_name = "Town"
        ordering = ["name"]


class Area(AbstractItem):

    """ Area Model Definition """

    class Meta:
        verbose_name = "Area"
        ordering = ["name"]
