from rest_framework import serializers

from users.serializers import RelatedUserSerializer

from .models import Club


class ClubSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()

    class Meta:
        model = Club
        exclude = ("modified",)
        read_only_fields = (
            "id",
            "host",
            "created",
            "updated",
        )

    # Field-level validation
    def validate_applicant(self, applicant_count):
        if applicant_count > 4:
            raise serializers.ValidationError("모집인원은 최대 4명입니다.")
        else:
            return applicant_count
