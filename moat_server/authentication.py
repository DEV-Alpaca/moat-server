import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

from apps.users.models import User


# https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decoded.get("pk")
            user = User.objects.get(pk=pk)
            return (user, None)
        except (ValueError, User.DoesNotExist):
            return None
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed(detail="(에러) JWT Format Invalid")
