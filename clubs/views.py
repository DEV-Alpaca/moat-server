from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Club
from .serializers import ReadClubSerializer, WriteClubSerializer


class ClubsView(APIView):
    def get(self, request):
        clubs = Club.objects.all()[:5]
        serializer = ReadClubSerializer(clubs, many=True).data
        return Response(serializer)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteClubSerializer(data=request.data)
        if serializer.is_valid():
            club = serializer.save(user=request.user)
            club_serializer = ReadClubSerializer(club).data
            return Response(data=club_serializer, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClubView(APIView):
    def get_club(self, pk):
        try:
            club = Club.objects.get(pk=pk)
            return club
        except Club.DoesNotExist:
            return None

    def get(self, request, pk):
        club = self.get_club(pk)
        if club is not None:
            serializer = ReadClubSerializer(club).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        club = self.get_club(pk)
        if club is not None:
            if club.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = WriteClubSerializer(club, data=request.data, partial=True)
            print(serializer.is_valid(), serializer.errors)
            if serializer.is_valid():
                serializer.save()
                return Response(ReadClubSerializer(club).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        club = self.get_club(pk)
        if club is not None:
            if club.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            club.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
