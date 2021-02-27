from django.urls import path

from . import views

app_name = "clubs"

urlpatterns = [
    path("", views.ClubsView.as_view()),
    path("<int:pk>/", views.ClubView.as_view()),
]
