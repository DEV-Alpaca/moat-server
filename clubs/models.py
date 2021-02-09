from django.db import models

from core.models import CoreModel


class Club(CoreModel):

    """ Club Model Definition """

    CLUB_SMALL_GROUP = "SG"
    CLUB_TALENT_SHARE = "TS"

    CLUB_TYPE_CHOICES = ((CLUB_SMALL_GROUP, "소모임"), (CLUB_TALENT_SHARE, "재능공유"))

    name = models.CharField(max_length=140)
    description = models.TextField()
    address = models.CharField(max_length=140)
    club_type = models.CharField(choices=CLUB_TYPE_CHOICES, max_length=2)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )

    def __str__(self):
        return self.name

    def photo_number(self):
        return self.photos.count()

    photo_number.short_description = "Photo Count"

    class Meta:
        ordering = ["-pk"]


class Photo(CoreModel):

    """ Photo Model Definition """

    file = models.ImageField()
    club = models.ForeignKey("Club", related_name="photos", on_delete=models.CASCADE)
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.club.name
