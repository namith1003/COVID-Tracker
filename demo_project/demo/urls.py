from django.contrib import admin
from django.urls import path, include
import models, views

urlpatterns = [
    path('', views.index, name="index"),
]
