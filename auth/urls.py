from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("token", views.generate_token, name="index"),
    path("token/authenticate", views.is_authenticated, name="index"),
]