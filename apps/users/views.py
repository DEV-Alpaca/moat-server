import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AuthSms, User
from .serializers import UserSerializer


class UsersView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(UserSerializer(new_user).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(UserSerializer(user).data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def login(request):
    phone_number = request.data.get("phone_number")
    password = request.data.get("password")

    if not phone_number or not password:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(phone_number=phone_number, password=password)
    if user is not None:
        encoded_jwt = jwt.encode(
            {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
        )
        return Response(data={"token": encoded_jwt})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class SMSCheckView(APIView):
    def post(self, request):
        try:
            phone_number = request.data["phone_number"]
            print(phone_number)
            AuthSms.objects.update_or_create(phone_number=phone_number)

            return Response({"message": "OK"})

        except KeyError:
            return Response(
                {"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        try:
            phone_number = request.query_params["phone_number"]
            auth_number = request.query_params["auth_number"]
            result = AuthSms.check_auth_number(phone_number, auth_number)

            return Response({"message": "OK", "result": result})

        except KeyError:
            return Response(
                {"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST
            )
