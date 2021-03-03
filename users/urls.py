from django.urls import path

from .views import MeView, SMSCheckView, UsersView, login, user_detail

app_name = "users"

urlpatterns = [
    path("", UsersView.as_view()),
    path("me/", MeView.as_view()),
    path("<int:pk>/", user_detail),
    path("token/", login),
    path("sms/", SMSCheckView.as_view()),
]
