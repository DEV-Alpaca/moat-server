from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Club
from .serializers import ClubSerializer


class OwnPagination(PageNumberPagination):
    page_size = 5


class ClubsView(APIView):
    def get(self, request):
        paginator = OwnPagination()
        clubs = Club.objects.all()
        results = paginator.paginate_queryset(clubs, request)
        # context 를 통해서 원하는 것(request 뿐만아니라 다른것도)을 serializer로 전달 할 수 있다.
        serializer = ClubSerializer(results, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            club = serializer.save(host=request.user)
            club_serializer = ClubSerializer(club).data
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
            serializer = ClubSerializer(club).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        club = self.get_club(pk)
        if club is not None:
            if club.host != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = ClubSerializer(club, data=request.data, partial=True)
            print(serializer.is_valid(), serializer.errors)
            if serializer.is_valid():
                serializer.save()
                return Response(ClubSerializer(club).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        club = self.get_club(pk)
        if club is not None:
            if club.host != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            club.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
