from rest_framework import serializers

from users.serializers import RelatedUserSerializer

from .models import Club


class ReadClubSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()

    class Meta:
        model = Club
        exclude = ("modified",)


class WriteClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        exclude = (
            "user",
            "modified",
            "created",
        )

    # Field-level validation
    def validate_beds(self, beds):
        if beds < 5:
            raise serializers.ValidationError("Your house is too small")
        else:
            return beds

    # Object-level validation
    def validate(self, data):
        # update 할 때(instance 가 있을 때)
        print("data: ", data)
        if self.instance:
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        # create 할 때만(instance 가 없을 때)
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out")
        if check_in == check_out:
            raise serializers.ValidationError("Not enough time between changes")
        return data
