from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "ventas"

urlpatterns = [
    path("ventas/", views.ventas, name="ventas"),
]
